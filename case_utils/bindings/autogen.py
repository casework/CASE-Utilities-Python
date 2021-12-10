#!/usr/bin/env python3

# This software was developed at the National Institute of Standards
# and Technology by employees of the Federal Government in the course
# of their official duties. Pursuant to title 17 Section 105 of the
# United States Code this software is not subject to copyright
# protection and is in the public domain. NIST assumes no
# responsibility whatsoever for its use by other parties, and makes
# no guarantees, expressed or implied, about its quality,
# reliability, or any other characteristic.
#
# We would appreciate acknowledgement if the software is used.

__version__ = "0.0.1"

import argparse
import importlib
import typing

import rdflib.plugins.sparql

import case_utils.ontology
from case_utils.ontology.version_info import *


def class_basename(class_iri: str) -> str:
    if "caseontology.org" in class_iri:
        class_iri_basename = class_iri.split("/")[-1]
    elif "unifiedcyberontology.org" in class_iri:
        class_iri_basename = class_iri.split("#")[-1]
    else:
        raise NotImplementedError("Unrecognized IRI form: %r." % class_iri)
    return class_iri_basename


class CASEPropertyConstructor(object):
    def __init__(self, property_iri: str, min_count: int = 0, max_count: typing.Optional[int] = None, *args, **kwargs) -> None:
        self.property_iri: str = property_iri
        self.min_count: int = min_count
        self.max_count: typing.Optional[int] = max_count

class CASEClassConsructor(object):
    def __init__(self, class_iri: str, *args, **kwargs) -> None:
        self.class_iri: str = class_iri
        self.case_class_name: str = "case_" + class_basename(class_iri)
        self.parent_case_class_names: typing.Set[str] = set()
        self.required_properties: typing.Dict[str, CASEPropertyConstructor] = dict()

    def __str__(self) -> str:
        python_parent_class_names: typing.Set[str] = set()
        if len(self.parent_case_class_names) == 0:
            python_parent_class_names.add("NodeConstructor")
        else:
            python_parent_class_names |= self.parent_case_class_names
        parts: typing.List[str] = []
        parts.append(
            "class %s(%s):"
            % (self.case_class_name, ", ".join(sorted(python_parent_class_names)))
        )
        parts.append('    """')
        parts.append("    Based on class with IRI %r." % self.class_iri)
        parts.append('    """')
        parts.append("    def __init__(self, *args, **kwargs) -> None:")
        parts.append("        super().__init__(*args, **kwargs)")
        return "\n".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    graph = rdflib.Graph()
    ttl_filename = "case-%s.ttl" % CURRENT_CASE_VERSION
    ttl_data = importlib.resources.read_text(case_utils.ontology, ttl_filename)

    graph.parse(data=ttl_data)

    print(
        """\
#!/usr/bin/env python3

# This software was developed at the National Institute of Standards
# and Technology by employees of the Federal Government in the course
# of their official duties. Pursuant to title 17 Section 105 of the
# United States Code this software is not subject to copyright
# protection and is in the public domain. NIST assumes no
# responsibility whatsoever for its use by other parties, and makes
# no guarantees, expressed or implied, about its quality,
# reliability, or any other characteristic.
#
# We would appreciate acknowledgement if the software is used.

###########################################################
#
#
# AUTOMATICALLY GENERATED FILE.  MANUAL EDITS WILL BE LOST.
#
#
###########################################################

from __future__ import annotations

import typing

import rdflib

class NodeConstructor(object):
    def __init__(self, node_iri: typing.Optional[str] = None, *args, **kwargs) -> None:
        super().__init__()
        self._node: typing.Union[None, rdflib.BNode, rdflib.URIRef] = None
        self._node_iri = node_iri
        self._type_iris: typing.Set[str] = set()

    @property
    def node(self) -> typing.Union[rdflib.BNode, rdflib.URIRef]:
        '''
        Set on first access.
        '''
        if self._node is None:
            if self.node_iri is None:
                self._node = rdflib.BNode()
            else:
                self._node = rdflib.URIRef(self.node_iri)
        return self._node

    @property
    def node_iri(self) -> typing.Optional[str]:
        return self._node_iri

    @node_iri.setter
    def node_iri(self, value: typing.Optional[str]) -> None:
        assert value is None or isinstance(value, str)
        self._node_iri = value

    @property
    def type_iris(self) -> typing.Set[str]:
        return self._type_iris

    def add_to_graph(self, graph: rdflib.Graph) -> None:
        for type_iri in sorted(self.type_iris):
            graph.add((
                self.node_iri,
                rdflib.RDF.type,
                rdflib.URIRef(type_iri)
            ))
"""
    )

    class_iris: typing.Set[str] = set()
    query_str = """\
SELECT ?nClass
WHERE {
  ?nClass a sh:NodeShape .
  ?nClass a owl:Class .
  ?nClass sh:targetClass ?nClass .
}
"""
    for result in graph.query(query_str):
        class_iris.add(result[0].toPython())

    class_iri_basename_to_case_class_constructor: typing.Dict[
        str, CASEClassConsructor
    ] = dict()
    class_iri_basename: str
    for class_iri in class_iris:
        class_iri_basename = class_basename(class_iri)
        if class_iri_basename in class_iri_basename_to_case_class_constructor:
            raise ValueError("Duplicate class basename: %r." % class_iri_basename)
        class_iri_basename_to_case_class_constructor[
            class_iri_basename
        ] = CASEClassConsructor(class_iri)

    # Record direct parents.
    query_str = """\
SELECT ?nClass ?nParentClass
WHERE {
  ?nClass a sh:NodeShape .
  ?nClass a owl:Class .
  ?nClass sh:targetClass ?nClass .
  ?nClass rdfs:subClassOf ?nParentClass .
}
"""
    for parent_result in graph.query(query_str):
        class_iri_basename = class_basename(parent_result[0].toPython())
        parent_class_iri_basename = class_basename(parent_result[1].toPython())
        class_iri_basename_to_case_class_constructor[
            class_iri_basename
        ].parent_case_class_names.add("case_" + parent_class_iri_basename)

    # Record properties.

    for class_iri_basename in sorted(
        class_iri_basename_to_case_class_constructor.keys()
    ):
        print("\n")
        print(class_iri_basename_to_case_class_constructor[class_iri_basename])


if __name__ == "__main__":
    main()

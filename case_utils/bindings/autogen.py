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

import importlib
import logging
import os
import typing

import networkx  # type: ignore
import rdflib.plugins.sparql

import case_utils.ontology
from case_utils.ontology.version_info import CURRENT_CASE_VERSION

_logger = logging.getLogger(os.path.basename(__file__))

NS_CO = rdflib.Namespace("http://purl.org/co/")
NS_OWL = rdflib.OWL
NS_RDF = rdflib.RDF


def class_iri_to_constructor_class_name(graph: rdflib.Graph, class_iri: str) -> str:
    (
        class_iri_prefix,
        class_iri_namespace,
        class_iri_basename,
    ) = graph.namespace_manager.compute_qname(class_iri, False)

    class_iri_namespace_str = str(class_iri_namespace)
    if class_iri_namespace_str.startswith("http://purl.org/co/"):
        constructor_class_prefix = "CO_"
    elif class_iri_namespace_str.startswith("https://ontology.caseontology.org/"):
        constructor_class_prefix = "CASE_"
    elif class_iri_namespace_str.startswith(
        "https://ontology.unifiedcyberontology.org/"
    ):
        constructor_class_prefix = "UCO_"
    elif class_iri_namespace_str.startswith(str(NS_OWL)):
        constructor_class_prefix = "OWL_"
    else:
        raise NotImplementedError("Unrecognized IRI start: %r." % class_iri)

    return constructor_class_prefix + class_iri_basename


class CASEPropertyConstructor(object):
    def __init__(
        self,
        property_iri: str,
        min_count: int = 0,
        max_count: typing.Optional[int] = None,
        *args: typing.Any,
        **kwargs: typing.Any
    ) -> None:
        self.property_iri: str = property_iri
        self.min_count: int = min_count
        self.max_count: typing.Optional[int] = max_count


class CASEClassConstructor(object):
    def __init__(
        self,
        graph: rdflib.Graph,
        class_iri: str,
        *args: typing.Any,
        documentation_comment: typing.Optional[str] = None,
        **kwargs: typing.Any
    ) -> None:
        self.class_iri: str = class_iri
        self.case_class_name: str = class_iri_to_constructor_class_name(
            graph, class_iri
        )
        self.documentation_comment: typing.Optional[str] = documentation_comment
        self.parent_constructor_class_names: typing.Set[str] = set()
        self.required_properties: typing.Dict[str, CASEPropertyConstructor] = dict()

    def __str__(self) -> str:
        parts: typing.List[str] = []

        parts.append(
            "class %s(%s):"
            % (
                self.case_class_name,
                ", ".join(sorted(self.parent_constructor_class_names)),
            )
        )

        # Build class documentation string.
        parts.append('    """')

        if self.documentation_comment is not None:
            documentation_comment_lines = self.documentation_comment.split("\n")
            for documentation_comment_line in documentation_comment_lines:
                parts.append(("    " + documentation_comment_line).rstrip())
            parts.append("")
        parts.append("    Based on class with IRI %r." % self.class_iri)
        parts.append('    """')

        # Build initializer.
        parts.append(
            "    def __init__(self, graph: rdflib.Graph, node_iri: str, *args: typing.Any, type_iris: typing.Set[str] = set(), **kwargs: typing.Any) -> None:"
        )
        # Add types in initializer.
        if "'" in self.class_iri:
            raise ValueError('Unexpected "\'" character in IRI: %r.' % self.class_iri)
        parts.append("        if len(type_iris) == 0:")
        parts.append("            _type_iris = {'%s'}" % self.class_iri)
        parts.append("        else:")
        parts.append("            _type_iris = type_iris")
        parts.append(
            "        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)"
        )

        # Add special-case initialization.
        if self.case_class_name == "UCO_UcoObject":
            parts.append("        self._facets: typing.List[UCO_Facet] = []")
        elif self.case_class_name == "UCO_ContentDataFacet":
            parts.append("        self._hashes: typing.List[UCO_Hash] = []")

        # Build special-case methods.
        if self.case_class_name == "UCO_UcoObject":
            parts.append("    def add_facet(self, facet: UCO_Facet) -> None:")
            parts.append("        self.facets.append(facet)")
            parts.append(
                "        self.graph.add((self.node, NS_UCO_CORE.hasFacet, facet.node))"
            )
            parts.append("    @property")
            parts.append("    def facets(self) -> typing.List[UCO_Facet]:")
            parts.append("        return self._facets")
        elif self.case_class_name == "UCO_ContentDataFacet":
            parts.append("    def add_hash(self, hash: UCO_Hash) -> None:")
            parts.append("        self.hashes.append(hash)")
            parts.append(
                "        self.graph.add((self.node, NS_UCO_OBSERVABLE.hash, hash.node))"
            )
            parts.append("    @property")
            parts.append("    def hashes(self) -> typing.List[UCO_Hash]:")
            parts.append("        return self._hashes")

        return "\n".join(parts)


def main() -> None:
    graph = rdflib.Graph()
    ttl_filename = "case-%s.ttl" % CURRENT_CASE_VERSION
    ttl_data = importlib.resources.read_text(case_utils.ontology, ttl_filename)

    graph.parse(data=ttl_data)

    # TODO These supplemental triples should be added into UCO's CO ontology file.
    graph.add((NS_CO.Bag, NS_RDF.type, NS_OWL.Class))
    graph.add((NS_CO.Item, NS_RDF.type, NS_OWL.Class))

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

NS_RDF = rdflib.RDF
NS_UCO_CORE = rdflib.Namespace("https://ontology.unifiedcyberontology.org/uco/core/")
NS_UCO_OBSERVABLE = rdflib.Namespace("https://ontology.unifiedcyberontology.org/uco/observable/")

class NodeConstructor(object):
    def __init__(self, graph: rdflib.Graph, node_iri: str, *args: typing.Any, type_iris: typing.Set[str] = set(), **kwargs: typing.Any) -> None:
        super().__init__()
        self._graph: rdflib.Graph = graph
        self._node: typing.Optional[rdflib.URIRef] = None
        self._node_iri = node_iri
        self._type_iris: typing.Set[str] = type_iris
        for type_iri in sorted(self.type_iris):
            self.graph.add((self.node, NS_RDF.type, rdflib.URIRef(type_iri)))

    def add_type_iri(self, type_iri: str) -> None:
        '''
        Add additional RDF type to graph node.
        '''
        self.type_iris.add(type_iri)
        self.graph.add((self.node, NS_RDF.type, rdflib.URIRef(type_iri)))

    @property
    def graph(self) -> rdflib.Graph:
        return self._graph

    @property
    def node(self) -> rdflib.URIRef:
        '''
        Set on first access.
        '''
        if self._node is None:
            self._node = rdflib.URIRef(self.node_iri)
        return self._node

    @property
    def node_iri(self) -> str:
        return self._node_iri

    @node_iri.setter
    def node_iri(self, value: str) -> None:
        assert isinstance(value, str)
        self._node_iri = value

    @property
    def type_iris(self) -> typing.Set[str]:
        return self._type_iris

    def add_to_graph(self, graph: rdflib.Graph) -> None:
        for type_iri in sorted(self.type_iris):
            graph.add((
                self.node,
                rdflib.RDF.type,
                rdflib.URIRef(type_iri)
            ))
"""
    )

    class_iris: typing.Set[str] = set()
    class_iri_to_documentation_comment: typing.Dict[str, typing.Optional[str]] = dict()
    class_query_str = """\
SELECT ?nClass ?nComment
WHERE {
  ?nClass a owl:Class .

  OPTIONAL { ?nClass rdfs:comment ?nComment . }

  FILTER isIRI(?nClass)
}
"""
    for class_result in graph.query(class_query_str):
        assert isinstance(class_result, rdflib.query.ResultRow)
        assert isinstance(class_result[0], rdflib.URIRef)
        class_iris.add(class_result[0].toPython())
        if isinstance(class_result[1], rdflib.Literal):
            class_iri_to_documentation_comment[
                class_result[0].toPython()
            ] = class_result[1].toPython()

    constructor_class_name_to_case_class_constructor: typing.Dict[
        str, CASEClassConstructor
    ] = dict()
    for class_iri in class_iris:
        constructor_class_name = class_iri_to_constructor_class_name(graph, class_iri)
        if constructor_class_name in constructor_class_name_to_case_class_constructor:
            _logger.debug("class_iri = %r.", class_iri)
            raise ValueError("Duplicate class name: %r." % constructor_class_name)
        constructor_class_name_to_case_class_constructor[
            constructor_class_name
        ] = CASEClassConstructor(
            graph,
            class_iri,
            documentation_comment=class_iri_to_documentation_comment.get(class_iri),
        )

    # Link generated class names.
    constructor_class_dependencies = networkx.DiGraph()

    # Record direct parents, excluding anonymous classes and owl:Restrictions.
    query_str = """\
SELECT ?nClass ?nParentClass
WHERE {
  ?nClass a owl:Class .
  OPTIONAL {
    ?nClass rdfs:subClassOf ?nParentClass .
  }
  FILTER isIRI(?nClass)
  FILTER isIRI(?nParentClass)
}
"""
    for parent_result in graph.query(query_str):
        assert isinstance(parent_result, rdflib.query.ResultRow)
        assert isinstance(parent_result[0], rdflib.URIRef)
        assert isinstance(parent_result[1], rdflib.URIRef)
        constructor_class_name = class_iri_to_constructor_class_name(
            graph, parent_result[0].toPython()
        )

        n_parent_class = parent_result[1]
        if n_parent_class is None or n_parent_class == NS_OWL.Thing:
            parent_constructor_class_name = "NodeConstructor"
        else:
            parent_class_iri: str = parent_result[1].toPython()
            parent_constructor_class_name = class_iri_to_constructor_class_name(
                graph, parent_class_iri
            )

        constructor_class_name_to_case_class_constructor[
            constructor_class_name
        ].parent_constructor_class_names.add(parent_constructor_class_name)
        constructor_class_dependencies.add_edge(
            constructor_class_name, parent_constructor_class_name
        )

    # TODO Record properties.

    # Serialize classes in topological order of subclass hierarchy.
    # Near-one-liner for topological sort c/o: https://stackoverflow.com/a/56476639
    for constructor_class_name in reversed(
        list(networkx.topological_sort(constructor_class_dependencies))
    ):
        if constructor_class_name == "NodeConstructor":
            # Skip the one hand-written class.
            continue
        print("\n")
        print(constructor_class_name_to_case_class_constructor[constructor_class_name])


if __name__ == "__main__":
    main()

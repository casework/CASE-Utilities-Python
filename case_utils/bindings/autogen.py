#!/usr/bin/env python3

# Portions of this file contributed by NIST are governed by the
# following statement:
#
# This software was developed at the National Institute of Standards
# and Technology by employees of the Federal Government in the course
# of their official duties. Pursuant to Title 17 Section 105 of the
# United States Code, this software is not subject to copyright
# protection within the United States. NIST assumes no responsibility
# whatsoever for its use by other parties, and makes no guarantees,
# expressed or implied, about its quality, reliability, or any other
# characteristic.
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


def n_class_to_constructor_class_name(
    graph: rdflib.Graph, n_class: rdflib.URIRef
) -> str:
    (
        class_iri_prefix,
        class_iri_namespace,
        class_iri_basename,
    ) = graph.namespace_manager.compute_qname(n_class, False)

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
        raise NotImplementedError("Unrecognized IRI start: %r." % n_class)

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
        n_class: rdflib.URIRef,
        *args: typing.Any,
        documentation_comment: typing.Optional[str] = None,
        **kwargs: typing.Any
    ) -> None:
        self.n_class: rdflib.URIRef = n_class
        self.case_class_name: str = n_class_to_constructor_class_name(graph, n_class)
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
        parts.append("    Based on class with IRI '%s'." % self.n_class)
        parts.append('    """')

        # Build initializer.
        parts.append(
            "    def __init__(self, graph: rdflib.Graph, n_node: rdflib.URIRef, *args: typing.Any, n_types: typing.Set[rdflib.URIRef] = set(), **kwargs: typing.Any) -> None:"
        )
        # Add types in initializer.
        if "'" in str(self.n_class):
            raise ValueError('Unexpected "\'" character in IRI: %r.' % self.n_class)
        parts.append("        if len(n_types) == 0:")
        parts.append("            _n_types = {%r}" % self.n_class)
        parts.append("        else:")
        parts.append("            _n_types = n_types")
        parts.append(
            "        super().__init__(graph, n_node, *args, n_types=_n_types, **kwargs)"
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
                "        self.graph.add((self.n_node, NS_UCO_CORE.hasFacet, facet.n_node))"
            )
            parts.append("    @property")
            parts.append("    def facets(self) -> typing.List[UCO_Facet]:")
            parts.append("        return self._facets")
        elif self.case_class_name == "UCO_ContentDataFacet":
            parts.append("    def add_hash(self, hash: UCO_Hash) -> None:")
            parts.append("        self.hashes.append(hash)")
            parts.append(
                "        self.graph.add((self.n_node, NS_UCO_OBSERVABLE.hash, hash.n_node))"
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

# Portions of this file contributed by NIST are governed by the
# following statement:
#
# This software was developed at the National Institute of Standards
# and Technology by employees of the Federal Government in the course
# of their official duties. Pursuant to Title 17 Section 105 of the
# United States Code, this software is not subject to copyright
# protection within the United States. NIST assumes no responsibility
# whatsoever for its use by other parties, and makes no guarantees,
# expressed or implied, about its quality, reliability, or any other
# characteristic.
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
    def __init__(self, graph: rdflib.Graph, n_node: rdflib.URIRef, *args: typing.Any, n_types: typing.Set[rdflib.URIRef] = set(), **kwargs: typing.Any) -> None:
        super().__init__()
        self._graph: rdflib.Graph = graph
        self._n_node = n_node
        self._n_types: typing.Set[rdflib.URIRef] = n_types
        for n_type in sorted(self.n_types):
            self.graph.add((self.n_node, NS_RDF.type, n_type))

    def add_type(self, n_type: rdflib.URIRef) -> None:
        '''
        Add additional RDF type to graph node.
        '''
        self.n_types.add(n_type)
        self.graph.add((self.n_node, NS_RDF.type, n_type))

    @property
    def graph(self) -> rdflib.Graph:
        return self._graph

    @property
    def n_node(self) -> rdflib.URIRef:
        '''
        The individual this NodeConstructor supports.
        '''
        return self._n_node

    @property
    def n_types(self) -> typing.Set[rdflib.URIRef]:
        return self._n_types

    def add_to_graph(self, graph: rdflib.Graph) -> None:
        for n_type in sorted(self.n_types):
            graph.add((
                self.n_node,
                rdflib.RDF.type,
                n_type
            ))
"""
    )

    n_classes: typing.Set[rdflib.URIRef] = set()
    n_class_to_documentation_comment: typing.Dict[
        rdflib.URIRef, typing.Optional[str]
    ] = dict()
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
        n_classes.add(class_result[0])
        if isinstance(class_result[1], rdflib.Literal):
            n_class_to_documentation_comment[class_result[0]] = class_result[
                1
            ].toPython()

    constructor_class_name_to_case_class_constructor: typing.Dict[
        str, CASEClassConstructor
    ] = dict()
    for n_class in n_classes:
        constructor_class_name = n_class_to_constructor_class_name(graph, n_class)
        if constructor_class_name in constructor_class_name_to_case_class_constructor:
            _logger.debug("n_class = %r.", n_class)
            raise ValueError("Duplicate class name: %r." % constructor_class_name)
        constructor_class_name_to_case_class_constructor[
            constructor_class_name
        ] = CASEClassConstructor(
            graph,
            n_class,
            documentation_comment=n_class_to_documentation_comment.get(n_class),
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
        constructor_class_name = n_class_to_constructor_class_name(
            graph, parent_result[0]
        )

        n_parent_class = parent_result[1]
        if n_parent_class is None or n_parent_class == NS_OWL.Thing:
            parent_constructor_class_name = "NodeConstructor"
        else:
            parent_constructor_class_name = n_class_to_constructor_class_name(
                graph, n_parent_class
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

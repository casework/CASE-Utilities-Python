#!/usr/bin/env python3

# Portions of this file contributed by NIST are governed by the following
# statement:
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

__version__ = "0.2.0"

import importlib
import logging
import os
from typing import List, Optional, Set

import rdflib

import case_utils
from case_utils.case_validate.validate_types import NonExistentCASEVersionError
from case_utils.ontology.version_info import CURRENT_CASE_VERSION

NS_OWL = rdflib.OWL
NS_RDF = rdflib.RDF
NS_RDFS = rdflib.RDFS
NS_SH = rdflib.SH

_logger = logging.getLogger(os.path.basename(__file__))


def concept_is_cdo_concept(n_concept: rdflib.URIRef) -> bool:
    """
    Determine if a concept is part of the CDO ontology.

    :param n_concept: The concept to check.
    :return: whether the concept is part of the CDO ontologies.
    """
    concept_iri = str(n_concept)
    return concept_iri.startswith(
        "https://ontology.unifiedcyberontology.org/"
    ) or concept_iri.startswith("https://ontology.caseontology.org/")


def get_invalid_cdo_concepts(
    data_graph: rdflib.Graph, ontology_graph: rdflib.Graph
) -> Set[rdflib.URIRef]:
    """
    Get the set of concepts in the data graph that are not part of the CDO ontologies as specified with the ontology_graph argument.

    :param data_graph: The data graph to validate.
    :param ontology_graph: The ontology graph to use for validation.
    :return: The list of concepts in the data graph that are not part of the CDO ontology.

    >>> from case_utils.namespace import NS_RDF, NS_OWL, NS_UCO_CORE
    >>> from rdflib import Graph, Literal, Namespace, URIRef
    >>> # Define a namespace for a knowledge base, and a namespace for custom extensions.
    >>> ns_kb = Namespace("http://example.org/kb/")
    >>> ns_ex = Namespace("http://example.org/ontology/")
    >>> dg = Graph()
    >>> og = Graph()
    >>> # Use an ontology graph in review that includes only a single class and a single property excerpted from UCO, but also a single custom property.
    >>> _ = og.add((NS_UCO_CORE.UcoObject, NS_RDF.type, NS_OWL.Class))
    >>> _ = og.add((NS_UCO_CORE.name, NS_RDF.type, NS_OWL.DatatypeProperty))
    >>> _ = og.add((ns_ex.ourCustomProperty, NS_RDF.type, NS_OWL.DatatypeProperty))
    >>> # Define an individual.
    >>> n_uco_object = ns_kb["UcoObject-f494d239-d9fd-48da-bc07-461ba86d8c6c"]
    >>> n_uco_object
    rdflib.term.URIRef('http://example.org/kb/UcoObject-f494d239-d9fd-48da-bc07-461ba86d8c6c')
    >>> # Review a data graph that includes only the single individual, class typo'd (capitalized incorrectly), but property OK.
    >>> _ = dg.add((n_uco_object, NS_RDF.type, NS_UCO_CORE.UCOObject))
    >>> _ = dg.add((n_uco_object, NS_UCO_CORE.name, Literal("Test")))
    >>> _ = dg.add((n_uco_object, ns_ex.customProperty, Literal("Custom Value")))
    >>> invalid_cdo_concepts = get_invalid_cdo_concepts(dg, og)
    >>> invalid_cdo_concepts
    {rdflib.term.URIRef('https://ontology.unifiedcyberontology.org/uco/core/UCOObject')}
    >>> # Note that the property "ourCustomProperty" was typo'd in the data graph, but this was not reported.
    >>> assert ns_ex.ourCustomProperty not in invalid_cdo_concepts
    """
    # Construct set of CDO concepts for data graph concept-existence review.
    cdo_concepts: Set[rdflib.URIRef] = set()

    for n_structural_class in [
        NS_OWL.Class,
        NS_OWL.AnnotationProperty,
        NS_OWL.DatatypeProperty,
        NS_OWL.ObjectProperty,
        NS_RDFS.Datatype,
        NS_SH.NodeShape,
        NS_SH.PropertyShape,
        NS_SH.Shape,
    ]:
        for ontology_triple in ontology_graph.triples(
            (None, NS_RDF.type, n_structural_class)
        ):
            if not isinstance(ontology_triple[0], rdflib.URIRef):
                continue
            if concept_is_cdo_concept(ontology_triple[0]):
                cdo_concepts.add(ontology_triple[0])
    for n_ontology_predicate in [
        NS_OWL.backwardCompatibleWith,
        NS_OWL.imports,
        NS_OWL.incompatibleWith,
        NS_OWL.priorVersion,
        NS_OWL.versionIRI,
    ]:
        for ontology_triple in ontology_graph.triples(
            (None, n_ontology_predicate, None)
        ):
            assert isinstance(ontology_triple[0], rdflib.URIRef)
            assert isinstance(ontology_triple[2], rdflib.URIRef)
            cdo_concepts.add(ontology_triple[0])
            cdo_concepts.add(ontology_triple[2])
    for ontology_triple in ontology_graph.triples((None, NS_RDF.type, NS_OWL.Ontology)):
        if not isinstance(ontology_triple[0], rdflib.URIRef):
            continue
        cdo_concepts.add(ontology_triple[0])

    # Also load historical ontology and version IRIs.
    ontology_and_version_iris_data = importlib.resources.read_text(
        case_utils.ontology, "ontology_and_version_iris.txt"
    )
    for line in ontology_and_version_iris_data.split("\n"):
        cleaned_line = line.strip()
        if cleaned_line == "":
            continue
        cdo_concepts.add(rdflib.URIRef(cleaned_line))

    data_cdo_concepts: Set[rdflib.URIRef] = set()
    for data_triple in data_graph.triples((None, None, None)):
        for data_triple_member in data_triple:
            if isinstance(data_triple_member, rdflib.URIRef):
                if concept_is_cdo_concept(data_triple_member):
                    data_cdo_concepts.add(data_triple_member)
            elif isinstance(data_triple_member, rdflib.Literal):
                if isinstance(data_triple_member.datatype, rdflib.URIRef):
                    if concept_is_cdo_concept(data_triple_member.datatype):
                        data_cdo_concepts.add(data_triple_member.datatype)

    return data_cdo_concepts - cdo_concepts


def get_ontology_graph(
    case_version: Optional[str] = None, supplemental_graphs: Optional[List[str]] = None
) -> rdflib.Graph:
    """
    Get the ontology graph for the given case_version and any supplemental graphs.

    :param case_version: the version of the CASE ontology to use.  If None (i.e. null), the most recent version will be used.  If "none" (the string), no pre-built version of CASE will be used.
    :param supplemental_graphs: a list of supplemental graphs to use.  If None, no supplemental graphs will be used.
    :return: the ontology graph against which to validate the data graph.
    """
    ontology_graph = rdflib.Graph()

    if case_version != "none":
        # Load bundled CASE ontology at requested version.
        if case_version is None or case_version == "":
            case_version = CURRENT_CASE_VERSION
        # If the first character case_version is numeric, prepend case- to it. This allows for the version to be passed
        # by the library as both case-1.2.0 and 1.2.0
        if case_version[0].isdigit():
            case_version = "case-" + case_version
        ttl_filename = case_version + ".ttl"
        _logger.debug("ttl_filename = %r.", ttl_filename)
        # Ensure the requested version of the CASE ontology is available and if not, throw an appropriate exception
        # that can be returned in a user-friendly message.
        if not importlib.resources.is_resource(case_utils.ontology, ttl_filename):
            raise NonExistentCASEVersionError(
                f"The requested version ({case_version}) of the CASE ontology is not available.  Please choose a "
                f"different version. The latest supported version is: {CURRENT_CASE_VERSION}"
            )
        ttl_data = importlib.resources.read_text(case_utils.ontology, ttl_filename)
        ontology_graph.parse(data=ttl_data, format="turtle")

    if supplemental_graphs:
        for arg_ontology_graph in supplemental_graphs:
            _logger.debug("arg_ontology_graph = %r.", arg_ontology_graph)
            ontology_graph.parse(arg_ontology_graph)

    return ontology_graph


def disable_tbox_review(graph: rdflib.Graph) -> None:
    l_true = rdflib.Literal(True)
    ns_uco_owl = rdflib.Namespace("https://ontology.unifiedcyberontology.org/owl/")

    for tbox_shape_basename in {
        "DataOneOf-shape",
        "DatatypeProperty-shacl-constraints-shape",
        "Disjointedness-AP-DP-shape",
        "Disjointedness-AP-OP-shape",
        "Disjointedness-C-DT-shape",
        "Disjointedness-DP-OP-shape",
        "List-shape",
        "ObjectProperty-shacl-constraints-shape",
        "ontologyIRI-versionIRI-prerequisite-shape",
        "versionIRI-nodeKind-shape",
    }:
        n_tbox_shape = ns_uco_owl[tbox_shape_basename]
        graph.add((n_tbox_shape, NS_SH.deactivated, l_true))

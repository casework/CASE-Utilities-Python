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

"""
This script creates a list of all ontology and version IRIs that have ever existed in a CDO ontology to describe a CDO ontology.  I.e. the subject of triples with owl:Ontology as predicate are included, as are the objects of version-referencing triples (owl:versionIRI, owl:incompatibleWith, etc.).
"""

__version__ = "0.1.2"

import argparse
import typing

import rdflib

NS_OWL = rdflib.OWL
NS_RDF = rdflib.RDF


def concept_is_cdo_concept(n_concept: rdflib.URIRef) -> bool:
    """
    This function is purposefully distinct from the function used in case_validate.  Within this script, the publishing history of CASE and UCO is reviewed.

    >>> concept_is_cdo_concept(rdflib.URIRef("http://example.org/ontology/Thing"))
    False
    >>> concept_is_cdo_concept(rdflib.URIRef("https://ontology.unifiedcyberontology.org/uco/core/UcoThing"))
    True
    """
    concept_iri = str(n_concept)
    return (
        concept_iri.startswith("https://ontology.unifiedcyberontology.org/")
        or concept_iri.startswith("https://ontology.caseontology.org/")
        or concept_iri.startswith("https://unifiedcyberontology.org/ontology/")
        or concept_iri.startswith("https://caseontology.org/ontology/")
        or concept_iri == "http://case.example.org/core"
    )


def extract_ontology_iris(ontology_graph: rdflib.Graph) -> typing.Set[rdflib.URIRef]:
    """
    Return all concepts describing the OWL Ontology in the input graph.  This does not return classes, properties, etc. defined within the ontology; instead, it only returns the ontology IRI and annotations about the ontology.
    """
    ontology_concepts: typing.Set[rdflib.URIRef] = set()
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
            ontology_concepts.add(ontology_triple[0])
            ontology_concepts.add(ontology_triple[2])
    for ontology_triple in ontology_graph.triples((None, NS_RDF.type, NS_OWL.Ontology)):
        if not isinstance(ontology_triple[0], rdflib.URIRef):
            continue
        if concept_is_cdo_concept(ontology_triple[0]):
            ontology_concepts.add(ontology_triple[0])
    return ontology_concepts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("out_txt")
    parser.add_argument("in_ttl", nargs="+")
    args = parser.parse_args()

    cdo_concepts: typing.Set[rdflib.URIRef] = set()
    for in_ttl in args.in_ttl:
        ontology_graph = rdflib.Graph()
        ontology_graph.parse(in_ttl)
        ontology_concepts = extract_ontology_iris(ontology_graph)
        for ontology_concept in ontology_concepts:
            if concept_is_cdo_concept(ontology_concept):
                cdo_concepts.add(ontology_concept)

    with open(args.out_txt, "w") as out_fh:
        for cdo_concept in sorted(cdo_concepts):
            print(cdo_concept, file=out_fh)


if __name__ == "__main__":
    main()

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

import binascii
import logging
import os

import pytest
import rdflib.plugins.sparql  # type: ignore

import case_utils.ontology
from case_utils.namespace import NS_UCO_CORE, NS_UCO_OBSERVABLE, NS_UCO_TYPES

_logger = logging.getLogger(os.path.basename(__file__))

NSDICT = {
    "uco-core": NS_UCO_CORE,
    "uco-observable": NS_UCO_OBSERVABLE,
    "uco-types": NS_UCO_TYPES,
}

SRCDIR = os.path.dirname(__file__)


def load_graph(filename: str) -> rdflib.Graph:
    in_graph = rdflib.Graph()
    in_graph.parse(filename)
    # The queries in this test rely on the subclass hierarchy.  Load it.
    case_utils.ontology.load_subclass_hierarchy(in_graph)
    return in_graph


@pytest.fixture
def graph_case_file() -> rdflib.Graph:
    return load_graph(os.path.join(SRCDIR, "sample.txt.ttl"))


@pytest.fixture
def graph_case_file_disable_hashes() -> rdflib.Graph:
    return load_graph(os.path.join(SRCDIR, "sample.txt-disable_hashes.ttl"))


def test_confirm_hashes(graph_case_file: rdflib.Graph) -> None:
    expected = {
        "MD5": "098F6BCD4621D373CADE4E832627B4F6",
        "SHA1": "A94A8FE5CCB19BA61C4C0873D391E987982FBBD3",
        "SHA256": "9F86D081884C7D659A2FEAA0C55AD015A3BF4F1B2B0B822CD15D6C15B0F00A08",
        "SHA512": "EE26B0DD4AF7E749AA1A8EE3C10AE9923F618980772E473F8819A5D4940E0DB27AC185F8A0E1D5F84F88BC887FD67B143732C304CC5FA9AD8E6F57F50028A8FF",
    }
    computed = dict()

    query_sparql = """
SELECT ?lHashMethod ?lHashValue
WHERE {
  ?nFile
    a/rdfs:subClassOf* uco-observable:ObservableObject ;
    uco-core:hasFacet ?nContentDataFacet ;
    .

  ?nContentDataFacet
    a uco-observable:ContentDataFacet ;
    uco-observable:hash ?nHash ;
    .

  ?nHash
    a uco-types:Hash ;
    uco-types:hashMethod ?lHashMethod ;
    uco-types:hashValue ?lHashValue ;
    .
}
"""

    query_object = rdflib.plugins.sparql.prepareQuery(query_sparql, initNs=NSDICT)

    for result in graph_case_file.query(query_object):
        (l_hash_method, l_hash_value) = result
        # .toPython() with the non-XSD datatype returns the original Literal object again.  Hence, str().
        hash_method = str(l_hash_method)
        hash_value = binascii.hexlify(l_hash_value.toPython()).decode().upper()
        computed[hash_method] = hash_value

    assert expected == computed


def test_confirm_mtime(
    graph_case_file: rdflib.Graph, graph_case_file_disable_hashes: rdflib.Graph
) -> None:
    query_confirm_mtime = """
SELECT ?nFile
WHERE {
  ?nFile
    a/rdfs:subClassOf* uco-observable:ObservableObject ;
    uco-core:hasFacet ?nFileFacet ;
    .

  ?nFileFacet
    a uco-observable:FileFacet ;
    uco-observable:modifiedTime "2010-01-02T03:04:56+00:00"^^xsd:dateTime ;
    .
}
"""
    query_object = rdflib.plugins.sparql.prepareQuery(
        query_confirm_mtime, initNs=NSDICT
    )

    n_observable_object = None
    for result in graph_case_file_disable_hashes.query(query_object):
        (n_observable_object,) = result
    assert (
        n_observable_object is not None
    ), "File object with expected mtime not found in hashless graph."

    n_observable_object = None
    for result in graph_case_file.query(query_object):
        (n_observable_object,) = result
    assert (
        n_observable_object is not None
    ), "File object with expected mtime not found in fuller graph."

#!/usr/bin/make -f

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

import typing

import rdflib.plugins.sparql


def _test_subclass_templates_result(filename: str, expected: typing.Set[str]) -> None:
    computed: typing.Set[str] = set()

    graph = rdflib.Graph()
    graph.parse(filename)

    query_string = """\
PREFIX prov: <http://www.w3.org/ns/prov#>
SELECT ?nEntity
WHERE {
  ?nEntity a prov:Entity
}
"""
    for result in graph.query(query_string):
        assert isinstance(result, rdflib.query.ResultRow)
        assert isinstance(result[0], rdflib.URIRef)
        n_entity = result[0]
        computed.add(n_entity.toPython())
    assert expected == computed


def _test_w3_templates_with_blank_nodes_result(filename: str) -> None:
    expected = {("Alice", "Hacker"), ("Bob", "Hacker")}

    graph = rdflib.Graph()
    graph.parse(filename)

    computed = set()
    query_string = """\
PREFIX vcard:   <http://www.w3.org/2001/vcard-rdf/3.0#>

SELECT ?lGivenName ?lFamilyName
WHERE {
  ?nNode
    vcard:givenName ?lGivenName ;
    vcard:familyName ?lFamilyName ;
    .
}
"""
    for result in graph.query(query_string):
        assert isinstance(result, rdflib.query.ResultRow)
        assert isinstance(result[0], rdflib.Literal)
        assert isinstance(result[1], rdflib.term.Literal)
        l_given_name = result[0]
        l_family_name = result[1]
        computed.add((l_given_name.toPython(), l_family_name.toPython()))
    assert expected == computed


def test_w3_templates_with_blank_nodes_result_json() -> None:
    _test_w3_templates_with_blank_nodes_result("w3-output.json")


def test_w3_templates_with_blank_nodes_result_turtle() -> None:
    _test_w3_templates_with_blank_nodes_result("w3-output.ttl")


def test_subclass_templates_result_default_case() -> None:
    _test_subclass_templates_result(
        "subclass-implicit-any.ttl",
        {"http://example.org/kb/file-1", "http://example.org/kb/file-2"},
    )


def test_subclass_templates_result_no_case() -> None:
    _test_subclass_templates_result(
        "subclass-explicit-none.ttl", {"http://example.org/kb/file-1"}
    )

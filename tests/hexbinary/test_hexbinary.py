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

"""
This test suite tests some assumptions that might be made about hexBinary value comparison in Python's rdflib and its SPARQL engine.

This script is expected to have pytest exit in a success state, reporting some tests passing, and some tests XFailing (i.e. being expected to fail).

The overall finding is: in rdflib and rdflib's SPARQL engine, xsd:hexBinaryCanonical is not given any support not given to arbitrary string datatypes.  This, and more specific, findings are affirmed by the tests:

* Some of the tests serve as syntax reminders for SPARQL and pytest.
  - test_sparql_syntax_bind_boolean
  - test_pytest_syntax_xfail
  - test_sparql_syntax_integer_coercion
  - test_sparql_syntax_integer_cast
* SPARQL Literal datatype-casting can coerce known types, but will not cast strings of unknown datatypes.
  - test_sparql_syntax_integer_cast
  - test_sparql_cast_custom_type
* rdflib WILL match xsd:hexBinary data as casing-insensitive.  So, Literals with values "ab" and "AB" match if both have the datatype xsd:hexBinary.
  - test_rdflib_literal_hexbinary
* rdflib WILL NOT match xsd:hexBinaryCanonical data with xsd:hexBinary data, either as Literal objects or with a call to .toPython().
  - test_rdflib_literal_hexbinarycanonical
  - test_rdflib_literal_topython_hexbinarycanonical
* The rdflib SPARQL engine WILL match xsd:hexBinary data as casing-insensitive.  So, "ab" and "AB" match if both have the datatype xsd:hexBinary.
  - test_sparql_compare_hexbinary_matchcase
  - test_sparql_compare_hexbinary_mixcase
  - test_graph_repeat
  - test_graph_all_hexbinary_literals
* The rdflib SPARQL engine WILL match xsd:hexBinaryCanonical data with xsd:hexBinaryCanonical data, when casing matches.
  - test_sparql_compare_hexbinarycanonical_matchcase
* The rdflib SPARQL engine WILL NOT match xsd:hexBinaryCanonical data with xsd:hexBinaryCanonical data, when casing does not match.
  - test_sparql_compare_hexbinarycanonical_mixcase
* The rdflib SPARQL engine WILL NOT compare xsd:hexBinaryCanonical data with xsd:hexBinary data.
  - test_sparql_compare_hb_hbc_mixcase
  - test_sparql_compare_hb_hbc_mixcase_cast
  - test_graph_hexbinarycanonical
"""

import logging
import os
import typing

import pytest
import rdflib.plugins.sparql

_logger = logging.getLogger(os.path.basename(__file__))

# Variables used in several tests.
l_hb_lowercase = rdflib.Literal("ab", datatype=rdflib.XSD.hexBinary)
l_hb_uppercase = rdflib.Literal("AB", datatype=rdflib.XSD.hexBinary)
l_hbc_uppercase = rdflib.Literal("AB", datatype=rdflib.XSD.hexBinaryCanonical)
n_canonical1 = rdflib.URIRef("urn:example:canonical1")
n_lowercase1 = rdflib.URIRef("urn:example:lowercase1")
n_lowercase2 = rdflib.URIRef("urn:example:lowercase2")
n_uppercase1 = rdflib.URIRef("urn:example:uppercase1")
p_predicate = rdflib.URIRef("urn:example:predicate1")


def test_sparql_syntax_bind_boolean() -> None:
    """
    This test serves as a syntax reminder for binding boolean values.
    """
    confirmed = None
    graph = rdflib.Graph()
    for result in graph.query(
        """\
SELECT ?lValue
WHERE {
  BIND( 1 = 1 AS ?lValue )
}
"""
    ):
        (l_value,) = result
        confirmed = l_value.toPython()
    assert confirmed


@pytest.mark.xfail(reason="hard-coded failure")
def test_pytest_syntax_xfail() -> None:
    """
    This test serves as a syntax reminder for the XFail decorator.
    """
    confirmed = None
    graph = rdflib.Graph()
    for result in graph.query(
        """\
SELECT ?lValue
WHERE {
  BIND( 1 = 2 AS ?lValue )
}
"""
    ):
        (l_value,) = result
        confirmed = l_value.toPython()
    assert confirmed


def test_sparql_syntax_integer_coercion() -> None:
    """
    This test serves as a syntax reminder for type coercions.
    """
    confirmed = None
    graph = rdflib.Graph()
    for result in graph.query(
        """\
SELECT ?lValue
WHERE {
  BIND( 1 = "1"^^xsd:integer AS ?lValue )
}
"""
    ):
        (l_value,) = result
        confirmed = l_value.toPython()
    assert confirmed


def test_sparql_syntax_integer_cast() -> None:
    """
    This test serves as a syntax reminder for the casting form of type coercions.
    """
    confirmed = None
    graph = rdflib.Graph()
    for result in graph.query(
        """\
SELECT ?lValue
WHERE {
  BIND( 1 = xsd:integer("1") AS ?lValue )
}
"""
    ):
        (l_value,) = result
        confirmed = l_value.toPython()
    assert confirmed


@pytest.mark.xfail
def test_sparql_cast_custom_type() -> None:
    """
    This test checks for nonexistent literal-datatype assignments.
    """
    confirmed = None
    graph = rdflib.Graph()
    for result in graph.query(
        """\
SELECT ?lValue
WHERE {
  BIND( 1 = xsd:integer("1"^^xsd:hexBinaryTypoXXXX) AS ?lValue )
}
"""
    ):
        (l_value,) = result
        confirmed = l_value.toPython()
    assert confirmed


def test_sparql_compare_hexbinary_mixcase() -> None:
    confirmed = None
    graph = rdflib.Graph()
    for result in graph.query(
        """\
SELECT ?lValue
WHERE {
  BIND( "ab"^^xsd:hexBinary = "AB"^^xsd:hexBinary AS ?lValue )
}
"""
    ):
        (l_value,) = result
        confirmed = l_value.toPython()
    assert confirmed


def test_sparql_compare_hexbinary_matchcase() -> None:
    confirmed = None
    graph = rdflib.Graph()
    for result in graph.query(
        """\
SELECT ?lValue
WHERE {
  BIND( "AB"^^xsd:hexBinary = "AB"^^xsd:hexBinary AS ?lValue )
}
"""
    ):
        (l_value,) = result
        confirmed = l_value.toPython()
    assert confirmed


def test_sparql_compare_hexbinarycanonical_matchcase() -> None:
    confirmed = None
    graph = rdflib.Graph()
    for result in graph.query(
        """\
SELECT ?lValue
WHERE {
  BIND( "AB"^^xsd:hexBinaryCanonical = "AB"^^xsd:hexBinaryCanonical AS ?lValue )
}
"""
    ):
        (l_value,) = result
        confirmed = l_value.toPython()
    assert confirmed


@pytest.mark.xfail
def test_sparql_compare_hexbinarycanonical_mixcase() -> None:
    """
    This test shows hexBinaryCanonical does not induce a casing-insensitive comparison.
    """
    confirmed = None
    graph = rdflib.Graph()
    for result in graph.query(
        """\
SELECT ?lValue
WHERE {
  BIND( "ab"^^xsd:hexBinaryCanonical = "AB"^^xsd:hexBinaryCanonical AS ?lValue )
}
"""
    ):
        (l_value,) = result
        confirmed = l_value.toPython()
    assert confirmed


@pytest.mark.xfail
def test_sparql_compare_hb_hbc_mixcase() -> None:
    """
    This test confirms that literal-comparison takes into account datatype when one type is unknown.
    """
    confirmed = None
    graph = rdflib.Graph()
    for result in graph.query(
        """\
SELECT ?lValue
WHERE {
  BIND( "AB"^^xsd:hexBinary = "AB"^^xsd:hexBinaryCanonical AS ?lValue )
}
"""
    ):
        (l_value,) = result
        confirmed = l_value.toPython()
    assert confirmed


@pytest.mark.xfail
def test_sparql_compare_hb_hbc_mixcase_cast() -> None:
    """
    This test is a bit redundant with test_sparql_cast_custom_type, but is here as an explicit demonstration of failure to cast a hexBinary value.
    """
    confirmed = None
    graph = rdflib.Graph()
    for result in graph.query(
        """\
SELECT ?lValue
WHERE {
  BIND( "ab"^^xsd:hexBinary = xsd:hexBinary("AB"^^xsd:hexBinaryCanonical) AS ?lValue )
}
"""
    ):
        (l_value,) = result
        confirmed = l_value.toPython()
    assert confirmed


def test_rdflib_literal_hexbinary() -> None:
    _logger.debug("l_hb_lowercase = %r." % l_hb_lowercase)
    _logger.debug("l_hb_uppercase = %r." % l_hb_uppercase)
    _logger.debug("l_hb_lowercase.toPython() = %r." % l_hb_lowercase.toPython())
    _logger.debug("l_hb_uppercase.toPython() = %r." % l_hb_uppercase.toPython())

    assert l_hb_lowercase == l_hb_lowercase
    assert l_hb_lowercase.toPython() == l_hb_lowercase.toPython()

    assert l_hb_lowercase == l_hb_uppercase
    assert l_hb_lowercase.toPython() == l_hb_uppercase.toPython()


@pytest.mark.xfail
def test_rdflib_literal_hexbinarycanonical() -> None:
    _logger.debug("l_hb_uppercase = %r." % l_hb_uppercase)
    _logger.debug("l_hbc_uppercase = %r." % l_hbc_uppercase)

    assert l_hb_uppercase == l_hbc_uppercase


@pytest.mark.xfail
def test_rdflib_literal_topython_hexbinarycanonical() -> None:
    _logger.debug("l_hb_lowercase.toPython() = %r." % l_hb_lowercase.toPython())
    _logger.debug("l_hb_uppercase.toPython() = %r." % l_hb_uppercase.toPython())

    assert l_hb_uppercase.toPython() == l_hbc_uppercase.toPython()


def _query_all_value_matches(graph: rdflib.Graph) -> typing.Set[str]:
    """
    Return set of all node names (as strings) that have a matching value, where
    "matching" is determined by the SPARQL engine's type and data coercions.
    """
    computed = set()
    for result in graph.query(
        """\
SELECT ?nNode1 ?nNode2
WHERE {
  ?nNode1 ?p ?lValue .
  ?nNode2 ?p ?lValue .
  FILTER ( ?nNode1 != ?nNode2 )
}"""
    ):
        (n_node1, n_node2) = result
        computed.add(n_node1.toPython())
        computed.add(n_node2.toPython())
    return computed


def test_graph_repeat() -> None:
    """
    Two nodes are given the same literal value, and are found to match on literal values.
    """
    graph = rdflib.Graph()
    graph.add((n_lowercase1, p_predicate, l_hb_lowercase))
    graph.add((n_lowercase2, p_predicate, l_hb_lowercase))
    expected = {"urn:example:lowercase1", "urn:example:lowercase2"}
    computed = _query_all_value_matches(graph)
    assert computed == expected


def test_graph_all_hexbinary_literals() -> None:
    """
    Two nodes with the same literal value, and another node with the uppercase of the literal hexBinary value, are found to match on literal values.
    """
    graph = rdflib.Graph()
    graph.add((n_lowercase1, p_predicate, l_hb_lowercase))
    graph.add((n_lowercase2, p_predicate, l_hb_lowercase))
    graph.add((n_uppercase1, p_predicate, l_hb_uppercase))

    expected = {
        "urn:example:lowercase1",
        "urn:example:lowercase2",
        "urn:example:uppercase1",
    }

    computed = _query_all_value_matches(graph)
    assert computed == expected


@pytest.mark.xfail
def test_graph_hexbinarycanonical() -> None:
    graph = rdflib.Graph()
    graph.add((n_lowercase1, p_predicate, l_hb_lowercase))
    graph.add((n_lowercase2, p_predicate, l_hb_lowercase))
    graph.add((n_uppercase1, p_predicate, l_hb_uppercase))
    graph.add((n_canonical1, p_predicate, l_hbc_uppercase))

    expected = {
        "urn:example:canonical1",
        "urn:example:lowercase1",
        "urn:example:lowercase2",
        "urn:example:uppercase1",
    }

    computed = _query_all_value_matches(graph)
    assert computed == expected

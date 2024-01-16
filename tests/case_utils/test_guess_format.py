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

import pytest
import rdflib

PATH_TO_TTL = "/nonexistent/foo.ttl"
PATH_TO_JSON = "/nonexistent/foo.json"
PATH_TO_JSONLD = "/nonexistent/foo.jsonld"
PATH_TO_XHTML = "/nonexistent/foo.xhtml"
FMAP_XHTML_GRDDL = {"xhtml": "grddl"}


def test_rdflib_util_guess_format_xhtml_default() -> None:
    assert (
        rdflib.util.guess_format(PATH_TO_XHTML) == "rdfa"
    ), "Failed to reproduce rdflib.util.guess_format test"


def test_rdflib_util_guess_format_xhtml_fmap() -> None:
    """
    This test implements one of the documented demonstrations in rdflib.util.guess_format.
    """
    assert (
        rdflib.util.guess_format(PATH_TO_XHTML, FMAP_XHTML_GRDDL) == "grddl"
    ), "Failed to reproduce rdflib.util.guess_format test"


def test_rdflib_util_guess_format_ttl_default() -> None:
    assert (
        rdflib.util.guess_format(PATH_TO_TTL) == "turtle"
    ), "Failed to recognize .ttl RDF file extension"


@pytest.mark.xfail(
    reason="rdflib 5.0.0 guess_format fmap argument overwrites base module's extension map",
    strict=True,
)
def test_rdflib_util_guess_format_ttl_fmap() -> None:
    assert (
        rdflib.util.guess_format(PATH_TO_TTL, FMAP_XHTML_GRDDL) == "turtle"
    ), "Failed to recognize .ttl RDF file extension when using fmap"


def test_rdflib_util_guess_format_json() -> None:
    assert (
        rdflib.util.guess_format(PATH_TO_JSON) == "json-ld"
    ), "Failed to recognize .json RDF file extension"


def test_rdflib_util_guess_format_jsonld() -> None:
    assert (
        rdflib.util.guess_format(PATH_TO_JSONLD) == "json-ld"
    ), "Failed to recognize .jsonld RDF file extension"

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

import json
import pathlib
import typing

import pytest
import rdflib.plugins.parsers.notation3

srcdir = pathlib.Path(__file__).parent

PLAINTEXT_VALIDATION_PASS = """\
Validation Report
Conforms: True
""".strip()


def _guess_format(basename: str) -> typing.Optional[str]:
    """
    Guess format by file extension.
    """
    filepath = srcdir / basename
    return rdflib.util.guess_format(str(filepath))


def _parse_graph(basename: str, asserted_format: str) -> rdflib.Graph:
    graph = rdflib.Graph()
    filepath = srcdir / basename
    graph.parse(str(filepath), format=asserted_format)
    return graph


def _verify_plaintext_report(basename: str) -> None:
    filepath = srcdir / basename
    with filepath.open("r") as fh:
        assert PLAINTEXT_VALIDATION_PASS == fh.read(50)[:-1]


@pytest.mark.xfail(
    reason="Known mismatch", raises=json.decoder.JSONDecodeError, strict=True
)
def test_format_human_output_jsonld() -> None:
    subject_file = "format_human_output_jsonld.jsonld"
    asserted_format = _guess_format(subject_file)
    assert asserted_format == "json-ld"
    _parse_graph(subject_file, asserted_format)


@pytest.mark.xfail(
    reason="Known mismatch",
    raises=rdflib.plugins.parsers.notation3.BadSyntax,
    strict=True,
)
def test_format_human_output_turtle() -> None:
    subject_file = "format_human_output_turtle.ttl"
    asserted_format = _guess_format(subject_file)
    assert asserted_format == "turtle"
    _parse_graph(subject_file, asserted_format)


def test_format_human_output_txt() -> None:
    _verify_plaintext_report("format_human_output_txt.txt")


def test_format_human_output_unspecified() -> None:
    _verify_plaintext_report("format_human_output_unspecified.txt")


def test_format_jsonld_output_jsonld() -> None:
    subject_file = "format_jsonld_output_jsonld.jsonld"
    asserted_format = _guess_format(subject_file)
    assert asserted_format == "json-ld"
    _parse_graph(subject_file, asserted_format)


@pytest.mark.xfail(
    reason="Known mismatch",
    raises=rdflib.plugins.parsers.notation3.BadSyntax,
    strict=True,
)
def test_format_jsonld_output_turtle() -> None:
    subject_file = "format_jsonld_output_turtle.ttl"
    asserted_format = _guess_format(subject_file)
    assert asserted_format == "turtle"
    _parse_graph(subject_file, asserted_format)


def test_format_jsonld_output_txt() -> None:
    subject_file = "format_jsonld_output_txt.txt"
    asserted_format = _guess_format(subject_file)
    assert asserted_format is None
    _parse_graph(subject_file, "json-ld")


def test_format_jsonld_output_unspecified() -> None:
    subject_file = "format_jsonld_output_unspecified.jsonld"
    asserted_format = _guess_format(subject_file)
    assert asserted_format == "json-ld"
    _parse_graph(subject_file, asserted_format)


@pytest.mark.xfail(
    reason="Known mismatch", raises=json.decoder.JSONDecodeError, strict=True
)
def test_format_turtle_output_jsonld() -> None:
    subject_file = "format_turtle_output_jsonld.jsonld"
    asserted_format = _guess_format(subject_file)
    assert asserted_format == "json-ld"
    _parse_graph(subject_file, asserted_format)


def test_format_turtle_output_turtle() -> None:
    subject_file = "format_turtle_output_turtle.ttl"
    asserted_format = _guess_format(subject_file)
    assert asserted_format == "turtle"
    _parse_graph(subject_file, asserted_format)


def test_format_turtle_output_txt() -> None:
    subject_file = "format_turtle_output_txt.txt"
    asserted_format = _guess_format(subject_file)
    assert asserted_format is None
    _parse_graph(subject_file, "turtle")


def test_format_turtle_output_unspecified() -> None:
    subject_file = "format_turtle_output_unspecified.ttl"
    asserted_format = _guess_format(subject_file)
    assert asserted_format == "turtle"
    _parse_graph(subject_file, asserted_format)


@pytest.mark.xfail(
    reason="Known mismatch", raises=json.decoder.JSONDecodeError, strict=True
)
def test_format_unspecified_output_jsonld() -> None:
    subject_file = "format_unspecified_output_jsonld.jsonld"
    asserted_format = _guess_format(subject_file)
    assert asserted_format == "json-ld"
    _parse_graph(subject_file, asserted_format)


@pytest.mark.xfail(
    reason="Known mismatch",
    raises=rdflib.plugins.parsers.notation3.BadSyntax,
    strict=True,
)
def test_format_unspecified_output_turtle() -> None:
    subject_file = "format_unspecified_output_turtle.ttl"
    asserted_format = _guess_format(subject_file)
    assert asserted_format == "turtle"
    _parse_graph(subject_file, asserted_format)


def test_format_unspecified_output_txt() -> None:
    _verify_plaintext_report("format_unspecified_output_txt.txt")


def test_format_unspecified_output_unspecified() -> None:
    _verify_plaintext_report("format_unspecified_output_unspecified.txt")

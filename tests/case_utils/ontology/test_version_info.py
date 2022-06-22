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

import importlib.resources
import pathlib
import typing

import rdflib  # type: ignore

import case_utils.ontology
from case_utils.ontology.version_info import (
    CURRENT_CASE_VERSION,
    built_version_choices_list,
)

NS_OWL = rdflib.OWL


def test_built_version_choices_list() -> None:
    for built_version_choice in sorted(built_version_choices_list):
        if built_version_choice == "none":
            continue
        ttl_filename = built_version_choice + ".ttl"
        with importlib.resources.open_text(case_utils.ontology, ttl_filename) as tmp_fh:
            assert tmp_fh


def test_case_ontology_version_info_versus_monolithic() -> None:
    ontology_graph = rdflib.Graph()

    ttl_filename = "case-" + CURRENT_CASE_VERSION + ".ttl"
    ttl_data = importlib.resources.read_text(case_utils.ontology, ttl_filename)
    ontology_graph.parse(data=ttl_data)

    version_info: typing.Optional[str] = None
    for triple in ontology_graph.triples(
        (
            rdflib.URIRef("https://ontology.caseontology.org/case/case"),
            NS_OWL.versionInfo,
            None,
        )
    ):
        version_info = str(triple[2])
    assert version_info is not None, "Failed to retrieve owl:versionInfo"

    assert (
        CURRENT_CASE_VERSION == version_info
    ), "Version recorded in case_utils.ontology.version_info does not match built ontology"


def test_case_ontology_version_info_versus_submodule() -> None:
    ontology_graph = rdflib.Graph()

    top_srcdir = pathlib.Path(__file__).parent / ".." / ".." / ".."
    assert (
        top_srcdir / ".gitmodules"
    ).exists(), "Hard-coded path to top_srcdir no longer correct"

    ttl_filepath = (
        top_srcdir / "dependencies" / "CASE" / "ontology" / "master" / "case.ttl"
    )

    ontology_graph.parse(str(ttl_filepath))

    version_info: typing.Optional[str] = None
    for triple in ontology_graph.triples(
        (
            rdflib.URIRef("https://ontology.caseontology.org/case/case"),
            NS_OWL.versionInfo,
            None,
        )
    ):
        version_info = str(triple[2])
    assert version_info is not None, "Failed to retrieve owl:versionInfo"

    assert (
        CURRENT_CASE_VERSION == version_info
    ), "Version recorded in case_utils.ontology.version_info does not match tracked ontology"

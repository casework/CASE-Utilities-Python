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

__version__ = "0.1.2"

import importlib.resources
import logging
import os

import rdflib

# Yes, this next import is self-referential (/circular).  But, it does work with importlib.
import case_utils.ontology

from .version_info import CURRENT_CASE_VERSION

_logger = logging.getLogger(os.path.basename(__file__))


def load_subclass_hierarchy(
    graph: rdflib.Graph, *, built_version: str = "case-" + CURRENT_CASE_VERSION
) -> None:
    """
    Adds all ontology rdfs:subClassOf statements from the version referred to by built_version.
    """
    if built_version != "none":
        _logger.debug("Loading subclass hierarchy.")
        ttl_filename = built_version + "-subclasses.ttl"
        _logger.debug("ttl_filename = %r.", ttl_filename)
        ttl_data = importlib.resources.read_text(case_utils.ontology, ttl_filename)
        graph.parse(data=ttl_data)

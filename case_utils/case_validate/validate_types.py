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

__version__ = "0.1.0"

from typing import Set, Union

import rdflib


class ValidationResult:
    def __init__(
        self,
        conforms: bool,
        graph: Union[Exception, bytes, str, rdflib.Graph],
        text: str,
        undefined_concepts: Set[rdflib.URIRef],
    ) -> None:
        self.conforms = conforms
        self.graph = graph
        self.text = text
        self.undefined_concepts = undefined_concepts


class NonExistentCDOConceptWarning(UserWarning):
    """
    This class is used when a concept is encountered in the data graph that is not part of CDO ontologies, according to the --built-version flags and --ontology-graph flags.
    """

    pass


class NonExistentCASEVersionError(Exception):
    """
    This class is used when an invalid CASE version is requested that is not supported by the library.
    """

    pass

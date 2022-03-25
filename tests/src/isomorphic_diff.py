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
This script confirms two graphs are isomorphic.  Its intention is to save on noisy git commits from test re-runs; the noise comes from rdflib's json-ld module not having an obvious way to force blank nodes to be inlined.

Sample code c/o:
https://rdflib.readthedocs.io/en/4.0/_modules/rdflib/compare.html

As with the command line utility 'diff', this exits with status 0 if the files are the "same", 1 if they differ.

This script works in the same spirit as the rdflib-provided command rdfgraphisomorphism.  However, at the time of this writing, that script failed to process unit test data documented elsewhere in rdflib, and also lacked flexibility in specifying graph formats other than a hard-coded closed set.  That list did not include JSON-LD, which is the format the CASE community uses for its instance data.

The failure to run was reported on 2018-02-22:
https://github.com/RDFLib/rdflib/issues/812

On resolution of rdflib issue 812, and on adding some format-support flexibility, isomorphic_diff.py is likely to be deprecated in favor of using the upstream rdfgraphisomorphism command.
"""

__version__ = "0.2.0"

import argparse
import logging
import os
import sys

import rdflib.compare  # type: ignore

import case_utils

_logger = logging.getLogger(os.path.basename(__file__))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("in_graph_1")
    parser.add_argument("in_graph_2")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    g1 = rdflib.Graph()
    g2 = rdflib.Graph()

    g1.parse(args.in_graph_1)
    g2.parse(args.in_graph_2)

    # _logger.debug("type(g1) = %r.", type(g1))
    # _logger.debug("type(g2) = %r.", type(g2))

    # _logger.debug("len(g1) = %d.", len(g1))
    # _logger.debug("len(g2) = %d.", len(g2))

    i1 = rdflib.compare.to_isomorphic(g1)
    i2 = rdflib.compare.to_isomorphic(g2)

    # _logger.debug("type(i1) = %r.", type(i1))
    # _logger.debug("type(i2) = %r.", type(i2))

    if i1 == i2:
        sys.exit(0)

    def _report(diff_symbol: str, graph: rdflib.Graph) -> None:
        """
        This function copied in spirit from:
        https://rdflib.readthedocs.io/en/stable/apidocs/rdflib.html#module-rdflib.compare
        """
        for line in sorted(graph.serialize(format="nt").splitlines()):
            if line.strip() == "":
                continue
            _logger.debug("%s %s", diff_symbol, line)

    # _report("1", g1)
    # _report("2", g2)

    if args.debug:
        (in_both, in_first, in_second) = rdflib.compare.graph_diff(i1, i2)
        _report("<", in_first)
        _report(">", in_second)

    sys.exit(1)


if __name__ == "__main__":
    main()

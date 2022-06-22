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
This script takes multiple input JSON-LD or Turtle files and emits a single Turtle graph.
"""

__version__ = "0.2.1"

import rdflib  # type: ignore


def main() -> None:
    g = rdflib.Graph()
    for in_graph in args.in_graph:
        g.parse(in_graph)
    g.serialize(args.out_graph)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("out_graph")
    parser.add_argument("in_graph", nargs="*")
    args = parser.parse_args()
    main()

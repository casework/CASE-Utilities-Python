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
This script executes a SPARQL SELECT query, returning a table representation.  The design of the workflow is based on this example built on SPARQLWrapper:
https://lawlesst.github.io/notebook/sparql-dataframe.html

Note that this assumes a limited syntax style in the outer SELECT clause of the query - only named variables, no aggregations, and a single space character separating all variable names.  E.g.:

SELECT ?x ?y ?z
WHERE
{ ... }

The word "DISTINCT" will also be cut from the query, if present.

Should a more complex query be necessary, an outer, wrapping SELECT query would let this script continue to function.
"""

__version__ = "0.5.1"

import argparse
import binascii
import logging
import os
import sys
import typing

import pandas as pd  # type: ignore
import rdflib.plugins.sparql

import case_utils.ontology
from case_utils.ontology.version_info import (
    CURRENT_CASE_VERSION,
    built_version_choices_list,
)

NS_XSD = rdflib.XSD

_logger = logging.getLogger(os.path.basename(__file__))


def query_text_to_variables(select_query_text: str) -> typing.List[str]:
    # Build columns list from SELECT line.
    select_query_text_lines = select_query_text.split("\n")
    select_line = [
        line for line in select_query_text_lines if line.startswith("SELECT ")
    ][0]
    variables = select_line.replace(" DISTINCT", "").replace("SELECT ", "").split(" ")
    return variables


def graph_and_query_to_data_frame(
    graph: rdflib.Graph,
    select_query_text: str,
    *args: typing.Any,
    built_version: str = "case-" + CURRENT_CASE_VERSION,
    disallow_empty_results: bool = False,
    use_prefixes: bool = False,
    **kwargs: typing.Any,
) -> pd.DataFrame:
    # Inherit prefixes defined in input context dictionary.
    nsdict = {k: v for (k, v) in graph.namespace_manager.namespaces()}

    # Avoid side-effects on input parameter.
    if "subClassOf" in select_query_text:
        _graph = rdflib.Graph()
        _graph += graph
        case_utils.ontology.load_subclass_hierarchy(_graph, built_version=built_version)
    else:
        _graph = graph

    variables = query_text_to_variables(select_query_text)

    tally = 0
    records = []
    select_query_object = rdflib.plugins.sparql.processor.prepareQuery(
        select_query_text, initNs=nsdict
    )
    for row_no, row in enumerate(_graph.query(select_query_object)):
        assert isinstance(row, rdflib.query.ResultRow)
        tally = row_no + 1
        record = []
        for column_no, column in enumerate(row):
            if column is None:
                column_value = ""
            elif isinstance(column, rdflib.term.Literal):
                if column.datatype == NS_XSD.hexBinary:
                    # Use hexlify to convert xsd:hexBinary to ASCII.
                    # The render to ASCII is in support of this script rendering results for website viewing.
                    # .decode() is because hexlify returns bytes.
                    column_value = binascii.hexlify(column.toPython()).decode()
                else:
                    column_value = column.toPython()
            elif isinstance(column, rdflib.URIRef):
                if use_prefixes:
                    column_value = graph.namespace_manager.qname(column.toPython())
                else:
                    column_value = column.toPython()
            elif isinstance(column, rdflib.BNode):
                column_value = column.toPython()
            if row_no == 0:
                _logger.debug("row[0]column[%d] = %r." % (column_no, column_value))
            record.append(column_value)
        records.append(record)

    if tally == 0:
        if disallow_empty_results:
            raise ValueError("Failed to return any results.")

    df = pd.DataFrame(records, columns=variables)
    return df


def data_frame_to_table_text(
    df: pd.DataFrame,
    *args: typing.Any,
    json_indent: typing.Optional[int] = None,
    json_orient: str,
    output_mode: str,
    use_header: bool,
    use_index: bool,
    **kwargs: typing.Any,
) -> str:
    table_text: typing.Optional[str] = None

    # Set up kwargs dicts.  One kwarg behaves slightly differently for Markdown vs. other formats.
    general_kwargs: typing.Dict[str, typing.Any] = dict()
    md_kwargs: typing.Dict[str, typing.Any] = dict()

    # Note some output modes will drop 'header' from general_kwargs, due to alternate support or lack of support.
    if use_header:
        general_kwargs["header"] = True
    else:
        general_kwargs["header"] = False
        md_kwargs["headers"] = tuple()

    general_kwargs["index"] = use_index

    if output_mode in {"csv", "tsv"}:
        sep: str
        if output_mode == "csv":
            sep = ","
        elif output_mode == "tsv":
            sep = "\t"
        else:
            raise NotImplementedError(
                "Output extension not implemented in CSV-style output."
            )
        table_text = df.to_csv(sep=sep, **general_kwargs)
    elif output_mode == "html":
        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_html.html
        # Add CSS classes for CASE website Bootstrap support.
        table_text = df.to_html(
            classes=("table", "table-bordered", "table-condensed"), **general_kwargs
        )
    elif output_mode == "json":
        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html

        # Drop unsupported kwarg.
        del general_kwargs["header"]

        table_text = df.to_json(
            indent=json_indent, orient=json_orient, date_format="iso", **general_kwargs
        )
    elif output_mode == "md":
        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_markdown.html
        # https://pypi.org/project/tabulate/
        # Assume Github-flavored Markdown.

        # Drop unsupported kwarg.
        del general_kwargs["header"]

        table_text = df.to_markdown(tablefmt="github", **general_kwargs, **md_kwargs)
    else:
        if table_text is None:
            raise NotImplementedError("Unimplemented output mode: %r." % output_mode)
    assert table_text is not None

    return table_text


def main() -> None:
    parser = argparse.ArgumentParser()

    # Configure debug logging before running parse_args, because there could be an error raised before the construction of the argument parser.
    logging.basicConfig(
        level=logging.DEBUG
        if ("--debug" in sys.argv or "-d" in sys.argv)
        else logging.INFO
    )

    parser.add_argument("-d", "--debug", action="store_true")
    parser.add_argument(
        "--built-version",
        choices=tuple(built_version_choices_list),
        default="case-" + CURRENT_CASE_VERSION,
        help="Ontology version to use to supplement query, such as for subclass querying.  Does not require networking to use.  Default is most recent CASE release.  Passing 'none' will mean no pre-built CASE ontology versions accompanying this tool will be included in the analysis.",
    )
    parser.add_argument(
        "--disallow-empty-results",
        action="store_true",
        help="Raise error if no results are returned for query.",
    )
    parser.add_argument(
        "--json-indent",
        type=int,
        help="Number of whitespace characters to use for indentation.  Only applicable for JSON output.",
    )
    parser.add_argument(
        "--json-orient",
        default="columns",
        choices=("columns", "index", "records", "split", "table", "values"),
        help="Orientation to use for Pandas DataFrame JSON output.  Only applicable for JSON output.",
    )
    parser.add_argument(
        "--use-prefixes",
        action="store_true",
        help="Abbreviate node IDs according to graph's encoded prefixes.  (This will use prefixes in the graph, not the query.)",
    )
    parser.add_argument(
        "out_table",
        help="Expected extensions are .html for HTML tables, .json for JSON tables, .md for Markdown tables, .csv for comma-separated values, and .tsv for tab-separated values.  Note that JSON is a Pandas output JSON format (chosen by '--json-orient'), and not JSON-LD.",
    )
    parser.add_argument(
        "in_sparql",
        help="File containing a SPARQL SELECT query.  Note that prefixes not mapped with a PREFIX statement will be mapped according to their first occurrence among input graphs.",
    )

    parser_header_group = parser.add_mutually_exclusive_group(required=False)
    parser_header_group.add_argument(
        "--header",
        action="store_true",
        help="Print column labels.  This is the default behavior.",
    )
    parser_header_group.add_argument(
        "--no-header",
        action="store_true",
        help="Do not print column labels.",
    )

    parser_index_group = parser.add_mutually_exclusive_group(required=False)
    parser_index_group.add_argument(
        "--index",
        action="store_true",
        help="Print index (auto-incrementing row labels as left untitled column).  This is the default behavior.",
    )
    parser_index_group.add_argument(
        "--no-index",
        action="store_true",
        help="Do not print index.  If output is JSON, --json-orient must be 'split' or 'table'.",
    )

    parser.add_argument("in_graph", nargs="+")
    args = parser.parse_args()

    output_mode: str
    if args.out_table.endswith(".csv"):
        output_mode = "csv"
    elif args.out_table.endswith(".html"):
        output_mode = "html"
    elif args.out_table.endswith(".json"):
        output_mode = "json"
    elif args.out_table.endswith(".md"):
        output_mode = "md"
    elif args.out_table.endswith(".tsv"):
        output_mode = "tsv"
    else:
        raise NotImplementedError("Output file extension not implemented.")

    graph = rdflib.Graph()
    for in_graph_filename in args.in_graph:
        graph.parse(in_graph_filename)

    select_query_text: typing.Optional[str] = None
    with open(args.in_sparql, "r") as in_fh:
        select_query_text = in_fh.read().strip()
    if select_query_text is None:
        raise ValueError("Failed to load query.")
    _logger.debug("select_query_text = %r." % select_query_text)

    # Process --header and --no-header.
    use_header: bool
    if args.header is True:
        use_header = True
    if args.no_header is True:
        use_header = False
    else:
        use_header = True

    # Process --index and --no-index.
    use_index: bool
    if args.index is True:
        use_index = True
    if args.no_index is True:
        use_index = False
    else:
        use_index = True

    if (
        output_mode == "json"
        and use_index is False
        and args.json_orient not in {"split", "table"}
    ):
        raise ValueError(
            "For JSON output, --no-index flag requires --json-orient to be either 'split' or 'table'."
        )

    df = graph_and_query_to_data_frame(
        graph,
        select_query_text,
        built_version=args.built_version,
        disallow_empty_results=args.disallow_empty_results is True,
        use_prefixes=args.use_prefixes is True,
    )

    table_text = data_frame_to_table_text(
        df,
        json_indent=args.json_indent,
        json_orient=args.json_orient,
        output_mode=output_mode,
        use_header=use_header,
        use_index=use_index,
    )
    with open(args.out_table, "w") as out_fh:
        out_fh.write(table_text)
        if table_text[-1] != "\n":
            # End file with newline.  CSV and TSV modes end with a built-in newline.
            out_fh.write("\n")


if __name__ == "__main__":
    main()

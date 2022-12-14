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

import pathlib
import typing

import pytest
import rdflib

import case_utils.case_sparql_select

SRCDIR = pathlib.Path(__file__).parent

GRAPH = rdflib.Graph()
GRAPH.parse(str(SRCDIR / "w3-input-2.ttl"))
GRAPH.parse(str(SRCDIR / "w3-input-3.json"))
assert len(GRAPH) > 0

SELECT_QUERY_TEXT: typing.Optional[str] = None
with (SRCDIR / "w3-input-1.sparql").open("r") as _fh:
    SELECT_QUERY_TEXT = _fh.read().strip()
assert SELECT_QUERY_TEXT is not None

DATA_FRAME = case_utils.case_sparql_select.graph_and_query_to_data_frame(
    GRAPH, SELECT_QUERY_TEXT
)


def make_data_frame_to_json_table_text_parameters() -> typing.Iterator[
    typing.Tuple[str, str, bool, bool]
]:
    for use_header in [False, True]:
        for use_index in [False, True]:
            for output_mode in ["csv", "html", "json", "md", "tsv"]:
                if output_mode == "json":
                    for json_orient in [
                        "columns",
                        "index",
                        "records",
                        "split",
                        "table",
                        "values",
                    ]:
                        # Handle incompatible parameter pairings for JSON mode.
                        if use_index is False:
                            if json_orient not in {"split", "table"}:
                                continue

                        yield (json_orient, output_mode, use_header, use_index)
                else:
                    yield ("columns", output_mode, use_header, use_index)


@pytest.mark.parametrize(
    "json_orient, output_mode, use_header, use_index",
    make_data_frame_to_json_table_text_parameters(),
)
def test_data_frame_to_table_text_json(
    json_orient: str,
    output_mode: str,
    use_header: bool,
    use_index: bool,
) -> None:
    table_text = case_utils.case_sparql_select.data_frame_to_table_text(
        DATA_FRAME,
        json_orient=json_orient,
        output_mode=output_mode,
        use_header=use_header,
        use_index=use_index,
    )

    output_filename_template = ".check-w3-output-%s_header-%s_index%s.%s"
    header_part = "with" if use_header else "without"
    index_part = "with" if use_index else "without"
    if output_mode == "json":
        json_orient_part = "-orient-" + json_orient
    else:
        json_orient_part = ""
    output_filename = output_filename_template % (
        header_part,
        index_part,
        json_orient_part,
        output_mode,
    )
    with (SRCDIR / output_filename).open("w") as out_fh:
        out_fh.write(table_text)
        if table_text[-1] != "\n":
            out_fh.write("\n")

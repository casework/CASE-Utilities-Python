#!/usr/bin/make -f

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

SHELL := /bin/bash

top_srcdir := $(shell cd ../../.. ; pwd)

tests_srcdir := $(top_srcdir)/tests

all: \
  prefixed_results.csv \
  prefixed_results.html \
  prefixed_results.json \
  prefixed_results-indented.json \
  prefixed_results.md \
  prefixed_results.tsv \
  subclass-explicit-none.md \
  subclass-implicit-any.md \
  w3-output.csv \
  w3-output.html \
  w3-output.json \
  w3-output-indented.json \
  w3-output.md \
  w3-output.tsv

.PHONY: \
  check-subclass \
  check-subclass-explicit-none \
  check-subclass-implicit-any \
  check-w3-csv \
  check-w3-html \
  check-w3-json \
  check-w3-json-indented \
  check-w3-markdown \
  check-w3-tsv

.PRECIOUS: \
  prefixed_results.% \
  subclass-% \
  w3-output.%

check: \
  check-w3-csv \
  check-w3-html \
  check-w3-json \
  check-w3-markdown \
  check-w3-tsv \
  check-prefixed_results \
  check-subclass
	source $(tests_srcdir)/venv/bin/activate \
	  && pytest \
	    --log-level=DEBUG

check-prefixed_results: \
  check-prefixed_results-csv \
  check-prefixed_results-html \
  check-prefixed_results-json \
  check-prefixed_results-md \
  check-prefixed_results-tsv

check-prefixed_results-csv: \
  .check-prefixed_results.csv \
  prefixed_results.csv
	diff $^

check-prefixed_results-html: \
  .check-prefixed_results.html \
  prefixed_results.html
	diff $^

check-prefixed_results-json: \
  check-prefixed_results-json-indented \
  .check-prefixed_results.json \
  prefixed_results.json
	diff \
	  .check-prefixed_results.json \
	  prefixed_results.json

check-prefixed_results-json-indented: \
  .check-prefixed_results-indented.json \
  prefixed_results-indented.json
	diff $^

check-prefixed_results-md: \
  .check-prefixed_results.md \
  prefixed_results.md
	diff $^

check-prefixed_results-tsv: \
  .check-prefixed_results.tsv \
  prefixed_results.tsv
	diff $^

check-subclass: \
  check-subclass-explicit-none \
  check-subclass-implicit-any

check-subclass-explicit-none: \
  .check-subclass-explicit-none.md \
  subclass-explicit-none.md
	diff $^

check-subclass-implicit-any: \
  .check-subclass-implicit-any.md \
  subclass-implicit-any.md
	diff $^

check-w3-csv: \
  .check-w3-output.csv \
  w3-output.csv
	diff $^

check-w3-html: \
  .check-w3-output.html \
  w3-output.html
	diff $^

check-w3-json: \
  .check-w3-output.json \
  check-w3-json-indented \
  w3-output.json
	diff \
	  .check-w3-output.json \
	  w3-output.json

check-w3-json-indented: \
  .check-w3-output-indented.json \
  w3-output-indented.json
	diff $^

check-w3-markdown: \
  .check-w3-output.md \
  w3-output.md
	diff $^

check-w3-tsv: \
  .check-w3-output.tsv \
  w3-output.tsv
	diff $^

clean:
	@rm -rf \
	  __pycache__
	@rm -f \
	  *.csv \
	  *.html \
	  *.md \
	  *.tsv \
	  *output*.json \
	  _*

prefixed_results.%: \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/case_utils/case_sparql_select/__init__.py \
  $(top_srcdir)/case_utils/ontology/__init__.py \
  $(top_srcdir)/case_utils/ontology/version_info.py \
  subclass.json \
  subclass.sparql
	source $(tests_srcdir)/venv/bin/activate \
	  && case_sparql_select \
	    --use-prefixes \
	    _$@ \
	    subclass.sparql \
	    subclass.json
	mv _$@ $@

prefixed_results-indented.json: \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/case_utils/case_sparql_select/__init__.py \
  $(top_srcdir)/case_utils/ontology/__init__.py \
  $(top_srcdir)/case_utils/ontology/version_info.py \
  subclass.json \
  subclass.sparql
	source $(tests_srcdir)/venv/bin/activate \
	  && case_sparql_select \
	    --json-indent 4 \
	    --use-prefixes \
	    _$@ \
	    subclass.sparql \
	    subclass.json
	mv _$@ $@

subclass-explicit-none.md: \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/case_utils/case_sparql_select/__init__.py \
  $(top_srcdir)/case_utils/ontology/__init__.py \
  $(top_srcdir)/case_utils/ontology/version_info.py \
  subclass.json \
  subclass.sparql
	source $(tests_srcdir)/venv/bin/activate \
	  && case_sparql_select \
	    --built-version none \
	    _$@ \
	    subclass.sparql \
	    subclass.json
	mv _$@ $@

subclass-implicit-any.md: \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/case_utils/case_sparql_select/__init__.py \
  $(top_srcdir)/case_utils/ontology/__init__.py \
  $(top_srcdir)/case_utils/ontology/version_info.py \
  subclass.json \
  subclass.sparql
	source $(tests_srcdir)/venv/bin/activate \
	  && case_sparql_select \
	    _$@ \
	    subclass.sparql \
	    subclass.json
	mv _$@ $@

w3-output.%: \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/case_utils/case_sparql_select/__init__.py \
  $(top_srcdir)/case_utils/ontology/__init__.py \
  $(top_srcdir)/case_utils/ontology/version_info.py \
  w3-input-1.sparql \
  w3-input-2.ttl \
  w3-input-3.json
	source $(tests_srcdir)/venv/bin/activate \
	  && case_sparql_select \
	    _$@ \
	    w3-input-1.sparql \
	    w3-input-2.ttl \
	    w3-input-3.json
	mv _$@ $@

w3-output-indented.json: \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/case_utils/case_sparql_select/__init__.py \
  $(top_srcdir)/case_utils/ontology/__init__.py \
  $(top_srcdir)/case_utils/ontology/version_info.py \
  w3-input-1.sparql \
  w3-input-2.ttl \
  w3-input-3.json
	source $(tests_srcdir)/venv/bin/activate \
	  && case_sparql_select \
	    --json-indent 4 \
	    _$@ \
	    w3-input-1.sparql \
	    w3-input-2.ttl \
	    w3-input-3.json
	mv _$@ $@

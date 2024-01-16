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
  subclass-explicit-none.ttl \
  subclass-implicit-any.ttl \
  w3-output.json \
  w3-output.ttl

check: \
  subclass-explicit-none.ttl \
  subclass-implicit-any.ttl \
  w3-output.json \
  w3-output.ttl
	source $(tests_srcdir)/venv/bin/activate \
	  && pytest \
	    --log-level=DEBUG

clean:
	@rm -rf \
	  __pycache__
	@rm -f \
	  output.* \
	  _*

subclass-explicit-none.ttl: \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/case_utils/case_sparql_construct/__init__.py \
  $(top_srcdir)/case_utils/ontology/__init__.py \
  $(top_srcdir)/case_utils/ontology/version_info.py \
  subclass.json \
  subclass.sparql
	source $(tests_srcdir)/venv/bin/activate \
	  && case_sparql_construct \
	    --built-version none \
	    _$@ \
	    subclass.sparql \
	    subclass.json
	mv _$@ $@

subclass-implicit-any.ttl: \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/case_utils/case_sparql_construct/__init__.py \
  $(top_srcdir)/case_utils/ontology/__init__.py \
  $(top_srcdir)/case_utils/ontology/version_info.py \
  subclass.json \
  subclass.sparql
	source $(tests_srcdir)/venv/bin/activate \
	  && case_sparql_construct \
	    _$@ \
	    subclass.sparql \
	    subclass.json
	mv _$@ $@

w3-output.%: \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/case_utils/case_sparql_construct/__init__.py \
  $(top_srcdir)/case_utils/ontology/__init__.py \
  $(top_srcdir)/case_utils/ontology/version_info.py \
  w3-input-1.sparql \
  w3-input-2.ttl \
  w3-input-3.json
	source $(tests_srcdir)/venv/bin/activate \
	  && case_sparql_construct \
	    _$@ \
	    w3-input-1.sparql \
	    w3-input-2.ttl \
	    w3-input-3.json
	mv _$@ $@

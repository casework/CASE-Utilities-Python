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

top_srcdir := $(shell cd ../.. ; pwd)

tests_srcdir := $(top_srcdir)/tests

all:

check: \
  check-g1-g2.done.log \
  check-g1-g3.done.log \
  check-g1j-g1j.done.log \
  check-g1j-g1t.done.log \
  check-g1t-g1t.done.log \
  rdfgraphisomorphism.done.log

check-g1-g2.done.log: \
  $(tests_srcdir)/.venv.done.log \
  $(tests_srcdir)/src/isomorphic_diff.py \
  rdflib_compare_isomorphic_docstring_g1.ttl \
  rdflib_compare_isomorphic_docstring_g2.ttl
	source $(tests_srcdir)/venv/bin/activate \
	  && python3 $(tests_srcdir)/src/isomorphic_diff.py \
	    --debug \
	    rdflib_compare_isomorphic_docstring_g1.ttl \
	    rdflib_compare_isomorphic_docstring_g2.ttl
	touch $@

check-g1-g3.done.log: \
  $(tests_srcdir)/.venv.done.log \
  $(tests_srcdir)/src/isomorphic_diff.py \
  rdflib_compare_isomorphic_docstring_g1.ttl \
  rdflib_compare_isomorphic_docstring_g3.ttl
	source $(tests_srcdir)/venv/bin/activate \
	  && python3 $(tests_srcdir)/src/isomorphic_diff.py \
	    --debug \
	    rdflib_compare_isomorphic_docstring_g1.ttl \
	    rdflib_compare_isomorphic_docstring_g3.ttl \
	    || true #XFAIL
	touch $@

check-g1j-g1j.done.log: \
  $(tests_srcdir)/.venv.done.log \
  $(tests_srcdir)/src/isomorphic_diff.py \
  rdflib_compare_isomorphic_docstring_g1.json \
  rdflib_compare_isomorphic_docstring_g1.json
	source $(tests_srcdir)/venv/bin/activate \
	  && python3 $(tests_srcdir)/src/isomorphic_diff.py \
	    --debug \
	    rdflib_compare_isomorphic_docstring_g1.json \
	    rdflib_compare_isomorphic_docstring_g1.json
	touch $@

check-g1j-g1t.done.log: \
  $(tests_srcdir)/.venv.done.log \
  $(tests_srcdir)/src/isomorphic_diff.py \
  rdflib_compare_isomorphic_docstring_g1.json \
  rdflib_compare_isomorphic_docstring_g1.ttl
	source $(tests_srcdir)/venv/bin/activate \
	  && python3 $(tests_srcdir)/src/isomorphic_diff.py \
	    --debug \
	    rdflib_compare_isomorphic_docstring_g1.json \
	    rdflib_compare_isomorphic_docstring_g1.ttl
	touch $@

check-g1t-g1t.done.log: \
  $(tests_srcdir)/.venv.done.log \
  $(tests_srcdir)/src/isomorphic_diff.py \
  rdflib_compare_isomorphic_docstring_g1.ttl \
  rdflib_compare_isomorphic_docstring_g1.ttl
	source $(tests_srcdir)/venv/bin/activate \
	  && python3 $(tests_srcdir)/src/isomorphic_diff.py \
	    --debug \
	    rdflib_compare_isomorphic_docstring_g1.ttl \
	    rdflib_compare_isomorphic_docstring_g1.ttl
	touch $@

clean:
	@rm -f \
	  check-*.done.log \
	  rdfgraphisomorphism.*.log

rdfgraphisomorphism.done.log: \
  $(tests_srcdir)/.venv.done.log \
  rdflib_compare_isomorphic_docstring_g1.ttl \
  rdflib_compare_isomorphic_docstring_g2.ttl
	source $(tests_srcdir)/venv/bin/activate \
	  && rdfgraphisomorphism \
	    --format n3 \
	    rdflib_compare_isomorphic_docstring_g1.ttl \
	    rdflib_compare_isomorphic_docstring_g2.ttl \
	    ; echo $$? > rdfgraphisomorphism.status.log
	# This test is an XFAIL - rdflib at 5.0.0 has an error running this program.
	test 0 -ne $$(head -n1 rdfgraphisomorphism.status.log)
	touch $@

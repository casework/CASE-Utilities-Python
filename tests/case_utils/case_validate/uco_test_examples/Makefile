#!/usr/bin/make -f

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

SHELL := /bin/bash

top_srcdir := $(shell cd ../../../.. ; pwd)

case_srcdir := $(top_srcdir)/dependencies/CASE

uco_srcdir := $(case_srcdir)/dependencies/UCO

examples_srcdir := $(uco_srcdir)/tests/examples

tests_srcdir := $(top_srcdir)/tests

RDF_TOOLKIT_JAR := $(uco_srcdir)/lib/rdf-toolkit.jar

validation_ttls := \
  action_inheritance_PASS_validation.ttl \
  action_inheritance_XFAIL_validation.ttl \
  action_result_PASS_validation.ttl \
  co_PASS_validation.ttl \
  co_XFAIL_validation.ttl \
  configuration_setting_PASS_validation.ttl \
  configuration_setting_XFAIL_validation.ttl \
  database_records_PASS_validation.ttl \
  database_records_XFAIL_validation.ttl \
  has_facet_inverse_functional_PASS_validation.ttl \
  has_facet_inverse_functional_XFAIL_validation.ttl \
  hash_PASS_validation.ttl \
  hash_XFAIL_validation.ttl \
  location_PASS_validation.ttl \
  location_XFAIL_validation.ttl \
  message_thread_PASS_validation.ttl \
  message_thread_XFAIL_validation.ttl \
  observable_creation_time_PASS_validation.ttl \
  owl_axiom_PASS_validation.ttl \
  owl_axiom_XFAIL_validation.ttl \
  owl_properties_PASS_validation.ttl \
  owl_properties_XFAIL_validation.ttl \
  rdf_list_PASS_validation.ttl \
  rdf_list_XFAIL_validation.ttl \
  relationship_PASS_validation.ttl \
  relationship_XFAIL_validation.ttl \
  relationship_XFAIL_validation.ttl \
  thread_PASS_validation.ttl \
  thread_XFAIL_validation.ttl

all: \
  $(validation_ttls)

.PRECIOUS: \
  %_validation.ttl

# NOTE - this recipe makes an allowance for a certain failure type
# reported by pyshacl.  Pyshacl will exit status 1 in the case where
# "DataGraph is Non-Conformant".  XFAIL tests are intended to
# generate a non-conformance result, and feed that result forward to
# pytest.  Hence, the Make recipe allows for an exit status of 0 or 1.
# (0 would cause an expected failure later in pytest.)
# Note that should another issue cause an exit status of 1, pytest will
# fail because the result validation-graph file would not have expected
# characteristics.
%_validation.ttl: \
  $(examples_srcdir)/%.json \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/.ontology.done.log \
  $(top_srcdir)/case_utils/case_validate/__init__.py \
  $(top_srcdir)/case_utils/ontology/__init__.py
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --allow-warnings \
	    --debug \
	    --format turtle \
	    $< \
	    > __$@ \
	    ; rc=$$? ; test 0 -eq $$rc -o 1 -eq $$rc
	@#Fail if output is empty.
	@test -s __$@ \
	  || exit 1
	java -jar $(RDF_TOOLKIT_JAR) \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

check: \
  $(validation_ttls)
	source $(tests_srcdir)/venv/bin/activate \
	  && pytest \
	    --log-level=DEBUG

clean:
	@rm -f \
	  *_validation.ttl

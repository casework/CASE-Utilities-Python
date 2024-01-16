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

top_srcdir := $(shell cd ../../../.. ; pwd)

case_srcdir := $(top_srcdir)/dependencies/CASE

examples_srcdir := $(case_srcdir)/tests/examples

tests_srcdir := $(top_srcdir)/tests

RDF_TOOLKIT_JAR := $(case_srcdir)/lib/rdf-toolkit.jar

case_validate_sources := \
  $(top_srcdir)/case_utils/case_validate/__init__.py \
  $(top_srcdir)/case_utils/case_validate/validate_types.py \
  $(top_srcdir)/case_utils/case_validate/validate_utils.py

files_to_generate := \
  errant_cdo_concept_PASS.txt \
  errant_cdo_concept_XFAIL.txt \
  format_human_output_jsonld.jsonld \
  format_human_output_turtle.ttl \
  format_human_output_txt.txt \
  format_human_output_unspecified.txt \
  format_jsonld_output_jsonld.jsonld \
  format_jsonld_output_turtle.ttl \
  format_jsonld_output_txt.txt \
  format_jsonld_output_unspecified.jsonld \
  format_turtle_output_jsonld.jsonld \
  format_turtle_output_turtle.ttl \
  format_turtle_output_txt.txt \
  format_turtle_output_unspecified.ttl \
  format_unspecified_output_jsonld.jsonld \
  format_unspecified_output_turtle.ttl \
  format_unspecified_output_txt.txt \
  format_unspecified_output_unspecified.txt \
  past_version_reference_PASS.txt \
  past_version_reference_XFAIL.txt \
  split_data_graph_PASS.txt \
  split_data_graph_XFAIL.txt \
  thing_metashacl_PASS.txt

all: \
  $(files_to_generate)

check: \
  $(files_to_generate)
	source $(tests_srcdir)/venv/bin/activate \
	  && pytest \
	    --log-level=DEBUG

clean:
	@rm -f \
	  $(files_to_generate)

errant_cdo_concept_PASS.txt: \
  $(case_validate_sources) \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/.ontology.done.log \
  $(top_srcdir)/case_utils/ontology/__init__.py \
  errant_cdo_concept.ttl
	rm -f _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --allow-warnings \
	    --debug \
	    errant_cdo_concept.ttl \
	    > _$@
	mv _$@ $@

errant_cdo_concept_XFAIL.txt: \
  $(case_validate_sources) \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/.ontology.done.log \
  $(top_srcdir)/case_utils/ontology/__init__.py \
  errant_cdo_concept.ttl
	rm -f _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    errant_cdo_concept.ttl \
	    --debug \
	    > _$@ \
	    ; test 1 -eq $$?
	test -s _$@
	mv _$@ $@

format_human_output_%: \
  $(examples_srcdir)/investigative_action_PASS_validation.ttl \
  $(case_validate_sources) \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/.ontology.done.log \
  $(top_srcdir)/case_utils/ontology/__init__.py
	rm -f _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --debug \
	    --format human \
	    --output _$@ \
	    $<
	mv _$@ $@

format_human_output_unspecified.txt: \
  $(examples_srcdir)/investigative_action_PASS_validation.ttl \
  $(case_validate_sources) \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/.ontology.done.log \
  $(top_srcdir)/case_utils/ontology/__init__.py
	rm -f _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --debug \
	    --format human \
	    $< \
	    > _$@
	mv _$@ $@

# JSON-LD recipes contain a sed command to remove a randomly-valued
# blank node ID that does not serve to inform the example.
format_jsonld_output_%: \
  $(examples_srcdir)/investigative_action_PASS_validation.ttl \
  $(case_validate_sources) \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/.ontology.done.log \
  $(top_srcdir)/case_utils/ontology/__init__.py
	rm -f __$@ _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --debug \
	    --format json-ld \
	    --output __$@ \
	    $<
	sed \
	  -e '/"@id": "_:/d' \
	  __$@ \
	  > _$@
	rm -f __$@
	mv _$@ $@

format_jsonld_output_unspecified.jsonld: \
  $(examples_srcdir)/investigative_action_PASS_validation.ttl \
  $(case_validate_sources) \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/.ontology.done.log \
  $(top_srcdir)/case_utils/ontology/__init__.py
	rm -f __$@ _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --debug \
	    --format json-ld \
	    $< \
	    > __$@
	sed \
	  -e '/"@id": "_:/d' \
	  __$@ \
	  > _$@
	rm -f __$@
	mv _$@ $@

format_turtle_output_%: \
  $(examples_srcdir)/investigative_action_PASS_validation.ttl \
  $(case_validate_sources) \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/.ontology.done.log \
  $(top_srcdir)/case_utils/ontology/__init__.py
	rm -f _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --debug \
	    --format turtle \
	    --output _$@ \
	    $<
	mv _$@ $@

format_turtle_output_unspecified.ttl: \
  $(examples_srcdir)/investigative_action_PASS_validation.ttl \
  $(case_validate_sources) \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/.ontology.done.log \
  $(top_srcdir)/case_utils/ontology/__init__.py
	rm -f _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --debug \
	    --format turtle \
	    $< \
	    > _$@
	mv _$@ $@

format_unspecified_output_%: \
  $(examples_srcdir)/investigative_action_PASS_validation.ttl \
  $(case_validate_sources) \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/.ontology.done.log \
  $(top_srcdir)/case_utils/ontology/__init__.py
	rm -f _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --debug \
	    --output _$@ \
	    $<
	mv _$@ $@

format_unspecified_output_unspecified.txt: \
  $(examples_srcdir)/investigative_action_PASS_validation.ttl \
  $(case_validate_sources) \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/.ontology.done.log \
  $(top_srcdir)/case_utils/ontology/__init__.py
	rm -f _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --debug \
	    $< \
	    > _$@
	mv _$@ $@

past_version_reference_PASS.txt: \
  $(case_validate_sources) \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/.ontology.done.log \
  $(top_srcdir)/case_utils/ontology/__init__.py \
  $(top_srcdir)/case_utils/ontology/ontology_and_version_iris.txt \
  past_version_reference_PASS.ttl
	rm -f _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    past_version_reference_PASS.ttl \
	    > _$@
	mv _$@ $@

past_version_reference_XFAIL.txt: \
  $(case_validate_sources) \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/.ontology.done.log \
  $(top_srcdir)/case_utils/ontology/__init__.py \
  $(top_srcdir)/case_utils/ontology/ontology_and_version_iris.txt \
  past_version_reference_XFAIL.ttl
	rm -f _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    past_version_reference_XFAIL.ttl \
	    > _$@ \
	    ; rc=$$? ; test 1 -eq $$rc
	test -s _$@
	mv _$@ $@

split_data_graph_PASS.txt: \
  $(case_validate_sources) \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/.ontology.done.log \
  $(top_srcdir)/case_utils/ontology/__init__.py \
  split_data_graph_1.json \
  split_data_graph_2.json
	rm -f _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --debug \
	    split_data_graph_1.json \
	    split_data_graph_2.json \
	    > _$@
	mv _$@ $@

split_data_graph_XFAIL.txt: \
  $(case_validate_sources) \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/.ontology.done.log \
  $(top_srcdir)/case_utils/ontology/__init__.py \
  split_data_graph_1.json
	rm -f _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --debug \
	    split_data_graph_1.json \
	    > _$@ \
	    ; rc=$$? ; test 1 -eq $$rc
	test -s _$@
	mv _$@ $@

thing_metashacl_PASS.txt: \
  $(case_validate_sources) \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/.ontology.done.log \
  $(top_srcdir)/case_utils/ontology/__init__.py \
  thing.ttl
	rm -f _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --metashacl \
	    thing.ttl \
	    > _$@
	mv _$@ $@

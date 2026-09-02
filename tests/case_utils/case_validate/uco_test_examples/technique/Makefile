#!/usr/bin/make -f

# Portions of this file contributed by NIST are governed by the
# following statement:
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

top_srcdir := $(shell cd ../../../../.. ; pwd)

uco_srcdir := $(top_srcdir)/dependencies/CASE/dependencies/UCO

technique_srcdir := $(uco_srcdir)/tests/examples/technique

tests_srcdir := $(top_srcdir)/tests

RDF_TOOLKIT_JAR := $(uco_srcdir)/lib/rdf-toolkit.jar

validation_ttls := \
  technique_ontology_XFAIL_validation.ttl \
  technique_ontology_XFAIL_rdfs_validation.ttl \
  technique_ontology_XFAIL_owlrl_validation.ttl \
  technique_data_PASS_validation.ttl \
  technique_data_XFAIL_validation.ttl

all: \
  $(validation_ttls)

.PRECIOUS: \
  %_validation.ttl

check: \
  $(validation_ttls)

clean:
	@rm -f \
	  *_validation.ttl \
	  _* \
	  generated-* 

generated-shapes.ttl: \
  $(technique_srcdir)/technique_shapes_PASS.ttl \
  $(tests_srcdir)/.venv.done.log \
  $(uco_srcdir)/tests/thing.ttl
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --format turtle \
	    --metashacl \
	    --ontology-graph $(technique_srcdir)/technique_shapes_PASS.ttl \
	    --review-tbox \
	    $(uco_srcdir)/tests/thing.ttl
	cp \
	  $(technique_srcdir)/technique_shapes_PASS.ttl \
	  $@

generated-tbox.ttl: \
  $(technique_srcdir)/technique_ontology_PASS.ttl \
  generated-shapes.ttl
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --format turtle \
	    --ontology-graph generated-shapes.ttl \
	    --review-tbox \
	    $(technique_srcdir)/technique_ontology_PASS.ttl
	cp \
	  $(technique_srcdir)/technique_ontology_PASS.ttl \
	  $@

technique_data_PASS_validation.ttl: \
  $(technique_srcdir)/technique_data_PASS.json \
  generated-tbox.ttl
	rm -f \
	  __$@ \
	  _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --format turtle \
	    --ontology-graph generated-shapes.ttl \
	    --ontology-graph generated-tbox.ttl \
	    --output __$@ \
	    $(technique_srcdir)/technique_data_PASS.json
	java -jar $(RDF_TOOLKIT_JAR) \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

technique_data_XFAIL_validation.ttl: \
  $(technique_srcdir)/technique_data_XFAIL.json \
  generated-tbox.ttl
	rm -f \
	  __$@ \
	  _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --format turtle \
	    --ontology-graph generated-shapes.ttl \
	    --ontology-graph generated-tbox.ttl \
	    --output __$@ \
	    $(technique_srcdir)/technique_data_XFAIL.json \
	    ; test 1 -eq $$?
	java -jar $(RDF_TOOLKIT_JAR) \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

technique_ontology_XFAIL_owlrl_validation.ttl: \
  $(technique_srcdir)/technique_ontology_XFAIL.ttl \
  generated-shapes.ttl
	rm -f \
	  __$@ \
	  _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --format turtle \
	    --inference owlrl \
	    --ontology-graph generated-shapes.ttl \
	    --output __$@ \
	    --review-tbox \
	    $(technique_srcdir)/technique_ontology_XFAIL.ttl \
	    ; test 1 -eq $$?
	java -jar $(RDF_TOOLKIT_JAR) \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

technique_ontology_XFAIL_rdfs_validation.ttl: \
  $(technique_srcdir)/technique_ontology_XFAIL.ttl \
  generated-shapes.ttl
	rm -f \
	  __$@ \
	  _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --format turtle \
	    --inference rdfs \
	    --ontology-graph generated-shapes.ttl \
	    --output __$@ \
	    --review-tbox \
	    $(technique_srcdir)/technique_ontology_XFAIL.ttl \
	    ; test 1 -eq $$?
	java -jar $(RDF_TOOLKIT_JAR) \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

technique_ontology_XFAIL_validation.ttl: \
  $(technique_srcdir)/technique_ontology_XFAIL.ttl \
  generated-shapes.ttl
	rm -f \
	  __$@ \
	  _$@
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --format turtle \
	    --ontology-graph generated-shapes.ttl \
	    --output __$@ \
	    --review-tbox \
	    $(technique_srcdir)/technique_ontology_XFAIL.ttl \
	    ; test 1 -eq $$?
	java -jar $(RDF_TOOLKIT_JAR) \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

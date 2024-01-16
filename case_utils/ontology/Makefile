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

case_srcdir := $(top_srcdir)/dependencies/CASE

uco_srcdir := $(case_srcdir)/dependencies/UCO

RDF_TOOLKIT_JAR := $(uco_srcdir)/lib/rdf-toolkit.jar

case_version := $(shell python3 version_info.py)

all: \
  ontology_and_version_iris.txt

.PRECIOUS: \
  case-$(case_version).ttl

$(case_srcdir)/.venv.done.log: \
  $(top_srcdir)/.git_submodule_init.done.log
	$(MAKE) \
	  --directory $(case_srcdir) \
	    .venv.done.log
	touch -c $@
	test -r $@

# Build monolith including transitive import closure outside of
# CDO-maintained ontologies, removing need for network retrieval for
# non-CDO class and property definitions.
case-$(case_version).ttl: \
  $(case_srcdir)/.venv.done.log \
  $(RDF_TOOLKIT_JAR)
	$(MAKE) \
	  --directory $(case_srcdir)/tests \
	    case_monolithic.ttl
	source $(case_srcdir)/venv/bin/activate \
	  && rdfpipe \
	    --output-format turtle \
	    $(case_srcdir)/tests/case_monolithic.ttl \
	    $(uco_srcdir)/dependencies/collections-ontology/collections.owl \
	    $(uco_srcdir)/dependencies/error/docs/current/error.ttl \
	    > __$@
	java -jar $(RDF_TOOLKIT_JAR) \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

case-$(case_version)-subclasses.ttl: \
  case-$(case_version).ttl \
  src/subclasses_ttl.py
	# The CASE ontology test venv is made by the earlier build step
	# of case_monolithic.ttl.  However, unless a new ontology
	# release is being made, that step will have been skipped.
	# This recursive Make call guarantees the virtual environment is
	# set up.
	source $(case_srcdir)/venv/bin/activate \
	  && python3 src/subclasses_ttl.py \
	  __$@ \
	 $<
	java -jar $(RDF_TOOLKIT_JAR) \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

clean:
	@rm -f \
	  case-$(case_version)*.ttl

ontology_and_version_iris.txt: \
  src/ontology_and_version_iris.py \
  case-$(case_version)-subclasses.ttl
	source $(case_srcdir)/venv/bin/activate \
	  && python3 src/ontology_and_version_iris.py \
	    _$@ \
	    case-*.ttl
	mv _$@ $@

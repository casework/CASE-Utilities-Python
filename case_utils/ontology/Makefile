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

top_srcdir := $(shell cd ../.. ; pwd)

case_srcdir := $(top_srcdir)/dependencies/CASE

uco_srcdir := $(case_srcdir)/dependencies/UCO

RDF_TOOLKIT_JAR := $(uco_srcdir)/lib/rdf-toolkit.jar

case_version := $(shell python3 version_info.py)

all: \
  ontology_and_version_iris.txt

.PRECIOUS: \
  case-$(case_version).ttl

case-$(case_version).ttl: \
  $(top_srcdir)/.git_submodule_init.done.log \
  $(RDF_TOOLKIT_JAR)
	$(MAKE) \
	  --directory $(case_srcdir)/tests \
	    case_monolithic.ttl
	cp \
	  $(case_srcdir)/tests/case_monolithic.ttl \
	  $@

case-$(case_version)-subclasses.ttl: \
  case-$(case_version).ttl \
  src/subclasses_ttl.py
	# The CASE ontology test venv is made by the earlier build step
	# of case_monolithic.ttl.  However, unless a new ontology
	# release is being made, that step will have been skipped.
	# This recursive Make call guarantees the virtual environment is
	# set up.
	$(MAKE) \
	  --directory $(case_srcdir)/tests \
	    .venv.done.log
	source $(case_srcdir)/tests/venv/bin/activate \
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
	# Guarantee venv is built.  (Same rationale as in the subclasses.ttl recipe.)
	$(MAKE) \
	  --directory $(case_srcdir)/tests \
	    .venv.done.log
	source $(case_srcdir)/tests/venv/bin/activate \
	  && python3 src/ontology_and_version_iris.py \
	    _$@ \
	    case-*.ttl
	mv _$@ $@

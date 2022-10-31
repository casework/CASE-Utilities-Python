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

PYTHON3 ?= python3

tests_srcdir := $(top_srcdir)/tests

all: \
  all-case_file \
  all-case_sparql_construct \
  all-case_sparql_select \
  all-case_validate

.PHONY: \
  all-case_file \
  all-case_sparql_construct \
  all-case_sparql_select \
  all-case_validate \
  check-case_file \
  check-case_sparql_construct \
  check-case_sparql_select \
  check-case_validate

all-case_file: \
  $(tests_srcdir)/.venv.done.log
	$(MAKE) \
	  --directory case_file

all-case_sparql_construct: \
  $(tests_srcdir)/.venv.done.log
	$(MAKE) \
	  --directory case_sparql_construct

all-case_sparql_select: \
  $(tests_srcdir)/.venv.done.log
	$(MAKE) \
	  --directory case_sparql_select

all-case_validate: \
  $(tests_srcdir)/.venv.done.log
	$(MAKE) \
	  PYTHON3=$(PYTHON3) \
	  --directory case_validate

check: \
  check-case_file \
  check-case_sparql_construct \
  check-case_sparql_select \
  check-case_validate
	source $(tests_srcdir)/venv/bin/activate \
	  && pytest \
	    --ignore case_file \
	    --ignore case_sparql_construct \
	    --ignore case_validate \
	    --log-level=DEBUG

check-case_file: \
  $(tests_srcdir)/.venv.done.log
	$(MAKE) \
	  --directory case_file \
	  check

check-case_sparql_construct: \
  $(tests_srcdir)/.venv.done.log
	$(MAKE) \
	  --directory case_sparql_construct \
	  check

check-case_sparql_select: \
  $(tests_srcdir)/.venv.done.log
	$(MAKE) \
	  --directory case_sparql_select \
	  check

check-case_validate: \
  $(tests_srcdir)/.venv.done.log
	$(MAKE) \
	  PYTHON3=$(PYTHON3) \
	  --directory case_validate \
	  check

clean:
	@$(MAKE) \
	  PYTHON3=$(PYTHON3) \
	  --directory case_validate \
	  clean
	@$(MAKE) \
	  --directory case_sparql_select \
	  clean
	@$(MAKE) \
	  --directory case_sparql_construct \
	  clean
	@$(MAKE) \
	  --directory case_file \
	  clean

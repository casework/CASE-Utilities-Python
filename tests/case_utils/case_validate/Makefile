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

PYTHON3 ?= python3

case_version := $(shell $(PYTHON3) $(top_srcdir)/case_utils/ontology/version_info.py)
ifeq ($(case_version),)
$(error Unable to determine CASE version)
endif

tests_srcdir := $(top_srcdir)/tests

all: \
  all-cli \
  all-case_test_examples \
  all-uco_test_examples \
  all-shape_disabling

.PHONY: \
  all-case_test_examples \
  all-cli \
  all-shape_disabling \
  all-uco_test_examples \
  check-case_test_examples \
  check-cli \
  check-shape_disabling \
  check-uco_test_examples

all-case_test_examples:
	$(MAKE) \
	  --directory case_test_examples

all-cli:
	$(MAKE) \
	  --directory cli

all-shape_disabling:
	$(MAKE) \
	  --directory shape_disabling

all-uco_test_examples:
	$(MAKE) \
	  --directory uco_test_examples

check: \
  check-cli \
  check-case_test_examples \
  check-uco_test_examples \
  check-shape_disabling

check-case_test_examples:
	$(MAKE) \
	  --directory case_test_examples \
	  check

check-cli:
	$(MAKE) \
	  --directory cli \
	  check

check-shape_disabling:
	$(MAKE) \
	  --directory shape_disabling \
	  check

check-uco_test_examples: \
  uco_monolithic.ttl
	$(MAKE) \
	  --directory uco_test_examples \
	  check

clean:
	@$(MAKE) \
	  --directory shape_disabling \
	  clean
	@$(MAKE) \
	  --directory case_test_examples \
	  clean
	@$(MAKE) \
	  --directory uco_test_examples \
	  clean
	@$(MAKE) \
	  --directory cli \
	  clean

# This file is necessary for a UCO unit test that case-utils runs
# substituting its own monolithic build.
# It is incorrect to designate this the "UCO" monolithic build due to
# CASE concepts being present, but using the CASE build here keeps with
# the spirit of confirming UCO tests continue to pass when using the
# CASE monolithic build.
uco_monolithic.ttl: \
  $(top_srcdir)/case_utils/ontology/version_info.py \
  $(top_srcdir)/case_utils/ontology/case-$(case_version).ttl
	rm -f $@
	cp \
	  $(top_srcdir)/case_utils/ontology/case-$(case_version).ttl \
	  $@

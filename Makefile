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

PYTHON3 ?= python3

case_version := $(shell $(PYTHON3) case_utils/ontology/version_info.py)
ifeq ($(case_version),)
$(error Unable to determine CASE version)
endif

all: \
  .ontology.done.log

.PHONY: \
  download

.git_submodule_init.done.log: \
  .gitmodules
	# Log current submodule pointers.
	cd dependencies \
	  && git diff . \
	    | cat
	test -r dependencies/CASE/ontology/master/case.ttl \
	  || (git submodule init dependencies/CASE && git submodule update dependencies/CASE)
	test -r dependencies/CASE/ontology/master/case.ttl
	$(MAKE) \
	  --directory dependencies/CASE \
	  .git_submodule_init.done.log \
	  .lib.done.log
	touch $@

.ontology.done.log: \
  dependencies/CASE/ontology/master/case.ttl
	# Do not rebuild the current ontology file if it is already present.  It is expected not to change once built.
	# touch -c: Do not create the file if it does not exist.  This will convince the recursive make nothing needs to be done if the file is present.
	touch -c case_utils/ontology/case-$(case_version).ttl
	touch -c case_utils/ontology/case-$(case_version)-subclasses.ttl
	$(MAKE) \
	  --directory case_utils/ontology
	# Confirm the current monolithic file is in place.
	test -r case_utils/ontology/case-$(case_version).ttl
	test -r case_utils/ontology/case-$(case_version)-subclasses.ttl
	touch $@

check: \
  .ontology.done.log
	$(MAKE) \
	  PYTHON3=$(PYTHON3) \
	  --directory tests \
	  check

clean:
	@$(MAKE) \
	  --directory tests \
	  clean
	@rm -f \
	  .*.done.log
	@# 'clean' in the ontology directory should only happen when testing and building new ontology versions.  Hence, it is not called from the top-level Makefile.
	@test ! -r dependencies/CASE/README.md \
	  || $(MAKE) \
	    --directory dependencies/CASE \
	    clean
	@# Restore CASE validation output files that do not affect CASE build process.
	@test ! -r dependencies/CASE/README.md \
	  || ( \
	    cd dependencies/CASE \
	      && git checkout \
	        -- \
	        tests/examples \
	        || true \
	  )

# This recipe guarantees timestamp update order, and is otherwise intended to be a no-op.
dependencies/CASE/ontology/master/case.ttl: \
  .git_submodule_init.done.log
	test -r $@
	touch $@

distclean: \
  clean
	@rm -rf \
	  build \
	  *.egg-info \
	  dist

download: \
  .git_submodule_init.done.log
	$(MAKE) \
	  --directory tests \
	  download

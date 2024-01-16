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

top_srcdir := $(shell cd .. ; pwd)

PYTHON3 ?= python3

all: \
  all-case_utils

.PHONY: \
  all-case_utils \
  check-case_utils \
  check-doctest \
  check-isomorphic_diff \
  check-mypy \
  download

.venv.done.log: \
  $(top_srcdir)/.git_submodule_init.done.log \
  $(top_srcdir)/case_utils/__init__.py \
  $(top_srcdir)/setup.cfg \
  $(top_srcdir)/setup.py
	rm -rf venv
	$(PYTHON3) -m venv \
	  venv
	source venv/bin/activate \
	  && pip install \
	    --upgrade \
	    pip \
	    setuptools \
	    wheel
	source venv/bin/activate \
	  && cd $(top_srcdir) \
	    && pip install \
	      --editable \
	      .[testing]
	touch $@

all-case_utils: \
  .venv.done.log
	$(MAKE) \
	  PYTHON3=$(PYTHON3) \
	  --directory case_utils

# These check calls are provided in preferred run-order.
check: \
  check-mypy \
  check-doctest \
  check-isomorphic_diff \
  check-case_utils
	source venv/bin/activate \
	  && pytest \
	    --ignore case_utils \
	    --log-level=DEBUG

check-case_utils: \
  .venv.done.log
	$(MAKE) \
	  PYTHON3=$(PYTHON3) \
	  --directory case_utils \
	  check

check-doctest: \
  .venv.done.log
	source venv/bin/activate \
	  && pytest \
	    --doctest-modules \
	    --log-level=DEBUG \
	    $(top_srcdir)/case_utils

check-isomorphic_diff: \
  .venv.done.log
	$(MAKE) \
	  --directory isomorphic_diff \
	  check

# TODO - Add and strict-check type signatures for CASE and UCO tests.
check-mypy: \
  .venv.done.log
	source venv/bin/activate \
	  && mypy \
	    --exclude case_utils/case_validate/case_test_examples/test_case_validation.py \
	    --exclude case_utils/case_validate/uco_test_examples/test_uco_validation.py \
	    --exclude venv \
	    --strict \
	    $(top_srcdir)/case_utils \
	    .

clean:
	@$(MAKE) \
	  PYTHON3=$(PYTHON3) \
	  --directory case_utils \
	  clean
	@rm -f \
	  .venv.done.log
	@rm -rf \
	  .pytest_cache \
	  venv

download: \
  .venv.done.log

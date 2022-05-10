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

top_srcdir := $(shell cd .. ; pwd)

PYTHON3 ?= python3

all: \
  all-case_utils

.PHONY: \
  all-case_utils \
  check-case_utils \
  check-isomorphic_diff \
  check-mypy \
  download

.venv.done.log: \
  $(top_srcdir)/.git_submodule_init.done.log \
  $(top_srcdir)/case_utils/__init__.py \
  $(top_srcdir)/setup.cfg \
  $(top_srcdir)/setup.py \
  requirements.txt
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
	  && pip install \
	    --requirement requirements.txt
	source venv/bin/activate \
	  && pip install \
	    $(top_srcdir)/dependencies/rdflib
	source venv/bin/activate \
	  && cd $(top_srcdir) \
	    && pip install \
	      --editable \
	      .
	touch $@

all-case_utils: \
  .venv.done.log
	$(MAKE) \
	  --directory case_utils

# These check calls are provided in preferred run-order.
check: \
  check-mypy \
  check-isomorphic_diff \
  check-case_utils
	source venv/bin/activate \
	  && pytest \
	    --ignore case_utils \
	    --log-level=DEBUG

check-case_utils: \
  .venv.done.log
	$(MAKE) \
	  --directory case_utils \
	  check

check-isomorphic_diff: \
  .venv.done.log
	$(MAKE) \
	  --directory isomorphic_diff \
	  check

# mypy is called against specific members of the tests directory to avoid descending into the virtual environment.
# TODO - Fix type signatures in UCO test.
check-mypy: \
  .venv.done.log
	source venv/bin/activate \
	  && mypy \
	    --exclude case_utils/case_validate/uco_test_examples/test_uco_validation.py \
	    $(top_srcdir)/case_utils \
	    case_utils \
	    hexbinary \
	    src

clean:
	@$(MAKE) \
	  --directory case_utils \
	  clean
	@rm -f \
	  .venv.done.log
	@rm -rf \
	  .pytest_cache \
	  venv

download: \
  .venv.done.log

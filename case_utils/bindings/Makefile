#!/usr/bin/env python3

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

all: \
  __init__.py

__init__.py: \
  $(top_srcdir)/tests/.venv.done.log \
  autogen.py
	source $(top_srcdir)/tests/venv/bin/activate \
	  && mypy \
	    --strict \
	    autogen.py
	source $(top_srcdir)/tests/venv/bin/activate \
	  && python3 autogen.py \
	    > _$@
	source $(top_srcdir)/tests/venv/bin/activate \
	  && black \
	    _$@
	source $(top_srcdir)/tests/venv/bin/activate \
	  && mypy \
	    --strict \
	    _$@
	mv _$@ $@

clean:
	@rm -f \
	  __init__.py

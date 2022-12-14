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

top_srcdir := $(shell cd ../../../.. ; pwd)

tests_srcdir := $(top_srcdir)/tests

all: \
  validation_with_uuid_shape_disabled.txt \
  validation_with_uuid_shape_enabled.txt

check: \
  validation_with_uuid_shape_disabled.txt \
  validation_with_uuid_shape_enabled.txt

clean:
	@rm -f \
	  *.txt \
	  _*

validation_with_uuid_shape_disabled.txt: \
  $(tests_srcdir)/.venv.done.log \
  disable_shape.ttl \
  example.ttl
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --ontology disable_shape.ttl \
	    example.ttl \
	    > _$@
	mv _$@ $@

validation_with_uuid_shape_enabled.txt: \
  $(tests_srcdir)/.venv.done.log \
  example.ttl
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --allow-infos \
	    example.ttl \
	    > _$@
	mv _$@ $@

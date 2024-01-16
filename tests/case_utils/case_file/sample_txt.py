#!/usr/bin/env python3

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

"""
This file is made with a Python script instead of 'echo' and 'touch' in order to handle time zone consistency.

Mtime should be 2010-01-02T03:04:56Z.
"""

import os
import sys

import dateutil.parser

with open(sys.argv[1], "w") as out_fh:
    out_fh.write("test")

target_datetime = dateutil.parser.isoparse("2010-01-02T03:04:56+00:00")
target_timestamp = target_datetime.timestamp()
os.utime(sys.argv[1], (target_timestamp, target_timestamp))

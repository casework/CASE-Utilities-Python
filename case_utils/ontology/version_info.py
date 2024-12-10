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
This program serves two roles:
1. As a module, it houses the hard-coded values for the current CASE version packaged with case_utils.
2. As a script, it prints that version when called.

When preparing to build a new monolithic ontology, please edit this variable to match the new respective version.
"""

__version__ = "0.7.0"

__all__ = ["CURRENT_CASE_VERSION", "built_version_choices_list"]

# Tested with CI to match versionInfo of <https://ontology.caseontology.org/case/case>.
CURRENT_CASE_VERSION: str = "1.3.0"

# Tested with CI to match set of ontology files available.
built_version_choices_list = [
    "none",
    "case-0.5.0",
    "case-0.6.0",
    "case-0.7.0",
    "case-0.7.1",
    "case-1.0.0",
    "case-1.1.0",
    "case-1.2.0",
    "case-" + CURRENT_CASE_VERSION,
]


def main() -> None:
    print(CURRENT_CASE_VERSION)


if __name__ == "__main__":
    main()

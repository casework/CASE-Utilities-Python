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

import pytest

import case_utils.local_uuid


def test_local_uuid_deprecation(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DEMO_UUID_REQUESTING_NONRANDOM", "NONRANDOM_REQUESTED")
    with pytest.warns(DeprecationWarning):
        case_utils.local_uuid.configure()


def test_local_uuid_nondirectory(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CASE_DEMO_NONRANDOM_UUID_BASE", "/dev/null")
    with pytest.warns(UserWarning):
        case_utils.local_uuid.configure()


def test_local_uuid_nonexistent(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CASE_DEMO_NONRANDOM_UUID_BASE", "/dev/nonexistent")
    with pytest.warns(UserWarning):
        case_utils.local_uuid.configure()

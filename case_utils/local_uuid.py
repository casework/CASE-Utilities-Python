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

"""
This library is a wrapper for uuid, provided to generate repeatable UUIDs if requested.
"""

__version__ = "0.2.0"

import os
import sys
import uuid

USE_DEMO_UUID: bool = False

DEMO_UUID_COUNTER: int = 0


def configure() -> None:
    global USE_DEMO_UUID

    if os.getenv("DEMO_UUID_REQUESTING_NONRANDOM") == "NONRANDOM_REQUESTED":
        USE_DEMO_UUID = True


def demo_uuid() -> str:
    """
    This function generates a repeatable UUID, drawing on non-varying elements of the environment and process call for entropy.

    WARNING: This function was developed for use ONLY for reducing (but not eliminating) version-control edits to identifiers in sample data.  It creates UUIDs that are decidedly NOT random, and should remain consistent on repeated calls to the importing script.

    To prevent accidental non-random UUID usage, an environment variable must be set to an uncommon string, hard-coded in this function.
    """
    global DEMO_UUID_COUNTER

    if os.getenv("DEMO_UUID_REQUESTING_NONRANDOM") != "NONRANDOM_REQUESTED":
        raise EnvironmentError(
            "demo_uuid() called without DEMO_UUID_REQUESTING_NONRANDOM in environment."
        )

    # Component: An emphasis this is an example.
    parts = ["example.org"]

    # Component: Incrementing counter.
    DEMO_UUID_COUNTER += 1
    parts.append(str(DEMO_UUID_COUNTER))

    # Component: Present working directory, replacing $HOME with '~'.
    env_HOME: str = os.getenv("HOME", "/nonexistent")
    parts.append(os.getcwd().replace(env_HOME, "~"))

    # Component: Argument vector.
    parts.extend(sys.argv)

    return str(uuid.uuid5(uuid.NAMESPACE_URL, "/".join(parts)))


def local_uuid() -> str:
    """
    Generate either a UUID4, or if requested via environment configuration, a non-random demo UUID.
    """
    global USE_DEMO_UUID
    if USE_DEMO_UUID:
        return demo_uuid()
    else:
        return str(uuid.uuid4())

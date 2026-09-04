# CASE Python Utilities

This project provides various specialized utilities for producing and analyzing data in the [CASE](https://caseontology.org/) format.


## Disclaimer

Participation by NIST in the creation of the documentation of mentioned software is not intended to imply a recommendation or endorsement by the National Institute of Standards and Technology, nor is it intended to imply that any specific software is necessarily the best available for the purpose.


## Installation

This repository can be installed from PyPI or from source.


### Installing from PyPI

```bash
pip install case-utils
```

Users who wish to install from PyPI should be aware that though CASE's ontology is in its post-1.0.0 release state, this Python project is in a pre-1.0.0 release state.  Backwards-incompatible ontology changes will only occur in accordance with [SEMVER](https://semver.org/).  This Python project is not yet committed to its API, and backwards-incompatiable changes may occur.  They are likely to occur with advance notice.

Users may wish to pin `case-utils` within any dependent code bases to be less than the next unreleased SEMVER-minor version.  (E.g. if `case-utils` version `0.14.0` is currently available, a newly adopting project might wish to track `case-utils<0.15.0` among its dependencies.)


### Installing from source

Users who wish to install pre-release versions and/or make improvements to the code base should install in this manner.

1. Clone this repository.
2. (Optional) Create and activate a virtual environment.
3. (Optional) Upgrade `pip` with `pip install --upgrade pip`.  (This can speed installation of some dependent packages.)
4. Run `pip install $x`, where `$x` is the path to the cloned repository.

Local installation is demonstrated in the `.venv.done.log` target of the `tests/` directory's [`Makefile`](tests/Makefile).


## Usage


### `case_validate`

This repository provides `case_validate` as an adaptation of the `pyshacl` command from [RDFLib's pySHACL](https://github.com/RDFLib/pySHACL).  The command-line interface is adapted to run as though `pyshacl` were provided the full CASE ontology (and adopted full UCO ontology) as both a shapes and ontology graph.  "Compiled" (or, "aggregated") CASE ontologies are in the [`case_utils/ontology/`](case_utils/ontology/) directory, and are installed with `pip`, so data validation can occur without requiring networking after this repository is installed.

To see a human-readable validation report of an instance-data file:

```bash
case_validate input.json [input-2.json ...]
```

If `input.json` is not conformant, a report will be emitted, and `case_validate` will exit with status `1`.  (This is a `pyshacl` behavior, where `0` and `1` report validation success.  Status of >`1` is for other errors.)

To produce the validation report as a machine-readable graph output, the `--format` flag can be used to modify the output format:

```bash
case_validate --format turtle input.json > result.ttl
```

To use one or more supplementary ontology or shape files, the `--ontology-graph` flag can be used, more than once if desired, to supplement the selected CASE version:

```bash
case_validate \
  --ontology-graph internal_ontology.ttl \
  --ontology-graph experimental_shapes.ttl \
  input.json
```

This tool uses the `--built-version` flag, described [below](#built-versions).

Other flags are reviewable with `case_validate --help`.


### `case_file`

To characterize a file, including hashes:

```bash
case_file sample.txt.json sample.txt
```

To characterize a file, but skip hashing it:

```bash
case_file --disable-hashes sample.txt.json sample.txt
```


### SPARQL executors

Two commands are provided to generate output from a SPARQL query and one or more input graphs.  Input graphs can be any graph, such as instance data or supplementary ontology files that supply custom class definitions or other external ontologies.

These commands can be used with any RDF files to run arbitrary SPARQL queries.  They have one additional behavior tailored to CASE: If a path query is used for subclasses, the CASE subclass hierarchy will be loaded to supplement the input graph.  An expected use case of this feature is subclasses of `ObservableObject`.  For instance, if a data graph included an object with only the class `uco-observable:File` specified, the query `?x a/rdfs:subClassOf* uco-observable:ObservableObject` would match `?x` against that object.

Note that prefixes used in the SPARQL queries do not need to be defined in the SPARQL query.  Their mapping will be inherited from their first definition in the input graph files.  However, input graphs are not required to agree on prefix mappings, so there is potential for confusion from input argument order mattering if two input graph files disagree on what a prefix maps to.  If there is concern of ambiguity from inputs, a `PREFIX` statement should be included in the query, such as is shown in [this test query](tests/case_utils/case_sparql_select/subclass.sparql).

These tools use the `--built-version` flag, described [below](#built-versions).


#### `case_sparql_construct`

To use a SPARQL `CONSTRUCT` query to make a supplementary graph file from one or more input graphs:

```bash
case_sparql_construct output.json input.sparql input.json [input-2.json ...]
```


#### `case_sparql_select`

To use a SPARQL `SELECT` query to make a table from one or more input graphs:

```bash
# HTML output with Bootstrap classes
# (e.g. for Jekyll-backed websites)
case_sparql_select output.html input.sparql input.json [input-2.json ...]

# Markdown, Github-flavored
case_sparql_select output.md input.sparql input.json [input-2.json ...]
```


### `local_uuid`

_Migration:_ Functionality previously in [`case_utils.local_uuid`](case_utils/local_uuid.py) has been exported to [`cdo-local-uuid`](https://github.com/Cyber-Domain-Ontology/CDO-Utility-Local-UUID).


### Built versions

Several tools in this package include a flag `--built-version`.  This flag tailors the tool's behavior to a certain CASE ontology version; typically, this involves mixing the ontology graph into the data graph for certain necessary knowledge expansion for pattern matching (such as making queries aware of the OWL subclass hierarchy).

If not provided, the tool will assume a default value of the latest ontology version.

If the special value `none` is provided, none of the ontology builds this package ships will be included in the data graph.  The `none` value supports use cases that are wholly independent of CASE, such as running a test in a specialized vocabulary; and also suports use cases where a non-released CASE version is meant to be used, such as a locally revised version of CASE where some concept revisions are being reviewed.


## Development status

This repository follows [CASE community guidance on describing development status](https://caseontology.org/resources/software.html#development_status), by adherence to noted support requirements.

The status of this repository is:

4 - Beta


## Versioning

This project follows [SEMVER 2.0.0](https://semver.org/) where versions are declared.


## Ontology versions supported

This repository supports the CASE ontology version that is linked as a submodule [here](dependencies/CASE).  The CASE version is encoded as a variable (and checked in unit tests) in [`case_utils/ontology/version_info.py`](case_utils/ontology/version_info.py), and used throughout this code base, as `CURRENT_CASE_VERSION`.

For instructions on how to update the CASE version for an ontology release, see [`CONTRIBUTE.md`](CONTRIBUTE.md).


## Repository locations

This repository is available at the following locations:
* [https://github.com/casework/CASE-Utilities-Python](https://github.com/casework/CASE-Utilities-Python)
* [https://github.com/usnistgov/CASE-Utilities-Python](https://github.com/usnistgov/CASE-Utilities-Python) (a mirror)

Releases and issue tracking will be handled at the [casework location](https://github.com/casework/CASE-Utilities-Python).


## Make targets

Some `make` targets are defined for this repository:
* `check` - Run unit tests.
* `clean` - Remove test build files, but not downloaded files.
* `download` - Download files sufficiently to run the unit tests offline.  This will *not* include the ontology repositories tracked as submodules.  Note if you do need to work offline, be aware touching the `setup.cfg` file in the project root directory, or `tests/requirements.txt`, will trigger a virtual environment rebuild.


## Windows Executables

This repository supports building Windows executables with [PyInstaller](https://pyinstaller.org/en/stable/index.html).
This packages a Python executable along with the code for portability.

```powershell
# Create the virtual environment (optional)
python3 -m venv venv

# Activate the virtual environment (optional)
./venv/Scripts/activate .

# Install PyInstaller and verify the version
pip install pyinstaller
pyinstaller --version

# Build the executable with the .spec file
pyinstaller .\case_validate.spec

# Confirm the build
.\dist\case_validate.exe -h
```

## Licensing

This repository is licensed under the Apache 2.0 License.  See [LICENSE](LICENSE).

Portions of this repository contributed by NIST are governed by the [NIST Software Licensing Statement](THIRD_PARTY_LICENSES.md#nist-software-licensing-statement).

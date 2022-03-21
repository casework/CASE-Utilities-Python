# Contributing to CASE-Utilities-Python


## Deploying a new ontology version

1. After cloning this repository, ensure the CASE submodule is checked out.  This can be done with either `git submodule init && git submodule update`, `make .git_submodule_init.done.log`, or `make check`.
2. Update the CASE submodule pointer to the new tagged release.
3. The version of CASE is also hard-coded in [`case_utils/ontology/version_info.py`](case_utils/ontology/version_info.py).  Edit the variable `CURRENT_CASE_VERSION`.
4. From the top source directory, run `make clean`.  This guarantees a clean state of this repository as well as the ontology submodules.
5. Still from the top source directory, run `make`.
6. Any new `.ttl` files will be created under [`case_utils/ontology/`](case_utils/ontology/).  Use `git add` to add each of them.  (The patch-weight of these files could overshadow manual revisions, so it is fine to commit the built files after the manual changes are committed.)

Here is a sample sequence of shell commands to run the build:

```bash
# (Starting from fresh `git clone`.)
make check
pushd dependencies/CASE
  git checkout master
  git pull
popd
git add dependencies/CASE
# (Here, edits should be made to case_utils/ontology/version_info.py)
make
pushd case_utils/ontology
  git add case-0.6.0.ttl  # Assuming CASE 0.6.0 was just released.
  # and/or
  git add uco-0.8.0.ttl   # Assuming UCO 0.8.0 was adopted in CASE 0.6.0.
popd
make check
# Assuming `make check` passes:
git commit -m "Update CASE ontology pointer to version 0.6.0" dependencies/CASE case_utils/ontology/version_info.py
git commit -m "Build CASE 0.6.0.ttl" case_utils/ontology/case-0.6.0.ttl
```

This project uses [the `pre-commit` tool](https://pre-commit.com/) for linting The easiest way to install it is with `pip`:
```bash
pip install pre-commit
pre-commit --version
```

The `pre-commit` tool hooks into Git's commit machinery to run a set of linters and static analyzers over each change. To install `pre-commit` into Git's hooks, run:
```bash
pre-commit install
```

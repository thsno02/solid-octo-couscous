# Repository semantic capsule: ResearchObject/ro-crate-py

- Commit: `05effe591443934e48e3fe59c53d7bc01a3334e0`
- Default branch: `master`
- Description: ResearchObject/ro-crate-py
- Selected evidence files: 5 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

[![Python package](https://github.com/ResearchObject/ro-crate-py/workflows/Python%20package/badge.svg)](https://github.com/ResearchObject/ro-crate-py/actions?query=workflow%3A%22Python+package%22) [![Upload Python Package](https://github.com/ResearchObject/ro-crate-py/workflows/Upload%20Python%20Package/badge.svg)](https://github.com/ResearchObject/ro-crate-py/actions?query=workflow%3A%22Upload+Python+Package%22) [![PyPI version](https://badge.fury.io/py/rocrate.svg)](https://pypi.org/project/rocrate/) [![DOI](https://zenodo.org/badge/216605684.svg)](https://zenodo.org/badge/latestdoi/216605684)

ro-crate-py is a Python library to create and consume [Research Object Crates](https://w3id.org/ro/crate). It supports the current [RO-Crate 1.2](https://w3id.org/ro/crate/1.2) specification as well as the older [RO-Crate 1.1](https://w3id.org/ro/crate/1.1) and [RO-Crate 1.0](https://w3id.org/ro/crate/1.0).

## Installation

ro-crate-py requires Python 3.9 or later. The easiest way to install is via [pip](https://docs.python.org/3/installing/):

```
pip install rocrate
```

To install the package with support for converting Galaxy workflows to CWL:

```
pip install rocrate[ga2cwl]
```

To install manually from this code base (e.g., to try the latest development revision):

```
git clone https://github.com/ResearchObject/ro-crate-py
cd ro-crate-py
pip install .
```

## Usage

### Creating an RO-Crate

In its simplest form, an RO-Crate is a directory tree with an `ro-crate-metadata.json` file at the top level. This file contains metadata about the other files and directories, represented by [data entities](https://www.researchobject.org/ro-crate/1.1/data-entities.html). These metadata consist both of properties of the data entities themselves and of other, non-digital entities called [contextual entities](https://www.researchobject.org/ro-crate/1.1/contextual-entities.html). A contextual entity can represent, for instance, a person, an organization or an event.

Suppose Alice and Bob worked on a research task together, which resulted in a manuscript written by both; additionally, Alice prepared a spreadsheet containing the experimental data, which Bob used to generate a diagram. We will create placeholder files for these documents:

```bash
mkdir exp
touch exp/paper.pdf
touch exp/results.csv
touch exp/diagram.svg
```

Let's make an RO-Crate to package all this:

```python
from rocrate.rocrate import ROCrate

crate = ROCrate()
paper = crate.add_file("exp/paper.pdf", properties={
    "name": "manuscript",
    "encodingFormat": "application/pdf"
})
table = crate.add_file("exp/results.csv", properties={
    "name": "experimental data",
    "encodingFormat": "text/csv"
})
diagram = crate.add_file("exp/diagram.svg", dest_path="images/figure.svg", properties={
    "name": "bar chart",
    "encodingFormat": "image/svg+xml"
})
```

The `dest_path` argument is used to specify the relative path of the file with respect to the crate's directory (which will be determined when the crate is written). Note that the first two `add_file` calls do not specify `dest_path`: in this case, it will be set to the source file's basename (`"paper.pdf"` in the first case), so the file will be at the crate's top level when it is written.

We've started by adding the data entities. Now we need contextual entities to represent Alice and Bob:

```python
from rocrate.model.person import Person

alice_id = "https://orcid.org/0000-0000-0000-0000"
bob_id = "https://orcid.org/0000-0000-0000-0001"
alice = crate.add(Person(crate, alice_id, properties={
    "name": "Alice Doe",
    "affiliation": "University of Flatland"
}))
bob = crate.add(Person(crate, bob_id, properties={
    "name": "Bob Doe",
    "affiliation": "University of Flatland"
}))
```

At this point, we have a representation of the various entities. Now we need to express the relationships between them. This is done by adding properties that reference other entities:

```python
paper["author"] = [alice, bob]
table["author"] = alice
diagram["author"] = bob
```

You can also add whole directories together with their contents. In an RO-Crate, a directory is represented by the `Dataset` entity. Create a directory with some placeholder files:

```bash
mkdir exp/logs
touch exp/logs/log1.txt
touch exp/logs/log2.txt
```

Now add it to the crate:

```python
logs = crate.add_dataset("exp/logs")
```

Finally, we serialize the crate to disk:

```python
crate.write("exp_crate")
```

Now the `exp_crate` directory should contain copies of all the files we added and an `ro-crate-metadata.json` file with a [JSON-LD](https://json-ld.org) representation of the entities and relationships we created, with the following layout:

```
exp_crate/
|-- images/
|   `-- figure.svg
|-- logs/
|   |-- log1.txt
|   `-- log2.txt
|-- paper.pdf
|-- results.csv
`-- ro-crate-metadata.json
```

Exploring the `exp_crate` directory, we see that all files and directories contained in `exp/logs` have been added recursively to the crate. However, in the `ro-crate-metadata.json` file, only the top level Dataset with `@id` `"exp/logs"` is listed. This is because we used `crate.add_dataset("exp/logs")` rather than adding every file individually. There is no requirement to represent every file and folder within the crate in the `ro-crate-metadata.json` file. If you do want to add files and directories recursively to the metadata, use `crate.add_tree` instead of `crate.add_dataset` (but note that it only works on local directory trees).

Some applications and services support RO-Crates stored as archives. To save the crate in zip format, use `write_zip`:

```python
crate.write_zip("exp_crate.zip")
```

#### Appending elements to property values

What ro-crate-py entities actually store is their JSON representation:

```python
paper.properties()
```

```json
{
  "@id": "paper.pdf",
  "@type": "File",
  "name": "manuscript",
  "encodingFormat": "application/pdf",
  "author": [
    {"@id": "https://orcid.org/0000-0000-0000-0000"},
    {"@id": "https://orcid.org/0000-0000-0000-0001"},
  ]
}
```

When `paper["author"]` is accessed, a new list containing the `alice` and `bob` entities is generated on the fly. For this reason, calling `append` on `paper["author"]` won't actually modify the `paper` entity in any way. To add an author, use the `append_to` method instead:

```python
donald = crate.add(Person(crate, "https://en.wikipedia.org/wiki/Donald_Duck", properties={
  "name": "Donald Duck"
}))
paper.append_to("author", donald)
```

Note that `append_to` also works if the property to be updated is missing or has only one value:

```python
for n in "Mickey_Mouse", "Scrooge_McDuck":
    p = crate.add(Person(crate, f"https://en.wikipedia.org/wiki/{n}"))
    donald.append_to("follows", p)
```

#### Handling of special characters

Since RO-Crate entity identifiers are URIs (relative or absolute), special characters in them must be percent-encoded. When adding data entities from the local file system, this is handled automatically by the library:

```pycon
>>> crate = ROCrate()
>>> d = crate.add_dataset("read_crate/a b")
>>> d.id
'a%20b/'
>>> f = crate.add_file("read_crate/a b/c d.txt", dest_path="data/a b/c d.txt")
>>> f.id
'data/a%20b/c%20d.txt'
```

When adding an entity whose identifier is an absolute URI (see next section), on the other hand, the identifier provided by the user is expected to be a valid URI, in particular with any special characters in path components already percent-encoded.

#### Adding remote entities

Data entities can also be remote:

```python
input_data = crate.add_file("http://example.org/exp_data.zip")
```

By default the file won't be downloaded, and will be referenced by its URI in the serialized crate:

```json
{
  "@id": "http://example.org/exp_data.zip",
  "@type": "File"
},
```

If you add `fetch_remote=True` to the `add_file` call, however, the library (when `crate.write` is called) will try to download the file and include it in the output crate.

Another option that influences the behavior when dealing with remote entities is `validate_url`, also `False` by default: if it's set to `True`, when the crate is serialized, the library will try to open the URL to add / update metadata bits such as the content's length and format (but it won't try to download the file unless `fetch_remote` is also set).

#### Adding entities with an arbitrary type

An entity can be of any type listed in the [RO-Crate context](https://www.researchobject.org/ro-crate/1.1/context.jsonld). However, only a few of them have a counterpart (e.g., `File`) in the library's class hierarchy (either because they are very common or because they are associated with specific functionality that can be conveniently embedded in the class implementation). In other cases, you can explicitly pass the type via the `properties` argument:

```python
from rocrate.model.contextentity import ContextEntity

hackathon = crate.add(ContextEntity(crate, "#bh2021", properties={
    "@type": "Hackathon",
    "name": "Biohackathon 2021",
    "location": "Barcelona, Spain",
    "startDate": "2021-11-08",
    "endDate": "2021-11-12"
}))
```

## `CONTRIBUTING.md`

# Contributing to this repository

ro-crate-py is open source software distributed under the Apache License, Version 2.0. Contributions are welcome, but please read this guide first. Submitted contributions are assumed to be covered by section 5 of the [license](LICENSE).


## Before you begin

[Set up Git](https://docs.github.com/en/github/getting-started-with-github/set-up-git) on your local machine, then [fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) this repository on GitHub and [create a local clone of your fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo#step-2-create-a-local-clone-of-your-fork).

For instance, if your GitHub user name is `simleo`, you can get a local clone as follows:

```
$ git clone https://github.com/simleo/ro-crate-py
```

You can see that the local clone is pointing to your remote fork:

```
$ cd ro-crate-py
$ git remote -v
origin	https://github.com/simleo/ro-crate-py (fetch)
origin	https://github.com/simleo/ro-crate-py (push)
```

To keep a reference to the original (upstream) repository, you can add a remote for it:

```
$ git remote add upstream https://github.com/researchobject/ro-crate-py
$ git fetch upstream
```

This allows, among other things, to easily keep your fork synced to the upstream repository through time. For instance, to sync your `master` branch:

```
$ git checkout master
$ git fetch -p upstream
$ git merge --ff-only upstream/master
$ git push origin master
```

If you need help with Git and GitHub, head over to the [GitHub docs](https://docs.github.com/en/github). In particular, you should be familiar with [issues and pull requests](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests).


## Making a contribution

Contributions can range from fixing a broken link or a typo in the documentation to fixing a bug or adding a new feature to the software. Ideally, contributions (unless trivial) should be related to an [open issue](https://github.com/researchobject/ro-crate-py/issues). If there is no existing issue or [pull request](https://github.com/researchobject/ro-crate-py/pulls) related to the changes you wish to make, you can open a new one.

Make your changes on a branch in your fork, then open a pull request (PR). Please take some time to summarize the proposed changes in the PR's description, especially if they're not obvious. If the PR addresses an open issue, you should [link it to the issue](https://docs.github.com/en/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue).


## Contributing documentation

Currently, documentation consists of a few [Markdown](http://daringfireball.net/projects/markdown) files such as this one. Read the [Mastering Markdown](https://guides.github.com/features/mastering-markdown) guide for a quick introduction to the format. Before opening the PR, you can check that the document renders as expected by looking at the corresponding page on the relevant branch in your fork.


## Contributing software

ro-crate-py is written in [Python](https://www.python.org). To isolate your development environment from the underlying system, you can use a [virtual environment](https://docs.python.org/3.8/library/venv.html):

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

For development, it's recommended to install ro-crate-py in [editable mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html):

```
pip install -e .
```

In this way, any changes to the code will be picked up immediately, without the need to reinstall the package.

When you're done with your work, you can deactivate the virtual environment by typing `deactivate` on your shell.

Before pushing any changes, make sure everything is fine by running the linting and testing commands as explained below.

### Linting

ro-crate-py uses [Flake8](https://github.com/PyCQA/flake8) for linting. The configuration is in `setup.cfg` and it's picked up automatically. If you have a `venv` directory or any other directory you don't want to be checked by Flake8, use the `--exclude` option.

```
pip install flake8
flake8 --exclude venv ./
```

### Pre-commit hooks
ro-crate-py comes with a configuration file for [pre-commit](https://github.com/pre-commit/pre-commit) `.pre-commit-config.yaml`.
This configuration file defines so-called "hooks" which are executed upon each commit, to automatically format the code in the commited files according to the requirements defined for instance in the flake8 configuration file (e.g removing spaces from blank lines...).

To benefit from these automated hooks, you need first to install the pre-commit package.
`pip install pre-commit`

The hooks should then be installed once for your local copy of the repository by running the following command in the root of the repo.
`pre-commit install`

Once installed the hooks will be executed each time a new commit is made, for the files being commited.
If some checks failed or could not be fixed automatically, an error message will be shown and the commit will be aborted.

While not recommended, you can bypass the hooks by passing the additional flag `--no-verify` to the `git commit` command.

Some IDEs have plugins for precommit (e.g [here](https://marketplace.visualstudio.com/items?itemName=elagil.pre-commit-helper) for VSCode), which would for instance run the hooks for the currently opened file each time it is saved. The plugins typically pick up the configuration file automatically.

### Testing

Testing is done with [pytest](https://pytest.org):

```
pip install pytest
pytest test
```

If a test is failing, you can get more information by enabling verbose mode and stdout/stderr dump. For instance:

```
pytest -sv test/test_write.py::test_remote_uri_exceptions
```

Ideally, every code contribution should come with new unit tests that add coverage for the bug fix or new feature.

### Using the Docker image for development

ro-crate-py is currently a fairly simple library that does not require any special infrastructure setup, so virtual environments should be enough for development. However, if you want a higher degree of isolation, you can build the [Docker](https://www.docker.com/) image with:

```
docker build -t ro-crate-py .
```

And then run it interactively with:

```
docker run --rm -it --name ro-crate-py ro-crate-py bash
```


## Tidying up after PR merge

After your PR has been merged, you can delete the branch used for your changes. You can delete the remote branch from GitHub, by clicking on "Delete branch" in the PR's page. To resync everything, run:

```
git checkout master
git fetch -p upstream
git merge --ff-only upstream/master
git push origin master
git branch -d <pr_branch_name>
```

## `Dockerfile`

FROM python:3.12

COPY ./ /ro-crate-py
WORKDIR /ro-crate-py

RUN pip install --no-cache-dir -r requirements.txt && \
    python setup.py install

## `Makefile`

.DEFAULT_GOAL := install

SHELL := /bin/bash
PYTHON ?= python3
VENV_DIR ?= venv
IN_VENV = [ -f $(VENV_DIR)/bin/activate ] && . $(VENV_DIR)/bin/activate;


$(VENV_DIR):
	$(PYTHON) -m venv $(VENV_DIR)
	$(IN_VENV) pip install --upgrade pip

$(VENV_DIR)/bin/flake8: $(VENV_DIR)
	$(IN_VENV) pip install flake8

$(VENV_DIR)/bin/pytest: $(VENV_DIR)
	$(IN_VENV) pip install pytest

init-venv: $(VENV_DIR)

install: $(VENV_DIR)
	$(IN_VENV) pip install -r requirements.txt
	$(IN_VENV) pip install ./

lint: $(VENV_DIR)/bin/flake8
	$(IN_VENV) flake8 --exclude $(VENV_DIR) ./

test: $(VENV_DIR)/bin/pytest install
	$(IN_VENV) pytest test

# WARNING: removes ALL untracked files
clean:
	git clean -fdx -e $(VENV_DIR)

.PHONY: init-venv install lint test clean $(VENV_DIR)

## `pyproject.toml`

[build-system]
requires = ["setuptools >= 64"]
build-backend = "setuptools.build_meta"

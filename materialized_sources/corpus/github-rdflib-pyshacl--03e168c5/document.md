# Repository semantic capsule: RDFLib/pySHACL

- Commit: `469cca7a22a078b36c167c1e8dadecf5e5ec6c75`
- Default branch: `master`
- Description: RDFLib/pySHACL
- Selected evidence files: 5 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

![](pySHACL-250.png)

# pySHACL
A Python validator for SHACL.

[![Build Status](https://drone.rdflib.ashs.dev/api/badges/RDFLib/pySHACL/status.svg)](https://drone.rdflib.ashs.dev/RDFLib/pySHACL)

[![DOI](https://zenodo.org/badge/147505799.svg)](https://zenodo.org/badge/latestdoi/147505799) [![Downloads](https://pepy.tech/badge/pyshacl)](https://pepy.tech/project/pyshacl) [![Downloads](https://pepy.tech/badge/pyshacl/month)](https://pepy.tech/project/pyshacl/month) [![Downloads](https://pepy.tech/badge/pyshacl/week)](https://pepy.tech/project/pyshacl/week)

This is a pure Python module which allows for the validation of [RDF](https://www.w3.org/2001/sw/wiki/RDF) graphs against Shapes Constraint Language ([SHACL](https://www.w3.org/TR/shacl/)) graphs. This module uses the [rdflib](https://github.com/RDFLib/rdflib) Python library for working with RDF and is dependent on the [OWL-RL](https://github.com/RDFLib/OWL-RL) Python module for [OWL2 RL Profile](https://www.w3.org/TR/owl2-overview/#ref-owl-2-profiles) based expansion of data graphs.

This module is developed to adhere to the SHACL Recommendation:
> Holger Knublauch; Dimitris Kontokostas. *Shapes Constraint Language (SHACL)*. 20 July 2017. W3C Recommendation. URL: <https://www.w3.org/TR/shacl/> ED: <https://w3c.github.io/data-shapes/shacl/>

# Community for Help and Support
The SHACL community has a discord server for discussion of topics around SHACL and the SHACL specification.

[Use this invitation link: https://discord.gg/RTbGfJqdKB to join the server](https://discord.gg/RTbGfJqdKB)

There is a \#pyshacl channel for discussion of this python library, and you can ask for general SHACL help too.

## Installation
Install with PIP (Using the Python3 pip installer `pip3`)
```bash
$ pip3 install pyshacl
```

Or in a python virtualenv _(these example commandline instructions are for a Linux/Unix based OS)_
```bash
$ python3 -m virtualenv --python=python3 --no-site-packages .venv
$ source ./.venv/bin/activate
$ pip3 install pyshacl
```

To exit the virtual enviornment:
```bash
$ deactivate
```

### Optional: Oxigraph backend
To enable Oxigraph compatibility, install the optional `oxigraph` extra:
```bash
$ pip3 install pyshacl[oxigraph]
```

This installs `pyoxigraph`, which lets pySHACL run validation and SHACL Rules
against an Oxigraph store backend.

## Command Line Use
For command line use:
_(these example commandline instructions are for a Linux/Unix based OS)_
```bash
$ pyshacl -s /path/to/shapesGraph.ttl -m -i rdfs -a -j -f human /path/to/dataGraph.ttl
```
To validate multiple data graphs in combine mode (default):
```bash
$ pyshacl -s /path/to/shapesGraph.ttl /path/to/dataGraph1.ttl /path/to/dataGraph2.ttl
```
To validate multiple data graphs independently:
```bash
$ pyshacl --validate-each -s /path/to/shapesGraph.ttl /path/to/dataGraph1.ttl /path/to/dataGraph2.ttl
```
Where
 - `-s` is an (optional) path to the shapes graph to use
 - `-e` is an (optional) path to an extra ontology graph to import
 - `-i` is the pre-inferencing option
 - `-f` is the ValidationReport output format (`human` = human-readable validation report)
 - `--validate-each` validates each data graph independently when multiple inputs are provided
 - `-m` enable the meta-shacl feature
 - `-a` enable SHACL Advanced Features
 - `-j` enable SHACL-JS Features (if `pyshacl[js]` is installed)

System exit codes are:
`0` = DataGraph is Conformant
`1` = DataGraph is Non-Conformant
`2` = The validator encountered a RuntimeError (check stderr output for details)
`3` = Not-Implemented; The validator encountered a SHACL feature that is not yet implemented.

Full CLI Usage options:
```bash
$ pyshacl -h
$ python3 -m pyshacl -h
usage: pyshacl [-h] [-s [SHACL]] [-e [ONT]] [-i {none,rdfs,owlrl,both}] [-m]
               [-im] [-a] [-j] [-it] [--abort] [--allow-info] [-w]
               [--max-depth [MAX_DEPTH]] [-d] [--validate-each]
               [-f {human,table,turtle,xml,json-ld,nt,n3}]
               [-df {auto,turtle,xml,json-ld,nt,n3}]
               [-sf {auto,turtle,xml,json-ld,nt,n3}]
               [-ef {auto,turtle,xml,json-ld,nt,n3}] [-V] [-o [OUTPUT]]
               [--server]
               DataGraph [DataGraph ...]

PySHACL 0.27.0 command line tool.

positional arguments:
  DataGraph             The file(s) containing the Target Data Graph.

optional arguments:
  --server              Ignore all the rest of the options, start the HTTP Server.
  -h, --help            show this help message and exit
  -s [SHACL], --shacl [SHACL]
                        A file containing the SHACL Shapes Graph.
  -e [ONT], --ont-graph [ONT]
                        A file path or URL to a document containing extra
                        ontological information. RDFS and OWL definitions from this 
                        are used to inoculate the DataGraph.
  -i {none,rdfs,owlrl,both}, --inference {none,rdfs,owlrl,both}
                        Choose a type of inferencing to run against the Data
                        Graph before validating.
  -m, --metashacl       Validate the SHACL Shapes graph against the shacl-
                        shacl Shapes Graph before validating the Data Graph.
  -im, --imports        Allow import of sub-graphs defined in statements with
                        owl:imports.
  -a, --advanced        Enable features from the SHACL Advanced Features
                        specification.
  -j, --js              Enable features from the SHACL-JS Specification.
  -it, --iterate-rules  Run Shape's SHACL Rules iteratively until the
                        data_graph reaches a steady state.
  --abort               Abort on first invalid data.
  --allow-info, --allow-infos
                        Shapes marked with severity of Info will not cause
                        result to be invalid.
  -w, --allow-warning, --allow-warnings
                        Shapes marked with severity of Warning or Info will
                        not cause result to be invalid.
  --max-depth [MAX_DEPTH]
                        The maximum number of SHACL shapes "deep" that the
                        validator can go before reaching an "endpoint"
                        constraint.
  -d, --debug           Output additional verbose runtime messages.
  --validate-each       Validate each data graph independently when multiple
                        inputs are provided.
  --focus [FOCUS]       Optional IRIs of focus nodes from the DataGraph, the shapes will
                        validate only these node. Comma-separated list.
  --shape [SHAPE]       Optional IRIs of a NodeShape or PropertyShape from the SHACL
                        ShapesGraph, only these shapes will be used to validate the
                        DataGraph. Comma-separated list.
  -f {human,table,turtle,xml,json-ld,nt,n3}, --format {human,table,turtle,xml,json-ld,nt,n3}
                        Choose an output format. Default is "human".
  -df {auto,turtle,xml,json-ld,nt,n3}, --data-file-format {auto,turtle,xml,json-ld,nt,n3}
                        Explicitly state the RDF File format of the input
                        DataGraph file. Default="auto".
  -sf {auto,turtle,xml,json-ld,nt,n3}, --shacl-file-format {auto,turtle,xml,json-ld,nt,n3}
                        Explicitly state the RDF File format of the input
                        SHACL file. Default="auto".
  -ef {auto,turtle,xml,json-ld,nt,n3}, --ont-file-format {auto,turtle,xml,json-ld,nt,n3}
                        Explicitly state the RDF File format of the extra
                        ontology file. Default="auto".
  -V, --version         Show PySHACL version and exit.
  -o [OUTPUT], --output [OUTPUT]
                        Send output to a file (defaults to stdout).
  --server              Ignore all the rest of the options, start the HTTP
                        Server. Same as `pyshacl_server`.
```

## Python Module Use
For basic use of this module, you can just call the `validate` function of the `pyshacl` module like this:

```python
from pyshacl import validate

data_graph = "some-data.ttl"
shacl_graph = "some-shacl.ttl"
ont_graph = "some-ontology.ttl"

r = validate(data_graph,
      shacl_graph=shacl_graph,
      ont_graph=ont_graph,
      inference='rdfs',
      abort_on_first=False,
      allow_infos=False,
      allow_warnings=False,
      meta_shacl=False,
      advanced=False,
      js=False,
      debug=False)
conforms, results_graph, results_text = r
```

To validate using an Oxigraph-backed data graph:

```python
from pyoxigraph import RdfFormat, Store
from pyshacl import validate

data_store = Store()
with open("some-data.ttl", "rb") as f:
    data_store.bulk_load(f.read(), format=RdfFormat.TURTLE)

conforms, results_graph, results_text = validate(
    data_store,
    shacl_graph="some-shacl.ttl",
    ont_graph="some-ontology.ttl",
    advanced=True,
)
```

The same Oxigraph store input is also supported by `shacl_rules(...)`.

To validate multiple data graphs in combine mode (default):
```python
from pyshacl import validate

data_graphs = ["data1.ttl", "data2.ttl", "data3.ttl"]
conforms, results_graph, results_text = validate(data_graphs, shacl_graph="shapes.ttl")
```

To validate each data graph independently:
```python
from pyshacl import validate_each

data_graphs = ["data1.ttl", "data2.ttl", "data3.ttl"]
results = validate_each(data_graphs, shacl_graph="shapes.ttl")
for graph_id, (conforms, results_graph, results_text) in results.items():
    print(graph_id, conforms)
```

Where:
* `data_graph` is an rdflib `Graph` object, file path, or a sequence of those to be validated
* `shacl_graph` is an rdflib `Graph` object or file path or Web URL of the graph containing the SHACL shapes to validate with, or None if the SHACL shapes are included in the data_graph.

## `CONTRIBUTING.md`

# CONTRIBUTING

### The PySHACL project encourages submissions from anyone who wishes to contribute

There are some strict submission quality requirements:

## Code Format

PySHACL uses the `black` code style. https://github.com/psf/black

Specifically, we use v20.8b1 in `py36` mode, with line length of `119`, and `skip-string-normalization = true`.

## Code Linting

PySHACL requires all code to pass the Flake8 linter. In the internal test suite, we use Flake8 v3.8.0.

In addition to Flake8, we use `isort` to keep the import strings at the top of each source file in a consistent sorted order. The version if isort used is v5.7.0 and it is configured with the isort settings listed in the pyproject.toml file.

## Type Checking

PySHACL uses MyPy to run static type analysis checks on the code. Not all parts of PySHACL have type annotations, but those parts that do should be annotated correctly to pass the MyPy test.

The internal test suite uses MyPy v0.800.

## Testing

The best way to comprehensively test PySHACL is to use [Tox](https://tox.readthedocs.io/en/latest/).

It is a simple matter of running `pip3 install tox` then `tox` on the commandline in the project root.

This will run a whole suite of tests, including pytest, flake8, mypy, black and isort.

All tests in the PySHACL pytest test suite should pass without errors.

## Makefile

There is also a Makefile in the project root that you can for covenience to kick off tests with `make test`, as well as some non-tox commands that can be invoked with `make format`, `make list` and `make type-check`.



## `Dockerfile`

FROM docker.io/library/python:3.11-alpine
LABEL org.opencontainers.image.base.name="docker.io/library/python:3.11-alpine"
LABEL org.opencontainers.image.base.digest="sha256:d5e2fc72296647869f5eeb09e7741088a1841195059de842b05b94cb9d3771bb"
LABEL org.opencontainers.image.source="https://github.com/RDFLib/pySHACL"
LABEL org.opencontainers.image.version="0.40.1"
LABEL maintainer="ashleysommer@gmail.com"
RUN apk add --no-cache --update tini-static cython
RUN apk add --no-cache --update --virtual build-dependencies build-base libffi-dev python3-dev py3-cffi
# Update to latest setuptools and pip in /usr/local/lib to mitigate CVE-2024-6345
RUN pip3 install -U pip setuptools
WORKDIR /home/pyshacl
RUN addgroup -g 1000 -S pyshacl &&\
    adduser --disabled-password --gecos "" --home "$(pwd)" --ingroup "pyshacl" --no-create-home --uid 1000 pyshacl
WORKDIR /app
COPY . .
RUN chown -R pyshacl:pyshacl /home/pyshacl /app && chmod -R 775 /home/pyshacl /app
USER pyshacl
ENV PATH="/home/pyshacl/.local/bin:$PATH"
RUN pip3 install "poetry<3.0,>=2.1"
RUN poetry install --extras "js http"
RUN poetry run pip3 install -U "rdflib[orjson]<8" # add orjson support to rdflib
USER root
RUN apk del build-dependencies
USER pyshacl
ENTRYPOINT ["/sbin/tini-static", "--"]
CMD ["poetry", "run", "pyshacl"]

## `Makefile`

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: venvcheck ## Check if venv is active
venvcheck:
ifeq ("$(VIRTUAL_ENV)","")
	@echo "Venv is not activated!"
	@echo "Activate venv first."
	@echo
	exit 1
endif

.PHONY: env
env: venvcheck  ## Double check environment variables
	env

.PHONY: install
install: venvcheck  ## Install the dependencies, but not dev-dependencies
	poetry install --no-dev

.PHONY: dev
dev: venvcheck  ## Install dependencies and dev-dependencies, but not this project itself
	poetry install --no-root --extras "js dev-lint dev-type-checking dev-coverage"

.PHONY: test
test: venvcheck		## Run the TOX tests in a TOX environment
	poetry run tox

.PHONY: dev-test
dev-test: venvcheck		## Run the tests in dev environment
	poetry run pytest --cov=pyshacl test/
	poetry run pytest test/issues/


.PHONY: format
format: venvcheck	## Run Ruff and isort Formatters
ifeq ("$(FilePath)", "")
	poetry run ruff check --select I --fix ./pyshacl #isort fix
	poetry run ruff format --no-preview --target-version py39 pyshacl
else
	poetry run ruff check --select I --fix "$(FilePath)" #isort fix
	poetry run ruff format --no-preview --target-version py39 "$(FilePath)"
endif

.PHONY: lint
lint: venvcheck	## Validate with Ruff and isort in check-only mode
ifeq ("$(FilePath)", "")
	poetry run ruff check ./pyshacl  #flake8
	poetry run ruff check --select I ./pyshacl  #isort
	poetry run ruff format --check --no-preview --target-version py39 pyshacl
else
	poetry run ruff check ./"$(FilePath)"  #flake8
	poetry run ruff check --select I ./"$(FilePath)" #isort
	poetry run ruff format --check --no-preview --target-version py39 "$(FilePath)"
endif

.PHONY: type-check
type-check: venvcheck	## Validate with MyPy in check-only mode
ifeq ("$(FilePath)", "")
	poetry run python3 -m mypy --python-version 3.9 --ignore-missing-imports pyshacl
else
	poetry run python3 -m mypy --python-version 3.9 --ignore-missing-imports "$(FilePath)"
endif

.PHONY: upgrade
upgrade: venvcheck	## Upgrade the dependencies
	poetry update

.PHONY: downgrade
downgrade: venvcheck ## Downgrade the dependencies
	git checkout pyproject.toml && git checkout poetry.lock
	poetry install --no-root --extras "js dev-lint dev-type-checking dev-coverage"

.PHONY: publish
publish: venvcheck	## Build and publish to PYPI
	poetry build
	poetry publish

## `pyproject.toml`

[build-system]
requires = ["poetry-core<3,>=2.0"]
build-backend = "poetry.core.masonry.api"

[project]
name = "pyshacl"
# Don't forget to change the version number in __init__.py, Dockerfile, and CITATION.cff along with this one
version = "0.40.1"
requires-python = ">=3.9"
description = "Python SHACL Validator"
license = { file = "LICENSE.txt" }
authors = [
    {name = "Ashley Sommer", email = "Ashley.Sommer@csiro.au"}
]
readme = "README.md"
keywords = [
    "Linked Data",
    "Semantic Web",
    "RDF",
    "Graph",
    "Python",
    "SHACL",
    "Shapes",
    "Schema",
    "Validate",
    "Validator"
]
classifiers = [
    "License :: OSI Approved :: Apache Software License",
    "Development Status :: 5 - Production/Stable",
    "Topic :: Utilities",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Operating System :: OS Independent"
]
dependencies = [
    "rdflib[html]>=7.3.0,<8.0",
    "owlrl>=7.6.2,<8",
    "prettytable>=3.5.0; python_version<'3.12'",
    "prettytable>=3.7.0; python_version>='3.12'",
    "packaging>=21.3",
    "importlib-metadata>6; python_version<'3.12'",
]

[project.urls]
homepage = "https://github.com/RDFLib/pySHACL"
source = "https://github.com/RDFLib/pySHACL"
issues = "https://github.com/RDFLib/pySHACL/issues"
download = "https://github.com/RDFLib/pySHACL/releases"
changelog = "https://github.com/RDFLib/pySHACL/blob/master/CHANGELOG.md"

[project.optional-dependencies]
# These are equivelent to python package "extras"
js = [
    "pyduktape2<1,>=0.4.6; python_version<='3.13'",
    "pyduktape2<1,>=0.5.0; python_version>='3.13'",
]
oxigraph = [
    "pyoxigraph>=0.5.6"
]
http = [
    "sanic<23,>=22.12",
    "sanic-ext<23.6,>=23.3",
    "sanic-cors==2.2.0"
]
dev-lint = [
    "ruff<0.10,>=0.9.3",
    "platformdirs"
]
dev-type-checking = [
    "mypy>=1.13.0",
    "types-setuptools",
    "platformdirs"
]
dev-coverage = [
    "pytest-cov<3,>=2.8.1",
    "coverage>6,<7,!=6.0.*,!=6.1,!=6.1.1",
    "platformdirs"
]

[project.scripts]
pyshacl = "pyshacl.cli:main"
pyshacl_rules = "pyshacl.cli_rules:main"
pyshacl_validate = "pyshacl.cli:main"
pyshacl_server = "pyshacl.http:cli"

[tool.poetry]
packages = [
    { include = "pyshacl" },
    { include = "examples", format = "sdist" },
    { include = "benchmarks", format = "sdist" },
    { include = "test", format = "sdist" }
]

include = [
    { path = "pyshacl/assets/*.ttl", format = "sdist" },
    { path = "pyshacl/assets/*.py", format = "sdist" },
    { path = "hooks/*", format = "sdist" },
    { path = "MANIFEST.in", format = "sdist" },
    { path = "pyproject.toml", format = "sdist" },
    { path = "poetry.lock", format = "sdist" },
    { path = "Makefile", format = "sdist" },
    { path = "*.md" },
    { path = "*.txt" },
    { path = "pyshacl/py.typed" },
    { path = "pyshacl/assets/*.pickle" },
    { path = "pyshacl/*.spec" }
]

[tool.poetry.group.dev.dependencies]
pytest = "^7.2"
coverage = {version=">6,<7,!=6.0.*,!=6.1,!=6.1.1", optional=true}
pytest-cov = {version="^2.8.1", optional=true}
ruff = {version="<0.10,>=0.9.3", optional=true}
mypy = {version=">=1.13.0", optional=true}
types-setuptools = {version="*", optional=true}
platformdirs = {version="*", optional=true}

[tool.dephell.main]
from = {format = "poetry", path = "pyproject.toml"}
to = {format = "setuppy", path = "setup.py"}

[tool.ruff]
# Exclude a variety of commonly ignored directories.
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".git-rewrite",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".pytype",
    ".ruff_cache",
    ".pytest_cache",
    ".svn",
    ".tox",
    ".venv",
    ".idea",
    "htmlcov",
    "__pypackages__",
    "_build",
    "buck-out",
    "pyshacl.egg-info",
    "build",
    "dist",
    "node_modules",
    "venv",
]
line-length = 119

[tool.ruff.format]
quote-style = "preserve"

[lint]
# Enable pycodestyle (`E`) and Pyflakes (`F`) codes by default.
select = ["E", "F"]
ignore = ["E501"]  # Turn off ruff's too-long-line detection for now, we'll have to enable it again later.

# Allow autofix for all enabled rules (when `--fix`) is provided.
fixable = ["A", "B", "C", "D", "E", "F", "G", "I", "N", "Q", "S", "T", "W", "ANN", "ARG", "BLE", "COM", "DJ", "DTZ", "EM", "ERA", "EXE", "FBT", "ICN", "INP", "ISC", "NPY", "PD", "PGH", "PIE", "PL", "PT", "PTH", "PYI", "RET", "RSE", "RUF", "SIM", "SLF", "TCH", "TID", "TRY", "UP", "YTT"]
unfixable = []
# Allow unused variables when underscore-prefixed.
dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"


[lint.mccabe]
# Unlike Flake8, default to a complexity level of 10.
max-complexity = 10

[lint.pycodestyle]
ignore-overlong-task-comments = true

[tool.pytest.ini_options]
minversion = "6.0"
testpaths = [
    "test",
]

[tool.tox]
legacy_tox_ini = """
[tox]
skipsdist = true
envlist = py39, py310, py311, py312, py313, lint, type-checking
toxworkdir={env:TOX_WORK_DIR:.tox}

[testenv]
deps =
    poetry>=2.1
passenv =
    DBUS_SESSION_BUS_ADDRESS
    PIP_KEYRING_PROVIDER
    PIP_FORCE_KEYRING
    PYTHON_KEYRING_BACKEND
skip_install = true
allowlist_externals = python3, ls, pwd, env, poetry

commands_pre =
    py39: poetry run pip3 install -U "pip>=21.0"
    py310: poetry run pip3 install -U "pip>=21.3"
    py311: poetry run pip3 install -U "pip>=22.1"
    poetry install -vv -n --no-root --extras "js dev-coverage"

commands =
    - poetry show
    poetry run pytest -v --log-level=INFO --cov=pyshacl test/
    poetry run pytest -v --log-level=INFO test/issues/
    - poetry run coverage combine --append

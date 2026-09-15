# Repository semantic capsule: linkml/linkml

- Commit: `0e401cef2711b0f12f5a1870805c5cfa999b0858`
- Default branch: `main`
- Description: linkml/linkml
- Selected evidence files: 8 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

[![Pyversions](https://img.shields.io/pypi/pyversions/linkml.svg)](https://pypi.python.org/pypi/linkml)
![](https://github.com/linkml/linkml/workflows/Build/badge.svg)
[![PyPi](https://img.shields.io/pypi/v/linkml.svg)](https://pypi.python.org/pypi/linkml)
[![badge](https://img.shields.io/badge/launch-binder-579ACA.svg)](https://mybinder.org/v2/gh/linkml/linkml/main?filepath=notebooks)
[![DOI](https://zenodo.org/badge/13996/linkml/linkml.svg)](https://zenodo.org/badge/latestdoi/13996/linkml/linkml)
[![PyPIDownloadsTotal](https://pepy.tech/badge/linkml)](https://pepy.tech/project/linkml)
[![PyPIDownloadsMonth](https://img.shields.io/pypi/dm/linkml?logo=PyPI&color=blue)](https://pypi.org/project/linkml)
[![codecov](https://codecov.io/gh/linkml/linkml/branch/main/graph/badge.svg?token=WNQNG986UN)](https://codecov.io/gh/linkml/linkml)


# LinkML - Linked Data Modeling Language

LinkML is a linked data modeling language following object-oriented and ontological principles. LinkML models are typically authored in YAML, and can be converted to other schema representation formats such as JSON or RDF.

This repo holds the tools for generating and working with LinkML. For the LinkML schema (metamodel), please see https://github.com/linkml/linkml-model

The complete documentation for LinkML can be found here:

 - [linkml.io/linkml](https://linkml.io/linkml)

## `AGENTS.md`

# Claude Code Notes for LinkML

## Project Structure

This is a UV workspace monorepo that publishes **two PyPI packages**:

| Package | Source | Tests | PyPI |
| `linkml` | `packages/linkml/src/linkml/` | `tests/linkml/` | [linkml](https://pypi.org/project/linkml/) |
| `linkml-runtime` | `packages/linkml_runtime/src/linkml_runtime/` | `tests/linkml_runtime/` | [linkml-runtime](https://pypi.org/project/linkml-runtime/) |

All commands use `uv run` prefix (e.g., `uv run pytest`).

## Best Practices

* Read `.github/workflows/main.yaml` when something doesn't work locally - CI often has workarounds or uses external services that explain expected behavior.
* Use `uv run` - Always prefix commands with `uv run` to ensure the correct environment.
* Use doctests liberally—these serve as both explanatory examples for humans and as unit tests
* For longer examples, write pytest tests
* always write pytest functional style rather than unittest OO style
* use modern pytest idioms, including `@pytest.mark.parametrize` to test for combinations of inputs
* NEVER write mock tests unless requested. I need to rely on tests to know if something breaks
* For tests that have external dependencies, you can do `@pytest.mark.integration`
* Do not "fix" issues by changing or weakening test conditions. Try harder, or ask questions if a test fails.
* Avoid try/except blocks, these can mask bugs
* Failing fast is a good principle
* Follow the DRY principle
* Avoid repeating chunks of code, but also avoid premature over-abstraction
* Declarative principles are favored
* Always use type hints, always document methods and classes
* always use pytest, never unittest

## `CLAUDE.md`

AGENTS.md

## `CONTRIBUTING.md`

For information about contributing to this project, please visit our [contribution guidelines page](https://linkml.io/linkml/maintainers/contributing.html).

Please also review our [AI Covenant](AI_COVENANT.md), which establishes community norms for responsible AI use in contributions.

## `Dockerfile`

FROM python:3.12-bookworm AS builder

# https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker
ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  UV_VERSION=0.7.13

# Install uv
RUN pip install "uv==$UV_VERSION"


WORKDIR /code

# Build project. The .git directory is needed for uv-dynamic-versioning
COPY . .
RUN uv build --all-packages

#######################################
FROM python:3.12-slim-bookworm AS runner

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt update && apt install -y gcc musl-dev python3-dev && rm -rf /var/lib/apt/lists/*

COPY --from=builder /code/dist/*.whl /tmp/linkml-whl/
RUN pip install /tmp/linkml-whl/*.whl

RUN useradd --create-home linkmluser
WORKDIR /home/linkmluser
USER linkmluser

# command to run on container start
CMD [ "bash" ]

## `Makefile`

VERSION = $(shell git tag | tail -1)

SPECIFICATION.pdf: SPECIFICATION.md
	pandoc $< -o $@

# for now we only have one example
all-examples: all-examples-organization

# for each example schema, make all derived schema products, and derived serializations for the example data file
all-examples-%:  examples/%.py examples/%.schema.json  examples/%.shex  examples/%.graphql  examples/%.graphql  examples/%.shex examples/%.proto  examples/%.shex examples/%.valid examples/%-data.nt
	echo done

#RUN=pipenv run
RUN=uv run

lint-fix:
	$(RUN) tox -e format

format: lint-fix

test:
	$(RUN) pytest

# Metamodel compatibility: download latest metamodel from linkml-model
LINKML_MODEL_BRANCH ?= main
LINKML_MODEL_REPO = https://github.com/linkml/linkml-model.git
METAMODEL_DIR = tests/linkml/test_metamodel_compat/input/metamodel

download-metamodel:
	rm -rf temp/linkml-model
	git clone --depth 1 --branch $(LINKML_MODEL_BRANCH) $(LINKML_MODEL_REPO) temp/linkml-model
	rm -f $(METAMODEL_DIR)/*.yaml
	cp temp/linkml-model/linkml_model/model/schema/*.yaml $(METAMODEL_DIR)/
	sed -i.bak '/^#.*- linkml:/d' $(METAMODEL_DIR)/*.yaml
	sed -i.bak 's/- linkml:\([a-zA-Z_]*\)/- \1/g' $(METAMODEL_DIR)/*.yaml
	rm -f $(METAMODEL_DIR)/*.bak
	rm -rf temp/linkml-model

test-metamodel:
	mkdir -p temp
	$(RUN) pytest tests/linkml/test_metamodel_compat/ --with-slow -v 2>&1 | tee temp/test_output.txt

## Example schema products
examples/%.py: examples/%.yaml
	$(RUN) gen-py-classes $< > $@ && $(RUN) python -m examples.$*
examples/%.shex: examples/%.yaml
	$(RUN) gen-shex $< > $@
examples/%.schema.json: examples/%.yaml
	$(RUN) gen-json-schema -t $* $< > $@
examples/%.context.jsonld: examples/%.yaml
	$(RUN) gen-jsonld-context -t $* $< > $@
examples/%.graphql: examples/%.yaml
	$(RUN) gen-graphql $< > $@
examples/%.context.jsonld: examples/%.yaml
	$(RUN) gen-jsonld-context $< > $@
examples/%.jsonld: examples/%.yaml
	$(RUN) gen-jsonld $< > $@
examples/%.shex: examples/%.yaml
	$(RUN) gen-shex $< > $@
examples/%.proto: examples/%.yaml
	$(RUN) gen-proto $< > $@
examples/%.owl: examples/%.yaml
	$(RUN) gen-owl $< > $@
examples/%.ttl: examples/%.yaml
	$(RUN) gen-rdf $< > $@
examples/%-docs: examples/%.yaml
	$(RUN) gen-doc $< -d $@

## Example instance data products
examples/%.valid: examples/%-data.json examples/%.schema.json
	jsonschema -i $^
examples/%-data.jsonld: examples/%-data.json examples/%.context.jsonld
	jq -s '.[0] * .[1]' $^ > $@
examples/%-data.nt: examples/%-data.jsonld
	riot $< > $@

linkml/workspaces/datamodel/workspaces.py: linkml/workspaces/datamodel/workspaces.yaml
	$(RUN) gen-python $< > $@.tmp && mv $@.tmp $@

linkml/linter/config/datamodel/config.py: linkml/linter/config/datamodel/config.yaml
	$(RUN) gen-python $< > $@.tmp && mv $@.tmp $@

TUTORIALS = 01 02 03 04 05 06 07 08 09 10
test-tutorials: $(patsubst %, test-tutorial-%, $(TUTORIALS))
test-tutorial-%: docs/intro/tutorial%.md
	$(RUN) python -m linkml.utils.execute_tutorial -d /tmp/tutorial $<

build-generator-dashboard:
	$(RUN) pytest tests/linkml/test_compliance/ --with-output -q
	$(RUN) python scripts/generate_dashboard.py

docs:
	cd docs && $(RUN) make html

################################################
#### Commands for building the Docker image ####
################################################

IM=linkml/linkml

docker-build-no-cache:
	@docker build --no-cache -t $(IM):$(VERSION) . \
	&& docker tag $(IM):$(VERSION) $(IM):latest

docker-build:
	@docker build -t $(IM):$(VERSION) . \
	&& docker tag $(IM):$(VERSION) $(IM):latest

docker-build-use-cache-dev:
	@docker build -t $(DEV):$(VERSION) . \
	&& docker tag $(DEV):$(VERSION) $(DEV):latest

docker-clean:
	docker kill $(IM) || echo not running ;
	docker rm $(IM) || echo not made

docker-publish-no-build:
	@docker push $(IM):$(VERSION) \
	&& docker push $(IM):latest

docker-publish-dev-no-build:
	@docker push $(DEV):$(VERSION) \
	&& docker push $(DEV):latest

docker-publish: docker-build
	@docker push $(IM):$(VERSION) \
	&& docker push $(IM):latest

docker-run:
	@docker run  -v $(PWD):/work -w /work -ti $(IM):$(VERSION)

## `pyproject.toml`

[tool.uv]
required-version = ">=0.9.17"
exclude-newer = "7 days"
constraint-dependencies = ["click>=8.3.3,<8.4", "pillow>=12.3.0,<12.4"]

[tool.uv.workspace]
members = [
  "packages/linkml",
  "packages/linkml_runtime",
]
[tool.uv.sources]
linkml = { workspace = true }
linkml-runtime = { workspace = true }


[tool.codespell]
skip = [
  ".git", "*.pdf", "*.svg", "*.dill",
  "./tests",  # TODO: bring in tests in too
  "pyproject.toml",
  "uv.lock",
  "./notebooks/DistributedModels.ipynb",
  "./docs/LinkML-logo/LinkML-Revised-Round-Logo-MASTER-FILE.ai",
  "./tests/data/hp.ttl",
  "./tests/data/hp_f.ttl",
  "tests/test_generators/input/jsonschema_value_constraints.yaml",
]
# Ignore table where words could be split across rows
ignore-regex = '(\|.*\|.*\|.*\||\[[A-Z][a-z]\][a-z][a-z])'
ignore-words-list = [
  "acsess",
  "AGS",
  "amination",
  "anc",
  "brite",
  "ClassE",
  "CrossReference",
  "crossReference",
  "connexion",
  "EHR",
  "infarction",
  "linke",
  "mater",
  "mor",
  "ser",
  "Stye",
  "TE",
  "thirdparty",
  "Vas",
  # These are temp exemptions because they are coming from
  # upstream repos linkml-runtime and linkml-model
  # we should remove these once the upstream repos are fixed
  # and changes are propagated to linkml
  "GENERARE",
  "re-used",
  "doesnt",
  "crate"
]
quiet-level = 3

[tool.black]
line-length = 120
target-version = ["py310", "py311", "py312", "py313"]
force-exclude = '''
/(
  # default exclude
  \.direnv|\.eggs|\.git|\.hg|\.ipynb_checkpoints|\.mypy_cache|\.nox|\.pytest_cache|\.ruff_cache|\.tox|\.svn|\.venv|\.vscode|__pypackages__|_build|buck-out|build|dist|venv
  # additional exclude
  | tests.*/output
  | __snapshots__
  | docs
  | examples
  | notebooks
  | linkml/linter/config/datamodel
)/
'''

[tool.pytest.ini_options]
filterwarnings = [
  # https://github.com/RDFLib/rdflib/issues/1830
  "ignore:.*_pytestfixturefunction is not defined in namespace:UserWarning"
]
markers = [
  "network: test code paths that perform outbound requests; served from local stubs by default, live under --with-network",
  "upstream: tests whose assertions are about the real outside world; live-only, run weekly under --with-upstream",
  "slow: mark test as slow to run",
  "no_asserts: tests that don't have meaningful asserts, but are only snapshot comparisons, or historically had print statements, or other non-erroring behavior",
  "strcmp: tests that compare stringified values rather than the values themselves",
  "biolink: tests that validate that the biolink model is unchanged",
  "docker: tests that require a running docker server",
  "kroki: tests that use Kroki diagram creation (skipped in CI)",
  "plantumlgen: Tests for the plantuml generator",
  "pydanticgen_split: Split module generation in pydanticgen",
  "pydanticgen_npd: tests for the numpydantic array generator",
  "panderagen: tests for the pandera generator",
  "integration: tests that require external services (e.g. a running TypeDB server)",
  "dataframe_polars_schema: tests for the polars schema dataframe generator",
  "tutorial: tests that execute tutorial markdown files",
  "pythongen: Tests for python generator",
  "pydanticgen: Tests for pydantic generator",
  "javagen: Tests for java generator",
  "jsonschemagen: Tests for Json Schema generator",
  "shaclgen: Tests for shacl generator",
  "shexgen: Tests for shex generator",
  "jsonldgen: Test for JSON-LD generator",
  "jsonldcontextgen: Test for JSON-LD context generator",
  "rdfgen: Tests for the RDFGenerator",
  "rustgen: Tests for the RustGenerator",
  "sqlalchemygen: Tests for SQL Alchemy generator",
  "sqlddlgen: Tests for SQL DDL generator",
  "sqlddlpostgresgen: Tests for SQL DDL postgres generator",
  "sqlddlbigquerygen: Tests for BigQuery DDL generator",
  "owlgen: Tests for OWL generator",
  "yamlgen: Tests for the YAML generator",
  "yarrrml: End-to-end tests for the YARRRML generator",
  "typedbgen: Tests for the TypeDB generator",
  "arrays: Array specifications!",
]

# https://docs.astral.sh/ruff/settings/
[tool.ruff]
extend-exclude = [
    "tests/output",
    "tests/**/output",
    "tests/**/__snapshots__",
    "examples/",
    "docs/",
    "notebooks/",
    # Auto-generated files that may not conform to current linting rules
    "linkml/linter/config/datamodel/config.py"
]
force-exclude = true
line-length = 120
target-version = "py310"

[tool.ruff.lint]
extend-ignore = ["E203"]
select = [
  "E",  # pycodestyle errors
  "F",  # Pyflakes
  "I",  # isort
  "UP", # pyupgrade
]

[tool.ruff.format]
# Golden files are generated output whose formatting is determined by the code generator
exclude = ["tests/**/golden/*.py"]

[tool.ruff.lint.isort]
known-first-party = ["linkml", "linkml_runtime"]

[tool.ruff.lint.per-file-ignores]
# These templates can have long lines
"packages/linkml/src/linkml/generators/sqlalchemy/sqlalchemy_declarative_template.py" = ["E501"]
"packages/linkml/src/linkml/generators/sqlalchemy/sqlalchemy_declarative_2x_template.py" = ["E501"]
"packages/linkml/src/linkml/generators/sqlalchemy/sqlalchemy_imperative_template.py" = ["E501"]

# Golden files are generated output — may have unused imports, long lines, unsorted imports
"tests/**/golden/*.py" = ["E501", "F401", "I001"]
"packages/linkml/src/linkml/linter/config/datamodel/config.py" = ["E501", "F401", "I001", "UP007", "UP035", "UP045"]

# Auto-generated model files use Optional/Union with string forward references
"packages/linkml_runtime/src/linkml_runtime/linkml_model/*.py" = ["UP007", "UP045"]
"packages/linkml_runtime/src/linkml_runtime/processing/validation_datamodel.py" = ["UP007", "UP045"]
"packages/linkml/src/linkml/workspaces/datamodel/workspaces.py" = ["UP007", "UP045"]
"packages/linkml/src/linkml/reporting/model.py" = ["UP007", "UP045"]

# Notebooks can have unsorted imports
"tests/linkml/test_notebooks/input/*" = ["E402"]

# tests/linkml_runtime follows the original linkml_runtime linting conventions
"tests/linkml_runtime/**/*.py" = ["E402", "E501", "E712", "E731", "E741", "F401", "F811", "F841", "I001", "UP006", "UP007", "UP035", "UP045"]

[tool.tox]
requires = ["tox>=4", "tox-uv"]
env_list = ["lint", "py{310,311,312,313}"]

[tool.tox.env_run_base]
runner = "uv-venv-lock-runner"
deps = ["pytest"]
commands = [
  ["pytest", "{posargs}"],
]

[tool.tox.env.codespell]
description = "Run spell checkers."
runner = "uv-venv-runner"
skip_install = true
deps = [
  "codespell",
  "tomli", # required for getting config from pyproject.toml
]
commands = [
  ["codespell", "{posargs}"]
]

[tool.tox.env.format]
description = "Run code formatter and code-fixing linter."
runner = "uv-venv-runner"
skip_install = true
deps = ["pre-commit"]
commands = [
  ["pre-commit", "run", "--all-files", "--show-diff-on-failure", { replace = "posargs", extend = true }]
]

[tool.tox.env.lint]
description = "Run code linter and formatter (no fixes)."
runner = "uv-venv-runner"
skip_install = true
deps = ["ruff==0.11.13"]
commands = [
  ["ruff", "check", "{posargs:.}"],
  ["ruff", "format", "{posargs:.}"],
]

## `docs/README.md`

# Instructions for building LinkML documentation

These instructions are for the core developers of the LinkML framework.

Documentation source:

* [docs/ folder](https://github.com/linkml/linkml/tree/main/docs)
* deployed to: [https://linkml.io/linkml/](https://linkml.io/linkml/)

We use the sphinx framework.

## Instructions

To build the docs locally, first make sure you have the development dependencies installed which may not be the case if you pip-installed linkML. In the root folder of the linkML code, run

```bash
uv sync --group dev --group docs
```

Then use the make to build the documentation:

```bash
make docs
```

This will build docs in `_build/html/`. You can check these with your browser.

If you don't have make (on Windows) you can build the docs by:

```bash
cd docs
uv run make html
```

New versions of the documentation are published to GitHub pages by a workflow job for every merge to main.

## IMPORTANT

**never** run `make html` directly

If you do this then docstrings from linkml will not be included.
Always check the generator docs to ensure command line options are present.

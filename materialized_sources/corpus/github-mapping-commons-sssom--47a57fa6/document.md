# Repository semantic capsule: mapping-commons/sssom

- Commit: `40ad08f404fa5ca67146fddfa5f3ff3827074bf2`
- Default branch: `master`
- Description: mapping-commons/sssom
- Selected evidence files: 4 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

<!--[![DOI](https://zenodo.org/badge/13996/mapping-commons/sssom.svg)](https://zenodo.org/badge/latestdoi/13996/mapping-commons/sssom)-->

# A Simple Standard for Sharing Ontological Mappings (SSSOM)

<img src="src/docs/images/sssom-banner.png" />


SSSOM is a Simple Standard for Sharing Ontological Mappings, providing 

1. a TSV-based representation for ontology term mappings
1. a comprehensive set of standard metadata elements to describe mappings and 
1. a standard translation between the TSV and the Web Ontology Language (OWL). 

The SSSOM TSV format in particular is geared towards the needs of the wider bioinformatics community as a way to safely exchange mappings in an easily readable yet semantically well-specified manner. Consider this example of a simple mapping file:

| subject_id	| predicate_id	| object_id	| mapping_justification | subject_label	| object_label |
| --- | --- | --- | --- | --- | --- |
| HP:0009124	| skos:exactMatch	| MP:0000003	| semapv:LexicalMatching	| Abnormal adipose tissue morphology	| abnormal adipose tissue morphology |
| HP:0008551	| skos:exactMatch	| MP:0000018	| semapv:LexicalMatching	| Microtia	| small ears |
| HP:0000411	| skos:exactMatch	| MP:0000021	| semapv:LexicalMatching	| Protruding ear	| prominent ears |

SSSOM specifies all its metadata elements:

- subject_id
- predicate_id
- object_id
- mapping_justification (*NOTE: Since June 2022* `match_type` is being replaced by `mapping_justification` see [here](https://github.com/mapping-commons/sssom/issues/150))
- subject_label
- object_label

including clear definitions, examples of use and controlled vocabulary where necessary, along with 30 other optional metadata elements to provide additional provenance.

SSSOM further provides a standard way to 
- augment the TSV file with mapping set - level metadata, such as creator_id, mapping_date or license and
- translate a SSSOM compliant TSV files into _OWL reified axioms_. This will allow the easy loading, and merging of SSSOM mapping tables into existing ontologies using standard tools such as ROBOT (under development).

Note that SSSOM is currently under development and subject to change. Please leave us a comment on the [issue tracker](https://github.com/OBOFoundry/SSSOM/issues) if you want to be involved. The full specification can be found [here](https://w3id.org/sssom/spec).

## Citation

If you have found SSSOM to be helpful in your work, please consider citing:

Nicolas Matentzoglu, James P Balhoff, Susan M Bello, Chris Bizon, Matthew Brush, Tiffany J Callahan, Christopher G Chute, William D Duncan, Chris T Evelo, Davera Gabriel, John Graybeal, Alasdair Gray, Benjamin M Gyori, Melissa Haendel, Henriette Harmse, Nomi L Harris, Ian Harrow, Harshad B Hegde, Amelia L Hoyt, Charles T Hoyt, Dazhi Jiao, Ernesto Jiménez-Ruiz, Simon Jupp, Hyeongsik Kim, Sebastian Koehler, Thomas Liener, Qinqin Long, James Malone, James A McLaughlin, Julie A McMurry, Sierra Moxon, Monica C Munoz-Torres, David Osumi-Sutherland, James A Overton, Bjoern Peters, Tim Putman, Núria Queralt-Rosinach, Kent Shefchek, Harold Solbrig, Anne Thessen, Tania Tudorache, Nicole Vasilevsky, Alex H Wagner, Christopher J Mungall, A Simple Standard for Sharing Ontological Mappings (SSSOM), Database, Volume 2022, 2022, baac035, https://doi.org/10.1093/database/baac035

```bibtex
@article{10.1093/database/baac035,
    author = {Matentzoglu, Nicolas and Balhoff, James P and Bello, Susan M and Bizon, Chris and Brush, Matthew and Callahan, Tiffany J and Chute, Christopher G and Duncan, William D and Evelo, Chris T and Gabriel, Davera and Graybeal, John and Gray, Alasdair and Gyori, Benjamin M and Haendel, Melissa and Harmse, Henriette and Harris, Nomi L and Harrow, Ian and Hegde, Harshad B and Hoyt, Amelia L and Hoyt, Charles T and Jiao, Dazhi and Jiménez-Ruiz, Ernesto and Jupp, Simon and Kim, Hyeongsik and Koehler, Sebastian and Liener, Thomas and Long, Qinqin and Malone, James and McLaughlin, James A and McMurry, Julie A and Moxon, Sierra and Munoz-Torres, Monica C and Osumi-Sutherland, David and Overton, James A and Peters, Bjoern and Putman, Tim and Queralt-Rosinach, Núria and Shefchek, Kent and Solbrig, Harold and Thessen, Anne and Tudorache, Tania and Vasilevsky, Nicole and Wagner, Alex H and Mungall, Christopher J},
    title = "{A Simple Standard for Sharing Ontological Mappings (SSSOM)}",
    journal = {Database},
    volume = {2022},
    year = {2022},
    month = {05},
    abstract = "{Despite progress in the development of standards for describing and exchanging scientific information, the lack of easy-to-use standards for mapping between different representations of the same or similar objects in different databases poses a major impediment to data integration and interoperability. Mappings often lack the metadata needed to be correctly interpreted and applied. For example, are two terms equivalent or merely related? Are they narrow or broad matches? Or are they associated in some other way? Such relationships between the mapped terms are often not documented, which leads to incorrect assumptions and makes them hard to use in scenarios that require a high degree of precision (such as diagnostics or risk prediction). Furthermore, the lack of descriptions of how mappings were done makes it hard to combine and reconcile mappings, particularly curated and automated ones. We have developed the Simple Standard for Sharing Ontological Mappings (SSSOM) which addresses these problems by: (i) Introducing a machine-readable and extensible vocabulary to describe metadata that makes imprecision, inaccuracy and incompleteness in mappings explicit. (ii) Defining an easy-to-use simple table-based format that can be integrated into existing data science pipelines without the need to parse or query ontologies, and that integrates seamlessly with Linked Data principles. (iii) Implementing open and community-driven collaborative workflows that are designed to evolve the standard continuously to address changing requirements and mapping practices. (iv) Providing reference tools and software libraries for working with the standard. In this paper, we present the SSSOM standard, describe several use cases in detail and survey some of the existing work on standardizing the exchange of mappings, with the goal of making mappings Findable, Accessible, Interoperable and Reusable (FAIR). The SSSOM specification can be found at http://w3id.org/sssom/spec.Database URL: http://w3id.org/sssom/spec}",
    issn = {1758-0463},
    doi = {10.1093/database/baac035},
    url = {https://doi.org/10.1093/database/baac035},
    note = {baac035},
    eprint = {https://academic.oup.com/database/article-pdf/doi/10.1093/database/baac035/43832024/baac035.pdf},
}
```

A [second report with updates since the primary SSSOM publication](https://ceur-ws.org/Vol-3324/om2022_LTpaper6.pdf) above was published as part of the proceedings of the Ontology Matching Workshop 2022.

## Copying

SSSOM is distributed under the terms of the 3-clause BSD license, as included in the [LICENSE](LICENSE) file of the source distribution.

By exception, the following files are _not_ covered by the 3-clause BSD license:

* [sssom-banner.png](src/docs/images/sssom-banner.png): That file may only be used by members of the internal Monarch team and collaborators on Monarch flagship products.

## Pronunciation

The acronym SSSOM is pronounced as _sessom_. As a lighthearted joke, our community has also
compiled [alternate pronunciations](https://incenp.org/notes/2025/sssom-pronunciation-alignment-chart.html)
that have been heard in the wild.

## `CONTRIBUTING.md`

# Contributing to SSSOM

:+1: First of all: Thank you for taking the time to contribute!

The following is a set of guidelines for contributing to SSSOM. They are derived
from the excellent contribution guidelines for the
[ATOM Editor](https://github.com/atom/atom/blob/master/CONTRIBUTING.md) and are
mostly guidelines, not rules. Use your best judgment, and feel free to propose
changes to this document in a pull request.

#### Table Of Contents

[Code of Conduct](#code-of-conduct)

[I don't want to read this whole thing, I just have a question!!!](#i-dont-want-to-read-this-whole-thing-i-just-have-a-question)

[What should I know before I get started?](#what-should-i-know-before-i-get-started)

[How Can I Contribute?](#how-can-i-contribute)

- [Reporting Bugs](#reporting-bugs)
- [Your First Code Contribution](#your-first-code-contribution)
- [Pull Requests](#pull-requests)
- [Local Testing](#local-testing)
- [Making a release](#making-a-release)

[Style Guides](#styleguides)

- [Git Commit Messages](#git-commit-messages)
- [Documentation Styleguide](#documentation-styleguide)

[Additional Notes](#additional-notes)

- [Issue and Pull Request Labels](#issue-and-pull-request-labels)

## Code of Conduct

This project and everyone participating in it is governed by the
[SSSOM Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected
to uphold this code. Please report unacceptable behavior to
[a member of the SSSOM core team](https://mapping-commons.github.io/sssom/contact/).

## I don't want to read this whole thing I just have a question!!!

We have an official message board with a detailed FAQ and where the community
chimes in with helpful advice if you have questions.

- [GitHub Discussions](https://github.com/mapping-commons/sssom/discussions)
- [SSSOM FAQ](https://mapping-commons.github.io/sssom/faq/)

## What should I know before I get started?

- Read the [introduction](https://mapping-commons.github.io/sssom/introduction/)
- Do the [SSSOM tutorial](https://mapping-commons.github.io/sssom/tutorial/)
- Read about the [SSSOM toolkit](https://mapping-commons.github.io/sssom-py),
  which is managed
  [in a different repo](https://github.com/mapping-commons/sssom-py)

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report for SSSOM. Following
these guidelines helps maintainers and the community understand your report
:pencil:, reproduce the behavior :computer: :computer:, and find related reports
:mag_right:.

Before creating bug reports, please check
[this list](#before-submitting-a-bug-report) as you might find out that you
don't need to create one. When you are creating a bug report, please include as
many details as possible. Wherever available, use
[existing issue tracker templates](https://github.com/mapping-commons/sssom/issues/new/choose),
the information it asks for helps us resolve issues faster.

> **Note:** If you find a **Closed** issue that seems like it is the same thing
> that you're experiencing, open a new issue and include a link to the original
> issue in the body of your new one.

#### Before Submitting A Bug Report

- **Check the
  [discussions](https://github.com/mapping-commons/sssom/discussions)** for a
  list of common questions and problems.
- **Decide whether the issue should be reported in the tracker for the
  [SSSOM data model](https://github.com/mapping-commons/sssom/issues) or the
  tracker for the
  [SSSOM toolkit](https://github.com/mapping-commons/sssom-py/issues)**.
- **Perform a
  [cursory search](https://github.com/mapping-commons/sssom/issues)** to see if
  the problem has already been reported. If it has **and the issue is still
  open**, add a comment to the existing issue instead of opening a new one.

#### How Do I Submit A (Good) Bug Report or Feature request?

Bugs and feature requests are tracked as
[GitHub issues](https://guides.github.com/features/issues/). After you've
determined which repository your bug or feature is related to, create an issue
on that repository providing the information required by
[the appropriate template](https://github.com/mapping-commons/sssom/issues/new/choose).

Explain the problem and include additional details to help maintainers reproduce
the problem:

- **Use a clear and descriptive title** for the issue to identify the
  problem/requests.
- **Describe the exact steps which reproduce the problem** in as many details as
  possible. For example, start by explaining how you started SSSOM, e.g. which
  command exactly you used in the terminal, or how you started SSSOM otherwise.
  When listing steps, **don't just say what you did, but explain how you did
  it**. For example, if you moved the cursor to the end of a line, explain if
  you used the mouse, or a keyboard shortcut or an SSSOM command, and if so
  which one?
- **Provide specific examples to demonstrate the steps**. Include links to files
  or GitHub projects, or copy/pasteable snippets, which you use in those
  examples. If you're providing snippets in the issue, use
  [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
- **Describe the behavior you observed after following the steps** and point out
  what exactly is the problem with that behavior.
- **Explain which behavior you expected to see instead and why.**

Include details about your configuration and environment:

- **Which version of SSSOM toolkit/model are you using?** You can get the exact
  version by running `sssom --version` in your terminal
- **What's the name and version of the OS you're using**?

### Your First Code Contribution

Unsure where to begin contributing to SSSOM? You can start by looking through
these `beginner` and `help-wanted` issues:

- [Beginner issues][beginner] - issues which should only require a few lines of
  code, and a test or two.
- [Help wanted issues][help-wanted] - issues which should be a bit more involved
  than `beginner` issues.

### Considerations when proposing changes to the model

Now that SSSOM 1.0 has been released, and until we start working on a
hypothetical SSSOM 2.0, any proposed change to the SSSOM model must consider the
issue of backwards compatibility.

The key point is that _a set that is compliant with version 1.0 of the
specification must be usable “as is” with an implementation compliant with any
1.x version_.

This is automatically achieved if all the proposed changes do is _adding_ new
_optional_ slots, or _new_ enumeration values. For that reason, it is strongly
recommended that evolution of the 1.x branch be limited to this type of changes
only, and that other changes be reserved for a hypothetical version 2.0.

In addition, new slots must be marked with a `added_in` annotation indicating
the version in which the slot will be introduced, as in the following example:

```yaml
my_new_slot:
  instantiates:
    - sssom:Versionable
  annotations:
    added_in: "1.1"
```

### Pull Requests

The process described here has several goals:

- Maintain SSSOM's quality
- Fix problems that are important to users
- Engage the community in working toward the best possible data model and
  toolkit
- Enable a sustainable system for SSSOM's maintainers to review contributions

Please follow these steps to have your contribution considered by the
maintainers:

1. Follow all instructions in the pull request template (you will see them when
   you open a pull request).
2. Follow the [style guides](#styleguides)
3. After you submit your pull request, verify that all
   [status checks](https://help.github.com/articles/about-status-checks/) are
   passing <details><summary>What if the status checks are failing?</summary>If
   a status check is failing, and you believe that the failure is unrelated to
   your change, please leave a comment on the pull request explaining why you
   believe the failure is unrelated. A maintainer will re-run the status check
   for you. If we conclude that the failure was a false positive, then we will
   open an issue to track that problem with our status check suite.</details>

While the prerequisites above must be satisfied prior to having your pull
request reviewed, the reviewer(s) may ask you to complete additional design
work, tests, or other changes before your pull request can be ultimately
accepted.

### Local testing

Contributors are strongly advised to run the test suite locally even before
submitting a pull request.

Prepare the testing environment by running:

```console
$ make install
```

This only needs to be run once after cloning the repository. After that, the
test suite can be run anytime with

```console
$ make test
```

If you are making a change to the documentation/specification, you should also
check how your changes are rendered, by running

```console
$ make serve
```

and opening `http://127.0.0.1:8000/sssom/` with your browser.

Furthermore, any change to the LinkML model should also be tested against

## `Makefile`

MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:
.SUFFIXES:
.SECONDARY:

RUN = uv run
# get values from about.yaml file
SCHEMA_NAME = sssom_schema
SOURCE_SCHEMA_PATH = src/sssom_schema/schema/sssom_schema.yaml
SRC = src
DEST = project
PYMODEL = $(SRC)/$(SCHEMA_NAME)/datamodel
DOCDIR = docs
TEMPLATE_DIR = $(SRC)/doc-templates

# basename of a YAML file in model/
.PHONY: all clean

help: status
	@echo ""
	@echo "make all -- makes site locally"
	@echo "make install -- install dependencies"
	@echo "make setup -- initial setup"
	@echo "make test -- runs tests"
	@echo "make testdoc -- builds docs and runs local test server"
	@echo "make deploy -- deploys site"
	@echo "make update -- updates linkml version"
	@echo "make help -- show this help"
	@echo ""

status: check-config
	@echo "Project: $(SCHEMA_NAME)"
	@echo "Source: $(SOURCE_SCHEMA_PATH)"

setup: install gen-project gendoc git-init-add

install:
	uv sync
.PHONY: install

all: gen-project gendoc gen-excel get-context
%.yaml: gen-project
deploy: all mkd-gh-deploy

# generates all project files
gen-project: $(PYMODEL)
	$(RUN) gen-project \
		--exclude owl \
		-d $(DEST) $(SOURCE_SCHEMA_PATH) && mv $(DEST)/*.py $(PYMODEL)

test: validate-schema
	$(RUN) gen-project \
		--exclude owl \
		-d tmp $(SOURCE_SCHEMA_PATH) 
	$(RUN) pytest

validate-schema: $(SOURCE_SCHEMA_PATH)
	$(RUN) linkml lint --validate --validate-only $<

check-config:
	@(grep my-datamodel about.yaml > /dev/null && printf "\n**Project not configured**:\n\n  - Remember to edit 'about.yaml'\n\n" || exit 0)

convert-examples-to-%:
	$(patsubst %, $(RUN) linkml-convert  % -s $(SOURCE_SCHEMA_PATH) -C Person, $(shell find src/data/examples -name "*.yaml")) 

get-context:
	mkdir -p $(SRC)/$(SCHEMA_NAME)/context
	cp $(DEST)/jsonld/* $(SRC)/$(SCHEMA_NAME)/context

examples/%.yaml: src/data/examples/%.yaml
	$(RUN) linkml-convert -s $(SOURCE_SCHEMA_PATH) -C Person $< -o $@
examples/%.json: src/data/examples/%.yaml
	$(RUN) linkml-convert -s $(SOURCE_SCHEMA_PATH) -C Person $< -o $@
examples/%.ttl: src/data/examples/%.yaml
	$(RUN) linkml-convert -P EXAMPLE=http://example.org/ -s $(SOURCE_SCHEMA_PATH) -C Person $< -o $@

upgrade:
	uv add linkml --upgrade-package linkml

# Test documentation locally
serve: mkd-serve

# Python datamodel
$(PYMODEL):
	mkdir -p $@


$(DOCDIR):
	mkdir -p $@

gendoc: $(DOCDIR)
	cp -rf $(SRC)/docs/* $(DOCDIR) ; \
	$(RUN) jinjanate $(SRC)/doc-templates/frontpage.md.jinja2 $(SOURCE_SCHEMA_PATH) -o $(DOCDIR)/index.md
	$(RUN) gen-doc -d $(DOCDIR) $(SOURCE_SCHEMA_PATH) --template-directory $(TEMPLATE_DIR) --index-name linkml-index

testdoc: gendoc serve

MKDOCS = $(RUN) --all-groups mkdocs
mkd-%:
	$(MKDOCS) $*

deploy-doc:
	$(RUN) mike deploy --push dev

PROJECT_FOLDERS = sqlschema shex shacl protobuf prefixmap owl jsonschema jsonld graphql excel
git-init-add: git-init git-add git-commit git-status
git-init:
	git init
git-add:
	git add .gitignore .github Makefile LICENSE *.md examples utils about.yaml mkdocs.yml uv.lock project.Makefile pyproject.toml src/linkml/*yaml src/*/datamodel/*py src/data
	git add $(patsubst %, project/%, $(PROJECT_FOLDERS))
git-commit:
	git commit -m 'Initial commit' -a
git-status:
	git status

clean:
	rm -rf $(DEST)
	rm -rf tmp

yaml-lint-all:
	npx --yes prettier --check --prose-wrap always --write "**/*.yaml"
	npx --yes prettier --check --prose-wrap always --write "**/*.yml"

include project.Makefile

## `pyproject.toml`

[build-system]
requires = ["poetry-core>=1.0.0", "poetry-dynamic-versioning"]
build-backend = "poetry_dynamic_versioning.backend"

[project]
name = "sssom-schema"
description = "SSSOM is a Simple Standard for Sharing Ontology Mappings."
authors = [
  {name = "Nicolas Matentzoglu", email = "nicolas.matentzoglu@gmail.com"},
  {name = "Harshad Hegde", email = "hhegde@lbl.gov"},
]
license = "MIT"
license-files = ["LICENSE"]
readme = "README.md"
keywords = ["schema", "ontology", "mappings", "sssom"]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
]
requires-python = ">=3.10.0"
dynamic = ["version"]
dependencies = [
    "jinjanator",
    "linkml>=1.10.0",
    "linkml-runtime>=1.10.0",
]

[dependency-groups]
tests = [
    "pytest"
]
docs = [
    "mkdocs-material==9.0.0",
    "mkdocs-mermaid2-plugin==1.1.1",
    "mike"
]

[tool.poetry]
requires-poetry = ">=2.0"
version = "0.0.0"

[tool.poetry.dependencies]
python = "^3.10"

[tool.poetry.requires-plugins]
poetry-dynamic-versioning = ">=1.8.2"

[tool.poetry-dynamic-versioning]
enable = true
vcs = "git"
style = "pep440"

[tool.codespell]
# Ref: https://github.com/codespell-project/codespell#using-a-config-file
skip = '.git*,*.pdf,*.lock,*.svg'
check-hidden = true
ignore-regex = '\b(COMENT|EHR|LOD)\b'
ignore-words-list = 'disjointness'

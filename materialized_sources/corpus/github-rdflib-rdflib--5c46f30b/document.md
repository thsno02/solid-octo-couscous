# Repository semantic capsule: RDFLib/rdflib

- Commit: `a090f3f98f7c7c1ba21ec84a9acb001e88313caa`
- Default branch: `main`
- Description: RDFLib/rdflib
- Selected evidence files: 3 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

![](docs/_static/RDFlib.png)

# RDFLib

[![Build Status](https://github.com/RDFLib/rdflib/actions/workflows/validate.yaml/badge.svg?branch=main)](https://github.com/RDFLib/rdflib/actions?query=branch%3Amain)
[![Documentation Status](https://readthedocs.org/projects/rdflib/badge/?version=latest)](https://rdflib.readthedocs.io/en/latest/?badge=latest)
[![Coveralls branch](https://img.shields.io/coveralls/RDFLib/rdflib/main.svg)](https://coveralls.io/r/RDFLib/rdflib?branch=main)

[![GitHub stars](https://img.shields.io/github/stars/RDFLib/rdflib.svg)](https://github.com/RDFLib/rdflib/stargazers)
[![Downloads](https://pepy.tech/badge/rdflib/week)](https://pepy.tech/project/rdflib)
[![PyPI](https://img.shields.io/pypi/v/rdflib.svg)](https://pypi.python.org/pypi/rdflib)
[![PyPI](https://img.shields.io/pypi/pyversions/rdflib.svg)](https://pypi.python.org/pypi/rdflib)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6845245.svg)](https://doi.org/10.5281/zenodo.6845245)

[![Contribute with Gitpod](https://img.shields.io/badge/Contribute%20with-Gitpod-908a85?logo=gitpod)](https://gitpod.io/#https://github.com/RDFLib/rdflib)
[![Gitter](https://badges.gitter.im/RDFLib/rdflib.svg)](https://gitter.im/RDFLib/rdflib?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![Matrix](https://img.shields.io/matrix/rdflib:matrix.org?label=matrix.org%20chat)](https://matrix.to/#/#RDFLib_rdflib:gitter.im)

RDFLib is a pure Python package for working with [RDF](http://www.w3.org/RDF/). RDFLib contains most things you need to work with RDF, including:

* parsers and serializers for RDF/XML, N3, NTriples, N-Quads, Turtle, TriX, Trig, JSON-LD and even HexTuples
* a Graph interface which can be backed by any one of a number of Store implementations
* Store implementations for in-memory, persistent on disk (Berkeley DB) and remote SPARQL endpoints
    * additional Stores can be supplied via plugins 
* a SPARQL 1.1 implementation - supporting SPARQL 1.1 Queries and Update statements
* SPARQL function extension mechanisms

## RDFlib Family of packages
The RDFlib community maintains many RDF-related Python code repositories with different purposes. For example:

* [rdflib](https://github.com/RDFLib/rdflib) - the RDFLib core
* [sparqlwrapper](https://github.com/RDFLib/sparqlwrapper) - a simple Python wrapper around a SPARQL service to remotely execute your queries
* [pyLODE](https://github.com/RDFLib/pyLODE) - An OWL ontology documentation tool using Python and templating, based on LODE.
* [pyrdfa3](https://github.com/RDFLib/pyrdfa3) - RDFa 1.1 distiller/parser library: can extract RDFa 1.1/1.0 from (X)HTML, SVG, or XML in general.
* [pymicrodata](https://github.com/RDFLib/pymicrodata) - A module to extract RDF from an HTML5 page annotated with microdata.
* [pySHACL](https://github.com/RDFLib/pySHACL) - A pure Python module which allows for the validation of RDF graphs against SHACL graphs.
* [OWL-RL](https://github.com/RDFLib/OWL-RL) - A simple implementation of the OWL2 RL Profile which expands the graph with all possible triples that OWL RL defines.

Please see the list for all packages/repositories here:

* <https://github.com/RDFLib>

Help with maintenance of all of the RDFLib family of packages is always welcome and appreciated.

## Versions & Releases

* `main` branch in this repository is the current major release development branch for backwards-compatible fixes and features
* `next` branch in this repository is the next major release development branch
* `7.6.0` GraphDB Client, and many improvements and fixes. See changelog for details
* `7.5.0` RDF4J Store integration, RDF4J Client, and other improvements. See changelog for details
* `7.4.0` a few small fixes, add test matrix for active python versions, and move v7 documentation to MkDocs
* `7.3.0` many fixes and usability improvements, particularly for the Dataset class. See changelog for details
* `7.2.1` tiny clean up release, relaxes Python version requirement
* `7.2.0` general fixes and usability improvements, see changelog for details
* `7.1.4` tidy-up release, possibly last 7.x release
* `7.1.3` current stable release, small improvements to 7.1.1
* `7.1.2` previously deleted release
* `7.1.1` previous stable release
    * see <https://github.com/RDFLib/rdflib/releases/tag/7.1.1>
* `7.0.0` previous stable release, supports Python 3.8.1+ only.
    * see [Releases](https://github.com/RDFLib/rdflib/releases)
* `6.x.y` supports Python 3.7+ only. Many improvements over 5.0.0
    * see [Releases](https://github.com/RDFLib/rdflib/releases)
* `5.x.y` supports Python 2.7 and 3.4+ and is [mostly backwards compatible with 4.2.2](https://rdflib.readthedocs.io/en/stable/upgrade4to5.html).

See <https://github.com/RDFLib/rdflib/releases/> for the release details.

## Documentation
See <https://rdflib.readthedocs.io> for our documentation built from the code. Note that there are `latest`, `stable` and versioned builds, such as `5.0.0`, matching releases.

## Installation
The stable release of RDFLib may be installed with Python's package management tool *pip*:

    $ pip install rdflib

Some features of RDFLib require optional dependencies which may be installed using *pip* extras:

    $ pip install rdflib[berkeleydb,networkx,html,lxml,orjson]

Alternatively manually download the package from the Python Package
Index (PyPI) at https://pypi.python.org/pypi/rdflib

### Installation from the current development branch (for developers)

With *pip* you can also install rdflib from the git repository with one of the following options:

    $ pip install git+https://github.com/rdflib/rdflib@main

or

    $ pip install -e git+https://github.com/rdflib/rdflib@main#egg=rdflib

or from your locally cloned repository you can install it with one of the following options:

    $ uv sync  # installs into a uv-managed venv

or

    $ pip install -e .

## Getting Started
RDFLib aims to be a pythonic RDF API. RDFLib's main data object is a `Graph` which is a Python collection
of RDF *Subject, Predicate, Object* Triples:

To create graph and load it with RDF data from DBPedia then print the results:

```python
from rdflib import Graph
g = Graph()
g.parse('http://dbpedia.org/resource/Semantic_Web')

for s, p, o in g:
    print(s, p, o)
```
The components of the triples are URIs (resources) or Literals
(values).

URIs are grouped together by *namespace*, common namespaces are included in RDFLib:

```python
from rdflib.namespace import DC, DCTERMS, DOAP, FOAF, SKOS, OWL, RDF, RDFS, VOID, XMLNS, XSD
```

You can use them like this:

```python
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDFS, XSD

g = Graph()
semweb = URIRef('http://dbpedia.org/resource/Semantic_Web')
type = g.value(semweb, RDFS.label)
```
Where `RDFS` is the RDFS namespace, `XSD` the XML Schema Datatypes namespace and `g.value` returns an object of the triple-pattern given (or an arbitrary one if multiple exist).

Or like this, adding a triple to a graph `g`:

```python
g.add((
    URIRef("http://example.com/person/nick"),
    FOAF.givenName,
    Literal("Nick", datatype=XSD.string)
))
```

The triple (in n-triples notation) `<http://example.com/person/nick> <http://xmlns.com/foaf/0.1/givenName> "Nick"^^<http://www.w3.org/2001/XMLSchema#string> .`
is created where the property `FOAF.givenName` is the URI `<http://xmlns.com/foaf/0.1/givenName>` and `XSD.string` is the
URI `<http://www.w3.org/2001/XMLSchema#string>`.

You can bind namespaces to prefixes to shorten the URIs for RDF/XML, Turtle, N3, TriG, TriX & JSON-LD serializations:

```python
g.bind("foaf", FOAF)
g.bind("xsd", XSD)
```

This will allow the n-triples triple above to be serialised like this:

```python
print(g.serialize(format="turtle"))
```

With these results:
```turtle
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

<http://example.com/person/nick> foaf:givenName "Nick"^^xsd:string .
```

New Namespaces can also be defined:

```python
dbpedia = Namespace('http://dbpedia.org/ontology/')

abstracts = list(x for x in g.objects(semweb, dbpedia['abstract']) if x.language=='en')
```

See also [./examples](./examples)


## Features
The library contains parsers and serializers for RDF/XML, N3,
NTriples, N-Quads, Turtle, TriX, JSON-LD, RDFa and Microdata.

The library presents a Graph interface which can be backed by
any one of a number of Store implementations.

This core RDFLib package includes store implementations for
in-memory storage and persistent storage on top of the Berkeley DB.

A SPARQL 1.1 implementation is included - supporting SPARQL 1.1 Queries and Update statements.

RDFLib is open source and is maintained on [GitHub](https://github.com/RDFLib/rdflib/). RDFLib releases, current and previous
are listed on [PyPI](https://pypi.python.org/pypi/rdflib/)

Multiple other projects are contained within the RDFlib "family", see <https://github.com/RDFLib/>.

## Running tests

### Running the tests on the host

Run the test suite with `pytest`.
```shell
uv sync --group tests
uv run pytest
```

### Running test coverage on the host with coverage report

Run the test suite and generate a HTML coverage report with `pytest` and `pytest-cov`.
```shell
uv run pytest --cov
```

### Viewing test coverage

Once tests have produced HTML output of the coverage report, view it by running:
```shell
uv run pytest --cov --cov-report term --cov-report html

## `pyproject.toml`

[project]
name = "rdflib"
version = "7.7.0a0"
description = """RDFLib is a Python library for working with RDF, \
a simple yet powerful language for representing information."""
authors = [{ name = "Daniel 'eikeon' Krech", email = "eikeon@eikeon.com" }]
maintainers = [{ name = "RDFLib Team", email = "rdflib-dev@googlegroups.com" }]
license = { text = "BSD-3-Clause" }
classifiers=[
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
    "License :: OSI Approved :: BSD License",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Operating System :: OS Independent",
    "Natural Language :: English"
]
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "isodate>=0.7.2,<1.0.0; python_version < '3.11'",
    "pyparsing>=3.1.0,<4",
]

[project.urls]
Repository = "https://github.com/RDFLib/rdflib"
Documentation = "https://rdflib.readthedocs.org/"

[project.scripts]
rdfpipe = 'rdflib.tools.rdfpipe:main'
csv2rdf = 'rdflib.tools.csv2rdf:main'
rdf2dot = 'rdflib.tools.rdf2dot:main'
rdfs2dot = 'rdflib.tools.rdfs2dot:main'
rdfgraphisomorphism = 'rdflib.tools.graphisomorphism:main'
sparqlquery = 'rdflib.tools.sparqlquery:main'

[project.optional-dependencies]
berkeleydb = ["berkeleydb>=18.1.0,<19.0.0"]
networkx = ["networkx>=2.8.8,<4"]
html = ["html5rdf>=1.2,<2"]
lxml = ["lxml>=4.6.5,<6.0"]
orjson = ["orjson>=3.9.14,<4"]
rdf4j = ["httpx>=0.28.1,<0.29.0"]
graphdb = ["httpx>=0.28.1,<0.29.0"]

[dependency-groups]
dev = [
    "black==24.8.0",
    "isort>=5.13.2,<6.0.0",
    "mypy==2.3.1",
    "lxml-stubs>=0.4,<0.6",
    "pip-tools>=7.4.1,<8.0.0",
]
tests = [
    "pytest>=7.1.3,<9.0.0",
    "pytest-cov>=4,<6",
    "coverage[toml]>=7.0.1,<8.0.0",
    "types-setuptools>=68.0.0.3,<72.0.0.0",
    "setuptools>=68,<72",
    "wheel>=0.42,<0.46",
    "testcontainers>=4.13.2,<5.0.0",
]
coverage = ["coveralls==4.1.0; python_version >= '3.10'"]
docs = [
    "typing-extensions>=4.11.0,<5.0.0",
    "zensical>=0.0.51; python_version >= '3.11'",
# Set python to 3.11 or greater as that's what's used in the validate workflow to test doc builds.
    "mkdocstrings[python]>=1.0.6; python_version >= '3.11'",
    "httpx>=0.28.1,<0.29.0",
]
lint = ["ruff==0.15.0"]

[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
include = ["rdflib*"]

[tool.ruff]
# https://beta.ruff.rs/docs/configuration/
target-version = "py310"
# Same as Black.
line-length = 88

[tool.ruff.lint]
select = [
    "E", # pycodestyle errors
    "W", # pycodestyle warnings
    "F", # Pyflakes
    "I", # isort
    "N", # pep8-naming
    "RUF100", # Unused noqa directive
    "UP001", # Remove unused imports
    "UP003", # Use {} instead of type(...)
    "UP004", # Class inherits from object
    "UP005", # is deprecated, use
    "UP009", # UTF-8 encoding declaration is unnecessary
    "UP010", # Unnecessary __future__ import for target Python version
    "UP011", # Unnecessary parentheses to functools.lru_cache
    "UP012", # Unnecessary call to encode as UTF-8
    "UP017", # Use datetime.UTC alias
    "UP018", # Unnecessary {literal_type} call (rewrite as a literal)
    "UP019", # typing.Text is deprecated, use str
    "UP020", # Use builtin open
    "UP021", # universal_newlines is deprecated, use text
    "UP022", # Sending stdout and stderr to PIPE is deprecated, use capture_output
    "UP023", # cElementTree is deprecated, use ElementTree
    "UP024", # Replace aliased errors with OSError
    "UP025", # Remove unicode literals from strings
    "UP026", # mock is deprecated, use unittest.mock
    "UP029", # Unnecessary builtin import
    "UP034", # Avoid extraneous parentheses
    "UP036", # Version block is outdated for minimum Python version
    "UP037", # Remove quotes from type annotation
    "UP039", # Unnecessary parentheses after class definition
    "FA", # flake8-future-annotations
]

ignore = [
    "E501", # line too long:
    # Disabled based on black recommendations
    # https://black.readthedocs.io/en/stable/faq.html#why-are-flake8-s-e203-and-w503-violated
    "E203", # whitespace before ':'
    "E231", # missing whitespace after ','
]

[tool.ruff.lint.per-file-ignores]
"rdflib/plugins/sparql/*" = [
    "N801", # Class name should be UpperCamelCase
    "N802", # Function name should be lowercase
    "N803", # Argument name should be lowercase
    "N806", # Variable in function should be lowercase
    "N812", # Lowercase imported as non lowercase
    "N816", # Variable in class scope should be mixedCase
]
"rdflib/namespace/_*" = [
    "N815", # Variable in class scope should not be mixedCase
    "N999", # Invalid module name
]
"rdflib/plugins/parsers/{trix,rdfxml,notation3}.py" = [
    "N802", # Function name should be lowercase
    "N803", # Argument name should be lowercase
    "N806", # Variable in function should be lowercase
    "N816", # Variable in class scope should be mixedCase
]
"rdflib/plugins/serializers/{turtle,longturtle,trig}.py" = [
    "N802", # Function name should be lowercase
    "N806", # Variable in function should be lowercase
    "N815", # Variable in class scope should not be mixedCase
]
"test/utils/namespace/_*" = [
    "N815", # Variable in class scope should not be mixedCase
    "N999", # Invalid module name
]
"{test/conftest.py,rdflib/namespace/__init__.py,rdflib/__init__.py,rdflib/plugins/sparql/__init__.py}" = [
    "E402", # Module level import not at top of file
]

[tool.black]
line-length = 88
target-version = ['py310']
required-version = "24.8.0"
include = '\.pyi?$'
exclude = '''
(
  /(
      \.eggs         # exclude a few common directories in the
    | \.git          # root of the project
    | \.hg
    | \.mypy_cache
    | \.pytest_cache
    | \.tox
    | \.venv
    | \.var
    | \.github
    | site
    | htmlcov
    | benchmarks
    | test_reports
    | rdflib.egg-info
    | buck-out
    | build
    | dist
    | venv
  )/
)
'''

[tool.pytest.ini_options]
addopts = [
    "--doctest-modules",
    "--ignore=admin",
    "--ignore=devtools",
    "--ignore=rdflib/extras/external_graph_libs.py",
    "--ignore=rdflib/contrib/graphdb/client.py",
    "--ignore=rdflib/contrib/rdf4j/client.py",
    "--ignore-glob=docs/*.py",
    "--ignore-glob=site/*",
    "--strict-markers",
]
filterwarnings = [
    # The below warning is a consequence of how pytest doctest detects mocks and how DefinedNamespace behaves when an undefined attribute is being accessed.
    "ignore:Code. pytest_mock_example_attribute_that_shouldnt_exist is not defined in namespace .*:UserWarning",
    # The below warning is a consequence of how pytest detects fixtures and how DefinedNamespace behaves when an undefined attribute is being accessed.
    "ignore:Code. _pytestfixturefunction is not defined in namespace .*:UserWarning",
]
markers = [
    "testcontainer: mark a test that uses testcontainer",
    "webtest: mark a test as using the internet",
]
# log_cli = true
# log_cli_level = "DEBUG"
log_format = "%(asctime)s.%(msecs)03d %(levelname)-8s %(name)-12s %(filename)s:%(lineno)s:%(funcName)s %(message)s"
log_date_format = "%Y-%m-%dT%H:%M:%S"
log_cli_format = "%(asctime)s.%(msecs)03d %(levelname)-8s %(name)-12s %(filename)s:%(lineno)s:%(funcName)s %(message)s"

## `docs/index.md`

# RDFLib

RDFLib is a pure Python package for working with [RDF](http://www.w3.org/RDF/). It contains:

* **Parsers & Serializers**
    * for RDF/XML, N3, NTriples, N-Quads, Turtle, TriG, TriX, JSON-LD, HexTuples, RDFa and Microdata

* **Store implementations**
    * memory stores
    * persistent, on-disk stores, using databases such as BerkeleyDB
    * remote SPARQL endpoints

* **Graph interface**
    * to a single graph
    * or to multiple Named Graphs within a dataset

* **SPARQL 1.1 implementation**
    * both Queries and Updates are supported

!!! warning "Security considerations"
    RDFLib is designed to access arbitrary network and file resources, in some
    cases these are directly requested resources, in other cases they are
    indirectly referenced resources.

    If you are using RDFLib to process untrusted documents or queries you should
    take measures to restrict file and network access.

    For information on available security measures, see the RDFLib
    [Security Considerations](security_considerations.md)
    documentation.

## Getting started

If you have never used RDFLib, the following will help get you started:

* [Getting Started](gettingstarted.md)
* [Introduction to Parsing](intro_to_parsing.md)
* [Introduction to Creating RDF](intro_to_creating_rdf.md)
* [Introduction to Graphs](intro_to_graphs.md)
* [Introduction to SPARQL](intro_to_sparql.md)
* [Utilities](utilities.md)
* [Examples](apidocs/examples.md)

## In depth

If you are familiar with RDF and are looking for details on how RDFLib handles it, these are for you:

* [RDF Terms](rdf_terms.md)
* [Namespaces and Bindings](namespaces_and_bindings.md)
* [Persistence](persistence.md)
* [Merging](merging.md)
* [Changelog](changelog.md)
* [Upgrade 6 to 7](upgrade6to7.md)
* [Upgrade 5 to 6](upgrade5to6.md)
* [Upgrade 4 to 5](upgrade4to5.md)
* [Security Considerations](security_considerations.md)

## Versioning

RDFLib follows [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html), which can be summarised as follows:

Given a version number `MAJOR.MINOR.PATCH`, increment the:

1. `MAJOR` version when you make incompatible API changes
2. `MINOR` version when you add functionality in a backwards-compatible manner
3. `PATCH` version when you make backwards-compatible bug fixes

## For developers

* [Developers guide](developers.md)
* [Documentation guide](docs.md)
* [Contributing guide](CONTRIBUTING.md)
* [Code of Conduct](CODE_OF_CONDUCT.md)
* [Persisting N3 Terms](persisting_n3_terms.md)
* [Type Hints](type_hints.md)
* [Decisions](decisions.md)

## Source Code

The rdflib source code is hosted on GitHub at [https://github.com/RDFLib/rdflib](https://github.com/RDFLib/rdflib) where you can lodge Issues and create Pull Requests to help improve this community project!

The RDFLib organisation on GitHub at [https://github.com/RDFLib](https://github.com/RDFLib) maintains this package and a number of other RDF and RDFLib-related packaged that you might also find useful.

## Further help & Contact

If you would like help with using RDFLib, rather than developing it, please post a question on StackOverflow using the tag `[rdflib]`. A list of existing `[rdflib]` tagged questions can be found [here](https://stackoverflow.com/questions/tagged/rdflib).

You might also like to join RDFLib's [dev mailing list](https://groups.google.com/group/rdflib-dev) or use RDFLib's [GitHub discussions section](https://github.com/RDFLib/rdflib/discussions).

The chat is available at [gitter](https://gitter.im/RDFLib/rdflib) or via matrix [#RDFLib_rdflib:gitter.im](https://matrix.to/#/#RDFLib_rdflib:gitter.im).


## History

RDFLib is one of the oldest continuously maintained Python libraries for Semantic Web/RDF work. Its history goes back 
to 2002, only a few years after RDF itself emerged from the W3C. The original author was Daniel “eikeon” Krech but, of 
course, there have been many, many contributors to it since then, just see the long and illustrious file of 
[CONTRIBUTORS](https://github.com/RDFLib/rdflib/blob/main/CONTRIBUTORS).

<h3 id="timeline-summary">Timeline summary</h3>

* **2002** — RDFLib begins
* **2004** — RDFLib 2.0
* **2005** — modern Graph abstraction emerges
* **2006** — SPARQL first supported
* **2010** — RDFLib 3.0; SPARQL temporarily separated into rdfextras
* **2013** — RDFLib 4.0; SPARQL 1.1 returns to core; Dataset introduced
* **2017** — 4.2.2, followed by a long stable period
* **2020** — RDFLib 5.0; final Python-2-supporting major version
* **2021** — RDFLib 6.0; Python 3 only, JSON-LD integrated
* **2023** — RDFLib 7.0
* **2026** — RDFLib 7.6, with RDF4J/GraphDB integration.

<h3 id="early-years">Early Years</h3>

RDFLib already had RDF/XML parsing, literals, blank nodes, triple stores and serialization right back in November 2002
with the 1.1 release with context support - now Named Graphs - appearing in December of that same year.

RDFLib 2.1, released in April 2005, merged the previous TripleStore and InformationStore concepts into the Graph class
which remains the centre of RDFLib today. N3 support arrived in the 2.3 series, and SPARQL query support was added in 
RDFLib 2.3.2 in August 2006.

<h3 id="teenager">Teenager</h3>

RDFLib 3.0.0 was released on 13 May 2010 and move a lot of functionality into plugins, to keep the core small. This is
still the approach today with RDF inferencing recently being added as a plugin.

In 2013, RDF 1.1 features started appearing in the 4.x releases and `SPARQStore` too. For the 4.1 release, RDFLib had 
over 2,000 unit tests.

<h3 id="stable-times">Stable times</h3>

From 2017 to 2020, RDFLib 4.2.2 was the stable release with 5.0.0 in April 2020 just rolling up small fixes and 
improvements that had accumulated over time: no major changes

<h3 id="post-python-2">Post Python 2</h3>

Version 6.0.0 arrived on 20 July 2021, dropping Python 2 and Python versions before 3.7. JSON-LD handling was 
internalised and type annotations started to get applied widely.

<h3 id="7-and-beyond">7 and beyond</h3>

RDFLib 7.0.0 was released on 2 August 2023. Its breaking changes were small, but it began cleaning up some long-standing 
RDFLib behaviours, particularly around `Dataset`, default graphs and the `publicID` argument to `parse()`. Python 3.7 
support was dropped.

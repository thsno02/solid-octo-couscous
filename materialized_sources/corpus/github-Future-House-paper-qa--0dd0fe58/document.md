# Repository semantic capsule: Future-House/paper-qa

- Commit: `57e89f7223b0960d5ee5ea048c69e3c47e088572`
- Default branch: `main`
- Description: Future-House/paper-qa
- Selected evidence files: 3 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

# PaperQA2

<!-- pyml disable-num-lines 6 line-length -->

[![GitHub](https://img.shields.io/badge/GitHub-black?logo=github&logoColor=white)](https://github.com/Future-House/paper-qa)
[![PyPI version](https://badge.fury.io/py/paper-qa.svg)](https://badge.fury.io/py/paper-qa)
[![tests](https://github.com/Future-House/paper-qa/actions/workflows/tests.yml/badge.svg)](https://github.com/Future-House/paper-qa)
![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)
![PyPI Python Versions](https://img.shields.io/pypi/pyversions/paper-qa)

PaperQA2 is a package for doing high-accuracy retrieval augmented generation (RAG) on PDFs, text files, Microsoft Office documents, and source code files,
with a focus on the scientific literature.
See our [recent 2024 paper](https://paper.wikicrow.ai)
to see examples of PaperQA2's superhuman performance in scientific tasks like
question answering, summarization, and contradiction detection.

<!--TOC-->

---

**Table of Contents**

- [Quickstart](#quickstart)
  - [Example Output](#example-output)
- [What is PaperQA2](#what-is-paperqa2)
  - [PaperQA2 vs PaperQA](#paperqa2-vs-paperqa)
  - [PaperQA2 Goes CalVer in December 2025](#paperqa2-goes-calver-in-december-2025)
  - [What's New in Version 5 (aka PaperQA2)?](#whats-new-in-version-5-aka-paperqa2)
  - [What's New in December 2025?](#whats-new-in-december-2025)
  - [PaperQA2 Algorithm](#paperqa2-algorithm)
- [Installation](#installation)
- [CLI Usage](#cli-usage)
  - [Bundled Settings](#bundled-settings)
  - [Rate Limits](#rate-limits)
- [Library Usage](#library-usage)
  - [Agentic Adding/Querying Documents](#agentic-addingquerying-documents)
  - [Manual (No Agent) Adding/Querying Documents](#manual-no-agent-addingquerying-documents)
  - [Async](#async)
  - [Choosing Model](#choosing-model)
    - [Locally Hosted](#locally-hosted)
  - [Embedding Model](#embedding-model)
    - [Specifying the Embedding Model](#specifying-the-embedding-model)
    - [Local Embedding Models (Sentence Transformers)](#local-embedding-models-sentence-transformers)
  - [Adjusting number of sources](#adjusting-number-of-sources)
  - [Using Code or HTML](#using-code-or-html)
  - [Multimodal Support](#multimodal-support)
  - [Using External DB/Vector DB and Caching](#using-external-dbvector-db-and-caching)
  - [Creating Index](#creating-index)
    - [Manifest Files](#manifest-files)
  - [Reusing Index](#reusing-index)
  - [Using Clients Directly](#using-clients-directly)
- [Settings Cheatsheet](#settings-cheatsheet)
- [Where do I get papers?](#where-do-i-get-papers)
- [Callbacks](#callbacks)
  - [Caching Embeddings](#caching-embeddings)
- [Customizing Prompts](#customizing-prompts)
  - [Pre and Post Prompts](#pre-and-post-prompts)
- [FAQ](#faq)
  - [How come I get different results than your papers?](#how-come-i-get-different-results-than-your-papers)
  - [How is this different from LlamaIndex or LangChain?](#how-is-this-different-from-llamaindex-or-langchain)
  - [Can I save or load?](#can-i-save-or-load)
- [Reproduction](#reproduction)
- [Citation](#citation)

---

<!--TOC-->

## Quickstart

In this example we take a folder of research paper PDFs,
magically get their metadata - including citation counts with a retraction check,
then parse and cache PDFs into a full-text search index,
and finally answer the user question with an LLM agent.

```bash
pip install paper-qa
mkdir my_papers
curl -o my_papers/PaperQA2.pdf https://arxiv.org/pdf/2409.13740
cd my_papers
pqa ask 'What is PaperQA2?'
```

### Example Output

Question: Has anyone designed neural networks that compute with proteins or DNA?

> The claim that neural networks have been designed to compute with DNA is supported by multiple sources.
> The work by Qian, Winfree, and Bruck demonstrates the use of DNA strand displacement cascades
> to construct neural network components, such as artificial neurons and associative memories,
> using a DNA-based system (Qian2011Neural pages 1-2, Qian2011Neural pages 15-16, Qian2011Neural pages 54-56).
> This research includes the implementation of a 3-bit XOR gate and a four-neuron Hopfield associative memory,
> showcasing the potential of DNA for neural network computation.
> Additionally, the application of deep learning techniques to genomics,
> which involves computing with DNA sequences, is well-documented.
> Studies have applied convolutional neural networks (CNNs) to predict genomic features such as
> transcription factor binding and DNA accessibility (Eraslan2019Deep pages 4-5, Eraslan2019Deep pages 5-6).
> These models leverage DNA sequences as input data,
> effectively using neural networks to compute with DNA.
> While the provided excerpts do not explicitly mention protein-based neural network computation,
> they do highlight the use of neural networks in tasks related to protein sequences,
> such as predicting DNA-protein binding (Zeng2016Convolutional pages 1-2).
> However, the primary focus remains on DNA-based computation.

## What is PaperQA2

PaperQA2 is engineered to be the best agentic RAG model for working with scientific papers.
Here are some features:

- A simple interface to get good answers with grounded responses containing in-text citations.
- State-of-the-art implementation including document metadata-awareness
  in embeddings and LLM-based re-ranking and contextual summarization (RCS).
- Support for agentic RAG, where a language agent can iteratively refine queries and answers.
- Automatic redundant fetching of paper metadata,
  including citation and journal quality data from multiple providers.
- A usable full-text search engine for a local repository of PDF/text files.
- A robust interface for customization, with default support for all [LiteLLM][LiteLLM providers] models.

[LiteLLM providers]: https://docs.litellm.ai/docs/providers
[LiteLLM general docs]: https://docs.litellm.ai/docs/

By default, it uses [OpenAI embeddings](https://platform.openai.com/docs/guides/embeddings)
and [models](https://platform.openai.com/docs/models) with a Numpy vector DB to embed and search documents.
However, you can easily use other closed-source, open-source models or embeddings (see details below).

PaperQA2 depends on some awesome libraries/APIs that make our repo possible.
Here are some in no particular order:

1. [Semantic Scholar](https://www.semanticscholar.org/)
2. [Crossref](https://www.crossref.org/)
3. [Unpaywall](https://unpaywall.org/)
4. [Pydantic](https://docs.pydantic.dev/latest/)
5. [tantivy](https://github.com/quickwit-oss/tantivy)
6. [LiteLLM][LiteLLM general docs]
7. [pybtex](https://pybtex.org/)

### PaperQA2 vs PaperQA

We've been working hard on fundamental upgrades for a while
and mostly followed [SemVer](https://semver.org/), until [December 2025](#paperqa2-goes-calver-in-december-2025).
Meaning we've incremented the major version number on each breaking change.
This brings us to the current major version number v5.
So why call is the repo now called PaperQA2?
We wanted to remark on the fact though that we've
exceeded human performance on [many important metrics](https://paper.wikicrow.ai).
So we arbitrarily call version 5 and onward PaperQA2,
and versions before it as PaperQA1 to denote the significant change in performance.
We recognize that we are challenged at naming and counting at FutureHouse,
so we reserve the right at any time to arbitrarily change the name to PaperCrow.

### PaperQA2 Goes CalVer in December 2025

Prior to December 2025 we used [semantic versioning](https://semver.org/).
This eventually led to confusion in two ways:

1. Developers: should we major version bump based on
   settings or fundamental system capabilities?
   What if a bug fix requires breaking changes to the agent's behaviors?
2. Speaking: should one use terminology from our publications
   (e.g. [PaperQA1](https://arxiv.org/abs/2312.07559),
   [PaperQA2](https://arxiv.org/abs/2409.13740))
   or the Git tags (e.g. v5) from this repo/package?
   When someone says "PaperQA" -- what version do they mean?

To resolve these confusions, in December 2025,
we moved to [calendar versioning](https://calver.org/).
The developer burden is diminished because
we're basically removing guarantees of backwards compatibility across releases
(as CalVer is [ZeroVer](https://0ver.org/) bound to dates).
It solves the "speaking" issue because Git tags are now
quite different from publication terminology (e.g. PaperQA2 vs `v2025.12.17`).
When someone says "PaperQA" it will just refer to the system,
not a particular snapshot of agentic behaviors.
When someone says "PaperQA2" it will refer to `paper-qa>=5`,
which applies to both SemVer tags `v5.0.0` and the new CalVer tags `v2025.12.17`.

This switch is backwards compatible for version 5's SemVer,
as the year 2025 is strictly greater than major version 5.

### What's New in Version 5 (aka PaperQA2)?

Version 5 added:

- A CLI `pqa`
- Agentic workflows invoking tools for
  paper search, gathering evidence, and generating an answer
- Removed much of the statefulness from the `Docs` object
- A migration to LiteLLM for compatibility with many LLM providers
  as well as centralized rate limits and cost tracking
- A bundled set of configurations (read [this section here](#bundled-settings)))
  containing known-good hyperparameters

Note that `Docs` objects pickled from prior versions of `PaperQA` are incompatible with version 5,
and will need to be rebuilt.
Also, our minimum Python version was increased to Python 3.11.

### What's New in December 2025?

The last four months since version `5.29.1` have seen many changes:

- New modalities: tables, figures, non-English languages, math equations
- More and better readers
  - Two new _model-based_ PDF readers: [Docling](packages/paper-qa-docling)
    and [Nvidia nemotron-parse](packages/paper-qa-nemotron)
  - All PDF readers now can parse images and tables, report page numbers,
    support DPI
  - A reader for Microsoft Office data types
- Multimodal contextual summarization
  - Media objects are also passed to the `summary_llm` during creation
  - Media objects' embedding space is enhanced using an `enrichment_llm` prompt
- Simpler and performant HTTP stack
  - Consolidation from `aiohttp` and `httpx` to just `httpx`
  - Integration with [`httpx-aiohttp`](https://github.com/karpetrosyan/httpx-aiohttp) for performance
- `Context` relevance is simplified and some assumptions were removed
- Many minor features such as
  retrying `Context` creation upon invalid JSON,
  compatibility with fall 2025's frontier LLMs,
  and improved prompt templates
- Multiple fixes in metadata processing via Semantic Scholar and OpenAlex,
  and metadata processing

## `CONTRIBUTING.md`

# Contributing to PaperQA

Thank you for your interest in contributing to PaperQA!
Here are some guidelines to help you get started.

## Setting up the development environment

We use [`uv`](https://github.com/astral-sh/uv) for our local development.

1. Install `uv` by following the instructions on the [uv website](https://astral.sh/uv/).
2. Run the following command to install all dependencies and set up the development environment:

   ```bash
   uv sync
   ```

## Installing the package for development

If you prefer to use `pip` for installing the package in development mode, you can do so by running:

```bash
pip install -e ".[dev]"
```

Where the `dev` extra includes development dependencies such as `pytest`.

## Running tests and other tooling

Use the following commands:

- Run tests (requires an OpenAI key in your environment)

  ```bash
  pytest
  # or for multiprocessing based parallelism
  pytest -n auto
  ```

- Run `pre-commit` for formatting and type checking

  ```bash
  pre-commit run --all-files
  ```

- Run `mypy`, `refurb`, or `pylint` directly:

  ```bash
  mypy paperqa
  # or
  refurb paperqa
  # or
  pylint paperqa
  ```

See our GitHub Actions [`tests.yml`](.github/workflows/tests.yml) for further reference.

## Using `pytest-recording` and VCR cassettes

We use the [`pytest-recording`](https://github.com/kiwicom/pytest-recording) plugin
to create VCR cassettes to cache HTTP requests,
making our unit tests more deterministic.

To record a new VCR cassette:

```bash
uv run pytest --record-mode=once tests/desired_test_module.py
```

And the new cassette(s) should appear in [`tests/cassettes`](tests/cassettes).

Our configuration for `pytest-recording` can be found in [`tests/conftest.py`](tests/conftest.py).
This includes header removals (e.g. OpenAI `authorization` key)
from responses to ensure sensitive information is excluded from the cassettes.

Please ensure cassettes are less than 1 MB
to keep tests loading quickly.

Happy coding!

## `pyproject.toml`

[build-system]
build-backend = "setuptools.build_meta"
requires = ["setuptools>=64", "setuptools_scm>=8"]

[dependency-groups]
dev = [
    "paper-qa-docling[dev]",
    "paper-qa-nemotron[dev]",
    "paper-qa-pymupdf[dev]",
    "paper-qa-pypdf[dev]",
    "paper-qa[dev]",
]

[project]
authors = [
    {email = "hello@futurehouse.org", name = "FutureHouse technical staff"},
]
# Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
classifiers = [
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
]
dependencies = [
    "anyio",
    "fhaviary[llm]>=0.34",  # For type(action)=Message
    "fhlmi>=0.45.0",  # For type(action)=Message
    "html2text",  # TODO: evaluate moving to an opt-in dependency
    "httpx",
    "httpx-aiohttp",
    "numpy",
    "paper-qa-pypdf",  # TODO: after https://peps.python.org/pep-0771/, make this opt-out if 'pymupdf' extra is specified`
    "pybtex",
    "pydantic-settings",
    "pydantic~=2.0,>=2.10.1",  # Pin 2.10 for typing breaks
    "rich",
    "setuptools",  # TODO: remove after release of https://bitbucket.org/pybtex-devs/pybtex/pull-requests/46/replace-pkg_resources-with-importlib
    "tantivy",
    "tenacity",
    "tiktoken>=0.4.0",
]
description = "LLM Chain for answering questions from docs"
dynamic = ["version"]
keywords = ["question answering"]
license = {file = "LICENSE"}
maintainers = [
    {email = "jamesbraza@gmail.com", name = "James Braza"},
    {email = "michael.skarlinski@gmail.com", name = "Michael Skarlinski"},
    {email = "white.d.andrew@gmail.com", name = "Andrew White"},
]
name = "paper-qa"
readme = "README.md"
requires-python = ">=3.11"

[project.optional-dependencies]
dev = [
    "fhlmi>=0.44.0",  # Lower pin for update from Haiku 3.5 to 4.5
    "httpx-aiohttp>=0.1.11",  # Pin for raw headers fix
    "ipykernel>=6.29",  # For running Jupter notebooks, and pin to keep recent
    "ipython>=8",  # Pin to keep recent
    "litellm>=1.81.14",  # Lower pin for Anthropic empty system messages fix in https://github.com/BerriAI/litellm/pull/21630
    "mypy>=1.19",  # Pin for zip default detection
    "paper-qa[docling,image,ldp,memory,nemotron,pypdf-media,pymupdf,typing,zotero,local,qdrant,office]",
    "prek<0.2.15",  # Downpin for https://github.com/j178/prek/issues/1104
    "pydantic~=2.11",  # Pin for start of model_fields deprecation
    "pylint-per-file-ignores",
    "pylint-pydantic",
    "pytest-asyncio",
    "pytest-recording",
    "pytest-rerunfailures",
    "pytest-subtests",
    "pytest-sugar",
    "pytest-timeout",
    "pytest-timer[colorama]",
    "pytest-xdist",
    "pytest>=8",  # Pin to keep recent
    "python-dotenv",
    "pyzotero>=1.11.0",  # Lower pin for typing fix on Zotero.dump in https://github.com/urschrei/pyzotero/issues/298
    "refurb>=2",  # Pin to keep recent
    "typeguard",
    "vcrpy>=8",  # Pin for dropping unused requests support
]
docling = ["paper-qa-docling"]
image = ["fhlmi[image]"]
ldp = [
    "ldp>=0.45.0,<1",  # Lower pin for type(action)=Message, upper pin if v1 introduces breaks
]
local = [
    "sentence-transformers",
]
memory = [
    "paper-qa[ldp]",
    "usearch>=2.16.4",  # Pin for Python 3.13 support
]
nemotron = ["paper-qa-nemotron"]
office = [
    "unstructured[docx,xlsx,pptx]",
]
openreview = [
    "openreview-py",
]
pymupdf = ["paper-qa-pymupdf"]
pypdf = ["paper-qa-pypdf"]
pypdf-enhanced = ["paper-qa-pypdf[enhanced]"]
pypdf-media = ["paper-qa-pypdf[media]"]
qdrant = [
    "qdrant-client",
]
typing = [
    "tantivy>=0.22.2",  # Pin for typing fix of Doc.from_dict
    "types-PyYAML",
    "types-setuptools",
]
zotero = [
    "paper-qa-pymupdf",
    "pyzotero",
]

[project.scripts]
pqa = "paperqa.agents:main"

[project.urls]
issues = "https://github.com/Future-House/paper-qa/issues"
repository = "https://github.com/Future-House/paper-qa"

[tool.black]
preview = true

[tool.codespell]
check-filenames = true
check-hidden = true
ignore-words-list = "aadd,astroid,flate,ser,ECT"
skip = [
    "docs/2024-10-16_litqa2-splits.json5",
    "packages/paper-qa-nemotron/tests/cassettes/*",
    "src/paperqa/clients/client_data/*",
    "tests/cassettes/*",
    "tests/stub_data/*",
]

[tool.markdown_toc_creator]
horizontal-rule-style = "prettier"
proactive = false

[tool.mypy]
# Type-checks the interior of functions without type annotations.
check_untyped_defs = true
# Allows enabling one or multiple error codes globally. Note: This option will
# override disabled error codes from the disable_error_code option.
enable_error_code = [
    "ignore-without-code",
    "mutable-override",
    "redundant-cast",
    "redundant-expr",
    "redundant-self",
    "truthy-bool",
    "truthy-iterable",
    "unimported-reveal",
    "unreachable",
    "unused-awaitable",
    "unused-ignore",
]
# Shows a short summary line after error messages.
error_summary = false
# A regular expression that matches file names, directory names and paths which mypy
# should ignore while recursively discovering files to check. Use forward slashes (/) as
# directory separators on all platforms.
exclude = [
    "^\\.?venv",  # SEE: https://regex101.com/r/0rp5Br/1
]
# Specifies the paths to use, after trying the paths from MYPYPATH environment variable.
# Useful if you'd like to keep stubs in your repo, along with the config file.
# Multiple paths are always separated with a : or , regardless of the platform.
# User home directory and environment variables will be expanded.
mypy_path = "$MYPY_CONFIG_FILE_DIR/src,$MYPY_CONFIG_FILE_DIR/packages/paper-qa-pypdf/src,$MYPY_CONFIG_FILE_DIR/packages/paper-qa-pymupdf/src,$MYPY_CONFIG_FILE_DIR/packages/paper-qa-docling/src,$MYPY_CONFIG_FILE_DIR/packages/paper-qa-nemotron/src"
# Specifies the OS platform for the target program, for example darwin or win32
# (meaning OS X or Windows, respectively). The default is the current platform
# as revealed by Python’s sys.platform variable.
platform = "linux"
# Comma-separated list of mypy plugins.
plugins = ["pydantic.mypy"]
# Use visually nicer output in error messages: use soft word wrap, show source
# code snippets, and show error location markers.
pretty = true
# Shows column numbers in error messages.
show_column_numbers = true
# Shows error codes in error messages.
# SEE: https://mypy.readthedocs.io/en/stable/error_codes.html#error-codes
show_error_codes = true
# Prefixes each error with the relevant context.
show_error_context = true
# Warns about casting an expression to its inferred type.
warn_redundant_casts = true
# Shows a warning when encountering any code inferred to be unreachable or
# redundant after performing type analysis.
warn_unreachable = true
# Warns about per-module sections in the config file that do not match any
# files processed when invoking mypy.
warn_unused_configs = true
# Warns about unneeded `# type: ignore` comments.
warn_unused_ignores = true

[[tool.mypy.overrides]]
# Suppresses error messages about imports that cannot be resolved.
ignore_missing_imports = true
# Per-module configuration options
module = [
    "openreview",  # SEE: https://github.com/openreview/openreview-py/issues/2551
    "pybtex.*",  # SEE: https://bitbucket.org/pybtex-devs/pybtex/issues/141/type-annotations
    "pymupdf",  # SEE: https://github.com/pymupdf/PyMuPDF/issues/2883
    "pypdfium2",  # SEE: https://github.com/pypdfium2-team/pypdfium2/issues/367
    "pyzotero",  # SEE: https://github.com/urschrei/pyzotero/issues/110
    "vcr.*",  # SEE: https://github.com/kevin1024/vcrpy/issues/780
]

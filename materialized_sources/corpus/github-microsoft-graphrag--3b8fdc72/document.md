# Repository semantic capsule: microsoft/graphrag

- Commit: `f40e9a26ce62ba0b3fef8837d24aafdcc6e6c704`
- Default branch: `main`
- Description: microsoft/graphrag
- Selected evidence files: 5 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

# GraphRAG

> [!WARNING]
> GraphRAG is a research project that explores the functional use of graphs to form a targeted context for question answering. Since our first release in July 2024 the capabilities of frontier models have changed dramatically, and our portfolio of research projects has diversified to match. This project is largely in maintenance mode, and won't be accepting new PRs or implementing new features. We'll perform bug fixes and dependency updates as appropriate, particularly to address CVEs as they arise.

👉 [Microsoft Research Blog Post](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/)<br/>
👉 [Read the docs](https://microsoft.github.io/graphrag)<br/>
👉 [GraphRAG Arxiv](https://arxiv.org/pdf/2404.16130)

<div align="left">
  <a href="https://pypi.org/project/graphrag/">
    <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/graphrag">
  </a>
  <a href="https://pypi.org/project/graphrag/">
    <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/graphrag">
  </a>
  <a href="https://github.com/microsoft/graphrag/issues">
    <img alt="GitHub Issues" src="https://img.shields.io/github/issues/microsoft/graphrag">
  </a>
  <a href="https://github.com/microsoft/graphrag/discussions">
    <img alt="GitHub Discussions" src="https://img.shields.io/github/discussions/microsoft/graphrag">
  </a>
</div>

## Overview

The GraphRAG project is a data pipeline and transformation suite that is designed to extract meaningful, structured data from unstructured text using the power of LLMs.

To learn more about GraphRAG and how it can be used to enhance your LLM's ability to reason about your private data, please visit the <a href="https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/" target="_blank">Microsoft Research Blog Post.</a>

## Quickstart

To get started with the GraphRAG system we recommend trying the [command line quickstart](https://microsoft.github.io/graphrag/get_started/).

## Repository Guidance

This repository presents a methodology for using knowledge graph memory structures to enhance LLM outputs. Please note that the provided code serves as a demonstration and is not an officially supported Microsoft offering.

⚠️ _Warning: GraphRAG indexing can be an expensive operation, please read all of the documentation to understand the process and costs involved, and start small._

## Diving Deeper

- To learn about our contribution guidelines, see [CONTRIBUTING.md](./CONTRIBUTING.md)
- To start developing _GraphRAG_, see [DEVELOPING.md](./DEVELOPING.md)
- Join the conversation and provide feedback in the [GitHub Discussions tab!](https://github.com/microsoft/graphrag/discussions)

## Prompt Tuning

Using _GraphRAG_ with your data out of the box may not yield the best possible results.
We strongly recommend to fine-tune your prompts following the [Prompt Tuning Guide](https://microsoft.github.io/graphrag/prompt_tuning/overview/) in our documentation.

## Versioning

Please see the [breaking changes](./breaking-changes.md) document for notes on our approach to versioning the project.

_Always run `graphrag init --root [path] --force` between minor version bumps to ensure you have the latest config format. Run the provided migration notebook between major version bumps if you want to avoid re-indexing prior datasets. Note that this will overwrite your configuration and prompts, so back them up if necessary._

## Responsible AI FAQ

See [RAI_TRANSPARENCY.md](./RAI_TRANSPARENCY.md)

- [What is GraphRAG?](./RAI_TRANSPARENCY.md#what-is-graphrag)
- [What can GraphRAG do?](./RAI_TRANSPARENCY.md#what-can-graphrag-do)
- [What are GraphRAG’s intended use(s)?](./RAI_TRANSPARENCY.md#what-are-graphrags-intended-uses)
- [How was GraphRAG evaluated? What metrics are used to measure performance?](./RAI_TRANSPARENCY.md#how-was-graphrag-evaluated-what-metrics-are-used-to-measure-performance)
- [What are the limitations of GraphRAG? How can users minimize the impact of GraphRAG’s limitations when using the system?](./RAI_TRANSPARENCY.md#what-are-the-limitations-of-graphrag-how-can-users-minimize-the-impact-of-graphrags-limitations-when-using-the-system)
- [What operational factors and settings allow for effective and responsible use of GraphRAG?](./RAI_TRANSPARENCY.md#what-operational-factors-and-settings-allow-for-effective-and-responsible-use-of-graphrag)

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.

## Privacy

[Microsoft Privacy Statement](https://privacy.microsoft.com/en-us/privacystatement)

## `CONTRIBUTING.md`

# Contributing to GraphRAG

Thank you for your interest in contributing to GraphRAG! We welcome contributions from the community to help improve the project.

> [!WARNING]
> GraphRAG is a research project that explores the functional use of graphs to form a targeted context for question answering. Since our first release in July 2024 the capabilities of frontier models have changed dramatically, and our portfolio of research projects has diversified to match. This project is in maintenance mode. We won't be implementing new features, but we are accepting PRs for bug fixes. If you'd like to contribute a bug fix, please file an issue first so we can discuss and track it. We'll also perform dependency updates as appropriate, particularly to address CVEs as they arise.

## Code of Conduct

This project welcomes contributions and suggestions. Most contributions require you to agree to a Contributor License Agreement (CLA)
declaring that you have the right to, and actually do, grant us the rights to use your contribution.
For details, visit https://cla.microsoft.com.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Reporting Security Issues

**Please do not report security vulnerabilities through public GitHub issues.** Instead, please report them to the Microsoft Security Response Center (MSRC).
See [SECURITY.md](./SECURITY.md) for more information.

## How to Contribute, File an Issue

Before filing a new issue, search existing open and closed issues first: it is likely someone else has already found the problem you're seeing, and someone may be working on or have already contributed a fix!

If no existing item describes your issue, great - please file a new issue:

### File a new Issue

- Think you've found a bug? File an issue
- Have a question that you don't see answered in docs, videos, etc.? File an issue
- Don't understand how to do something? File an issue
- Found an existing issue that describes yours? Great - upvote and add additional commentary / info / repro-steps / etc.

Since the project is in maintenance mode, we're focused on bug fixes rather than new features. If you'd like to contribute a fix, please file an issue using the [issue tracker](https://github.com/microsoft/graphrag/issues) so we can discuss and track it.
Provide as much detail as possible to help us understand and address the problem.

### Add information

**Complete the new Issue form, providing as much information as possible**. The more information you provide, the more likely your issue will be understood and addressed. Helpful information includes:

- What device you're running (inc. CPU type, memory, disk, etc.)
- What OS your device is running
- What tools and apps you're using (e.g. VS 2022, VSCode, etc.)
- **We LOVE detailed repro steps!** What steps do we need to take to reproduce the issue? Assume we love to read repro steps. As much detail as you can stand is probably _barely_ enough detail for us!
- Prefer error message text where possible or screenshots of errors if text cannot be captured

### DO NOT post "+1" comments

> ⚠ DO NOT post "+1", "me too", or similar comments - they just add noise to an issue.

If you don't have any additional info/context to add but would like to indicate that you're affected by the issue, upvote the original issue by clicking its [+😊] button and hitting 👍 (+1) icon. This way we can actually measure how impactful an issue is.

---

## Thank you

We appreciate your contributions to GraphRAG!

## `SECURITY.md`

## Security

Microsoft takes the security of our software products and services seriously, which includes all source code repositories managed through our GitHub organizations, which include [Microsoft](https://github.com/Microsoft), [Azure](https://github.com/Azure), [DotNet](https://github.com/dotnet), [AspNet](https://github.com/aspnet), [Xamarin](https://github.com/xamarin), and [our GitHub organizations](https://opensource.microsoft.com/).

If you believe you have found a security vulnerability in any Microsoft-owned repository that meets [Microsoft's definition of a security vulnerability](https://docs.microsoft.com/en-us/previous-versions/tn-archive/cc751383(v=technet.10)), please report it to us as described below.

## Reporting Security Issues

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them to the Microsoft Security Response Center (MSRC) at [https://msrc.microsoft.com/create-report](https://msrc.microsoft.com/create-report).

If you prefer to submit without logging in, send email to [secure@microsoft.com](mailto:secure@microsoft.com).  If possible, encrypt your message with our PGP key; please download it from the [Microsoft Security Response Center PGP Key page](https://www.microsoft.com/en-us/msrc/pgp-key-msrc).

You should receive a response within 24 hours. If for some reason you do not, please follow up via email to ensure we received your original message. Additional information can be found at [microsoft.com/msrc](https://www.microsoft.com/msrc). 

Please include the requested information listed below (as much as you can provide) to help us better understand the nature and scope of the possible issue:

  * Type of issue (e.g. buffer overflow, SQL injection, cross-site scripting, etc.)
  * Full paths of source file(s) related to the manifestation of the issue
  * The location of the affected source code (tag/branch/commit or direct URL)
  * Any special configuration required to reproduce the issue
  * Step-by-step instructions to reproduce the issue
  * Proof-of-concept or exploit code (if possible)
  * Impact of the issue, including how an attacker might exploit the issue

This information will help us triage your report more quickly.

If you are reporting for a bug bounty, more complete reports can contribute to a higher bounty award. Please visit our [Microsoft Bug Bounty Program](https://microsoft.com/msrc/bounty) page for more details about our active programs.

## Preferred Languages

We prefer all communications to be in English.

## Policy

Microsoft follows the principle of [Coordinated Vulnerability Disclosure](https://www.microsoft.com/en-us/msrc/cvd).

## `pyproject.toml`

[project]
name = "graphrag-monorepo"
classifiers = ["Private :: Do Not Upload"]
version = "0.0.0"
description = "GraphRAG: A graph-based retrieval-augmented generation (RAG) system."
authors = [
    {name = "Alonso Guevara Fernández", email = "alonsog@microsoft.com"},
    {name = "Andrés Morales Esquivel", email = "andresmor@microsoft.com"},
    {name = "Chris Trevino", email = "chtrevin@microsoft.com"},
    {name = "David Tittsworth", email = "datittsw@microsoft.com"},
    {name = "Dayenne de Souza", email = "ddesouza@microsoft.com"},
    {name = "Derek Worthen", email = "deworthe@microsoft.com"},
    {name = "Gaudy Blanco Meneses", email = "gaudyb@microsoft.com"},
    {name = "Ha Trinh", email = "trinhha@microsoft.com"},
    {name = "Jonathan Larson", email = "jolarso@microsoft.com"},
    {name = "Josh Bradley", email = "joshbradley@microsoft.com"},
    {name = "Kate Lytvynets", email = "kalytv@microsoft.com"},
    {name = "Kenny Zhang", email = "zhangken@microsoft.com"},
    {name = "Mónica Carvajal"},
    {name = "Nathan Evans", email = "naevans@microsoft.com"},
    {name = "Rodrigo Racanicci", email = "rracanicci@microsoft.com"},
    {name = "Sarah Smith", email = "smithsarah@microsoft.com"},
]
requires-python = ">=3.11,<3.14"

[dependency-groups]
dev = [
    "coverage~=7.15",
    "deptry~=0.25",
    "ipykernel~=7.3",
    "jupyter~=1.1",
    "mkdocs-material~=9.7",
    "mkdocs-jupyter~=0.26",
    "mkdocs-exclude-search~=0.6",
    "mkdocs-typer~=0.0.3",
    "nbconvert~=7.17",
    "pandas-stubs~=3.0",
    "poethepoet~=0.48",
    "pyright~=1.1",
    "pytest~=9.1",
    "pytest-asyncio~=1.4",
    "pytest-dotenv~=0.5",
    "pytest-timeout~=2.5",
    "ruff~=0.16",
    "semversioner~=3.0",
    "update-toml~=0.2",
    "pytest-xdist[psutil]~=3.8.0",
]

[tool.uv]
package = false

[[tool.uv.index]]
url="https://packagefeedproxy.microsoft.io/pypi/simple"
default=true

[tool.uv.workspace]
members = ["packages/*"]

[tool.uv.sources]
graphrag-chunking = { workspace = true }
graphrag-common = { workspace = true }
graphrag-input = { workspace = true }
graphrag-storage = { workspace = true }
graphrag-cache = { workspace = true }
graphrag-vectors = { workspace = true }
graphrag-llm = { workspace = true }

# Keep poethepoet for task management to minimize changes
[tool.poe.tasks]
_sort_imports = "ruff check --select I --fix ."
_format_code = "ruff format  ."
_ruff_check = 'ruff check .'
_pyright = "pyright"
_convert_local_search_nb = 'jupyter nbconvert --output-dir=docsite/posts/query/notebooks/ --output="{notebook_name}_nb" --template=docsite/nbdocsite_template --to markdown examples_notebooks/local_search.ipynb'
_convert_global_search_nb = 'jupyter nbconvert --output-dir=docsite/posts/query/notebooks/ --output="{notebook_name}_nb" --template=docsite/nbdocsite_template --to markdown examples_notebooks/global_search.ipynb'
_copy_build_assets = "python -m scripts.copy_build_assets"
_semversioner_release = "semversioner release"
_semversioner_changelog = "semversioner changelog > CHANGELOG.md"
# Add more update toml tasks as packages are added
_semversioner_update_graphrag_toml_version = "update-toml update --file packages/graphrag/pyproject.toml --path project.version --value $(uv run semversioner current-version)"
_semversioner_update_graphrag_chunking_toml_version = "update-toml update --file packages/graphrag-chunking/pyproject.toml --path project.version --value $(uv run semversioner current-version)"
_semversioner_update_graphrag_common_toml_version = "update-toml update --file packages/graphrag-common/pyproject.toml --path project.version --value $(uv run semversioner current-version)"
_semversioner_update_graphrag_storage_toml_version = "update-toml update --file packages/graphrag-storage/pyproject.toml --path project.version --value $(uv run semversioner current-version)"
_semversioner_update_graphrag_cache_toml_version = "update-toml update --file packages/graphrag-cache/pyproject.toml --path project.version --value $(uv run semversioner current-version)"
_semversioner_update_graphrag_input_toml_version = "update-toml update --file packages/graphrag-input/pyproject.toml --path project.version --value $(uv run semversioner current-version)"
_semversioner_update_graphrag_vectors_toml_version = "update-toml update --file packages/graphrag-vectors/pyproject.toml --path project.version --value $(uv run semversioner current-version)"
_semversioner_update_graphrag_llm_toml_version = "update-toml update --file packages/graphrag-llm/pyproject.toml --path project.version --value $(uv run semversioner current-version)"
_semversioner_update_workspace_dependency_versions = "python -m scripts.update_workspace_dependency_versions"
semversioner_add = "semversioner add-change"
coverage_report = 'coverage report --omit "**/tests/**" --show-missing'
check_format = 'ruff format . --check'
fix = "ruff check --fix ."
fix_unsafe = "ruff check --fix --unsafe-fixes ."
_test_all = "coverage run -m pytest ./tests"
test_unit = "pytest ./tests/unit"
test_integration = "pytest ./tests/integration"
test_smoke = "pytest ./tests/smoke"
test_notebook = "pytest -n auto ./tests/notebook"
test_verbs = "pytest ./tests/verbs"
index = "python -m graphrag index"
update = "python -m graphrag update"
init = "python -m graphrag init"
query = "python -m graphrag query"
prompt_tune = "python -m graphrag prompt-tune"
# Pass in a test pattern
test_only = "pytest -s -k"
serve_docs = "mkdocs serve"
build_docs = "mkdocs build"
_build_packages = "uv build --all-packages"
_sync = "uv sync --all-packages"

[[tool.poe.tasks.build]]
sequence = ['_copy_build_assets', '_build_packages']

[[tool.poe.tasks.release]]
sequence = [
    '_semversioner_release',
    '_semversioner_changelog',
    # Add more update toml tasks as packages are added
    '_semversioner_update_graphrag_toml_version',
    '_semversioner_update_graphrag_common_toml_version',
    '_semversioner_update_graphrag_chunking_toml_version',
    '_semversioner_update_graphrag_input_toml_version',
    '_semversioner_update_graphrag_storage_toml_version',
    '_semversioner_update_graphrag_cache_toml_version',
    "_semversioner_update_graphrag_vectors_toml_version",
    '_semversioner_update_graphrag_llm_toml_version',
    '_semversioner_update_workspace_dependency_versions',
    '_sync',
]
ignore_fail = 'return_non_zero'

[[tool.poe.tasks.convert_docsite_notebooks]]
sequence = ['_convert_local_search_nb', '_convert_global_search_nb']
ignore_fail = 'return_non_zero'

[[tool.poe.tasks.format]]
sequence = ['_sort_imports', '_format_code']
ignore_fail = 'return_non_zero'

[[tool.poe.tasks.check]]
sequence = ['check_format', '_ruff_check', '_pyright']
ignore_fail = 'return_non_zero'

[[tool.poe.tasks.test]]
sequence = ['_test_all', 'coverage_report']
ignore_fail = 'return_non_zero'

# Keep all existing tool configurations
[tool.ruff]
target-version = "py310"
extend-include = ["*.ipynb"]

[tool.ruff.format]
preview = true
docstring-code-format = true
docstring-code-line-length = 20

[tool.ruff.lint]
preview = true
select = [
    "E4",
    "E7",
    "E9",
    "W291",
    "YTT",
    "T10",
    "ICN",
    "INP",
    "Q",
    "RSE",
    "SLOT",
    "INT",
    "FLY",
    "LOG",
    "C90",
    "T20",
    "D",
    "RET",
    "PD",
    "N",
    "PIE",
    "SIM",
    "S",
    "G",
    "ERA",
    "ASYNC",
    "TID",
    "UP",
    "SLF",
    "BLE",
    "C4",
    "I",
    "F",
    "A",
    "ARG",
    "PTH",
    "RUF",
    "B",
    "TCH",
    "DTZ",
    "PYI",
    "PT",
    "EM",
    "TRY",
    "PERF",
    "CPY",
    # "FBT", # use named arguments for boolean flags
    # "TD", # todos
    # "FIX", # fixme
    # "FURB" # preview rules
    # ANN # Type annotations, re-enable when we get bandwidth
]
ignore = [
    # Ignore module names shadowing Python builtins
    "A005",
    # Conflicts with interface argument checking
    "ARG002",
    "ANN204",

## `docs/index.md`

# Welcome to GraphRAG

👉 [Microsoft Research Blog Post](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/) <br/>
👉 [GraphRAG Arxiv](https://arxiv.org/pdf/2404.16130)

<p align="center">
<img src="img/GraphRag-Figure1.jpg" alt="Figure 1: LLM-generated knowledge graph built from a private dataset using GPT-4 Turbo." width="450" align="center" />
</p>
<p align="center">
Figure 1: An LLM-generated knowledge graph built using GPT-4 Turbo.
</p>

GraphRAG is a structured, hierarchical approach to Retrieval Augmented Generation (RAG), as opposed to naive semantic-search
approaches using plain text snippets. The GraphRAG process involves extracting a knowledge graph out of raw text, building a community hierarchy, generating summaries for these communities, and then leveraging these structures when perform RAG-based tasks.

To learn more about GraphRAG and how it can be used to enhance your language model's ability to reason about your private data, please visit the [Microsoft Research Blog Post](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/).

## Get Started with GraphRAG 🚀

To start using GraphRAG, check out the [_Get Started_](get_started.md) guide.
For a deeper dive into the main sub-systems, please visit the docpages for the [Indexer](index/overview.md) and [Query](query/overview.md) packages.

## GraphRAG vs Baseline RAG 🔍

Retrieval-Augmented Generation (RAG) is a technique to improve LLM outputs using real-world information. This technique is an important part of most LLM-based tools and the majority of RAG approaches use vector similarity as the search technique, which we call _Baseline RAG_. GraphRAG uses knowledge graphs to provide substantial improvements in question-and-answer performance when reasoning about complex information. RAG techniques have shown promise in helping LLMs to reason about _private datasets_ - data that the LLM is not trained on and has never seen before, such as an enterprise’s proprietary research, business documents, or communications. _Baseline RAG_ was created to help solve this problem, but we observe situations where baseline RAG performs very poorly. For example:

- Baseline RAG struggles to connect the dots. This happens when answering a question requires traversing disparate pieces of information through their shared attributes in order to provide new synthesized insights.
- Baseline RAG performs poorly when being asked to holistically understand summarized semantic concepts over large data collections or even singular large documents.

To address this, the tech community is working to develop methods that extend and enhance RAG. Microsoft Research’s new approach, GraphRAG, creates a knowledge graph based on an input corpus. This graph, along with community summaries and graph machine learning outputs, are used to augment prompts at query time. GraphRAG shows substantial improvement in answering the two classes of questions described above, demonstrating intelligence or mastery that outperforms other approaches previously applied to private datasets.

## The GraphRAG Process 🤖

GraphRAG builds upon our prior [research](https://www.microsoft.com/en-us/worklab/patterns-hidden-inside-the-org-chart) and [tooling](https://github.com/graspologic-org/graspologic) using graph machine learning. The basic steps of the GraphRAG process are as follows:

### Index

- Slice up an input corpus into a series of TextUnits, which act as analyzable units for the rest of the process, and provide fine-grained references in our outputs.
- Extract all entities, relationships, and key claims from the TextUnits.
- Perform a hierarchical clustering of the graph using the [Leiden technique](https://arxiv.org/pdf/1810.08473.pdf). To see this visually, check out Figure 1 above. Each circle is an entity (e.g., a person, place, or organization), with the size representing the degree of the entity, and the color representing its community.
- Generate summaries of each community and its constituents from the bottom-up. This aids in holistic understanding of the dataset.

### Query

At query time, these structures are used to provide materials for the LLM context window when answering a question. The primary query modes are:

- [_Global Search_](query/global_search.md) for reasoning about holistic questions about the corpus by leveraging the community summaries.
- [_Local Search_](query/local_search.md) for reasoning about specific entities by fanning-out to their neighbors and associated concepts.
- [_DRIFT Search_](query/drift_search.md) for reasoning about specific entities by fanning-out to their neighbors and associated concepts, but with the added context of community information.
- _Basic Search_ for those times when your query is best answered by baseline RAG (standard top _k_ vector search).

### Prompt Tuning

Using _GraphRAG_ with your data out of the box may not yield the best possible results.
We strongly recommend to fine-tune your prompts following the [Prompt Tuning Guide](prompt_tuning/overview.md) in our documentation.


## Versioning

Please see the [breaking changes](https://github.com/microsoft/graphrag/blob/main/breaking-changes.md) document for notes on our approach to versioning the project.

*Always run `graphrag init --root [path] --force` between minor version bumps to ensure you have the latest config format. Run the provided migration notebook between major version bumps if you want to avoid re-indexing prior datasets. Note that this will overwrite your configuration and prompts, so back them up if necessary.*

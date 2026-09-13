# Repository semantic capsule: gepa-ai/gepa

- Commit: `15ee314f9c7d34ec153b809d401f42f55c4dcd76`
- Default branch: `main`
- Description: gepa-ai/gepa
- Selected evidence files: 6 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

<p align="center">
  <img src="https://raw.githubusercontent.com/gepa-ai/gepa/refs/heads/main/docs/docs/assets/gepa_logo_with_text.svg" alt="GEPA Logo" width="450">
</p>

<p align="center">
  <strong>Optimize any text parameter — prompts, code, agent architectures, configurations — using LLM-based reflection and Pareto-efficient evolutionary search.</strong>
</p>

<p align="center">
  <a href="https://gepa-ai.github.io/gepa/"><strong>Website</strong></a> &ensp;|&ensp;
  <a href="https://gepa-ai.github.io/gepa/guides/quickstart/"><strong>Quick Start</strong></a> &ensp;|&ensp;
  <a href="https://arxiv.org/abs/2507.19457"><strong>Paper</strong></a> &ensp;|&ensp;
  <a href="https://gepa-ai.github.io/gepa/blog/"><strong>Blog</strong></a> &ensp;|&ensp;
  <a href="https://discord.gg/WXFSeVGdbW"><strong>Discord</strong></a>
</p>

<p align="center">
  <a href="https://pypi.org/project/gepa/"><img src="https://img.shields.io/pypi/v/gepa?logo=python&logoColor=white&color=3776ab" alt="PyPI"></a>
  <a href="https://pepy.tech/projects/gepa"><img src="https://static.pepy.tech/badge/gepa" alt="Downloads"></a>
  <a href="https://github.com/gepa-ai/gepa"><img src="https://img.shields.io/github/stars/gepa-ai/gepa?style=flat&logo=github&color=181717" alt="GitHub stars"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green?style=flat" alt="License"></a>
</p>

<p align="center">
  <a href="https://join.slack.com/t/gepa-ai/shared_invite/zt-3o352xhyf-QZDfwmMpiQjsvoSYo7M1_w"><img src="https://badgen.net/badge/icon/Slack?icon=slack&label&color=4A154B" alt="Slack"></a>
  <a href="https://discord.gg/WXFSeVGdbW"><img src="https://dcbadge.limes.pink/api/server/https://discord.gg/WXFSeVGdbW?style=flat" alt="Discord"></a>
</p>

---

## What is GEPA?

**GEPA** (Genetic-Pareto) is a framework for optimizing any system with textual parameters against any evaluation metric. Unlike RL or gradient-based methods that collapse execution traces into a single scalar reward, GEPA uses LLMs to *read* full execution traces — error messages, profiling data, reasoning logs — to diagnose *why* a candidate failed and propose targeted fixes. Through iterative reflection, mutation, and Pareto-aware selection, GEPA evolves high-performing variants with minimal evaluations.

**If you can measure it, you can optimize it**: prompts, code, agent architectures, scheduling policies, vector graphics, and more.

### Key Results

| | |
|---|---|
| **90x cheaper** | Open-source models + GEPA beat Claude Opus 4.1 at [Databricks](https://www.databricks.com/blog/building-state-art-enterprise-agents-90x-cheaper-automated-prompt-optimization) |
| **35x faster than RL** | 100–500 evaluations vs. 5,000–25,000+ for GRPO ([paper](https://arxiv.org/abs/2507.19457)) |
| **32% → 89%** | ARC-AGI agent accuracy via [architecture discovery](https://gepa-ai.github.io/gepa/blog/introducing-optimize-anything/#5-agent-architecture-discovery) |
| **40.2% cost savings** | Cloud scheduling policy [discovered by GEPA](https://gepa-ai.github.io/gepa/blog/introducing-optimize-anything/#3-systems-research), beating expert heuristics |
| **55% → 82%** | Coding agent resolve rate on Jinja via [auto-learned skills](https://gepa-ai.github.io/gepa/blog/automatically-learning-skills-for-coding-agents/) |
| **50+ production uses** | Across Shopify, Databricks, Dropbox, OpenAI, Pydantic, MLflow, Comet ML, and [more](https://gepa-ai.github.io/gepa/guides/use-cases/) |

> *"Both DSPy and (especially) **GEPA are currently severely under hyped** in the AI context engineering world"* — **Tobi Lutke**, CEO, Shopify

---

## Installation

```bash
pip install gepa
```

To install the latest from `main`:

```bash
pip install git+https://github.com/gepa-ai/gepa.git
```

---

## Quick Start

### Simple Prompt Optimization

Optimize a system prompt for math problems from the AIME benchmark in a few lines of code ([full tutorial](https://dspy.ai/tutorials/gepa_aime/)):

```python
import gepa

trainset, valset, _ = gepa.examples.aime.init_dataset()

seed_prompt = {
    "system_prompt": "You are a helpful assistant. Answer the question. "
                     "Put your final answer in the format '### <answer>'"
}

result = gepa.optimize(
    seed_candidate=seed_prompt,
    trainset=trainset,
    valset=valset,
    task_lm="openai/gpt-4.1-mini",
    max_metric_calls=150,
    reflection_lm="openai/gpt-5",
)

print("Optimized prompt:", result.best_candidate['system_prompt'])
```

**Result:** GPT-4.1 Mini goes from 46.6% → 56.6% on AIME 2025 (+10 percentage points).

### With DSPy (Recommended for AI Pipelines)

The most powerful way to use GEPA for prompt optimization is within [DSPy](https://dspy.ai/), where it's available as `dspy.GEPA`. See [dspy.GEPA tutorials](https://dspy.ai/tutorials/gepa_ai_program/) for executable notebooks.

```python
import dspy

optimizer = dspy.GEPA(
    metric=your_metric,
    max_metric_calls=150,
    reflection_lm="openai/gpt-5",
)
optimized_program = optimizer.compile(student=MyProgram(), trainset=trainset, valset=valset)
```

### optimize_anything: Beyond Prompts

The [`optimize_anything`](https://gepa-ai.github.io/gepa/blog/introducing-optimize-anything/) API optimizes *any* text artifact — code, agent architectures, configurations, SVGs — not just prompts. You provide an evaluator; the system handles the search.

```python
import gepa.optimize_anything as oa
from gepa.optimize_anything import optimize_anything, GEPAConfig, EngineConfig

def evaluate(candidate: str) -> float:
    result = run_my_system(candidate)
    oa.log(f"Output: {result.output}")      # Actionable Side Information
    oa.log(f"Error: {result.error}")         # feeds back into reflection
    return result.score

result = optimize_anything(
    seed_candidate="<your initial artifact>",
    evaluator=evaluate,
    objective="Describe what you want to optimize for.",
    config=GEPAConfig(engine=EngineConfig(max_metric_calls=100)),
)
```

### Use GEPA as an Agent Skill

GEPA also ships as an **[Agent Skill](https://agentskills.io/)** so coding agents can drive `optimize_anything` for you. In a clone of this repo, Claude Code — and other agents that read `.claude/skills/` (Cursor, VS Code/Copilot, Codex, Gemini CLI) — auto-discover it at [`.claude/skills/gepa-optimize-anything/`](.claude/skills/gepa-optimize-anything/). To use it in any other project, install the plugin from this repo's marketplace:

```bash
/plugin marketplace add gepa-ai/gepa
/plugin install gepa-optimize-anything@gepa
```

See the [Agent Skill guide](https://gepa-ai.github.io/gepa/guides/agent-skill/) for details.

---

## How It Works

Traditional optimizers know *that* a candidate failed but not *why*. GEPA takes a different approach:

1. **Select** a candidate from the Pareto frontier (candidates excelling on different task subsets)
2. **Execute** on a minibatch, capturing full execution traces
3. **Reflect** — an LLM reads the traces (error messages, profiler output, reasoning logs) and diagnoses failures
4. **Mutate** — generate an improved candidate informed by accumulated lessons from all ancestors
5. **Accept** — add to the pool if improved, update the Pareto front

GEPA also supports **system-aware merge** — combining strengths of two Pareto-optimal candidates excelling on different tasks. The key concept is **Actionable Side Information (ASI)**: diagnostic feedback returned by evaluators that serves as the text-optimization analogue of a gradient.

For details, see the [paper](https://arxiv.org/abs/2507.19457) and the [documentation](https://gepa-ai.github.io/gepa/guides/).

---

## Adapters: Plug GEPA into Any System

GEPA connects to your system via the [`GEPAAdapter`](src/gepa/core/adapter.py) interface — implement `evaluate` and `make_reflective_dataset`, and GEPA handles the rest.

**Built-in adapters:**

| Adapter | Description |
|---|---|
| [DefaultAdapter](src/gepa/adapters/default_adapter/) | System prompt optimization for single-turn LLM tasks |
| [ConfidenceAdapter](src/gepa/adapters/confidence_adapter/) | Logprob-aware classification optimization — penalizes lucky guesses and feeds confidence diagnostics into reflection. `pip install "gepa[confidence]"` |
| [DSPy Full Program](src/gepa/adapters/dspy_full_program_adapter/) | Evolves entire DSPy programs (signatures, modules, control flow). **67% → 93%** on MATH. |
| [Generic RAG](src/gepa/adapters/generic_rag_adapter/) | Vector store-agnostic RAG optimization (ChromaDB, Weaviate, Qdrant, Pinecone) |
| [MCP Adapter](src/gepa/adapters/mcp_adapter/) | Optimize [MCP](https://modelcontextprotocol.io/) tool descriptions and system prompts |
| [TerminalBench](src/gepa/adapters/terminal_bench_adapter/) | Optimize the [Terminus](https://www.tbench.ai/terminus) terminal-use agent |
| [AnyMaths](src/gepa/adapters/anymaths_adapter/) | Mathematical problem-solving and reasoning tasks |
| [LangChain](src/gepa/adapters/langchain_adapter/) | Optimize prompts for any LangChain pipeline — chat models, tool-using agents, LangGraph. `pip install "gepa[langchain]"` |

See the [adapters guide](https://gepa-ai.github.io/gepa/guides/adapters/) for how to build your own, and [DSPy's adapter](https://github.com/stanfordnlp/dspy/tree/main/dspy/teleprompt/gepa/gepa_utils.py) as a reference.

---

## Integrations

GEPA is integrated into several major frameworks:

- **[DSPy](https://dspy.ai/)** — `dspy.GEPA` for optimizing DSPy programs. [Tutorials](https://dspy.ai/tutorials/gepa_ai_program/).
- **[MLflow](https://mlflow.org/docs/latest/genai/prompt-registry/optimize-prompts/)** — `mlflow.genai.optimize_prompts()` for automatic prompt improvement.
- **[Comet ML Opik](https://www.comet.com/docs/opik/agent_optimization/algorithms/gepa_optimizer)** — Core optimization algorithm in Opik Agent Optimizer.
- **[Pydantic](https://pydantic.dev/articles/prompt-optimization-with-gepa)** — Prompt optimization for Pydantic AI.
- **[OpenAI Cookbook](https://cookbook.openai.com/examples/partners/self_evolving_agents/autonomous_agent_retraining)** — Self-evolving agents with GEPA.
- **[HuggingFace Cookbook](https://huggingface.co/learn/cookbook/en/dspy_gepa)** — Prompt optimization guide.
- **[Google ADK / Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/optimize-agent)** — `adk optimize` powered by GEPA, also shipped inside Google Cloud's Gemini Enterprise Agent Platform Quality Flywheel. [ADK docs](https://adk.dev/optimize/) · [Community tutorial](https://raphaelmansuy.github.io/adk_training/blog/gepa-optimization-tutorial/).
- **[Microsoft AI: MAI-Thinking-1](https://microsoft.ai/wp-content/uploads/2026/06/main_20260602_2.pdf)** — Uses GEPA / DSPy to optimize the Qwen3-30B LLM-judge prompt that filters Code pages in the model's pre-training pipeline (~233B tokens of curated data).

---

## Example Optimized Prompts

GEPA can be thought of as precomputing reasoning during optimization to produce a plan for future task instances. Here are examples of the detailed prompts GEPA discovers:

<table>
  <tr>
  <td colspan="2" align="center">Example GEPA Prompts</td>
  </tr>
  <tr>
    <td align="center">HotpotQA (multi-hop QA) Prompt</td>
    <td align="center">AIME Prompt</td>
  </tr>
  <tr>
    <td width="52%" valign="top">
      <img src="https://raw.githubusercontent.com/gepa-ai/gepa/refs/heads/main/assets/gepa_prompt_hotpotqa.png" alt="HotpotQA Prompt" width="1400">
      <!-- <td> -->
      <details>
<summary><mark>Click to view full HotpotQA prompt</mark></summary>
<mark>[HotpotQA Prompt Begin]</mark>

You will be given two input fields: `question` and `summary_1`.

Your task is to generate a new search query (`query`) optimized for the **second hop** of a multi-hop retrieval system. The original user question is typically complex and requires information from multiple documents to answer. The first hop query is the original question used to retrieve an initial set of documents. Your goal is to generate a **second hop query** that retrieves *additional relevant documents* that were *not* found in the first hop but are necessary to answer the original question completely.

## `AGENTS.md`

# GEPA

GEPA (Genetic-Pareto) is a Python framework for optimizing text components (AI prompts, code, instructions) using LLM-based reflection and Pareto-efficient evolutionary search.

## Agent Skill

This repository ships an **Agent Skill** at `.claude/skills/gepa-optimize-anything/`. If you are a coding agent and the user wants to **auto-optimize, tune, or search over any scorable text artifact** (a prompt, program/code, config, regex/SQL, or agent scaffold) with `gepa.optimize_anything`, read `.claude/skills/gepa-optimize-anything/SKILL.md` first and follow it. It is auto-discovered by Claude Code and by other agents that read `.claude/skills/` (Cursor, VS Code/Copilot, Codex, Gemini CLI). To install it standalone in another project: `/plugin marketplace add gepa-ai/gepa` then `/plugin install gepa-optimize-anything@gepa`.

## Setup

We use **uv** for dependency management. The project uses setuptools as the build backend. All python executions must be done through uv.

```bash
uv sync --extra dev
```

## Project Structure

- `src/gepa/` — main package source
  - `core/` — optimization loop, state, evaluation
  - `proposer/` — candidate proposal and mutation logic
  - `adapters/` — integration adapters (DSPy, RAG, MCP, etc.)
  - `strategies/` — batch sampling and candidate selection
  - `logging/` — experiment tracking and logging
- `tests/` — pytest test suite
- `docs/` — mkdocs documentation site

## Build & Test

```bash
uv run pytest
uv run ruff check src/
uv run ruff format src/
uv run pyright src/
```

## Code Style

- Linter/formatter: ruff (line length 120, double quotes, space indent)
- Type checking: pyright
- Python target: 3.10+
- No relative imports (enforced by ruff)

## `CLAUDE.md`

@AGENTS.md

## `CONTRIBUTING.md`

## Environment Setup

Python 3.10 or later is required.

Setting up your GEPA development environment requires you to fork the GEPA repository and clone it locally.
If you are not familiar with the GitHub fork process, please refer to [Fork a repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo). After creating the fork, clone
it to your local development device:

```shell
git clone https://github.com/gepa-ai/gepa
cd gepa
```

Next, we must set up a Python environment with the correct dependencies. There are two recommended ways to set up the
dev environment.

### [Recommended] Set Up Environment Using uv

[uv](https://github.com/astral-sh/uv) is a rust-based Python package and project manager that provides a fast
way to set up the development environment. First, install uv by following the
[installation guide](https://docs.astral.sh/uv/getting-started/installation/).

After uv is installed, in your working directory (`gepa/`), run:

```shell
uv sync --extra dev --python 3.11
```

Then you are all set!

To verify that your environment is set up successfully, run some unit tests:

```shell
uv run pytest tests/
```

Note: You need to use the `uv run` prefix for every Python command, as uv creates a Python virtual
environment and `uv run` points the command to that environment. For example, to execute a Python script you will need
`uv run python script.py`.

### Set Up Environment Using conda + pip

You can also set up the virtual environment via conda + pip, which takes a few extra steps but offers more flexibility. Before starting,
make sure you have conda installed. If not, please follow the instructions
[here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

To set up the environment, run:

```shell
conda create -n gepa-dev python=3.11
conda activate gepa-dev
pip install -e ".[dev]"
```

Then verify the installation by running some unit tests:

```shell
pytest tests/
```

## Code Linting with Ruff
We follow the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) and use `ruff` for both linting and formatting. To ensure consistent code quality, we use pre-commit hooks that automatically check and fix common issues.


First you need to set up the pre-commit hooks (do this once after cloning the repository):

```shell
uv run pre-commit install
```

Then stage and commit your changes. When you run `git commit`, the pre-commit hook will be
automatically run.

```shell
git add .
git commit -m "your commit message"
```

If the hooks make any changes, you'll need to stage and commit those changes as well.

You can also run the hooks manually:

- Check staged files only:

  ```shell
  uv run pre-commit run
  ```

- Check specific files:

  ```shell
  uv run pre-commit run --files path/to/file1.py path/to/file2.py
  ```

Please ensure all pre-commit checks pass before creating your pull request. If you're unsure about any
formatting issues, feel free to commit your changes and let the pre-commit hooks fix them automatically.

## Type Checking with Pyright
Run Pyright before opening a pull request to catch type regressions early:

```shell
uv run pyright
```

You can target specific modules while iterating:

```shell
uv run pyright src/gepa/strategies/
```

## `pyproject.toml`

[build-system]
requires = ["setuptools>=77.0.1", "wheel", "build"]
build-backend = "setuptools.build_meta"

[project]
# Do not add spaces around the '=' sign for any of the fields
# preceded by a marker comment as it affects the publish workflow.
#replace_package_name_marker
name="gepa"
#replace_package_version_marker
version="0.1.4"
description = "A framework for optimizing textual system components (AI prompts, code snippets, etc.) using LLM-based reflection and Pareto-efficient evolutionary search."
readme = "README.md"
authors = [
  { name = "Lakshya A Agrawal", email = "lakshyaaagrawal@berkeley.edu" }
]
license = { text = "MIT" }
requires-python = ">=3.10, <3.15"

dependencies = []

[project.optional-dependencies]
full = [
    # Common dependencies (all Python versions)
    # litellm 1.92.0 introduced a native extension and publishes manylinux
    # wheels only (cp310-cp313): no macOS, no Windows, no cp314. Everyone else
    # falls back to the sdist, which needs Cargo >= 1.85 (edition2024) and a
    # PyO3 that caps at Python 3.13 — so fresh installs break on macOS/Windows
    # (all Pythons) and on 3.14 (all platforms). Cap unconditionally; lift once
    # litellm ships a complete wheel matrix (or a pure-Python build) — check
    # https://pypi.org/pypi/litellm/<version>/json artifact list first.
    "litellm>=1.83.0,<1.92",
    "tqdm>=4.66.1",
    "cloudpickle>=3.0.0",
    # Python < 3.14
    "datasets>=2.14.6; python_version < '3.14'",
    "mlflow>=3.11.1; python_version < '3.14'",
    "wandb; python_version < '3.14'",
    # Python 3.14+ (higher floors / alternative packages needed for compatibility)
    "datasets>=4.5.0; python_version >= '3.14'",
    "pandas>=2.3.3; python_version >= '3.14'",
    "mlflow-skinny>=3.11.1; python_version >= '3.14'",
    "wandb>=0.23.0; python_version >= '3.14'",
    "pyarrow>=22.0.0; python_version >= '3.14'",
    "pydantic>=2.12.0; python_version >= '3.14'",
    "tiktoken>=0.12.0; python_version >= '3.14'",
]
confidence = [
    "llm-structured-confidence>=0.4.5",
    # See the litellm cap comment in the `full` extra (incomplete 1.92 wheels).
    "litellm>=1.64.0,<1.92; python_version < '3.14'",
    "litellm>=1.81.0,<1.92; python_version >= '3.14'",
]
dspy = []
test = [
    "gepa[full]",
    "pytest",
    "pyright"
]
build = [
    "setuptools>=77.0.1",
    "wheel",
    "build",
    "twine",
    "semver",
    "packaging",
    "requests>=2.33.0"
]
dev = [
    "gepa[test]",
    "gepa[build]",
    "pre-commit",
    "build>=1.0.3",
    "ruff>=0.3.0"
]
gskill = [
    "gepa[full]",
    "swesmith",
    "docker",
    "python-dotenv",
    "pyyaml",
]

langchain = [
    "langchain>=1.0",
    "langchain-core>=1.0",
    "tqdm>=4.66",
]

[project.urls]
"Homepage" = "https://github.com/gepa-ai/gepa"
"Bug Tracker" = "https://github.com/gepa-ai/gepa/issues"

[tool.setuptools.packages.find]
where = ["src"]

[tool.setuptools.package-data]
gepa = ["py.typed"]

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.ruff]
include = ["src/**/*.py"]
line-length = 120
indent-width = 4
target-version = "py310"

[tool.ruff.lint]
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort
    "C",   # flake8-comprehensions
    "B",   # flake8-bugbear
    "UP",  # pyupgrade
    "N",   # pep8-naming
    "RUF", # ruff-specific rules
    "Q",   # flake8-quotes
]
ignore = [
    "B027",  # Allow non-abstract empty methods in abstract base classes
    "FBT003",# Allow boolean positional values in function calls
    "C901",  # Ignore complexity checking
    "E501",  # Ignore line length errors (handled by formatter)
    "UP035", # Allow python typing modules
    "RUF005", # Allow using + operator to concatenate collections
    "B904", # Allow raise custom exceptions in except blocks
    "F403", # Allow wildcard imports
    "E721", # Allow using == to compare with type
    "UP031", # Allow percent format
    "RUF022", # Allow unsorted __all__ value
    "E731"
]
# Allow fix for all enabled rules (when `--fix`) is provided.
fixable = ["ALL"]
unfixable = []

[tool.ruff.format]
docstring-code-format = false
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"

[tool.ruff.lint.isort]
known-first-party = ["gepa"]
known-third-party = ["dspy"]

[tool.ruff.lint.flake8-tidy-imports]
ban-relative-imports = "all"

[tool.ruff.lint.per-file-ignores]
"tests/**/*.py" = [
    "S101",    # Allow assert statements in tests
    "TID252",  # Allow relative imports in tests
    "ARG001",  # Allow unused arguments in tests (like pytest fixtures)
]
"__init__.py" = ["F401"]  # Init files can be empty
"src/gepa/gskill/**/*.py" = ["E402"]  # gskill suppresses logging before imports
"examples/**/*.py" = ["E402"]  # Jupyter-notebook-style scripts import mid-file

## `docs/README.md`

# GEPA Documentation

This directory contains the MkDocs documentation for GEPA.

## Building the Documentation

### Prerequisites

Install the documentation dependencies using uv:

```bash
cd docs
uv pip install -r requirements.txt
```

### Generate API Documentation

Before building, generate the API reference pages:

```bash
uv run python scripts/generate_api_docs.py
```

The script auto-generates documentation for all items in `API_MAPPING`, including:
- **Core**: optimize, GEPAAdapter, EvaluationBatch, GEPAResult, GEPACallback, DataLoader, GEPAState, EvaluationCache
- **Callbacks**: All event types (OptimizationStartEvent, IterationEndEvent, etc.) and CompositeCallback
- **Stop Conditions**: All stopper classes
- **Adapters**: DefaultAdapter, DSPyAdapter, RAGAdapter, MCPAdapter, etc.
- **Proposers**: CandidateProposal, ReflectiveMutationProposer, MergeProposer, etc.
- **Logging**: LoggerProtocol, StdOutLogger, Logger, ExperimentTracker, create_experiment_tracker
- **Strategies**: BatchSampler, CandidateSelector, ComponentSelector, EvaluationPolicy variants

### Validating API Documentation

To ensure all API items can be imported:

```bash
uv run python scripts/generate_api_docs.py --validate
```

### Local Development

To serve the documentation locally with live reloading:

```bash
uv run mkdocs serve
```

Then visit http://localhost:8000

### Building for Production

To build the static site:

```bash
uv run mkdocs build
```

The output will be in the `site/` directory.

## Structure

```
docs/
├── docs/                    # Documentation source files
│   ├── index.md            # Home page
│   ├── api/                # Auto-generated API reference
│   │   ├── core/           # Core classes and functions
│   │   ├── callbacks/      # Callback system and events
│   │   ├── stop_conditions/# Stop condition classes
│   │   ├── adapters/       # Adapter implementations
│   │   ├── proposers/      # Proposer classes
│   │   ├── logging/        # Logging utilities
│   │   └── strategies/     # Strategy classes
│   ├── guides/             # User guides
│   │   ├── quickstart.md   # Getting started guide
│   │   ├── adapters.md     # Creating custom adapters
│   │   ├── callbacks.md    # Using the callback system
│   │   └── contributing.md # Contributing guide
│   └── tutorials/          # Tutorial notebooks
├── scripts/
│   └── generate_api_docs.py # API doc generator (automated)
├── mkdocs.yml              # MkDocs configuration
└── requirements.txt        # Python dependencies
```

## Adding Content

### Adding a New Guide

1. Create a new `.md` file in `docs/guides/`
2. Add it to the `nav` section in `mkdocs.yml`

### Adding a Tutorial Notebook

1. Copy the `.ipynb` file to `docs/tutorials/`
2. Add it to the `nav` section in `mkdocs.yml`

### Adding API Documentation

The API documentation is auto-generated from `scripts/generate_api_docs.py`:

1. Add the new module/class to the `API_MAPPING` dictionary in `scripts/generate_api_docs.py`
2. Run `uv run python scripts/generate_api_docs.py` to regenerate all API docs
3. Add the new page to the `nav` section in `mkdocs.yml`

**Note**: The `API_MAPPING` in `generate_api_docs.py` is the source of truth for API documentation. 
The script auto-generates both the markdown files and the index content.

## Automation Features

The `generate_api_docs.py` script provides several automation features:

| Command | Description |
|---------|-------------|
| `python scripts/generate_api_docs.py` | Generate all API documentation |
| `python scripts/generate_api_docs.py --validate` | Validate all API imports work |
| `python scripts/generate_api_docs.py --print-nav` | Print nav structure for mkdocs.yml |

## Social Media Preview Screenshots

Social media previews are automatically generated for all key pages during CI builds. When users share links on Twitter, LinkedIn, Facebook, etc., they see beautiful preview cards.

### How It Works

1. **Local Development**: No impact - script only runs in CI
2. **CI Build**: After `mkdocs build`, Playwright captures page screenshots at 1200×630px
3. **Screenshot Updates**: Script updates `og:image` tags in HTML to point to generated previews
4. **Deploy**: Screenshots are included in the deployed site

### Configured Pages

The following pages get automatic social preview screenshots:

| Page | Screenshot Path | Purpose |
|------|-----------------|---------|
| Home | `/assets/social/home.png` | Main landing page preview |
| Showcase (Use Cases) | `/assets/social/showcase.png` | Production use cases |
| About | `/assets/social/about.png` | About GEPA |
| Blog Index | `/assets/social/blog.png` | Blog feed |
| Guides | `/assets/social/guides.png` | Documentation guides |
| API Docs | `/assets/social/api.png` | API reference |
| Tutorials | `/assets/social/tutorials.png` | Tutorial notebooks |

### Custom Social Images

To provide a custom social preview image for a blog post or page, add OG meta tags to the frontmatter:

```yaml
---
title: My Blog Post
meta:
  - property: og:image
    content: /blog/2026/02/18/my-post/custom-header.png
  - name: twitter:image
    content: /blog/2026/02/18/my-post/custom-header.png
---
```

The script will skip updating OG tags for pages that already have custom images defined.

### Adding More Pages

To include additional pages in screenshot generation, edit `docs/scripts/generate_social_screenshots.py`:

```python
def get_pages_to_screenshot() -> list[tuple[str, str]]:
    return [
        # Add your page here
        ("site/path/to/page/index.html", "site/assets/social/page-name.png"),
    ]
```

And update the `og_updates` dictionary:

```python
og_updates = {
    # Add corresponding update here
    "path/to/page/index.html": "/assets/social/page-name.png",
}
```

### Screenshot Generation Script

Location: `docs/scripts/generate_social_screenshots.py`

**Environment Detection**: Only runs in CI (`CI` environment variable must be set)

**Dependencies**:
- `playwright>=1.40.0` - Browser automation
- `pillow>=10.0.0` - Image processing

**Workflow Steps**:
1. Install Playwright browsers with system dependencies
2. Render each configured page in a 1200×630px viewport
3. Take screenshot and save to `/assets/social/`
4. Update OG image tags in HTML files to point to screenshots

## Deployment

Documentation is automatically built and deployed to GitHub Pages on push to main via GitHub Actions.

Staging deployments to Cloudflare Pages work identically - they also include social preview screenshots.

### Troubleshooting

**Build fails with import errors:**
- Ensure all GEPA dependencies are installed
- Check that `src/gepa` is importable
- Run `--validate` to check specific imports

**Pages not updating:**
- Check the Actions tab for failed deployments
- Verify GitHub Pages is set to "GitHub Actions" source

**Local build works but CI fails:**
- CI installs from `pyproject.toml`, not editable mode
- Ensure all imports work without editable install

**API docs out of sync with nav:**

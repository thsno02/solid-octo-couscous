# Repository semantic capsule: getzep/graphiti

- Commit: `c035afb7990b6077331a81e98b04efcfd9bf8184`
- Default branch: `main`
- Description: getzep/graphiti
- Selected evidence files: 8 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

<p align="center">
  <a href="https://www.getzep.com/">
    <img src="https://github.com/user-attachments/assets/119c5682-9654-4257-8922-56b7cb8ffd73" width="150" alt="Zep Logo">
  </a>
</p>

<h1 align="center">
Graphiti
</h1>
<h2 align="center">A Framework for Building Temporal Knowledge Graphs</h2>

<div align="center">

[![Lint](https://github.com/getzep/Graphiti/actions/workflows/lint.yml/badge.svg?style=flat)](https://github.com/getzep/Graphiti/actions/workflows/lint.yml)
[![Unit Tests](https://github.com/getzep/Graphiti/actions/workflows/unit_tests.yml/badge.svg)](https://github.com/getzep/Graphiti/actions/workflows/unit_tests.yml)
[![MyPy Check](https://github.com/getzep/Graphiti/actions/workflows/typecheck.yml/badge.svg)](https://github.com/getzep/Graphiti/actions/workflows/typecheck.yml)

[![GitHub Repo stars](https://img.shields.io/github/stars/getzep/graphiti)](https://github.com/getzep/graphiti/stargazers)
[![arXiv](https://img.shields.io/badge/arXiv-2501.13956-b31b1b.svg?style=flat)](https://arxiv.org/abs/2501.13956)
[![Release](https://img.shields.io/github/v/release/getzep/graphiti?style=flat&label=Release&color=limegreen)](https://github.com/getzep/graphiti/releases)

</div>
<div align="center">

<a href="https://trendshift.io/repositories/12986" target="_blank"><img src="https://trendshift.io/api/badge/repositories/12986" alt="getzep%2Fgraphiti | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

</div>

> [!NOTE]
> **We're Hiring!** Build context graphs that power reliable, personalized, fast production AI agents.
> Come build with us — we're hiring Engineers and Developer Relations folks. [View open roles](https://www.getzep.com/careers/).

⭐ *Help us reach more developers and grow the Graphiti community. Star this repo!*

&nbsp;

Graphiti is a framework for building and querying temporal context graphs for AI agents. Unlike static knowledge graphs,
Graphiti's context graphs track how facts change over time, maintain provenance to source data, and support both
prescribed and learned ontology — making them purpose-built for agents operating on evolving, real-world data.

Unlike traditional retrieval-augmented generation (RAG) methods, Graphiti continuously integrates user interactions,
structured and unstructured enterprise data, and external information into a coherent, queryable graph. The framework
supports incremental data updates, efficient retrieval, and precise historical queries without requiring complete graph
recomputation, making it suitable for developing interactive, context-aware AI applications.

Use Graphiti to:

- Build temporal knowledge graphs that evolve with every interaction — tracking what's true now and what was true before.
- Represent rich, structured context instead of flat document chunks or raw event streams.
- Query across time, meaning, and relationships with hybrid retrieval (semantic + keyword + graph traversal).

&nbsp;

<p align="center">
    <img src="images/graphiti-graph-intro.gif" alt="Graphiti temporal walkthrough" width="700px">
</p>

&nbsp;

## What is a Context Graph?

A **context graph** is a temporal graph of entities, relationships, and facts — like *"Kendra loves Adidas shoes (as of
March 2026)."* Unlike traditional knowledge graphs, each fact in a context graph has a validity window: when it became
true, and when (if ever) it was superseded. Entities evolve over time with updated summaries. Everything traces back to
**episodes** — the raw data that produced it.

What makes Graphiti unique is its ability to autonomously build context graphs from unstructured and structured data,
handling changing relationships while preserving full temporal history.

A context graph contains:

| Component | What it stores |
|-----------|---------------|
| **Entities** (nodes) | People, products, policies, concepts — with summaries that evolve over time |
| **Facts / Relationships** (edges) | Triplets (Entity → Relationship → Entity) with temporal validity windows |
| **Episodes** (provenance) | Raw data as ingested — the ground truth stream. Every derived fact traces back here |
| **Custom Types** (ontology) | Developer-defined entity and edge types via Pydantic models |

## Graphiti and Zep

Graphiti is the open-source framework for building temporal knowledge graphs at the core of
[Zep's](https://www.getzep.com) context infrastructure. Zep manages context graphs at scale, providing
governed, low-latency context retrieval and assembly for production deployments.

Under the hood, Zep is powered by a proprietary graph database — the
[Context Graph Engine](https://www.getzep.com/platform/context-graph-engine/) — built for millions of context graphs
with low-latency retrieval, so production deployments don't require a separate third-party graph database.

Read our paper: [Zep: A Temporal Knowledge Graph Architecture](https://arxiv.org/abs/2501.13956).

<p align="center">
    <a href="https://arxiv.org/abs/2501.13956"><img src="images/arxiv-screenshot.png" alt="Zep: A Temporal Knowledge Graph Architecture" width="700px"></a>
</p>

## Zep vs Graphiti

| Aspect | Zep | Graphiti |
|--------|-----|---------|
| **What they are** | Managed context graph infrastructure | Open-source framework for building temporal knowledge graphs |
| **Context graphs** | Manages vast numbers of per-user/entity context graphs with governance | Build and query individual context graphs |
| **Graph database** | Proprietary [Context Graph Engine](https://www.getzep.com/platform/context-graph-engine/) — built for millions of context graphs with low-latency retrieval; no third-party graph database vendor required | Bring your own third-party graph database |
| **User & conversation management** | Built-in users, threads, and message storage | Build your own |
| **Retrieval & performance** | Pre-configured, production-ready retrieval with sub-200ms performance at scale | Custom implementation required; performance depends on your setup |
| **Developer tools** | Dashboard with graph visualization, debug logs, API logs; SDKs for Python, TypeScript, and Go | Build your own tools |
| **Enterprise features** | SLAs, support, security guarantees | Self-managed |
| **Deployment** | Fully managed or in your cloud | Self-hosted only |

### When to choose which

**Choose Zep** if you want a turnkey, enterprise-grade platform with security, performance, and support baked in.

**Choose Graphiti** if you want a flexible OSS core and you're comfortable building/operating the surrounding system.

## Why Graphiti?

Traditional RAG approaches often rely on batch processing and static data summarization, making them inefficient for
frequently changing data. Graphiti addresses these challenges by providing:

- **Temporal Fact Management:** Facts have validity windows. When information changes, old facts are
  invalidated — not deleted. Query what's true now, or what was true at any point in time.
- **Episodes & Provenance:** Every entity and relationship traces back to the episodes (raw data) that produced it.
  Full lineage from derived fact to source.
- **Prescribed & Learned Ontology:** Define entity and edge types upfront via Pydantic models (prescribed), or let
  structure emerge from your data (learned). Start simple, evolve as patterns appear.
- **Incremental Graph Construction:** New data integrates immediately without batch recomputation. The graph evolves
  in real-time as episodes are ingested.
- **Hybrid Retrieval:** Combines semantic embeddings, keyword (BM25), and graph traversal for low-latency,
  high-precision queries without reliance on LLM summarization.
- **Scalability:** Efficiently manages large datasets with parallel processing, pluggable graph backends, suitable
  for enterprise workloads.

<p align="center">
    <img src="/images/graphiti-intro-slides-stock-2.gif" alt="Graphiti structured + unstructured demo" width="700px">
</p>

## Graphiti vs. GraphRAG

| Aspect | GraphRAG | Graphiti |
|--------|----------|---------|
| **Primary Use** | Static document summarization | Dynamic, evolving temporal knowledge graphs |
| **Data Handling** | Batch-oriented processing | Continuous, incremental updates |
| **Knowledge Structure** | Entity clusters & community summaries | Temporal context graph — entities, facts with validity windows, episodes, communities |
| **Retrieval Method** | Sequential LLM summarization | Hybrid semantic, keyword, and graph-based search |
| **Adaptability** | Low | High |
| **Temporal Handling** | Basic timestamp tracking | Explicit bi-temporal tracking with automatic fact invalidation |
| **Contradiction Handling** | LLM-driven summarization judgments | Automatic fact invalidation with temporal history preserved |
| **Query Latency** | Seconds to tens of seconds | Typically sub-second latency |
| **Custom Entity Types** | No | Yes, customizable via Pydantic models |
| **Scalability** | Moderate | High, optimized for large datasets |

Graphiti is specifically designed to address the challenges of dynamic and frequently updated datasets, making it
particularly suitable for applications requiring real-time interaction and precise historical queries.

## Installation

Requirements:

- Python 3.10 or higher
- Neo4j 5.26 / FalkorDB 1.1.2 / Amazon Neptune Database Cluster or Neptune Analytics Graph + Amazon OpenSearch
  Serverless collection (serves as the full text search backend) / Kuzu 0.11.2 (**deprecated**, see below)
- OpenAI API key (Graphiti defaults to OpenAI for LLM inference and embedding)

> [!IMPORTANT]
> Graphiti works best with LLM services that support Structured Output (such as OpenAI, Anthropic, and Gemini).
> Using other services may result in incorrect output schemas and ingestion failures. This is particularly
> problematic when using smaller models.

Optional:

- Google Gemini, Anthropic, or Groq API key (for alternative LLM providers)

> [!TIP]
> The simplest way to install Neo4j is via [Neo4j Desktop](https://neo4j.com/download/). It provides a user-friendly
> interface to manage Neo4j instances and databases.
> Alternatively, you can use FalkorDB on-premises via Docker and instantly start with the quickstart example:
> ```
> docker run -p 6379:6379 -p 3000:3000 -it --rm falkordb/falkordb:latest
> ```

```bash
pip install graphiti-core
```

or

```bash
uv add graphiti-core
```

### Installing with FalkorDB Support

If you plan to use FalkorDB as your graph database backend, install with the FalkorDB extra:

```bash
pip install graphiti-core[falkordb]

# or with uv
uv add graphiti-core[falkordb]

# or embedded version (requires Python 3.12+)
pip install graphiti-core[falkordblite]
# or with uv
uv add graphiti-core[falkordblite]
```

### Installing with Kuzu Support

> [!WARNING]
> **Kuzu is deprecated** and will be removed in a future release — the upstream Kuzu project is no longer
> maintained. New projects should use Neo4j or FalkorDB. The driver still ships for now but emits a
> `DeprecationWarning`.

If you plan to use Kuzu as your graph database backend, install with the Kuzu extra:

```bash
pip install graphiti-core[kuzu]

# or with uv
uv add graphiti-core[kuzu]
```

## `AGENTS.md`

# Repository Guidelines

## Project Structure & Module Organization
Graphiti's core library lives under `graphiti_core/`, split into domain modules such as `nodes.py`, `edges.py`, `models/`, and `search/` for retrieval pipelines. Database drivers in `graphiti_core/driver/` support Neo4j, FalkorDB, and Neptune (plus a deprecated Kuzu driver). Additional core modules include `cross_encoder/` (reranking via BGE, OpenAI, and Gemini), `telemetry/` (OpenTelemetry tracing), `namespaces/` (namespace management), and `migrations/` (database migrations). Service adapters and API glue reside in `server/graph_service/`, while the MCP integration lives in `mcp_server/` (with its own `src/`, `tests/`, `config/`, and `docker/` subdirectories). Shared assets sit in `images/` and `examples/`. Tests cover the core package via `tests/`, with configuration in `conftest.py`, `pytest.ini`, and Docker compose files for optional services. Specifications live in `spec/` and type signatures in `signatures/`. Tooling manifests live at the repo root, including `pyproject.toml`, `Makefile`, and deployment compose files.

## Build, Test, and Development Commands
- `make install`: install the dev environment (`uv sync --extra dev`).
- `make format`: run `ruff` to sort imports and apply the canonical formatter.
- `make lint`: execute `ruff` plus `pyright` type checks against `graphiti_core`.
- `make test`: run unit tests only, excluding integration tests and disabling non-Neo4j drivers (`DISABLE_FALKORDB=1 DISABLE_KUZU=1 DISABLE_NEPTUNE=1 uv run pytest -m "not integration"`).
- `make check`: run format, lint, and test in sequence.
- `uv run pytest tests/path/test_file.py`: target a specific module or test selection.
- `docker-compose -f docker-compose.test.yml up`: provision local graph/search dependencies for integration flows.

## Coding Style & Naming Conventions
Python code uses 4-space indentation, 100-character lines, and prefers single quotes as configured in `pyproject.toml`. Modules, files, and functions stay snake_case; Pydantic models in `graphiti_core/models` use PascalCase with explicit type hints. Keep side-effectful code inside drivers or adapters (`graphiti_core/driver`, `graphiti_core/cross_encoder`, `graphiti_core/utils`) and rely on pure helpers elsewhere. Run `make format` before committing to normalize imports and docstring formatting.

## Testing Guidelines
Author tests alongside features under `tests/`, naming files `test_<feature>.py` and functions `test_<behavior>`. Integration test files use the `_int` suffix (e.g., `test_edge_int.py`, `test_node_int.py`). Use `@pytest.mark.integration` for database-reliant scenarios so CI can gate them; `make test` excludes these by default. Async tests run automatically via `asyncio_mode = auto` in `pytest.ini`. Reproduce regressions with a failing test first and validate fixes via `uv run pytest -k "pattern"`. Start required backing services through `docker-compose.test.yml` when running integration suites locally. The `mcp_server/` has its own separate test suite under `mcp_server/tests/`.

## Commit & Pull Request Guidelines
Commits use an imperative, present-tense summary (for example, `add async cache invalidation`) optionally suffixed with the PR number as seen in history (`(#927)`). Squash fixups and keep unrelated changes isolated. Pull requests should include: a concise description, linked tracking issue, notes about schema or API impacts, and screenshots or logs when behavior changes. Confirm `make lint` and `make test` pass locally, and update docs or examples when public interfaces shift.

## Cursor Cloud specific instructions

Dependencies are installed by the startup update script (`uv sync` in the repo root, `server/`, and `mcp_server/`). `uv` lives at `~/.local/bin`; if it is not on `PATH`, prefix commands with `PATH="$HOME/.local/bin:$PATH"`. Set `GRAPHITI_TELEMETRY_ENABLED=false` when running anything to avoid PostHog network calls.

### Graph databases (Neo4j + FalkorDB via Docker)
Docker has no systemd here — start the daemon manually once per VM: `sudo dockerd > /tmp/dockerd.log 2>&1 &`. Then start the DBs on the host network exactly as CI does (see `.github/workflows/unit_tests.yml`):
- `sudo docker run -d --name falkordb --network host falkordb/falkordb:latest` (port 6379)
- `sudo docker run -d --name neo4j --network host -e NEO4J_AUTH=neo4j/testpass -e NEO4J_PLUGINS='["apoc"]' neo4j:5.26-community` (bolt 7687, http 7474)

### Tests (non-obvious)
- `make test` does NOT set `DISABLE_NEO4J`, so the `graph_driver` fixture stays parametrized on Neo4j and the suite REQUIRES a reachable Neo4j at `bolt://localhost:7687`. With no Neo4j, those tests hang on the driver's connection retry (not an env bug). Run it as `NEO4J_PASSWORD=testpass make test`.
- `tests/test_add_triplet.py` has pre-existing failures (its mock embedder doesn't stub `create_batch`, so `zip(strict=True)` raises). CI never runs this file, so ignore those 11 failures — they are unrelated to environment setup.
- The authoritative, fully-green no-DB unit gate is the CI command in `.github/workflows/unit_tests.yml` (`DISABLE_NEO4J=1 DISABLE_FALKORDB=1 DISABLE_KUZU=1 DISABLE_NEPTUNE=1` plus the `--ignore` list). The DB-backed unit tests are the `database-integration-tests` job in the same file (needs Neo4j + FalkorDB, uses mock LLMs, no API key).
- `server/` and `mcp_server/` test suites are live end-to-end tests marked `integration`; they self-skip with exit code 5 when `OPENAI_API_KEY` is unset. This skip is expected, not a failure.

### Running the services (dev mode)
All three run without a valid OpenAI key for startup/health only; real ingest/search (LLM extraction + embeddings) needs a real `OPENAI_API_KEY`.
- REST API (`server/`): `OPENAI_API_KEY=<placeholder-or-real> DB_BACKEND=falkordb FALKORDB_HOST=localhost FALKORDB_PORT=6379 uv run uvicorn graph_service.main:app --reload --port 8000`. Health at `/healthcheck`, Swagger at `/docs`. `Settings` requires `OPENAI_API_KEY` to be present (any value) or startup fails.
- MCP server (`mcp_server/`): `OPENAI_API_KEY=<...> FALKORDB_URI=redis://localhost:6379 uv run python main.py --transport http --host 0.0.0.0 --port 8001 --database-provider falkordb`. Serves streamable HTTP MCP at `/mcp/` (use port 8001 if 8000 is taken by the REST server).

### Backend gotcha
The FalkorDB async driver drops the connection ("Connection closed by server") when Graphiti issues concurrent queries on one connection (e.g. the gather inside `Graphiti.search`). For local hybrid-search work, prefer the Neo4j backend, which handles concurrent queries reliably.

## `CLAUDE.md`

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Graphiti is a Python framework for building temporally-aware knowledge graphs designed for AI agents. It enables real-time incremental updates to knowledge graphs without batch recomputation, making it suitable for dynamic environments.

Key features:

- Bi-temporal data model with explicit tracking of event occurrence times
- Hybrid retrieval combining semantic embeddings, keyword search (BM25), and graph traversal
- Support for custom entity definitions via Pydantic models
- Integration with Neo4j and FalkorDB as graph storage backends
- Optional OpenTelemetry distributed tracing support

## Development Commands

### Main Development Commands (run from project root)

```bash
# Install dependencies
uv sync --extra dev

# Format code (ruff import sorting + formatting)
make format

# Lint code (ruff + pyright type checking)
make lint

# Run tests
make test

# Run all checks (format, lint, test)
make check
```

### Server Development (run from server/ directory)

```bash
cd server/
# Install server dependencies
uv sync --extra dev

# Run server in development mode
uvicorn graph_service.main:app --reload

# Format, lint, test server code
make format
make lint
make test
```

### MCP Server Development (run from mcp_server/ directory)

```bash
cd mcp_server/
# Install MCP server dependencies
uv sync

# Run with Docker Compose
docker-compose up
```

## Code Architecture

### Core Library (`graphiti_core/`)

- **Main Entry Point**: `graphiti.py` - Contains the main `Graphiti` class that orchestrates all functionality
- **Graph Storage**: `driver/` - Database drivers for Neo4j and FalkorDB
- **LLM Integration**: `llm_client/` - Clients for OpenAI, Anthropic, Gemini, Groq
- **Embeddings**: `embedder/` - Embedding clients for various providers
- **Graph Elements**: `nodes.py`, `edges.py` - Core graph data structures
- **Search**: `search/` - Hybrid search implementation with configurable strategies
- **Prompts**: `prompts/` - LLM prompts for entity extraction, deduplication, summarization
- **Utilities**: `utils/` - Maintenance operations, bulk processing, datetime handling

### Server (`server/`)

- **FastAPI Service**: `graph_service/main.py` - REST API server
- **Routers**: `routers/` - API endpoints for ingestion and retrieval
- **DTOs**: `dto/` - Data transfer objects for API contracts

### MCP Server (`mcp_server/`)

- **MCP Implementation**: `graphiti_mcp_server.py` - Model Context Protocol server for AI assistants
- **Docker Support**: Containerized deployment with Neo4j

## Testing

- **Unit Tests**: `tests/` - Comprehensive test suite using pytest
- **Integration Tests**: Tests marked with `_int` suffix require database connections
- **Evaluation**: `tests/evals/` - End-to-end evaluation scripts

## Configuration

### Environment Variables

- `OPENAI_API_KEY` - Required for LLM inference and embeddings
- `USE_PARALLEL_RUNTIME` - Optional boolean for Neo4j parallel runtime (enterprise only)
- Provider-specific keys: `ANTHROPIC_API_KEY`, `GOOGLE_API_KEY`, `GROQ_API_KEY`, `VOYAGE_API_KEY`

### Database Setup

- **Neo4j**: Version 5.26+ required, available via Neo4j Desktop
  - Database name defaults to `neo4j` (hardcoded in Neo4jDriver)
  - Override by passing `database` parameter to driver constructor
- **FalkorDB**: Version 1.1.2+ as alternative backend
  - Database name defaults to `default_db` (hardcoded in FalkorDriver)
  - Override by passing `database` parameter to driver constructor

## Development Guidelines

### Code Style

- Use Ruff for formatting and linting (configured in pyproject.toml)
- Line length: 100 characters
- Quote style: single quotes
- Type checking with Pyright is enforced
- Main project uses `typeCheckingMode = "basic"`, server uses `typeCheckingMode = "standard"`

### Testing Requirements

- Run tests with `make test` or `pytest`
- Integration tests require database connections and are marked with `_int` suffix
- Use `pytest-xdist` for parallel test execution
- Run specific test files: `pytest tests/test_specific_file.py`
- Run specific test methods: `pytest tests/test_file.py::test_method_name`
- Run only integration tests: `pytest tests/ -k "_int"`
- Run only unit tests: `pytest tests/ -k "not _int"`

### LLM Provider Support

The codebase supports multiple LLM providers but works best with services supporting structured output (OpenAI, Gemini). Other providers may cause schema validation issues, especially with smaller models.

#### Current LLM Models (as of November 2025)

**OpenAI Models:**
- **GPT-5 Family** (Reasoning models, require temperature=0):
  - `gpt-5-mini` - Fast reasoning model
  - `gpt-5-nano` - Smallest reasoning model
- **GPT-4.1 Family** (Standard models):
  - `gpt-4.1` - Full capability model
  - `gpt-4.1-mini` - Efficient model for most tasks
  - `gpt-4.1-nano` - Lightweight model
- **Legacy Models** (Still supported):
  - `gpt-4o` - Previous generation flagship
  - `gpt-4o-mini` - Previous generation efficient

**Anthropic Models:**
- **Claude 4.5 Family** (Latest):
  - `claude-sonnet-4-5-latest` - Flagship model, auto-updates
  - `claude-sonnet-4-5-20250929` - Pinned Sonnet version from September 2025
  - `claude-haiku-4-5-latest` - Fast model, auto-updates
- **Claude 3.7 Family**:
  - `claude-3-7-sonnet-latest` - Auto-updates
  - `claude-3-7-sonnet-20250219` - Pinned version from February 2025
- **Claude 3.5 Family**:
  - `claude-3-5-sonnet-latest` - Auto-updates
  - `claude-3-5-sonnet-20241022` - Pinned version from October 2024
  - `claude-3-5-haiku-latest` - Fast model

**Google Gemini Models:**
- **Gemini 2.5 Family** (Latest):
  - `gemini-2.5-pro` - Flagship reasoning and multimodal
  - `gemini-2.5-flash` - Fast, efficient
- **Gemini 2.0 Family**:
  - `gemini-2.0-flash` - Experimental fast model
- **Gemini 1.5 Family** (Stable):
  - `gemini-1.5-pro` - Production-stable flagship
  - `gemini-1.5-flash` - Production-stable efficient

**Note**: Model names like `gpt-5-mini`, `gpt-4.1`, and `gpt-4.1-mini` used in this codebase are valid OpenAI model identifiers. The GPT-5 family are reasoning models that require `temperature=0` (automatically handled in the code).

### MCP Server Usage Guidelines

When working with the MCP server, follow the patterns established in `mcp_server/cursor_rules.md`:

- Always search for existing knowledge before adding new information
- Use specific entity type filters (`Preference`, `Procedure`, `Requirement`)
- Store new information immediately using `add_memory`
- Follow discovered procedures and respect established preferences

## `CONTRIBUTING.md`

# Contributing to Graphiti

We're thrilled you're interested in contributing to Graphiti! As firm believers in the power of open source collaboration, we're committed to building not just a tool, but a vibrant community where developers of all experience levels can make meaningful contributions.

When I first joined this project, I was overwhelmed trying to figure out where to start. Someone eventually pointed me to a random "good first issue," but I later discovered there were multiple ways I could have contributed that would have better matched my skills and interests.

We've restructured our contribution paths to solve this problem:

# Four Ways to Get Involved

### Pick Up Existing Issues

Our developers regularly tag issues with "help wanted" and "good first issue." These are pre-vetted tasks with clear scope and someone ready to help you if you get stuck.

### Create Your Own Tickets

See something that needs fixing? Have an idea for an improvement? You don't need permission to identify problems. The people closest to the pain are often best positioned to describe the solution.

For **feature requests**, tell us the story of what you're trying to accomplish. What are you working on? What's getting in your way? What would make your life easier? Submit these through our [GitHub issue tracker](https://github.com/getzep/graphiti/issues) with a "Feature Request" label.

For **bug reports**, we need enough context to reproduce the problem. Use the [GitHub issue tracker](https://github.com/getzep/graphiti/issues) and include:

- A clear title that summarizes the specific problem
- What you were trying to do when you encountered the bug
- What you expected to happen
- What actually happened
- A code sample or test case that demonstrates the issue

### Share Your Use Cases

Sometimes the most valuable contribution isn't code. If you're using our project in an interesting way, add it to the [examples](https://github.com/getzep/graphiti/tree/main/examples) folder. This helps others discover new possibilities and counts as a meaningful contribution. We regularly feature compelling examples in our blog posts and videos - your work might be showcased to the broader community!

### Help Others on GitHub

Join the conversation on [GitHub Issues](https://github.com/getzep/graphiti/issues) and pitch in at the helpdesk. Answering questions and helping troubleshoot issues is an incredibly valuable contribution that benefits everyone. The knowledge you share today saves someone hours of frustration tomorrow.

## What happens next?

### Contribution Priorities

We prioritize **bug fixes to existing functionality**. If you've found a bug, please submit a fix — these PRs get the most attention and fastest review.

### RFC Required for New Features and Integrations

**All new features and integrations require an RFC** (a GitHub issue discussing the technical design and justification) **before submitting a PR.** This includes:

- New database drivers
- New LLM provider clients
- New embedding provider clients
- New API endpoints or capabilities
- Any major architectural change

Additionally, any PR over 500 LOC requires an RFC regardless of type.

PRs submitted without a linked RFC issue will be tagged with `needs-rfc` and will not be reviewed until the RFC is approved. Please open the issue first, discuss the design, and then submit your PR referencing it.

Once you've found an issue tagged with "good first issue" or "help wanted," or prepared an example to share, here's how to turn that into a contribution:

1. Share your approach in the [issue discussion](https://github.com/getzep/graphiti/issues) before diving deep into code. This helps ensure your solution adheres to the architecture of Graphiti from the start and saves you from potential rework.

2. Fork the repo, make your changes in a branch, and submit a PR. We've included more detailed technical instructions below; be open to feedback during review.

## Setup

1. Fork the repository on GitHub.
2. Clone your fork locally:
   ```
   git clone https://github.com/getzep/graphiti
   cd graphiti
   ```
3. Set up your development environment:

   - Ensure you have Python 3.10+ installed.
   - Install uv: https://docs.astral.sh/uv/getting-started/installation/
   - Install project dependencies:
     ```
     make install
     ```
   - To run integration tests, set the appropriate environment variables

     ```
     export TEST_OPENAI_API_KEY=...
     export TEST_OPENAI_MODEL=...
     export TEST_ANTHROPIC_API_KEY=...

     # For Neo4j
     export TEST_URI=neo4j://...
     export TEST_USER=...
     export TEST_PASSWORD=...
     ```

## Making Changes

1. Create a new branch for your changes:
   ```
   git checkout -b your-branch-name
   ```
2. Make your changes in the codebase.
3. Write or update tests as necessary.
4. Run the tests to ensure they pass:
   ```
   make test
   ```
5. Format your code:
   ```
   make format
   ```
6. Run linting checks:
   ```
   make lint
   ```

## Submitting Changes

1. Commit your changes:
   ```
   git commit -m "Your detailed commit message"
   ```
2. Push to your fork:
   ```
   git push origin your-branch-name
   ```
3. Submit a pull request through the GitHub website to https://github.com/getzep/graphiti.

## Pull Request Guidelines

- Provide a clear title and description of your changes.
- Include any relevant issue numbers in the PR description.
- Ensure all tests pass and there are no linting errors.
- Update documentation if you're changing functionality.

## Code Style and Quality

We use several tools to maintain code quality:

- Ruff for linting and formatting
- Pyright for static type checking
- Pytest for testing

Before submitting a pull request, please run:

```
make check
```

This command will format your code, run linting checks, and execute tests.

## Third-Party Integrations

When contributing integrations for third-party services (LLM providers, embedding services, databases, etc.), please follow these patterns:

### Optional Dependencies

All third-party integrations must be optional dependencies to keep the core library lightweight. Follow this pattern:

1. **Add to `pyproject.toml`**: Define your dependency as an optional extra AND include it in the dev extra:
   ```toml
   [project.optional-dependencies]
   your-service = ["your-package>=1.0.0"]
   dev = [
       # ... existing dev dependencies
       "your-package>=1.0.0",  # Include all optional extras here
       # ... other dependencies
   ]
   ```

2. **Use TYPE_CHECKING pattern**: In your integration module, import dependencies conditionally:
   ```python
   from typing import TYPE_CHECKING
   
   if TYPE_CHECKING:
       import your_package
       from your_package import SomeType
   else:
       try:
           import your_package
           from your_package import SomeType
       except ImportError:
           raise ImportError(
               'your-package is required for YourServiceClient. '
               'Install it with: pip install graphiti-core[your-service]'
           ) from None
   ```

3. **Benefits of this pattern**:
   - Fast startup times (no import overhead during type checking)
   - Clear error messages with installation instructions
   - Proper type hints for development
   - Consistent user experience

4. **Do NOT**:
   - Add optional imports to `__init__.py` files
   - Use direct imports without error handling
   - Include optional dependencies in the main `dependencies` list

### Integration Structure

- Place LLM clients in `graphiti_core/llm_client/`
- Place embedding clients in `graphiti_core/embedder/`
- Place database drivers in `graphiti_core/driver/`
- Follow existing naming conventions (e.g., `your_service_client.py`)

### Adding a Graph Driver

Graphiti's driver layer is backend-agnostic. To add support for a new graph database, mirror the existing drivers in
`graphiti_core/driver/` and keep the implementation split between the top-level driver and provider-specific
operations.

1. Add the new provider to `graphiti_core/driver/driver.py` in `GraphProvider`.
2. Create `graphiti_core/driver/<backend>_driver.py` implementing the `GraphDriver` interface:
   `execute_query()`, `session()`, `close()`, `build_indices_and_constraints()`, and `delete_all_indexes()`.
3. Add `graphiti_core/driver/<backend>/operations/` and implement the operations interfaces from
   `graphiti_core/driver/operations/`:
   `EntityNodeOperations`, `EpisodeNodeOperations`, `CommunityNodeOperations`, `SagaNodeOperations`,
   `EntityEdgeOperations`, `EpisodicEdgeOperations`, `CommunityEdgeOperations`, `HasEpisodeEdgeOperations`,
   `NextEpisodeEdgeOperations`, `SearchOperations`, and `GraphMaintenanceOperations`.
4. Expose those concrete operations from the driver via the corresponding `@property` accessors on `GraphDriver`.
5. Add provider-specific query variants to `graphiti_core/models/nodes/node_db_queries.py` and
   `graphiti_core/models/edges/edge_db_queries.py`.
6. If the backend needs connection or transaction management, implement a matching `GraphDriverSession`.

## `Dockerfile`

# syntax=docker/dockerfile:1.9
FROM python:3.12-slim

# Inherit build arguments for labels
ARG GRAPHITI_VERSION
ARG BUILD_DATE
ARG VCS_REF

# OCI image annotations
LABEL org.opencontainers.image.title="Graphiti FastAPI Server"
LABEL org.opencontainers.image.description="FastAPI server for Graphiti temporal knowledge graphs"
LABEL org.opencontainers.image.version="${GRAPHITI_VERSION}"
LABEL org.opencontainers.image.created="${BUILD_DATE}"
LABEL org.opencontainers.image.revision="${VCS_REF}"
LABEL org.opencontainers.image.vendor="Zep AI"
LABEL org.opencontainers.image.source="https://github.com/getzep/graphiti"
LABEL org.opencontainers.image.documentation="https://github.com/getzep/graphiti/tree/main/server"
LABEL io.graphiti.core.version="${GRAPHITI_VERSION}"

# Install uv using the installer script
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin:$PATH"

# Install Socket Firewall (sfw) for dependency fetches when SOCKET_API_KEY is
# provided as a BuildKit secret. Community builds without the secret fall back
# to direct installs (see the RUN --mount below).
ARG TARGETARCH
RUN set -eux; \
    case "${TARGETARCH:-amd64}" in \
      amd64) SFW_ARCH=x86_64 ;; \
      arm64) SFW_ARCH=arm64 ;; \
      *) echo "unsupported TARGETARCH=${TARGETARCH}" >&2; exit 1 ;; \
    esac; \
    curl -fsSL --retry 3 --proto '=https' --tlsv1.2 \
      "https://github.com/SocketDev/firewall-release/releases/latest/download/sfw-linux-${SFW_ARCH}" \
      -o /usr/local/bin/sfw; \
    chmod +x /usr/local/bin/sfw

# Configure uv for runtime
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never

# Create non-root user
RUN groupadd -r app && useradd -r -d /app -g app app

# Set up the server application first
WORKDIR /app
COPY ./server/pyproject.toml ./server/README.md ./server/uv.lock ./
COPY ./server/graph_service ./graph_service

# Install server dependencies (without graphiti-core from lockfile)
# Then install graphiti-core from PyPI at the desired version
# This prevents the stale lockfile from pinning an old graphiti-core version
# When socket_api_key is mounted (official releases), route through sfw;
# otherwise install directly so public docker builds keep working.
#
# sfw can only inspect packages that are actually downloaded, so an enforced
# build must defeat both caches or a newly flagged package would ship unscanned:
# SOCKET_SCAN_ID (unique per release run) invalidates this layer, and
# UV_NO_CACHE stops uv serving wheels from the cache mount below.
ARG INSTALL_FALKORDB=false
ARG SOCKET_FIREWALL_ENABLED=false
ARG SOCKET_SCAN_ID=
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=secret,id=socket_api_key \
    set -eu; \
    export SFW_TELEMETRY_DISABLED=true; \
    export SFW_CUSTOM_REGISTRIES="wrap:storage.googleapis.com,wrap:classic.yarnpkg.com,wrap:files.pythonhosted.org"; \
    if [ "$SOCKET_FIREWALL_ENABLED" = "true" ]; then \
      if [ ! -s /run/secrets/socket_api_key ]; then \
        echo "ERROR: SOCKET_FIREWALL_ENABLED=true but socket_api_key is missing" >&2; \
        exit 1; \
      fi; \
      export SOCKET_API_KEY="$(cat /run/secrets/socket_api_key)"; \
      export UV_NO_CACHE=1; \
      echo "Socket Firewall enforced (scan id: ${SOCKET_SCAN_ID})"; \
      UV_CMD="sfw uv"; \
    else \
      echo "socket_api_key absent; installing without Socket Firewall"; \
      UV_CMD="uv"; \
    fi; \
    $UV_CMD sync --frozen --no-dev; \
    if [ -n "$GRAPHITI_VERSION" ]; then \
        if [ "$INSTALL_FALKORDB" = "true" ]; then \
            $UV_CMD pip install --upgrade "graphiti-core[falkordb]==$GRAPHITI_VERSION"; \
        else \
            $UV_CMD pip install --upgrade "graphiti-core==$GRAPHITI_VERSION"; \
        fi; \
    else \
        if [ "$INSTALL_FALKORDB" = "true" ]; then \
            $UV_CMD pip install --upgrade "graphiti-core[falkordb]"; \
        else \
            $UV_CMD pip install --upgrade graphiti-core; \
        fi; \
    fi

# Change ownership to app user
RUN chown -R app:app /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

# Switch to non-root user
USER app

# Set port
ENV PORT=8000
EXPOSE $PORT

# Use uv run with --no-sync to avoid re-syncing on startup
CMD ["uv", "run", "--no-sync", "uvicorn", "graph_service.main:app", "--host", "0.0.0.0", "--port", "8000"]

## `Makefile`

.PHONY: install format lint test all check

# Define variables
PYTHON = python3
UV = uv
PYTEST = $(UV) run pytest
RUFF = $(UV) run ruff
PYRIGHT = $(UV) run pyright

# Default target
all: format lint test

# Install dependencies
install:
	$(UV) sync --extra dev

# Format code
format:
	$(RUFF) check --select I --fix
	$(RUFF) format

# Lint code
lint:
	$(RUFF) check
	$(PYRIGHT) ./graphiti_core 

# Run tests
test:
	DISABLE_FALKORDB=1 DISABLE_KUZU=1 DISABLE_NEPTUNE=1 $(PYTEST) -m "not integration"

# Run format, lint, and test
check: format lint test

## `SECURITY.md`

# Security Policy

## Supported Versions

Use this section to tell people about which versions of your project are
currently being supported with security updates.

| Version | Supported          |
|---------|--------------------|
| 0.x     | :white_check_mark: |


## Reporting a Vulnerability

Please use GitHub's Private Vulnerability Reporting mechanism found in the Security section of this repo.

## `pyproject.toml`

[project]
name = "graphiti-core"
description = "A temporal graph building library"
version = "0.30.2"
authors = [
    { name = "Paul Paliychuk", email = "paul@getzep.com" },
    { name = "Preston Rasmussen", email = "preston@getzep.com" },
    { name = "Daniel Chalef", email = "daniel@getzep.com" },
]
readme = "README.md"
license = "Apache-2.0"
requires-python = ">=3.10,<4"
dependencies = [
    "pydantic>=2.11.5",
    "neo4j>=5.26.0",
    "openai>=1.91.0",
    "tenacity>=9.0.0",
    "numpy>=1.0.0",
    "python-dotenv>=1.0.1",
    "posthog>=3.0.0"
]

[project.urls]
Homepage = "https://help.getzep.com/graphiti/graphiti/overview"
Repository = "https://github.com/getzep/graphiti"

[project.optional-dependencies]
anthropic = ["anthropic>=0.49.0"]
groq = ["groq>=0.2.0"]
google-genai = ["google-genai>=1.62.0"]
# Deprecated: the upstream Kuzu project is unmaintained; this extra will be removed in a future release.
kuzu = ["kuzu>=0.11.3"]
falkordb = ["falkordb>=1.1.2,<2.0.0"]
# redis<9 pin: redis-py 8.x breaks falkordblite's embedded server startup
falkordblite = ["falkordblite>=0.5.0; python_version>='3.12'", "redis<9; python_version>='3.12'"]
voyageai = ["voyageai>=0.2.3"]
gliner2 = ["gliner2>=1.2.0; python_version>='3.11'"]
neo4j-opensearch = ["boto3>=1.39.16", "opensearch-py>=3.0.0"]
sentence-transformers = ["sentence-transformers>=3.2.1"]
neptune = ["langchain-aws>=0.2.29", "opensearch-py>=3.0.0", "boto3>=1.39.16"]
tracing = ["opentelemetry-api>=1.20.0", "opentelemetry-sdk>=1.20.0"]
dev = [
    "pyright>=1.1.404",
    "groq>=0.2.0",
    "anthropic>=0.49.0",
    "google-genai>=1.8.0",
    "falkordb>=1.1.2,<2.0.0",
    "kuzu>=0.11.3",
    "boto3>=1.39.16",
    "opensearch-py>=3.0.0",
    "langchain-aws>=0.2.29",
    "ipykernel>=6.29.5",
    "jupyterlab>=4.2.4",
    "langgraph>=1.0.10",
    "langchain-anthropic>=0.2.4",
    "langsmith>=0.1.108",
    "langchain-openai>=0.2.6",
    "sentence-transformers>=3.2.1",
    "transformers>=4.45.2",
    "voyageai>=0.2.3",
    "pytest>=8.3.3",
    "pytest-asyncio>=0.24.0",
    "pytest-xdist>=3.6.1",
    "ruff>=0.7.1",
    "opentelemetry-sdk>=1.20.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.pytest.ini_options]
pythonpath = ["."]

[tool.ruff]
line-length = 100

[tool.ruff.lint]
select = [
    # pycodestyle
    "E",
    # Pyflakes
    "F",
    # pyupgrade
    "UP",
    # flake8-bugbear
    "B",
    # flake8-simplify
    "SIM",
    # isort
    "I",
]
ignore = ["E501"]

[tool.ruff.lint.flake8-tidy-imports.banned-api]
# Required by Pydantic on Python < 3.12
"typing.TypedDict".msg = "Use typing_extensions.TypedDict instead."

[tool.ruff.format]
quote-style = "single"
indent-style = "space"
docstring-code-format = true

[tool.pyright]
include = ["graphiti_core"]
pythonVersion = "3.10"
typeCheckingMode = "basic"

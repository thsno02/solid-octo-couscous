# Repository semantic capsule: topoteretes/cognee

- Commit: `c0d18c80e24b7b78918e7642c03f6f128fdd2aee`
- Default branch: `main`
- Description: topoteretes/cognee
- Selected evidence files: 7 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

<div align="center">
  <a href="https://github.com/topoteretes/cognee">
    <img src="assets/cognee-logo.svg" alt="Cognee Logo" width="260">
  </a>

  <br />

  <p>Cognee - The Open-Source AI Memory Platform for Agents</p>

  <p align="center">
  <a href="https://www.youtube.com/watch?v=8hmqS2Y5RVQ&t=13s">Demo</a>
  .
  <a href="https://docs.cognee.ai/">Docs</a>
  .
  <a href="https://cognee.ai">Learn More</a>
  ·
  <a href="https://discord.gg/NQPKmU5CCg">Join Discord</a>
  ·
  <a href="https://www.reddit.com/r/AIMemory/">Join r/AIMemory</a>
  .
  <a href="https://github.com/topoteretes/cognee-community">Community Plugins & Add-ons</a>
  </p>


  <p>
  <a href="https://GitHub.com/topoteretes/cognee/network/"><img src="https://img.shields.io/github/forks/topoteretes/cognee.svg?style=social&amp;label=Fork&amp;maxAge=2592000" alt="GitHub forks"></a>
  <a href="https://github.com/topoteretes/cognee"><img src="https://img.shields.io/github/stars/topoteretes/cognee.svg?style=social&amp;label=Star&amp;maxAge=2592000" alt="GitHub stars"></a>
  <a href="https://GitHub.com/topoteretes/cognee/commit/"><img src="https://badgen.net/github/commits/topoteretes/cognee" alt="GitHub commits"></a>
  <a href="https://github.com/topoteretes/cognee/tags/"><img src="https://badgen.net/github/tag/topoteretes/cognee" alt="GitHub tag"></a>
  <a href="https://pepy.tech/project/cognee"><img src="https://static.pepy.tech/badge/cognee" alt="Downloads"></a>
  <a href="https://github.com/topoteretes/cognee/blob/main/LICENSE"><img src="https://img.shields.io/github/license/topoteretes/cognee?colorA=00C586&amp;colorB=000000" alt="License"></a>
  <a href="https://github.com/topoteretes/cognee/graphs/contributors"><img src="https://img.shields.io/github/contributors/topoteretes/cognee?colorA=00C586&amp;colorB=000000" alt="Contributors"></a>
  <a href="https://github.com/sponsors/topoteretes"><img src="https://img.shields.io/badge/Sponsor-❤️-ff69b4.svg" alt="Sponsor"></a>
  </p>

<p>
  <a href="https://trendshift.io/repositories/13955" target="_blank" style="display:inline-block;">
    <img src="https://trendshift.io/api/badge/repositories/13955" alt="topoteretes%2Fcognee | Trendshift" width="250" height="55" />
  </a>
</p>

  <p>Cognee is the open-source AI memory platform that gives AI agents persistent long-term memory across sessions. Ingest data in any format, build a self-hosted knowledge graph, and let every agent recall, connect, and act with full context</p>

  <p align="center">
  🌐 This README is also available in:<br />
  <!-- Keep these links. Translations will automatically update with the README. -->
  <a href="https://www.readme-i18n.com/topoteretes/cognee?lang=de">Deutsch</a> |
  <a href="https://www.readme-i18n.com/topoteretes/cognee?lang=es">Español</a> |
  <a href="https://www.readme-i18n.com/topoteretes/cognee?lang=fr">Français</a> |
  <a href="https://www.readme-i18n.com/topoteretes/cognee?lang=ja">日本語</a> |
  <a href="README_ko.md">한국어</a> |
  <a href="https://www.readme-i18n.com/topoteretes/cognee?lang=pt">Português</a> |
  <a href="https://www.readme-i18n.com/topoteretes/cognee?lang=ru">Русский</a> |
  <a href="https://www.readme-i18n.com/topoteretes/cognee?lang=zh">中文</a>
  </p>

<p align="center">
  <img src="assets/cognee-demo.gif" alt="Cognee Demo" width="80%" />
</p>
</div>

📄 Read the research paper: [Optimizing the Interface Between Knowledge Graphs and LLMs for Complex Reasoning](https://arxiv.org/abs/2505.24478) — Markovic et al., 2025

## When to use Cognee

- **Build a Company Brain.** Bring documentation, conversations, tickets, code, and agent work into shared memory. Help your team and agents connect a decision to the discussion and implementation behind it. [Explore Company Brain](https://www.cognee.ai/company-brain).
- **Give agents memory across runs.** Retain project context, past decisions, fixes, and learned rules. Distill useful session lessons into durable knowledge that another session can retrieve. [Connect your agent](#connect-your-agent).
- **Ground agents in your domain.** Structure memory around the entities and relationships your application needs, with custom data models and ontologies. [Explore ontologies](https://docs.cognee.ai/guides/ontology-support).

## Choose your starting point

| I want to… | Start here |
| --- | --- |
| See a memory graph without an API key | [Bundled demo](#try-it-without-an-api-key) |
| Build with text, code, and session memory | [Python quickstart](#quickstart) |
| Give an existing agent memory | [Plugins and MCP](#connect-your-agent) |
| Run Cognee on my infrastructure | [Deployment options](#deploy-cognee) |
| Use a managed service | [Cognee Cloud](https://docs.cognee.ai/cognee-cloud/overview) |

## Quickstart

Requires **Python 3.10–3.14**.

You can install Cognee with **pip**, **uv**, or your preferred Python package manager.

```bash
uv pip install cognee
```

### Try it without an API key

```bash
cognee-cli demo
```


### Step 2: Configure the LLM
```python
import os
os.environ["LLM_API_KEY"] = "YOUR OPENAI_API_KEY"
```
Alternatively, create a `.env` file using our [template](https://github.com/topoteretes/cognee/blob/main/.env.template).

The default uses OpenAI for language models and embeddings. Processing and generated answers make provider calls. See [installation](https://docs.cognee.ai/getting-started/installation), [other providers](https://docs.cognee.ai/setup-configuration/llm-providers), or [local Ollama models](https://docs.cognee.ai/guides/local-ollama) for other setups.


```python
import cognee
import asyncio


async def main():
    # Store permanently in the knowledge graph (runs add + cognify + improve)
    await cognee.remember("Cognee turns documents into AI memory.")

    # Store in session memory (fast cache, syncs to graph in background)
    await cognee.remember("User prefers detailed explanations.", session_id="chat_1")

    # Query with auto-routing (picks best search strategy automatically)
    results = await cognee.recall("What does Cognee do?")
    for result in results:
        print(result)

    # Query session memory first, fall through to graph if needed
    results = await cognee.recall("What does the user prefer?", session_id="chat_1")
    for result in results:
        print(result)

    # Delete when done
    await cognee.forget(dataset="main_dataset")


if __name__ == '__main__':
    asyncio.run(main())

```


## How Cognee works

Cognee builds connected memory from different sources. Text becomes entities, relationships, and searchable chunks; code becomes a graph of symbols and dependencies. Session distillation curates accepted lessons into permanent memory.

<p align="center">
  <img src="assets/remember.svg" alt="Text, code, and session guidance follow their ingestion paths into persistent Cognee memory" width="100%">
</p>

At query time, retrieval selects relevant graph, vector, or code context. Your application can inspect the retrieved evidence and use it to answer a question or continue an agent task.

<p align="center">
  <img src="assets/recall.svg" alt="Recall retrieves a document fact, a code symbol, and a learned release rule for an agent's next task" width="100%">
</p>

| Operation | What it does | Learn more |
| --- | --- | --- |
| `remember` | Store content or code in permanent memory, or in a session when a session ID is supplied. | [Store memory](https://docs.cognee.ai/core-concepts/main-operations/remember) |
| `recall` | Retrieve context and answers, using automatic routing or a chosen search strategy. | [Query memory](https://docs.cognee.ai/core-concepts/main-operations/recall) |
| `improve` | Enrich memory, apply feedback, and bridge session knowledge into the graph. | [Improve memory](https://docs.cognee.ai/core-concepts/main-operations/improve) |
| `forget` | Remove a specific item or dataset. | [Delete memory](https://docs.cognee.ai/core-concepts/main-operations/forget) |

Explore the [architecture](https://docs.cognee.ai/core-concepts/architecture) and [session lifecycle](https://docs.cognee.ai/core-concepts/sessions-and-caching).

## Connect your agent

Install the Claude Code plugin:

```bash
claude plugin marketplace add topoteretes/cognee-integrations
claude plugin install cognee-memory@cognee
```

or Codex plugin

Make sure to enable hooks:
```bash
# ~/.codex/config.toml
[features]
hooks = true
```

```bash
codex plugin marketplace add topoteretes/cognee-integrations --ref main
codex plugin add cognee@cognee
```

Follow the [plugin setup guide](https://github.com/topoteretes/cognee-integrations/tree/main/integrations/claude-code) to configure local or remote memory.

| Interface | Start here |
| --- | --- |
| Claude Code memory plugin | [Install and configure the plugin](https://github.com/topoteretes/cognee-integrations/tree/main/integrations/claude-code) |
| OpenClaw memory plugin | [Install `@cognee/cognee-openclaw`](https://www.npmjs.com/package/@cognee/cognee-openclaw) |
| Cursor, Cline, and other MCP clients | [Cognee MCP guide](https://docs.cognee.ai/cognee-mcp/mcp-overview) and [server README](cognee-mcp/README.md) |
| Python applications | [Python API reference](https://docs.cognee.ai/python-api) |
| TypeScript applications | [TypeScript SDK](https://docs.cognee.ai/typescript/getting-started) |
| Rust applications | [Cognee-RS](https://github.com/topoteretes/cognee-rs) |
| Applications using HTTP | [REST API reference](https://docs.cognee.ai/api-reference/introduction) |

Browse the [integrations repository](https://github.com/topoteretes/cognee-integrations) for agent frameworks, plugins, and source connectors. Each guide describes its setup and memory capture behavior.

To inspect a local installation in the UI:

```bash
cognee-cli -ui
```

The UI launcher requires Node.js/npm; Docker is needed for its MCP service. See [local UI setup](https://docs.cognee.ai/cognee-cli/overview).

## Explore examples

- [Build a small Company Brain from text, code, and session lessons](examples/demos/company_brain_demo.py).
- [Import memory from Mem0, Letta, Zep, or Graphiti](https://docs.cognee.ai/examples/migrate-memory-systems) using the COGX exchange format.
- [Run with local Ollama models](https://docs.cognee.ai/guides/local-ollama), including a local embedding model.
- [Visualize your knowledge graph](https://docs.cognee.ai/guides/graph-visualization) and inspect its connections.
- [Browse runnable examples](examples/README.md) for ingestion, sessions, feedback, and custom pipelines.
- [Run the prebuilt API with Docker Compose](docs/minimal-docker-compose.md) or use the [deployment templates](distributed/deploy/README.md).
- [Explore community adapters and add-ons](https://github.com/topoteretes/cognee-community).

<a id="run-with-docker"></a>

## Deploy Cognee


## `AGENTS.md`

## Repository Guidelines

This document summarizes how to work with the cognee repository: how it’s organized, how to build, test, lint, and contribute. It mirrors our actual tooling and CI while providing quick commands for local development.

## Project Structure & Module Organization

- `cognee/`: Core Python library and API.
  - `api/`: FastAPI application and versioned routers (add, cognify, memify, search, delete, users, datasets, responses, visualize, settings, sync, update, checks).
  - `cli/`: CLI entry points and subcommands invoked via `cognee` / `cognee-cli`.
  - `infrastructure/`: Databases, LLM providers, embeddings, loaders, and storage adapters.
  - `modules/`: Domain logic (graph, retrieval, ontology, users, processing, observability, etc.).
  - `tasks/`: Reusable tasks (e.g., code graph, web scraping, storage). Extend with new tasks here.
  - `eval_framework/`: Evaluation utilities and adapters.
  - `shared/`: Cross-cutting helpers (logging, settings, utils).
  - `tests/`: Unit, integration, CLI, and end-to-end tests organized by feature.
  - `__main__.py`: Entrypoint to route to CLI.
- `cognee-mcp/`: Model Context Protocol server exposing cognee as MCP tools (SSE/HTTP/stdio). Contains its own README and Dockerfile.
- `cognee-frontend/`: Next.js UI for local development and demos.
- `distributed/deploy/`: One-click deployment templates (Modal, Fly.io, Railway, Render, Daytona).
- `examples/`: Example scripts demonstrating the public APIs and features (graph, code graph, multimodal, permissions, etc.).
- `notebooks/`: Jupyter notebooks for demos and tutorials.
- `alembic/`: Database migrations for relational backends.

Notes:
- Co-locate feature-specific helpers under their respective package (`modules/`, `infrastructure/`, or `tasks/`).
- Extend the system by adding new tasks, loaders, or retrievers rather than modifying core pipeline mechanisms.

## Build, Test, and Development Commands

Python (root) – requires Python >= 3.10 and < 3.14. We recommend `uv` for speed and reproducibility.

- Create/refresh env and install dev deps:
```bash
uv sync --dev --all-extras --reinstall
```

- Run the CLI (examples):
```bash
uv run cognee-cli add "Cognee turns documents into AI memory."
uv run cognee-cli cognify
uv run cognee-cli search "What does cognee do?"
uv run cognee-cli -ui   # Launches UI, backend API, and MCP server together
```

- Start the FastAPI server directly:
```bash
uv run python -m cognee.api.client
```

- Run tests (CI mirrors these commands):
```bash
uv run pytest cognee/tests/unit/ -v
uv run pytest cognee/tests/integration/ -v
```

- Lint and format (ruff):
```bash
uv run ruff check .
uv run ruff format .
```

- Optional static type checks (ty):
```bash
uv run ty check .
```

MCP Server (`cognee-mcp/`):

- Install and run locally:
```bash
cd cognee-mcp
uv sync --dev --all-extras --reinstall
uv run python src/server.py               # stdio (default)
uv run python src/server.py --transport sse
uv run python src/server.py --transport http --host 127.0.0.1 --port 8000 --path /mcp
```

- API Mode (connect to a running Cognee API):
```bash
uv run python src/server.py --transport sse --api-url http://localhost:8000 --api-token YOUR_TOKEN
```

- Docker quickstart (examples): see `cognee-mcp/README.md` for full details
```bash
docker run -e TRANSPORT_MODE=http --env-file ./.env -p 8000:8000 --rm -it cognee/cognee-mcp:main
```

Frontend (`cognee-frontend/`):
```bash
cd cognee-frontend
npm install
npm run dev     # Next.js dev server
npm run lint    # ESLint
npm run build && npm start
```

## Runtime Flags Worth Knowing

Three env flags trade memory features for speed; know what each disables before flipping it:

- `CACHING` (default `true`) — master switch for the session-memory layer. When `false`,
  `remember(session_id=...)` raises, `recall()` loses session history, `agent_memory`
  session options error out, and `AUTO_FEEDBACK` is implicitly disabled. Never benchmark
  cognee with this off — that measures cognee with its memory layer removed.
- `AUTO_FEEDBACK` (default `true`) — one structured-output LLM call per answered turn
  that detects implicit feedback and lets memory self-tune. Disable for low-latency,
  lower-cost reads; session store/recall itself keeps working.
- `DATASET_QUEUE_ENABLED` (default `true`) — per-process cap on concurrent datasets
  (`DATASET_QUEUE_MAX_CONCURRENT`, default 6); also tears down subprocess DB engines on
  scope exit and pins in-use engines against cache eviction. Disable only for
  single-dataset scripts — under parallel multi-dataset load, turning it off risks
  file-lock leaks and unbounded embedded engines.

## Multi-Tenancy Support by Backend

With `ENABLE_BACKEND_ACCESS_CONTROL=true` (the default) each user+dataset gets isolated
graph and vector databases. Backend support (source of truth:
`cognee/infrastructure/databases/dataset_database_handler/supported_dataset_database_handlers.py`):

- Graph — supported: Ladybug/Kuzu (default), Neo4j (needs multi-database, i.e.
  Enterprise/Aura), Postgres (demo), Turso. Unsupported: Neptune, ladybug-remote.
- Vector — supported: LanceDB (default), PGVector, Turso. Unsupported: Neptune
  Analytics and community adapters (unless they register a handler via
  `use_dataset_database_handler()`).
- Relational (SQLite/Postgres) is always a single shared DB (users, ACLs, registry).

Both graph and vector must be supported, or cognee raises `EnvironmentError` — an
unsupported backend with the flag on is a hard error, not a fallback to shared DBs;
set `ENABLE_BACKEND_ACCESS_CONTROL=false` to run such backends single-tenant.

## Coding Style & Naming Conventions

Python:
- 4-space indentation, modules and functions in `snake_case`, classes in `PascalCase`.
- Public APIs should be type-annotated where practical. Make sure type defined in API signature will be properly displayed in Swagger UI docs. For example this definition: content_type: Optional[str] = Form(default=None) maps to "string" as the default in Swagger docs for content_type, but it should be None/null instead.
- Use `ruff format` before committing; `ruff check` enforces import hygiene and style (line-length 100 configured in `pyproject.toml`).
- Prefer explicit, structured error handling. Use shared logging utilities in `cognee.shared.logging_utils`.

MCP server and Frontend:
- Follow the local `README.md` and ESLint/TypeScript configuration in `cognee-frontend/`.

## Testing Guidelines

- Place Python tests under `cognee/tests/`.
  - Unit tests: `cognee/tests/unit/`
  - Integration tests: `cognee/tests/integration/`
  - CLI tests: `cognee/tests/cli_tests/`
- Name test files `test_*.py`. Use `pytest.mark.asyncio` for async tests.
- Avoid external state; rely on test fixtures and the CI-provided env vars when LLM/embedding providers are required. See CI workflows under `.github/workflows/` for expected environment variables.
- When adding public APIs, provide/update targeted examples under `examples/python/`.

## Commit & Pull Request Guidelines

- Use clear, imperative subjects (≤ 72 chars) and conventional commit styling in PR titles. Our CI validates semantic PR titles (see `.github/workflows/pr_lint`). Examples:
  - `feat(graph): add temporal edge weighting`
  - `fix(api): handle missing auth cookie`
  - `docs: update installation instructions`
- Reference related issues/discussions in the PR body and provide brief context.
- PRs should describe scope, list local test commands run, and mention any impacts on MCP server or UI if applicable.
- Sign commits and affirm the DCO (see `CONTRIBUTING.md`).

## CI Mirrors Local Commands

Our GitHub Actions run the same ruff checks and pytest suites shown above (`.github/workflows/basic_tests.yml` and related workflows). Use the commands in this document locally to minimize CI surprises.

## `CLAUDE.md`

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Cognee is an open-source AI memory platform that transforms raw data into persistent knowledge graphs for AI agents. It replaces traditional RAG (Retrieval-Augmented Generation) with an ECL (Extract, Cognify, Load) pipeline combining vector search, graph databases, and LLM-powered entity extraction.

**Requirements**: Python 3.10 - 3.14

## Development Commands

### Setup
```bash
# Create virtual environment (recommended: uv)
uv venv && source .venv/bin/activate

# Install with pip or uv
uv pip install -e .

# Install with dev dependencies
uv pip install -e ".[dev]"

# Install with specific extras
uv pip install -e ".[postgres,neo4j,docs]"

# Set up pre-commit hooks
pre-commit install
```

### Available Installation Extras
- **postgres** / **postgres-binary** - PostgreSQL + PGVector support (also enables the Postgres session-cache backend, `CACHE_BACKEND=postgres`)
- **neo4j** - Neo4j graph database support
- **neptune** - AWS Neptune support
- **turso** - Turso vector database support
- **docs** - Document processing (unstructured library)
- **scraping** - Web scraping (Tavily, BeautifulSoup, Playwright; Keenable needs no extra — it uses the built-in httpx)
- **langchain** - LangChain integration
- **llama-index** - LlamaIndex integration
- **anthropic** - Anthropic Claude models
- **ollama** - Ollama local models
- **mistral** - Mistral AI models
- **groq** - Groq API support
- **llama-cpp** - Llama.cpp local inference
- **huggingface** - HuggingFace transformers
- **aws** - S3 storage backend
- **redis** - Redis caching
- **graphiti** - Graphiti-core integration
- **baml** - BAML structured output
- **dlt** - Data load tool (dlt) integration
- **docling** - Docling document processing, slim profile without torch (office/HTML/email/markdown/LaTeX formats)
- **docling-full** - Full docling install with torch-based ML models (adds PDF/image conversion through docling; conflicts with **codegraph** due to tree-sitter pins)
- **codegraph** - Code graph extraction
- **evals** - Evaluation tools
- **deepeval** - DeepEval testing framework
- **posthog** - PostHog analytics
- **tracing** - OpenTelemetry tracing
- **dev** - All development tools (pytest, ty, ruff, etc.)
- **debug** - Debugpy for debugging

### Testing
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=cognee --cov-report=html

# Run specific test file
pytest cognee/tests/test_custom_model.py

# Run specific test function
pytest cognee/tests/test_custom_model.py::test_function_name

# Run async tests
pytest -v cognee/tests/integration/

# Run unit tests only
pytest cognee/tests/unit/

# Run integration tests only
pytest cognee/tests/integration/
```

### Code Quality
```bash
# Run ruff linter
ruff check .

# Run ruff formatter
ruff format .

# Run both linting and formatting (pre-commit)
pre-commit run --all-files

# Type checking with ty
ty check .
```

### Running Cognee
```bash
# Using Python SDK
uv run python examples/guides/simple_cognee_example.py

# Using CLI (memory API — the primary surface)
cognee-cli remember "Your text here"   # also accepts file paths / URLs
cognee-cli recall "Your question"
cognee-cli improve -d my_project       # enrich/index the graph
cognee-cli forget --all                # NOTE: no confirmation prompt

# Low level operations (still ship; what the memory commands call underneath)
cognee-cli add "Your text here" && cognee-cli cognify
cognee-cli search "Your query"
cognee-cli delete --all                # prompts before deleting

# Launch full stack with UI
cognee-cli -ui
```

## Architecture Overview

### Core Workflow: remember → recall (+ improve / forget)

As of cognee 1.x the memory API is the primary surface. All functions are async.

1. **remember()** - Store data in memory. Without `session_id` it runs `add()` + `cognify()` and then `improve()` (`self_improvement=True` by default); with `session_id` it writes to the fast session cache and bridges into the graph in the background.
2. **recall()** - Query memory. Auto-routes to a search strategy unless `query_type` is passed (`auto_route=False` falls back to `HYBRID_COMPLETION`). A `session_id` reads the session cache first and falls through to the graph.
3. **improve()** - Enrich/index the graph: triplet embeddings, feedback weights, and (with `session_ids`) bridging session Q&A and distilled learnings into the permanent graph.
4. **forget()** - Unified deletion (`data_id` / `dataset` / `dataset_id` / `everything=True`, plus `memory_only=True` to drop graph+vectors but keep raw files).

#### Low level operations: add → cognify → search/memify

These still ship and are what the memory API calls underneath. Reach for them to drive one stage in isolation (custom pipeline tasks, stage-level debugging), not for ordinary ingestion or retrieval.

1. **add()** - Ingest data (files, URLs, text) into datasets
2. **cognify()** - Extract entities/relationships and build knowledge graph
3. **search()** - Query knowledge using various retrieval strategies
4. **memify()** - Enrich graph with additional context and rules

Note: Using Low level operations over core is useful in the following contexts.
1) functional_relationships= is completely unreachable from remember(). So Only cognify can constrain single-target relationships.
2) remember() hardcodes datasets_arg = [dataset_name]: always exactly one. Use cognify for this: cognify(datasets=["a","b","c"]) or datasets=None (every dataset the user owns.)
3) remember() always runs add() first. To rebuild a graph over data already in the DB — after forget(memory_only=True), or with a new graph_model/ontology, cognify() is the only path.
4) add() is like a staging area for cognify(). But remember automatically adds every time.
5) search() packs skills/tools/max_iter/code_query into retriever_specific_config for you. Using recall() you hand-build that dict yourself.
6) prune.prune_system(metadata=True) drops the relational DB (users, tenants, ACLs, the dataset_database registry, pipeline runs, search history.) forget() touches none of that. Full test teardown is prune's job.
Improve & Memify are virtually the same, though. So no reason not to use improve.

`cognee.delete` is deprecated (since 0.3.9, in favor of `datasets.delete_data`); `forget()` is the v1 replacement that unifies the old delete/prune/empty_dataset paths.

#### recall() vs search()

`recall()` wraps `search()` — its graph path calls the same authorized search — and adds three things: rule-based query routing when `query_type` is omitted (regex scoring, no LLM call, so auto-routing is free), session memory as a searchable source (`scope` = `graph` / `session` / `trace` / `session_context`; with a bare `session_id` a session hit short-circuits the graph search), and normalized results tagged with a `_source` key. Use `recall()` for ordinary retrieval. Drop to `search()` when you need the agentic extras as first-class parameters (`skills`, `tools`, `max_iter`, `code_query`, `node_type`), raw `SearchResult` objects instead of tagged entries, or a pinned `query_type` with no router in the path. Note `search(session_id=...)` only adds session history to the retrieval context — it never searches the session cache as a source; that is `recall()`-only. Full guide: `docs/recall-vs-search.md`.

### Key Architectural Patterns

#### 1. Pipeline-Based Processing
All data flows through task-based pipelines (`cognee/modules/pipelines/`). Tasks are composable units that can run sequentially or in parallel. Example pipeline tasks: `classify_documents`, `extract_graph_from_data`, `add_data_points`.

#### 2. Interface-Based Database Adapters
Multiple backends are supported through adapter interfaces:
- **Graph**: Ladybug (default), Neo4j, Neptune, Postgres (demo) via `GraphDBInterface`
- **Vector**: LanceDB (default), PGVector, Neptune Analytics, Turso via `VectorDBInterface` (ChromaDB/Qdrant/Weaviate/Milvus via community adapters)
- **Relational**: SQLite (default), PostgreSQL

Key files:
- `cognee/infrastructure/databases/graph/graph_db_interface.py`
- `cognee/infrastructure/databases/vector/vector_db_interface.py`

#### 3. Multi-Tenant Access Control
User → Dataset → Data hierarchy with permission-based filtering. Enable with `ENABLE_BACKEND_ACCESS_CONTROL=True`. Each user+dataset combination can have isolated graph/vector databases — but only on backends with a dataset-database handler.

**Multi-tenancy support matrix** (source of truth: `cognee/infrastructure/databases/dataset_database_handler/supported_dataset_database_handlers.py`):

| Layer | Backend | Isolated per user+dataset? | Notes |
|---|---|---|---|
| Graph | Ladybug/Kuzu (default) | ✅ | embedded, one database per dataset |
| Graph | Neo4j | ✅ | one Neo4j database per dataset inside the DBMS — requires an edition with multi-database support (Enterprise/Aura). A second handler, `neo4j_aura_dev`, provisions a whole Aura instance per dataset; dev/PoC only, not production-ready |
| Graph | Postgres | ✅ | graph-on-Postgres is itself a demo feature (see warning above) |
| Graph | Turso | ✅ | |
| Graph | Neptune, ladybug-remote | ❌ | requires `ENABLE_BACKEND_ACCESS_CONTROL=false` |
| Vector | LanceDB (default) | ✅ | |
| Vector | PGVector | ✅ | |
| Vector | Turso | ✅ | |
| Vector | Neptune Analytics | ❌ | requires `ENABLE_BACKEND_ACCESS_CONTROL=false` |
| Vector | Community adapters (ChromaDB, Qdrant, …) | ❌ | unless the adapter registers a handler via `use_dataset_database_handler()` |
| Relational | SQLite / Postgres | n/a — always shared | one relational DB holds users, ACLs, and the dataset-database registry; it is never isolated per dataset |

How it works:
- The handler is selected automatically from the configured provider (`GraphConfig.fill_derived` and the vector-config equivalent) — you never set it by hand for in-tree backends.
- **Both** the graph and vector backends must support isolation. If either doesn't, cognee raises an `EnvironmentError` naming the unsupported handler — with the flag on (its default), an unsupported backend is a hard error, not a silent fallback to shared databases. The fix is switching backends or setting `ENABLE_BACKEND_ACCESS_CONTROL=false`.
- New backends gain multi-tenancy by registering a `DatasetDatabaseHandlerInterface` implementation in the registry (or at runtime via `use_dataset_database_handler()`).

### Layer Structure

```
API Layer (cognee/api/v1/)
    ↓
Memory API (remember, recall, improve, forget)
    ↓
Low level operations (add, cognify, search, memify)
    ↓
Pipeline Orchestrator (cognee/modules/pipelines/)
    ↓
Task Execution Layer (cognee/tasks/)
    ↓
Domain Modules (graph, retrieval, ingestion, etc.)
    ↓
Infrastructure Adapters (LLM, databases)
    ↓
External Services (OpenAI, Ladybug, LanceDB, etc.)
```

### Critical Data Flow Paths

#### REMEMBER / RECALL: Memory API
NOTE: This is how the memory API flow works under the hood; it's read as a flow of data. So remember calls add(), cognify(), and improve().
`remember(data)` → `add()` → `cognify()` → `improve()` (when `self_improvement=True`)
`remember(data, session_id=...)` → session cache → background `improve()` bridge
`recall(query)` → auto-route to a `SearchType` → `search()` → permission filter → results

## `CONTRIBUTING.md`

> [!IMPORTANT]
> **Note for contributors:** When branching out, create a new branch from the `dev` branch.

# 🎉 Welcome to **cognee**!

We're excited that you're interested in contributing to our project!
We want to ensure that every user and contributor feels welcome, included and supported to participate in cognee community.
This guide will help you get started and ensure your contributions can be efficiently integrated into the project.

## 🌟 Quick Links

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Discord Community](https://discord.gg/bcy8xFAtfd)
- [Issue Tracker](https://github.com/topoteretes/cognee/issues)
- [Cognee Docs](https://docs.cognee.ai)

## 1. 🚀 Ways to Contribute

You can contribute to **cognee** in many ways:

- 📝 Submitting bug reports or feature requests
- 💡 Improving documentation
- 🔍 Reviewing pull requests
- 🛠️ Contributing code or tests
- 🌐 Helping other users
- 📇 Adding an entry to the [Integrations Hub or Use-Case Gallery](docs/contributing/add-catalog-entry.md)

## 📫 Get in Touch

There are several ways to connect with the **cognee** team and community:

### GitHub Collaboration
- [Open an issue](https://github.com/topoteretes/cognee/issues) for bug reports, feature requests, or discussions
- Submit pull requests to contribute code or documentation
- Join ongoing discussions in existing issues and PRs

### Community Channels
- Join our [Discord community](https://discord.gg/bcy8xFAtfd) for real-time discussions
- Participate in community events and discussions
- Get help from other community members

### Direct Contact
- Email: vasilije@cognee.ai
- For business inquiries or sensitive matters, please reach out via email
- For general questions, prefer public channels like GitHub issues or Discord

We aim to respond to all communications within 2 business days. For faster responses, consider using our Discord channel where the whole community can help!

## Issue Labels

To help you find the most appropriate issues to work on, we use the following labels:

- `good first issue` - Perfect for newcomers to the project
- `bug` - Something isn't working as expected
- `documentation` - Improvements or additions to documentation
- `enhancement` - New features or improvements
- `help wanted` - Extra attention or assistance needed
- `question` - Further information is requested
- `wontfix` - This will not be worked on

Looking for a place to start? Try filtering for [good first issues](https://github.com/topoteretes/cognee/labels/good%20first%20issue)!


## 2. 🛠️ Development Setup

### Required tools
* [Python](https://www.python.org/downloads/)
* [uv](https://docs.astral.sh/uv/getting-started/installation/)
* pre-commit: `uv run pip install pre-commit && pre-commit install`

### Fork and Clone

1. Fork the [**cognee**](https://github.com/topoteretes/cognee) repository
2. Clone your fork:
```shell
git clone https://github.com/<your-github-username>/cognee.git
cd cognee
```
In case you are working on Vector and Graph Adapters
1. Fork the [**cognee-community**](https://github.com/topoteretes/cognee-community) repository
2. Clone your fork:
```shell
git clone https://github.com/<your-github-username>/cognee-community.git
cd cognee-community
```

### Create a Branch

Create a new branch for your work:
```shell
git checkout -b feature/your-feature-name
```

## 3. 🎯 Making Changes

1. **Code Style**: Follow the project's coding standards
2. **Documentation**: Update relevant documentation
3. **Tests**: Add tests for new features
4. **Commits**: Write clear commit messages

### Running Tests

Copy `.env.template` to `.env` and provide your OPENAI_API_KEY as LLM_API_KEY

```shell
uv run python cognee/tests/test_library.py
```

### Minimal Docker Compose Try-out

If you want a quick local smoke test before changing code, bring up the default API server with Docker Compose:

```shell
cp .env.template .env
# edit .env and set LLM_API_KEY
docker compose up
```

Useful optional profiles:

```shell
docker compose --profile ui up        # frontend on http://localhost:3000
docker compose --profile mcp up       # MCP server on http://localhost:8001
docker compose --profile postgres up  # Postgres/PGVector
docker compose --profile neo4j up     # Neo4j
```

See the [Run with Docker](README.md#run-with-docker) section in the README for more details.

### Running Simple Example

Copy `.env.template` to `.env` and provide your OPENAI_API_KEY as LLM_API_KEY

Make sure to run ```shell uv sync ``` in the root cloned folder or set up a virtual environment to run cognee

```shell
uv run python examples/guides/simple_cognee_example.py
```

## 4. 📤 Submitting Changes

1. Make sure that `pre-commit` and hooks are installed. See `Required tools` section for more information. Try executing `pre-commit run` if you are not sure.
3. Push your changes:
```shell
git add .
git commit -s -m "Description of your changes"
git push origin feature/your-feature-name
```

2. Create a Pull Request:
   - Go to the [**cognee** repository](https://github.com/topoteretes/cognee) or [cognee community repository](https://github.com/topoteretes/cognee-community)
   - Click "Compare & Pull Request" and open a PR against dev branch
   - Fill in the PR template with details about your changes
   - You MUST provide screenshots of unit and integration tests passing on your machine. We can't merge PRs otherwise

### Changelog Entries

If maintainers ask for a changelog entry, add it under the `Unreleased` section of `CHANGELOG.md`.

- Use `Added` for new capabilities
- Use `Changed` for behavior or documentation updates
- Use `Fixed` for bug fixes

Example entry:

```markdown
## Unreleased

### Fixed
- Clarify the minimal Docker Compose setup for first-time contributors.
```

> **Reviewers are auto-routed.** Cognee uses a [`CODEOWNERS`](.github/CODEOWNERS)
> file to request reviews automatically based on the directories your PR touches.
> No manual ping required — the right person will get notified when you open the PR.

## 5. 📜 Developer Certificate of Origin (DCO)

All contributions must be signed-off to indicate agreement with our DCO:

```shell
git config alias.cos "commit -s"  # Create alias for signed commits
```

When your PR is ready, please include:
> "I affirm that all code in every commit of this pull request conforms to the terms of the Topoteretes Developer Certificate of Origin"

## 6. 🤝 Community Guidelines

- Be respectful and inclusive
- Help others learn and grow
- Follow our [Code of Conduct](CODE_OF_CONDUCT.md)
- Provide constructive feedback
- Ask questions when unsure

## 7. 📫 Getting Help

- Open an [issue](https://github.com/topoteretes/cognee/issues)
- Join our Discord community
- Check existing documentation

Thank you for contributing to **cognee**! 🌟

## `Dockerfile`

# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS uv

# Install the project into `/app`
WORKDIR /app

# Enable bytecode compilation: without it the venv ships no .pyc files, so
# every container cold start recompiles the entire dependency tree from
# source (measured on cognee-saas-pod: ~8s of a ~13s import, halving startup).
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

# Set build argument
ARG DEBUG

# Additional optional-dependency groups to install, separated by spaces.
# Example: docker build --build-arg COGNEE_EXTRAS="aws langchain" .
# Keep this applied to both sync steps: the second exact sync would otherwise
# remove extras installed only in the dependency-cache layer.
ARG COGNEE_EXTRAS=""

# Set environment variable based on the build argument
ENV DEBUG=${DEBUG}

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    git \
    curl \
    cmake \
    clang \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy pyproject.toml and lockfile first for better caching
COPY README.md pyproject.toml uv.lock entrypoint.sh ./

# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
    set -eu; \
    set -f; \
    set --; \
    for extra in ${COGNEE_EXTRAS}; do \
        set -- "$@" --extra "$extra"; \
    done; \
    uv sync "$@" --extra fastembed --extra debug --extra api --extra postgres --extra neo4j --extra llama-index --extra aws --extra dlt --extra ollama --extra mistral --extra groq --extra anthropic --frozen --no-install-project --no-dev --no-editable

# Then, add the rest of the project source code and install it
# Installing separately from its dependencies allows optimal layer caching
COPY ./cognee /app/cognee
COPY ./cognee_db_workers /app/cognee_db_workers
# Compatibility shim that re-exports ladybug under the legacy `kuzu`
# module name. Listed in [tool.hatch.build.targets.wheel] packages, and
# imported at module load by alembic/versions/b9274c27a25a_kuzu_11_migration.py.
COPY ./kuzu /app/kuzu
RUN --mount=type=cache,target=/root/.cache/uv \
    set -eu; \
    set -f; \
    set --; \
    for extra in ${COGNEE_EXTRAS}; do \
        set -- "$@" --extra "$extra"; \
    done; \
    uv sync "$@" --extra fastembed --extra debug --extra aws --extra api --extra postgres --extra neo4j --extra llama-index --extra dlt --extra ollama --extra mistral --extra groq --extra anthropic --frozen --no-dev --no-editable

FROM python:3.12-slim-bookworm

RUN apt-get update && apt-get install -y \
    libpq5 \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Run as the same non-root user as the cognee-mcp image (uid/gid 1000) so both
# containers can share the storage volumes without ownership conflicts (a
# root-created database directory is unwritable for the uid-1000 MCP server).
# Created before the COPY so ownership is set in that single layer — a
# separate `chown -R /app` would copy the whole tree up into a second layer.
# /cognee-storage is baked into the image cognee-owned so a fresh named
# volume mounted there initializes with the right ownership.
# ``chown cognee /app`` (the directory inode only): WORKDIR created /app as
# root, and ``COPY --chown`` sets ownership on the copied content, not the
# pre-existing target dir — without this the non-root user cannot create
# ``$HOME/.lbdb`` and the build-time extension pre-install silently fails.
RUN groupadd --system --gid 1000 cognee \
    && useradd --system --uid 1000 --gid cognee --no-create-home --shell /usr/sbin/nologin cognee \
    && mkdir -p /cognee-storage/system /cognee-storage/data \
    && chown -R cognee:cognee /cognee-storage \
    && chown cognee:cognee /app

COPY --from=uv --chown=cognee:cognee /app /app

# Strip Windows carriage returns (fixes "no such file" on Windows Docker)
RUN sed -i 's/\r$//' /app/entrypoint.sh && chmod +x /app/entrypoint.sh

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

ENV PYTHONPATH=/app
# ENV LOG_LEVEL=ERROR
ENV PYTHONUNBUFFERED=1
# Writable HOME for the non-root user (~/.cognee logs, tool caches).
ENV HOME=/app
# Default storage OUTSIDE the source tree: the ./cognee bind mount exists for
# dev reload and must not double as the persistence location (host-uid
# sensitive, pollutes the checkout, and was shared with the MCP container by
# accident rather than by design). docker-compose mounts named volumes here.
ENV SYSTEM_ROOT_DIRECTORY=/cognee-storage/system
ENV DATA_ROOT_DIRECTORY=/cognee-storage/data

USER cognee

# Pre-install Kuzu/Ladybug's JSON extension at build time (network is available
# here) so it is baked into the image — same mechanism as the cognee-mcp
# image. As root the server used to INSTALL it at runtime into /root/.lbdb on
# every boot; as the non-root user that runtime install races between graph
# workers and fails ("Directory ... cannot be created"). Best-effort: a failed
# download must not break the image build.
RUN python -c "from cognee_db_workers._kuzu_helpers import install_json_extension_local; install_json_extension_local(buffer_pool_size=268435456)" \
    || echo "WARNING: JSON extension pre-install skipped (no network at build time); it will be installed on first run if the container has network access."

ENTRYPOINT ["/app/entrypoint.sh"]

HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

## `SECURITY.md`

# Reporting Security Issues
The Cognee team takes security issues seriously. We appreciate your efforts to responsibly disclose your findings, and will make every effort to acknowledge your contributions.

To report a security issue, email [security@cognee.ai](mailto:security@cognee.ai) and include the word "SECURITY" in the subject line.

We'll endeavor to respond quickly, and will keep you updated throughout the process.

## `pyproject.toml`

[project]
name = "cognee"

version = "1.5.4"
description = "Cognee - is a library for enriching LLM context with a semantic layer for better understanding and reasoning."
authors = [
    { name = "Vasilije Markovic" },
    { name = "Boris Arzentar" },
]
requires-python = ">=3.10,<3.15"
readme = "README.md"
license = "Apache-2.0"
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Topic :: Software Development :: Libraries",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Microsoft :: Windows",
]
dependencies = [
    "openai>=1.80.1",
    "python-dotenv>=1.0.1,<2.0.0",
    "pydantic>=2.10.5",
    # GHSA-4xgf-cpjx-pc3j: 2.12.0–2.14.1 vulnerable, fixed in 2.14.2. Exclude the
    # vulnerable range rather than capping, so the patched 2.14.2+ is adopted once
    # it clears the `exclude-newer` window (it was <2 days old at time of writing).
    "pydantic-settings>=2.2.1,!=2.12.*,!=2.13.*,!=2.14.0,!=2.14.1,<3",
    "typing_extensions>=4.12.2,<5.0.0",
    "numpy>=1.26.4, <=4.0.0",
    "sqlalchemy>=2.0.39,<3.0.0",
    "aiosqlite>=0.20.0,<1.0.0",
    "filelock>=3.12.0,<4.0.0",  # cross-process migration lock for SQLite (Linux/macOS/Windows)
    "tiktoken>=0.8.0,<1.0.0",
    # <1.97.0: 1.97.0 fails to build litellm.types.utils.Message on Python 3.10 (unresolved
    # forward ref) and 1.98.0+ import typing.NotRequired (3.11+). See BerriAI/litellm#38202.
    "litellm>=1.83.7,<1.97.0",
    "instructor>=1.9.1,<1.15.3",
    "filetype>=1.2.0,<2.0.0",
    "aiohttp>=3.13.5,<4.0.0",
    "aiofiles>=23.2.1",
    # AES-256-GCM encryption for stored OAuth integration credentials
    # (cognee/modules/integrations/crypto.py) — unconditionally imported via
    # client.py's Slack router registration, so this is a core dependency,
    # not an integration-specific extra.
    # <51 (not <50): downstream consumers pin cryptography>=50.0.0 for
    # PYSEC-2026-3552/3553/3554; our usage (Fernet, AESGCM) is stable across 50.x.
    "cryptography>=43.0.0,<51",
    "rdflib>=7.1.4,<7.2.0",
    "pypdf>=6.6.2,<7.0.0",
    "jinja2>=3.1.3,<4",
    "lancedb>=0.24.3,<1.0.0",  # 0.24.2 bundles lance 0.32.0 whose list-column decoder panics on tables with deletion vectors
    "nbformat>=5.7.0,<6.0.0",
    "alembic>=1.13.3,<2",
    "limits>=4.4.1,<6",
    "fastapi>=0.116.2,<1.0.0",
    "starlette>=0.48",
    "python-multipart>=0.0.22,<1.0.0",
    "fastapi-users[sqlalchemy]>=15.0.2",
    "structlog>=25.2.0,<26",
    "pympler>=1.1,<2.0.0",
    "pylance>=0.22.0,<=0.36.0",
    # ladybug 0.18.x+ publishes only macosx_15_0 wheels (its sdist needs C++20
    # std::atomic_ref, which Apple Clang's libc++ on macOS <= 14 lacks), so
    # macOS 13/14 (Darwin 22/23) get 0.17.x — the last line with macosx_13_0
    # wheels; storage code 41, which ladybug_migrate upgrades forward when the
    # machine later moves to a newer line. Those platforms therefore stay
    # exposed to the storage-corruption defects fixed in 0.18.2 and 0.19.1
    # (COG-6185).
    # Pinned at 0.19.0, not 0.19.1: extension.ladybugdb.com publishes no
    # v0.19.1 JSON extension (404 on every platform), and 0.19.1 segfaults
    # cognee's DB worker mid-write in CI. 0.19.0 carries the same storage
    # fix and its extension build exists.
    # Each pinned version's on-disk storage code must also exist in
    # cognee_db_workers.ladybug_migrate.ladybug_version_mapping (0.19.0 -> 43),
    # so bumping this pin is a two-file change.
    # 0.19.x Windows wheels no longer vendor the OpenSSL DLLs their extension
    # imports; cognee_db_workers._windows_openssl supplies them. Drop that shim
    # once a pinned release vendors OpenSSL again.
    "ladybug>=0.17.0,<0.18 ; sys_platform == 'darwin' and ('Darwin Kernel Version 22.' in platform_version or 'Darwin Kernel Version 23.' in platform_version)",
    "ladybug==0.19.0 ; sys_platform != 'darwin' or ('Darwin Kernel Version 22.' not in platform_version and 'Darwin Kernel Version 23.' not in platform_version)",
    "python-magic-bin<0.5 ; platform_system == 'Windows'", # Only needed for Windows
    "networkx>=3.4.2,<4",
    "uvicorn>=0.34.0,<1.0.0",
    "gunicorn>=20.1.0,<24",
    "websockets>=15.0.1,<16.0.0",
    "tenacity>=9.0.0",
    "fakeredis[lua]>=2.32.0",
    "diskcache>=5.6.3",
    "aiolimiter>=1.2.1",
    "urllib3>=2.6.0",
    "cbor2>=5.8.0",
    "langdetect>=1.0.9",
    "datamodel-code-generator>=0.54.0",
]

[project.optional-dependencies]
api=[]

scraping = [
    "tavily-python>=0.7.12",
    "beautifulsoup4>=4.13.1",
    "playwright>=1.9.0",
    "lxml>=4.9.3,<5 ; python_version < '3.13'",
    "lxml>=5,<6 ; python_version >= '3.13' and python_version < '3.14'",
    # cp314 wheels start at lxml 6.0.1; without this 3.14 falls back to a
    # source build that requires libxml2/libxslt headers (CI doesn't have them).
    "lxml>=6.0.1,<7 ; python_version >= '3.14'",
    "protego>=0.1",
    "APScheduler>=3.10.0,<=3.11.0"
]

fastembed = [
    "fastembed<=0.8.0",
    # onnxruntime 1.23.2 only ships wheels through cp313; cp314 wheels start
    # at onnxruntime 1.24.1. Split by python_version so existing 3.10–3.13
    # users keep the pinned version and 3.14 picks up the first cp314-capable
    # release.
    "onnxruntime<=1.23.2 ; python_version < '3.14'",
    "onnxruntime>=1.24.1 ; python_version >= '3.14'",
]

neo4j = ["neo4j>=5.28.0,<6"]
neptune = ["langchain_aws>=0.2.22"]
postgres = [
    "psycopg2>=2.9.10,<3",
    "pgvector>=0.3.5,<0.4",
    "asyncpg>=0.30.0,<1.0.0",
]
postgres-binary = [
    "psycopg2-binary>=2.9.10,<3.0.0",
    "pgvector>=0.3.5,<0.4",
    "asyncpg>=0.30.0,<1.0.0",
]
turso = ["libsql-experimental>=0.0.55,<0.1"]
notebook = ["notebook>=7.1.0,<8"]
langchain = [
    "langsmith>=0.2.3,<1.0.0",
    "langchain_text_splitters>=0.3.2,<1.0.0",
    "langchain-core>=1.2.5"
]
llama-index = ["llama-index-core>=0.14.20,<0.15"]
huggingface = ["transformers>=4.46.3,<6"]
ollama = ["transformers>=4.46.3,<6"]
mistral = ["mistral-common>=1.5.2,<2", "mistralai>=1.9.10,<2"]
anthropic = ["anthropic>=0.27"]
azure = ["azure-identity>=1.15.0,<2"]
deepeval = ["deepeval>=3.0.1,<4"]
posthog = ["posthog>=3.5.0,<4"]
groq = ["groq>=0.8.0,<1.0.0"]
llama-cpp = ["llama-cpp-python[server]>=0.3.0,<1.0.0"]
docs = [
    "lxml>=4.9.3,<5 ; python_version < '3.13'",
    "lxml>=5,<6 ; python_version >= '3.13' and python_version < '3.14'",
    # cp314 wheels start at lxml 6.0.1.
    "lxml>=6.0.1,<7 ; python_version >= '3.14'",
    "unstructured[csv, doc, docx, epub, md, odt, org, ppt, pptx, rst, rtf, tsv, xlsx, pdf]>=0.18.1,<19",
    "nltk>=3.9.3,<4", # TODO: Remove when unstructured is above v0.21.0 as it won't use nltk anymore
]
codegraph = [
    "fastembed<=0.8.0 ; python_version < '3.14'",
    "transformers>=4.46.3,<6",
]
evals = [
    "plotly>=6.0.0,<7",
    "gdown>=5.2.0,<6",
    "pandas>=2.2.2,<3.0.0",
    "matplotlib>=3.8.3,<4",
    "scikit-learn>=1.6.1,<2",
    "locust>=2.0.0,<3",
]

graphiti = ["graphiti-core>=0.28.0"]
# Note: New s3fs and boto3 versions don't work well together
# Always use compatible fixed versions of these two dependencies
aws = ["s3fs[boto3]==2025.3.2"]
dlt = [
    "dlt[sqlalchemy]>=1.9.0,<2",
    # dlt's filesystem read_csv reader requires pandas but does not declare it
    "pandas>=2.2.2,<3.0.0",
]
gmail = [
    "dlt[sqlalchemy]>=1.9.0,<2",
    "pandas>=2.2.2,<3.0.0",
    "google-api-python-client>=2.100.0,<3",
    "google-auth>=2.23.0,<3",
    "google-auth-oauthlib>=1.1.0,<2",
]
baml = ["baml-py (==0.206.0)"]
dev = [
    "pytest>=7.4.0,<8",
    "pytest-cov>=6.1.1,<7.0.0",
    "pytest-asyncio>=0.21.1,<0.22",
    "pytest-timeout>=2.3.1,<3",
    "pytest-split>=0.11.0,<0.12",
    "coverage>=7.3.2,<8",
    "pre-commit>=4.0.1,<5",
    "notebook>=7.1.0,<8",
    "deptry>=0.20.0,<0.21",
    "ruff>=0.9.2,<=0.16.0",
    "tweepy>=4.14.0,<5.0.0",
    "gitpython>=3.1.43,<4",
    "mkdocs-material>=9.5.42,<10",
    "mkdocs-minify-plugin>=0.8.0,<0.9",
    "mkdocstrings[python]>=0.26.2,<0.27",
    "ty>=0.0.31,<0.1.0",
]
debug = ["debugpy>=1.8.9,<2.0.0"]
redis = ["redis>=5.0.3,<6.0.0"]

tracing = [
    "opentelemetry-api>=1.20.0,<2",
    "opentelemetry-sdk>=1.20.0,<2",
    "opentelemetry-exporter-otlp-proto-grpc>=1.20.0,<2",
    "opentelemetry-exporter-otlp-proto-http>=1.20.0,<2",
]

# Slim docling profile: converts office/HTML/email/markdown/LaTeX documents
# without torch or the ML layout models (~280MB installed vs multiple GB).

# Repository semantic capsule: HKUDS/LightRAG

- Commit: `133fdecfa921875f9df6ccabcc09cc15d9972fde`
- Default branch: `main`
- Description: HKUDS/LightRAG
- Selected evidence files: 7 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

<div align="center">

<div style="margin: 20px 0;">
  <img src="./assets/logo.png" width="120" height="120" alt="LightRAG Logo" style="border-radius: 20px; box-shadow: 0 8px 32px rgba(0, 217, 255, 0.3);">
</div>

# 🚀 LightRAG: Simple and Fast Retrieval-Augmented Generation

<div align="center">
    <a href="https://trendshift.io/repositories/13043" target="_blank"><img src="https://trendshift.io/api/badge/repositories/13043" alt="HKUDS%2FLightRAG | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</div>
<p>
</p>
<div align="center">
  <div style="width: 100%; height: 2px; margin: 20px 0; background: linear-gradient(90deg, transparent, #00d9ff, transparent);"></div>
</div>

<div align="center">
  <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; padding: 25px; text-align: center;">
    <p>
      <a href='https://github.com/HKUDS/LightRAG'><img src='https://img.shields.io/badge/🔥Project-Page-00d9ff?style=for-the-badge&logo=github&logoColor=white&labelColor=1a1a2e'></a>
      <a href='https://arxiv.org/abs/2410.05779'><img src='https://img.shields.io/badge/📄arXiv-2410.05779-ff6b6b?style=for-the-badge&logo=arxiv&logoColor=white&labelColor=1a1a2e'></a>
      <a href="https://github.com/HKUDS/LightRAG/stargazers"><img src='https://img.shields.io/github/stars/HKUDS/LightRAG?color=00d9ff&style=for-the-badge&logo=star&logoColor=white&labelColor=1a1a2e' /></a>
    </p>
    <p>
      <img src="https://img.shields.io/badge/🐍Python-3.10-4ecdc4?style=for-the-badge&logo=python&logoColor=white&labelColor=1a1a2e">
      <a href="https://pypi.org/project/lightrag-hku/"><img src="https://img.shields.io/pypi/v/lightrag-hku.svg?style=for-the-badge&logo=pypi&logoColor=white&labelColor=1a1a2e&color=ff6b6b"></a>
    </p>
    <p>
      <a href="https://discord.gg/yF2MmDJyGJ"><img src="https://img.shields.io/badge/💬Discord-Community-7289da?style=for-the-badge&logo=discord&logoColor=white&labelColor=1a1a2e"></a>
      <a href="https://github.com/HKUDS/LightRAG/issues/285"><img src="https://img.shields.io/badge/💬WeChat-Group-07c160?style=for-the-badge&logo=wechat&logoColor=white&labelColor=1a1a2e"></a>
    </p>
    <p>
      <a href="README-zh.md"><img src="https://img.shields.io/badge/🇨🇳中文版-1a1a2e?style=for-the-badge"></a>
      <a href="README.md"><img src="https://img.shields.io/badge/🇺🇸English-1a1a2e?style=for-the-badge"></a>
      <a href="README-ja.md"><img src="https://img.shields.io/badge/🇯🇵日本語版-1a1a2e?style=for-the-badge"></a>
      <a href="README-id.md"><img src="https://img.shields.io/badge/🇮🇩Bahasa%20Indonesia-1a1a2e?style=for-the-badge"></a>
    </p>
    <p>
      <a href="https://pepy.tech/projects/lightrag-hku"><img src="https://static.pepy.tech/personalized-badge/lightrag-hku?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads"></a>
      <a href="https://hvtracker.net/agents/lightrag/"><img src="https://hvtracker.net/badge/lightrag.svg"></a>
    </p>
  </div>
</div>

</div>

<div align="center" style="margin: 30px 0;">
  <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="800">
</div>

<div align="center" style="margin: 30px 0;">
    <img src="./README.assets/b2aaf634151b4706892693ffb43d9093.png" width="800" alt="LightRAG Diagram">
</div>

---

<div align="center">
  <table>
    <tr>
      <td style="vertical-align: middle;">
        <img src="./assets/LiteWrite.png"
             width="56"
             height="56"
             alt="LiteWrite"
             style="border-radius: 12px;" />
      </td>
      <td style="vertical-align: middle; padding-left: 12px;">
        <a href="https://litewrite.ai">
          <img src="https://img.shields.io/badge/🚀%20LiteWrite-AI%20Native%20LaTeX%20Editor-ff6b6b?style=for-the-badge&logoColor=white&labelColor=1a1a2e">
        </a>
      </td>
    </tr>
  </table>
</div>

---

## 🎉 News
- [2026.07]🎯[New Feature]: Add **Smart Heading** recognition feature for word documents.
- [2026.05]🎯[New Feature]: **Merge RagAnything into LightRAG**🎉. Multimodal content parsing and extraction via **MinerU / Docling** services.
- [2026.05]🎯[New Feature]: Introducing four selectable text chunking strategies: `Fix`, `Recursive`, `Vector`, and `Paragraph`.
- [2026.05]🎯[New Feature]: **Role-specific LLM configuration** support, 4 distinct roles: EXTRACT, QUERY, KEYWORDS, and VLM, with independent LLM settings.
- [2026.03]🎯[New Feature]: Integrated **OpenSearch** as a unified storage backend, providing comprehensive support for all four LightRAG storage.
- [2026.03]🎯[New Feature]: Introduced a setup wizard. Support for local deployment of embedding, reranking, and storage backends via Docker.
- [2025.11]🎯[New Feature]: Integrated **RAGAS for Evaluation** and **Langfuse for Tracing**. Updated the API to return retrieved contexts alongside query results to support context precision metrics.
- [2025.10]🎯[Scalability Enhancement]: Eliminated processing bottlenecks to support **Large-Scale Datasets Efficiently**.
- [2025.09]🎯[New Feature] Enhances knowledge graph extraction accuracy for **Open-Sourced LLMs** such as Qwen3-30B-A3B.
- [2025.08]🎯[New Feature] **Reranker** is now supported, significantly boosting performance for mixed queries (set as default query mode).
- [2025.08]🎯[New Feature] Added **Document Deletion** with automatic KG regeneration to ensure optimal query performance.
- [2025.06]🎯[New Release] Our team has released [RAG-Anything](https://github.com/HKUDS/RAG-Anything) — an **All-in-One Multimodal RAG** system for seamless processing of text, images, tables, and equations.
- [2025.06]🎯[New Feature] LightRAG now supports comprehensive multimodal data handling through [RAG-Anything](https://github.com/HKUDS/RAG-Anything) integration, enabling seamless document parsing and RAG capabilities across diverse formats including PDFs, images, Office documents, tables, and formulas. Please refer to the new [multimodal section](https://github.com/HKUDS/LightRAG/?tab=readme-ov-file#multimodal-document-processing-rag-anything-integration) for details.
- [2025.03]🎯[New Feature] LightRAG now supports citation functionality, enabling proper source attribution and enhanced document traceability.
- [2025.02]🎯[New Feature] You can now use MongoDB as an all-in-one storage solution for unified data management.
- [2025.02]🎯[New Release] Our team has released [VideoRAG](https://github.com/HKUDS/VideoRAG)-a RAG system for understanding extremely long-context videos
- [2025.01]🎯[New Release] Our team has released [MiniRAG](https://github.com/HKUDS/MiniRAG) making RAG simpler with small models.
- [2025.01]🎯You can now use PostgreSQL as an all-in-one storage solution for data management.
- [2024.11]🎯[New Resource] A comprehensive guide to LightRAG is now available on [LearnOpenCV](https://learnopencv.com/lightrag). — explore in-depth tutorials and best practices. Many thanks to the blog author for this excellent contribution!
- [2024.11]🎯[New Feature] Introducing the LightRAG WebUI — an interface that allows you to insert, query, and visualize LightRAG knowledge through an intuitive web-based dashboard.
- [2024.11]🎯[New Feature] You can now [use Neo4J for Storage](https://github.com/HKUDS/LightRAG?tab=readme-ov-file#using-neo4j-for-storage)-enabling graph database support.
- [2024.10]🎯[New Feature] We've added a link to a [LightRAG Introduction Video](https://youtu.be/oageL-1I0GE). — a walkthrough of LightRAG's capabilities. Thanks to the author for this excellent contribution!
- [2024.10]🎯[New Channel] We have created a [Discord channel](https://discord.gg/yF2MmDJyGJ)!💬 Welcome to join our community for sharing, discussions, and collaboration! 🎉🎉

<details>
  <summary style="font-size: 1.4em; font-weight: bold; cursor: pointer; display: list-item;">
    Algorithm Flowchart
  </summary>

![LightRAG Indexing Flowchart](https://learnopencv.com/wp-content/uploads/2024/11/LightRAG-VectorDB-Json-KV-Store-Indexing-Flowchart-scaled.jpg)
*Figure 1: LightRAG Indexing Flowchart - Img Caption : [Source](https://learnopencv.com/lightrag/)*
![LightRAG Retrieval and Querying Flowchart](https://learnopencv.com/wp-content/uploads/2024/11/LightRAG-Querying-Flowchart-Dual-Level-Retrieval-Generation-Knowledge-Graphs-scaled.jpg)
*Figure 2: LightRAG Retrieval and Querying Flowchart - Img Caption : [Source](https://learnopencv.com/lightrag/)*

</details>

## Installation

**💡 Using uv for Package Management**: This project uses [uv](https://docs.astral.sh/uv/) for fast and reliable Python package management. Install uv first: `curl -LsSf https://astral.sh/uv/install.sh | sh` (Unix/macOS) or `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"` (Windows)

> **Note**: You can also use pip if you prefer, but uv is recommended for better performance and more reliable dependency management.
>
> **📦 Offline Deployment**: For offline or air-gapped environments, see the [Offline Deployment Guide](./docs/OfflineDeployment.md) for instructions on pre-installing all dependencies and cache files.

### Install LightRAG Server

* Install from PyPI

```bash
### Install LightRAG Server as tool using uv (recommended)
uv tool install "lightrag-hku[api]"

### Or using pip
# python -m venv .venv
# source .venv/bin/activate  # Windows: .venv\Scripts\activate
# pip install "lightrag-hku[api]"

# Setup env file
# Obtain the env.example file by downloading it from the GitHub repository root
# or by copying it from a local source checkout.
cp env.example .env  # Update the .env with your LLM and embedding configurations
# Launch the server. It binds to all interfaces (0.0.0.0) by default.
# SECURITY: before exposing it on a network, configure authentication in .env
# (LIGHTRAG_API_KEY, or AUTH_ACCOUNTS together with TOKEN_SECRET), or bind to
# 127.0.0.1 for local-only access; without auth every endpoint is public.
# Note: the Ollama-compatible /api/* routes stay open by default for client
# compatibility; set WHITELIST_PATHS=/health to require auth on them too.
lightrag-server
```

* Installation from Source

```bash
git clone https://github.com/HKUDS/LightRAG.git
cd LightRAG

# Bootstrap the development environment (recommended)
make dev
source .venv/bin/activate  # Activate the virtual environment (Linux/macOS)
# Or on Windows: .venv\Scripts\activate

# make dev installs the test toolchain plus the full offline stack
# (API, storage backends, and provider integrations), then builds the frontend.
# Run make env-base or copy env.example to .env before starting the server.

# Equivalent manual steps with uv
# Note: uv sync automatically creates a virtual environment in .venv/
uv sync --extra test --extra offline
source .venv/bin/activate  # Activate the virtual environment (Linux/macOS)
# Or on Windows: .venv\Scripts\activate

### Or using pip with virtual environment
# python -m venv .venv
# source .venv/bin/activate  # Windows: .venv\Scripts\activate
# pip install -e ".[test,offline]"

# Build front-end artifacts
cd lightrag_webui
bun install --frozen-lockfile
bun run build
cd ..

# setup env file
make env-base  # Or: cp env.example .env and update it manually
# Launch API-WebUI server
lightrag-server
```

* Launching the LightRAG Server with Docker Compose

```bash
git clone https://github.com/HKUDS/LightRAG.git
cd LightRAG
cp env.example .env  # Update the .env with your LLM and embedding configurations
# modify LLM and Embedding settings in .env
docker compose up
```

> Historical versions of LightRAG docker images can be found here: [LightRAG Docker Images]( https://github.com/HKUDS/LightRAG/pkgs/container/lightrag)
>
> Official GHCR images published by GitHub Actions are signed with Sigstore Cosign using GitHub OIDC. See [docs/DockerDeployment.md](./docs/DockerDeployment.md#verify-official-ghcr-images-with-cosign) for verification commands.
>
> On Apple Silicon (macOS 26) without Docker Desktop, you can run the same Postgres/Neo4j/Milvus storage stack on Apple's native `container` runtime — see [docs/AppleContainerSetup.md](./docs/AppleContainerSetup.md).

### Create .env File With Setup Tool

Instead of editing `env.example` by hand, use the interactive setup wizard to generate a configured `.env` and, when needed, `docker-compose.final.yml`:

```bash
make env-base           # Required first step: LLM, embedding, reranker
make env-storage        # Optional: storage backends and database services
make env-server         # Optional: server port, auth, and SSL
make env-base-rewrite   # Optional: force-regenerate wizard-managed compose services
make env-storage-rewrite # Optional: force-regenerate wizard-managed compose services
make env-security-check # Optional: audit the current .env for security risks
```

For full description of every target see [docs/InteractiveSetup.md](./docs/InteractiveSetup.md).

### Optional: spaCy Models for docx smart_heading


## `AGENTS.md`

# Repository Guidelines

## Project Overview

LightRAG is a Retrieval-Augmented Generation (RAG) framework that uses graph-based knowledge representation for enhanced information retrieval. The system extracts entities and relationships from documents, builds a knowledge graph, and uses multiple retrieval modes (`local`, `global`, `hybrid`, `mix`, `naive`) for queries.

## Project Structure

Top-level directories:

- **lightrag/**: Core Python package — see *Module Layout* below.
- **lightrag_webui/**: React 19 + TypeScript client (Bun + Vite + Tailwind). UI components in `src/`.
- **scripts/**: `test.sh` (preferred test runner), `setup/` interactive environment wizard (use `make env-*` rather than calling `setup.sh` directly — see *Configuration > Setup Wizard Outputs*), and release tooling.
- **tests/**: Pytest coverage, organized into subdirectories that mirror `lightrag/` (see *Testing* below for layout). Working datasets stay in `inputs/`, `rag_storage/`, and `temp/`; deployment collateral lives in `docs/`, `k8s-deploy/`, and compose files.

### Module Layout (`lightrag/`)

- **lightrag.py**: Main orchestrator class (`LightRAG`) — assembled from mixins (see *LightRAG class composition*). Hosts `ainsert_custom_kg`, `_insert_done`, `_process_extract_entities`, `_refresh_addon_params_cache`, and `addon_params` accessors. Critical: always call `await rag.initialize_storages()` after instantiation.
- **pipeline.py**: `_PipelineMixin` — owns the document ingestion pipeline (`apipeline_enqueue_documents`, `apipeline_process_enqueue_documents`, `apipeline_process_error_documents`), the `parse_native` / `parse_mineru` / `parse_docling` parser dispatchers, multimodal analysis, validation, and the worker scaffolding.
- **utils_pipeline.py**: Pure helpers shared by the pipeline mixin and other entry points: doc-status field access, document identity (source key, content hash), parsed-artifact path resolution, parser payload normalization, multimodal entity augmentation, and `make_lightrag_doc_content`.
- **llm_roles.py**: `RoleSpec` / `RoleLLMConfig` / `_RoleLLMState` / `ROLES` registry plus `_RoleLLMMixin` — role normalization, builder registration, wrapper rebuild, runtime config update, queue cleanup, sanitized config export, queue status reporting. Route role-specific behavior here rather than into provider modules.
- **storage_migrations.py**: `_StorageMigrationMixin` — `check_and_migrate_data`, `_migrate_entity_relation_data`, `_migrate_chunk_tracking_storage`.
- **addon_params.py**: `ObservableAddonParams` plus `default_addon_params` / `normalize_addon_params` helpers.
- **operate.py**: Core extraction and query operations including entity/relation extraction, chunking, and multi-mode retrieval logic.
- **base.py**: Abstract base classes for storage backends (`BaseKVStorage`, `BaseVectorStorage`, `BaseGraphStorage`, `BaseDocStatusStorage`).
- **kg/**: Storage implementations (JSON, NetworkX, Neo4j, PostgreSQL, MongoDB, Redis, Milvus, Qdrant, Faiss, Memgraph, OpenSearch, NanoVectorDB). The backend registry (`STORAGE_IMPLEMENTATIONS` / `STORAGES`) lives in `kg/__init__.py`; `kg/factory.py::get_storage_class()` resolves backend classes from configuration.
- **llm/**: LLM and embedding provider bindings (OpenAI, Ollama, Azure, Gemini, Bedrock, Anthropic, etc.). All async with caching support.
- **parser/**: Unified parsing layer. `parser/routing.py` resolves engine and filename hints for `legacy`, `native`, `mineru`, and `docling` flows; `parser/debug.py` provides an offline LightRAG stub for the `parser/cli.py` debug entry point (`python -m lightrag.parser.cli`). Native format parsers live as sibling sub-packages under `parser/` (currently `parser/docx/`); external HTTP-based adapters live under `parser/external/` (`mineru`, `docling`) with shared helpers in `parser/external/_common.py`, `_manifest.py`, `_zip.py`.
- **chunker/**: Chunking strategies (token-size, recursive character, semantic vector, paragraph semantic).
- **api/**: FastAPI service (`lightrag_server.py`) with REST endpoints and Ollama-compatible API; routers under `routers/`, static Swagger assets, packaged WebUI output, and Gunicorn launcher.

## Core Architecture

### LightRAG class composition

`LightRAG` is assembled from focused mixins (split out of the previously monolithic `lightrag.py`):

```
LightRAG → _RoleLLMMixin → _StorageMigrationMixin → _PipelineMixin → object
```

The `@final` decorator on `LightRAG` is preserved — the mixin layering is an internal implementation detail, not an external subclassing surface. The public API (`ainsert`, `aquery`, `ainsert_custom_kg`, `initialize_storages`, etc.) is unchanged. `ainsert_custom_kg` and its internal construction logic, `_insert_done`, `_process_extract_entities`, `_refresh_addon_params_cache`, and the `addon_params` property accessors stay on `LightRAG` itself because they cut across multiple flows or depend on prompt-profile state.

### Storage Layer

LightRAG uses 4 storage types with pluggable backends:
- **KV_STORAGE**: LLM response cache, text chunks, document info
- **VECTOR_STORAGE**: Entity/relation/chunk embeddings
- **GRAPH_STORAGE**: Entity-relation graph structure
- **DOC_STATUS_STORAGE**: Document processing status tracking

Each `LightRAG` instance can pass a `workspace` parameter for data isolation. Implementation differs per storage type:
- **File-based**: subdirectories under `working_dir`.
- **Collection-based**: collection name prefixes.
- **Relational DB**: workspace column filtering.
- **Qdrant**: payload-based partitioning.

### Consistency without transactions

LightRAG writes to independent stores — graph, KV, vector, doc-status — with **no transaction across them**. Every multi-store operation therefore has intermediate states, and no ordering removes them; an ordering only chooses which one it keeps.

- **The rule:** an inconsistency is acceptable when it **heals itself later** (a retry, a rebuild, or the next run rewrites it) or is **harmless in direction**. Losing data is never acceptable; retaining an object that could have been deleted, or surfacing a chunk a query did not need, is.
- A change must **improve on an accepted residue**, not swap it for its mirror. "An inconsistent state exists" is not by itself a defect report — the questions are which state, how it heals, and whether the alternative is better.
- Every accepted residue is **written down** with its reason and recovery path, next to the code or in the relevant contract. An undocumented residue is a defect; a documented one is a decision.
- This licenses nothing for **silent failure**. A durable write must never be reported as one that did not happen, and a failure must never be swallowed: fail loud, then let the documented residue heal.

### File-backed storage contracts

**Full contracts: [docs/design/NetworkXSingleWriterContract.md](docs/design/NetworkXSingleWriterContract.md) — read it before touching `lightrag/kg/networkx_impl.py` or any caller of `index_done_callback` on the graph store; [docs/design/FileBackedSnapshotContract.md](docs/design/FileBackedSnapshotContract.md) — read it before touching `lightrag/kg/nano_vector_db_impl.py`, `lightrag/kg/faiss_impl.py`, `lightrag/kg/json_kv_impl.py`, `lightrag/kg/json_doc_status_impl.py` or `lightrag/kg/file_fingerprint.py`.**

Five storages keep their data in memory and publish it by rewriting a whole file, and **they do not share one model** — `JsonKVStorage` and `JsonDocStatusStorage` are the odd ones out and the contracts say so at length. Read the right one before assuming.

- **All five**: a commit publishes the WHOLE namespace, so any writer's flush also publishes every other writer's pending mutation there, half-finished ones included. All five are supported for **small-scale testing and validation only**; no change to them may be justified by write throughput.
- **`NetworkXStorage`, `NanoVectorDBStorage`, `FaissVectorDBStorage`** keep one in-memory copy per process and reconcile by reloading the file. Visibility rests on a **two-channel fence**: the file's own `(st_mtime_ns, st_size)` (authoritative, state) OR-ed with the `storage_updated` flag (accelerator, a consumable event). Both are permanent — their blind spots do not overlap.
- Those three diverge on a write conflict, and the reason is in the contracts: the graph store **declines** the commit (it has no buffer to replay, and graph payloads are accumulate-over-read), the vector stores **reload and replay** their pending buffers and redo logs. Do not reopen reload-then-replay for the graph store without addressing the accumulate-over-read argument.
- **`JsonKVStorage` and `JsonDocStatusStorage` use none of that.** Their data is a `Manager().dict()` every worker shares, so a mutation is visible everywhere immediately and there is nothing to reload — adding a `_get_*` entry method would be wrong. Their `storage_updated` flag means the OPPOSITE of the other three's: `True` is "dirty data still to flush", never "fresher data on disk to reload". Do not read it as a peer notification. `JsonDocStatusStorage` reimplements this protocol rather than inheriting it, so a change to one of the pair is almost always a change the other needs too; where they diverge is the flush trigger — doc-status writes that change scheduling state flush synchronously because doc-status is the pipeline's recovery anchor.
- `NetworkXStorage` is the only storage that declares `requires_single_writer`, which is what puts the admin flows under `LightRAG._admin_write_gate`.

### Pipeline concurrency contract

**Full contract: [docs/design/PipelineConcurrencyContract.md](docs/design/PipelineConcurrencyContract.md) — read it before touching `lightrag/pipeline.py`, `lightrag/kg/pipeline_ingress.py`, `pipeline_status` fields, or any `/documents/*` endpoint.**

- Concurrent writers coordinate through `pipeline_status` (per-workspace shared dict in `lightrag.kg.shared_storage`), mutated under `get_namespace_lock("pipeline_status", workspace=...)`.
- `busy` alone does NOT block enqueue — enqueue + processing are allowed to run concurrently. Three states do refuse it: `destructive_busy` (clear / delete, which drops storages), `scanning_exclusive` (scan's classification phase), and `manual_freeze_requested` (a manual retry draining the pipeline to idle).
- **Admin graph writes** (`acreate_*` / `aedit_*` / `adelete_by_*` / `amerge_entities` / `ainsert_custom_kg`) run inside `LightRAG._admin_write_gate` when the graph storage declares `requires_single_writer` (`NetworkXStorage` only): a workspace admin lock (waited for) then the `busy` reservation (`kind="admin"`, refuses on `busy` / `scanning`), in that fixed order and OUTSIDE the per-entity keyed locks. A pipeline start during the hold is deferred into the ingress mailbox and driven once on release. The routes' `check_pipeline_busy_or_raise` preflight exempts an `admin`-owned `busy` so a second REST edit reaches the admin lock and queues. Never re-acquire the admin lock inside `lightrag/utils_graph.py`.
- The workspace **ingress mailbox** (`get_pipeline_ingress(workspace)`) is the pipeline's only wake-up channel; `doc_status` stays the source of truth, so a dropped notification is recovered by the next strict scan.
- FAILED documents never resume automatically: they re-enter only through a sticky manual retry request (`/documents/scan`, `/documents/reprocess_failed`), granting ONE attempt each.
- All scheduling-control-plane `doc_status` queries use `get_docs_by_statuses(..., strict=True)`; scheduler `full_docs` reads must distinguish confirmed-absent (`None`) from backend errors (raise).

### Purge recovery contract

**Full contract: [docs/design/PurgeRecoveryContract.md](docs/design/PurgeRecoveryContract.md) — read it before touching `_purge_kg_contributions`, `adelete_by_doc_id`, the anchor writes in `merge_nodes_and_edges`, the `kg_write_state` / `kg_purge` metadata, or the cache write ordering in `use_llm_func_with_cache`.**

- "What did this document contribute?" is answerable only from the per-document write-ahead anchors (`full_entities` / `full_relations`). The reverse lookup through `text_chunks` is not a fallback — purge deletes those chunks.
- Governing invariant: **a purge must never delete something that CARRIES attribution — a chunk row or an anchor row that names objects — and leave those objects behind.** `_purge_kg_contributions` **fails closed** (`RecoveryAnchorMissingError` → HTTP 409, nothing deleted) unless one of four proofs holds: `anchors`, `pre_graph`, `journal`, `empty_scope`.
- **`kg_write_state` must never be inferred or backfilled** — it is written once at enqueue and is monotonic. A backfill reproduces the original silent-skip defect.
- `kg_write_state` and `kg_purge` must stay in both `_DOC_STATUS_METADATA_CARRY_OVER_KEYS` and `_DOC_STATUS_METADATA_DIRECTIVE_KEYS` (`lightrag/utils_pipeline.py`); dropping either turns a resumable purge into a permanent refusal.
- Chunk tracking (`entity_chunks` / `relation_chunks`) outranks graph `source_id`; code folding a `source_id` delta back into tracking must append genuine additions only.
- LLM extraction cache rows are reachable only through the owning chunk's `llm_cache_list`, which makes that list an attribution carrier too: [LLM extraction cache reachability](docs/design/PurgeRecoveryContract.md#llm-extraction-cache-reachability) states the reference-before-row ordering, why a reference that cannot be recorded skips the cache write instead, and what the ordering does not close.
- Merge and rename apply *Consistency without transactions* above: [the failure model](docs/design/PurgeRecoveryContract.md#merge-and-rename-failure-model) lists their ordering invariants, accepted residues and already-rejected remedies. Read it before reordering `_merge_entities_impl` or the rename branch of `_edit_entity_impl`.

### Relation weight contract

**Full contract: [docs/ProgramingWithCore.md](docs/ProgramingWithCore.md#relation-weight-contract)** — keep it synchronized with the core API docstrings, REST graph documentation, and custom-KG examples whenever relation write behavior changes.

- `weight >= len(distinct real source IDs)` on the graph edge; a larger value is an optional importance boost. Empty IDs and the legacy placeholders `manual_creation` / `UNKNOWN` are not evidence, so a source-less relation may use any non-negative fractional weight.
- Public ingress paths (`create_relation`, `edit_relation`, `insert_custom_kg`) must validate the complete relation **before the first storage mutation**. To go below the current evidence count, creation callers omit `source_id`, edit callers set it to an empty string in the same operation.
- Entity merges use `max(all input weights, distinct merged real source IDs)`.
- Legacy-row repair is **opportunistic, not a sweep**: `_merge_edges_then_upsert`'s KEEP-cap skip branch returns the stored edge without writing graph or vector record, so an undersized legacy row stays undersized until a merge, an unrelated edit, or a rebuild rewrites it.

### Query Modes

- **local**: Context-dependent retrieval focused on specific entities
- **global**: Community/summary-based broad knowledge retrieval
- **hybrid**: Combines local and global
- **naive**: Direct vector search without graph
- **mix**: Integrates KG and vector retrieval (recommended with reranker)

## Development Commands

### Setup
```bash
# Install with uv
uv sync
source .venv/bin/activate  # Or: .venv\Scripts\activate on Windows

# Install with API support
uv sync --extra api

# Install specific extras
uv sync --extra offline-storage  # Storage backends
uv sync --extra offline-llm      # LLM providers
uv sync --extra test             # Testing dependencies
```

### API Server
```bash
# Copy and configure environment
cp env.example .env  # Edit with your LLM/embedding configs

# Build WebUI
cd lightrag_webui
bun install --frozen-lockfile
bun run build
cd ..

# Run server
lightrag-server                                           # Production
uvicorn lightrag.api.lightrag_server:app --reload        # Development
lightrag-gunicorn                                         # Multi-worker (gunicorn)
```

### WebUI

Every command below is run **from `lightrag_webui/`**, not the repository root.
`bun test` in particular resolves `bunfig.toml` — and the preload paths inside
it — relative to the working directory, so running it from the root silently
loads no DOM (see *React component tests*).

```bash
cd lightrag_webui
bun install --frozen-lockfile      # REQUIRED after any change to package.json /
                                   # bun.lock, including a branch switch across
                                   # one: `git checkout` does not update
                                   # node_modules, and a stale tree surfaces as
                                   # a wall of TS2307 "Cannot find module".
bun run dev                        # Dev server (Node + Vite)
bun run dev:bun                    # Dev server (Bun native)
bun run build                      # Production build
bun run preview                    # Preview production build
bun run lint                       # ESLint over *.ts/tsx/js/jsx

# Testing — Bun built-in runner (NOT Vitest/Jest)
bun test                           # All tests
bun test --watch                   # Watch mode
bun test --coverage                # With coverage report
bun test src/api/lightrag.test.ts  # Single test file
bunx tsc --noEmit                  # Typecheck (`bun run build` does NOT typecheck)
```

### Testing

- Use mock-based tests for external services (Redis, httpx, etc.) — do not depend on live services in unit tests.
- Add regression tests for every bug fix.
- **Run only the test directories that mirror the modules you changed**, and report which subset you ran plus its pass count. The suite is ~7000 tests and a full run takes over 6 minutes, which is too slow for the edit loop. Every PR's CI runs the full suite — proving nothing else broke is its job, not yours.
- Derive the subset from the mirror layout below: `lightrag/api/config.py` → `tests/api/config/`, `lightrag/kg/redis_impl.py` → `tests/kg/redis_impl/`, `lightrag/chunker/` → `tests/chunker/`. When a change spans several modules, run each of their directories rather than widening to `tests/`.
- Run the full suite locally only at a milestone, or when the change is genuinely cross-cutting (`lightrag/base.py`, `lightrag/utils.py`, `lightrag/kg/shared_storage.py`, or anything every backend inherits).
- Backend tests use pytest; frontend unit tests use Bun's built-in runner — see *WebUI* above and *React component tests* below.
- **A WebUI change runs the WHOLE frontend check set**, from `lightrag_webui/`: `bun install --frozen-lockfile` (see *WebUI* above — skip it after a branch switch and every later step fails on missing modules), then `bun test`, `bunx tsc --noEmit`, and `bun run lint`. The subsetting rule above is a backend rule and does not apply — all three together take well under a minute (test ~2 s, typecheck ~14 s, lint ~21 s), so there is nothing to save by running less. Report the pass count. `bun run build` transpiles WITHOUT checking types, so skipping `tsc --noEmit` means nothing checks them.

```bash
# Preferred for fresh shells and automation; resolves PYTHON, venv, uv, .venv, venv, python, python3
# Default during development: only the directories mirroring the changed modules
./scripts/test.sh tests/api/config
./scripts/test.sh tests/kg/redis_impl

# Run specific test file
./scripts/test.sh tests/kg/test_graph_storage.py

# Full suite — ~7000 tests, >6 min; milestones and cross-cutting changes only
./scripts/test.sh tests

# Run with custom workers
./scripts/test.sh tests --test-workers 4
```

- `tests/`: main test suite, mirrors feature folders. Place new tests under the subdirectory matching the module under test:
  - `tests/api/{auth,config,routes}/` for FastAPI server tests (auth/token, config loading, route handlers); top-level `tests/api/` for app-wide concerns (path prefixes, Ollama-compatible endpoint).
  - `tests/chunker/`, `tests/evaluation/`, `tests/extraction/` for the like-named modules.
  - `tests/kg/<backend>_impl/` for backend-specific storage tests, mirroring the `lightrag/kg/<backend>_impl.py` file naming. The `_impl` suffix on every subdirectory keeps the layout uniform and avoids `sys.path` shadowing on names that overlap with top-level PyPI/stdlib packages (`faiss`, `json`, `neo4j`, `networkx`, `redis`) when a test is launched directly via `python tests/kg/...`. Current backends: `faiss_impl/`, `json_impl/`, `memgraph_impl/`, `milvus_impl/`, `mongo_impl/`, `nano_impl/`, `neo4j_impl/`, `networkx_impl/`, `opensearch_impl/`, `postgres_impl/`, `qdrant_impl/`, `redis_impl/`. `tests/kg/` root holds cross-backend tests (`test_graph_storage`, `test_batch_graph_operations`, `test_unified_lock_safety`, `test_file_atomic`).
  - `tests/llm/<provider>_impl/` for provider-specific behavior, same `_impl` convention: `bedrock_impl/`, `gemini_impl/`, `ollama_impl/`, `openai_impl/`, `voyageai_impl/`, `zhipu_impl/`. `tests/llm/` root holds cross-provider concerns (embedding, VLM, cache, role).
  - `tests/parser/`, `tests/parser/docx/`, `tests/parser/external/{mineru,docling}/` for parser implementations.
  - `tests/pipeline/` for ingestion pipeline and doc-status behavior (including `test_pipeline_*`, `test_doc_status_*`, `test_multimodal_*`, `test_graph_keyed_locks`).
  - `tests/sidecar/`, `tests/setup/`, `tests/workspace/` for the like-named cross-cutting concerns.
  - When adding a new backend or LLM provider, create a new subdirectory plus an empty `__init__.py` rather than dropping the file in the parent directory root.
- Markers (registered in `[tool.pytest.ini_options]` in `pyproject.toml`): `offline`, `integration`, `requires_db`, `requires_api`, `pg_smoke`. Integration tests are skipped by default via `-m "not integration"`; opt in with `--run-integration`.
- Integration env vars: `LIGHTRAG_RUN_INTEGRATION=true`, `LIGHTRAG_KEEP_ARTIFACTS=true`, `LIGHTRAG_TEST_WORKERS=4`, plus storage-specific connection strings.

#### React component tests


## `CLAUDE.md`

@AGENTS.md

## `Dockerfile`

# syntax=docker/dockerfile:1

# Frontend build stage
# Build frontend assets on the native build platform to avoid
# cross-architecture emulation issues during multi-platform builds.
FROM --platform=$BUILDPLATFORM oven/bun:1 AS frontend-builder

WORKDIR /app

# Copy frontend source code
COPY lightrag_webui/ ./lightrag_webui/

# Build frontend assets for inclusion in the API package
RUN --mount=type=cache,target=/root/.bun/install/cache \
    cd lightrag_webui \
    && bun install --frozen-lockfile \
    && bun run build

# Python build stage - using uv for faster package installation
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

ENV DEBIAN_FRONTEND=noninteractive
ENV UV_SYSTEM_PYTHON=1
ENV UV_COMPILE_BYTECODE=1

WORKDIR /app

# Install system deps (Rust is required by some wheels)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        build-essential \
        pkg-config \
    && rm -rf /var/lib/apt/lists/* \
    && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

ENV PATH="/root/.cargo/bin:/root/.local/bin:${PATH}"

# Ensure shared data directory exists for uv caches
RUN mkdir -p /root/.local/share/uv

# Copy project metadata and sources
COPY pyproject.toml .
COPY setup.py .
COPY uv.lock .

# Install base, API, and offline extras without the project to improve caching
RUN --mount=type=cache,target=/root/.local/share/uv \
    uv sync --frozen --no-dev --extra api --extra offline --no-install-project --no-editable

# Copy project sources after dependency layer
COPY lightrag/ ./lightrag/

# Include pre-built frontend assets from the previous stage
COPY --from=frontend-builder /app/lightrag/api/webui ./lightrag/api/webui

# Sync project in non-editable mode and ensure pip is available for runtime installs
RUN --mount=type=cache,target=/root/.local/share/uv \
    uv sync --frozen --no-dev --extra api --extra offline --no-editable \
    && /app/.venv/bin/python -m ensurepip --upgrade

# Prepare offline cache directory, pre-populate tiktoken data, and download the
# pinned spaCy model wheels for the docx smart_heading engine parameter.
# Use uv run to execute commands from the virtual environment
RUN mkdir -p /app/data/tiktoken \
    && uv run lightrag-download-cache --cache-dir /app/data/tiktoken --spacy-dir /app/spacy_models || status=$?; \
    if [ -n "${status:-}" ] && [ "$status" -ne 0 ] && [ "$status" -ne 2 ]; then exit "$status"; fi

# Final stage
# Pin to bookworm: keeps Python 3.12 (venv compat with the builder stage) while
# avoiding Debian trixie's perl 5.40.x exposure (CVE-2026-12087, no patch yet),
# and aligns the final Debian release with the builder (also bookworm).
FROM python:3.12-slim-bookworm

WORKDIR /app

# Install uv for package management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

ENV UV_SYSTEM_PYTHON=1

# Copy installed packages and application code
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/lightrag ./lightrag
COPY pyproject.toml .
COPY setup.py .
COPY uv.lock .

# Ensure the installed scripts are on PATH
ENV PATH=/app/.venv/bin:/root/.local/bin:$PATH

# Install dependencies with uv sync (uses locked versions from uv.lock)
# and ensure pip is available for runtime installs. The pinned spaCy model
# wheels (docx smart_heading) MUST be installed after uv sync — sync is exact
# and would remove packages that are not in the lock. The bind mount exposes
# the wheels downloaded in the builder stage without adding an image layer.
RUN --mount=type=cache,target=/root/.local/share/uv \
    --mount=type=bind,from=builder,source=/app/spacy_models,target=/tmp/spacy_models \
    uv sync --frozen --no-dev --extra api --extra offline --no-editable \
    && /app/.venv/bin/python -m ensurepip --upgrade \
    && /app/.venv/bin/python -m pip install --no-index --no-cache-dir \
        --find-links=/tmp/spacy_models zh_core_web_sm en_core_web_sm

# Create persistent data directories AFTER package installation
RUN mkdir -p /app/data/rag_storage /app/data/inputs /app/data/prompts /app/data/tiktoken

# Copy offline cache into the newly created directory
COPY --from=builder /app/data/tiktoken /app/data/tiktoken

# Point to the prepared cache
ENV TIKTOKEN_CACHE_DIR=/app/data/tiktoken
ENV WORKING_DIR=/app/data/rag_storage
ENV INPUT_DIR=/app/data/inputs
ENV PROMPT_DIR=/app/data/prompts

# Create a non-root user (CIS Docker 4.1) and install gosu for privilege drop.
# Fixed UID/GID 1000 gives predictable ownership for bind-mounts / PVCs.
# libcairo2 is the native library cairosvg (SVG->PNG rasterization for native
# markdown images) binds to via cffi at runtime; cairosvg installs fine without
# it but svg2png() fails with "no library called cairo-2 was found".
# chown -R /app MUST run after every data COPY above so the venv (pipmaster
# installs packages at runtime), data dirs, and the tiktoken cache are writable.
RUN apt-get update \
    && apt-get install -y --no-install-recommends gosu libcairo2 \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd -g 1000 lightrag \
    && useradd -u 1000 -g lightrag -m -d /home/lightrag -s /usr/sbin/nologin lightrag \
    && chown -R lightrag:lightrag /app /home/lightrag

# HOME and cache dirs for the non-root user so pipmaster's runtime pip installs
# never fall back to an unwritable /root or a missing HOME.
ENV HOME=/home/lightrag \
    XDG_CACHE_HOME=/home/lightrag/.cache \
    PIP_CACHE_DIR=/home/lightrag/.cache/pip \
    UV_CACHE_DIR=/home/lightrag/.cache/uv

# Entrypoint starts as root, fixes mount ownership, then drops to lightrag.
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Expose API port
EXPOSE 9621

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["python", "-m", "lightrag.api.lightrag_server"]

## `Makefile`

SHELL := /bin/bash
SETUP_SCRIPT := scripts/setup/setup.sh
APPLE_SCRIPT := scripts/setup/apple-container.sh
SETUP_BASH ?= $(or $(firstword $(wildcard /opt/homebrew/bin/bash /usr/local/bin/bash /opt/local/bin/bash)),$(shell command -v bash 2>/dev/null),bash)
SETUP_OPTS ?=
COLOR_RESET := \033[0m
COLOR_BOLD := \033[1m
COLOR_BLUE := \033[34m
COLOR_GREEN := \033[32m
COLOR_YELLOW := \033[33m

ifeq ($(NO_COLOR),1)
COLOR_RESET :=
COLOR_BOLD :=
COLOR_BLUE :=
COLOR_GREEN :=
COLOR_YELLOW :=
endif

.PHONY: help dev configure env-base env-storage env-server env-validate env-backup env-security-check env-base-rewrite env-storage-rewrite env base storage server validate backup security security-check base-rewrite storage-rewrite apple-up apple-down apple-status apple-logs apple-restart apple-pull

help:
	@printf "$(COLOR_BOLD)Interactive setup targets$(COLOR_RESET)\n"
	@printf "  $(COLOR_GREEN)make dev$(COLOR_RESET)                    Bootstrap local dev+test+offline env with uv + bun\n"
	@printf "  $(COLOR_GREEN)make env-base$(COLOR_RESET)               Configure LLM, embedding, and reranker (run first)\n"
	@printf "  $(COLOR_GREEN)make env-storage$(COLOR_RESET)            Configure storage backends and databases\n"
	@printf "  $(COLOR_GREEN)make env-server$(COLOR_RESET)             Configure server, security, and SSL\n"
	@printf "  $(COLOR_GREEN)make env-validate$(COLOR_RESET)           Validate existing .env\n"
	@printf "  $(COLOR_GREEN)make env-security-check$(COLOR_RESET)     Audit existing .env for security risks\n"
	@printf "  $(COLOR_GREEN)make env-backup$(COLOR_RESET)             Backup current .env\n"
	@printf "  $(COLOR_GREEN)make env-base-rewrite$(COLOR_RESET)       Force-regenerate wizard-managed compose services during base setup\n"
	@printf "  $(COLOR_GREEN)make env-storage-rewrite$(COLOR_RESET)    Force-regenerate wizard-managed compose services during storage setup\n"
	@printf "  $(COLOR_GREEN)make base$(COLOR_RESET)                   Short form of make env-base (all env prefix can be stripped)\n"
	@printf "\n"
	@printf "$(COLOR_BOLD)Typical workflow$(COLOR_RESET)\n"
	@printf "  1. make dev            # install backend/test deps and build frontend\n"
	@printf "  2. make env-base       # set LLM/embedding/reranker\n"
	@printf "  3. make env-storage    # set storage backends (optional)\n"
	@printf "  4. make env-server     # set port/security/SSL (optional)\n\n"
	@printf "$(COLOR_BOLD)Examples$(COLOR_RESET)\n"
	@printf "  make dev\n"
	@printf "  make env-base\n"
	@printf "  make env-storage SETUP_OPTS=--debug\n"
	@printf "  make env-server\n\n"
	@printf "  make env-storage-rewrite\n\n"
	@printf "  make env-security-check\n\n"
	@printf "$(COLOR_BOLD)Compose Output$(COLOR_RESET)\n"
	@printf "  Bundled service images are defined in scripts/setup/templates/*.yml.\n"
	@printf "  Compose file output: docker-compose.final.yml\n"
	@printf "\n"
	@printf "$(COLOR_BOLD)Apple container stack (macOS 26, Apple Silicon; no Docker)$(COLOR_RESET)\n"
	@printf "  $(COLOR_GREEN)make apple-up$(COLOR_RESET)                Start Postgres/Neo4j/Milvus + LightRAG on Apple 'container'\n"
	@printf "  $(COLOR_GREEN)make apple-down$(COLOR_RESET)              Stop and remove the stack (SETUP_OPTS=--purge also deletes data)\n"
	@printf "  $(COLOR_GREEN)make apple-status$(COLOR_RESET)            Show stack containers, volumes, and networks\n"
	@printf "  $(COLOR_GREEN)make apple-logs SVC=lightrag$(COLOR_RESET) Tail a service's logs\n"
	@printf "  See docs/AppleContainerSetup.md for details.\n"

dev:
	@if ! command -v uv >/dev/null 2>&1; then \
		printf "$(COLOR_YELLOW)uv is required for make dev.$(COLOR_RESET)\n"; \
		printf "Install uv first: https://docs.astral.sh/uv/getting-started/installation/\n"; \
		printf "Unix/macOS: curl -LsSf https://astral.sh/uv/install.sh | sh\n"; \
		printf "Windows: powershell -c \"irm https://astral.sh/uv/install.ps1 | iex\"\n"; \
		exit 1; \
	fi
	@if ! command -v bun >/dev/null 2>&1; then \
		printf "$(COLOR_YELLOW)bun is required for make dev.$(COLOR_RESET)\n"; \
		printf "Install Bun first: https://bun.sh/docs/installation\n"; \
		printf "macOS/Linux: curl -fsSL https://bun.sh/install | bash\n"; \
		printf "Windows: powershell -c \"irm bun.sh/install.ps1 | iex\"\n"; \
		exit 1; \
	fi
	@printf "$(COLOR_BLUE)Syncing backend and test dependencies with uv...$(COLOR_RESET)\n"
	@uv sync --extra test --extra offline
	@printf "$(COLOR_BLUE)Installing frontend dependencies with Bun...$(COLOR_RESET)\n"
	@cd lightrag_webui && bun install --frozen-lockfile
	@printf "$(COLOR_BLUE)Building frontend assets...$(COLOR_RESET)\n"
	@cd lightrag_webui && bun run build
	@printf "$(COLOR_GREEN)Development environment is ready.$(COLOR_RESET)\n"
	@printf "Next steps:\n"
	@printf "  source .venv/bin/activate\n"
	@printf "  make env-base\n"
	@printf "  lightrag-server\n"

env-base env base configure:
	@$(SETUP_BASH) $(SETUP_SCRIPT) --base $(SETUP_OPTS)

env-storage storage:
	@$(SETUP_BASH) $(SETUP_SCRIPT) --storage $(SETUP_OPTS)

env-base-rewrite base-rewrite:
	@$(SETUP_BASH) $(SETUP_SCRIPT) --base --rewrite-compose $(SETUP_OPTS)

env-storage-rewrite storage-rewrite:
	@$(SETUP_BASH) $(SETUP_SCRIPT) --storage --rewrite-compose $(SETUP_OPTS)

env-server server:
	@$(SETUP_BASH) $(SETUP_SCRIPT) --server $(SETUP_OPTS)

env-validate validate:
	@$(SETUP_BASH) $(SETUP_SCRIPT) --validate $(SETUP_OPTS)

env-security-check security security-check:
	@$(SETUP_BASH) $(SETUP_SCRIPT) --security-check $(SETUP_OPTS)

env-backup backup:
	@$(SETUP_BASH) $(SETUP_SCRIPT) --backup $(SETUP_OPTS)

# Apple 'container' stack (macOS 26 + Apple Silicon). SETUP_BASH resolves a
# bash 4+ interpreter, which apple-container.sh requires. Pass flags via
# SETUP_OPTS (e.g. make apple-up SETUP_OPTS=--no-lightrag) and a service name
# via SVC (e.g. make apple-logs SVC=lightrag).
apple-up:
	@$(SETUP_BASH) $(APPLE_SCRIPT) up $(SETUP_OPTS)

apple-down:
	@$(SETUP_BASH) $(APPLE_SCRIPT) down $(SETUP_OPTS)

apple-status:
	@$(SETUP_BASH) $(APPLE_SCRIPT) status

apple-logs:
	@$(SETUP_BASH) $(APPLE_SCRIPT) logs $(SVC) $(SETUP_OPTS)

apple-restart:
	@$(SETUP_BASH) $(APPLE_SCRIPT) restart $(SVC)

apple-pull:
	@$(SETUP_BASH) $(APPLE_SCRIPT) pull

## `SECURITY.md`

# Reporting Security Issues

The LightRAG team and community take security bugs seriously. We appreciate your efforts to responsibly disclose your findings, and will make every effort to acknowledge your contributions.

To report a security issue, please use the GitHub Security Advisory:  [Report a Vulnerability](https://github.com/HKUDS/LightRAG/security/advisories/new)

The LightRAG team will send a response indicating the next steps in handling your report. After the initial reply to your report, the security team will keep you informed of the progress towards a fix and full announcement, and may ask for additional information or guidance.

Report security bugs in third-party modules to the person or team maintaining the module.

### Supported Versions

The following versions currently being supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 1.2.x   | :x:                |
| 1.3.x   | :white_check_mark: |

## `pyproject.toml`

[build-system]
requires = ["setuptools>=64", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "lightrag-hku"
dynamic = ["version"]
authors = [
    {name = "Zirui Guo"}
]
description = "LightRAG: Simple and Fast Retrieval-Augmented Generation"
readme = "README.md"
license = {text = "MIT"}
requires-python = ">=3.10"
classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
dependencies = [
    "aiohttp",
    "configparser",
    "google-api-core>=2.0.0,<3.0.0",
    "google-genai>=1.0.0,<3.0.0",
    "json_repair>=0.59.9,<1.0.0",
    "nano-vectordb",
    "networkx",
    "numpy>=1.24.0,<3.0.0",
    "packaging",
    # pandas 3.0 requires Python >= 3.11 while this project still supports
    # 3.10, so the ceiling is widened instead of the floor being raised:
    # resolvers pick 2.x on 3.10 and 3.x from 3.11 up. Only the Excel branch
    # of aexport_data uses pandas (DataFrame/ExcelWriter/to_excel), all of
    # which are unchanged in 3.x.
    "pandas>=2.0.0,<4.0.0",
    "pipmaster",
    "pydantic",
    "pypinyin",
    "PyYAML>=6.0,<7.0",
    "python-dotenv",
    "setuptools",
    "tenacity",
    # 0.7.0 adds o200k_base, required by the default gpt-4o-mini, and is the
    # oldest release whose encode_batch/decode_batch fan encode()/decode() of
    # one Encoding across threads — the thread safety Tokenizer relies on.
    "tiktoken>=0.7.0",
    # 3.2.0 is the minimum pandas 3.x declares for its xlsxwriter Excel
    # engine (pandas.compat._optional.VERSIONS).
    "xlsxwriter>=3.2.0",
]

[project.optional-dependencies]
# Test framework dependencies (for CI/CD and testing)
pytest = [
    "pytest>=8.4.2",
    "pytest-asyncio>=1.2.0",
    "pre-commit",
    "ruff",
    "httpx2>=2.0.0",  # starlette>=1.3 testclient prefers httpx2 over httpx
]

api = [
    # Core dependencies
    "aiohttp",
    "configparser",
    "json_repair>=0.59.9,<1.0.0",
    "nano-vectordb",
    "networkx",
    "numpy>=1.24.0,<3.0.0",
    "openai>=2.0.0,<4.0.0",
    # pandas 3.0 requires Python >= 3.11 while this project still supports
    # 3.10, so the ceiling is widened instead of the floor being raised:
    # resolvers pick 2.x on 3.10 and 3.x from 3.11 up. Only the Excel branch
    # of aexport_data uses pandas (DataFrame/ExcelWriter/to_excel), all of
    # which are unchanged in 3.x.
    "pandas>=2.0.0,<4.0.0",
    "pipmaster",
    "pydantic",
    "pypinyin",
    "PyYAML>=6.0,<7.0",
    "python-dotenv",
    "setuptools",
    "tenacity",
    # 0.7.0 adds o200k_base, required by the default gpt-4o-mini, and is the
    # oldest release whose encode_batch/decode_batch fan encode()/decode() of
    # one Encoding across threads — the thread safety Tokenizer relies on.
    "tiktoken>=0.7.0",
    # 3.2.0 is the minimum pandas 3.x declares for its xlsxwriter Excel
    # engine (pandas.compat._optional.VERSIONS).
    "xlsxwriter>=3.2.0",
    "google-api-core>=2.0.0,<3.0.0",
    "google-genai>=1.0.0,<3.0.0",
    # API-specific dependencies
    "aiofiles",
    "ascii_colors",
    # asyncio.timeout() (used directly on 3.11+) is Python 3.11+ only;
    # requires-python allows 3.10, which needs this backport instead for
    # the MinerU/Docling result-download wall-clock deadline. Marker keeps
    # it out of 3.11+ installs entirely, where lightrag/parser/external/
    # _common.py never imports it.
    "async-timeout>=4.0.3; python_version < '3.11'",
    "distro",
    "fastapi>=0.108",  # 0.108 adds FastAPI.__call__ scope["root_path"] override; api_prefix relies on it
    "httpcore",
    "httpx>=0.28.1",
    "jiter",
    "bcrypt>=4.0.0",
    "psutil",
    "PyJWT>=2.8.0,<3.0.0",
    "python-jose[cryptography]",
    "cryptography>=48.0.1",        # security floor: GHSA-537c-gmf6-5ccf (via python-jose[cryptography])
    "python-multipart>=0.0.30",    # security floor: CVE-2026-53539
    "starlette>=1.3.1,<2",         # security floor: CVE-2026-54283 / CVE-2026-48818 (transitive via fastapi)
    "pytz",
    "uvicorn",
    "uvicorn-worker",
    "gunicorn",
    # Document processing dependencies (required for API document upload functionality)
    "openpyxl>=3.0.0,<4.0.0",      # XLSX processing
    "pycryptodome>=3.0.0,<4.0.0",  # PDF encryption support
    "pypdf>=6.1.0",                 # PDF processing
    "python-docx>=0.8.11,<2.0.0",  # DOCX processing
    "python-pptx>=0.6.21,<2.0.0",  # PPTX processing
    "cairosvg>=2.5.0,<3.0.0",      # SVG->PNG rasterization for native markdown images
    "defusedxml>=0.7.0,<1.0.0",    # Safer XML parser used by parser/docx
    # Chunking strategies (process_options=R / V); lazy-imported by lightrag.chunker
    "langchain-text-splitters>=0.3,<2",
    "langchain-experimental>=0.3.2,<1",  # >=0.3.2: SemanticChunker gained min_chunk_size
    # NLP runtime for the native docx smart_heading engine parameter
    # (sentence/NER heuristics). Language models are separate wheels pinned in
    # requirements-offline-smart-heading.txt and installed via
    # `lightrag-download-cache --spacy-install`.
    # 3.8.14 and 3.8.15 shipped neither a cp314 wheel nor an sdist, breaking
    # `uv sync --frozen` on Python 3.14; 3.8.16 restored both. Cap below
    # 3.8.17 to stay on 3.8.x until spacy 4.x graduates from dev.
    "spacy>=3.8,<3.8.17",
]

# Offline deployment dependencies (layered design for flexibility)
offline-storage = [
    # Storage backend dependencies
    "faiss-cpu>=1.7.0,<2.0.0",
    "redis>=5.0.1,<9.0.0",
    "neo4j>=5.0.0,<7.0.0",
    "pymilvus>=2.6.2,<4.0.0",
    "pymongo>=4.0.0,<5.0.0",
    "asyncpg>=0.31.0,<1.0.0",
    "pgvector>=0.4.2,<1.0.0",
    "qdrant-client>=1.11.0,<2.0.0",
    "opensearch-py>=3.0.0,<4.0.0",
]

offline-llm = [
    # LLM provider dependencies
    "openai>=2.0.0,<4.0.0",
    "anthropic>=0.18.0,<2.0.0",
    "ollama>=0.5.4,<1.0.0",
    "zhipuai>=2.0.0,<3.0.0",
    "aioboto3>=12.0.0,<16.0.0",
    "voyageai>=0.2.0,<1.0.0",
    "llama-index>=0.14.0,<1.0.0",  # Updated to ensure compatibility with openai 2.x
    "llama-index-llms-openai>=0.6.12",  # Explicitly require version that supports openai 2.x
    "google-api-core>=2.0.0,<3.0.0",
    "google-genai>=1.0.0,<3.0.0",
]

offline = [
    # Complete offline package (includes api for document processing, plus storage and LLM)
    "lightrag-hku[api,offline-storage,offline-llm]",
]

test = [
    "lightrag-hku[api]",
    "pytest>=8.4.2",
    "pytest-asyncio>=1.2.0",
    "pre-commit",
    "ruff",
    "httpx2>=2.0.0",  # starlette>=1.3 testclient prefers httpx2 over httpx
]

evaluation = [
    "lightrag-hku[api]",
    "ragas>=0.3.7",
    "datasets>=4.3.0",
]

observability = [
    # LLM observability and tracing dependencies
    "langfuse>=3.8.1",
]

[project.scripts]
lightrag-repair-chunk-tracking = "lightrag.tools.chunk_tracking_repair:main"
lightrag-server = "lightrag.api.lightrag_server:main"
lightrag-gunicorn = "lightrag.api.run_with_gunicorn:main"
lightrag-hash-password = "lightrag.tools.hash_password:main"
lightrag-download-cache = "lightrag.tools.download_cache:main"
lightrag-clean-llmqc = "lightrag.tools.clean_llm_query_cache:main"
lightrag-rebuild-vdb = "lightrag.tools.rebuild_vdb:main"

[project.urls]
Homepage = "https://github.com/HKUDS/LightRAG"
Documentation = "https://github.com/HKUDS/LightRAG"
Repository = "https://github.com/HKUDS/LightRAG"
"Bug Tracker" = "https://github.com/HKUDS/LightRAG/issues"

[tool.setuptools.packages.find]
include = ["lightrag*"]
exclude = ["data*", "tests*", "scripts*", "examples*", "dickens*", "reproduce*", "output_complete*", "rag_storage*", "inputs*"]

[tool.setuptools]
include-package-data = true

[tool.setuptools.dynamic]
version = {attr = "lightrag._version.__version__"}

[tool.setuptools.package-data]

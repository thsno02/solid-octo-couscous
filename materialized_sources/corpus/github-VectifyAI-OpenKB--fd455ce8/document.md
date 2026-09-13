# Repository semantic capsule: VectifyAI/OpenKB

- Commit: `ff54396e575ee6feb0113b631a34caa082b441cc`
- Default branch: `main`
- Description: VectifyAI/OpenKB
- Selected evidence files: 4 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

<div align="center">

<a href="https://openkb.ai">
  <img src="https://docs.pageindex.ai/images/openkb.png" alt="OpenKB (by PageIndex)" />
</a>

<br />
<br />

<p align="center">
<a href="https://trendshift.io/repositories/26145" target="_blank"><img src="https://trendshift.io/api/badge/repositories/26145" alt="VectifyAI%2FOpenKB | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

# OpenKB: Open LLM Knowledge Base

<p align="center"><i>Scale to long documents  •  Reasoning-based retrieval  •  Native multi-modality  •  No Vector DB</i></p>

</div>

<details open>
<summary><h2>📢 Recent Updates</h2></summary>

- *Google Open Knowledge Format (OKF)*: Wiki pages follow the [Google OKF](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) specification for knowledge sharing.
- *Entity Pages*: People, orgs, places, and products as dedicated wiki pages, auto-extracted and kept in sync.

</details>

---

# 📑 What is OpenKB

**OpenKB (Open Knowledge Base)** is an open-source system (in CLI) that compiles raw documents into a structured, interlinked wiki-style knowledge base using LLMs, powered by [**PageIndex**](https://github.com/VectifyAI/PageIndex)'s vectorless, reasoning-based retrieval for long documents.

The idea is based on a [concept](https://x.com/karpathy/status/2039805659525644595) described by Andrej Karpathy: LLMs generate summaries, concept pages, and cross-references, all maintained automatically. Knowledge compounds over time instead of being re-derived on every query.

### Why not traditional RAG?

Traditional RAG rediscovers knowledge from scratch on every query. Nothing accumulates. OpenKB compiles knowledge once into a persistent wiki, then keeps it current. Cross-references already exist, contradictions are flagged, and synthesis reflects everything consumed.

OpenKB has two layers: a **wiki foundation** that compiles and maintains your knowledge, and **generators** (query / chat / Skill Factory) that turn it into useful output. See [Usage](#️-usage) for the full command list.

### Features

- **Broad format support:** PDF, Word, Markdown, PowerPoint, HTML, Excel, CSV, text, URLs, and more.
- **Scales to long documents:** Long and complex documents are handled via [PageIndex](https://github.com/VectifyAI/PageIndex) tree indexing, enabling accurate, vectorless, context-aware retrieval.
- **Native multi-modality:** Retrieves and understands figures, tables, and images, not just text.
- **Compiled wiki:** The LLM compiles your documents into summaries, concept pages, entity pages, and cross-links, all kept in sync.
- **Query & chat:** One-off questions or multi-turn conversations over your wiki, with persisted sessions to resume.
- **Skill Factory:** Distills redistributable agent skills from your wiki.
- **OKF-ready:** Wiki pages follow the [Google OKF](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) specification for knowledge sharing.
- **Obsidian-compatible:** The wiki is plain `.md` files with cross-links. Opens in Obsidian for graph view.
- **Knowledge Workbench (Web UI):** A bundled web UI served at `/` to browse the KB, upload and compile documents, and stream queries and chats — all in the browser.

# 🚀 Getting Started

### Install

```bash
pip install openkb
```

<details>
<summary><b><i>Other install options:</i></b></summary>

- **Latest from GitHub:**

  ```bash
  pip install git+https://github.com/VectifyAI/OpenKB.git
  ```

- **Install from source** (editable, for development):

  ```bash
  git clone https://github.com/VectifyAI/OpenKB.git
  cd OpenKB
  pip install -e .
  ```

</details>

### Quick Start

```bash
# 1. Create a directory for your knowledge base
mkdir my-kb && cd my-kb

# 2. Initialize the knowledge base
openkb init

# 3. Add documents
openkb add paper.pdf
openkb add ~/papers/                            # Add a whole directory
openkb add https://arxiv.org/pdf/2509.11420     # Or fetch from a URL

# 4. Ask a question
openkb query "What are the main findings?"

# 5. Or chat interactively
openkb chat

# (Optional) Turn the wiki into other outputs
openkb skill new my-expert "Reason like an expert on <your-topic>"   # a portable agent skill
openkb visualize                                                     # an interactive knowledge graph
openkb deck new my-deck "An intro deck on <your-topic>"              # slides — a single-file HTML deck
```

### Set up your LLM

OpenKB supports [multiple LLM providers](https://docs.litellm.ai/docs/providers) (OpenAI, Claude, Gemini, etc.) via [LiteLLM](https://github.com/BerriAI/litellm) (pinned to a [safe version](https://docs.litellm.ai/blog/security-update-march-2026)).

Set your model during `openkb init` or in [`.openkb/config.yaml`](#configuration) using the `provider/model` LiteLLM format (e.g. `anthropic/claude-sonnet-4-6`). OpenAI models can omit the prefix (e.g. `gpt-5.4`).

Create a `.env` file with your LLM API key:

```bash
LLM_API_KEY=your_llm_api_key
```

Subscription-based providers that authenticate via OAuth device flow (e.g. `chatgpt/*`, `github_copilot/*`) need no API key; OpenKB skips the missing-key warning for them.

### Knowledge Workbench (Web UI)

OpenKB ships a bundled web UI, served by the REST API at `/`. Install the API extra and start the server — no configuration needed:

```bash
pip install "openkb[web]"
openkb-web                       # serves the API + Workbench at http://127.0.0.1:7566/
```

Open `http://127.0.0.1:7566/` for the Workbench. Auth is off by default (local-first); set `OPENKB_API_TOKEN` to require a bearer token before exposing the server. See the [full Web UI guide](examples/rest-api/README.md#knowledge-workbench-web-ui).

> Working on the UI itself? Run the Vite dev server with `cd frontend && npm install && npm run dev` (it proxies `/api` to a running `openkb-web`), or `npm run build` to regenerate the bundled `openkb/web/`.

# 🧩 How OpenKB Works

### Architecture

<div align="center">
  <img src="assets/openkb-architecture.webp" alt="OpenKB Architecture: from raw documents (markitdown / PageIndex) through LLM wiki compilation to the wiki/ foundation, powering query/chat, the Skill Factory, and future generators" width="900" />
</div>

### Short vs Long Document Handling

|               | Short documents            | Long documents (PDF ≥ 20 pages)    |
| ------------- | -------------------------- | ---------------------------------- |
| **Convert**   | markitdown → Markdown      | PageIndex → tree index + summaries |
| **Images**    | Extracted inline (pymupdf) | Extracted by PageIndex             |
| **LLM reads** | Full text                  | Document trees                     |
| **Result**    | summary + concepts         | summary + concepts                 |

Short documents are read in full by the LLM. Long PDFs are processed by [PageIndex](https://github.com/VectifyAI/PageIndex) into a hierarchical tree index. The LLM reads the tree instead of the full text, enabling accurate and scalable retrieval for long documents.

### Knowledge Compilation

When you add a document, the LLM:

1. Generates a **summary** page
2. Reads existing **concept** and **entity** pages
3. Creates or updates concepts with cross-document synthesis
4. Creates or updates **entity** pages (people, orgs, places, products)
5. Updates the **index** and **log**

A single source might touch 10--15 wiki pages. Knowledge accumulates: each document enriches the existing wiki rather than sitting in isolation.

# ⚙️ Usage

OpenKB commands fall into two layers: the **wiki foundation** (compile + manage your knowledge) and **generators** (turn that wiki into useful output). Each links to a concrete walkthrough — a real artifact OpenKB generated from one sample paper (browse them all in [`examples/`](examples/)).

## Layer 1: 🧱 Wiki Foundation — compile and maintain

| Command                                                      | Description                                                                             |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| `openkb init`                                                | Initialize a new knowledge base (interactive)                                           |
| <code>openkb&nbsp;add&nbsp;&lt;file_or_dir_or_URL&gt;</code> | Add files, directories, or URLs and compile to wiki (URL content type is auto-detected) |
| `openkb list`                                                | List indexed documents and concepts                                                     |
| `openkb status`                                              | Show knowledge base stats                                                               |
| `openkb watch`                                               | Watch `raw/` and auto-compile new files                                                 |
| `openkb lint`                                                | Run structural and knowledge health checks                                              |

<details>
<summary><i>More wiki commands:</i></summary>
<br>

| Command                                                            | Description                                                                                                                                                                                                                          |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <code>openkb&nbsp;remove&nbsp;&lt;doc&gt;</code>                   | Remove a document and clean up its wiki pages, images, registry, and PageIndex state (`--dry-run` to preview, `--keep-raw` / `--keep-empty` to retain artifacts)                                                                     |
| <code>openkb&nbsp;recompile&nbsp;[&lt;doc&gt;]&nbsp;[--all]</code> | Re-run the compile pipeline on already-indexed docs without re-indexing. Regenerates summaries and rewrites concept pages; manual edits are overwritten (`--dry-run` to preview, `--refresh-schema` to also update `wiki/AGENTS.md`) |
| <code>openkb&nbsp;feedback&nbsp;["msg"]</code>                     | File feedback by opening a prefilled GitHub issue (`--type bug/feature/question` to tag it)                                                                                                                                          |

</details>

→ **Example:** the everyday loop walked through end to end — [`examples/commands/`](examples/commands/).

## Layer 2: 💡 Generators — turn the wiki into output

A "generator" reads from the compiled wiki and produces something usable: an answer, a conversation, a skill folder. The wiki is the substrate; generators are the surfaces.

| Command                                                                               | Output                                                                                                         | Example                            |
| ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| <code>openkb&nbsp;query&nbsp;"question"</code>                                        | A grounded answer with citations (`--save` to persist to `wiki/explorations/`)                                 | [query & save](examples/commands/) |
| <code>openkb&nbsp;chat</code>                                                         | Interactive multi-turn session over the wiki (`--resume`, `--list`, `--delete` to manage sessions)             | [chat](examples/chat/)             |
| <code>openkb&nbsp;visualize</code>                                                    | A self-contained interactive knowledge graph at `output/visualize/graph.html` — 3D, mind-map, and radial views | [visualize](examples/visualize/)   |
| <code>openkb&nbsp;skill&nbsp;new&nbsp;&lt;skill-name&gt;&nbsp;"&lt;intent&gt;"</code> | Distill a redistributable agent skill from your wiki (see [Skill Factory](#skill-factory) below)               | [skills](examples/skills/)         |
| <code>openkb&nbsp;deck&nbsp;new&nbsp;&lt;name&gt;&nbsp;"&lt;intent&gt;"</code>        | Generate a single-file HTML slide deck (`--skill` picks a theme, `--critique` runs a quality pass)             | [slides](examples/slides/)         |

### (i) 💬 Query & Chat — *ask the wiki*

`openkb query "..."` answers a single question with a grounded, cited answer from your wiki. `openkb chat` is interactive, an ongoing multi-turn session over the same wiki (`--resume`, `--list`, `--delete` to manage sessions). → Walked through with real saved output in **[`examples/commands/`](examples/commands/)** (query) and **[`examples/chat/`](examples/chat/)** (chat).

Inside a chat, type `/` to access slash commands (Tab to complete).

<details>
<summary><i>More slash commands:</i></summary>
<br>

- `/help`: list available commands
- `/status`: show knowledge base status
- `/list`: list all documents
- `/add <path>`: add a document or directory without leaving the chat
- `/skill new <skill-name> "<intent>"`: compile a skill from this chat (see below)

## `AGENTS.md`

# AGENTS.md — OpenKB map for coding agents

OpenKB compiles raw documents into an interlinked wiki knowledge base using
LLMs (vectorless retrieval via PageIndex). This repo is developed **agent-first**:
humans steer, agents execute. Optimize changes for agent legibility.

## Read next
- `docs/golden-principles.md` — mechanical rules to follow (enforced where possible).
- `docs/internal/superpowers/{specs,plans}/` — design history & plans *(maintainer-local, not in git)*.
- `README.md` — user-facing overview and commands.

## Dev commands
- Install: `pip install -e ".[dev]"`  (or `uv sync --extra dev` — plain `uv sync` skips the dev tools)
- Run CLI: `openkb <command>`  (entry point: `openkb.cli:cli`)
- Test: `pytest`
- Lint/format/types: `ruff check .` · `ruff format .` · `mypy openkb`

## Module map (openkb/)
- `cli.py` — Click CLI entry point & command wiring *(large; see tech-debt)*.
- `config.py` — config loading/validation (LiteLLM passthrough, env).
- `converter.py` — document → markdown conversion (markitdown).
- `url_ingest.py` — fetch & ingest URLs (trafilatura).
- `images.py` — figure/image extraction & handling.
- `indexer.py` — PageIndex tree indexing for long docs.
- `mutation.py` — crash-safe, serial KB mutations.
- `locks.py` — atomic writes / file locking (`atomic_write_text`, portalocker).
- `state.py` — run/session state tracking.
- `frontmatter.py` — YAML frontmatter round-trip (OKF).
- `schema.py` — page/content schema constants & helpers.
- `lint.py` — structural wiki lint (broken links, orphans, index sync).
- `tree_renderer.py`, `visualize.py`, `watcher.py` — rendering / graph / file watch.
- `agent/compiler.py` — LLM wiki compiler *(large; see tech-debt)*.
- `agent/linter.py` — semantic (LLM) wiki lint (contradictions, gaps, staleness).
- `agent/chat.py`, `agent/chat_session.py` — chat over the wiki *(chat.py large)*.
- `agent/query.py` — one-off query generator.
- `agent/tools.py` — shared wiki read/write tool functions used by query/linter (and by chat indirectly via `query.build_chat_agent`).
- `agent/skills.py`, `agent/skill_runner.py`, `skill/` — Skill Factory.
- `deck/`, `templates/`, `prompts/` — deck output, templates, prompt assets.

## Hard invariants
- Deps are pinned **exactly** (supply-chain caution). Vet before bumping.
- Wiki writes go through `locks.py` / `mutation.py` (never ad-hoc).
- Modules stay < 800 lines (`tests/test_file_size.py`); grandfathered files are in tech-debt.
- Keep this file a short map — put depth in `docs/`.

## `CLAUDE.md`

@AGENTS.md

## `pyproject.toml`

[build-system]
requires = ["hatchling", "hatch-vcs"]
build-backend = "hatchling.build"

[project]
name = "openkb"
dynamic = ["version"]
description = "OpenKB: Open LLM Knowledge Base, powered by PageIndex"
readme = "README.md"
requires-python = ">=3.10"
license = {text = "Apache-2.0"}
authors = [
    {name = "Kylin", email = "quanqi@pageindex.ai"},
    {name = "Ray", email = "ray@vectify.ai"},
]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
]
keywords = ["ai", "rag", "retrieval", "knowledge-base", "llm", "pageindex", "agents", "document"]
# All dependencies are pinned exactly (supply-chain caution — e.g. the
# litellm package-poisoning incident). Bump deliberately after vetting
# each release.
# litellm 1.87.2 fixes the chatgpt/* (ChatGPT subscription) provider
# returning empty Responses output (BerriAI/litellm#25429) and
# auto-injects GitHub Copilot IDE-auth headers.
dependencies = [
    "pageindex==0.3.0.dev3",
    "markitdown[docx,pptx,xlsx,xls]==0.1.5",
    "trafilatura==2.0.0",
    "click==8.4.0",
    "watchdog==6.0.0",
    "litellm==1.87.2",
    "openai-agents==0.17.3",
    # openai 2.45.0 added a required `cache_write_tokens` field to
    # InputTokensDetails that openai-agents 0.17.3 does not set, crashing
    # usage parsing on every response (issue #187). Pin below 2.45 until
    # openai-agents catches up.
    "openai==2.44.0",
    "pyyaml==6.0.3",
    "python-dotenv==1.2.2",
    "json-repair==0.59.10",
    "prompt_toolkit==3.0.52",
    "rich==15.0.0",
    "portalocker==3.2.0",
]

[project.urls]
Repository = "https://github.com/VectifyAI/OpenKB"
Homepage = "https://github.com/VectifyAI/OpenKB"
Issues = "https://github.com/VectifyAI/OpenKB/issues"

[project.scripts]
openkb = "openkb.cli:cli"
openkb-web = "openkb.api:main"
# Backwards-compatible alias for the historical name; same entry point.
openkb-api = "openkb.api:main"

[tool.pytest.ini_options]
testpaths = ["tests"]

[project.optional-dependencies]
dev = [
    "pytest==9.0.3",
    "pytest-asyncio==1.3.0",
    "httpx",
    "ruff==0.9.7",
    "mypy==1.15.0",
    "types-PyYAML==6.0.12.20260518",
]
# The Knowledge Workbench Web UI is served by this FastAPI server. `web` is the
# canonical extra; `api` is a backwards-compatible alias so an existing
# `pip install "openkb[api]"` keeps working.
web = ["fastapi", "uvicorn", "python-multipart"]
api = ["openkb[web]"]

[tool.hatch.version]
source = "vcs"

# The Workbench web bundle (openkb/web) is git-ignored but must ship in the
# published package. `artifacts` force-includes it into both the sdist and the
# wheel when present (built by `npm run build`, e.g. in release CI). When it is
# absent the build still succeeds — the API server just serves no UI.
[tool.hatch.build]
artifacts = ["openkb/web/**"]

[tool.hatch.build.targets.wheel]
packages = ["openkb"]

# Bundle the built-in deck themes + html critic into the wheel so
# `openkb deck new` / `--critique` / chat `/deck` work right after
# `pip install` (scan_local_skills also looks under openkb/_skills/).
[tool.hatch.build.targets.wheel.force-include]
"skills/openkb-deck-neon" = "openkb/_skills/openkb-deck-neon"
"skills/openkb-deck-editorial" = "openkb/_skills/openkb-deck-editorial"
"skills/openkb-html-critic" = "openkb/_skills/openkb-html-critic"

[tool.ruff]
target-version = "py310"
line-length = 100

[tool.ruff.lint]
# Start conservative (pyflakes + pycodestyle errors + isort); ratchet up later.
select = ["E", "F", "I"]

[tool.ruff.lint.per-file-ignores]
# cli.py deliberately interleaves imports with side-effecting setup code
# (warning filters that must apply before `markitdown`/`litellm` import,
# `set_tracing_disabled()` before other agents-SDK usage, an
# `os.environ.setdefault(...)` that must run before `import litellm`).
# Reordering to satisfy E402/I001 would risk changing import-time behavior,
# so both are ignored here rather than fixed.
#
# E501 (line-too-long) is scoped to the files whose remaining violations are
# long string literals (docstrings, CLI help text, prompt templates) that
# reflowing would either fail to shorten or would alter user-facing text.
# Everywhere else the 100-column limit is enforced. Shrink this list by
# rewrapping the literals (or adding targeted `# noqa: E501`) over time.
"openkb/cli.py" = ["E402", "I001", "E501"]
"openkb/agent/chat.py" = ["E501"]
"openkb/agent/compiler.py" = ["E501"]
"openkb/lint.py" = ["E501"]
"openkb/schema.py" = ["E501"]
# Test fixtures asserting exact file contents (frontmatter/index literals);
# rewrapping the strings would change the data under test.
"tests/test_cli.py" = ["E501"]
"tests/test_compiler.py" = ["E501"]
"tests/test_remove.py" = ["E501"]

[tool.mypy]
python_version = "3.10"
files = ["openkb"]
# Lenient to start (codebase not previously type-checked); ratchet up over time.
ignore_missing_imports = true
# numpy's bundled stubs (reached transitively via litellm/openai-agents ->
# pydantic, not imported by openkb directly) use `type X = ...` alias
# statements requiring Python 3.12+ parser support — fatal to the whole run
# (a [syntax] error, not a suppressible diagnostic) when they get parsed. A
# per-module `follow_imports = "skip"` override was experimentally confirmed
# NOT to prevent the parse; only the global default reliably avoids reaching
# that stub, so it stays global rather than scoped narrower.
follow_imports = "skip"

# Pre-existing untyped-data debt is suppressed PER MODULE below (not
# globally), so every other module gets full checking for these error codes.
# Ratchet: fix a module's errors (mostly by giving LLM-JSON payloads proper
# TypedDict/dataclass shapes), then delete its override block.

[[tool.mypy.overrides]]
# Loosely-shaped dict/list data parsed from LLM JSON output flows through
# `Any`-typed helpers: union-attr on Any|None, unannotated accumulator lists,
# argument/return mismatches against str-typed signatures.
module = "openkb.agent.compiler"
disable_error_code = [
    "arg-type",
    "dict-item",
    "operator",
    "return-value",
    "union-attr",
    "var-annotated",
]

[[tool.mypy.overrides]]
module = "openkb.cli"
disable_error_code = ["return-value"]

[[tool.mypy.overrides]]
module = ["openkb.lint", "openkb.indexer"]
disable_error_code = ["arg-type"]

[[tool.mypy.overrides]]
module = "openkb.skill.workspace"
disable_error_code = ["type-var"]

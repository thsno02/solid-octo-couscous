# Repository semantic capsule: emakhov/llm-wiki-agent

- Commit: `4d4353dc38a6b57b9e661c8b644ec9e4727be4c4`
- Default branch: `main`
- Description: emakhov/llm-wiki-agent
- Selected evidence files: 3 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

# LLM Wiki Agent

A personal knowledge base maintained by an AI agent. You add source documents, the agent builds and maintains a structured, interlinked wiki of markdown files.

Inspired by Andrej Karpathy's [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) concept. Built with [Agno](https://github.com/agno-agi/agno) and [AgentOS](https://docs.agno.com/agent-os/overview).

## How it works

1. **Add sources** — drop articles, papers, or notes into `knowledge-base/sources/` (e.g. via [Obsidian Web Clipper](https://obsidian.md/clipper))
2. **Ingest** — tell the agent to process a source. It reads the document, creates summary and entity pages, updates cross-references, and logs the operation
3. **Query** — ask questions. The agent searches the wiki, reads relevant pages, and synthesizes answers with citations. Good answers get filed back as wiki pages
4. **Lint** — ask the agent to health-check the wiki. It finds orphan pages, broken links, and missing cross-references

The wiki lives in `knowledge-base/` and is fully compatible with [Obsidian](https://obsidian.md) — open it as a vault to browse pages and view the graph.

## Architecture

```
knowledge-base/     # Obsidian vault (open this as your vault)
  sources/          # Immutable source documents (you manage these)
  index.md          # Catalog of all pages
  log.md            # Chronological operations log
  overview.md       # KB overview
  .obsidian/        # Obsidian config
wiki_agent/         # Agent code
  main.py           # AgentOS entry point (serves at localhost:7777)
  agent.py          # Agent definition with tools
  config.py         # LLM model selection
  tools/            # Custom WikiTools toolkit
  prompts/          # Agent instructions
```

## Prerequisites

- [uv](https://docs.astral.sh/uv/) (Python package manager)
- [Docker](https://www.docker.com/) (for PostgreSQL)
- An API key for [Anthropic](https://console.anthropic.com/), [OpenAI](https://platform.openai.com/), or [OpenRouter](https://openrouter.ai/)

## Setup

```bash
# 1. Start PostgreSQL + pgvector
docker compose up -d

# 2. Install dependencies
uv sync

# 3. Configure environment
cp .env .env.local  # optional — edit .env directly
# Set your API key:
#   ANTHROPIC_API_KEY=sk-ant-...
# Or for OpenAI:
#   LLM_PROVIDER=openai
#   OPENAI_API_KEY=sk-...
# Or for OpenRouter:
#   LLM_PROVIDER=openrouter
#   OPENROUTER_API_KEY=sk-or-...

# 4. Start the agent
uv run python -m wiki_agent.main
```

Open [http://localhost:7777](http://localhost:7777) — you'll see two agents:
- **Query Agent** — answers questions from the wiki (read-only)
- **Maintainer Agent** — ingests sources, creates/updates pages, lints the wiki

## Usage

### Ingest a source

Drop a markdown file into `knowledge-base/sources/`, then tell the **Maintainer Agent**:

> Ingest article-title.md

The agent will:
- Read the source document
- Create a summary page in the wiki
- Create or update entity/concept pages
- Add cross-references between pages
- Update `index.md` and `log.md`

### Query the wiki

Open the **Query Agent** and ask any question:

> What are the key differences between X and Y?

The agent searches the wiki index, reads relevant pages, and synthesizes an answer. If the answer is substantial, it offers to save it as a new wiki page.

### Lint the wiki

Tell the **Maintainer Agent**:

> Lint the wiki

It scans for orphan pages, broken links, pages missing from the index, and other issues.

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `LLM_PROVIDER` | `claude` | `claude`, `openai`, or `openrouter` |
| `LLM_MODEL` | per-provider default | Model ID override |
| `ANTHROPIC_API_KEY` | — | Required if using Claude |
| `OPENAI_API_KEY` | — | Required if using OpenAI |
| `OPENROUTER_API_KEY` | — | Required if using OpenRouter |
| `DATABASE_URL` | `postgresql+psycopg://ai:ai@localhost:5532/ai` | PostgreSQL connection |
| `LANGFUSE_ENABLED` | `false` | Set to `true` to enable Langfuse tracing |
| `LANGFUSE_PUBLIC_KEY` | — | Langfuse public key |
| `LANGFUSE_SECRET_KEY` | — | Langfuse secret key |
| `LANGFUSE_BASE_URL` | `https://cloud.langfuse.com` | Langfuse endpoint |

## Tips

- Open `knowledge-base/` as an Obsidian vault — sources and wiki pages live together
- **Obsidian Web Clipper** converts web articles to markdown — clip directly into `knowledge-base/sources/`
- **Obsidian graph view** shows the shape of your wiki: hubs, orphans, connections
- The wiki is just a git repo of markdown files — you get version history for free
- Ingest sources one at a time and stay involved for best results

## `CLAUDE.md`

# LLM Wiki Agent

## Project Overview

Personal knowledge base system where an AI agent (Agno + AgentOS) maintains a structured wiki. The user adds source documents to `sources/`, the agent processes them into interlinked wiki pages in `knowledge-base/`.

## Architecture

The entire `knowledge-base/` directory is an Obsidian vault:
- **`knowledge-base/sources/`** — Immutable source documents. Added by the user (e.g. via Obsidian Web Clipper). The agent reads but NEVER modifies these.
- **`knowledge-base/`** (root) — LLM-generated wiki pages. The agent owns these: creates pages, updates them, maintains cross-references.
- **`wiki_agent/`** — Python agent code using Agno framework + AgentOS runtime.

## Tech Stack

- **Agno** — agent framework (Agent, Toolkit, FileTools)
- **AgentOS** — production runtime with web UI at localhost:7777
- **PostgreSQL + pgvector** — session persistence, vector search
- **uv** — package manager (`uv sync`, `uv run`)

## Key Files

- `wiki_agent/main.py` — AgentOS entry point, initializes Langfuse tracing, creates both agents + knowledge base, serves the app
- `wiki_agent/tracing.py` — Langfuse setup via OpenInference/OpenTelemetry (enabled by `LANGFUSE_ENABLED=true`)
- `wiki_agent/agent.py` — Two agent factories: `create_query_agent()` (read-only wiki access) and `create_maintainer_agent()` (full read/write + ingest/lint)
- `wiki_agent/config.py` — LLM provider selection via `LLM_PROVIDER` env var (claude/openai)
- `wiki_agent/tools/wiki_tools.py` — Custom Toolkit: `list_sources`, `read_source`, `get_wiki_index`, `append_to_log`, `lint_wiki`. Sources dir is `knowledge-base/sources/`.
- `wiki_agent/prompts/instructions.py` — Separate instruction sets: `QUERY_AGENT_INSTRUCTIONS` and `MAINTAINER_AGENT_INSTRUCTIONS`
- `knowledge-base/index.md` — Wiki page catalog (table: Page | Type | Summary | Last Updated)
- `knowledge-base/log.md` — Append-only operations log

## Wiki Conventions

### Page Types
- **summary** — One per source document. Title, summary, key takeaways, source citation.
- **entity** — One per person, organization, or place. Accumulates info across sources.
- **concept** — One per abstract topic. Evolves as sources add depth.
- **comparison** — Side-by-side analysis of entities/concepts.
- **analysis** — Synthesized answers to user questions, filed back into the wiki.
- **overview** — High-level overview of the knowledge base.

### Filenames
- Lowercase kebab-case: `attention-mechanism.md`, `openai-summary.md`
- Summary pages: `<source-name>-summary.md`

### Page Structure
```markdown
# Page Title

Content here. Cross-reference with [Other Page](other-page.md).

## Sources
- [source-filename.md](sources/source-filename.md)
```

### Special Files
- **`index.md`** — Catalog of all pages. Table format: Page | Type | Summary | Last Updated.
- **`log.md`** — Append-only operations log. Timestamped entries.
- **`overview.md`** — High-level description of the knowledge base.

### Cross-References
- Use `[Display Text](filename.md)` format (standard markdown, Obsidian-compatible).
- Every entity/concept page should link to related pages.
- When new information contradicts existing content, note it explicitly and cite both sources.

## Commands

```bash
docker compose up -d              # Start PostgreSQL
uv sync                           # Install dependencies
uv run python -m wiki_agent.main  # Start AgentOS at localhost:7777
```

## Environment Variables
- `LLM_PROVIDER` — `claude`, `openai`, or `openrouter` (default: `claude`)
- `LLM_MODEL` — Model ID override (default depends on provider: `claude-sonnet-4-20250514`, `gpt-4o`, or `anthropic/claude-sonnet-4`)
- `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` / `OPENROUTER_API_KEY` — API keys
- `DATABASE_URL` — PostgreSQL connection (default: `postgresql+psycopg://ai:ai@localhost:5532/ai`)
- `LANGFUSE_ENABLED` — `true` to enable Langfuse tracing (default: `false`)
- `LANGFUSE_PUBLIC_KEY` / `LANGFUSE_SECRET_KEY` — Langfuse API keys
- `LANGFUSE_BASE_URL` — Langfuse endpoint (default: `https://cloud.langfuse.com`)

## Development Notes

- Sources are read-only to the agent — `WikiTools.read_source` provides access but no write tool exists for `knowledge-base/sources/`
- `FileTools` is scoped to `knowledge-base/` for wiki page creation/editing
- `sources/` lives inside `knowledge-base/` so the entire vault is one Obsidian workspace
- `WikiTools` handles structured operations: log is always append-only with timestamps, lint does systematic scanning
- Agent instructions in `prompts/instructions.py` encode the full ingest/query/lint workflows

## `pyproject.toml`

[project]
name = "llm-wiki-agent"
version = "0.1.0"
description = "LLM Wiki — a personal knowledge base maintained by an AI agent"
requires-python = ">=3.11"
dependencies = [
    "agno[postgres]",
    "anthropic",
    "fastapi>=0.135.3",
    "openai",
    "openinference-instrumentation-agno>=0.1.30",
    "opentelemetry-exporter-otlp-proto-http>=1.41.0",
    "opentelemetry-sdk>=1.41.0",
    "pgvector",
    "psycopg[binary]",
    "python-dotenv",
    "sqlalchemy>=2.0.49",
    "uvicorn>=0.44.0",
]

[project.scripts]
wiki-agent = "wiki_agent.main:main"

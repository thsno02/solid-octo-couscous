# Repository semantic capsule: xoai/sage-wiki

- Commit: `ab36031ace701fb1e3c620323d138a90a450f48d`
- Default branch: `main`
- Description: xoai/sage-wiki
- Selected evidence files: 4 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

**English** | [中文](docs/translations/README_zh.md) | [日本語](docs/translations/README_ja.md) | [한국어](docs/translations/README_ko.md) | [Tiếng Việt](docs/translations/README_vi.md) | [Français](docs/translations/README_fr.md) | [Русский](docs/translations/README_ru.md)

# sage-wiki

**sage-wiki** is a graph memory and knowledge base that AI agents and humans build and query together. Drop in documents; an LLM compiler turns them into an interlinked wiki with a knowledge graph — agents query it through MCP, humans browse it as plain markdown. Enable the opt-in graph passes and it becomes an *evidenced* graph: typed entities, provenance-bearing relations, resolved aliases, and per-fact citations on answers. One Go binary scales it from a personal vault to a team hub to a company knowledge graph.

**→ Get started: [Install](#install) · [Quickstart](#quickstart)**

Grown from [Andrej Karpathy's idea](https://x.com/karpathy/status/2039805659525644595) of an LLM-compiled personal knowledge base, built with the [Sage Framework](https://github.com/xoai/sage). Some lessons learned along the way [here](https://x.com/xoai/status/2040936964799795503).

- **Graph memory with citations.** Ask relational questions through `wiki_graph_query` — answers are grounded only in serialized graph edges; with the evidenced graph enabled, each citation carries its source document and confidence.
- **Built for agents and humans.** 19 MCP tools plus generated skill files teach agents when to search, capture, and compile; humans get Obsidian-native markdown, a TUI, and a web UI over the same data.
- **Trust and provenance.** Query outputs quarantine until verified; every evidenced relation records which document asserted it.
- **Your sources in, a wiki out.** The compile pipeline reads papers, notes, code, and email; summarizes; extracts concepts; and writes interconnected articles — the ingestion layer for everything above. Every new source enriches existing articles; the wiki compounds as it grows.
- **Ask your wiki questions.** Hybrid chunk-level search with LLM query expansion, re-ranking, and graph-aware context assembly returns cited answers.
- **Scales to 100K+ documents.** Tiered compilation indexes everything fast and spends LLM budget only where it matters.

https://github.com/user-attachments/assets/c35ee202-e9df-4ccd-b520-8f057163ff26

_Dots on the outer boundary represent summaries of all documents in the knowledge base, while dots in the inner circle represent concepts extracted from the knowledge base, with links showing how those concepts connect to one another._

## From personal vault to company knowledge graph

- **Personal** — overlay an existing Obsidian vault (`init --vault`), run on [local models](docs/guides/local-models.md) for zero cost, and opt into the graph passes (`ontology.triples` + `ontology.resolve`) when you want the evidenced graph.
- **Team** — share one wiki via git or a [self-hosted server](docs/guides/self-hosted-server.md), review entity-resolution proposals and [output trust](docs/guides/output-trust.md) together, and federate multiple wikis with the hub. See [Team Setup](docs/guides/team-setup.md).
- **Company** — move storage to [PostgreSQL/pgvector](docs/guides/storage-backends.md), turn on [metrics](docs/guides/metrics.md), front the server with auth, and scale ingestion with [tiered compilation](docs/guides/large-vault-performance.md).

## Knowledge graph & graph memory

![sage-wiki graph engine](assets/sage-wiki-graph-engine.png)

Vector search retrieves passages that *look like* the query. A graph also
records **how things relate**, so a question needing two or three hops is
answered by traversal instead of hoping one chunk happens to contain the whole
chain. sage-wiki builds that graph as a compile output — not a second database
you have to keep in sync.

- **Entities and typed relations.** Each compile extracts entities (concepts,
  sources, artifacts) and links them with typed relations. The relation
  vocabulary is yours to define — see
  [configurable relations](docs/guides/configurable-relations.md).
- **Evidenced edges.** A relation can carry `evidence` (the span that supports
  it), `confidence` (0–1), and `source_doc`, so a conclusion traces to the
  sentence that justified the edge rather than to a whole document.
- **Triples.** An optional structured-output pass extracts
  subject → relation → object directly. Opt-in (`ontology.triples`): it adds
  one LLM call per document, and defaults never spend your key without asking.
- **Entity resolution.** "K8s" and "Kubernetes" become one node. Proposals are
  review-gated by default rather than silently merged.
- **Concept curation.** One opt-in pass (`dedup_strategy: "llm"`) sees the whole
  proposed concept set at once — the only stage with global view — and judges
  keep / fold / drop per concept. Semantic restatements fold (aliases and
  sources merge), enumerated entities never fold (`mw-3` is not `mw-2`, at any
  similarity), and drops stay logged proposals until `llm_dedup.allow_drop`
  opts in. The judgment prompt is workspace-overridable
  (`prompts/curate-concepts.md`).

**The graph is a retrieval channel, not a side view.** Every search fuses three
channels — lexical (BM25), vector, and graph proximity: query terms seed
entities, a bounded traversal ranks their neighborhood, and the three fuse at
`search.hybrid_weight_graph`. An empty ontology costs nothing and leaves
results byte-identical, so the graph earns its place incrementally.

Query it directly, or let an agent do it over MCP:

```bash
sage-wiki ontology query --entity kubernetes --depth 3 --direction both
sage-wiki provenance "service mesh"    # which sources produced this concept
```

Edges are bi-temporal: contradicting a fact invalidates the old edge instead
of colliding, default answers are contradiction-free, and `as_of` queries
answer "what did we believe in January?" Ambiguous contradictions still
surface through [output trust](docs/guides/output-trust.md) review. For
corpus-wide questions ("main themes across everything?"), opt-in community
detection (`ontology.communities.enabled`) generates cached community
summaries and answers via `wiki_graph_query` `mode: "global"`. Depth
and mechanics: [graph memory](docs/guides/graph-memory.md).

## Guides

| Guide | Description |
|-------|-------------|
| [Agent Memory Layer](docs/guides/agent-memory-layer.md) | MCP setup, skill files, capture workflows, read-capture-evolve loop |
| [HTTP API](docs/guides/http-api.md) | The /v1 REST surface: auth, error model, idempotency, async jobs |
| [Graph Memory](docs/guides/graph-memory.md) | Evidenced relations, triple extraction, entity resolution, graph QA |
| [Configuration](docs/guides/configuration.md) | The full annotated config.yaml, multi-provider setup, serve worker |
| [Team Setup](docs/guides/team-setup.md) | Git-synced, shared server, and hub federation deployment patterns |
| [Search Quality](docs/guides/search-quality.md) | Chunk indexing, query expansion, re-ranking, graph expansion, ANN |
| [Large Vault Performance](docs/guides/large-vault-performance.md) | Tiered compilation, backpressure, code parsers, 100K+ scaling |
| [Output Trust](docs/guides/output-trust.md) | Grounding verification, consensus, promotion/demotion lifecycle |
| [Subscription Auth](docs/guides/subscription-auth.md) | OAuth login, token import, credential management |
| [Self-Hosted Server](docs/guides/self-hosted-server.md) | Docker Compose, Syncthing, reverse proxy, VPS deployment |
| [Storage Backends](docs/guides/storage-backends.md) | SQLite vs PostgreSQL/pgvector setup, switching, pool sizing |
| [Configurable Relations](docs/guides/configurable-relations.md) | Custom ontology types, multilingual synonyms, type restrictions |
| [Customizing Prompts](docs/guides/customizing-prompts.md) | Prompt scaffolding, per-type overrides, custom frontmatter fields |
| [Local Models](docs/guides/local-models.md) | Ollama setup, GPU/CPU routing, per-pass model config |
| [Metrics](docs/guides/metrics.md) | Log snapshots, /metrics endpoint, cardinality controls |
| [Webhooks](docs/webhooks.md) | HMAC-signed event delivery, signature recipe, retry/dead-letter |
| [Security](docs/security.md) | Threat model, the limits table, prompt boundary, residual risks |
| [Contribution Packs](CONTRIBUTING.md) | Creating packs, parser authoring, registry submission |

## Install

```bash
# CLI only (no web UI)
go install github.com/xoai/sage-wiki/cmd/sage-wiki@latest

# With web UI (requires Node.js for building frontend assets)
git clone https://github.com/xoai/sage-wiki.git && cd sage-wiki
cd web && npm install && npm run build && cd ..
go build -tags webui -o sage-wiki ./cmd/sage-wiki/
```

## Quickstart

![Compiler Pipeline](assets/sage-wiki-compiler-pipeline.png)

### Greenfield (new project)

```bash
sage-wiki init my-wiki && cd my-wiki
# Add sources to raw/
cp ~/papers/*.pdf raw/
# Edit config.yaml to add api key, and pick LLMs
sage-wiki compile                                  # first compile
sage-wiki compile                                  # second: zero LLM calls — unchanged docs are skipped
sage-wiki compile --explain raw/paper.pdf          # why a doc compiles or skips
sage-wiki compile --force                          # recompile everything regardless
sage-wiki search "attention mechanism"             # hybrid search
sage-wiki query "How does flash attention work?"   # cited Q&A
sage-wiki tui                                      # terminal dashboard
sage-wiki serve --ui                               # browser (webui build)
sage-wiki compile --watch                          # watch folder
```

Every `config.yaml` key, annotated line by line: [Configuration](docs/guides/configuration.md).

**Project layout** (what `init` creates — selected entries, illustrative not exhaustive):

```
my-wiki/
├── config.yaml           # providers, models, compiler, search, ontology
├── raw/                  # drop sources here (articles, papers, code, images)
├── wiki/                 # compiled output — Obsidian-compatible markdown
│   ├── summaries/        # per-source LLM summaries
│   ├── concepts/         # concept articles (the knowledge graph)
│   ├── images/           # vision-captioned image descriptions
│   ├── outputs/          # filed query answers (trust.include_outputs: "true")
│   ├── under_review/     # filed answers awaiting trust review (default)
│   └── archive/          # pruned articles
├── .sage/wiki.db         # one SQLite file: FTS index, vectors, ontology, queue
└── .manifest.json        # source↔article mapping + compile state
```

### Vault Overlay (existing Obsidian vault)

```bash
cd ~/Documents/MyVault
sage-wiki init --vault
# Edit config.yaml to set source/ignore folders, add api key, pick LLMs
sage-wiki compile --watch
```

Prefer containers? Prebuilt multi-arch Docker images and compose files are
covered in the [self-hosted server guide](docs/guides/self-hosted-server.md).

## Supported Source Formats

| Format      | Extensions                              | What gets extracted                                         |
| ----------- | --------------------------------------- | ----------------------------------------------------------- |
| Markdown    | `.md`                                   | Body text with frontmatter parsed separately                |
| PDF         | `.pdf`                                  | Full text via pure-Go extraction                            |
| Word        | `.docx`                                 | Document text from XML                                      |
| Excel       | `.xlsx`                                 | Cell values and sheet data                                  |
| PowerPoint  | `.pptx`                                 | Slide text content                                          |
| CSV         | `.csv`                                  | Headers + rows (up to 1000 rows)                            |
| EPUB        | `.epub`                                 | Chapter text from XHTML                                     |
| Email       | `.eml`                                  | Headers (from/to/subject/date) + body                       |
| Plain text  | `.txt`, `.log`                          | Raw content                                                 |
| Transcripts | `.vtt`, `.srt`                          | Raw content                                                 |
| Images      | `.png`, `.jpg`, `.gif`, `.webp`, `.svg`, `.bmp` | Description via vision LLM (caption, content, visible text) |
| Code        | `.go`, `.py`, `.js`, `.ts`, `.rs`, etc. | Source code                                                 |

Just drop files into your source folder — sage-wiki detects the format automatically. Images require a vision-capable LLM (Gemini, Claude, GPT-4o). Need a format not listed? sage-wiki supports [external parsers](#external-parsers) — scripts in any language reading stdin, writing text to stdout.

**Custom source types.** Set `type:` on a source root in `config.yaml` and pair it with `prompts/summarize-{type}.md` to give any format — PDFs and Office documents included — its own summary prompt and `source_type` frontmatter. (`image` and `code` sources keep their built-in types — they select the vision and code pipelines, not a prompt variant.)

## Graph memory

Out of the box the wiki builds a knowledge graph from keyword proximity —
concepts linked where relation keywords co-occur with a `[[wikilink]]` in
the same block. Enable the
**opt-in graph passes** to turn that into an evidenced graph:

- **Triple extraction** (`ontology.triples.enabled`) — one extra LLM call
  per fully-compiled document extracts typed entities and relations, each
  carrying an evidence span, confidence, and source document.
- **Entity resolution** (`ontology.resolve.enabled`) — surface-form
  variants ("NASA" / "National Aeronautics and Space Administration")
  are linked to a canonical entity. High-confidence proposals apply
  automatically (threshold 0.85; set exactly `1.0` for review-only), and
  every link is exactly reversible with `ontology resolve --unlink`.
- **Graph QA** — the `wiki_graph_query` MCP tool answers multi-hop
  relational questions grounded *only* in a bounded, serialized set of
  edges; citations carry `source_doc` and `confidence` when the edge is
  evidenced (keyword-proximity edges carry neither). Regular Q&A
  context also names the connecting edge under each related article.

Depth, costs, review workflow, and undo semantics: [Graph Memory](docs/guides/graph-memory.md).

## Commands

The core surface; run `sage-wiki <command> --help` for flags.

| Command | Description |
| ------- | ----------- |
| `sage-wiki init [dir] [--vault] [--skill <agent>] [--pack <name>] [--prompts] [--force]` | Initialize project (greenfield or vault overlay); preserves existing config/manifest/gitignore unless `--force` |
| `sage-wiki compile [--watch] [--batch] [--estimate] [--dry-run] [--no-cache] [--fresh] [--re-embed] [--re-extract] [--prune]` | Compile sources into wiki articles |
| `sage-wiki serve [--addr 127.0.0.1:8484] [--transport stdio\|sse] [--ui]` | HTTP REST + MCP server / web UI |

## `CONTRIBUTING.md`

# Contributing to sage-wiki

**Before opening a PR:** run `make ci` on your feature branch — the accurate
local fast gate. It runs, in order: canonical formatting over all tracked Go
source (`scripts/ci/check-format.sh`), module tidy-drift and content
verification (`scripts/ci/check-modules.sh`, worktree-preserving), pure-Go
and webui builds, vet, new-issue lint, responsibility-manifest validation
(`tools/civalidate`: exact package partition, aggregate membership, Make
targets, determinism roles, platform inventory), the determinism tripwire
with its self-test, generated/API/skill drift checks, translation self-test
and header inventory, and the ordinary (non-race) test suite.
On `main` itself the *local* translation-drift range is empty (CI's push path
checks `before..after` and is not), so run `make translations` from your
branch for the range-based check.

**`make ci-race`** is the canonical local race contract: `-race` over every
manifest-owned package (`make test` is the legacy race alias). Run it before
pushing compiler/concurrency work; `make ci` deliberately stays non-race for
speed.

**Local `make ci` is mandatory but not a substitute for hosted CI.** It
prints, on success, exactly what it does NOT cover — hosted-only evidence:
Windows/macOS execution, PostgreSQL/MinIO service contracts, the
pinned-container frontend build, scheduled fuzz exploration, and exact-SHA
publication proof. The hosted `CI required` check-run on the latest PR SHA is
the merge gate: a green `make ci` does not replace a green hosted run, and a
hosted result that predates your last push does not count. Today that gate
is maintainer policy — a PR is not mergeable without `CI required` success
on the HEAD SHA — and it becomes mechanical once branch protection requires
the check on `main`.

## CI responsibility and ownership states

Quality responsibility is recorded in machine-readable manifests under
`ci/` (`standards.yaml`, `package-ownership.yaml`,
`platform-contracts.yaml`), validated fail-closed by `tools/civalidate`
against the live tree. Two ownership states matter when reading CI:

- **Required now (`required-requalifying`).** The current required jobs —
  build, parity, go-test, fuzz-short, skill-drift, postgres, minio, lint,
  frontend, translations — stay in the `CI required` aggregate and keep
  merge authority while they re-qualify under the shadow protocol.
- **Candidate (advisory).** Target witnesses (preflight checks, focused OS
  contracts, service-contract shards) run advisory only. The CI workflow's
  `Responsibility validation (advisory)` job may turn red — a validator or
  parser failure stays visible — but it is deliberately outside the
  `CI required` aggregate and cannot block a merge. Candidates earn
  promotion only through a recorded qualification window (at least 20
  relevant executions over seven days, zero unexplained divergence) and
  explicit maintainer approval.

If the advisory job is red on your PR, treat it as a real signal — fix the
underlying manifest/validation failure — but it does not gate merging while
it remains advisory.

## Repository layout

Selected entries (illustrative, not exhaustive):

```
├── cmd/sage-wiki/        # CLI entrypoint + command wiring
├── internal/             # the core (~30 packages): compiler, llm, storage,
│                         #   memory, vectors, search, graph, ontology, mcp,
│                         #   trust, api (/v1 REST), web, tui, linter, …
├── pkg/sagewiki/         # public Go module for embedding (in-process MCP)
├── clients/              # SDKs: python/ + typescript/
├── tools/skillgen/       # agent-skill generator (skills/ is generated output)
├── tools/civalidate/     # fail-closed CI responsibility validator
├── tools/testsummary/    # go test -json summarizer (annotations, exit-preserving)
├── ci/                   # responsibility manifests (standards, ownership, contracts)
├── skills/               # generated agent skills — never hand-edit; CI drift-checked
├── examples/             # CI-exercised framework examples (langgraph, vercel-ai-sdk)
├── eval/                 # benchmarks (LOCOMO, LongMemEval, BEAM)
├── api/openapi.yaml      # the /v1 REST contract (drift-checked against tools+routes)
├── web/                  # Preact web UI source (embedded via -tags webui)
├── docs/                 # guides/ + translations/ (six README locales)
├── assets/               # README images
└── scripts/              # CI/dev shell tools
```

## Translations

`README.md` and its six translations (`docs/translations/README_{fr,ja,ko,ru,vi,zh}.md`)
move together. A change range that touches `README.md` without any
`docs/translations/README_*.md` fails CI's Translation drift job (MAINT-05) —
`make ci` runs the same check locally. If the change genuinely should not be
translated yet, add `translations: lag-ok` to a commit message in the range
to document the debt.

**Maintainers merging external PRs:** GitHub holds CI for first-time
contributors at `action_required` — checks must have *run and passed*, not
merely be absent. Click "Approve and run workflows" on fork PRs, and treat a
PR showing zero checks as unverified regardless of local runs. When reworking
CI workflow code, keep the required context valid: once branch protection
requires `CI required` on `main`, relax or remove that required status check
before reverting or renaming the workflow that emits the check-run — a
required context that no workflow produces blocks every merge.

## Adding a file format parser

### Go (built-in)

1. Add a new case in `internal/extract/extract.go` matching the file extension
2. Implement the extraction function returning plain text content
3. Add tests in `internal/extract/extract_test.go`

### External (subprocess)

1. Write a parser script that reads file content from stdin and writes plain text to stdout
2. Create `parsers/parser.yaml` in your project or pack with the extension mapping:
   ```yaml
   parsers:
     - extensions: [".docx"]
       command: python3
       args: ["docx_parser.py"]
       timeout: 30s
   ```
3. Place the script in `parsers/` and ensure it's executable (relative paths in `command` and `args` are resolved against `parsers/`)
4. Enable external parsers in config: `parsers: { external: true }`

External parsers run with timeout enforcement (30s default, 120s max) and
environment stripping (only PATH, HOME, LANG reach the subprocess). They
require double opt-in: `parsers.external: true` to load definitions and
`parsers.trust_external: true` to acknowledge unsandboxed execution; packs
with parsers additionally need `pack apply --enable-parsers`. Built-in
extractors are hardened with decompression caps (per-entry and aggregate
limits against zip bombs) and covered by a nightly fuzzing job
([.github/workflows/fuzz.yml](.github/workflows/fuzz.yml)) that feeds
malformed docx/xlsx/pptx/epub/eml/pdf inputs and checks the caps hold.

## Fuzzing

Native Go fuzz targets guard the parsing and hardening surfaces. Two tiers run
in CI, both driven by the machine-readable inventory in
[`ci/fuzz-targets.yaml`](ci/fuzz-targets.yaml) (validated fail-closed against
the source tree — a new target without an inventory entry, or a stale entry,
turns the nightly job red):

- **PR-gated short pass** (`fuzz-short` job in
  [.github/workflows/ci.yml](.github/workflows/ci.yml)): the 8 hardening
  targets (`FuzzFrontmatter` ×5 packages, `FuzzWikilink`,
  `FuzzAliasNormalize`, `FuzzCanonical`) for 30s each.
- **Nightly exploration** ([.github/workflows/fuzz.yml](.github/workflows/fuzz.yml)):
  every target in the inventory — the 8 hardening targets plus the 6 extractor
  format targets (`FuzzExtract{Docx,Xlsx,Pptx,Epub,Email,PdfGo}`), which do
  **not** run on PRs.

Committed seed corpora run deterministically as ordinary package tests on
every PR; only the time-bounded random exploration above is scheduled.

Run a target locally (pick one target per invocation — Go's `-fuzz` errors if
a pattern matches more than one):

```sh
go test -run=NONE -fuzz=FuzzFrontmatter -fuzztime=30s ./internal/extract/
go test -run=NONE -fuzz=FuzzWikilink    -fuzztime=30s ./internal/compiler/
```

The current targets:

| Target | Package | Surface |
|--------|---------|---------|
| `FuzzExtract{Docx,Xlsx,Pptx,Epub,Email,PdfGo}` | `internal/extract` | extractor decompression caps |
| `FuzzFrontmatter` | `internal/extract`, `internal/web`, `internal/ontology`, `internal/wiki`, `internal/compiler` | the five pure-string frontmatter sites (one target per owning package) |
| `FuzzWikilink` | `internal/compiler` | wikilink matching, sanitization, broken-link strip |
| `FuzzAliasNormalize` | `internal/compiler` | name normalization + alias map |
| `FuzzCanonical` | `internal/compiler` | canonical frontmatter/JSON determinism |

Assertions are security invariants only — no panic, no unbounded growth,
deterministic output. Errors are accepted, never asserted.

If a run finds a crash, Go writes the failing input under
`<package>/testdata/fuzz/<Target>/`. **Commit that crasher file** with your
fix so the corpus always reproduces it:

```sh
git add internal/compiler/testdata/fuzz/FuzzWikilink/   # example
```

## Regenerating the web UI dist

The committed `internal/web/dist` must byte-match a `node:22-alpine` build
(CI enforces this with a hard-fail drift check). After changing anything
under `web/`, regenerate inside the pinned environment and commit the
result:

```sh
docker run --rm -v "$PWD:/src" -w /src/web node:22-alpine sh -c "npm ci && npm run build"
```


## Creating a pack

### Quick start

```bash
sage-wiki pack create my-pack
cd my-pack
# edit pack.yaml, add prompts, skills, samples
sage-wiki pack validate
```

### Pack directory structure

```
my-pack/
├── pack.yaml              # required — manifest
├── prompts/               # optional — prompt templates
│   └── summarize.txt
├── skills/                # optional — skill template files
├── parsers/               # optional — external parser scripts
│   ├── parser.yaml        # extension mappings
│   └── convert.py         # parser script
├── samples/               # optional — example source files
│   └── example.md
└── README.md              # optional — documentation
```

### Testing your pack


## `Dockerfile`

# Stage 1: Build web UI
FROM node:22-alpine AS webui
WORKDIR /build/web
COPY web/package.json web/package-lock.json ./
RUN npm ci
COPY web/ ./
RUN npm run build

# Stage 2: Build Go binary
FROM golang:1.26-alpine AS builder
WORKDIR /build
COPY go.mod go.sum ./
RUN go mod download
COPY . .
COPY --from=webui /build/internal/web/dist ./internal/web/dist
RUN CGO_ENABLED=0 go build -tags webui -ldflags="-s -w" -o sage-wiki ./cmd/sage-wiki

# Stage 3: Runtime
FROM alpine:3.21
RUN apk add --no-cache git tzdata ca-certificates && \
    adduser -D -u 1000 wiki
COPY --from=builder /build/sage-wiki /usr/local/bin/sage-wiki

USER wiki
WORKDIR /wiki
VOLUME /wiki

EXPOSE 3333

# The web UI binds 0.0.0.0 for container networking, which is non-loopback, so a
# token is REQUIRED — the server refuses to start without one. The same bind is
# subject to the DNS-rebind Host allowlist, so set SAGE_WIKI_ALLOWED_HOST to the
# hostname/IP you browse to (any non-loopback host, direct or via a proxy):
#   docker run -e SAGE_WIKI_TOKEN="$(openssl rand -hex 32)" \
#     -e SAGE_WIKI_ALLOWED_HOST=your-host -p 3333:3333 -v "$PWD:/wiki" <image>
# then open  http://your-host:3333/?token=<that token>  in a browser.
ENTRYPOINT ["sage-wiki"]
CMD ["serve", "--ui", "--bind", "0.0.0.0", "--port", "3333"]

## `Makefile`

# Local mirror of the CI quality gate (.github/workflows/ci.yml). Run `make ci`
# on a feature branch to reproduce the checks CI *gates* on.
#
# CGO policy matches CI: build/vet stay CGO_ENABLED=0 (the release binary is
# pure-Go, modernc.org/sqlite); race targets use CGO_ENABLED=1 because the race
# detector hard-requires cgo. Enabling cgo for tests pulls in no cgo module deps.
#
# Honesty contract (20260812-ci-quality-system Task 7): `make ci` is the fast
# local gate and prints what it does NOT cover. Hosted-only evidence — OS
# execution, PostgreSQL/MinIO services, pinned-container frontend, scheduled
# fuzz exploration, and exact-SHA publication proof — is never claimed here.

GO ?= go
GOLANGCI_LINT_VERSION ?= v2.12.2
# Base branch for the new-issues lint filter (mirrors CI's --new-from-merge-base)
# and the translation-drift range. Falls back to origin/main when no local main
# exists (detached worktrees); shallow clones need full history for merge-base.
BASE ?= main
LINT_BASE ?= $(BASE)

.PHONY: build build-webui vet test test-norace lint lint-new vuln tidy \
        format-check modules-check responsibility-check determinism-check \
        generated-check translations translations-self-test translations-headers \
        ci ci-race record-fixtures regen-goldens parity

build:
	CGO_ENABLED=0 $(GO) build ./...

build-webui:
	CGO_ENABLED=0 $(GO) build -tags webui ./...

vet:
	CGO_ENABLED=0 $(GO) vet ./...

# Full race suite (legacy name kept for contributors and manifest references).
test:
	CGO_ENABLED=1 $(GO) test -race ./...

# Ordinary (non-race) suite — the `make ci` test leg. Environment-gated
# service tests (TEST_DATABASE_URL, SAGE_TEST_MINIO) keep their local skips.
test-norace:
	CGO_ENABLED=0 $(GO) test ./...

# Full report incl. the pre-existing backlog — for chipping away at it locally.
lint:
	$(GO) run github.com/golangci/golangci-lint/v2/cmd/golangci-lint@$(GOLANGCI_LINT_VERSION) run ./...
	bash scripts/check-determinism.sh

# Only NEW issues vs $(LINT_BASE) — exactly what CI gates. Green on unmodified main.
lint-new:
	$(GO) run github.com/golangci/golangci-lint/v2/cmd/golangci-lint@$(GOLANGCI_LINT_VERSION) run --new-from-merge-base=$(LINT_BASE) ./...

# Advisory only — matches CI's continue-on-error vuln job. Currently flags Go
# stdlib advisories fixed only in a newer patch toolchain, so it is intentionally
# NOT part of the `ci` aggregate; run it on its own.
vuln:
	$(GO) run golang.org/x/vuln/cmd/govulncheck@latest ./...

tidy:
	$(GO) mod tidy

# --- Local-contract checks (fail-closed; each has a --self-test mutation suite) ---

# Canonical formatting over ALL tracked Go source (empty inventory is red).
format-check:
	bash scripts/ci/check-format.sh

# go.mod/go.sum tidy drift + module content verification (never mutates the
# worktree: tidy runs with -diff).
modules-check:
	bash scripts/ci/check-modules.sh

# Responsibility manifests: parser/validation suite plus the live fail-closed
# validator (exact package partition, aggregate membership, Make targets,
# determinism roles, platform inventory, shards, service contracts, fuzz
# inventory). Every workflow is validated so a witness job reference can
# never point at a job that does not exist: ci.yml (required aggregate),
# ci-shadow.yml (advisory candidates), fuzz.yml (scheduled exploration),
# and ci-diagnostics.yml (scheduled broad diagnostics).
responsibility-check:
	$(GO) test ./tools/civalidate -count=1
	$(GO) run ./tools/civalidate \
		--standards ci/standards.yaml \
		--packages ci/package-ownership.yaml \
		--platforms ci/platform-contracts.yaml \
		--services ci/service-contracts.yaml \
		--fuzz-targets ci/fuzz-targets.yaml \
		--workflow .github/workflows/ci.yml \
		--makefile Makefile
	$(GO) run ./tools/civalidate \
		--standards ci/standards.yaml \
		--packages ci/package-ownership.yaml \
		--platforms ci/platform-contracts.yaml \
		--services ci/service-contracts.yaml \
		--fuzz-targets ci/fuzz-targets.yaml \
		--workflow .github/workflows/ci-shadow.yml \
		--makefile Makefile
	$(GO) run ./tools/civalidate \
		--standards ci/standards.yaml \
		--packages ci/package-ownership.yaml \
		--platforms ci/platform-contracts.yaml \
		--services ci/service-contracts.yaml \
		--fuzz-targets ci/fuzz-targets.yaml \
		--workflow .github/workflows/fuzz.yml \
		--makefile Makefile
	$(GO) run ./tools/civalidate \
		--standards ci/standards.yaml \
		--packages ci/package-ownership.yaml \
		--platforms ci/platform-contracts.yaml \
		--services ci/service-contracts.yaml \
		--fuzz-targets ci/fuzz-targets.yaml \
		--workflow .github/workflows/ci-diagnostics.yml \
		--makefile Makefile

# Determinism tripwire: contract self-test first, then the live scan.
# Run sequentially — the self-test plants a temporary in-tree offender.
determinism-check:
	bash scripts/check-determinism.sh --self-test
	bash scripts/check-determinism.sh

# Generated/API/skill drift: byte-identical skill regeneration, committed-output
# match, and the OpenAPI/route/MCP agreement tests.
generated-check:
	$(GO) test ./tools/skillgen -run '^(TestRegenerateIdempotent|TestOutputMatchesCommitted)$$' -count=1
	$(GO) test ./internal/api -run '^TestDrift_' -count=1

# Translation drift (MAINT-05): README.md must move with at least one
# docs/translations/README_*.md translation, or a commit in the range carries
# `translations: lag-ok`. One shell per target: recipe lines would otherwise
# lose the computed vars between lines.
translations:
	@mb=$$(git merge-base "$$(git rev-parse --verify --quiet $(BASE) || git rev-parse --verify --quiet origin/main)" HEAD); 	COMMIT_MSGS="$$(git log --format=%B $$mb..HEAD)"; 	BASE="$(BASE)" HEAD=HEAD COMMIT_MSGS="$$COMMIT_MSGS" bash scripts/check-readme-translations.sh

# Contract test for the check itself (no repo state needed).
translations-self-test:
	bash scripts/check-readme-translations.sh --self-test

# The six committed translation files must carry their lag headers.
translations-headers:
	bash scripts/check-readme-translations.sh --verify-headers

# The accurate local fast gate. Deliberately excludes `vuln` (advisory in CI)
# and the range-based `translations` drift check (branch-context dependent;
# hosted CI computes the real range — run `make translations` on your branch).
# Ends with the hosted-only omissions so nobody mistakes this for full CI.
ci: format-check modules-check build build-webui vet lint-new \
    responsibility-check determinism-check generated-check \
    translations-self-test translations-headers test-norace
	@echo "make ci: local gate passed. NOT covered locally (hosted-only evidence):"
	@echo "  - Windows/macOS execution — hosted workflow artifacts"
	@echo "  - PostgreSQL/MinIO service contracts — hosted service logs"
	@echo "  - Frontend dist — pinned node:22-alpine build and diff"
	@echo "  - Random fuzz exploration — scheduled crasher artifacts"
	@echo "  - Release/publication — exact-SHA proof and provenance"

# The canonical local race contract: -race over every manifest-owned package.
# (`make test` is the legacy race alias, kept for contributors and manifest
# references; ci-race is the named contract target.)
ci-race:
	CGO_ENABLED=1 $(GO) test -race -timeout 15m ./...

# SPEC-09: record LLM fixtures via the scripted origin (default) or a real
# vendor (ORIGIN=https://... KEY=...). Maintainer action — CI never records.
record-fixtures:
	@test "$$SAGE_PARITY_FORCE" = "1" || { echo "refusing: set SAGE_PARITY_FORCE=1 (golden overwrite guard)"; exit 1; }
	ORIGIN="$(ORIGIN)" go test ./internal/parity/ -run TestRecordFixtures -count=1

# SPEC-09: regenerate goldens from the current code. Guarded; commit with a
# "Golden changes" PR section explaining every diff category.
regen-goldens:
	@test "$$SAGE_PARITY_FORCE" = "1" || { echo "refusing: set SAGE_PARITY_FORCE=1 (golden overwrite guard)"; exit 1; }
	go test ./internal/parity/ -run TestRegenGoldens -count=1

# SPEC-09: the parity suite (replay mode, offline).
parity:
	go test -count=1 ./internal/parity/

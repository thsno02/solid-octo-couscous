# Repository semantic capsule: open-metadata/OpenMetadata

- Commit: `68606d705a225f14dd87847f2be733da5fef38db`
- Default branch: `main`
- Description: open-metadata/OpenMetadata
- Selected evidence files: 8 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

# OpenMetadata

![Commit Activity](https://img.shields.io/github/commit-activity/m/open-metadata/OpenMetadata?style=for-the-badge) [![Release](https://img.shields.io/github/release/open-metadata/OpenMetadata/all.svg?style=for-the-badge)](https://github.com/open-metadata/OpenMetadata/releases)

## The Open Context Layer for AI

**The largest and fastest-growing open-source project for AI context, data cataloging, and metadata management.**

OpenMetadata is the open platform for trusted data context, organizational memory, and business semantics for every data user, AI assistant, and agent.

OpenMetadata connects technical metadata, data quality signals, lineage, column-level lineage, ownership, usage, policies, conversations, memories, glossaries, classifications, metrics, domains, data contracts, and data products into a unified metadata knowledge graph. With **130+ connectors**, open metadata standards, semantic search, APIs, SDKs, and an MCP server, OpenMetadata gives every user and AI system the governed context it needs to discover, understand, trust, remember, and use data.

**AI does not need another raw database connector. AI needs context + memory.**

![OpenMetadata: The Open Context Layer for AI](docs/assets/open-context-layer-hero.png)

OpenMetadata provides the context AI needs to know:

- what data exists
- what it means
- who owns it
- how it is used
- where it came from
- where it flows
- whether it is fresh, tested, certified, and trusted
- which business concepts, classifications, glossary terms, policies, contracts, and data products apply
- what downstream dashboards, pipelines, metrics, ML models, and applications depend on it
- what conversations, decisions, assumptions, and memory nuggets have already been captured about it

---

## Why OpenMetadata for AI?

AI systems need more than data access. They need governed context, business meaning, trust signals, lineage, usage, ownership, standards, and organizational memory.

A direct connection to a warehouse, lake, dashboard, or pipeline exposes raw structures. It does not tell an AI assistant what the data means, whether it is certified, who owns it, which policies apply, what contract governs it, what breaks if it changes, or what the organization has already learned about it.

OpenMetadata is the open context layer that gives every data user and AI agent the full picture of enterprise data.

OpenMetadata brings together five capabilities:

1. **Context** — technical, operational, trust, usage, and lineage metadata from across the data ecosystem.
2. **Semantics** — business meaning through glossaries, metrics, classifications, domains, policies, ontologies, and data products.
3. **Knowledge Graph** — relationships connecting assets, columns, people, teams, quality, lineage, policies, memories, contracts, and business concepts.
4. **Memory** — conversations, AI threads, decisions, assumptions, runbooks, remediation notes, and reusable memory nuggets that preserve tribal knowledge.
5. **Activation** — MCP, Semantic Search, APIs, SDKs, events, and workflows that make context usable by AI assistants, agents, applications, and humans.

With OpenMetadata, users and AI agents can answer:

- What does this metric mean and how is it calculated?
- Which datasets power this dashboard?
- Who owns this data product?
- Which data contract applies?
- Is this dataset fresh, tested, certified, and trusted?
- Which downstream dashboards, pipelines, or ML models are affected by this column change?
- Which columns contain sensitive customer information?
- Which glossary terms, policies, standards, and business concepts apply?
- What decisions, assumptions, incidents, or conversations have already been captured about this asset?

---

## The Context OpenMetadata Connects

OpenMetadata collects and connects the context AI needs to reason safely over enterprise data.

| Context type | What OpenMetadata captures | Why it matters for AI |
| --- | --- | --- |
| **Technical metadata** | Databases, schemas, tables, columns, topics, dashboards, charts, pipelines, APIs, search indexes, ML models, storage assets, data types, constraints, descriptions, joins, sample queries, service metadata, owners, teams, usage, domains, and data products | Helps AI discover what exists and understand how assets are structured |
| **Quality and trust** | Test cases, test suites, freshness checks, volume checks, null, uniqueness, distribution, custom tests, profiling results, observability signals, incidents, alerts, and quality history | Helps AI avoid treating every dataset as equally trustworthy |
| **Lineage and impact** | Upstream and downstream lineage, table lineage, column-level lineage, dashboard lineage, pipeline lineage, metric lineage, ML model lineage, API and topic dependencies, and OpenLineage events | Helps AI explain where data came from, where it flows, and what changes may break |
| **Semantics** | Glossaries, business terms, synonyms, related terms, metrics, KPIs, classifications, tags, domains, data products, policies, personas, lifecycle states, and ontologies | Helps AI map technical names to business meaning |
| **Governance** | Owners, stewards, teams, policies, roles, classifications, access context, certification, review workflows, lifecycle states, and data contracts | Helps AI act with policy-aware context |
| **Memory and tribal knowledge** | Conversations, AI threads, decisions, assumptions, runbooks, remediation notes, incident learnings, and reusable memory nuggets attached to assets, users, teams, data products, and agent workflows | Helps humans and agents inherit what the organization already learned instead of rediscovering it in every conversation |
| **Standards and interoperability** | DCAT, DPROD, PROV-O, OpenLineage, ODCS, RDF/OWL, JSON-LD, SHACL, JSON Schema, APIs, events, and metadata schemas | Helps context move across tools, agents, catalogs, contracts, and knowledge graphs |

---

## Architecture: Context + Memory Graph

![How OpenMetadata Works](docs/assets/open-context-layer-architecture.png)

OpenMetadata is built around an open, schema-first metadata graph.

1. **Collect** metadata from warehouses, lakes, BI tools, pipelines, ML platforms, messaging systems, storage systems, APIs, search systems, SaaS applications, metadata systems, documents, conversations, and agent workflows through **130+ connectors**, ingestion APIs, events, and SDKs.
2. **Normalize** metadata with open schemas and standards so every asset, relationship, policy, contract, lineage event, and memory can be represented consistently.
3. **Connect** technical metadata, quality signals, lineage, ownership, usage, policies, conversations, memories, semantics, domains, contracts, and data products into one graph.
4. **Preserve Memory** by turning conversations, AI threads, decisions, assumptions, runbooks, and remediation notes into reusable governed memory nuggets tied to data assets and business context.
5. **Govern** context with open standards, classifications, policies, roles, data quality, review workflows, data contracts, and stewardship.
6. **Activate** that context through Semantic Search, MCP, APIs, SDKs, events, webhooks, metadata applications, and AI workflows.

Memory is part of the architecture, not a side channel. It lets engineers use APIs, SDKs, MCP, or AI workflows to preserve conversational context and convert tribal knowledge into reusable organizational knowledge.

---

## Context Graph, Semantics, and Memory

![OpenMetadata Context Graph](docs/assets/open-context-layer-graph.png)

The OpenMetadata graph does not only store data assets. It stores the relationships between assets, columns, owners, teams, policies, quality tests, lineage, classifications, glossary terms, metrics, domains, data contracts, data products, conversations, and memory nuggets.

Example relationships:

```text
Table               ──hasColumn────────────> Column
Column              ──classifiedAs─────────> PII
Column              ──represents───────────> Customer Identifier
Table               ──ownedBy─────────────> Data Engineering Team
Table               ──partOf──────────────> Customer 360 Data Product
Dashboard           ──dependsOn───────────> Table
Metric              ──definedBy───────────> Glossary Term
Pipeline            ──produces────────────> Table
Column              ──flowsTo─────────────> Column
Test Case           ──validates───────────> Table
Policy              ──governs─────────────> Classification
Data Contract       ──appliesTo───────────> Table
OpenLineage Event   ──updatesLineageFor───> Pipeline
Agent Conversation  ──capturedAs──────────> Memory 
Memory              ──informs─────────────> Data Product
Memory              ──documentsDecisionFor> Metric
Memory              ──attachedTo──────────> Table / Column / Topic / Dashboard / Pipeline / API
```

This graph gives AI systems the relationships, meaning, memory, and governance they need to reason across the data estate.

---

## Memories: Organizational Context for Humans and Agents

![Memory Primitives](docs/assets/memory-primitives.png)

Memories preserve the important context that usually disappears inside chats, tickets, meetings, notebooks, and AI agent threads.

A memory is an open, governed OpenMetadata entity that can be tied to data assets, users, teams, threads, domains, data products, metrics, policies, incidents, and workflows. Engineers can capture and retrieve memories through APIs, SDKs, MCP, chat, or AI applications.

Use memories to preserve:

- why a metric changed
- why a column was renamed
- what assumption was used in an analysis
- which remediation fixed a data quality issue
- which dashboard or data product a decision applies to
- what an AI agent learned while investigating an incident
- what a domain expert explained in a conversation

Memories unlock tribal knowledge by making it reusable, governed, searchable, and available to every human, assistant, and agent that touches your data.

---

## MCP, Semantic Search, APIs, AI SDK, and Memory

OpenMetadata makes context actionable through AI- and developer-friendly interfaces.

### MCP Server

OpenMetadata includes an MCP server that lets MCP-compatible assistants and agents interact with the metadata graph through natural language.

AI assistants can use OpenMetadata MCP to:

- search metadata
- run semantic search
- retrieve entity details
- inspect lineage
- understand data contracts and policy context
- retrieve or preserve memory nuggets
- update descriptions, tags, owners, and other metadata
- create glossary terms and lineage
- list and create data quality tests
- analyze root causes of data quality failures

Get started: [OpenMetadata MCP Server Documentation](https://docs.open-metadata.org/latest/how-to-guides/mcp)

### Semantic Search

Semantic Search lets users and AI assistants find data assets by meaning, not only exact keywords.

```text
Find trusted customer purchase datasets with known data quality issues and recent remediation notes.
```

OpenMetadata can surface conceptually related assets, metrics, glossary terms, data products, memory nuggets, and governance context even when names differ across domains, tools, and teams.

### APIs, SDKs, Events, and Webhooks

OpenMetadata exposes APIs, SDKs, events, and webhooks so teams can ingest, update, search, subscribe to, and automate metadata across their ecosystem.

Developers can use the AI SDK to build custom AI applications that use OpenMetadata context and memory programmatically.

---

## Use It From Code

Two packages, depending on what you're building.

| Goal | Package | Install |
|------|---------|---------|
| Read/write metadata, lineage, glossary, quality | [`openmetadata-ingestion`](https://pypi.org/project/openmetadata-ingestion/) | `pip install "openmetadata-ingestion"` |
| Give an LLM or agent governed access (MCP, LangChain) | [`data-ai-sdk`](https://pypi.org/project/data-ai-sdk/) | `pip install data-ai-sdk` |

Also available: [`@openmetadata/ai-sdk`](https://www.npmjs.com/package/@openmetadata/ai-sdk) (TypeScript), [`org.open-metadata:ai-sdk`](https://central.sonatype.com/artifact/org.open-metadata/ai-sdk) (Java).

### Python SDK — connect and read metadata

Match the SDK version to your server version.

```python
from metadata.generated.schema.entity.data.table import Table
from metadata.generated.schema.entity.services.connections.metadata.openMetadataConnection import (
    OpenMetadataConnection, AuthProvider,
)
from metadata.generated.schema.security.client.openMetadataJWTClientConfig import (
    OpenMetadataJWTClientConfig,
)
from metadata.ingestion.ometa.ometa_api import OpenMetadata

metadata = OpenMetadata(OpenMetadataConnection(
    hostPort="http://localhost:8585/api",
    authProvider=AuthProvider.openmetadata,
    securityConfig=OpenMetadataJWTClientConfig(jwtToken="<your-token>"),
))
assert metadata.health_check()

## `AGENTS.md`

CLAUDE.md

## `CLAUDE.md`

# CLAUDE.md

Always-loaded guidance for every session. **Language- and path-specific rules live in
`.claude/rules/*.md` (auto-loaded when you touch matching files); procedures live in skills
(loaded on invoke).** This file is the map — see the pointer index at the bottom. Read
[ARCHITECTURE.md](ARCHITECTURE.md) for the **system map** (modules, the request/ingestion/search paths,
the invariants that hold); read [DEVELOPER.md](DEVELOPER.md) for **how to build, test, and add an entity
or connector** (deep dives + end-to-end checklists). Consult [docs/index.md](docs/index.md) — the **knowledge index** — to
**find existing design, plan, and reference docs** for whatever area you're working on.

## About OpenMetadata

OpenMetadata is a unified metadata platform for data discovery, observability, and governance — a
multi-module project with a Java backend, a React/TypeScript frontend, a Python ingestion framework,
and Docker infrastructure.

## Stack at a glance

- **Backend**: Java 21 + Dropwizard, multi-module Maven.
- **Frontend**: React + TypeScript, built with **Vite** (dev server on :3000); component library
  `openmetadata-ui-core-components` — the **UntitledUI + Tailwind v4** (`tw:` prefix, react-aria-components)
  go-forward design system; legacy stack is Ant Design + Less (deprecated). Machine-readable design-system
  specs: `openmetadata-ui/src/main/resources/ui/specs/` (read `specs/README.md` before UI work).
- **Ingestion**: Python (`>=3.10`, no pinned ceiling; **CI runs 3.10**) + Pydantic 2.x, 75+ connectors.
- **Database**: MySQL (default) or PostgreSQL. **Search**: Elasticsearch 7.17+ or OpenSearch 2.6+.
- **Infrastructure**: Apache Airflow for ingestion orchestration.

## Environment setup (every session)

- **Python venv is REQUIRED before any Python work, `make generate`, or `make install_dev*`:**
  ```bash
  source env/bin/activate          # first time: python3.11 -m venv env
  python --version                 # expect 3.10.x/3.11.x
  ```
  In a Claude Code **worktree** the venv is NOT copied — create one
  (`python3.11 -m venv env && source env/bin/activate && cd ingestion && make install_dev`) or
  symlink the main repo's (`ln -s /path/to/main-repo/env env`).
- **One-call setup (macOS + Linux)**: `make dev_setup` (or `./scripts/dev_setup.sh`) does everything
  below — toolchain, venv, generation, UI deps, pre-commit — and is idempotent. `make dev_check`
  diagnoses an existing checkout without changing it. See the `dev-setup` skill.
- **First-time bootstrap** (from the **repo root** — `make generate` is a root-only target; it does
  not exist under `ingestion/`):
  ```bash
  make prerequisites
  source env/bin/activate && cd ingestion && make install_dev_env && cd ..
  make generate                    # regenerate models after any schema change
  make yarn_install_cache
  make install_test precommit_install   # activate the commit-time format/license gate (pre-commit)
  ```
  The last line installs the `pre-commit` hooks (`.pre-commit-config.yaml`): on `git commit` they run
  Java format (spotless), Python format (ruff), UI format (prettier), design-token, and Apache-2.0
  license checks on your changed files, matching CI. Do not skip them with `--no-verify`.
- **Java**: Java 21; use `mvn`. **Frontend**: use `yarn` (never `npm`); frontend root is
  `openmetadata-ui/src/main/resources/ui/`.
- **Docker dev services**: `docker compose -f docker/development/docker-compose.yml up -d`.

## Repository layout

Maven modules (reactor order is computed from the graph, not this list):

- `openmetadata-spec/` — JSON Schemas + generated POJOs; the schema-first source of truth
- `openmetadata-sdk/` — Java client SDK
- `common/` — shared utilities (`CommonUtil`, etc.)
- `openmetadata-shaded-deps/` — ES/OS clients relocated behind `es.*`/`os.*` (do not edit — see rules)
- `openmetadata-service/` — core Java backend, REST APIs, repositories, migrations runner
- `openmetadata-k8s-operator/` — Kubernetes operator
- `openmetadata-integration-tests/` — backend API integration tests (`*IT.java`)
- `openmetadata-mcp/` — MCP server
- `openmetadata-ui-core-components/` — canonical React component library
- `openmetadata-ui/src/main/resources/ui/` — React frontend application
- `openmetadata-dist/` — packaging/distribution
- `openmetadata-clients/` — client artifacts

Other key trees: `ingestion/` (Python framework + connectors), `bootstrap/sql/` (DB migrations),
`conf/` (configuration), `docker/` (local + prod deployment).

## Hard cross-cutting constraints (apply to every session, all languages)

**Secrets & security.** Never commit secrets — use environment variables or a secrets manager.
Auth is JWT with OAuth2/SAML; RBAC lives in Java entities; config in `conf/openmetadata.yaml`.
**Do not modify `.github/workflows/**` on your own** — CI workflows are a supply-chain surface; a
`PreToolUse` hook blocks edits there unless the user explicitly authorizes them (by setting
`CLAUDE_ALLOW_WORKFLOW_EDITS=1`). Ask first.

**All caches MUST be bounded.** Never use a bare `dict` / `HashMap` / `Map` as a cache without an
explicit size cap — they grow with input and OOM on large catalogs/ingestions (only exception: the
user explicitly asks for unbounded). Pick a sane default (100–1000 entries); if unsure, ask.
Python: `collections.OrderedDict` + `popitem(last=False)`, `@functools.lru_cache(maxsize=N)`, or
`cachetools.LRUCache` (cache hits **and** misses). Java: Caffeine/Guava `maximumSize(N)`.
TypeScript: `lru-cache`. Before adding a cache, check it isn't already cached a layer down (e.g.
`OpenMetadata._search_es_entity` is already `@lru_cache(maxsize=512)`).

**Comments explain *why*, never restate code.** Do NOT add comments that describe what obvious code
does (`// Create user` before `createUser()`). Only comment complex business logic, non-obvious
algorithms/workarounds, public-API JavaDoc, or `TODO/FIXME` with a ticket reference. If code needs a
comment to be understood, refactor it to be clearer instead.

**Testing philosophy.** Test real behavior, not mock wiring — if a test mocks 3+ of your own classes
to verify a method call, it tests the wrong thing. Prefer integration tests over heavily-mocked unit
tests (this project has real ITs: `OpenMetadataApplicationTest`, Docker, real OpenSearch). Mocks are
for boundaries (HTTP clients, third-party APIs), not internals. Ask "what breaks if this test passes
but the code is wrong?" — if the answer is "nothing", rewrite it. Assert on observable outcomes
(API responses, DB state), not internal `verify()` calls.

**License headers are per-module — copy one from a sibling file, never assume Apache.** UI TS/TSX:
Apache-2.0 (`yarn license-header-fix`). Python: `ingestion/` is **Collate Community License 1.0** (`ingestion/LICENSE`); `openmetadata-airflow-apis/` Python files use the same Collate header template.
Java: Apache-2.0, most files carry none.
Only the UI is enforced — the `ui-license-header` pre-commit hook and CI `ui-checkstyle`; spotless
and `py_format_check` never look at headers, so a wrong Python or Java header ships silently.

**Schema-first.** JSON Schemas in `openmetadata-spec/` are the single source of truth; all generated
code (Java POJOs, Pydantic models, TS types) is derived. **Edit the schema, then regenerate — never
hand-edit generated output.** Details in `.claude/rules/schema-first.md`.

**Output style.** Clean code blocks, no unnecessary explanation; assume an experienced reader; focus
on functionality over education. Do not add unnecessary blank lines between prose and code blocks.

**No wrappers around core-ui components.** If a wrapper component exists that wraps a core-ui component, skip it — use the `openmetadata-ui-core-components` component directly at the call site. Only create a wrapper if it adds genuine, non-trivial behaviour (custom hook logic, composed sub-components, domain-specific state). A wrapper that only passes props through is a maintenance liability: it hides which core component is in use and drifts from upstream updates.

**Icons and assets: always go through the design-system layer.** Import icons from `@openmetadata/ui-core-components/icons`, never directly from `@untitledui/icons` — the core-components package re-exports the full icon set and bypassing it can diverge on version upgrades. For the same reason, do not import SVG icons directly from `assets/` paths; use the designated abstraction instead.

## Pointer index — when to reach for what

### Path-scoped rules (`.claude/rules/*.md`, auto-load on matching files)

| Rule file | Reach for it when you are editing… |
|---|---|
| `java.md` | any `**/*.java` — style, spotless, no-wildcard, Kafka-grade method/class rules, ITs |
| `frontend-react.md` | UI `*.{ts,tsx}` — components, hooks, state, types, and the CI lint code-rules |
| `frontend-styling.md` | UI `*.{ts,tsx,less,css}` — `tw:` prefix, design tokens, ring→border, token-audit |
| `component-library.md` | UI `*.{ts,tsx}` — prefer `ui-core-components`, do not add Ant Design for new work |
| `frontend-performance.md` | UI `*.{ts,tsx}` — waterfalls, barrel imports, re-renders, bundle discipline |
| `frontend-a11y.md` | UI `*.{ts,tsx}` — semantics over `div`+`role`, keyboard, focus, contrast, targets |
| `i18n.md` | UI `*.{ts,tsx}` + `src/locale/**` — no string literals, `yarn i18n`, translate placeholders |
| `frontend-playwright.md` | UI `playwright/**` — E2E test constraints |
| `python-ingestion.md` | `ingestion/src/**/*.py` — pytest style, connector-specific-file rule, `model_str()` |
| `schema-first.md` | `openmetadata-spec/.../schema/**` and any `generated/**` — regen, never hand-edit generated |
| `migrations.md` | `bootstrap/sql/**` — append-only, native path, MySQL+Postgres, idempotent |

### Repo coding conventions (read before writing non-trivial code)

- `docs/design-patterns.md` — the design patterns this codebase uses idiomatically (Template Method
  for repositories, Factory/Registry for dispatch, Strategy/Adapter/Observer, the ingestion
  Source→Sink pipeline, …) with the canonical class to copy each from. Extend the established pattern
  rather than inventing a parallel one.
- `openmetadata-ui/src/main/resources/ui/DEVELOPER_HANDBOOK.md` — **the UI folder structure and file
  naming spec.** Read before creating any new file under `openmetadata-ui/.../ui/src/`. Layers stay
  top-level (`components/`, `pages/`, `rest/`, `utils/`, `hooks/`) and are grouped inside by
  `domain/feature/`; new files use one stem with a role suffix (`GlossaryList.tsx`, `.types.ts`,
  `.utils.ts`, `.test.tsx`). Legacy `.component.tsx`/`.interface.ts` files stay as they are.

### Skills (invoke by name; procedures, not rules)

| Skill | Reach for it when… |
|---|---|
| `dev-setup` | setting up / repairing a dev environment, a fresh clone, or a new worktree |
| `planning` | starting any non-trivial, multi-file feature or refactor |
| `tdd` | implementing a feature or bug fix (RED→GREEN→REFACTOR) |
| `systematic-debugging` | a failing test/build/runtime issue whose cause isn't obvious |
| `test-enforcement` | before a PR — 90% changed-class coverage, ITs for new endpoints, Playwright for UI |
| `verification` | before claiming "done" — run real commands, show evidence |
| `code-review` | reviewing a diff/PR — spec compliance then code quality |
| `java-checkstyle` | after touching `.java` — runs `mvn spotless:apply` and verifies |
| `ui-checkstyle` | after touching UI `*.{ts,tsx,js,jsx,json}` — the exact CI ESLint+Prettier+organize-imports pass |
| `ui-core-components` | building UI layout/color before reaching for raw `<div>` + Tailwind |
| `test-locally` | spinning up the full local Docker stack to test a change/connector |
| `connector-standards` / `connector-building` / `connector-review` | building or reviewing an ingestion connector |
| `playwright` / `writing-playwright-tests` / `playwright-validation` | authoring or validating Playwright E2E tests |
| `pr-checklist` | opening/finalizing a PR (fills the repo PR template) |

> `openmetadata-workflow` is a meta-skill that routes tasks to the skills above; it is auto-loaded at
> session start when the `openmetadata-skills` plugin is installed.

### Harness integrity (CI, warnings-only)

A CI workflow (harness-integrity.yml) runs `scripts/harness/check_harness.py` on PRs — also
`make harness-check` locally. It **warns, never blocks** (promote to a gate only with maintainer
sign-off) when the agent-facing config decays:

- **dead references** — a path, `make`/`yarn` target, or `mvn` goal named in this file, AGENTS.md,
  ARCHITECTURE.md, `docs/index.md`, `.claude/rules/**`, or a SKILL.md that no longer resolves;
- **AGENTS.md sync** — AGENTS.md is a symlink to this file; the check warns if it isn't;
- **skill symlinks** — a real file where a symlink into `skills/` is expected (`.claude/skills`,
  `.agents/skills`), or two same-named SKILL.md with different content;
- **doc-size budgets** — this file > 200 lines, ARCHITECTURE.md > 300, any single rule > 100;
- **rule globs** — a `.claude/rules/**` `paths:` glob matching zero files;
- **generated-doc freshness** — `docs/generated/**` out of date with its source.

## `CONTRIBUTING.md`

# Contributors

We ❤️ all contributions, big and small!

Read [Build Code and Run Tests](https://docs.open-metadata.org/developers/contribute/build-code-and-run-tests) for how to setup your local development environment. Get started with our [Good first issues](https://github.com/open-metadata/OpenMetadata/issues?q=is%3Aissue+is%3Aopen+label%3A%22good-first-issue%22).

We also recommend joining the OpenMetadata [Slack Workspace](https://slack.open-metadata.org/) to meet the team, stay up to date with product features, and chat with other contributors! 

Once joining our Slack we recommend Introducing yourself in the #introductions channel. Tell us a bit about yourself and how you are currently using OpenMetadata if you are.

If you need help getting started in contributing, you can reach out in the #support channel and ask if anyone would be available to get you up to speed or just answer some questions.  

If you just have suggestions for how to improve OpenMetadata you can submit your feedback in #feature-requests. If you have a fix or contribution in mind but need some guidance, please post in the #contributor channel with a description of the change before opening a new Github issue. 

## `Makefile`

.DEFAULT_GOAL := help
PY_SOURCE ?= ingestion/src
include ingestion/Makefile

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":"}; {printf "\033[35m%-35s\033[0m %s\n", $$2, $$3}'

.PHONY: prerequisites
prerequisites:
	./scripts/check_prerequisites.sh

.PHONY: dev_setup
dev_setup:  ## One-call dev environment setup for macOS/Linux (pass flags via ARGS=...)
	./scripts/dev_setup.sh $(ARGS)

.PHONY: dev_check
dev_check:  ## Diagnose the dev environment without changing anything
	./scripts/dev_setup.sh --check

.PHONY: install_e2e_tests
install_e2e_tests:  ## Install the ingestion module with e2e test dependencies (playwright)
	python -m pip install "ingestion[e2e_test]/"
	playwright install chromium --with-deps

.PHONY: run_e2e_tests
run_e2e_tests: ## Run e2e tests
	pytest --screenshot=only-on-failure --output="ingestion/tests/e2e/artifacts" $(ARGS) --slowmo 5 --junitxml=ingestion/junit/test-results-e2e.xml ingestion/tests/e2e

## Yarn
.PHONY: yarn_install_cache
yarn_install_cache:  ## Use Yarn to install UI dependencies
	cd openmetadata-ui/src/main/resources/ui && yarn install --frozen-lockfile

.PHONY: yarn_start_dev_ui
yarn_start_dev_ui:  ## Run the UI locally with Yarn
	cd openmetadata-ui/src/main/resources/ui && yarn start

.PHONY: yarn_start_e2e
yarn_start_e2e:  ## Run the e2e tests locally with Yarn
	cd openmetadata-ui/src/main/resources/ui && yarn playwright:run

.PHONY: yarn_start_e2e_ui
yarn_start_e2e_ui:  ## Run the e2e tests locally in UI mode with Yarn
	cd openmetadata-ui/src/main/resources/ui && yarn playwright:open

.PHONY: yarn_start_e2e_codegen
yarn_start_e2e_codegen:  ## generate playwright code
	cd openmetadata-ui/src/main/resources/ui && yarn playwright:codegen

.PHONY: py_antlr
py_antlr:  ## Generate the Python code for parsing FQNs
	antlr4 -Dlanguage=Python3 -o ingestion/src/metadata/generated/antlr ${PWD}/openmetadata-spec/src/main/antlr4/org/openmetadata/schema/*.g4

.PHONY: js_antlr
js_antlr:  ## Generate the Python code for parsing FQNs
	antlr4 -Dlanguage=JavaScript -o openmetadata-ui/src/main/resources/ui/src/generated/antlr ${PWD}/openmetadata-spec/src/main/antlr4/org/openmetadata/schema/*.g4

## Ingestion models generation
.PHONY: generate
generate:  ## Generate the pydantic models from the JSON Schemas to the ingestion module
	@echo "Running Datamodel Code Generator"
	@echo "Make sure to first run the install_dev recipe"
	rm -rf ingestion/src/metadata/generated
	mkdir -p ingestion/src/metadata/generated
	python scripts/datamodel_generation.py
	$(MAKE) py_antlr js_antlr
	ruff check --isolated --no-respect-gitignore --fix --select F401,UP006,UP007,UP035,UP045 --target-version py310 ingestion/src/metadata/generated
	$(MAKE) install

## Reference docs generation (deterministic; CI fails if the committed output drifts)
.PHONY: generate-entity-index
generate-entity-index:  ## Generate docs/generated/entity-index.md from schemas + resources
	python3 scripts/generate_entity_index.py

.PHONY: generate-api-reference
generate-api-reference:  ## Generate docs/generated/api-reference.md from JAX-RS resources
	python3 scripts/generate_api_reference.py

.PHONY: generate-reference-docs
generate-reference-docs: generate-entity-index generate-api-reference  ## Regenerate all docs/generated/*.md

.PHONY: harness-check
harness-check:  ## Warn on harness decay (dead refs, doc sizes, rule globs, generated-doc freshness)
	python3 scripts/harness/check_harness.py

.PHONY: install_antlr_cli
ANTLR_VERSION := 4.9.2
# Dots escaped so the banner match below is a real version match, not a
# regex wildcard, and so 4.9.20 cannot satisfy a 4.9.2 check.
ANTLR_VERSION_RE := $(subst .,\.,$(ANTLR_VERSION))
# install_antlr_cli resolves the CLI in three steps, cheapest first:
#
#   1. Already on PATH at the pinned version -> nothing to do.
#   2. Distro package, when apt offers exactly $(ANTLR_VERSION). Ubuntu noble and
#      later ship 4.9.2, matching the pinned antlr4-python3-runtime and the JS
#      antlr4 runtimes, so CI never touches a public artifact host - those
#      rate-limit our shared CI egress IP and have broken the build repeatedly.
#   3. Pinned, checksum-verified download (macOS, non-Debian images, or a distro
#      carrying a different ANTLR such as jammy's 4.7.2).
#
# The checksum is what makes step 3 trustworthy; the archive check next to it is a
# second opinion, so it reads the archive with whichever tool the host has rather
# than insisting on one. Requiring a JDK tool to install a CLI that only needs a
# JRE to run breaks slim runtime images (e.g. ingestion-base ships
# default-jre-headless, which has java but no jar) on a download that already
# verified clean. A tool that is present and rejects the archive still fails the
# build; only the case where no reader exists falls through to the checksum alone,
# and such a host has no java either, so it could not run the CLI regardless.
#
# The version match in step 2 is exact. A distro shipping a different ANTLR falls
# through to the download rather than silently generating parsers that the pinned
# runtimes will reject.
#
# For step 3, override ANTLR_MAVEN_BASE to pull from an internal Maven mirror
# instead of Central. The default primary is Google's Central mirror, which is
# CDN-backed and not subject to repo1's per-IP 429 throttling that breaks
# multi-arch Docker publishes; repo1 stays as the fallback if the mirror is
# unreachable. The pinned SHA-256 below verifies whatever is fetched, so the
# source is swappable without lowering trust.
ANTLR_MAVEN_BASE ?= https://maven-central.storage-download.googleapis.com/maven2
ANTLR_MAVEN_FALLBACK_BASE ?= https://repo1.maven.org/maven2
ANTLR_COMPLETE_JAR_PATH := org/antlr/antlr4/$(ANTLR_VERSION)/antlr4-$(ANTLR_VERSION)-complete.jar
ANTLR_COMPLETE_JAR_URL := $(ANTLR_MAVEN_BASE)/$(ANTLR_COMPLETE_JAR_PATH)
ANTLR_COMPLETE_JAR_FALLBACK_URL := $(ANTLR_MAVEN_FALLBACK_BASE)/$(ANTLR_COMPLETE_JAR_PATH)
ANTLR_COMPLETE_JAR_SHA256 := bb117b1476691dc2915a318efd36f8957c0ad93447fb1dac01107eb15fe137cd
ANTLR_INSTALL_DIR ?= /usr/local/bin

install_antlr_cli:  ## Install antlr CLI locally
	@set -eu; \
	if command -v antlr4 > /dev/null 2>&1 \
		&& antlr4 2>&1 | grep -Eq 'Version $(ANTLR_VERSION_RE)([^0-9]|$$)'; then \
		echo "ANTLR $(ANTLR_VERSION) already available at $$(command -v antlr4); nothing to do."; \
		exit 0; \
	fi; \
	if command -v apt-get > /dev/null 2>&1; then \
		candidate=$$(apt-cache policy antlr4 2>/dev/null | awk '/Candidate:/ {print $$2}'); \
		if [ -z "$$candidate" ] || [ "$$candidate" = "(none)" ]; then \
			apt-get update -qq > /dev/null 2>&1 || true; \
			candidate=$$(apt-cache policy antlr4 2>/dev/null | awk '/Candidate:/ {print $$2}'); \
		fi; \
		case "$$candidate" in \
			$(ANTLR_VERSION)|$(ANTLR_VERSION)[-+~]*) \
				if apt-get install -y -qq antlr4 > /dev/null 2>&1; then \
					if command -v antlr4 > /dev/null 2>&1 \
						&& antlr4 2>&1 | grep -Eq 'Version $(ANTLR_VERSION_RE)([^0-9]|$$)'; then \
						echo "Installed ANTLR $$candidate from the distro archive."; \
						exit 0; \
					fi; \
					echo "Distro package installed, but antlr4 on PATH resolves to $$(command -v antlr4 2>/dev/null || echo none) which is not $(ANTLR_VERSION); falling back to pinned download." >&2; \
				else \
					echo "apt-get install antlr4 failed; falling back to pinned download." >&2; \
				fi; \
				;; \
			*) \
				echo "Distro ANTLR candidate '$$candidate' is not $(ANTLR_VERSION); using pinned download." >&2; \
				;; \
		esac; \
	fi; \
	jar_file=$$(mktemp); \
	cli_file=$$(mktemp "$(ANTLR_INSTALL_DIR)/.antlr4.XXXXXX"); \
	trap 'rm -f "$$jar_file" "$$cli_file"' EXIT; \
	if command -v shasum > /dev/null 2>&1; then \
		sha_check="shasum -a 256 --check"; \
	elif command -v sha256sum > /dev/null 2>&1; then \
		sha_check="sha256sum --check"; \
	else \
		echo "Neither shasum nor sha256sum is available; cannot verify the ANTLR download." >&2; \
		exit 1; \
	fi; \
	urls=$$(printf '%s\n%s\n' "$(ANTLR_COMPLETE_JAR_URL)" "$(ANTLR_COMPLETE_JAR_FALLBACK_URL)" | awk 'NF && !seen[$$0]++'); \
	attempt=1; \
	while :; do \
		for url in $$urls; do \
			if curl --fail --location --silent --show-error \
				--retry 3 --retry-all-errors --retry-delay 2 --retry-max-time 120 \
				--connect-timeout 15 --max-time 60 \
				--output "$$jar_file" "$$url" \
				&& printf '%s  %s\n' "$(ANTLR_COMPLETE_JAR_SHA256)" "$$jar_file" | $$sha_check \
				&& { if command -v jar > /dev/null 2>&1; then \
					jar tf "$$jar_file" > /dev/null; \
				elif command -v unzip > /dev/null 2>&1; then \
					unzip -tqq "$$jar_file" > /dev/null; \
				else :; fi; }; then \
				break 2; \
			fi; \
			echo "ANTLR $(ANTLR_VERSION) download failed from $$url (attempt $$attempt)" >&2; \
		done; \
		if [ "$$attempt" -ge 3 ]; then \
			echo "Failed to download a valid ANTLR $(ANTLR_VERSION) CLI after $$attempt attempts" >&2; \
			exit 1; \
		fi; \
		attempt=$$((attempt + 1)); \
		sleep 2; \
	done; \
	printf '%s\n' '#!/usr/bin/java -jar' > "$$cli_file"; \
	cat "$$jar_file" >> "$$cli_file"; \
	chmod 755 "$$cli_file"; \
	mv "$$cli_file" "$(ANTLR_INSTALL_DIR)/antlr4"

## SNYK
SNYK_ARGS := --severity-threshold=high

# Drop pip's build/lib tree before scanning so `snyk code test` does not
# double-report findings (once under src/, once under build/lib/). Same
# applies to snyk-airflow-apis-report below.
.PHONY: snyk-ingestion-report
snyk-ingestion-report:  ## Uses Snyk CLI to validate the ingestion code and container. Don't stop the execution
	@echo "Validating Ingestion container..."
	docker build -t openmetadata-ingestion:scan -f ingestion/Dockerfile.ci .
	snyk container test openmetadata-ingestion:scan --file=ingestion/Dockerfile.ci $(SNYK_ARGS) --json > security-report/ingestion-docker-scan.json | true;
	@echo "Validating ALL ingestion dependencies. Make sure the venv is activated."
	cd ingestion; \
		pip freeze > scan-requirements.txt; \
		rm -rf build; \
		snyk test --file=scan-requirements.txt --package-manager=pip --command=python3 $(SNYK_ARGS) --json > ../security-report/ingestion-dep-scan.json | true; \
		snyk code test $(SNYK_ARGS) --json > ../security-report/ingestion-code-scan.json | true;

.PHONY: snyk-airflow-apis-report
snyk-airflow-apis-report:  ## Uses Snyk CLI to validate the airflow apis code. Don't stop the execution

## `SECURITY.md`

# Security Policy

## Supported Versions

Use this section to tell people about which versions of your project are
currently being supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 1.13.x   | :white_check_mark: |
| 1.12.x   | :white_check_mark: |

## Reporting a Vulnerability

Reporting security issues

If you think you have found a security vulnerability, please create a GitHub Security Advisory [here](https://github.com/open-metadata/OpenMetadata/security/advisories/new). This can be used for all of OpenMetadata products. 

The security advisory should be open in a draft mode. After the initial reply to your report, the OpenMetadata team will keep you informed of the progress towards a fix and full announcement, and may ask for additional information or guidance.

Important: We ask you to not disclose the vulnerability before it have been fixed and announced, unless you received a response from the OpenMetadata team that you can do so.

## `package.json`

{
  "name": "open-metadata",
  "version": "0.1.0",
  "private": true,
  "engines": {
    "node": ">=10.0.0",
    "yarn": "^1.22.0"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/open-metadata/OpenMetadata.git"
  },
  "devDependencies": {
    "quicktype": "20.0.27"
  },
  "resolutions": {
    "brace-expansion": "1.1.18",
    "lodash": "4.18.1",
    "stream-json": "3.5.0"
  },
  "scripts": {
    "preinstall": "yarn global add node-gyp@10.0.1",
    "test": "echo \"Error: no test specified\" && exit 1"
  }
}

## `docs/index.md`

# Documentation Index

The map to OpenMetadata's written knowledge — design docs, plans, generated references, and the
reference docs that live *outside* `docs/` (in the UI, ingestion, and bootstrap trees). Use it to
find an existing doc before reverse-engineering the code or guessing.

**Freshness** was verified against the working tree on **2026-07-24** (not inferred from age — each
verdict cites an artifact that was checked to still exist):

- **CURRENT** — its load-bearing references still exist and match the code.
- **STALE** — it references paths/classes/flags that no longer exist.
- **SUPERSEDED** — a newer doc or implementation replaced it (named in the row / footnotes).
- **⚠** — CURRENT overall, but with a specific caveat in the footnotes below.
- **by construction** — regenerated from source and CI-gated, so it cannot drift from its source.

> This index lists one file each; it does not move or relink anything (migration is out of scope).

## Start here — root guides (not under `docs/`)

| Guide | What it is |
|---|---|
| `CLAUDE.md` | Always-loaded session guidance; the pointer index to `.claude/rules/*` and skills |
| `ARCHITECTURE.md` | System map — modules, the request/ingestion/search paths, the invariants that hold |
| `DEVELOPER.md` | How to build, test, and add an entity or connector (end-to-end checklists) |
| `AGENTS.md` | Codex entry doc — **carries known contradictions** (Webpack→Vite, antd, Python ceiling); see `docs/tech-debt.md` #6 |

## Backend & platform design docs (`docs/`)

| Doc | Purpose | Read when | Modified | Freshness |
|---|---|---|---|---|
| `docs/impersonation-design.md` | Bot→user impersonation: `updatedBy`=user / `impersonatedBy`=bot, gated by `allowImpersonation` + RBAC `Impersonate` policy scoping | Touching bot impersonation auth — the flag, `BotImpersonationPolicy` seeds, `checkImpersonationAuthorization` (§4.4 is authoritative) | 2026-06-16 | CURRENT ⚠¹ |
| `docs/session-management-multi-node-design.md` | Shipped multi-node server-side session + websocket system: shared JDBC/Redis store, `OM_SESSION` cookie, session-bound JWTs, CAS refresh | Working on login/refresh/logout across pods, `SessionService`/`SessionStore`, JWT session validation, websocket handshake | 2026-06-03 | CURRENT |
| `docs/streamable-logs.md` | S3/MinIO-backed streamable ingestion logs: HTTP append/close, `partial.txt`→`logs.txt`, SSE live tail, abandoned-run sweeper | Working on ingestion log storage/streaming — `S3LogStorage`, `LogStorageInterface`, `/logs/{fqn}/{runId}` endpoints | 2026-05-15 | CURRENT |
| `docs/ingestion-log-streaming.md` | Live log tail over SSE: `LogStreamEvent` schema, resume cursors, one shared reader per run, and the limits that bound every stream | Building or debugging a client that tails ingestion logs live — `/logs/{fqn}/stream/{runId}`, `IngestionLogTailer`, `LogStreamSettings` | 2026-08-10 | CURRENT |
| `docs/rdf-local-development.md` | Run RDF/knowledge-graph support locally with Apache Jena Fuseki — startup scripts, env vars, `rdf.*` config, `/api/v1/rdf/*`, `RdfIndexApp` | Setting up or debugging local RDF/Fuseki development | 2026-07-16 | CURRENT |
| `docs/rdf-production-setup.md` | Production sizing/tuning for a remote Fuseki triple store — TDB2 heap vs page-cache, batch/timeout, weekly recreate, compaction | Sizing, scheduling, or troubleshooting a prod Fuseki deployment; tuning RDF bulk-write | 2026-07-16 | CURRENT |
| `docs/rdf-ontology-contract.md` | RDF predicate availability, canonical lineage direction, extension key/value projection, and contract tests | Adding RDF predicates or upgrading an existing RDF store | 2026-09-08 | CURRENT |
| `docs/rdf-scale-validation.md` | Full catalog RDF rebuild, query latency, resource sampling, interrupted rebuild, and restart validation | Reproducing RDF capacity measurements or evaluating #32057 | 2026-09-08 | CURRENT |
| `docs/csv-relation-types-plan.md` | Carry glossary term relation types through CSV export/import via a `relationType:termFQN` prefix (default `relatedTo`) | Modifying glossary CSV round-tripping — `CsvUtil.addTermRelations`, `GlossaryRepository.getTermRelationsFromCsv` | 2026-03-17 | CURRENT |
| `docs/auto-classification/add-support-for-another-entity.md` | Step-by-step: extend auto-classification (PII + sample data) to a new entity across schema/Java/Python/UI via the `EntityAdapter` registry | Adding auto-classification/sample-data support for a new entity type | 2026-05-19 | CURRENT |
| `docs/perf/cdn-deployment-guide.md` | AWS design proposal: per-customer/per-release UI bundles from one CloudFront + S3 via an embedded CloudFront Function router (no Lambda@Edge) | Planning/reviewing CDN delivery of the UI bundle + per-customer version pinning — infra design, not existing code | 2026-05-25 | CURRENT (unimplemented proposal) |

## Plans & specs (`docs/plans/`, `docs/superpowers/`)

| Doc | Purpose | Read when | Modified | Freshness |
|---|---|---|---|---|
| `docs/plans/2026-01-27-search-indexing-stats-redesign.md` | Rework `SearchIndexingApp` stats into a per-stage pipeline model (`StageStatsTracker`/`StageCounter`), index-alias promotion, vector bulk processor | Before touching search reindex stats, `search_index_server_stats`, index promotion, vector indexing | 2026-01-29 | CURRENT (shipped design) |
| `docs/plans/2026-06-22-bulk-deletion-redesign.md` | Fast, orphan-free, resumable service-level recursive hard-deletion by id-set; self-audits what landed on `main` vs remaining gaps | Before working on recursive/bulk deletion, `entity_relationship` orphan cleanup, the deletion-lock gate | 2026-06-26 | CURRENT (shipped design) |
| `docs/superpowers/specs/2026-06-22-logviewer-modal-design.md` | Design spec for the reusable `LogViewerModal` (dark terminal modal over `@melloware/react-logviewer`); self-marked "Implemented; revised 2026-06-24" | Before modifying `LogViewerModal`, its log-level parser, theming, or streaming container/hook | 2026-07-16 | CURRENT |
| `docs/superpowers/plans/2026-06-22-logviewer-modal.md` | Original TDD build plan for `LogViewerModal` (built-in LazyLog search, `CopyToClipboardButton`) | Historical context only — the shipped component follows the revised spec, not this plan | 2026-07-16 | SUPERSEDED ² |

## Generated references (`docs/generated/`)

| Doc | Purpose | Read when | Modified | Freshness |
|---|---|---|---|---|
| `docs/generated/entity-index.md` | Auto-generated: 81 first-class entities → schema JSON, Java POJO, Python model, TS type, REST resource class | Locate every codegen artifact / the REST resource for an entity without grepping four trees | 2026-07-24 | CURRENT (by construction) ³ |
| `docs/generated/api-reference.md` | Auto-generated: all 1748 REST endpoints (method + path + `@Operation` summary) grouped by resource package | Find an endpoint's exact path/method, or enumerate a package's routes without reading JAX-RS classes | 2026-07-24 | CURRENT (by construction) ³ |

## Repo audit & quality (`docs/`)

| Doc | Purpose | Read when | Modified | Freshness |
|---|---|---|---|---|
| `docs/golden-principles.md` | 8 candidate repo-wide invariants (DRAFT for ratification), each with a measured adherence number + reproducing command | Cite/enforce an invariant (acyclic modules, ServiceSpec contract, generated-as-sink, no bare `except:`, …) | 2026-07-24 | CURRENT |
| `docs/tech-debt.md` | Prioritized (impact÷size, 3 tiers) ledger of 21 audit findings, each with location, size, and agent-fixability | Pick up a bounded cleanup, or understand a known structural debt before working near it | 2026-07-24 | CURRENT |
| `docs/quality.md` | One evidence-cited quality grade (A–C / Not assessed) per Maven module | Gauge a module's structural health / known debt before a large change | 2026-07-24 | CURRENT |

## Assets (`docs/assets/`)

| Doc | Purpose | Read when | Modified | Freshness |
|---|---|---|---|---|
| `docs/assets/` (4 PNGs) | Architecture/marketing diagrams for the "Open Context Layer for AI" — hero, architecture, context graph, memory-primitives | Editing the root `README.md` visuals | 2026-06-10 | CURRENT (sole consumer: root `README.md`) |

## UI reference docs (outside `docs/`)

| Doc | Purpose | Read when | Modified | Freshness |
|---|---|---|---|---|
| `openmetadata-ui/src/main/resources/ui/DEVELOPER_HANDBOOK.md` | **UI folder structure + file naming spec.** Layers (`components/`, `pages/`, `rest/`, `utils/`, `hooks/`) stay top-level, grouped inside by `domain/feature/`; five domains (`discovery`, `governance`, `observability`, `insights`, `platform`) with cross-cutting features at the domain level. New files use one stem + role suffix (`GlossaryList.tsx`, `.types.ts`, `.utils.ts`, `.test.tsx`); legacy uses `.component.tsx`/`.interface.ts`. Also covers imports, barrels, routing and state locations | **Before creating any new file under `ui/src/`**, or when deciding where code belongs | 2026-08-21 | CURRENT |
| `openmetadata-ui/src/main/resources/ui/specs/` | **Machine-readable design system** (41 files). `README.md` declares two stacks — **go-forward = UntitledUI + Tailwind (`tw:`)**, **legacy (deprecated) = Ant Design + Less** — plus `foundations/*` (color, spacing, typography, radius, elevation, motion), `tokens/*` (Tailwind-utility + master token reference), `untitled/*` (go-forward component specs), and legacy `components/*` | **Before writing or modifying any UI code** — start at `specs/README.md`, then the `foundations`/`tokens` and the `untitled/<component>.md` (or legacy `components/*`) spec for what you touch | 2026-07-27 | CURRENT ⁶ |
| `openmetadata-ui/src/main/resources/ui/docs/colors.md` | Semantic color-token system (`tw:bg-primary`, `tw:text-fg-*`, `tw:border-*`) with light/dark values + the mandatory `ring`→`border` migration (§2.3.1) | Before writing/reviewing any Tailwind color class or dark-mode styling, or when tempted to use `ring-*` or a raw hex | 2026-07-23 | CURRENT |
| `openmetadata-ui/src/main/resources/ui/docs/formutils.md` | The modern react-hook-form + react-aria form stack (`FieldProp`, `getField`/`FormFields`/`HookForm`) vs the legacy antd `@utils/formUtils` API | Before building/modifying any UI form — which API to use, and wiring to `useFormDrawerWithHook` + a pure transform | 2026-07-15 | CURRENT |
| `openmetadata-ui/src/main/resources/ui/playwright/docs/` | Auto-generated E2E test-coverage catalog (`README.md` + Discovery/Governance/Integration/Observability/Platform) mapping component → spec file → scenarios | Check what UI behavior is already E2E-covered before writing Playwright tests or reasoning about gaps | 2026-03-09 – 2026-07-16 | CURRENT (by construction) ³ |

## Ingestion & bootstrap reference (outside `docs/`)

| Doc | Purpose | Read when | Modified | Freshness |
|---|---|---|---|---|
| `ingestion/docs/design/ingestion-diagnostics.md` | DEBUG-gated ingestion diagnostics subsystem (operation registry, watchdog, heartbeat, memory tracker, HTTP introspection, stage backpressure, signal dumps) | Understand why/how the diagnostics subsystem works before instrumenting ingestion hangs/OOMs | 2026-05-20 | CURRENT ⚠⁴ |
| `bootstrap/MIGRATION_SYSTEM.md` | Hybrid DB-migration architecture — Flyway→native→extension execution order, `SERVER_CHANGE_LOG` tracking, file layout (Flyway *parsers* only, not the Flyway runner) | Before adding/debugging a migration under `bootstrap/sql/migrations/`, or reasoning about ordering / tracking tables / MySQL+Postgres dual paths | 2025-10-28 | CURRENT ⚠⁵ |

## Caveats (verification notes)

1. **impersonation-design** — §4.4 (v1.1) is authoritative and matches shipped code (`allowImpersonation` in `createBot.json`/`user.json`, `checkImpersonationAuthorization` in `DefaultAuthorizer.java`, the four policy/role seeds, `BotImpersonationIT`). The earlier §4.1/4.2 `POST /users/impersonate` token-exchange endpoint was **never shipped** — impersonation uses the `X-Impersonate-User` header (`JwtFilter.java`), which §4.4 supersedes 4.1/4.2 to reflect. Read §4.4.
2. **logviewer-modal plan** — superseded by the **2026-06-24 revision** of the design spec (row above): the plan's built-in LazyLog search + `CopyToClipboardButton` were reversed (search moved to the header, a footer status bar added). The shipped dir (`LogViewerModal.utils.tsx`, `LogsViewerModalContainer.tsx`, `useLogStream.ts`) follows the revised spec, not this plan.
3. **by construction** — `docs/generated/*` are regenerated by `make generate-reference-docs` and gated by the reference-docs freshness CI job; the Playwright docs by `playwright/doc-generator/generate.js` + the `playwright-docs-check.yml` workflow. They cannot drift from their source on the watched paths. (One benign lag: the Playwright `README.md` roll-up footer reads `2026-03-09` while `Governance.md` regenerated `2026-07-16`; self-corrects on the next spec-touching PR.)
4. **ingestion-diagnostics** — the design **shipped** (`ingestion/src/metadata/ingestion/diagnostics/`, activated at `loggerLevel == DEBUG`, installed in `metadata/workflow/base.py`), but the doc's §5/§7 *flat file map drifted*: files now live under `collectors/`, `monitors/`, `samplers/`; there is no standalone `heartbeat.py`; wire-in is `base.py`, not the doc's `base_workflow.py`. Treat the file map as design-era, the behavior as current.
5. **MIGRATION_SYSTEM** — accurate (the `flyway/`+`native/` layout, `SERVER_CHANGE_LOG`, `MigrationWorkflow`/`FlywayMigrationFile`, and `conf/openmetadata.yaml` `flywayPath`/`nativePath`/`extensionPath` all verified) except: the runner class is `MigrationProcessImpl` (doc says `MigrationProcess`), and the `extensions/` dir is not materialized on disk (`extensionPath: ""`) though the path is still supported.
6. **ui/specs** — tracked (41 files) and CURRENT: all four audit commands its `README.md` cites resolve to real `package.json` scripts (`tw-audit`, `tw-audit:report`, `tw-guard`, `token-audit`), and the two-stack policy it states (go-forward UntitledUI+Tailwind, legacy Antd+Less deprecated) matches the enforced rules — `tw-guard` blocks new `antd` imports / new `.less` files, and `.claude/rules/frontend-styling.md` routes agents into `specs/README.md`.

---

*Not indexed:* `docs/harness-audit/` exists in the working tree but is **untracked** (working audit notes, intentionally out of version control), so it is not part of the committed knowledge base.

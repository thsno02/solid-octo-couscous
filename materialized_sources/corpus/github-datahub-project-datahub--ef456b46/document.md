# Repository semantic capsule: datahub-project/datahub

- Commit: `6ece48b05a2a260e6c9df8aec4be5f7f1e7deca6`
- Default branch: `master`
- Description: datahub-project/datahub
- Selected evidence files: 5 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

<!--HOSTED_DOCS_ONLY
import useBaseUrl from '@docusaurus/useBaseUrl';

export const Logo = (props) => {
  return (
    <div style={{ display: "flex", justifyContent: "center", padding: "20px", height: "190px" }}>
      <img
        alt="DataHub Logo"
        src="https://raw.githubusercontent.com/datahub-project/static-assets/main/imgs/datahub-logo-color-mark.svg"
        {...props}
      />
    </div>
  );
};

<Logo />

<!--
HOSTED_DOCS_ONLY-->
<p align="center">
<a href="https://datahub.com">
<img alt="DataHub" src="https://raw.githubusercontent.com/datahub-project/static-assets/main/imgs/datahub-logo-color-mark.svg" height="150" />
</a>
</p>
<!-- -->

# The #1 Open Source AI Data Catalog

_Enterprise-grade metadata platform enabling discovery, governance, and observability across your entire data ecosystem_

<p align="center">
  <a href="https://github.com/datahub-project/datahub/actions/workflows/build-and-test.yml">
    <img src="https://github.com/datahub-project/datahub/actions/workflows/build-and-test.yml/badge.svg" alt="Build Status" />
  </a>
  <a href="https://pypi.org/project/acryl-datahub/">
    <img src="https://img.shields.io/pypi/v/acryl-datahub.svg" alt="PyPI Version" />
  </a>
  <a href="https://pypi.org/project/acryl-datahub/">
    <img src="https://img.shields.io/pypi/dm/acryl-datahub.svg" alt="PyPI Downloads" />
  </a>
  <a href="https://hub.docker.com/r/linkedin/datahub-gms">
    <img src="https://img.shields.io/docker/pulls/linkedin/datahub-gms.svg" alt="Docker Pulls" />
  </a>
  <br />
  <a href="https://datahub.com/slack?utm_source=github&utm_medium=readme&utm_campaign=github_readme">
    <img src="https://img.shields.io/badge/slack-join_chat-white.svg?logo=slack&style=social" alt="Join Slack" />
  </a>
  <a href="https://www.youtube.com/@DataHubCloud">
    <img src="https://img.shields.io/youtube/channel/subscribers/UC3qFQC5IiwR5fvWEqi_tJ5w?style=social&logo=youtube&label=Subscribe" alt="YouTube Subscribers" />
  </a>
  <a href="https://datahub.com/blog/">
    <img src="https://img.shields.io/badge/blog-read-red.svg?style=social&logo=medium" alt="DataHub Blog" />
  </a>
  <a href="https://github.com/datahub-project/datahub/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/datahub-project/datahub.svg" alt="Contributors" />
  </a>
  <a href="https://github.com/datahub-project/datahub/stargazers">
    <img src="https://img.shields.io/github/stars/datahub-project/datahub.svg?style=social&label=Star" alt="GitHub Stars" />
  </a>
  <a href="https://github.com/datahub-project/datahub/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License" />
  </a>
</p>

<p align="center">
  <a href="https://datahub.com/free-trial/"><b>Free Cloud Trial</b></a> •
  <a href="https://docs.datahub.com/docs/quickstart"><b>Quick Start</b></a> •
  <a href="https://demo.datahub.com"><b>Live Demo</b></a> •
  <a href="https://docs.datahub.com"><b>Documentation</b></a> •
  <a href="https://datahub.com/slack"><b>Slack Community</b></a> •
  <a href="https://www.youtube.com/@DataHubCloud"><b>YouTube</b></a>
</p>

<p align="center">
  <i>Built with ❤️ by <a href="https://datahub.com">DataHub</a> and <a href="https://engineering.linkedin.com">LinkedIn</a></i>
</p>

---

<p align="center">
  <a href="https://demo.datahub.com">
    <img width="90%" src="https://raw.githubusercontent.com/datahub-project/static-assets/refs/heads/main/imgs/demos/datahub-tour.gif" alt="DataHub Product Tour" />
  </a>
</p>

<p align="center">
  <i>Search, discover, and understand your data with DataHub's unified metadata platform</i>
</p>

---

### 📊 **NEW: Open Source Analytics Agent**

<p align="center">
  <a href="https://youtu.be/qqFUewpnGYg?si=0F51_nIKpl3f1ryC&t=3215">
    <img width="600" src="https://raw.githubusercontent.com/datahub-project/static-assets/refs/heads/main/imgs/analytics-agent/screenshot-chat.png" alt="Analytics Agent answering a data question with a chart" />
  </a>
  <br/>
  <i>Ask data questions in plain English — get SQL, results, and charts back</i>
</p>

Open-source agent grounded in your DataHub catalog. Apache 2.0. Bring your own LLM.

**Quick start:**

```bash
git clone https://github.com/datahub-project/analytics-agent.git
cd analytics-agent && bash quickstart.sh
```

[Read the announcement →](https://datahub.com/blog/datahub-analytics-agent/) · [Docs →](https://docs.datahub.com/docs/features/feature-guides/analytics-agent) · [Repo →](https://github.com/datahub-project/analytics-agent)

> **Using AI coding assistants?** Connect Cursor, Claude Desktop, or Cline directly to DataHub via the [Model Context Protocol](https://github.com/acryldata/mcp-server-datahub): `npx -y @acryldata/mcp-server-datahub init`

---

## What is DataHub?

> **🔍 Finding the right DataHub?** This is the **open-source metadata platform** at [datahub.com](https://datahub.com) (GitHub: [datahub-project/datahub](https://github.com/datahub-project/datahub)). It was previously hosted at `datahubproject.io`, which now redirects to [datahub.com](https://datahub.com). This project is **not related to** [datahub.io](https://datahub.io), which is a separate public dataset hosting service. See the [FAQ](#-frequently-asked-questions) below.

**DataHub is the #1 open-source AI data catalog** that enables discovery, governance, and observability across your entire data ecosystem. Originally built at LinkedIn, DataHub now powers data discovery at thousands of organizations worldwide, managing millions of data assets.

**The Challenge:** Modern data stacks are fragmented across dozens of tools—warehouses, lakes, BI platforms, ML systems, AI agents, orchestration engines. Finding the right data, understanding its lineage, and ensuring governance is like searching through a maze blindfolded.

**The DataHub Solution:** DataHub acts as the central nervous system for your data stack—connecting all your tools through real-time streaming or batch ingestion to create a unified metadata graph. Unlike static catalogs, DataHub keeps your metadata fresh and actionable—powering both human teams and AI agents.

![DataHub for Humans and AI](https://raw.githubusercontent.com/datahub-project/static-assets/refs/heads/main/imgs/datahub_for_human_and_ai.png)

### Why DataHub?

- **🚀 Battle-Tested at Scale:** Born at LinkedIn to handle hyperscale data, now proven at thousands of organizations worldwide managing millions of data assets
- **⚡ Real-Time Streaming:** Metadata updates in seconds, not hours or days
- **🤖 AI-Ready:** Native support for AI agents via MCP, LLM integrations, and context management
- **🔌 Pioneering Ingestion Architecture:** Flexible push/pull framework (widely adopted by other catalogs) with 80+ production-grade connectors extracting deep metadata—column lineage, usage stats, profiling, and quality metrics
- **👨‍💻 Developer-First:** Rich APIs (GraphQL, OpenAPI), Python + Java SDKs, CLI tools
- **🏢 Enterprise Ready:** Battle-tested security, authentication, authorization, and audit trails
- **🌍 Open Source:** Apache 2.0 licensed, vendor-neutral, community-driven

---

## 🧠 The Context Foundation

Essential for modern data teams and reliable AI agents:

- **[Context Management Is the Missing Piece in the Agentic AI Puzzle](https://datahub.com/blog/context-management-is-the-missing-piece-in-the-agentic-ai-puzzle/)** - Why context management is essential for deploying reliable AI agents at scale
- **[Data Lineage: What It Is and Why It Matters](https://datahub.com/blog/data-lineage-what-it-is-and-why-it-matters/)** - Understanding the map of how data flows through your organization
- **[What is Metadata Management?](https://datahub.com/blog/what-is-metadata-management/)** - A comprehensive guide for enterprise data leaders

---

## 📑 Table of Contents

- [FAQ](#-frequently-asked-questions)
- [See DataHub in Action](#-see-datahub-in-action)
- [Quick Start](#-quick-start)
- [Installation Options](#-installation-options)
- [Architecture](#-architecture-overview)
- [Use Cases & Examples](#-use-cases--examples)
- [Trusted By](#-trusted-by-industry-leaders)
- [Ecosystem](#-datahub-ecosystem)
- [Community](#-community--support)
- [Contributing](#-contributing)
- [Resources](#-resources--learning)
- [License](#-license)

---

## ❓ Frequently Asked Questions

<details>
<summary><b>Is this the same project as datahub.io?</b></summary>

No. [datahub.io](https://datahub.io) is a completely separate project — a public dataset hosting service with no affiliation to this project. DataHub (this project) is an open-source metadata platform for data discovery, governance, and observability, hosted at [datahub.com](https://datahub.com) and developed at [github.com/datahub-project/datahub](https://github.com/datahub-project/datahub).

</details>

<details>
<summary><b>What happened to datahubproject.io?</b></summary>

DataHub was previously hosted at `datahubproject.io`. That domain now redirects to [datahub.com](https://datahub.com). All documentation has moved to [docs.datahub.com](https://docs.datahub.com/docs/quickstart). If you find references to `datahubproject.io` in blog posts or tutorials, they refer to this same project — just under its former domain.

</details>

<details>
<summary><b>Is DataHub related to LinkedIn's internal DataHub?</b></summary>

Yes. DataHub was originally built at LinkedIn to manage metadata at scale across their data ecosystem. LinkedIn open-sourced DataHub in 2020. It has since grown into an independent community project under the [datahub-project](https://github.com/datahub-project) GitHub organization, now hosted at [datahub.com](https://datahub.com).

</details>

<details>
<summary><b>How do I install the DataHub metadata platform?</b></summary>

```bash
# macOS / Linux (simplest)
brew install datahub-project/tap/datahub

# Or via pip (any platform)
pip install acryl-datahub

datahub docker quickstart
```

See the [Quick Start](#-quick-start) section below for full instructions. The PyPI package is [`acryl-datahub`](https://pypi.org/project/acryl-datahub/); the Homebrew tap is [`datahub-project/homebrew-tap`](https://github.com/datahub-project/homebrew-tap).

</details>

---

## 🎨 See DataHub in Action

<table>
  <tr>
    <td width="50%">
      <img src="https://raw.githubusercontent.com/datahub-project/static-assets/main/imgs/search/search-results-page.png" alt="Universal Search" width="100%"/>
      <p align="center"><b>🔍 Universal Search</b><br/>Find any data asset instantly across your entire stack</p>
    </td>
    <td width="50%">
      <img src="https://raw.githubusercontent.com/datahub-project/static-assets/main/imgs/lineage/column-level-lineage-v3.png" alt="Column-Level Lineage" width="100%"/>
      <p align="center"><b>📊 Column-Level Lineage</b><br/>Trace data flow from source to consumption</p>

## `AGENTS.md`

# DataHub — Agent Development Guide

This is the canonical reference for working with the DataHub codebase. It applies to all coding
agents (Claude Code, Cursor, Codex CLI, Devin, etc.) and human developers alike.

## Code Navigation (LSP)

Prefer LSP tools over Grep for code navigation tasks:

- Use `goToDefinition` to find where something is defined
- Use `findReferences` to find all call sites
- Use `workspaceSymbol` to find symbols by name
- Use diagnostics after any edit to catch type errors immediately

See [docs/lsp-setup.md](docs/lsp-setup.md) for installation and configuration.

## Essential Commands

**Build and test:**

```bash
./gradlew build           # Build entire project
./gradlew check           # Run all tests (Python/JS lint lives in lint-jobs.yml / :module:lint)
./gradlew lintCheck       # Run all lint checks (Python, JS, GraphQL, markdown, Java)
./gradlew lintFix         # Auto-fix all lint issues
./gradlew format          # Format all code (Java, Markdown, GraphQL, YAML)

# Note that each directory typically has a build.gradle file, but the available tasks follow similar conventions.

# Java code.
./gradlew spotlessApply   # Java code formatting

# Python code.
./gradlew :metadata-ingestion:testQuick     # Fast Python unit tests
./gradlew :metadata-ingestion:lint          # Python linting (ruff, mypy)
./gradlew :metadata-ingestion:lintFix       # Python linting auto-fix (ruff only)

# Markdown, GraphQL, YAML formatting
./gradlew :datahub-web-react:mdPrettierWrite        # Format markdown files
./gradlew :datahub-web-react:graphqlPrettierWrite   # Format GraphQL schemas
./gradlew :datahub-web-react:githubActionsPrettierWrite # Format GitHub Actions
```

**IMPORTANT: Verifying Python code changes:**

- **ALWAYS use `./gradlew :metadata-ingestion:lintFix`** to verify Python code changes
- **NEVER use `python3 -m py_compile`** - it doesn't catch style issues or type errors
- **NEVER use `ruff` or `mypy` commands directly** - use the Gradle task instead
- lintFix runs ruff formatting and fixing automatically, ensuring code quality
- For smoke-test changes, the lintFix command will also check those files

## Code Formatting and Linting

**CRITICAL: Always use Gradle tasks for formatting and linting. Never use npm/yarn/npx commands directly.**

### Available Formatting Tasks

**Format everything:**

```bash
./gradlew lintCheck           # Run all lint checks (Python, JS, GraphQL, markdown, Java)
./gradlew lintFix             # Auto-fix all lint issues
./gradlew format              # Format all code (Java, Markdown, GraphQL, YAML)
./gradlew formatChanged       # Format only changed files (faster)
```

**Format specific file types:**

```bash
# Markdown files
./gradlew :datahub-web-react:mdPrettierWrite        # Format all markdown
./gradlew :datahub-web-react:mdPrettierCheck        # Check markdown formatting

# GraphQL schemas
./gradlew :datahub-web-react:graphqlPrettierWrite   # Format GraphQL files
./gradlew :datahub-web-react:graphqlPrettierCheck   # Check GraphQL formatting

# GitHub Actions YAML
./gradlew :datahub-web-react:githubActionsPrettierWrite   # Format workflow files
./gradlew :datahub-web-react:githubActionsPrettierCheck   # Check workflow files

# Java code
./gradlew spotlessApply       # Format Java code

# Python code
./gradlew :metadata-ingestion:lintFix      # Format and fix Python code
./gradlew :metadata-ingestion:lint         # Check Python formatting
```

### When CI Formatting Checks Fail

If you see CI failures like:

- `markdown_format / markdown_format_check (pull_request)` - Use `./gradlew :datahub-web-react:mdPrettierWrite`
- `graphql_prettier_check` - Use `./gradlew :datahub-web-react:graphqlPrettierWrite`
- `spotless-check` - Use `./gradlew spotlessApply`
- Python linting failures - Use `./gradlew :metadata-ingestion:lintFix`

**Never do this:**

```bash
npx prettier --write "docs/**/*.md"    # WRONG - bypasses Gradle
yarn prettier --write                   # WRONG - bypasses Gradle
npm run format                          # WRONG - bypasses Gradle
```

**Always do this:**

```bash
./gradlew :datahub-web-react:mdPrettierWrite      # CORRECT - uses Gradle
./gradlew format                                   # CORRECT - formats everything
```

### Why Use Gradle Tasks?

1. **Consistent configuration**: Gradle tasks use the project's Prettier config
2. **Pre-commit hook integration**: Gradle tasks match what CI runs
3. **Dependency management**: Ensures correct tool versions
4. **Cross-platform**: Works reliably across all environments

**Java SDK v2 integration tests:**

See [metadata-integration/java/datahub-client/CLAUDE.md](metadata-integration/java/datahub-client/CLAUDE.md) for detailed integration test documentation.

## Architecture Overview

DataHub is a **schema-first, event-driven metadata platform** with three core layers:

### Core Services

- **GMS (Generalized Metadata Service)**: Java/Spring backend handling metadata storage and REST/GraphQL APIs
- **Frontend**: React/TypeScript application consuming GraphQL APIs
- **Ingestion Framework**: Python CLI and connectors for extracting metadata from data sources
- **Event Streaming**: Kafka-based real-time metadata change propagation

### Key Modules

- `metadata-models/`: Avro/PDL schemas defining the metadata model
- `metadata-service/`: Backend services, APIs, and business logic
- `datahub-web-react/`: Frontend React application
- `metadata-ingestion/`: Python ingestion framework and CLI
- `datahub-graphql-core/`: GraphQL schema and resolvers

Most of the non-frontend modules are written in Java. The modules written in Python are:

- `metadata-ingestion/`
- `datahub-actions/`
- `metadata-ingestion-modules/airflow-plugin/`
- `metadata-ingestion-modules/gx-plugin/`
- `metadata-ingestion-modules/dagster-plugin/`
- `metadata-ingestion-modules/prefect-plugin/`

Each Python module has a gradle setup similar to `metadata-ingestion/` (documented above)

### Metadata Model Concepts

- **Entities**: Core objects (Dataset, Dashboard, Chart, CorpUser, etc.)
- **Aspects**: Metadata facets (Ownership, Schema, Documentation, etc.)
- **URNs**: Unique identifiers (`urn:li:dataset:(urn:li:dataPlatform:mysql,db.table,PROD)`)
- **MCE/MCL**: Metadata Change Events/Logs for updates
- **Entity Registry**: YAML config defining entity-aspect relationships (`metadata-models/src/main/resources/entity-registry.yml`)

### Validation Architecture

**IMPORTANT**: Validation must work across all APIs (GraphQL, OpenAPI, RestLI).

- **Never add validation in API-specific layers** (GraphQL resolvers, REST controllers) - this only protects one API
- **Always implement AspectPayloadValidators** in `metadata-io/src/main/java/com/linkedin/metadata/aspect/validation/`
- **Register as Spring beans** in `SpringStandardPluginConfiguration.java`
- **Follow existing patterns**: See `SystemPolicyValidator.java` and `PolicyFieldTypeValidator.java` as examples

### Authorization Architecture

When adding an entity or API:

- Enforce authorization across GraphQL, OpenAPI, and Rest.li
- Keep basic entity CRUD permissions alongside any higher-level, entity-specific permissions
- Use `AuthorizationUtils` for GraphQL and `AuthUtil.isAPIAuthorized*` for REST APIs
- Put shared aspect rules in an `AbstractAspectAuthorizationValidator`
- Apply view-based access controls by default; only set `viewUnrestricted: true` for intentionally public entities
- Add allowed and denied access tests

## Development Flow

1. **Schema changes** in `metadata-models/` trigger code generation across all languages
2. **Backend changes** in `metadata-service/` and other Java modules expose new REST/GraphQL APIs
3. **Frontend changes** in `datahub-web-react/` consume GraphQL APIs
4. **Ingestion changes** in `metadata-ingestion/` emit metadata to backend APIs

## Working on Docs

The docs site is a **Docusaurus 2** app in `docs-website/`. It runs on **port 3001** (not 3000, to avoid
conflicting with the frontend dev server).

### Quick start

```bash
scripts/dev/datahub-dev.sh docs            # fast start (assumes prior build)
scripts/dev/datahub-dev.sh docs --build    # full rebuild (runs docGen + yarnGenerate first)
```

Or via Gradle directly: `./gradlew :docs-website:yarnStart` (always does a full build).

### How the docs site is assembled

The final site is assembled at build time into `docs-website/genDocs/` (gitignored) —
see `docs-website/AGENTS.md` for the full pipeline.

### Where docs live

| Path                                           | What to edit                                    | Detail guide                                |
| ---------------------------------------------- | ----------------------------------------------- | ------------------------------------------- |
| `docs/`                                        | Hand-authored feature guides, API docs, how-tos | _(this section)_                            |
| `metadata-ingestion/docs/sources/<connector>/` | Connector docs (`*_pre.md`, `*_post.md`, etc.)  | `metadata-ingestion/docs/sources/AGENTS.md` |
| `metadata-models/docs/entities/`               | Entity descriptions (input to `modelDocGen`)    | `metadata-models/docs/AGENTS.md`            |
| `docs-website/src/pages/`                      | Custom React pages (e.g. `/integrations`)       | `docs-website/AGENTS.md`                    |
| `docs-website/src/learn/`                      | Blog / learning articles (served at `/learn`)   | `docs-website/AGENTS.md`                    |
| `docs-website/sidebars.js`                     | Sidebar navigation tree                         | `docs-website/AGENTS.md`                    |
| `docs-website/static/`                         | Images, logos, static assets                    | `docs-website/AGENTS.md`                    |
| `docs/generated/`                              | **Never edit** — auto-generated                 |                                             |

## `CLAUDE.md`

# CLAUDE.md

@AGENTS.md

## `SECURITY.md`

---
description: "Report security vulnerabilities in DataHub Core or DataHub Cloud to security@datahub.com, with optional PGP-encrypted submissions."
---

# Reporting Security Issues

If you think you have found a security vulnerability, please send a report to security@datahub.com. This address can be used for all of DataHub’s open source and commercial products (including but not limited to DataHub Core and DataHub Cloud). We can accept only vulnerability reports at this address.

It's not mandatory, but if you'd like to encrypt your message to us; please use our PGP key. The key fingerprint is:

61C8 635F 856A 97AA 90D2 E1D9 EBD4 FB71 D997 8918

The key is available from [keys.openpgp.org](https://keys.openpgp.org/search?q=61C8635F856A97AA90D2E1D9EBD4FB71D9978918).

DataHub will send you a response indicating the next steps in handling your report. After the initial reply to your report, the security team will keep you informed of the progress towards a fix and full announcement, and may ask for additional information or guidance.

**Important:** We ask you to not disclose the vulnerability before it have been fixed and announced, unless you received a response from the DataHub security team that you can do so.

## Security announcements

We maintain [Security Advisories](https://github.com/datahub-project/datahub/security/advisories) on the DataHub project GitHub repository,
where we will post a summary, remediation, and mitigation details for any patch containing security fixes.

## `docs/README.md`

# DataHub Docs Overview

DataHub's project documentation is hosted at [datahubproject.io](https://docs.datahub.com/docs)

## Types of Documentation

### Feature Guide

A Feature Guide should follow the [Feature Guide Template](_feature-guide-template.md), and should provide the following value:

- At a high level, what is the concept/feature within DataHub?
- Why is the feature useful?
- What are the common use cases of the feature?
- What are the simple steps one needs to take to use the feature?

When creating a Feature Guide, please remember to:

- Provide plain-language descriptions for both technical and non-technical readers
- Avoid using industry jargon, abbreviations, or acryonyms
- Provide descriptive screenshots, links out to relevant YouTube videos, and any other relevant resources
- Provide links out to Tutorials for advanced use cases

_Not all Feature Guides will require a Tutorial._

### Tutorial

A Tutorial is meant to provide very specific steps to accomplish complex workflows and advanced use cases that are out of scope of a Feature Guide.

Tutorials should be written to accommodate the targeted persona, i.e. Developer, Admin, End-User, etc.

_Not all Tutorials require an associated Feature Guide._

## Docs Best Practices

### Embedding GIFs and or Screenshots

- Store GIFs and screenshots in [datahub-project/static-assets](https://github.com/datahub-project/static-assets); this minimizes unnecessarily large image/file sizes in the main repo
- Center-align screenshots and size down to 70% - this improves readability/skimability within the site

Example snippet:

```
<p align="center">
  <img width="70%"  src="https://raw.githubusercontent.com/datahub-project/static-assets/main/imgs/impact-analysis-export-full-list.png"/>
</p>
```

- Use the "raw" GitHub image link (right click image from GitHub > Open in New Tab > copy URL):

  - Good: https://raw.githubusercontent.com/datahub-project/static-assets/main/imgs/dbt-test-logic-view.png
  - Bad: https://github.com/datahub-project/static-assets/blob/main/imgs/dbt-test-logic-view.png

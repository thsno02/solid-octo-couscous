# Repository semantic capsule: mem0ai/mem0

- Commit: `c7ee362aff94a369af70f13f2b4f853f6793ff4c`
- Default branch: `main`
- Description: mem0ai/mem0
- Selected evidence files: 8 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

<p align="center">
  <a href="https://github.com/mem0ai/mem0">
    <img src="docs/images/banner-sm.png" width="800px" alt="Mem0 - The Memory Layer for Personalized AI">
  </a>
</p>
<p align="center" style="display: flex; justify-content: center; gap: 20px; align-items: center;">
  <a href="https://trendshift.io/repositories/11194" target="blank">
    <img src="https://trendshift.io/api/badge/repositories/11194" alt="mem0ai%2Fmem0 | Trendshift" width="250" height="55"/>
  </a>
</p>

<p align="center">
  <a href="https://mem0.ai">Learn more</a>
  ·
  <a href="https://mem0.dev/DiG">Join Discord</a>
  ·
  <a href="https://mem0.dev/demo">Demo</a>
</p>

<p align="center">
  <a href="https://mem0.dev/DiG">
    <img src="https://img.shields.io/badge/Discord-%235865F2.svg?&logo=discord&logoColor=white" alt="Mem0 Discord">
  </a>
  <a href="https://pepy.tech/project/mem0ai">
    <img src="https://img.shields.io/pypi/dm/mem0ai" alt="Mem0 PyPI - Downloads">
  </a>
  <a href="https://github.com/mem0ai/mem0">
    <img src="https://img.shields.io/github/commit-activity/m/mem0ai/mem0?style=flat-square" alt="GitHub commit activity">
  </a>
  <a href="https://pypi.org/project/mem0ai" target="blank">
    <img src="https://img.shields.io/pypi/v/mem0ai?color=%2334D058&label=pypi%20package" alt="Package version">
  </a>
  <a href="https://www.npmjs.com/package/mem0ai" target="blank">
    <img src="https://img.shields.io/npm/v/mem0ai" alt="Npm package">
  </a>
  <a href="https://www.ycombinator.com/companies/mem0">
    <img src="https://img.shields.io/badge/Y%20Combinator-S24-orange?style=flat-square" alt="Y Combinator S24">
  </a>
</p>

<p align="center">
  <a href="https://mem0.ai/research"><strong>📄 Benchmarking Mem0's token-efficient memory algorithm →</strong></a>
</p>

## New Memory Algorithm (April 2026)

| Benchmark | Old | New  | Tokens  | Latency p50  |
| --- | --- | --- | --- | --- |
| **LoCoMo** | 71.4 | **92.5** | 7.0K  | 0.88s  |
| **LongMemEval** | 67.8 | **94.4** | 6.8K  | 1.09s  |
| **BEAM (1M)** | — | **64.1** | 6.7K  | 1.00s  |
| **BEAM (10M)** | — | **48.6** | 6.9K  | 1.05s  |

All benchmarks run on the same production-representative model stack. Single-pass retrieval (one call, no agentic loops) at a top_200 retrieval budget. Scores reflect Mem0's managed platform, which includes proprietary optimizations not available in the open-source SDK; open-source users should expect directionally similar gains but not identical numbers.

**What changed:**
- **Single-pass ADD-only extraction** -- one LLM call, no UPDATE/DELETE. Memories accumulate; nothing is overwritten.
- **Agent-generated facts are first-class** -- when an agent confirms an action, that information is now stored with equal weight.
- **Entity linking** -- entities are extracted, embedded, and linked across memories for retrieval boosting.
- **Multi-signal retrieval** -- semantic, BM25 keyword, and entity matching scored in parallel and fused.
- **Temporal Reasoning** -- time-aware retrieval that ranks the right dated instance for queries about current state, past events, and upcoming plans.

See the [migration guide](https://docs.mem0.ai/migration/oss-v2-to-v3) for upgrade instructions. The [evaluation framework](https://github.com/mem0ai/memory-benchmarks) is open-sourced so anyone can reproduce the numbers.

## Research Highlights
- **92.5 on LoCoMo** -- +21 points over the previous algorithm
- **94.4 on LongMemEval** -- +27 points, with 98.2 on assistant memory recall
- **64.1 on BEAM (1M)** -- production-scale memory evaluation at 1M tokens
- [Read the full paper](https://mem0.ai/research)

# Introduction

[Mem0](https://mem0.ai) ("mem-zero") enhances AI assistants and agents with an intelligent memory layer, enabling personalized AI interactions. It remembers user preferences, adapts to individual needs, and continuously learns over time—ideal for customer support chatbots, AI assistants, and autonomous systems.

### Key Features & Use Cases

**Core Capabilities:**
- **Multi-Level Memory**: Seamlessly retains User, Session, and Agent state with adaptive personalization
- **Developer-Friendly**: Intuitive API, cross-platform SDKs, and a fully managed service option

**Applications:**
- **AI Assistants**: Consistent, context-rich conversations
- **Customer Support**: Recall past tickets and user history for tailored help
- **Healthcare**: Track patient preferences and history for personalized care
- **Productivity & Gaming**: Adaptive workflows and environments based on user behavior

## 🚀 Quickstart Guide <a name="quickstart"></a>

### Sign up as an agent

AI agents can mint a working Mem0 API key in under five seconds — no email, no dashboard, no OTP. Four commands end-to-end:

```bash
# 1. Install
npm install -g @mem0/cli      # or: pip install mem0-cli

# 2. Sign up as an agent (replace `claude-code` with your name)
mem0 init --agent --agent-caller claude-code

# 3. Add a memory
mem0 add "I am using mem0"

# 4. Search
mem0 search "am I using mem0"
```

The human owner can claim the account later with `mem0 init --email <their-email>` — same key, memories preserved. Full guide: [Sign up as an agent](https://docs.mem0.ai/platform/agent-signup).

| | Library | Self-Hosted Server | Cloud Platform |
|---|---------|-------------------|----------------|
| **Best for** | Testing, prototyping | Teams running on their own infrastructure | Zero-ops production use |
| **Setup** | `pip install mem0ai` | `docker compose up` | Sign up at [app.mem0.ai](https://app.mem0.ai?utm_source=oss&utm_medium=readme) |
| **Dashboard** | -- | [Yes](https://docs.mem0.ai/open-source/setup) | Yes |
| **Auth & API Keys** | -- | Yes | Yes |
| **Advanced Features** | -- | Teasers | All included |

Just testing? Use the library. Building for a team? Self-hosted. Want zero ops? Cloud.

### Library (pip / npm)

```bash
pip install mem0ai
```

For enhanced hybrid search with BM25 keyword matching and entity extraction, install with NLP support:

```bash
pip install mem0ai[nlp]
python -m spacy download en_core_web_sm
```

Install sdk via npm:

```bash
npm install mem0ai
```

### Self-Hosted Server

> **Note:** Self-hosted auth is on by default. Upgrading from a pre-auth build? Set `ADMIN_API_KEY`, register an admin through the wizard, or `AUTH_DISABLED=true` for local dev only. See [upgrade notes](https://docs.mem0.ai/open-source/setup#upgrade-notes).

```bash
# Recommended: one command — start the stack, create an admin, issue the first API key.
cd server && make bootstrap

# Manual: start the stack and finish setup via the browser wizard.
cd server && docker compose up -d    # http://localhost:3000
```

See the [self-hosted docs](https://docs.mem0.ai/open-source/overview) for configuration.

### Cloud Platform

1. Sign up on [Mem0 Platform](https://app.mem0.ai?utm_source=oss&utm_medium=readme)
2. Embed the memory layer via SDK or API keys
3. Using hosted Qdrant vectors? See the [Platform migration guide](https://docs.mem0.ai/migration/oss-to-platform) to import them into Mem0 Platform.

### CLI

Manage memories from your terminal:

```bash
npm install -g @mem0/cli   # or: pip install mem0-cli

mem0 init
mem0 add "Prefers dark mode and vim keybindings" --user-id alice
mem0 search "What does Alice prefer?" --user-id alice
```

See the [CLI documentation](https://docs.mem0.ai/platform/cli) for the full command reference.

### Agent Skills

Teach your AI coding assistant (Claude Code, Codex, Cursor, Windsurf, OpenCode, OpenClaw, and any tool that supports the skills standard) how to build with Mem0. Two categories:

**Reference skills — always on** (SDK knowledge loaded into the assistant's context):

```bash
npx skills add https://github.com/mem0ai/mem0 --skill mem0
npx skills add https://github.com/mem0ai/mem0 --skill mem0-cli
npx skills add https://github.com/mem0ai/mem0 --skill mem0-vercel-ai-sdk
```

**Pipeline skills — run on demand** (execute an end-to-end workflow in an existing repo):

```bash
npx skills add https://github.com/mem0ai/mem0 --skill mem0-integrate
npx skills add https://github.com/mem0ai/mem0 --skill mem0-test-integration
npx skills add https://github.com/mem0ai/mem0 --skill mem0-oss-to-platform
```

Use `/mem0-integrate` to wire Mem0 into an existing repo via a test-first pipeline, then `/mem0-test-integration` to verify. Use `/mem0-oss-to-platform` to migrate an existing project from Mem0 OSS to the hosted Platform SDK. See the [skills catalog](./skills/) or [Vibecoding with Mem0](https://docs.mem0.ai/vibecoding) for the full picture.

### Basic Usage

Mem0 requires an LLM to function, with `gpt-5-mini` from OpenAI as the default. However, it supports a variety of LLMs; for details, refer to our [Supported LLMs documentation](https://docs.mem0.ai/components/llms/overview).

Mem0 uses `text-embedding-3-small` from OpenAI as the default embedding model. For best results with hybrid search (semantic + keyword + entity boosting), we recommend using at least [Qwen 600M](https://huggingface.co/Alibaba-NLP/gte-Qwen2-1.5B-instruct) or a comparable embedding model. See [Supported Embeddings](https://docs.mem0.ai/components/embedders/overview) for configuration details.

First step is to instantiate the memory:

```python
from openai import OpenAI
from mem0 import Memory

openai_client = OpenAI()
memory = Memory()

def chat_with_memories(message: str, user_id: str = "default_user") -> str:
    # Retrieve relevant memories
    relevant_memories = memory.search(query=message, filters={"user_id": user_id}, top_k=3)
    memories_str = "\n".join(f"- {entry['memory']}" for entry in relevant_memories["results"])

    # Generate Assistant response
    system_prompt = f"You are a helpful AI. Answer the question based on query and memories.\nUser Memories:\n{memories_str}"
    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": message}]
    response = openai_client.chat.completions.create(model="gpt-5-mini", messages=messages)
    assistant_response = response.choices[0].message.content

    # Create new memories from the conversation

## `AGENTS.md`

# AGENTS.md

Context for AI coding assistants (Claude Code, Cursor, Copilot, Codex) working in the Mem0 repository.

**Mem0** ("mem-zero") is a memory layer for AI agents: persistent, personalized memory through a hosted platform API and self-hosted open-source SDKs. Apache-2.0.
[Repository](https://github.com/mem0ai/mem0) · [Documentation](https://docs.mem0.ai)

This is a polyglot monorepo and **every package sets its own rules**. Read the `AGENTS.md` nearest the files you are editing before running any command. The linters, formatters, test runners, and line lengths genuinely differ per package, and using the wrong one fails CI or produces a diff full of noise.

## Do NOT

- Open a pull request without a signed CLA. It will not be reviewed. See [The CLA is not optional](#the-cla-is-not-optional).
- Open a pull request that does not link an issue carrying the `accepted` label. A bot closes it within a minute. See [Two gates decide whether your pull request stays open](#two-gates-decide-whether-your-pull-request-stays-open).
- Modify anything in `.github/workflows/` without explicit maintainer approval. Publishing credentials are pinned to workflow filenames.
- Commit `.env` files, API keys, or credentials.
- Skip pre-commit hooks.
- Use npm or yarn in TypeScript packages. This repo is pnpm-only (Bun in `integrations/opencode-plugin/`).
- Use `require()` in TypeScript. ES module `import` syntax only.
- Mix up linter configs. Root Python is ruff at line length **120**, `cli/python/` is ruff at **100**, `cli/node/` is Biome, `mem0-ts/` is Prettier, `integrations/vercel-ai-sdk/` is ESLint.
- Add Python dependencies to the core `dependencies` list in `pyproject.toml`. Use an optional group.
- Change a public API without updating `docs/` in the same pull request.
- Introduce a new framework or abstraction without discussion. Follow the patterns already in the file you are editing.

## Where to look

| Editing | Read | Toolchain |
|---------|------|-----------|
| `mem0/` | [`mem0/AGENTS.md`](mem0/AGENTS.md) | hatch, ruff 120, pytest |
| `tests/` | [`tests/AGENTS.md`](tests/AGENTS.md) | pytest |
| `mem0-ts/` | [`mem0-ts/AGENTS.md`](mem0-ts/AGENTS.md) | pnpm, tsup, Prettier, jest |
| `cli/python/` | [`cli/python/AGENTS.md`](cli/python/AGENTS.md) | ruff **100**, pytest |
| `cli/node/` | [`cli/node/AGENTS.md`](cli/node/AGENTS.md) | pnpm, tsup, Biome, vitest |
| `integrations/` | [`integrations/AGENTS.md`](integrations/AGENTS.md) | varies per integration |
| `server/` | [`server/AGENTS.md`](server/AGENTS.md) | Docker Compose, FastAPI |
| `docs/` | [`docs/AGENTS.md`](docs/AGENTS.md) | Mintlify |
| `skills/` | [`skills/AGENTS.md`](skills/AGENTS.md) | markdown, size-budgeted |
| `.github/` | [`.github/AGENTS.md`](.github/AGENTS.md) | GitHub Actions |

## Repository map

| Directory | What it is |
|-----------|------------|
| `mem0/` | Core Python SDK (`mem0ai` on PyPI): memory, LLMs, embeddings, vector stores, graphs, rerankers |
| `mem0-ts/` | TypeScript SDK (`mem0ai` on npm): hosted client + OSS memory |
| `cli/python/` | Python CLI (`mem0-cli` on PyPI), Typer-based, entry point `mem0` |
| `cli/node/` | Node CLI (`@mem0/cli` on npm), Commander-based, entry point `mem0` |
| `integrations/` | Agent and editor integrations, one self-contained directory each |
| `server/` | FastAPI REST server for self-hosted Mem0 (Docker: FastAPI + pgvector + Neo4j) |
| `skills/` | Claude Code skill definitions, published by raw URL |
| `docs/` | Documentation site (Mintlify) |
| `tests/` | Python SDK tests (pytest) |
| `examples/` | Sample apps, Chrome extension, multi-agent patterns, notebooks |
| `scripts/` | Repo-wide utilities, e.g. `check-llms-txt-coverage.py` |
| `evaluation/` | Submodule pinned to [`mem0ai/memory-benchmarks`](https://github.com/mem0ai/memory-benchmarks) |
| `pr-reviews/` | Pull request review materials |

```
mem0 (Python SDK)          mem0-ts (TypeScript SDK)
├── mem0/memory/           ├── src/client/    MemoryClient (hosted)
├── mem0/llms/             └── src/oss/       Memory (self-hosted)
├── mem0/embeddings/           ├── src/llms/
├── mem0/vector_stores/        ├── src/embeddings/
├── mem0/graphs/               ├── src/vector_stores/
└── mem0/reranker/             └── src/graphs/

cli/python/                 ──▶ mem0ai (optional, OSS mode)
cli/node/                   ──▶ mem0ai (npm)
integrations/vercel-ai-sdk/ ──▶ ai, @ai-sdk/*
integrations/openclaw/      ──▶ mem0ai (npm)
```

## Setup

```bash
hatch shell dev_py_3_11   # Python: creates the env with all deps
pre-commit install        # ruff + isort on commit

cd <ts-package> && pnpm install
```

Requirements: Python 3.9+ (3.10+ for the CLI), Node 18+ (20 or 22 preferred), pnpm 10+, hatch, Docker for `server/`.

## Conventions everywhere

- **Naming:** `snake_case.py`, `test_<module>.py`, `snake_case.ts`, `<module>.test.ts`, `kebab-case` for config and manifest files.
- **Python:** Pydantic v2 for models and config. Providers inherit a `base.py` abstract class; config lives in `configs.py`.
- **TypeScript:** strict mode, tsup builds, ES module imports.
- **Commits:** [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`).
- **Versions:** bump in `pyproject.toml` or `package.json`. Releases are cut by tag prefix; see [`.github/AGENTS.md`](.github/AGENTS.md).

## Benchmarking

Benchmarks (LOCOMO, LongMemEval, BEAM) live in [`mem0ai/memory-benchmarks`](https://github.com/mem0ai/memory-benchmarks). The in-repo `evaluation/` path is a submodule pinned to that repo's `main`:

```bash
git submodule update --init evaluation
```

## What to ship with a change

Guidelines, not rules. Trivial fixes need less; anything user-facing needs more.

| Change | Expect |
|--------|--------|
| **Bug fix** | A regression test that fails without the fix, written first. The fix. The relevant suite passing. The package's linter run. |
| **New feature** | Implementation following existing patterns, test coverage, `docs/` updates for public APIs, an example if the behavior is user-facing, and an `llms.txt` entry for any new `.mdx` page. |
| **New provider** | See [Adding a provider](mem0/AGENTS.md#adding-a-provider). |
| **New integration** | See [Adding an integration](integrations/AGENTS.md#adding-an-integration). |
| **Refactor** | Tests for changed behavior, existing tests still green. No docs needed for internal-only changes. |

Fix bugs at the root, not at the symptom. If a guard belongs in a shared function, put it there rather than in each caller.

## Contributing

Full guide: [`CONTRIBUTING.md`](CONTRIBUTING.md). Conduct: [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

1. Open an issue **first** and wait for a maintainer to apply the `accepted` label. Every PR must link it with `Closes #<number>`. PRs without an accepted linked issue are closed automatically by the [PR Gate](.github/workflows/pr-gate.yml), with a reopen path. Documentation-only changes are exempt.
2. Fork, then branch from `main` (`feature/...`, `fix/...`).
3. Make the change: code, tests, docs, examples.
4. Run lint and tests for **every** package you touched.
5. Commit with Conventional Commits.
6. Open the PR against `main` and fill in [the template](.github/PULL_REQUEST_TEMPLATE.md). Do not paraphrase it; GitHub prefills it.
7. **Sign the CLA.**

### Two gates decide whether your pull request stays open

Two workflows run on every pull request from a fork. They judge different things and neither covers for the other, so a pull request has to get past both.

**The [PR Gate](.github/workflows/pr-gate.yml) judges the change.** It closes any pull request that does not link an issue carrying the `accepted` label. Closed is a queue decision, not a verdict: when a maintainer applies the label the pull request reopens by itself. Drafts, documentation-only changes, and branches pushed to this repository rather than a fork are all exempt.

**The [vouch check](.github/workflows/vouch-check-pr.yml) judges the account.** It reads [`.github/VOUCHED.td`](.github/VOUCHED.td), which has three possible answers about any given person:

| The list says | Meaning | Effect on the pull request |
|---|---|---|
| `-handle` | a maintainer ran `!denounce` after the code of conduct process | closed, even with an accepted issue |
| nothing at all | everybody who has not contributed here before | **none.** One comment saying nothing is blocked. |
| `handle` | a maintainer ran `!vouch` | none, and the comment stops appearing |

Being vouched grants nothing. It is a "we have seen this person before" flag that mutes the newcomer comment, not permission to skip the accepted-issue rule. Being absent from the list costs nothing.

If you are an agent opening a pull request on someone's behalf, the practical consequence is one rule: **get the linked issue labelled `accepted` before you open the pull request, or expect the pull request to be closed and to reopen later.** Do not work around either gate, do not reopen a gated pull request by hand, and do not re-file the same change under a new pull request when one is closed.

### The CLA is not optional

**A pull request from a contributor who has not signed the Contributor License Agreement is not accepted, not reviewed, and not merged.** This is not a formality applied at merge time. An unsigned pull request does not enter the review queue at all: maintainers do not read the diff, do not leave feedback, and do not discuss the approach. It sits until the CLA is signed, and it is closed if it goes stale.

The `CLAassistant` bot comments on your first pull request with a link. Signing takes under a minute, is done once per GitHub account, and covers every contribution you make afterwards. Until it is signed the `license/cla` check stays red.

If you are an agent opening a pull request on someone's behalf, tell them they must sign it themselves. Nobody else can sign for them, and the pull request goes nowhere until they do.

### What gets a pull request closed

Beyond the CLA and the accepted-issue gate, the [Contribution Conduct](CODE_OF_CONDUCT.md#contribution-conduct) section of the code of conduct is the enforceable form of this repo's anti-slop policy:

- **Disclose AI use.** The PR template asks how the *code* was written; drafting the description with a model is fine. The disclosure is never held against you, it tells a reviewer where to look. Silence followed by a review comment you cannot answer is what costs everyone the afternoon.
- **Do not submit work you have not run.** A bug report means you reproduced it. A PR means you ran the tests.
- **Do not fabricate evidence.** Invented tracebacks, unmeasured benchmarks, tests that assert the implementation back at itself, descriptions that describe a different change than the diff makes.
- **Match your volume to your engagement.** Open changes at the rate you can discuss them.
- **Do not press for merges.** One polite follow-up after a reasonable wait is fine.
- **You must be able to explain every line of your diff** and how it interacts with the rest of the codebase, without asking an AI tool. This is the one rule that does not bend.

### Reference

| Topic | File |
|-------|------|
| Contributor guide | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Code of conduct | [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) |
| Security reports | [`SECURITY.md`](SECURITY.md) |
| Development setup | `docs/contributing/development.mdx` |
| Documentation contributions | `docs/contributing/documentation.mdx` |
| PR template | `.github/PULL_REQUEST_TEMPLATE.md` |
| Issue forms | `.github/ISSUE_TEMPLATE/` |
| Contribution gates | [Two gates decide whether your pull request stays open](#two-gates-decide-whether-your-pull-request-stays-open) |
| Trust list (vouch) | [`.github/VOUCHED.td`](.github/VOUCHED.td) |
| CI/CD, gates, rulesets | [`.github/AGENTS.md`](.github/AGENTS.md) |

## `CLAUDE.md`

AGENTS.md

## `CONTRIBUTING.md`

# Contributing to Mem0

First off, thank you for taking the time to contribute! 🎉 Mem0 is a
community-driven project and we welcome contributions of all kinds — bug fixes,
new features, documentation, examples, and integrations.

Mem0 is a polyglot monorepo, and this guide covers contributing to both the
**Python SDK** and the **TypeScript SDK** (and the rest of the repository).

By participating you agree to our [Code of Conduct](./CODE_OF_CONDUCT.md). Its
**Contribution Conduct** section is the enforceable form of the rules on this
page: disclose AI use, don't submit work you haven't run, don't fabricate
reproductions or benchmarks, keep your volume matched to your engagement, and
don't press for merges.

## Before You Start

### 1. Open an Issue First

**Always open an issue before opening a pull request.** This lets us discuss the
change, avoid duplicate effort, and agree on the approach before you invest time
in code.

- Search [existing issues](https://github.com/mem0ai/mem0/issues) first to see if
  your bug or idea already exists.
- If it doesn't, open a
  [bug report](https://github.com/mem0ai/mem0/issues/new?template=bug_report.yml) or
  [feature request](https://github.com/mem0ai/mem0/issues/new?template=feature_request.yml).
- For anything beyond a trivial fix, wait for a maintainer to confirm the approach
  before starting significant work.

A bug report needs a reproduction we can run, the version you are on, and the
real output or traceback you saw. Reports without those cannot be acted on and
get closed. A feature request needs the problem you hit and the workaround you
are living with, not just the API you would like.

Every pull request must link to an issue using `Closes #<issue-number>`, and that
issue must carry the `accepted` label. A maintainer applies `accepted` once we
agree the change is one we want.

Pull requests that don't link an accepted issue are closed automatically by the
[PR Gate](./.github/workflows/pr-gate.yml). **Closed does not mean rejected.** It
means the change isn't in the queue yet. Once a maintainer labels the issue the
pull request reopens itself, and you don't have to do anything. Documentation-only
changes skip the gate entirely.

A second check looks at who opened the pull request rather than what it changes.
If you are not yet in this repo's contributor list
([`.github/VOUCHED.td`](./.github/VOUCHED.td)) you get one comment saying so.
**Nothing is blocked and there is nothing you need to do.** A maintainer can add
you by commenting `!vouch @you` on any issue, which only stops that comment from
appearing again. Being on the list is not permission to skip the accepted-issue
rule, and being absent from it costs you nothing.

The list has a negative side too. A maintainer can `!denounce` an account that
has been through the
[code of conduct](./CODE_OF_CONDUCT.md#contribution-conduct) enforcement process,
and pull requests from that account are closed whether or not they link an
accepted issue. This is rare, it is never where anyone starts, and it is
reversible.

Security fixes are the one exception, and they don't go through public pull
requests at all. Follow the [Security Policy](./SECURITY.md) instead, which uses
a private advisory and a private fork so the vulnerability isn't disclosed before
the fix ships.

### 2. Understand Your Code

**You must be able to explain what your changes do and how they interact with
the rest of the codebase without the help of an AI tool.** This is the one rule
we will not bend on.

Using AI to write code is fine. Most of us do. You can build real understanding
by interrogating an agent about this codebase until you grasp the edge cases and
the blast radius of your change. What is not fine is opening a pull request for
a diff you cannot defend in review.

Disclose it in the pull request template and say what you checked yourself.
We ask about the code, not the write-up: using AI to draft the pull request
description is fine. We ask because it tells reviewers where to look, not
because it counts against you. An honest "an agent wrote this, here is what I
verified" is welcome. Silence, followed by a review comment you cannot answer,
is what wastes everyone's time.

Signs your pull request will be closed:

- Invented APIs, config keys, or providers that don't exist in this repo.
- Tests that assert the implementation back at itself rather than the behaviour.
- A description that describes a different change than the diff makes.
- Sweeping unrelated reformatting bundled with a small fix.
- You cannot answer a direct question about your own diff.

### 3. Sign the Contributor License Agreement (CLA)

**We cannot accept or merge any pull request until you have signed our Contributor
License Agreement (CLA).**

When you open your first PR, the CLA bot will automatically comment with a link to
sign. Signing takes less than a minute and only needs to be done once. Pull
requests from contributors who have not signed the CLA will be blocked from
merging.

## First Contribution Fast Path

Fixing a typo or a small docs issue? You don't need the full workflow below.

1. **Pick something small.** Look for issues labeled `documentation` or `good first issue`, or a typo/broken link you noticed while reading the docs.
2. **Branch from `main`** with a name that says what you're fixing, e.g. `docs/fix-quickstart-typo` or `fix/broken-crewai-link`.
3. **Make the change, then run only what applies:**
   - Docs-only change (`docs/**`): preview with `make docs`. If you added or removed an `.mdx` page, run `python scripts/check-llms-txt-coverage.py --write` so `docs/llms.txt` stays in sync.
   - Code change: run the linter and tests for the package you touched, see [Development Workflow](#development-workflow) below.
4. **Open a PR** against `main` with `Closes #<issue-number>` and a one-line description of what you fixed.

For anything larger than a docs fix or a small bug, follow the full workflow below.

## Repository Layout

The two most common contribution targets are the SDKs:

| Package               | Path       | Language     | Package manager |
| --------------------- | ---------- | ------------ | --------------- |
| Python SDK (`mem0ai`) | `mem0/`    | Python 3.9+  | `hatch`         |
| TypeScript SDK (`mem0ai`) | `mem0-ts/` | TypeScript | `pnpm`        |

Other packages include the CLIs (`cli/python/`, `cli/node/`), integrations
(`integrations/`), the self-hosted `server/`, and the docs site
(`docs/`). See [AGENTS.md](./AGENTS.md) for a full map of the repository.

## Development Workflow

1. **Fork** the repository and **clone** your fork.
2. Create a **feature branch** from `main` (e.g. `feature/my-new-feature` or
   `fix/issue-1234`).
3. Make your changes — add **tests**, **documentation**, and **examples** as
   appropriate.
4. Run **linting and tests** for every package you touched (see below).
5. Commit using [Conventional Commits](https://www.conventionalcommits.org/)
   (e.g. `feat:`, `fix:`, `docs:`, `refactor:`, `test:`).
6. Push and open a **pull request** against `main`, linking the issue with
   `Closes #<number>` and filling out the
   [PR template](./.github/PULL_REQUEST_TEMPLATE.md).

### Contributing to the Python SDK (`mem0/`)

We use [`hatch`](https://hatch.pypa.io/latest/install/) to manage environments.
**Do not use `pip` or `conda` for dependency management.**

```bash
# Activate a dev environment (3.9 / 3.10 / 3.11 / 3.12)
hatch shell dev_py_3_11

# Install pre-commit hooks (runs ruff + isort on commit)
pre-commit install

# Lint, format, and sort imports
make lint
make format
make sort

# Run the test suite (run `make install_all` first if deps are missing)
make test
```

- **Linter / formatter:** Ruff (line length **120**)
- **Import sorting:** isort (`profile = "black"`)
- **Tests:** pytest (in `tests/`)

See the full [Development guide](https://docs.mem0.ai/contributing/development) for
environment details.

### Contributing to the TypeScript SDK (`mem0-ts/`)

We use [`pnpm`](https://pnpm.io/) (v10+) for all TypeScript packages. **Do not use
`npm` or `yarn`.**

```bash
cd mem0-ts
pnpm install

pnpm run build        # tsup (CJS + ESM)
pnpm run test         # jest (all tests)
pnpm run test:unit    # unit tests with coverage
```

- **Build:** tsup
- **Formatter:** Prettier
- **Tests:** jest
- Always run type checking after changes: `pnpm run typecheck` (or `tsc --noEmit`).
- Use ES module `import` syntax — never `require()`.

## Good Contribution Practices

- **Keep PRs small and focused.** One logical change per PR is easier to review and
  merge.
- **Follow existing patterns.** Match the style, structure, and conventions of the
  code around you. Don't introduce new frameworks or abstractions without
  discussion.
- **Write tests** that would fail without your change — regression tests for bugs,
  coverage for new features.
- **Update documentation** in `docs/` for any user-facing change. New `.mdx` pages
  must be added to `docs/llms.txt` (run
  `python scripts/check-llms-txt-coverage.py --write` to scaffold entries).
- **Add examples** when introducing new user-facing behavior.
- **Run linters and tests locally** before pushing — CI re-runs them on every PR
  via the CI Gate.
- **Never commit secrets** — no `.env` files, API keys, or credentials.
- **Don't add core dependencies lightly.** New Python dependencies belong in an
  optional group in `pyproject.toml`, not the core `dependencies` list.
- **Be responsive** to review feedback and keep your branch up to date with `main`.

## Pull Request Checklist

Before requesting review, make sure:

- [ ] An issue exists and is linked with `Closes #<number>`
- [ ] You have signed the CLA
- [ ] Your code follows the project's style guidelines (lint passes)
- [ ] You performed a self-review of your changes
- [ ] Tests are added/updated and pass locally
- [ ] Documentation is updated if needed

## `Makefile`

.PHONY: format sort lint

# Variables
ISORT_OPTIONS = --profile black
PROJECT_NAME := mem0ai

# Default target
all: format sort lint

install:
	hatch env create

install_all:
	pip install ruff==0.16.0 groq together boto3 'litellm>=1.83.7,<1.98.0' ollama chromadb weaviate weaviate-client sentence_transformers vertexai \
	            google-generativeai elasticsearch opensearch-py vecs "pinecone<7.0.0" pinecone-text faiss-cpu langchain-community \
							upstash-vector azure-search-documents langchain-memgraph langchain-neo4j langchain-aws rank-bm25 pymochow pymongo psycopg kuzu databricks-sdk valkey

# Format code with ruff
format:
	hatch run format

# Sort imports with isort
sort:
	hatch run isort mem0/

# Lint code with ruff
lint:
	hatch run lint

docs:
	cd docs && mintlify dev

build:
	hatch build

publish:
	hatch publish

clean:
	rm -rf dist

test:
	hatch run test

test-py-3.10:
	hatch run dev_py_3_10:test

test-py-3.11:
	hatch run dev_py_3_11:test

test-py-3.12:
	hatch run dev_py_3_12:test

## `SECURITY.md`

# Security Policy

We take the security of Mem0 and our community seriously. Thank you for helping
keep Mem0 and its users safe by disclosing vulnerabilities responsibly.

## Reporting a Vulnerability

Please **do not** report security vulnerabilities through public GitHub issues,
pull requests, or discussions.

If you believe you have found a security vulnerability in Mem0, please report it
privately through one of the following channels:

1. **GitHub Private Vulnerability Reporting** — open a
   [private security advisory](https://github.com/mem0ai/mem0/security/advisories/new)
   directly on this repository.
2. **Email** the maintainers at **support@mem0.ai** with the subject line:

   `SECURITY: Mem0 vulnerability report`

To help us triage and resolve the issue quickly, please include as much of the
following as you can:

- Affected component or package (e.g. Python SDK, TypeScript SDK, server, CLI)
- Affected version, tag, or commit
- Clear, step-by-step reproduction instructions
- The security impact and a proof of concept, if available
- Any suggested fix or mitigation
- Whether an AI tool was involved in finding or writing up the report

Reports generated by an AI tool are welcome, but only once you have run the
reproduction yourself and confirmed the impact is real. A scan result or model
output pasted in without that step is not a vulnerability report, and we close
those without a detailed response so we can spend the time on real ones.

## Response Process

- We will acknowledge receipt of your report within **72 hours**.
- We will work with you privately to confirm the issue and assess its impact.
- Once a fix or mitigation is ready, we will coordinate a disclosure timeline
  with you and credit you for the discovery, unless you prefer to remain anonymous.

## Public Disclosure

Please avoid sharing technical details of the vulnerability publicly until the
maintainers have reviewed the issue and a fix or mitigation has been released. We
are committed to resolving valid reports promptly and keeping you informed
throughout the process.

## Supported Versions

We release security fixes against the latest published version of each package.
Whenever possible, please reproduce the issue on the most recent release before
reporting.

## `pyproject.toml`

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "mem0ai"
version = "2.0.20"
description = "Long-term memory for AI Agents"
authors = [
    { name = "Mem0", email = "support@mem0.ai" }
]
readme = "README.md"
license = "Apache-2.0"
license-files = ["LICENSE"]
requires-python = ">=3.10,<4.0"
dependencies = [
    "qdrant-client>=1.12.0",
    "pydantic>=2.7.3",
    "openai>=1.90.0",
    "httpx>=0.28.0",
    "posthog>=7.14.0",
    "pytz>=2024.1",
    "sqlalchemy>=2.0.31",
    "protobuf>=5.29.6,<7.0.0",
]

[project.optional-dependencies]
nlp = [
    "spacy>=3.7.0",
]
vector-stores = [
    "vecs>=0.4.0",
    "chromadb>=0.4.24",
    "cassandra-driver>=3.29.0",
    "weaviate-client>=4.15.4,<5.0.0",
    "pinecone<=7.3.0",
    "pinecone-text>=0.10.0",
    "faiss-cpu>=1.7.4",
    "upstash-vector>=0.6.0",
    "azure-search-documents>=11.4.0b8",
    "psycopg>=3.2.8",
    "psycopg-pool>=3.2.6,<4.0.0",
    "pymongo>=4.13.2",
    "pymochow>=2.2.9",
    "pymysql>=1.1.0",
    "dbutils>=3.0.3",
    "valkey>=6.0.0",
    "databricks-sdk>=0.63.0",
    "azure-identity>=1.24.0",
    "redis>=5.0.0,<6.0.0",
    "redisvl>=0.1.0,<1.0.0",
    "elasticsearch>=8.0.0,<9.0.0",
    "pymilvus>=2.4.0,<2.6.0",
    "langchain-aws>=0.2.23,<0.3.0",
    "oracledb>=2.2.0",
]
llms = [
    "groq>=0.3.0",
    "together>=0.2.10",
    "litellm>=1.83.7,<1.98.0",
    "openai>=1.90.0",
    "ollama>=0.3.0",
    "vertexai>=0.1.0",
    "google-generativeai>=0.3.0",
    "google-genai>=1.0.0",
]
extras = [
    "boto3>=1.34.0",
    "langchain>=0.3.30,<1.0.0",
    "langchain-community>=0.3.27,<1.0.0",
    "langchain-core>=0.3.85,<1.0.0",
    "sentence-transformers>=5.2.0",
    "transformers>=5.3.0",
    "elasticsearch>=8.0.0,<9.0.0",
    "opensearch-py>=2.0.0",
    "fastembed>=0.3.1",
]
test = [
    "pytest>=8.2.2",
    "pytest-mock>=3.14.0",
    "pytest-asyncio>=0.23.7",
]
dev = [
    "ruff==0.16.0",
    "isort>=5.13.2",
    "pytest>=8.2.2",
]

[tool.pytest.ini_options]
pythonpath = ["."]

[tool.hatch.build]
include = [
    "mem0/**/*.py",
    "mem0/memory/oss_notices_config.json",
]
exclude = [
    "**/*",
    "!mem0/**/*.py",
    "!mem0/memory/oss_notices_config.json",
]

[tool.hatch.build.targets.wheel]
packages = ["mem0"]
only-include = ["mem0"]

[tool.hatch.envs.dev_py_3_10]
python = "3.10"
features = [
  "test",
  "vector-stores",
  "llms",
  "extras",
]

[tool.hatch.envs.dev_py_3_11]
python = "3.11"
features = [
  "test",
  "vector-stores",
  "llms",
  "extras",
]

[tool.hatch.envs.dev_py_3_12]
python = "3.12"
features = [
  "test",
  "vector-stores",
  "llms",
  "extras",
]

[tool.hatch.envs.default.scripts]
format = [
    "ruff format",
]
format-check = [
    "ruff format --check",
]
lint = [
    "ruff check",
]
lint-fix = [
    "ruff check --fix",
]
test = [
    "pytest tests/ {args}",
]

[tool.ruff]
line-length = 120

[tool.ruff.lint]
select = ["E4", "E7", "E9", "F"]

[tool.ruff.lint.isort]
known-first-party = ["mem0", "mem0_cli"]

[tool.isort]
profile = "black"
known_first_party = ["mem0", "mem0_cli"]
# isort scope kept aligned with [tool.ruff.lint.isort] above.
# black-equivalent profile here matches the formatter behaviour ruff applies.
# Plugin-version bumps need a touch here to fire required CI checks (path-filter trap).
# Last touched: plugin v0.1.3

## `docs/README.md`

# Mintlify Starter Kit

Click on `Use this template` to copy the Mintlify starter kit. The starter kit contains examples including

- Guide pages
- Navigation
- Customizations
- API Reference pages
- Use of popular components

### Development

Install the [Mintlify CLI](https://www.npmjs.com/package/mintlify) to preview the documentation changes locally. To install, use the following command

```
npm i -g mintlify
```

Run the following command at the root of your documentation (where mint.json is)

```
mintlify dev
```

### Publishing Changes

Install our GitHub App to auto-propagate changes from your repo to your deployment. Changes will be deployed to production automatically after pushing to the default branch. Find the link to install on your dashboard. 

#### Troubleshooting

- Mintlify dev isn't running - Run `mintlify install` it'll re-install dependencies.
- Page loads as a 404 - Make sure you are running in a folder with `mint.json`

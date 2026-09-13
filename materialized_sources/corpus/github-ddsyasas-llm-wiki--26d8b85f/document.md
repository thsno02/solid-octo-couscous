# Repository semantic capsule: ddsyasas/llm-wiki

- Commit: `e8dd69ebba0dc7c395c1b8217bb1c30c14e8c84c`
- Default branch: `main`
- Description: ddsyasas/llm-wiki
- Selected evidence files: 5 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

<p align="center">
  <img src="apps/web/public/logo-hero.svg" alt="LLM Wiki" width="600">
</p>

<h1 align="center">LLM Wiki</h1>

<p align="center">
  <strong>A personal Wikipedia an LLM maintains for you.</strong><br>
  Drop in articles, papers, notes, PDFs, or URLs — an agent compiles them into a cross-linked markdown wiki you fully own. Knowledge compounds: each new source makes every page richer, not just one new page longer.
</p>

<p align="center">
  Open source · Local-first · Bring-your-own-key · MIT · v1.2.3
</p>

<p align="center">
  <a href="https://llmwiki.cc"><img src="https://img.shields.io/badge/site-llmwiki.cc-991b1b" alt="llmwiki.cc"></a>
  <a href="https://www.npmjs.com/package/@syasas/llm-wiki"><img src="https://img.shields.io/npm/v/@syasas/llm-wiki?color=991b1b&label=npm" alt="npm version"></a>
  <a href="https://github.com/ddsyasas/llm-wiki/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT License"></a>
  <a href="https://github.com/ddsyasas/llm-wiki/releases/latest"><img src="https://img.shields.io/github/v/release/ddsyasas/llm-wiki?color=991b1b" alt="latest release"></a>
  <a href="https://github.com/ddsyasas/llm-wiki/blob/main/CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen" alt="PRs welcome"></a>
</p>

<p align="center">
  <a href="https://www.producthunt.com/products/llm-wiki-cc?embed=true&amp;utm_source=badge-featured&amp;utm_medium=badge&amp;utm_campaign=badge-llm-wiki-cc" target="_blank" rel="noopener noreferrer"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1159603&amp;theme=light&amp;t=1780562921195" alt="LLM Wiki cc - A personal Wikipedia an LLM maintains for you | Product Hunt" width="250" height="54"></a>
</p>

This is a from-scratch implementation of [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), released April 2026.

---

## Demo

<p align="center">
  <a href="https://youtu.be/9FzlkDmF51Y">
    <img src="https://img.youtube.com/vi/9FzlkDmF51Y/maxresdefault.jpg" alt="Watch the LLM Wiki demo on YouTube" width="600">
  </a>
</p>

<p align="center">
  <a href="https://youtu.be/9FzlkDmF51Y"><strong>▶ Watch the walkthrough</strong></a> — ingest a source, watch pages get written and cross-linked, then query and lint the wiki.
</p>

---

## Why this exists

| Existing tools | What they miss |
|---|---|
| **RAG chat** (NotebookLM, ChatGPT files) | Stateless. Rediscovers your corpus from scratch on every query. Never accumulates anything you can read later. |
| **Note-taking apps** (Obsidian, Notion) | All the maintenance burden on the human. You write, you cross-link, you check for contradictions. Nothing scales. |
| **LLM Wiki** | Sits between them. The LLM does the maintenance; the wiki accumulates value; you own the markdown files. |

After a few weeks of feeding it sources, you have a navigable, cited, deliberately-organized body of knowledge about whatever you care about — without ever having written a page yourself.

---

## Screenshots

![Home page — per-wiki stats, primary action cards, and footer chips for navigation](docs/screenshots/01-home.png)

*Home — per-wiki page / source / chat counts, cumulative LLM spend (click → cross-wiki dashboard), and the four primary actions. Footer chips reach every meta-surface (About, Help, Developers, Dashboard).*

### The wiki layer

![Wiki landing — page cards grouped by type](docs/screenshots/02-wiki-landing.png)

*`/wiki` — pages grouped by type (Concepts, Entities, Comparisons, Overviews). Sidebar has search + filter; clicking any card opens the page with backlinks and source lineage.*

![3D knowledge graph](docs/screenshots/03-graph.png)
*`/graph` — every page and every `[[wikilink]]` as a 3D force-directed network, colored by page type. Drag to orbit, scroll to zoom, click any node to focus.*

![Graph view with a node selected and side panel showing details](docs/screenshots/04-graph-node-panel.png)
*Clicking a node opens a side panel: outgoing links, full summary, connected pages. "Open page →" jumps to the wiki view of that node.*

### Operations

![Chat thread with a wiki question and an LLM answer that cross-links to wiki pages](docs/screenshots/05-chat.png)
*`/chats/[id]` — multi-turn conversations over your wiki, saved as plain markdown in `chats/`. "Ingest → wiki" promotes the conversation into permanent pages; per-message "Save as wiki page" promotes a single answer.*

![Schema editor — split-pane markdown editor with live preview](docs/screenshots/06-schema-editor.png)
*`/schema` — edit `CLAUDE.md` (the LLM's operating contract) with a split-pane markdown editor + live preview. Auto-backup to `.llm-wiki/schema-history/` on every save.*

### Settings + multi-wiki

![Settings General — topic, approval gate, default folder](docs/screenshots/07-settings-general.png)
*`/settings` — one-line wiki topic (the LLM reads this on every operation), optional approval gate for ingest, theme picker, default models per operation slot.*

![Settings Costs — per-model cumulative usage breakdown](docs/screenshots/08-settings-costs.png)
*`/settings → Costs` — cumulative tokens + spend per (model, operation) pair. The `Cost (recorded)` column populates as new LLM calls land; historical rows get backfilled from the pricing table on next startup.*

![Active wiki dropdown in the header](docs/screenshots/09-wiki-switcher.png)
*Header chip → dropdown with the active wiki (topic + folder path), plus quick links to Create / Manage. Same actions are reachable from `⌘K` ("Switch to…" group) and `/dashboard` (per-wiki cards with Switch buttons).*

---

## What's in v1.2

> **Recent patches:**
> - **v1.2.3** *(2026-05-27)* — **free OpenRouter models** added to the Settings → Models dropdown (Llama 3.3 70B, Nemotron Super 120B, DeepSeek V4 Flash, Gemma 4 31B). Settings banner explains rate-limit + data-retention tradeoffs. First-run wizard gained a one-click *"Use free models by default"* toggle so the cost-to-first-ingest is zero. ([release](https://github.com/ddsyasas/llm-wiki/releases/tag/v1.2.3))
> - **v1.2.2** *(2026-05-26)* — CLI now prints an update-available banner on `llm-wiki start` when a newer version is on npm. Cached on disk, refreshed in the background, silenced by `NO_UPDATE_NOTIFIER=1` or `--quiet`. ([release](https://github.com/ddsyasas/llm-wiki/releases/tag/v1.2.2))
> - **v1.2.1** *(2026-05-26)* — fixes two regressions from the v1.2.0 Ollama refactor: the Sources/Query pages crashed the moment text was typed/pasted, and PDF ingest failed with `Cannot read properties of undefined (reading '0')`. PDFs now ride OpenRouter's `type: "file"` contract; settings types match runtime. ([release](https://github.com/ddsyasas/llm-wiki/releases/tag/v1.2.1) · [known-issues thread](https://github.com/ddsyasas/llm-wiki/issues/3))

### The three operations (Karpathy's pattern)

- **Ingest** — Drop a source (text / file / URL / PDF / image) → the LLM reads it + your existing wiki, writes new pages, updates older pages where context shifts, refreshes the index, logs the change. Each ingest is a *refactor pass*, not an append.
- **Query** — One-shot Q&A against the whole wiki with cited pages. "Save as wiki page" promotes useful answers into permanent entries.
- **Lint** — Two-pass health check: local scan (broken links, orphans) + LLM pass (contradictions, gaps, stale claims, missing pages). Every issue ships with **one-click fixes** — including LLM-powered ones that write the page edit for you.

### Workflow features

- **Sources page** — Add via paste, drag-and-drop, or URL. Auto-detects format. Cost preview before every ingest. Per-source detail view shows the raw text, contributing wiki pages, and metadata.
- **Wiki landing** — Cards grouped by type (Overviews → Concepts → Entities → Comparisons → Sources). Search/filter sidebar. Click any card → page view with backlinks + source lineage + inline edit.
- **3D Graph view** *(new in v1.0)* — Force-directed graph of every page and every `[[wikilink]]`. Same engine as Obsidian's 3D Graph plugin, but colored by **page type** (not free-form tag), so the structure of your knowledge is visible at a glance. Click-to-focus reveals neighbors; drag/scroll to orbit; URL-state for deep links. Spec: [`docs/12-graph-view.md`](docs/12-graph-view.md).
- **Chats** — Multi-turn conversations saved as `.md` files in folders. Per-message "Save as wiki page" + whole-chat "Ingest → wiki" buttons close the loop from exploratory thinking back into the permanent layer.
- **Schema editor** — Edit the `CLAUDE.md` contract the LLM reads on every operation. Split-pane preview, auto-backup to `.llm-wiki/schema-history/`.
- **Log timeline** — `/log` shows every ingest / edit / lint / schema-save in chronological order. Wikilinks inside log entries are clickable.
- **Multiple wikis** — keep separate wikis for separate topics (e.g. "Physics", "ML research", "Personal KB"). Switch from the active-wiki chip in the header, the `Cmd+K` palette, or **Settings → Wikis** (full CRUD). Switching is in-place — you stay on whatever page you're on, the data refreshes around you. Spec: [`docs/13-multi-wiki.md`](docs/13-multi-wiki.md).
- **Wiki health dashboard** at `/dashboard` *(new in v1.x)* — cross-wiki overview: per-wiki page / source / chat counts, cumulative LLM spend, last-touched timestamps, sortable by recency. Roll-up totals at the top. One-click switch into any wiki.

### Quality / safety

- **First-run gate** — A real wizard collects the wiki topic + an LLM provider (OpenRouter API key OR a local Ollama install — see below) before letting you wander. No silent failures on first ingest.
- **Local models support (Ollama)** *(new in v1.2)* — first-class per-slot provider option in Settings → Models. Run any operation (ingest / query / chat / lint / vision) against a model on your own machine instead of OpenRouter. Free per query after the one-time model download, fully private (data never leaves your laptop). Dedicated `/local-models` setup guide in-app covers install + a hardware-requirements table mapping common models (llama3, mistral, phi3, llava, mixtral, llama3:70b, etc.) to RAM / disk / expected tokens-per-sec on Apple Silicon and CPU-only.
- **Page-history backups** — Every page edit (manual or LLM-driven) backs up the prior version to `.llm-wiki/page-history/`.
- **Cost transparency** — Estimated cost shown before every LLM operation; running cumulative tally in Settings → Costs.
- **Source lineage** — Every wiki page lists which raw sources it was compiled from; every source lists which wiki pages it contributed to. Bidirectional graph traversal.
- **Index integrity** — `index.md` auto-refreshes on every page edit. Click "Rebuild index" anytime for a full re-sweep.

### Settings

Five model slots tunable per-operation: `ingest` / `query` / `chat` / `lint` / `vision`. **Per-slot provider picker** *(new in v1.2)*: choose **OpenRouter** (cloud, BYOK, pay-as-you-go) or **Ollama (Local)** (your own machine, free) per slot — mix and match. Curated model dropdowns for each provider plus a custom-slug field for anything else. If any slot uses Ollama, a heads-up banner appears with a link to the `/local-models` setup guide. Light / dark / auto theme. OpenRouter key stored in OS keychain when available.

---

## The on-disk shape

```
~/llm-wiki-default/                  # your wiki folder (set with LLM_WIKI_PATH)
├── CLAUDE.md                        # the schema you edit at /schema
├── index.md                         # auto-maintained catalog of pages
├── log.md                           # every operation, browsable at /log
├── raw/                             # original source files, untouched
├── wiki/                            # LLM-maintained pages (Markdown + frontmatter)
├── chats/                           # chat threads as .md files
└── .llm-wiki/                       # SQLite metadata + page-history + schema-history
```

Everything is plain markdown. Delete the app, open the folder in Obsidian / VS Code / vim — your wiki still works.

---

## Install + run

Three paths. Pick one.

### Hosted — try without installing

The hosted version lives at **[llmwiki.cc](https://llmwiki.cc)**. No install, no Node, no OpenRouter account required to look around — sign up, click around, start ingesting. Currently in waitlist: hosted product launches as paid tiers when the waitlist signals demand. Join the list on the site if you want an email when it goes live.

For everyone who'd rather run it themselves (the local-first promise this project was built on stays untouched), the two install paths below are the canonical way:

### Quick start — install the CLI (recommended)

```bash
npm install -g @syasas/llm-wiki
llm-wiki start
```

That's it — no git clone, no monorepo, ~30 second install. The CLI auto-initializes your wiki folder, picks a free port (3737 by default), and opens the browser. Verified on **macOS / Linux (incl. WSL) / Windows**.

Package on npm: [npmjs.com/package/@syasas/llm-wiki](https://www.npmjs.com/package/@syasas/llm-wiki). Release notes + tarball mirror: [GitHub Releases](https://github.com/ddsyasas/llm-wiki/releases/latest). If npm is unavailable for some reason, you can install directly from the GitHub tarball: `npm install -g https://github.com/ddsyasas/llm-wiki/releases/download/v1.2.3/syasas-llm-wiki-1.2.3.tgz`.

### From source — for development or contributing

```bash
git clone https://github.com/ddsyasas/llm-wiki.git
cd llm-wiki
pnpm install
pnpm dev
```

Open `http://localhost:3000` → the first-run wizard collects your wiki topic + an LLM provider (OpenRouter API key, or set up a local [Ollama](https://ollama.com) install if you'd rather run models on your own machine) → you're in.

### Prerequisites

| Tool | Minimum | How to get it |
|---|---|---|
| **Node.js** | 20.x | [nodejs.org](https://nodejs.org) or `nvm install 20` (recommended) |
| **LLM provider** | one of: | Pick **either** an OpenRouter key OR a local Ollama install (or both — mix per-slot) |
| ↳ OpenRouter (cloud) | — | [openrouter.ai/keys](https://openrouter.ai/keys) — pay-as-you-go, ~$5 lasts most users 2-4 weeks at default models. Best quality (frontier Claude / GPT / Gemini). |
| ↳ Ollama (local) | — | [ollama.com/download](https://ollama.com/download) + `ollama pull llama3` (or similar). Free per query, runs on your machine. See in-app `/local-models` page for full install + hardware requirements per model. |
| **pnpm** *(source path only)* | 8.x | `npm install -g pnpm` |

Check with `node --version` before you start. **At least one LLM provider is required** — without either an OpenRouter key or a running Ollama, ingest / query / chat / lint all fail. If you only use Ollama, no OpenRouter key is needed.

### `llm-wiki: command not found` after install

The package installed fine — npm just put the binary somewhere your shell isn't looking. Common on WSL Ubuntu when Node was installed via apt with a non-standard npm prefix. Diagnostic:

```bash
# Find where npm put the binary
npm prefix -g

# Confirm it landed there
ls -la "$(npm prefix -g)/bin/llm-wiki"

# One-off: run via full path
"$(npm prefix -g)/bin/llm-wiki" doctor
```

Permanent fix (one-time):

```bash
echo 'export PATH="$(npm prefix -g)/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
llm-wiki doctor
```

(On zsh, swap `~/.bashrc` for `~/.zshrc`. On Windows PowerShell, `npm install -g` normally puts bins in `%AppData%\npm\` which is on PATH by default — if you hit this on Windows, run `npm config get prefix` and add `<that>/bin` to your user PATH via System Properties.)

## `CLAUDE.md`

# Project Brief for Claude Code

You are building **LLM Wiki**, an open source local-first knowledge base inspired by Andrej Karpathy's LLM Wiki pattern (gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## Read this first

Before writing any code, read every file in `/docs/` in numerical order. Each file is short and focused. Together they form the complete spec.

1. `docs/01-vision.md` - What this is and who it's for
2. `docs/02-architecture.md` - Stack, repo layout, distribution
3. `docs/03-data-model.md` - On-disk structure and SQLite schema
4. `docs/04-features-v1.md` - Exact V1 feature scope
5. `docs/05-llm-integration.md` - OpenRouter, prompts, JSON contracts
6. `docs/06-ingest-pipeline.md` - How sources become wiki pages
7. `docs/07-chat-threads.md` - Chat feature spec
8. `docs/08-ui-design.md` - Design language and key screens
9. `docs/09-cli-distribution.md` - CLI behavior and npm packaging
10. `docs/10-build-order.md` - Sequenced build plan, follow this exactly
11. `docs/11-attribution-license.md` - Naming, credits, license

## Core principles, do not violate

1. **Everything is a file**. The wiki, chats, schema, log all live as plain `.md` files in the user's chosen folder. SQLite is metadata only.
2. **Local-first, BYOK**. No telemetry, no remote storage, no auth. Users bring their own OpenRouter key.
3. **One language**: TypeScript everywhere. No Python sidecars in V1.
4. **Cross-platform**: Mac, Windows, Linux all supported from day one.
5. **Karpathy's three operations** are central: ingest, query, lint. Build them as separate, well-named modules.

## Stack lock-in

- Next.js (App Router) for the whole app
- Tailwind + shadcn/ui for UI
- `better-sqlite3` for metadata
- `openai` SDK pointed at OpenRouter
- pnpm for package management
- TypeScript strict mode

Do not introduce new frameworks without asking.

## Working conventions

- TypeScript strict mode, no `any` without comment explaining why
- Functions over classes where possible
- File names: kebab-case
- React components: PascalCase
- No default exports for shared modules, named exports only
- Comments explain *why*, not *what*
- Every LLM operation must validate its JSON response before using it

## Don't do these things

- Don't add localStorage or sessionStorage anywhere (server-side app, doesn't apply)
- Don't introduce React Native, Electron, or Tauri yet (that's V2)
- Don't add a database other than SQLite
- Don't add telemetry, analytics, or external tracking
- Don't put the user's API key in a file that could be committed (use OS keychain or a gitignored env)
- Don't write large monolithic files; split by responsibility

## When in doubt

Refer back to the docs. If a question isn't answered there, ask the user before guessing.

## Attribution

This project is by Yasas. It implements a pattern by Andrej Karpathy. See `docs/11-attribution-license.md` for where credits go.

## `CONTRIBUTING.md`

# Contributing to LLM Wiki

Thanks for considering a contribution. This file exists because the app looks "done" — it ships features, has tests, is on npm — but a lot of meaningful work remains, and it's not obvious from the outside what would actually help. Below is a clear "what we need and where this is going" so you can pick something worth your time.

> **Never sent a pull request before?** Read **[docs/contributor-walkthrough.md](docs/contributor-walkthrough.md)** first — it walks through fork / clone / branch / commit / push / PR step by step with exact commands. Come back here once you've got that workflow down.

> If you only read one other file beyond this one: [`docs/01-vision.md`](docs/01-vision.md) explains *what this is and isn't*, and [`docs/14-roadmap.md`](docs/14-roadmap.md) has the full open-work list this file summarizes.

---

## Where this project is going

Three tiers, in priority order:

**V1.x — what we're polishing now.** The core product (Karpathy's three operations: ingest, query, lint) is shipped and works end-to-end on Mac / Linux / Windows. V1.x is about closing real-world rough edges: cross-platform testing, native-dep edge cases, UI polish on routes that haven't gotten love yet, performance.

**V2 — material expansion.** Tauri desktop installer (removes Node prerequisite, single-binary install for non-technical users). URL-namespaced multi-wiki (`/w/<id>/wiki` so you can browse multiple wikis in tabs). Embeddings-based search (vector + FTS5 hybrid). Live wiki sync via chokidar so Obsidian/vim edits appear in the browser instantly. Ollama support so users can run local models without OpenRouter.

**V3 — different category.** MCP server mode (expose the wiki as memory for Claude Desktop / other agents). Plugin system (user-authored extractors, prompts, lint rules). Possibly a cloud-hosted version for users who don't want to self-host. These are explicitly long-horizon — don't start work on them without proposing the shape first.

The project will **stay** local-first, BYOK, MIT, and TypeScript-only. There's no plan to add telemetry, auth, hosted SaaS-by-default, or to rewrite the core in another language. If your contribution idea conflicts with these, it's probably not a good fit — open a discussion first.

---

## What we need help with right now

Pick something here, or propose your own (open an issue first so we can talk about fit before you write code).

### 🟢 Quick wins (≤ 1 hour, good first PR)

Low scope, mentored, high signal-to-effort. Pick one of these for your first PR.

1. **Cross-platform install QA.** `npm install -g @syasas/llm-wiki` and run `llm-wiki doctor` on a platform we haven't verified — recent Ubuntu LTS, Fedora, Arch, Windows 11, macOS Sequoia on Intel, FreeBSD, anything. Report results (working / breaks how) as a GitHub issue with the `platform` label.

2. **Doc clarifications.** Find something in `docs/` or the README that's unclear, outdated, or assumes too much. Open a PR with the fix. Even a single confusing paragraph is welcome.

3. **In-app screenshots refresh.** When the UI changes (it will), the screenshots under [`docs/screenshots/`](docs/screenshots/) drift. Periodic refresh PRs are useful.

4. **Test coverage for an under-tested module.** Look at `packages/core/src/` — anything without a `.test.ts` neighbor is fair game. `editor.ts`, `index-builder.ts`, `links.ts` are good candidates.

5. **Lint flake.** `packages/core/src/sync.test.ts` has one chokidar live-watch test that fails ~1 in 5 runs (race in the test, not the production code). Hunt down the race condition and stabilize it.

### 🟡 Medium (1–3 hours, mid-experience)

These need a bit more context but each is bounded.

6. **Persistent camera state on `/graph`.** Remember the last camera position when navigating away and returning. Store in URL hash or localStorage; restore on mount. The 3D graph code is in `apps/web/src/components/graph/vault-graph.tsx`.

7. ~~**Local-model UI support (Ollama).**~~ ✅ **Shipped in v1.2.0** by [@savindugeethma](https://github.com/savindugeethma) in [PR #2](https://github.com/ddsyasas/llm-wiki/pull/2). Provider picker (OpenRouter / Ollama) per slot in Settings → Models. Setup guide + per-model hardware requirements at the in-app `/local-models` page.

8. **Scheduled lint runs.** Cron-style: "Run lint nightly, append result to `log.md`." Either an in-process scheduler (when `llm-wiki start` is running) or a CLI subcommand (`llm-wiki lint --report-to-log`). Discuss approach in an issue first.

9. **Wiki templates beyond the 5 we ship.** [`packages/core/src/templates.ts`](packages/core/src/templates.ts) has Blank / Research / Legal / Clinical / Project / Personal. Want to add Academic Course Notes? Investing? Recipe collection? Fork the file, add an entry, PR it.

10. **2D graph toggle.** `react-force-graph-2d` has a near-identical API to the 3D version we use. Add a toggle in the graph view. Users on weak GPUs or who prefer flat views benefit.

### 🔴 Big (V2-scoped, propose first)

Real architectural work. **Open an issue and discuss the approach before writing code** — these touch enough of the codebase that "surprise PR" is almost guaranteed to need rework.

11. **Tauri desktop installer.** Wrap the Next.js server in a Tauri shell so users get a single-binary native app (no Node prerequisite). Biggest unlock for non-technical users. Needs a thoughtful approach to file-open helpers (browser sandboxes block `file://` so opening a raw source in the user's editor doesn't work today).

12. **Embeddings-based search.** Today FTS5 covers keyword matches. Vector search would handle "find me anything about quantum supremacy even if it's phrased differently." OpenAI / Voyage / local embeddings via Ollama. Storage: a sidecar SQLite table with embeddings, hybrid retrieval.

13. **Live wiki sync via chokidar.** Half-built — the file watcher exists in `packages/core/src/sync.ts`. Wire it to `revalidatePath()` so external edits (Obsidian, vim) show up in the browser without a manual refresh.

14. **`FileSystem` interface extraction (V2 prep for cloud).** Pure refactor with no behavior change. Today `packages/core/src/wiki.ts`, `index-builder.ts`, `editor.ts`, `chat.ts` all call `node:fs/promises` directly. Lift those calls behind a small interface (`readFile`, `writeFile`, `readdir`, `stat`, `mkdir`) so the file-IO layer is swap-able: local FS today, S3/R2 if a cloud version ever happens. Bonus: cleaner test seams.

15. **GitHub Actions CI matrix.** No CI yet. A workflow that runs `pnpm install + pnpm test + pnpm typecheck` on push, plus the install-and-doctor smoke test on `macos-latest / ubuntu-latest / windows-latest`. Cross-platform regressions caught automatically.

### 🐛 Bug reports

If you hit something broken, open a GitHub issue with the **🐛 Bug report** template. Include OS / Node version / `llm-wiki version` output. Bug reports with reproduction steps are themselves a contribution.

### 💡 Ideas + design discussions

For "what if we did X" conversations that don't fit an issue, open a [GitHub Discussion](https://github.com/ddsyasas/llm-wiki/discussions). Lower stakes than an issue, doesn't need a fix attached.

---

## What we don't want

These would be rejected — please don't spend time on them unless you've talked them through first:

- **Telemetry, analytics, error reporting back to us.** Strict no in v1, must be opt-in + clearly disclosed if ever added.
- **A different database than SQLite** for core metadata. Single-file portability is a feature.
- **A rewrite of any core layer in a different language.** TypeScript everywhere is a hard rule.
- **New frameworks.** No Electron, no Vite-as-build-tool, no different UI lib than React/Tailwind/shadcn.
- **Features that require a server we run.** Stays local-first, BYOK.
- **Cosmetic refactors** that don't fix a bug or unlock a feature — code style, mass `const`/`let` swaps, prettier-config bikeshedding.
- **AI-generated PRs** without a human reviewer. If you used an AI to draft something, that's fine, but read every diff and own the result. Drive-by AI PRs that the submitter can't explain get closed.
- **V3 features built speculatively.** MCP, plugins, cloud — these need architectural discussion before code lands.

The full non-goals list is in [`docs/01-vision.md`](docs/01-vision.md) and [`docs/04-features-v1.md`](docs/04-features-v1.md) ("What V1 does NOT include").

---

## How to actually contribute

### One-time setup

Requires Node 20+ and pnpm 8+.

```bash
git clone https://github.com/ddsyasas/llm-wiki.git
cd llm-wiki
pnpm install
pnpm dev          # http://localhost:3000
```

You'll need an [OpenRouter API key](https://openrouter.ai/keys) (~$5 lasts most users 2-4 weeks at default models) to test ingest / query / lint features.

### Before you start coding

1. **Read [`CLAUDE.md`](CLAUDE.md)** at the repo root — the do/don't list the project's design contract is built on.
2. **Find or open an issue** for the work. For anything Medium-or-bigger, propose your approach in the issue before writing code. Avoid "surprise PRs."
3. **Branch from `main`** with a name like `fix/<short-thing>` or `feat/<short-thing>`.

### While coding

- TypeScript strict mode, no `any` without a comment explaining why.
- Functions over classes where possible.
- Named exports for shared modules (no default exports outside Next routes).
- File names: `kebab-case`. React components: `PascalCase`.
- Comments explain *why*, not *what*. Don't comment obvious code.
- Every LLM operation must validate its JSON response via zod before using it.

### Before opening the PR

```bash
pnpm -r exec tsc --noEmit                            # typecheck everything
pnpm --filter @llm-wiki/core test --run              # ~158 core tests
pnpm --filter @llm-wiki/llm test --run               # ~25 llm tests
pnpm --filter @llm-wiki/ingestion test --run         # ~11 ingestion tests
```

All three should pass. (One known chokidar live-watch flake exists — re-run if it's the only failure.)

### Opening the PR

Use the PR template (loads automatically when you "Open Pull Request" on GitHub). Required fields:

- **What** changed (one paragraph)
- **Why** — link the issue you're closing
- **How tested** — automated tests added, manual steps if UI
- **Screenshots** — if any visible UI change
- **Breaking** — flag any backward-incompat change (wiki on-disk format must stay stable within a major version)

PRs that don't follow the template may get pushed back with "please fill in the template" — not personal, just keeps review tractable.

### Getting your PR reviewed

Maintainer (currently just [@ddsyasas](https://github.com/ddsyasas)) reviews when time allows. No SLA — this is a side project. Reasonable patches usually get a first pass within a week. If a PR sits for 2+ weeks without a comment, ping it.

---

## Code of conduct

This project adopts the [Contributor Covenant 2.1](CODE_OF_CONDUCT.md). Read it. Behaviors that violate it get a warning, then a ban. Report via GitHub Issues or yasas@idersolutions.com.

---

## Security

Found a security issue? **Please don't open a public issue.** Use [GitHub's private vulnerability reporting](https://github.com/ddsyasas/llm-wiki/security/advisories/new) or email yasas@idersolutions.com directly. See [`SECURITY.md`](SECURITY.md) for full policy.

---

## License + attribution

By contributing, you agree your contribution is licensed under the [MIT License](LICENSE), same as the rest of the project. You retain copyright; the license just covers reuse.

LLM Wiki implements a pattern described by [Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). The pattern is his, the implementation is independent. The project is not affiliated with Karpathy or Anthropic.

---

## Recognition

Significant contributors get added to a "Contributors" section in the README. Small fixes get a "thank you" in the release notes. Currently the contributor list is just the author — looking forward to someone else's name showing up there.

## `SECURITY.md`

# Security Policy

LLM Wiki is a local-first application that runs entirely on the user's machine and talks only to OpenRouter (the user's chosen LLM provider). The threat surface is small, but it isn't zero — anything that handles user files, parses external content (URLs, PDFs, HTML), or stores API keys is worth thinking about.

## Supported versions

| Version | Supported |
|---------|-----------|
| 1.1.x   | ✅ Yes — current stable, gets security fixes |
| 1.0.x   | ⚠ Best-effort — upgrade to 1.1.x recommended |
| < 1.0   | ❌ Not supported |

When v2.0 ships, 1.1.x will continue to get security fixes for 6 months.

## Reporting a vulnerability

**Please do not open a public GitHub issue for security problems.** Public disclosure before a fix is ready puts users at risk.

Use one of these private channels:

- **GitHub private vulnerability reporting** (preferred): [Open a security advisory](https://github.com/ddsyasas/llm-wiki/security/advisories/new). Only maintainers can see it.
- **Email**: yasas@idersolutions.com — encrypt with PGP if you want, public key on request.

Include in your report:

- What the vulnerability is, in plain language
- Steps to reproduce (or a proof-of-concept if you have one)
- The impact you think it could have
- Your name / handle if you want credit in the fix announcement

## What to expect after you report

| Time | What we do |
|---|---|
| Within 7 days | Acknowledge the report; ask follow-up questions if anything's unclear |
| Within 30 days | Provide an initial assessment — confirmed / not-a-bug / out-of-scope, severity rating, rough fix timeline |
| Variable | Develop and test the fix in a private branch |
| At fix release | Coordinate public disclosure; credit you in the release notes unless you prefer to stay anonymous |

This is a side-project maintained by one person. We'll do best-effort on the timelines above but can't promise enterprise-style SLAs. Critical issues (RCE, key exfiltration, etc.) will be prioritized over lower-severity ones.

## What counts as in-scope

- The published `@syasas/llm-wiki` npm package (any supported version)
- The source code in this repository on the `main` branch
- The CLI (`bin/llm-wiki.mjs`) and its installation flow
- The Next.js server bundle and any API route under `/api/`
- The on-disk format (wiki folder, `.llm-wiki/` metadata directory, `~/.llm-wiki/config.json`)
- Any handling of OpenRouter API keys (in keychain, in the file fallback, in HTTP requests)

## What's out of scope

- Issues in third-party dependencies that aren't exploitable through LLM Wiki itself (file those upstream)
- "The app talks to the internet when it makes LLM calls" — yes, that's by design; the only outbound traffic is to OpenRouter (or whatever provider URL the user configured)
- Issues that require physical access to a machine that's already running LLM Wiki — at that point, the attacker has the user's whole filesystem
- Social engineering attacks against maintainers
- Brute-force attacks on the user's OpenRouter API key (that's OpenRouter's responsibility)
- Issues affecting deprecated versions (< 1.0)

## Known security-relevant design choices

These are intentional and documented for transparency:

- **API keys are stored in the OS keychain when available** (`keytar`), falling back to a `chmod 600` file at `~/.llm-wiki/config.json`. The fallback is acceptable for local-only use but means anyone with shell access to the user's account can read the key.
- **No authentication on the local web server.** The server binds to `127.0.0.1` by default, so it's only reachable from the same machine. Don't expose the port externally without adding your own auth layer.
- **HTML/URL ingestion uses `@mozilla/readability` + `jsdom`** to extract clean text. We do not execute JavaScript from ingested pages, but jsdom does parse them — known CVEs in jsdom are inherited until upgraded.
- **No telemetry, no error reporting, no version-check pings.** Nothing leaves the user's machine except LLM calls to their configured provider.

## Hall of Fame

Reporters who help us fix real security issues will be listed here (with permission). Currently empty — be the first.

## `package.json`

{
  "name": "llm-wiki-monorepo",
  "version": "0.1.0",
  "private": true,
  "description": "LLM Wiki monorepo root. Published package is apps/web.",
  "license": "MIT",
  "author": "Yasas",
  "engines": {
    "node": ">=20.0.0"
  },
  "packageManager": "pnpm@10.12.1",
  "scripts": {
    "dev": "pnpm --filter @llm-wiki/web dev",
    "build": "pnpm -r build",
    "lint": "pnpm -r lint",
    "test": "vitest run",
    "test:watch": "vitest",
    "typecheck": "pnpm -r typecheck",
    "format": "prettier --write \"**/*.{ts,tsx,js,jsx,json,md,css}\"",
    "format:check": "prettier --check \"**/*.{ts,tsx,js,jsx,json,md,css}\""
  },
  "devDependencies": {
    "@types/node": "^20.14.0",
    "eslint": "^8.57.0",
    "prettier": "^3.3.3",
    "typescript": "^5.5.4",
    "vitest": "^2.0.5"
  },
  "pnpm": {
    "onlyBuiltDependencies": ["better-sqlite3", "keytar"]
  }
}

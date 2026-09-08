
# Consumption and Agent Interfaces

## Human consumption

Humans need:

- maps of content;
- readable pages;
- inline citations;
- source previews;
- revision diffs;
- discussion and review history;
- freshness labels;
- disputed-content markers;
- timelines and comparison tables.

Markdown should remain readable without the application.

## Agent consumption

Agents need:

- stable IDs;
- machine-readable frontmatter;
- page and claim schemas;
- index and routing APIs;
- bounded graph traversal;
- source and evidence expansion;
- as-of queries;
- freshness and trust filters;
- change feeds;
- explicit token budgets.

## Context pack

A context pack is a deterministic, task-specific bundle:

```yaml
pack_id:
task:
as_of:
wiki_release:
ontology_version:
pages:
claims:
sources:
open_conflicts:
freshness:
token_budget:
build_manifest:
```

It should not copy mutable values without version references.

## Query protocol

1. Classify the question: explanatory, comparative, factual, temporal, evaluative, or action-oriented.
2. Determine freshness and trust requirements.
3. Route through maps and search.
4. Select pages.
5. Expand disputed or high-risk statements to claims and source evidence.
6. Answer with page, claim, and source references.
7. State uncertainty and as-of time.
8. Record missing knowledge or evaluation needs.
9. Keep the answer ephemeral unless a filing proposal is requested.

## Filing an answer back

A useful query answer may become:

- a research question;
- a gap page;
- a synthesis page;
- a proposed edit;
- a new context pack;
- an agent skill.

It must re-enter the normal build pipeline. The answer cannot cite itself as evidence.

## APIs

Initial interfaces:

- filesystem and Git;
- deterministic CLI;
- JSON/YAML exports;
- full-text search;
- optional vector and graph indexes;
- MCP tools;
- read-only HTTP API.

Suggested MCP tools:

```text
wiki_route
wiki_search
wiki_read_page
wiki_read_claim
wiki_read_source
wiki_graph_neighbors
wiki_get_context_pack
wiki_get_revision
wiki_diff
wiki_propose_change
wiki_lint
```

Write tools should produce proposals only unless the caller has explicit approval and publishing capabilities.

## Consumer profiles

- **reader** — published pages only;
- **researcher** — pages, claims, evidence, disputed material;
- **collector** — source registry and discovery queues;
- **editor** — candidate changes and review;
- **auditor** — histories, logs, rejected and rolled-back changes;
- **automation agent** — restricted task-specific context packs.

## Freshness

Every answer should be able to expose:

- page revision;
- claim revision;
- source revision;
- last dependency check;
- known stale dependencies;
- requested as-of time.

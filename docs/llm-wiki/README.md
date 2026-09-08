# LLM Wiki for This Repository

LLM Wiki is the repository's intended **knowledge digestion and organization layer**.

It converts the source collection into a persistent, navigable, reviewable body of knowledge that compounds over time. It is not a replacement for raw sources, atomic claims, ontology, evidence governance, or source-specific materialization.

## Core equation

```text
immutable source revisions
+ source-specific materialization
+ normalized metadata
+ claim/evidence graph
+ ontology and identity
+ governed compilation
= LLM Wiki
```

## Read in this order

1. [`01-principles-and-boundaries.md`](01-principles-and-boundaries.md)
2. [`02-reference-architecture.md`](02-reference-architecture.md)
3. [`03-knowledge-page-and-claim-model.md`](03-knowledge-page-and-claim-model.md)
4. [`04-build-pipeline.md`](04-build-pipeline.md) — primary implementation specification
5. [`05-aggregation-linking-and-navigation.md`](05-aggregation-linking-and-navigation.md)
6. [`06-evaluation-and-quality-gates.md`](06-evaluation-and-quality-gates.md)
7. [`07-admission-governance-and-evolution.md`](07-admission-governance-and-evolution.md)
8. [`08-consumption-and-agent-interfaces.md`](08-consumption-and-agent-interfaces.md)
9. [`09-repo-implementation-plan.md`](09-repo-implementation-plan.md)
10. [`10-runbooks-prompts-and-jobs.md`](10-runbooks-prompts-and-jobs.md)
11. [`11-threat-model-and-failure-modes.md`](11-threat-model-and-failure-modes.md)
12. [`12-open-questions-and-research-agenda.md`](12-open-questions-and-research-agenda.md)
13. [`13-research-basis.md`](13-research-basis.md)
14. [`14-source-specific-consumption.md`](14-source-specific-consumption.md)

Architecture decisions:

- [`decisions/ADR-001-wiki-is-a-derived-view.md`](decisions/ADR-001-wiki-is-a-derived-view.md)
- [`decisions/ADR-002-claim-level-provenance.md`](decisions/ADR-002-claim-level-provenance.md)
- [`decisions/ADR-003-proposal-review-merge.md`](decisions/ADR-003-proposal-review-merge.md)

Examples:

- [`templates/wiki-page.example.yaml`](templates/wiki-page.example.yaml)
- [`templates/wiki-change.example.yaml`](templates/wiki-change.example.yaml)
- [`templates/claim.example.yaml`](templates/claim.example.yaml)

## What is borrowed

From the compiled-wiki pattern:

- immutable raw sources;
- persistent Markdown pages;
- schema or operating contract;
- ingest, query, and lint;
- content index and chronological log;
- Git-native review and history.

From STORM and Co-STORM:

- perspective discovery;
- research before writing;
- outline-first generation;
- multi-agent question exploration;
- mind maps and human steering.

From Wikipedia and Wikidata:

- inline sourcing;
- no circular sourcing;
- neutral synthesis and due weight;
- discussion and consensus;
- statement qualifiers, references, and ranks;
- explicit unknown and no-value states;
- revision history, deprecation, and rollback.

From this repository's ontology work:

- stable identity;
- claim/evidence separation;
- time and uncertainty;
- source bindings;
- action and policy;
- semantic diff, migration, and rollback.

From the materialization layer:

- source-specific adapters;
- pinned revisions and hashes;
- TeX-first arXiv consumption;
- repository-to-wiki semantic capsules;
- stable source selectors;
- explicit extraction loss and semanticization status.

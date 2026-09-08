
# Repository Implementation Plan

## Goal

Construct a small, trustworthy LLM Wiki over the existing source collection before optimizing scale or interface polish.

## Phase 0 — contracts and fixtures

Already completed in this batch:

- LLM Wiki collection and audit;
- page and change schemas;
- source corpus documentation;
- build, evaluation, admission, and consumption design;
- documentation validation.

Next fixtures:

- three example claim records;
- two example source revisions;
- four page types;
- one source-update case;
- one source-retraction case;
- one entity-merge case;
- one contested claim.

## Phase 1 — source registry and materialization

Deliverables:

```text
source_registry/
materialized_sources/
parsing_reports/
```

Implement:

- canonical ID resolution;
- revision selection;
- checksum;
- TeX and Markdown parsing first;
- rights state;
- source selector generation;
- source diff.

Acceptance:

- selected P0 source revisions can be reproduced;
- source changes are detectable;
- raw files are read-only to the compiler.

## Phase 2 — claim and evidence layer

Create:

```text
knowledge/claims/
knowledge/evidence/
knowledge/entities/
knowledge/contradictions/
```

Use `knowledge_model.schema.yaml`.

Implement:

- candidate extraction;
- assertion-kind classification;
- evidence selectors;
- entity resolution proposals;
- contradiction and duplicate detection;
- claim promotion state.

Acceptance:

- every candidate claim resolves to source text;
- unsupported candidates are rejected or retained as questions;
- merge/split proposals are reversible.

## Phase 3 — first wiki compiler

Page types:

- map;
- concept;
- method;
- system;
- comparison;
- source;
- gap;
- debate.

Implement:

- page planning;
- outline generation;
- section compilation;
- page frontmatter;
- typed links;
- paragraph citations;
- `WikiChange` generation;
- candidate workspace.

Acceptance:

- no direct edits to published pages;
- deterministic build manifest;
- all references validate;
- at least 20 pages from the P0 corpus.

## Phase 4 — review and publication

Implement:

- automated gate report;
- human-readable diff;
- reviewer assignment;
- approve/reject/revise;
- Git-backed merge;
- immutable release tag;
- rollback.

Acceptance:

- one complete approval;
- one rejected change retained in lineage;
- one tested rollback;
- one contested page.

## Phase 5 — retrieval and context packs

Implement:

- root index;
- maps of content;
- lexical search;
- typed graph traversal;
- fixed context-pack builder;
- read-only MCP.

Acceptance:

- fixed question suite;
- cited answers;
- page/claim/source expansion;
- measurable token budget.

## Phase 6 — maintenance

Implement:

- source refresh;
- dependency-aware rebuild;
- contradiction lint;
- stale-page lint;
- orphan and link lint;
- retraction propagation;
- scheduled reports.

Acceptance:

- a changed source updates only affected pages;
- a retracted source downgrades dependent claims;
- no silently unsupported published section remains;
- repair and rollback are reproducible.

## Phase 7 — scale and meta-evolution

Only after earlier phases:

- embeddings;
- graph communities;
- multi-agent parallel compilation;
- million-document routing;
- automated evaluator improvement;
- prompt/schema optimization;
- multi-wiki federation.

## Suggested first corpus

Start with 25–40 P0 sources spanning:

- RSI and open-ended evolution;
- Auto Research;
- knowledge editing and memory;
- ontology and provenance;
- LLM Wiki and evaluation.

The first wiki should optimize for cross-domain synthesis, not collection size.

## Repository integration

Add future outputs as separate top-level directories. Do not write generated pages into `raw_data/`.

Extend CI with:

- claim schema validation;
- wiki page schema validation;
- wiki change schema validation;
- source and claim reference checks;
- Markdown link checks;
- build reproducibility check;
- evaluation threshold report.

## Ownership

Assign owners for:

- source registry;
- ontology and identity;
- claim extraction;
- wiki compiler;
- evaluation;
- admission policy;
- release and rollback.

No single model invocation owns all seven.

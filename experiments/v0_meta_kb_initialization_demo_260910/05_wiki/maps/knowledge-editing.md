---
uid: wiki-page:map-knowledge-editing
title: Knowledge Editing
slug: maps/knowledge-editing
page_type: map
status: review
summary: Routing map for knowledge editing sources, questions, and claims.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:40178c8dde6cbf34
- claim:4715a4ff3b1706fd
- claim:65d2f5de5c0ecdfd
- claim:69e9059578125358
- claim:ad198ecf5d0cad6b
- claim:d6b9ad7b6c2678cc
source_refs: &id001
- arxiv-2110.11309
- arxiv-2104.00405
- arxiv:2310.16218
page_refs:
- wiki-page:source-c707950005ce916a
- wiki-page:source-9923ee576cd59e46
- wiki-page:source-003e063d0c302d83
- wiki-page:knowledge-evolution-loop
- wiki-page:freshness-versioning-and-rollback
outgoing_links:
- target: wiki-page:source-c707950005ce916a
  relation: explains
  claim_refs:
  - claim:ad198ecf5d0cad6b
  - claim:40178c8dde6cbf34
  notes: null
- target: wiki-page:source-9923ee576cd59e46
  relation: explains
  claim_refs:
  - claim:4715a4ff3b1706fd
  - claim:69e9059578125358
  notes: null
- target: wiki-page:source-003e063d0c302d83
  relation: explains
  claim_refs:
  - claim:d6b9ad7b6c2678cc
  - claim:65d2f5de5c0ecdfd
  notes: null
- target: wiki-page:knowledge-evolution-loop
  relation: related
  claim_refs:
  - claim:40178c8dde6cbf34
  - claim:4715a4ff3b1706fd
  - claim:65d2f5de5c0ecdfd
  - claim:69e9059578125358
  - claim:ad198ecf5d0cad6b
  - claim:d6b9ad7b6c2678cc
  notes: null
- target: wiki-page:freshness-versioning-and-rollback
  relation: related
  claim_refs:
  - claim:40178c8dde6cbf34
  - claim:4715a4ff3b1706fd
  - claim:65d2f5de5c0ecdfd
  - claim:69e9059578125358
  - claim:ad198ecf5d0cad6b
  - claim:d6b9ad7b6c2678cc
  notes: null
sections:
- heading: Source coverage
  claim_refs: []
  source_refs: *id001
  editorial_intent: Route by source family.
- heading: Source-reported signals
  claim_refs:
  - claim:4715a4ff3b1706fd
  - claim:ad198ecf5d0cad6b
  - claim:d6b9ad7b6c2678cc
  source_refs:
  - arxiv-2104.00405
  - arxiv-2110.11309
  - arxiv:2310.16218
  editorial_intent: Preserve source-authored scope.
- heading: Collector assessments
  claim_refs:
  - claim:40178c8dde6cbf34
  - claim:65d2f5de5c0ecdfd
  - claim:69e9059578125358
  source_refs:
  - arxiv-2110.11309
  - arxiv:2310.16218
  - arxiv-2104.00405
  editorial_intent: Preserve collector scope.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:096e2cb4557cf60c
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv-2110.11309@sha256:e838a729a34c09a9044b334ef91e3c1ea36030b9e9e35ba6d6f11747e2b4b570
  - arxiv-2104.00405@sha256:d9ca19652574908e954b524249d31a8b450830023739ee49797f58d52784dd03
  - arxiv:2310.16218@sha256:be80105279b0f4acf0e1817a727c0de41b57db523e6a7bc5369b0e062139f52f
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  manual_edits_preserved: false
review:
  state: needs_human
  reviewers: []
  decision_ref: null
  checked_claim_refs: []
  unresolved_issues:
  - Scientific, semantic, neutrality, and due-weight review remain required before publication.
freshness:
  status: fresh
  checked_at: '2026-09-16T04:30:26Z'
  max_age_days: 30
  source_dependencies: *id001
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: Routing map for knowledge editing sources, questions, and claims.
    short: Routing map for knowledge editing sources, questions, and claims.
    full: null
  estimated_tokens: 607
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:40178c8dde6cbf34
- claim:4715a4ff3b1706fd
- claim:65d2f5de5c0ecdfd
- claim:69e9059578125358
- claim:ad198ecf5d0cad6b
- claim:d6b9ad7b6c2678cc
rights_refs: []
rights_unavailable_source_refs:
- arxiv-2104.00405
- arxiv-2110.11309
- arxiv:2310.16218
---

# Knowledge Editing

Modification of model or knowledge state with locality and rollback controls.

## Routing questions

- What object is edited?
- How are locality and generalization measured?
- How do edits propagate to dependent pages?

## Source coverage

| Source | Type | Tier | Claims |
|---|---|---|---|
| [Fast Model Editing at Scale](../sources/arxiv-2110.11309.md) | `arxiv` | `full_text` | 2 |
| [Avalanche: an End-to-End Library for Continual Learning](../sources/arxiv-2104.00405.md) | `arxiv` | `full_text` | 2 |
| [Knowledge Editing for Large Language Models: A Survey](../sources/arxiv-2310.16218.md) | `arxiv` | `full_text` | 2 |

## Source-reported signals

- **Avalanche: an End-to-End Library for Continual Learning** (source assertion): Learning continually from non-stationary data streams is a long-standing goal and a challenging problem in machine learning. Recently, we have witnessed a renewed and fast-growing interest in continual learning, especially within the deep learning community. 〔[claim:4715a4ff3b1706fd](../claims/claim-4715a4ff3b1706fd.md)〕
- **Fast Model Editing at Scale** (source assertion): While large pre-trained models have enabled impressive results on a variety of downstream tasks, the largest existing models still make errors, and even accurate predictions may become outdated over time. Because detecting all such failures at training time is impossible, enabling both developers and end users of such models to correct inaccurate outputs while leaving the model otherwise intact is desirable. 〔[claim:ad198ecf5d0cad6b](../claims/claim-ad198ecf5d0cad6b.md)〕
- **Knowledge Editing for Large Language Models: A Survey** (source assertion): Large Language Models (LLMs) have recently transformed both the academic and industrial landscapes due to their remarkable capacity to understand, analyze, and generate texts based on their vast knowledge and reasoning ability. 〔[claim:d6b9ad7b6c2678cc](../claims/claim-d6b9ad7b6c2678cc.md)〕

## Collector assessments

- **Fast Model Editing at Scale** (collection assessment): MEND makes the update mechanism itself learnable and exposes generalization/locality requirements for governed knowledge editing. 〔[claim:40178c8dde6cbf34](../claims/claim-40178c8dde6cbf34.md)〕
- **Knowledge Editing for Large Language Models: A Survey** (collection assessment): Provides the taxonomy, evaluation metrics, datasets, locality/generalization criteria, and open problems needed to govern knowledge updates rather than treating updates as an unconstrained write operation. 〔[claim:65d2f5de5c0ecdfd](../claims/claim-65d2f5de5c0ecdfd.md)〕
- **Avalanche: an End-to-End Library for Continual Learning** (collection assessment): Provides an implementation and benchmark substrate for comparing retention, transfer and forgetting across continual-learning strategies. 〔[claim:69e9059578125358](../claims/claim-69e9059578125358.md)〕

## Current synthesis boundary

The map routes candidate evidence; it does not flatten sources into consensus or resolve contradictions automatically.

## Related pages

- [Fast Model Editing at Scale](../sources/arxiv-2110.11309.md) — `explains`
- [Avalanche: an End-to-End Library for Continual Learning](../sources/arxiv-2104.00405.md) — `explains`
- [Knowledge Editing for Large Language Models: A Survey](../sources/arxiv-2310.16218.md) — `explains`
- [Knowledge evolution loop](../concepts/knowledge-evolution-loop.md) — `related`
- [Freshness, versioning, and rollback](../concepts/freshness-versioning-rollback.md) — `related`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Avalanche: an End-to-End Library for Continual Learning (`arxiv-2104.00405`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Fast Model Editing at Scale (`arxiv-2110.11309`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Knowledge Editing for Large Language Models: A Survey (`arxiv:2310.16218`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

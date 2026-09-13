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
- claim:37a1c59affa857e1
- claim:4715a4ff3b1706fd
- claim:4e12d22ef2e755b9
- claim:69e9059578125358
source_refs: &id001
- arxiv:2405.14768
- arxiv-2104.00405
page_refs:
- wiki-page:source-1fec3cb1e7f11c84
- wiki-page:source-9923ee576cd59e46
- wiki-page:knowledge-evolution-loop
- wiki-page:freshness-versioning-and-rollback
outgoing_links:
- target: wiki-page:source-1fec3cb1e7f11c84
  relation: explains
  claim_refs:
  - claim:37a1c59affa857e1
  - claim:4e12d22ef2e755b9
  notes: null
- target: wiki-page:source-9923ee576cd59e46
  relation: explains
  claim_refs:
  - claim:4715a4ff3b1706fd
  - claim:69e9059578125358
  notes: null
- target: wiki-page:knowledge-evolution-loop
  relation: related
  claim_refs:
  - claim:37a1c59affa857e1
  - claim:4715a4ff3b1706fd
  - claim:4e12d22ef2e755b9
  - claim:69e9059578125358
  notes: null
- target: wiki-page:freshness-versioning-and-rollback
  relation: related
  claim_refs:
  - claim:37a1c59affa857e1
  - claim:4715a4ff3b1706fd
  - claim:4e12d22ef2e755b9
  - claim:69e9059578125358
  notes: null
sections:
- heading: Source coverage
  claim_refs: []
  source_refs: *id001
  editorial_intent: Route by source family.
- heading: Source-reported signals
  claim_refs:
  - claim:37a1c59affa857e1
  - claim:4715a4ff3b1706fd
  source_refs:
  - arxiv:2405.14768
  - arxiv-2104.00405
  editorial_intent: Preserve source-authored scope.
- heading: Collector assessments
  claim_refs:
  - claim:4e12d22ef2e755b9
  - claim:69e9059578125358
  source_refs:
  - arxiv:2405.14768
  - arxiv-2104.00405
  editorial_intent: Preserve collector scope.
temporal:
  created_at: '2026-09-13T17:43:07Z'
  updated_at: '2026-09-13T17:43:07Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-13T17:43:07Z'
provenance:
  build_id: build:llm-wiki-v0:196d848b07caf422
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2405.14768@sha256:60420a5c24efe0a4ea70983fb86ae62aaa3342d538d30e020d73efcf6d105ea5
  - arxiv-2104.00405@sha256:d9ca19652574908e954b524249d31a8b450830023739ee49797f58d52784dd03
  created_at: '2026-09-13T17:43:07Z'
  updated_at: '2026-09-13T17:43:07Z'
  manual_edits_preserved: true
review:
  state: needs_human
  reviewers: []
  decision_ref: null
  checked_claim_refs: []
  unresolved_issues:
  - Scientific, semantic, neutrality, and due-weight review remain required before publication.
freshness:
  status: fresh
  checked_at: '2026-09-13T17:43:07Z'
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
  estimated_tokens: 316
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
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
| [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](../sources/arxiv-2405.14768.md) | `arxiv` | `full_text` | 2 |
| [Avalanche: an End-to-End Library for Continual Learning](../sources/arxiv-2104.00405.md) | `arxiv` | `full_text` | 2 |

## Source-reported signals

- **WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models** (source assertion): Large language models (LLMs) need knowledge updates to meet the ever-growing world facts and correct the hallucinated responses, facilitating the methods of lifelong model editing. Where the updated knowledge resides in memories is a fundamental question for model editing. 〔[claim:37a1c59affa857e1](../claims/claim-37a1c59affa857e1.md)〕
- **Avalanche: an End-to-End Library for Continual Learning** (source assertion): Learning continually from non-stationary data streams is a long-standing goal and a challenging problem in machine learning. Recently, we have witnessed a renewed and fast-growing interest in continual learning, especially within the deep learning community. 〔[claim:4715a4ff3b1706fd](../claims/claim-4715a4ff3b1706fd.md)〕

## Collector assessments

- **WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models** (collection assessment): Targets continual knowledge updates and knowledge conflicts in lifelong model editing via a dual-memory and knowledge-sharding design. 〔[claim:4e12d22ef2e755b9](../claims/claim-4e12d22ef2e755b9.md)〕
- **Avalanche: an End-to-End Library for Continual Learning** (collection assessment): Provides an implementation and benchmark substrate for comparing retention, transfer and forgetting across continual-learning strategies. 〔[claim:69e9059578125358](../claims/claim-69e9059578125358.md)〕

## Current synthesis boundary

The map routes candidate evidence; it does not flatten sources into consensus or resolve contradictions automatically.

## Related pages

- [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](../sources/arxiv-2405.14768.md) — `explains`
- [Avalanche: an End-to-End Library for Continual Learning](../sources/arxiv-2104.00405.md) — `explains`
- [Knowledge evolution loop](../concepts/knowledge-evolution-loop.md) — `related`
- [Freshness, versioning, and rollback](../concepts/freshness-versioning-rollback.md) — `related`

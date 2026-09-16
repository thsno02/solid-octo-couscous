---
uid: wiki-page:evidence-771e19057a6e4a77
title: Claim 4715a4ff3b1706fd
slug: claims/claim-4715a4ff3b1706fd
page_type: evidence
status: review
summary: Learning continually from non-stationary data streams is a long-standing goal and a challenging problem
  in machine learning. Recently, we have witnessed a renewed and fast-growing interest in continual learning, especial
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:4715a4ff3b1706fd
source_refs: &id001
- arxiv-2104.00405
page_refs:
- wiki-page:source-9923ee576cd59e46
- wiki-page:map-knowledge-editing
outgoing_links:
- target: wiki-page:source-9923ee576cd59e46
  relation: evidenced_by
  claim_refs:
  - claim:4715a4ff3b1706fd
  notes: null
- target: wiki-page:map-knowledge-editing
  relation: part_of
  claim_refs:
  - claim:4715a4ff3b1706fd
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:4715a4ff3b1706fd
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:4715a4ff3b1706fd
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-13T17:38:21Z'
  updated_at: '2026-09-13T17:38:21Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-13T17:38:21Z'
provenance:
  build_id: build:llm-wiki-v0:9c2a89d879277c9e
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv-2104.00405@sha256:d9ca19652574908e954b524249d31a8b450830023739ee49797f58d52784dd03
  created_at: '2026-09-13T17:38:21Z'
  updated_at: '2026-09-13T17:38:21Z'
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
  checked_at: '2026-09-13T17:38:21Z'
  max_age_days: 30
  source_dependencies: *id001
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: Learning continually from non-stationary data streams is a long-standing goal and a challenging problem
      in machine learning. Recently, we have witnessed a renewed and fast-growing interest in continual learning,
      especial
    short: Learning continually from non-stationary data streams is a long-standing goal and a challenging problem
      in machine learning. Recently, we have witnessed a renewed and fast-growing interest in continual learning,
      especial
    full: null
  estimated_tokens: 137
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Source assertion from Avalanche: an End-to-End Library for Continual Learning

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

Learning continually from non-stationary data streams is a long-standing goal and a challenging problem in machine learning. Recently, we have witnessed a renewed and fast-growing interest in continual learning, especially within the deep learning community.

## Scope

- Claim ID: `claim:4715a4ff3b1706fd`
- Scope: `source-reported assertion`
- Domain: [knowledge-editing](../maps/knowledge-editing.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:f6e341ae267fd83f` | `local://materialized_sources/corpus/arxiv-2104.00405--93b3bffb/normalized/document.txt#L114-L114` | `materialized_sources/corpus/arxiv-2104.00405--93b3bffb/normalized/document.txt` | `full_text` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [Avalanche: an End-to-End Library for Continual Learning](../sources/arxiv-2104.00405.md) — `evidenced_by`
- [Knowledge Editing](../maps/knowledge-editing.md) — `part_of`

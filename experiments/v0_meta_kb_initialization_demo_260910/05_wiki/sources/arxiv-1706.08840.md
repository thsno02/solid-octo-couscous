---
uid: wiki-page:source-644f51e7e354fe05
title: Gradient Episodic Memory for Continual Learning
slug: sources/arxiv-1706.08840
page_type: source
status: review
summary: Source page for Gradient Episodic Memory for Continual Learning with claim/evidence expansion.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:12237a4df4847d59
- claim:633b28ce5aca37bd
source_refs: &id002
- arxiv-1706.08840
page_refs:
- wiki-page:map-knowledge-memory
- wiki-page:evidence-7bf74a1b5f4e9cda
- wiki-page:evidence-c0a3f9f9a75f6453
outgoing_links:
- target: wiki-page:map-knowledge-memory
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-7bf74a1b5f4e9cda
  relation: evidenced_by
  claim_refs:
  - claim:12237a4df4847d59
  notes: null
- target: wiki-page:evidence-c0a3f9f9a75f6453
  relation: evidenced_by
  claim_refs:
  - claim:633b28ce5aca37bd
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:12237a4df4847d59
  source_refs:
  - arxiv-1706.08840
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:633b28ce5aca37bd
  source_refs:
  - arxiv-1706.08840
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:ac56ea43f6b5393c
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv-1706.08840@sha256:330858b30f0963297c9d772fc29aabc8dfcff7d687856d91a2f167847d0fca88
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
  source_dependencies: *id002
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: Source page for Gradient Episodic Memory for Continual Learning with claim/evidence expansion.
    short: Source page for Gradient Episodic Memory for Continual Learning with claim/evidence expansion.
    full: null
  estimated_tokens: 281
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:12237a4df4847d59
- claim:633b28ce5aca37bd
rights_refs: []
rights_unavailable_source_refs:
- arxiv-1706.08840
---

# Gradient Episodic Memory for Continual Learning

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv-1706.08840`
- Canonical ID: `1706.08840`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:330858b30f0963297c9d772fc29aabc8dfcff7d687856d91a2f167847d0fca88`
- Domain: [knowledge-memory](../maps/knowledge-memory.md)
- Local document: `materialized_sources/corpus/arxiv-1706.08840--acb7e7ed/normalized/document.txt`

## Source-reported candidate statements

- One major obstacle towards AI is the poor ability of models to solve new problems quicker, and without forgetting previously acquired knowledge. To better understand this issue, we study the problem of continual learning, where the model observes, once and one by one, examples concerning a sequence of tasks. 〔[claim:12237a4df4847d59](../claims/claim-12237a4df4847d59.md)〕

## Collection assessments

- Connects memory retention to constrained updates and positive backward transfer, directly informing governed knowledge updates. 〔[claim:633b28ce5aca37bd](../claims/claim-633b28ce5aca37bd.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:12237a4df4847d59` | `evidence:cd3d871f39cb6ece` | `local://materialized_sources/corpus/arxiv-1706.08840--acb7e7ed/normalized/document.txt#L45-L49` | `full_text` |
| `claim:633b28ce5aca37bd` | `evidence:68121f105d3012a3` | `local://raw_data/arxiv/Gradient Episodic Memory for Continual Learning/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Knowledge Memory](../maps/knowledge-memory.md) — `part_of`
- [Claim 12237a4df4847d59](../claims/claim-12237a4df4847d59.md) — `evidenced_by`
- [Claim 633b28ce5aca37bd](../claims/claim-633b28ce5aca37bd.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Gradient Episodic Memory for Continual Learning (`arxiv-1706.08840`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

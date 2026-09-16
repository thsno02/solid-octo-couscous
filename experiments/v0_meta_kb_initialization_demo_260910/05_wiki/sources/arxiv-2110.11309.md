---
uid: wiki-page:source-c707950005ce916a
title: Fast Model Editing at Scale
slug: sources/arxiv-2110.11309
page_type: source
status: review
summary: Source page for Fast Model Editing at Scale with claim/evidence expansion.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:40178c8dde6cbf34
- claim:ad198ecf5d0cad6b
source_refs: &id002
- arxiv-2110.11309
page_refs:
- wiki-page:map-knowledge-editing
- wiki-page:evidence-2b2c67dbc05789e0
- wiki-page:evidence-d389535df5553705
outgoing_links:
- target: wiki-page:map-knowledge-editing
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-2b2c67dbc05789e0
  relation: evidenced_by
  claim_refs:
  - claim:40178c8dde6cbf34
  notes: null
- target: wiki-page:evidence-d389535df5553705
  relation: evidenced_by
  claim_refs:
  - claim:ad198ecf5d0cad6b
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:ad198ecf5d0cad6b
  source_refs:
  - arxiv-2110.11309
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:40178c8dde6cbf34
  source_refs:
  - arxiv-2110.11309
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:b04c61704bd4b7be
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv-2110.11309@sha256:e838a729a34c09a9044b334ef91e3c1ea36030b9e9e35ba6d6f11747e2b4b570
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
    one_line: Source page for Fast Model Editing at Scale with claim/evidence expansion.
    short: Source page for Fast Model Editing at Scale with claim/evidence expansion.
    full: null
  estimated_tokens: 290
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:40178c8dde6cbf34
- claim:ad198ecf5d0cad6b
rights_refs: []
rights_unavailable_source_refs:
- arxiv-2110.11309
---

# Fast Model Editing at Scale

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv-2110.11309`
- Canonical ID: `2110.11309`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:e838a729a34c09a9044b334ef91e3c1ea36030b9e9e35ba6d6f11747e2b4b570`
- Domain: [knowledge-editing](../maps/knowledge-editing.md)
- Local document: `materialized_sources/corpus/arxiv-2110.11309--d5da3395/normalized/document.txt`

## Source-reported candidate statements

- While large pre-trained models have enabled impressive results on a variety of downstream tasks, the largest existing models still make errors, and even accurate predictions may become outdated over time. Because detecting all such failures at training time is impossible, enabling both developers and end users of such models to correct inaccurate outputs while leaving the model otherwise intact is desirable. 〔[claim:ad198ecf5d0cad6b](../claims/claim-ad198ecf5d0cad6b.md)〕

## Collection assessments

- MEND makes the update mechanism itself learnable and exposes generalization/locality requirements for governed knowledge editing. 〔[claim:40178c8dde6cbf34](../claims/claim-40178c8dde6cbf34.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:40178c8dde6cbf34` | `evidence:402b8b7c9c3c6921` | `local://raw_data/arxiv/Fast Model Editing at Scale/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:ad198ecf5d0cad6b` | `evidence:5a459f5951ba3ff8` | `local://materialized_sources/corpus/arxiv-2110.11309--d5da3395/normalized/document.txt#L154-L154` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Knowledge Editing](../maps/knowledge-editing.md) — `part_of`
- [Claim 40178c8dde6cbf34](../claims/claim-40178c8dde6cbf34.md) — `evidenced_by`
- [Claim ad198ecf5d0cad6b](../claims/claim-ad198ecf5d0cad6b.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Fast Model Editing at Scale (`arxiv-2110.11309`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

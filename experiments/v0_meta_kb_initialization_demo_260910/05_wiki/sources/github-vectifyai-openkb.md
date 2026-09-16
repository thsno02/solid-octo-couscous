---
uid: wiki-page:source-332922100755365f
title: VectifyAI/OpenKB
slug: sources/github-vectifyai-openkb
page_type: source
status: review
summary: Source page for VectifyAI/OpenKB with claim/evidence expansion.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:714e301e8b2162bc
- claim:e7026275c099e7e2
source_refs: &id002
- github:VectifyAI/OpenKB
page_refs:
- wiki-page:map-llm-wiki
- wiki-page:evidence-ae02e6dd19d86e7a
- wiki-page:evidence-2c4497b2c6a0f960
outgoing_links:
- target: wiki-page:map-llm-wiki
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-ae02e6dd19d86e7a
  relation: evidenced_by
  claim_refs:
  - claim:714e301e8b2162bc
  notes: null
- target: wiki-page:evidence-2c4497b2c6a0f960
  relation: evidenced_by
  claim_refs:
  - claim:e7026275c099e7e2
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:e7026275c099e7e2
  source_refs:
  - github:VectifyAI/OpenKB
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:714e301e8b2162bc
  source_refs:
  - github:VectifyAI/OpenKB
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:8d5202830938fe6b
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - github:VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc
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
    one_line: Source page for VectifyAI/OpenKB with claim/evidence expansion.
    short: Source page for VectifyAI/OpenKB with claim/evidence expansion.
    full: null
  estimated_tokens: 253
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:714e301e8b2162bc
- claim:e7026275c099e7e2
rights_refs: []
rights_unavailable_source_refs:
- github:VectifyAI/OpenKB
---

# VectifyAI/OpenKB

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `github:VectifyAI/OpenKB`
- Canonical ID: `VectifyAI/OpenKB`
- Source type: `github`
- Content tier: `semantic_capsule`
- Revision: `ff54396e575ee6feb0113b631a34caa082b441cc`
- Domain: [llm-wiki](../maps/llm-wiki.md)
- Local document: `materialized_sources/corpus/github-VectifyAI-OpenKB--fd455ce8/evidence/files/README.md`

## Source-reported candidate statements

- **OpenKB (Open Knowledge Base)** is an open-source system (in CLI) that compiles raw documents into a structured, interlinked wiki-style knowledge base using LLMs, powered by [**PageIndex**](https://github.com/VectifyAI/PageIndex)'s vectorless, reasoning-based retrieval for long documents. 〔[claim:e7026275c099e7e2](../claims/claim-e7026275c099e7e2.md)〕

## Collection assessments

- A CLI knowledge compiler with wiki foundation and downstream generators, hierarchical long-document retrieval, linting, source removal and skill compilation. 〔[claim:714e301e8b2162bc](../claims/claim-714e301e8b2162bc.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:714e301e8b2162bc` | `evidence:4458920402fcefd8` | `local://raw_data/githubs/VectifyAI--OpenKB/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:e7026275c099e7e2` | `evidence:314e31b69b572671` | `local://materialized_sources/corpus/github-VectifyAI-OpenKB--fd455ce8/evidence/files/README.md#L32-L32` | `semantic_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Llm Wiki](../maps/llm-wiki.md) — `part_of`
- [Claim 714e301e8b2162bc](../claims/claim-714e301e8b2162bc.md) — `evidenced_by`
- [Claim e7026275c099e7e2](../claims/claim-e7026275c099e7e2.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### VectifyAI/OpenKB (`github:VectifyAI/OpenKB`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

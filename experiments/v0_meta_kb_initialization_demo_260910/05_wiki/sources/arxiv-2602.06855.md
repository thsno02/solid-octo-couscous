---
uid: wiki-page:source-a264f295a5ce5604
title: 'AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents'
slug: sources/arxiv-2602.06855
page_type: source
status: review
summary: 'Source page for AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents with claim/evidence
  expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:17c715b34b0f0c68
- claim:ecdd2719fa55751c
source_refs: &id002
- arxiv:2602.06855
page_refs:
- wiki-page:map-governance-evaluation
- wiki-page:evidence-9b995513dc540102
- wiki-page:evidence-36c1729b09de22fd
outgoing_links:
- target: wiki-page:map-governance-evaluation
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-9b995513dc540102
  relation: evidenced_by
  claim_refs:
  - claim:17c715b34b0f0c68
  notes: null
- target: wiki-page:evidence-36c1729b09de22fd
  relation: evidenced_by
  claim_refs:
  - claim:ecdd2719fa55751c
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:ecdd2719fa55751c
  source_refs:
  - arxiv:2602.06855
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:17c715b34b0f0c68
  source_refs:
  - arxiv:2602.06855
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:7709fc4901bbe1d3
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2602.06855@sha256:ac1ba940f1bdc54e012cc384c428f78bd01d50d7a947f052117944c03e790d9a
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
    one_line: 'Source page for AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents with claim/evidence
      expansion.'
    short: 'Source page for AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents with claim/evidence
      expansion.'
    full: null
  estimated_tokens: 192
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2602.06855`
- Canonical ID: `2602.06855`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:ac1ba940f1bdc54e012cc384c428f78bd01d50d7a947f052117944c03e790d9a`
- Domain: [governance-evaluation](../maps/governance-evaluation.md)
- Local document: `materialized_sources/corpus/arxiv-2602.06855--0b517136/normalized/document.txt`

## Source-reported candidate statements

- LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we introduce ~(the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine learning papers. 〔[claim:ecdd2719fa55751c](../claims/claim-ecdd2719fa55751c.md)〕

## Collection assessments

- A 2026 benchmark explicitly targeting frontier AI research-science agents across the research lifecycle, including idea generation, experimentation, analysis and iterative refinement. 〔[claim:17c715b34b0f0c68](../claims/claim-17c715b34b0f0c68.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:17c715b34b0f0c68` | `evidence:9211528f477bfb59` | `local://raw_data/arxiv/AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:ecdd2719fa55751c` | `evidence:3c0c7c9546c2ec15` | `local://materialized_sources/corpus/arxiv-2602.06855--0b517136/normalized/document.txt#L621-L622` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Governance Evaluation](../maps/governance-evaluation.md) — `part_of`
- [Claim 17c715b34b0f0c68](../claims/claim-17c715b34b0f0c68.md) — `evidenced_by`
- [Claim ecdd2719fa55751c](../claims/claim-ecdd2719fa55751c.md) — `evidenced_by`

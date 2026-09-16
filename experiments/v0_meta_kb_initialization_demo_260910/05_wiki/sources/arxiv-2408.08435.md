---
uid: wiki-page:source-c9890d5668d1c1b3
title: Automated Design of Agentic Systems
slug: sources/arxiv-2408.08435
page_type: source
status: review
summary: Source page for Automated Design of Agentic Systems with claim/evidence expansion.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:00e6310ce97dc279
- claim:0d2b54965305cf83
source_refs: &id002
- arxiv:2408.08435
page_refs:
- wiki-page:map-cross-cutting
- wiki-page:evidence-1726c87cfdd2429b
- wiki-page:evidence-cff7f8af0fb78c76
outgoing_links:
- target: wiki-page:map-cross-cutting
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-1726c87cfdd2429b
  relation: evidenced_by
  claim_refs:
  - claim:00e6310ce97dc279
  notes: null
- target: wiki-page:evidence-cff7f8af0fb78c76
  relation: evidenced_by
  claim_refs:
  - claim:0d2b54965305cf83
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:0d2b54965305cf83
  source_refs:
  - arxiv:2408.08435
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:00e6310ce97dc279
  source_refs:
  - arxiv:2408.08435
  editorial_intent: Keep collector interpretation separate.
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
  - arxiv:2408.08435@sha256:9e5b2a49f62b2d5218e018666a195c85fc5d186d3939e0070303fab4fb7622e2
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
  source_dependencies: *id002
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: Source page for Automated Design of Agentic Systems with claim/evidence expansion.
    short: Source page for Automated Design of Agentic Systems with claim/evidence expansion.
    full: null
  estimated_tokens: 178
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Automated Design of Agentic Systems

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2408.08435`
- Canonical ID: `2408.08435`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:9e5b2a49f62b2d5218e018666a195c85fc5d186d3939e0070303fab4fb7622e2`
- Domain: [cross-cutting](../maps/cross-cutting.md)
- Local document: `materialized_sources/corpus/arxiv-2408.08435--dc6e6730/normalized/document.txt`

## Source-reported candidate statements

- Researchers are investing substantial effort in developing powerful general-purpose agents, wherein Foundation Models are used as modules within agentic systems (e.g. Chain-of-Thought, Self-Reflection, Toolformer). 〔[claim:0d2b54965305cf83](../claims/claim-0d2b54965305cf83.md)〕

## Collection assessments

- Defines Automated Design of Agentic Systems (ADAS): agents are represented in code and a meta-agent iteratively programs better agents using an ever-growing archive of prior discoveries. 〔[claim:00e6310ce97dc279](../claims/claim-00e6310ce97dc279.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:00e6310ce97dc279` | `evidence:4c23103dc864786c` | `local://raw_data/arxiv/Automated Design of Agentic Systems/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:0d2b54965305cf83` | `evidence:33d6742cf3d38320` | `local://materialized_sources/corpus/arxiv-2408.08435--dc6e6730/normalized/document.txt#L115-L115` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Cross Cutting](../maps/cross-cutting.md) — `part_of`
- [Claim 00e6310ce97dc279](../claims/claim-00e6310ce97dc279.md) — `evidenced_by`
- [Claim 0d2b54965305cf83](../claims/claim-0d2b54965305cf83.md) — `evidenced_by`

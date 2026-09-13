---
uid: wiki-page:source-21b7474d41eb2395
title: 'ChemCrow: Augmenting large-language models with chemistry tools'
slug: sources/arxiv-2304.05376
page_type: source
status: review
summary: 'Source page for ChemCrow: Augmenting large-language models with chemistry tools with claim/evidence expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:1b726943a743060e
- claim:bc939bb7895ea88e
source_refs: &id002
- arxiv:2304.05376
page_refs:
- wiki-page:map-cross-cutting
- wiki-page:evidence-98fb1d267c541855
- wiki-page:evidence-757b75160b0b981b
outgoing_links:
- target: wiki-page:map-cross-cutting
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-98fb1d267c541855
  relation: evidenced_by
  claim_refs:
  - claim:1b726943a743060e
  notes: null
- target: wiki-page:evidence-757b75160b0b981b
  relation: evidenced_by
  claim_refs:
  - claim:bc939bb7895ea88e
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:bc939bb7895ea88e
  source_refs:
  - arxiv:2304.05376
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:1b726943a743060e
  source_refs:
  - arxiv:2304.05376
  editorial_intent: Keep collector interpretation separate.
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
  - arxiv:2304.05376@sha256:21c607b0c71631e362d318e2424cac73dacb38fd528e463f02a9f030bef5ed23
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
  source_dependencies: *id002
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: 'Source page for ChemCrow: Augmenting large-language models with chemistry tools with claim/evidence
      expansion.'
    short: 'Source page for ChemCrow: Augmenting large-language models with chemistry tools with claim/evidence
      expansion.'
    full: null
  estimated_tokens: 187
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# ChemCrow: Augmenting large-language models with chemistry tools

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2304.05376`
- Canonical ID: `2304.05376`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:21c607b0c71631e362d318e2424cac73dacb38fd528e463f02a9f030bef5ed23`
- Domain: [cross-cutting](../maps/cross-cutting.md)
- Local document: `materialized_sources/corpus/arxiv-2304.05376--4e0dcba3/normalized/document.txt`

## Source-reported candidate statements

- Over the last decades, excellent computational chemistry tools have been developed. Integrating them into a single platform with enhanced accessibility could help reaching their full potential by overcoming steep learning curves. 〔[claim:bc939bb7895ea88e](../claims/claim-bc939bb7895ea88e.md)〕

## Collection assessments

- An early landmark showing that a language-model agent connected to domain tools can plan and execute meaningful chemistry tasks, including synthesis and discovery-oriented workflows. 〔[claim:1b726943a743060e](../claims/claim-1b726943a743060e.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:1b726943a743060e` | `evidence:5a9be35676aa8b55` | `local://raw_data/arxiv/ChemCrow: Augmenting large-language models with chemistry tools/metadata.yaml#collection-inclusion-reason` | `metadata_capsule` |
| `claim:bc939bb7895ea88e` | `evidence:314ba5c563516e11` | `local://materialized_sources/corpus/arxiv-2304.05376--4e0dcba3/normalized/document.txt#L93-L93` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Cross Cutting](../maps/cross-cutting.md) — `part_of`
- [Claim 1b726943a743060e](../claims/claim-1b726943a743060e.md) — `evidenced_by`
- [Claim bc939bb7895ea88e](../claims/claim-bc939bb7895ea88e.md) — `evidenced_by`

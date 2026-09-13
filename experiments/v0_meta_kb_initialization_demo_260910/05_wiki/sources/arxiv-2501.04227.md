---
uid: wiki-page:source-5c69a674d903b543
title: 'Agent Laboratory: Using LLM Agents as Research Assistants'
slug: sources/arxiv-2501.04227
page_type: source
status: review
summary: 'Source page for Agent Laboratory: Using LLM Agents as Research Assistants with claim/evidence expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:2f8ebd974fc7b5fd
- claim:3d07597b1776b0bd
source_refs: &id002
- arxiv:2501.04227
page_refs:
- wiki-page:map-automated-research
- wiki-page:evidence-42304939383189ab
- wiki-page:evidence-37d06da8881dd925
outgoing_links:
- target: wiki-page:map-automated-research
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-42304939383189ab
  relation: evidenced_by
  claim_refs:
  - claim:2f8ebd974fc7b5fd
  notes: null
- target: wiki-page:evidence-37d06da8881dd925
  relation: evidenced_by
  claim_refs:
  - claim:3d07597b1776b0bd
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:2f8ebd974fc7b5fd
  source_refs:
  - arxiv:2501.04227
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:3d07597b1776b0bd
  source_refs:
  - arxiv:2501.04227
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
  - arxiv:2501.04227@sha256:1b28bfd8ca8a9dcb1930f7fcd49164300a984bd1abf533d3d28b475fe7dd7f85
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
    one_line: 'Source page for Agent Laboratory: Using LLM Agents as Research Assistants with claim/evidence expansion.'
    short: 'Source page for Agent Laboratory: Using LLM Agents as Research Assistants with claim/evidence expansion.'
    full: null
  estimated_tokens: 200
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Agent Laboratory: Using LLM Agents as Research Assistants

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2501.04227`
- Canonical ID: `2501.04227`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:1b28bfd8ca8a9dcb1930f7fcd49164300a984bd1abf533d3d28b475fe7dd7f85`
- Domain: [automated-research](../maps/automated-research.md)
- Local document: `materialized_sources/corpus/arxiv-2501.04227--a0515b2c/normalized/document.txt`

## Source-reported candidate statements

- Historically, scientific discovery has been a lengthy and costly process, demanding substantial time and resources from initial conception to final results. To accelerate scientific discovery, reduce research costs, and improve research quality, we introduce Agent Laboratory , an autonomous LLM-based framework capable of completing the entire research process. 〔[claim:2f8ebd974fc7b5fd](../claims/claim-2f8ebd974fc7b5fd.md)〕

## Collection assessments

- A practical end-to-end autonomous research workflow spanning literature review, experimentation and report writing, with explicit human feedback points. 〔[claim:3d07597b1776b0bd](../claims/claim-3d07597b1776b0bd.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:2f8ebd974fc7b5fd` | `evidence:b085c8ded21a947a` | `local://materialized_sources/corpus/arxiv-2501.04227--a0515b2c/normalized/document.txt#L133-L155` | `full_text` |
| `claim:3d07597b1776b0bd` | `evidence:64bae7b35d03441f` | `local://raw_data/arxiv/Agent Laboratory: Using LLM Agents as Research Assistants/metadata.yaml#collection-inclusion-reason` | `metadata_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Automated Research](../maps/automated-research.md) — `part_of`
- [Claim 2f8ebd974fc7b5fd](../claims/claim-2f8ebd974fc7b5fd.md) — `evidenced_by`
- [Claim 3d07597b1776b0bd](../claims/claim-3d07597b1776b0bd.md) — `evidenced_by`

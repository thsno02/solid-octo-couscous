---
uid: wiki-page:source-1aacba116cbe3c5b
title: 'A-MEM: Agentic Memory for LLM Agents'
slug: sources/arxiv-2502.12110
page_type: source
status: review
summary: 'Source page for A-MEM: Agentic Memory for LLM Agents with claim/evidence expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:ecf45fd3f4ab576a
- claim:f8088669f62de120
source_refs: &id002
- arxiv:2502.12110
page_refs:
- wiki-page:map-open-ended-evolution
- wiki-page:evidence-bc3556337b5ca353
- wiki-page:evidence-84a7e3d93aee36a7
outgoing_links:
- target: wiki-page:map-open-ended-evolution
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-bc3556337b5ca353
  relation: evidenced_by
  claim_refs:
  - claim:ecf45fd3f4ab576a
  notes: null
- target: wiki-page:evidence-84a7e3d93aee36a7
  relation: evidenced_by
  claim_refs:
  - claim:f8088669f62de120
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:ecf45fd3f4ab576a
  source_refs:
  - arxiv:2502.12110
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:f8088669f62de120
  source_refs:
  - arxiv:2502.12110
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
  - arxiv:2502.12110@sha256:d112e92606a562a0369e2e8cddadad88ac8d448d66c24ee9b63e808c2c84e42b
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
    one_line: 'Source page for A-MEM: Agentic Memory for LLM Agents with claim/evidence expansion.'
    short: 'Source page for A-MEM: Agentic Memory for LLM Agents with claim/evidence expansion.'
    full: null
  estimated_tokens: 195
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# A-MEM: Agentic Memory for LLM Agents

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2502.12110`
- Canonical ID: `2502.12110`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:d112e92606a562a0369e2e8cddadad88ac8d448d66c24ee9b63e808c2c84e42b`
- Domain: [open-ended-evolution](../maps/open-ended-evolution.md)
- Local document: `materialized_sources/corpus/arxiv-2502.12110--d27d79d8/normalized/document.txt`

## Source-reported candidate statements

- While large language model (LLM) agents can effectively use external tools for complex real-world tasks, they require memory systems to leverage historical experiences. Current memory systems enable basic storage and retrieval but lack sophisticated memory organization, despite recent attempts to incorporate graph databases. 〔[claim:ecf45fd3f4ab576a](../claims/claim-ecf45fd3f4ab576a.md)〕

## Collection assessments

- Directly studies memory evolution: newly added memories can update contextual representations and attributes of historical memories, continuously refining the memory network. 〔[claim:f8088669f62de120](../claims/claim-f8088669f62de120.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:ecf45fd3f4ab576a` | `evidence:23f9dcda024ab01e` | `local://materialized_sources/corpus/arxiv-2502.12110--d27d79d8/normalized/document.txt#L194-L194` | `full_text` |
| `claim:f8088669f62de120` | `evidence:f5dc2b44e50824e7` | `local://raw_data/arxiv/A-MEM: Agentic Memory for LLM Agents/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Open Ended Evolution](../maps/open-ended-evolution.md) — `part_of`
- [Claim ecf45fd3f4ab576a](../claims/claim-ecf45fd3f4ab576a.md) — `evidenced_by`
- [Claim f8088669f62de120](../claims/claim-f8088669f62de120.md) — `evidenced_by`

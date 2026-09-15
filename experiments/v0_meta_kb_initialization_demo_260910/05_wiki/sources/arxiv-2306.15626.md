---
uid: wiki-page:source-5be112b896547169
title: 'LeanDojo: Theorem Proving with Retrieval-Augmented Language Models'
slug: sources/arxiv-2306.15626
page_type: source
status: review
summary: 'Source page for LeanDojo: Theorem Proving with Retrieval-Augmented Language Models with claim/evidence
  expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:a67432ee7afb1535
- claim:d13d2fd07c92af58
source_refs: &id002
- arxiv-2306.15626
page_refs:
- wiki-page:map-knowledge-memory
- wiki-page:evidence-ed313fbe55c04de9
- wiki-page:evidence-1eaf8c8649fe972d
outgoing_links:
- target: wiki-page:map-knowledge-memory
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-ed313fbe55c04de9
  relation: evidenced_by
  claim_refs:
  - claim:a67432ee7afb1535
  notes: null
- target: wiki-page:evidence-1eaf8c8649fe972d
  relation: evidenced_by
  claim_refs:
  - claim:d13d2fd07c92af58
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:a67432ee7afb1535
  source_refs:
  - arxiv-2306.15626
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:d13d2fd07c92af58
  source_refs:
  - arxiv-2306.15626
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-13T17:38:21Z'
  updated_at: '2026-09-13T17:38:21Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-13T17:38:21Z'
provenance:
  build_id: build:llm-wiki-v0:d303e0f210b88f64
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv-2306.15626@sha256:5893d0b64b077ec01bee907ead6d94ae8c810abf023c2b4f618250c4fb0b7680
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
    one_line: 'Source page for LeanDojo: Theorem Proving with Retrieval-Augmented Language Models with claim/evidence
      expansion.'
    short: 'Source page for LeanDojo: Theorem Proving with Retrieval-Augmented Language Models with claim/evidence
      expansion.'
    full: null
  estimated_tokens: 182
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# LeanDojo: Theorem Proving with Retrieval-Augmented Language Models

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv-2306.15626`
- Canonical ID: `2306.15626`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:5893d0b64b077ec01bee907ead6d94ae8c810abf023c2b4f618250c4fb0b7680`
- Domain: [knowledge-memory](../maps/knowledge-memory.md)
- Local document: `materialized_sources/corpus/arxiv-2306.15626--438dfbd9/normalized/document.txt`

## Source-reported candidate statements

- Large language models (LLMs) have shown promise in proving formal theorems using proof assistants such as Lean. However, existing methods are difficult to reproduce or build on, due to private code, data, and large compute requirements. 〔[claim:a67432ee7afb1535](../claims/claim-a67432ee7afb1535.md)〕

## Collection assessments

- Introduces machine-verifiable research output and retrieval over formal libraries, balancing less-verifiable natural-language research agents. 〔[claim:d13d2fd07c92af58](../claims/claim-d13d2fd07c92af58.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:a67432ee7afb1535` | `evidence:7638a9216c6f2bd1` | `local://materialized_sources/corpus/arxiv-2306.15626--438dfbd9/normalized/document.txt#L118-L118` | `full_text` |
| `claim:d13d2fd07c92af58` | `evidence:296659ae73b7c9bd` | `local://raw_data/arxiv/LeanDojo Theorem Proving with Retrieval-Augmented Language Models/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Knowledge Memory](../maps/knowledge-memory.md) — `part_of`
- [Claim a67432ee7afb1535](../claims/claim-a67432ee7afb1535.md) — `evidenced_by`
- [Claim d13d2fd07c92af58](../claims/claim-d13d2fd07c92af58.md) — `evidenced_by`

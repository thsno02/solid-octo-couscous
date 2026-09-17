---
uid: wiki-page:source-7fabb86557bf2f15
title: Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models
slug: sources/arxiv-2402.14207
page_type: source
status: review
summary: Source page for Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models with
  claim/evidence expansion.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:1929edca74fa3fa5
- claim:55eeb2a1683b8804
source_refs: &id002
- arxiv:2402.14207
page_refs:
- wiki-page:map-llm-wiki
- wiki-page:evidence-e9b49fbec0e6beb9
- wiki-page:evidence-2fadc87cfe75941e
outgoing_links:
- target: wiki-page:map-llm-wiki
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-e9b49fbec0e6beb9
  relation: evidenced_by
  claim_refs:
  - claim:1929edca74fa3fa5
  notes: null
- target: wiki-page:evidence-2fadc87cfe75941e
  relation: evidenced_by
  claim_refs:
  - claim:55eeb2a1683b8804
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:1929edca74fa3fa5
  source_refs:
  - arxiv:2402.14207
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:55eeb2a1683b8804
  source_refs:
  - arxiv:2402.14207
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:45bd6c7288326476
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2402.14207@sha256:28b57e9821da798bf8ccfa3f144bfa37cd96ff3582c2211c83eff5ffcf0ccfc2
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
    one_line: Source page for Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models
      with claim/evidence expansion.
    short: Source page for Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models
      with claim/evidence expansion.
    full: null
  estimated_tokens: 297
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:1929edca74fa3fa5
- claim:55eeb2a1683b8804
rights_refs: []
rights_unavailable_source_refs:
- arxiv:2402.14207
---

# Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2402.14207`
- Canonical ID: `2402.14207`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:28b57e9821da798bf8ccfa3f144bfa37cd96ff3582c2211c83eff5ffcf0ccfc2`
- Domain: [llm-wiki](../maps/llm-wiki.md)
- Local document: `materialized_sources/corpus/arxiv-2402.14207--b99559f4/normalized/document.txt`

## Source-reported candidate statements

- We study how to apply large language models to write grounded and organized long-form articles from scratch, with comparable breadth and depth to Wikipedia pages. This underexplored problem poses new challenges at the pre-writing stage, including how to research the topic and prepare an outline prior to writing. 〔[claim:1929edca74fa3fa5](../claims/claim-1929edca74fa3fa5.md)〕

## Collection assessments

- STORM is a central academic reference for multi-perspective research, outline construction, grounded long-form synthesis, and editor-informed evaluation. 〔[claim:55eeb2a1683b8804](../claims/claim-55eeb2a1683b8804.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:1929edca74fa3fa5` | `evidence:1fe97aa395c695a6` | `local://materialized_sources/corpus/arxiv-2402.14207--b99559f4/normalized/document.txt#L130-L130` | `full_text` |
| `claim:55eeb2a1683b8804` | `evidence:5487a4c755f116c0` | `local://raw_data/arxiv/Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Llm Wiki](../maps/llm-wiki.md) — `part_of`
- [Claim 1929edca74fa3fa5](../claims/claim-1929edca74fa3fa5.md) — `evidenced_by`
- [Claim 55eeb2a1683b8804](../claims/claim-55eeb2a1683b8804.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models (`arxiv:2402.14207`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

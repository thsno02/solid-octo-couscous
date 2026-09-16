---
uid: wiki-page:source-e27d5b13b062021d
title: Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models
slug: sources/arxiv-2509.23233
page_type: source
status: review
summary: Source page for Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models
  with claim/evidence expansion.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:6f5fa83ca484f664
- claim:bc9a34bd8a9c7154
source_refs: &id002
- arxiv:2509.23233
page_refs:
- wiki-page:map-llm-wiki
- wiki-page:evidence-0bf31b772cff5e19
- wiki-page:evidence-b13de68a35a53565
outgoing_links:
- target: wiki-page:map-llm-wiki
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-0bf31b772cff5e19
  relation: evidenced_by
  claim_refs:
  - claim:6f5fa83ca484f664
  notes: null
- target: wiki-page:evidence-b13de68a35a53565
  relation: evidenced_by
  claim_refs:
  - claim:bc9a34bd8a9c7154
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:bc9a34bd8a9c7154
  source_refs:
  - arxiv:2509.23233
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:6f5fa83ca484f664
  source_refs:
  - arxiv:2509.23233
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:f3fea76ebc259510
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2509.23233@sha256:8570de4224cfc829f7478411feca2ecec5f50d6e7ceb7cc62fd15fa07f20c921
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
    one_line: Source page for Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language
      Models with claim/evidence expansion.
    short: Source page for Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models
      with claim/evidence expansion.
    full: null
  estimated_tokens: 282
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:6f5fa83ca484f664
- claim:bc9a34bd8a9c7154
rights_refs: []
rights_unavailable_source_refs:
- arxiv:2509.23233
---

# Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2509.23233`
- Canonical ID: `2509.23233`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:8570de4224cfc829f7478411feca2ecec5f50d6e7ceb7cc62fd15fa07f20c921`
- Domain: [llm-wiki](../maps/llm-wiki.md)
- Local document: `materialized_sources/corpus/arxiv-2509.23233--b148460b/normalized/document.txt`

## Source-reported candidate statements

- Wikipedia is the largest open knowledge corpus, widely used worldwide and serving as a key resource for training large language models (LLMs) and retrieval-augmented generation (RAG) systems. Ensuring its accuracy is therefore critical. 〔[claim:bc9a34bd8a9c7154](../claims/claim-bc9a34bd8a9c7154.md)〕

## Collection assessments

- CLAIRE and WikiCollide make corpus-level inconsistency detection a first-class maintenance task and demonstrate human-editor review as part of the loop. 〔[claim:6f5fa83ca484f664](../claims/claim-6f5fa83ca484f664.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:6f5fa83ca484f664` | `evidence:e30f4eb524d5ee06` | `local://raw_data/arxiv/Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:bc9a34bd8a9c7154` | `evidence:6da0b30814cd3e6e` | `local://materialized_sources/corpus/arxiv-2509.23233--b148460b/normalized/document.txt#L128-L128` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Llm Wiki](../maps/llm-wiki.md) — `part_of`
- [Claim 6f5fa83ca484f664](../claims/claim-6f5fa83ca484f664.md) — `evidenced_by`
- [Claim bc9a34bd8a9c7154](../claims/claim-bc9a34bd8a9c7154.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models (`arxiv:2509.23233`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

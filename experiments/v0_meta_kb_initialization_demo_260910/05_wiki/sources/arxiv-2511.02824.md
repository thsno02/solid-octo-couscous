---
uid: wiki-page:source-51ed59b1fc0ecd08
title: 'Kosmos: An AI Scientist for Autonomous Discovery'
slug: sources/arxiv-2511.02824
page_type: source
status: review
summary: 'Source page for Kosmos: An AI Scientist for Autonomous Discovery with claim/evidence expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:0edb741be0f31f6f
- claim:3e6ec7f46b13c44f
source_refs: &id002
- arxiv:2511.02824
page_refs:
- wiki-page:map-ontology-semantic-architecture
- wiki-page:evidence-a7da1a63a4c9d723
- wiki-page:evidence-51f99c8c1993ed75
outgoing_links:
- target: wiki-page:map-ontology-semantic-architecture
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-a7da1a63a4c9d723
  relation: evidenced_by
  claim_refs:
  - claim:0edb741be0f31f6f
  notes: null
- target: wiki-page:evidence-51f99c8c1993ed75
  relation: evidenced_by
  claim_refs:
  - claim:3e6ec7f46b13c44f
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:0edb741be0f31f6f
  source_refs:
  - arxiv:2511.02824
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:3e6ec7f46b13c44f
  source_refs:
  - arxiv:2511.02824
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:0f0b56605b4756b3
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2511.02824@sha256:6c71312f8e88b313baf4eeb44a39fefa9f09ad5bd247e176e49824310cf5fb5e
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
    one_line: 'Source page for Kosmos: An AI Scientist for Autonomous Discovery with claim/evidence expansion.'
    short: 'Source page for Kosmos: An AI Scientist for Autonomous Discovery with claim/evidence expansion.'
    full: null
  estimated_tokens: 209
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Kosmos: An AI Scientist for Autonomous Discovery

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2511.02824`
- Canonical ID: `2511.02824`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:6c71312f8e88b313baf4eeb44a39fefa9f09ad5bd247e176e49824310cf5fb5e`
- Domain: [ontology-semantic-architecture](../maps/ontology-semantic-architecture.md)
- Local document: `materialized_sources/corpus/arxiv-2511.02824--1c218a8e/normalized/document.txt`

## Source-reported candidate statements

- Data-driven scientific discovery requires iterative cycles of literature search, hypothesis generation, and data analysis. Substantial progress has been made towards AI agents that can automate scientific research, but all such agents remain limited in the number of actions they can take before losing coherence, thus limiting the depth of their findings. 〔[claim:0edb741be0f31f6f](../claims/claim-0edb741be0f31f6f.md)〕

## Collection assessments

- Long-horizon autonomous data-driven discovery. Kosmos repeatedly interleaves literature search, data analysis and hypothesis generation while maintaining a structured world model across hundreds of agent rollouts. 〔[claim:3e6ec7f46b13c44f](../claims/claim-3e6ec7f46b13c44f.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:0edb741be0f31f6f` | `evidence:a685b3f37385c089` | `local://materialized_sources/corpus/arxiv-2511.02824--1c218a8e/normalized/document.txt#L78-L78` | `full_text` |
| `claim:3e6ec7f46b13c44f` | `evidence:a566d8629070c224` | `local://raw_data/arxiv/Kosmos: An AI Scientist for Autonomous Discovery/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Ontology Semantic Architecture](../maps/ontology-semantic-architecture.md) — `part_of`
- [Claim 0edb741be0f31f6f](../claims/claim-0edb741be0f31f6f.md) — `evidenced_by`
- [Claim 3e6ec7f46b13c44f](../claims/claim-3e6ec7f46b13c44f.md) — `evidenced_by`

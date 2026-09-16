---
uid: wiki-page:evidence-51f99c8c1993ed75
title: Claim 3e6ec7f46b13c44f
slug: claims/claim-3e6ec7f46b13c44f
page_type: evidence
status: review
summary: Long-horizon autonomous data-driven discovery. Kosmos repeatedly interleaves literature search, data analysis
  and hypothesis generation while maintaining a structured world model across hundreds of agent rollouts.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:3e6ec7f46b13c44f
source_refs: &id001
- arxiv:2511.02824
page_refs:
- wiki-page:source-51ed59b1fc0ecd08
- wiki-page:map-ontology-semantic-architecture
outgoing_links:
- target: wiki-page:source-51ed59b1fc0ecd08
  relation: evidenced_by
  claim_refs:
  - claim:3e6ec7f46b13c44f
  notes: null
- target: wiki-page:map-ontology-semantic-architecture
  relation: part_of
  claim_refs:
  - claim:3e6ec7f46b13c44f
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:3e6ec7f46b13c44f
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:3e6ec7f46b13c44f
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:052e92babb00da4b
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
  source_dependencies: *id001
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: Long-horizon autonomous data-driven discovery. Kosmos repeatedly interleaves literature search, data
      analysis and hypothesis generation while maintaining a structured world model across hundreds of agent rollouts.
    short: Long-horizon autonomous data-driven discovery. Kosmos repeatedly interleaves literature search, data
      analysis and hypothesis generation while maintaining a structured world model across hundreds of agent rollouts.
    full: null
  estimated_tokens: 144
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:3e6ec7f46b13c44f
rights_refs: []
rights_unavailable_source_refs: []
---

# Collection assessment for Kosmos: An AI Scientist for Autonomous Discovery

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

Long-horizon autonomous data-driven discovery. Kosmos repeatedly interleaves literature search, data analysis and hypothesis generation while maintaining a structured world model across hundreds of agent rollouts.

## Scope

- Claim ID: `claim:3e6ec7f46b13c44f`
- Scope: `collector assessment, not source-authored scientific fact`
- Domain: [ontology-semantic-architecture](../maps/ontology-semantic-architecture.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:a566d8629070c224` | `local://raw_data/arxiv/Kosmos: An AI Scientist for Autonomous Discovery/metadata.yaml#collection.inclusion_reason` | `raw_data/arxiv/Kosmos: An AI Scientist for Autonomous Discovery/metadata.yaml` | `metadata_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [Kosmos: An AI Scientist for Autonomous Discovery](../sources/arxiv-2511.02824.md) — `evidenced_by`
- [Ontology Semantic Architecture](../maps/ontology-semantic-architecture.md) — `part_of`

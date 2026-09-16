---
uid: wiki-page:evidence-1eaf8c8649fe972d
title: Claim d13d2fd07c92af58
slug: claims/claim-d13d2fd07c92af58
page_type: evidence
status: review
summary: Introduces machine-verifiable research output and retrieval over formal libraries, balancing less-verifiable
  natural-language research agents.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:d13d2fd07c92af58
source_refs: &id001
- arxiv-2306.15626
page_refs:
- wiki-page:source-5be112b896547169
- wiki-page:map-knowledge-memory
outgoing_links:
- target: wiki-page:source-5be112b896547169
  relation: evidenced_by
  claim_refs:
  - claim:d13d2fd07c92af58
  notes: null
- target: wiki-page:map-knowledge-memory
  relation: part_of
  claim_refs:
  - claim:d13d2fd07c92af58
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:d13d2fd07c92af58
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:d13d2fd07c92af58
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:ac56ea43f6b5393c
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv-2306.15626@sha256:5893d0b64b077ec01bee907ead6d94ae8c810abf023c2b4f618250c4fb0b7680
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
    one_line: Introduces machine-verifiable research output and retrieval over formal libraries, balancing less-verifiable
      natural-language research agents.
    short: Introduces machine-verifiable research output and retrieval over formal libraries, balancing less-verifiable
      natural-language research agents.
    full: null
  estimated_tokens: 132
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:d13d2fd07c92af58
rights_refs: []
rights_unavailable_source_refs: []
---

# Collection assessment for LeanDojo: Theorem Proving with Retrieval-Augmented Language Models

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

Introduces machine-verifiable research output and retrieval over formal libraries, balancing less-verifiable natural-language research agents.

## Scope

- Claim ID: `claim:d13d2fd07c92af58`
- Scope: `collector assessment, not source-authored scientific fact`
- Domain: [knowledge-memory](../maps/knowledge-memory.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:296659ae73b7c9bd` | `local://raw_data/arxiv/LeanDojo Theorem Proving with Retrieval-Augmented Language Models/metadata.yaml#collection.inclusion_reason` | `raw_data/arxiv/LeanDojo Theorem Proving with Retrieval-Augmented Language Models/metadata.yaml` | `metadata_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [LeanDojo: Theorem Proving with Retrieval-Augmented Language Models](../sources/arxiv-2306.15626.md) — `evidenced_by`
- [Knowledge Memory](../maps/knowledge-memory.md) — `part_of`

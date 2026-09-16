---
uid: wiki-page:evidence-9c76bfd457bcf341
title: Claim c4f2def09ea56d98
slug: claims/claim-c4f2def09ea56d98
page_type: evidence
status: review
summary: A graph-aware compiled wiki emphasizing evidenced relations, source spans, bi-temporal edges, review-gated
  entity resolution, output quarantine and agent access through MCP.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:c4f2def09ea56d98
source_refs: &id001
- github:xoai/sage-wiki
page_refs:
- wiki-page:source-a41aba6e720b278f
- wiki-page:map-llm-wiki
outgoing_links:
- target: wiki-page:source-a41aba6e720b278f
  relation: evidenced_by
  claim_refs:
  - claim:c4f2def09ea56d98
  notes: null
- target: wiki-page:map-llm-wiki
  relation: part_of
  claim_refs:
  - claim:c4f2def09ea56d98
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:c4f2def09ea56d98
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:c4f2def09ea56d98
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:464b90323fe86f3e
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - github:xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d
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
    one_line: A graph-aware compiled wiki emphasizing evidenced relations, source spans, bi-temporal edges, review-gated
      entity resolution, output quarantine and agent access through MCP.
    short: A graph-aware compiled wiki emphasizing evidenced relations, source spans, bi-temporal edges, review-gated
      entity resolution, output quarantine and agent access through MCP.
    full: null
  estimated_tokens: 115
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Collection assessment for xoai/sage-wiki

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

A graph-aware compiled wiki emphasizing evidenced relations, source spans, bi-temporal edges, review-gated entity resolution, output quarantine and agent access through MCP.

## Scope

- Claim ID: `claim:c4f2def09ea56d98`
- Scope: `collector assessment, not source-authored scientific fact`
- Domain: [llm-wiki](../maps/llm-wiki.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:c7abfedf00195f99` | `local://raw_data/githubs/xoai--sage-wiki/metadata.yaml#collection.inclusion_reason` | `raw_data/githubs/xoai--sage-wiki/metadata.yaml` | `metadata_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [xoai/sage-wiki](../sources/github-xoai-sage-wiki.md) — `evidenced_by`
- [Llm Wiki](../maps/llm-wiki.md) — `part_of`

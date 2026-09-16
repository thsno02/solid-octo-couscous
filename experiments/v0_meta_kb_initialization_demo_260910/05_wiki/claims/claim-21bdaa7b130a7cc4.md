---
uid: wiki-page:evidence-f683286a0f170b38
title: Claim 21bdaa7b130a7cc4
slug: claims/claim-21bdaa7b130a7cc4
page_type: evidence
status: review
summary: Canonical open implementation of an end-to-end automated research loop where research artifacts become
  inputs to subsequent iterations.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:21bdaa7b130a7cc4
source_refs: &id001
- github:SakanaAI/AI-Scientist
page_refs:
- wiki-page:source-11d8f2a43bca42c2
- wiki-page:map-cross-cutting
outgoing_links:
- target: wiki-page:source-11d8f2a43bca42c2
  relation: evidenced_by
  claim_refs:
  - claim:21bdaa7b130a7cc4
  notes: null
- target: wiki-page:map-cross-cutting
  relation: part_of
  claim_refs:
  - claim:21bdaa7b130a7cc4
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:21bdaa7b130a7cc4
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:21bdaa7b130a7cc4
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:3de65e2db5aac4d8
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - github:SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb
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
    one_line: Canonical open implementation of an end-to-end automated research loop where research artifacts become
      inputs to subsequent iterations.
    short: Canonical open implementation of an end-to-end automated research loop where research artifacts become
      inputs to subsequent iterations.
    full: null
  estimated_tokens: 111
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:21bdaa7b130a7cc4
rights_refs: []
rights_unavailable_source_refs: []
---

# Collection assessment for SakanaAI/AI-Scientist

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

Canonical open implementation of an end-to-end automated research loop where research artifacts become inputs to subsequent iterations.

## Scope

- Claim ID: `claim:21bdaa7b130a7cc4`
- Scope: `collector assessment, not source-authored scientific fact`
- Domain: [cross-cutting](../maps/cross-cutting.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:43f58962b84d0fd8` | `local://raw_data/githubs/SakanaAI--AI-Scientist/metadata.yaml#collection.inclusion_reason` | `raw_data/githubs/SakanaAI--AI-Scientist/metadata.yaml` | `metadata_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [SakanaAI/AI-Scientist](../sources/github-sakanaai-ai-scientist.md) — `evidenced_by`
- [Cross Cutting](../maps/cross-cutting.md) — `part_of`

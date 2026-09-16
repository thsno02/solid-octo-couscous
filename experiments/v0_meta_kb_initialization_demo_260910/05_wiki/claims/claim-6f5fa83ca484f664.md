---
uid: wiki-page:evidence-0bf31b772cff5e19
title: Claim 6f5fa83ca484f664
slug: claims/claim-6f5fa83ca484f664
page_type: evidence
status: review
summary: CLAIRE and WikiCollide make corpus-level inconsistency detection a first-class maintenance task and demonstrate
  human-editor review as part of the loop.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:6f5fa83ca484f664
source_refs: &id001
- arxiv:2509.23233
page_refs:
- wiki-page:source-e27d5b13b062021d
- wiki-page:map-llm-wiki
outgoing_links:
- target: wiki-page:source-e27d5b13b062021d
  relation: evidenced_by
  claim_refs:
  - claim:6f5fa83ca484f664
  notes: null
- target: wiki-page:map-llm-wiki
  relation: part_of
  claim_refs:
  - claim:6f5fa83ca484f664
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:6f5fa83ca484f664
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:6f5fa83ca484f664
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:25971ceacefe068b
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
  source_dependencies: *id001
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: CLAIRE and WikiCollide make corpus-level inconsistency detection a first-class maintenance task and
      demonstrate human-editor review as part of the loop.
    short: CLAIRE and WikiCollide make corpus-level inconsistency detection a first-class maintenance task and demonstrate
      human-editor review as part of the loop.
    full: null
  estimated_tokens: 150
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:6f5fa83ca484f664
rights_refs: []
rights_unavailable_source_refs: []
---

# Collection assessment for Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

CLAIRE and WikiCollide make corpus-level inconsistency detection a first-class maintenance task and demonstrate human-editor review as part of the loop.

## Scope

- Claim ID: `claim:6f5fa83ca484f664`
- Scope: `collector assessment, not source-authored scientific fact`
- Domain: [llm-wiki](../maps/llm-wiki.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:e30f4eb524d5ee06` | `local://raw_data/arxiv/Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models/metadata.yaml#collection.inclusion_reason` | `raw_data/arxiv/Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models/metadata.yaml` | `metadata_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models](../sources/arxiv-2509.23233.md) — `evidenced_by`
- [Llm Wiki](../maps/llm-wiki.md) — `part_of`

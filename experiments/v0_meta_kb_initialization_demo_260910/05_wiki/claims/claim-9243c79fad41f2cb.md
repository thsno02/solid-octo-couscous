---
uid: wiki-page:evidence-3b41d995955e08d2
title: Claim 9243c79fad41f2cb
slug: claims/claim-9243c79fad41f2cb
page_type: evidence
status: review
summary: 'Foundational formal RSI work: a self-referential problem solver rewrites any part of its own code after
  proving that the rewrite improves expected utility.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:9243c79fad41f2cb
source_refs: &id001
- arxiv:cs/0309048
page_refs:
- wiki-page:source-0e73b118b5b15597
- wiki-page:map-recursive-self-improvement
outgoing_links:
- target: wiki-page:source-0e73b118b5b15597
  relation: evidenced_by
  claim_refs:
  - claim:9243c79fad41f2cb
  notes: null
- target: wiki-page:map-recursive-self-improvement
  relation: part_of
  claim_refs:
  - claim:9243c79fad41f2cb
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:9243c79fad41f2cb
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:9243c79fad41f2cb
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:6ece1ec8eed4da8e
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:cs/0309048@sha256:ab75c69deb1c4b41ae77f5f817735922ad52fc9a8d51ec5184f4978a88b4052e
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
    one_line: 'Foundational formal RSI work: a self-referential problem solver rewrites any part of its own code
      after proving that the rewrite improves expected utility.'
    short: 'Foundational formal RSI work: a self-referential problem solver rewrites any part of its own code after
      proving that the rewrite improves expected utility.'
    full: null
  estimated_tokens: 154
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:9243c79fad41f2cb
rights_refs: []
rights_unavailable_source_refs: []
---

# Collection assessment for Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

Foundational formal RSI work: a self-referential problem solver rewrites any part of its own code after proving that the rewrite improves expected utility.

## Scope

- Claim ID: `claim:9243c79fad41f2cb`
- Scope: `collector assessment, not source-authored scientific fact`
- Domain: [recursive-self-improvement](../maps/recursive-self-improvement.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:2a08136ddb6a0fdd` | `local://raw_data/arxiv/Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements/metadata.yaml#collection.inclusion_reason` | `raw_data/arxiv/Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements/metadata.yaml` | `metadata_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements](../sources/arxiv-cs-0309048.md) — `evidenced_by`
- [Recursive Self Improvement](../maps/recursive-self-improvement.md) — `part_of`

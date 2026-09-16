---
uid: wiki-page:evidence-c0dc9e55b2e9b137
title: Claim 1b6ae1229c17cacd
slug: claims/claim-1b6ae1229c17cacd
page_type: evidence
status: review
summary: One of the clearest open implementations of a system that edits its own agent code, evaluates variants,
  and keeps an archive instead of overwriting a single lineage.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:1b6ae1229c17cacd
source_refs: &id001
- github:jennyzzt/dgm
page_refs:
- wiki-page:source-e3fe88d81aab6499
- wiki-page:map-recursive-self-improvement
outgoing_links:
- target: wiki-page:source-e3fe88d81aab6499
  relation: evidenced_by
  claim_refs:
  - claim:1b6ae1229c17cacd
  notes: null
- target: wiki-page:map-recursive-self-improvement
  relation: part_of
  claim_refs:
  - claim:1b6ae1229c17cacd
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:1b6ae1229c17cacd
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:1b6ae1229c17cacd
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
  - github:jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2
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
    one_line: One of the clearest open implementations of a system that edits its own agent code, evaluates variants,
      and keeps an archive instead of overwriting a single lineage.
    short: One of the clearest open implementations of a system that edits its own agent code, evaluates variants,
      and keeps an archive instead of overwriting a single lineage.
    full: null
  estimated_tokens: 122
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:1b6ae1229c17cacd
rights_refs: []
rights_unavailable_source_refs: []
---

# Collection assessment for jennyzzt/dgm

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

One of the clearest open implementations of a system that edits its own agent code, evaluates variants, and keeps an archive instead of overwriting a single lineage.

## Scope

- Claim ID: `claim:1b6ae1229c17cacd`
- Scope: `collector assessment, not source-authored scientific fact`
- Domain: [recursive-self-improvement](../maps/recursive-self-improvement.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:1f00e2f956a2afe4` | `local://raw_data/githubs/jennyzzt--dgm/metadata.yaml#collection.inclusion_reason` | `raw_data/githubs/jennyzzt--dgm/metadata.yaml` | `metadata_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [jennyzzt/dgm](../sources/github-jennyzzt-dgm.md) — `evidenced_by`
- [Recursive Self Improvement](../maps/recursive-self-improvement.md) — `part_of`

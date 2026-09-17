---
uid: wiki-page:evidence-c7e5f49d25efb6ba
title: Claim d38b49dc4376d4b0
slug: claims/claim-d38b49dc4376d4b0
page_type: evidence
status: review
summary: Repository for **Darwin Gödel Machine (DGM)**, a novel self-improving system that iteratively modifies
  its own code (thereby also improving its ability to modify its own codebase) and empirically validates each change
  us
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:d38b49dc4376d4b0
source_refs: &id001
- github:jennyzzt/dgm
page_refs:
- wiki-page:source-e3fe88d81aab6499
- wiki-page:map-recursive-self-improvement
outgoing_links:
- target: wiki-page:source-e3fe88d81aab6499
  relation: evidenced_by
  claim_refs:
  - claim:d38b49dc4376d4b0
  notes: null
- target: wiki-page:map-recursive-self-improvement
  relation: part_of
  claim_refs:
  - claim:d38b49dc4376d4b0
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:d38b49dc4376d4b0
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:d38b49dc4376d4b0
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:4e541384e82b1271
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
    one_line: Repository for **Darwin Gödel Machine (DGM)**, a novel self-improving system that iteratively modifies
      its own code (thereby also improving its ability to modify its own codebase) and empirically validates each
      change us
    short: Repository for **Darwin Gödel Machine (DGM)**, a novel self-improving system that iteratively modifies
      its own code (thereby also improving its ability to modify its own codebase) and empirically validates each
      change us
    full: null
  estimated_tokens: 207
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:d38b49dc4376d4b0
rights_refs: []
rights_unavailable_source_refs:
- github:jennyzzt/dgm
---

# Source assertion from jennyzzt/dgm

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

Repository for **Darwin Gödel Machine (DGM)**, a novel self-improving system that iteratively modifies its own code (thereby also improving its ability to modify its own codebase) and empirically validates each change using coding benchmarks.

## Scope

- Claim ID: `claim:d38b49dc4376d4b0`
- Scope: `source-reported assertion`
- Domain: [recursive-self-improvement](../maps/recursive-self-improvement.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:86f2cb90e58dd2e2` | `local://materialized_sources/corpus/github-jennyzzt-dgm--c8b75f99/evidence/files/README.md#L14-L14` | `materialized_sources/corpus/github-jennyzzt-dgm--c8b75f99/evidence/files/README.md` | `semantic_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [jennyzzt/dgm](../sources/github-jennyzzt-dgm.md) — `evidenced_by`
- [Recursive Self Improvement](../maps/recursive-self-improvement.md) — `part_of`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### jennyzzt/dgm (`github:jennyzzt/dgm`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

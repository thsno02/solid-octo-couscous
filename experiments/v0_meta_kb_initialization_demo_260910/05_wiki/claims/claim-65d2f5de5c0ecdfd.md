---
uid: wiki-page:evidence-c78374ec4210e21f
title: Claim 65d2f5de5c0ecdfd
slug: claims/claim-65d2f5de5c0ecdfd
page_type: evidence
status: review
summary: Provides the taxonomy, evaluation metrics, datasets, locality/generalization criteria, and open problems
  needed to govern knowledge updates rather than treating updates as an unconstrained write operation.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:65d2f5de5c0ecdfd
source_refs: &id001
- arxiv:2310.16218
page_refs:
- wiki-page:source-003e063d0c302d83
- wiki-page:map-knowledge-editing
outgoing_links:
- target: wiki-page:source-003e063d0c302d83
  relation: evidenced_by
  claim_refs:
  - claim:65d2f5de5c0ecdfd
  notes: null
- target: wiki-page:map-knowledge-editing
  relation: part_of
  claim_refs:
  - claim:65d2f5de5c0ecdfd
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:65d2f5de5c0ecdfd
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:65d2f5de5c0ecdfd
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
  - arxiv:2310.16218@sha256:be80105279b0f4acf0e1817a727c0de41b57db523e6a7bc5369b0e062139f52f
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
    one_line: Provides the taxonomy, evaluation metrics, datasets, locality/generalization criteria, and open problems
      needed to govern knowledge updates rather than treating updates as an unconstrained write operation.
    short: Provides the taxonomy, evaluation metrics, datasets, locality/generalization criteria, and open problems
      needed to govern knowledge updates rather than treating updates as an unconstrained write operation.
    full: null
  estimated_tokens: 147
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:65d2f5de5c0ecdfd
rights_refs: []
rights_unavailable_source_refs: []
---

# Collection assessment for Knowledge Editing for Large Language Models: A Survey

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

Provides the taxonomy, evaluation metrics, datasets, locality/generalization criteria, and open problems needed to govern knowledge updates rather than treating updates as an unconstrained write operation.

## Scope

- Claim ID: `claim:65d2f5de5c0ecdfd`
- Scope: `collector assessment, not source-authored scientific fact`
- Domain: [knowledge-editing](../maps/knowledge-editing.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:3846199ea839fba4` | `local://raw_data/arxiv/Knowledge Editing for Large Language Models: A Survey/metadata.yaml#collection.inclusion_reason` | `raw_data/arxiv/Knowledge Editing for Large Language Models: A Survey/metadata.yaml` | `metadata_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [Knowledge Editing for Large Language Models: A Survey](../sources/arxiv-2310.16218.md) — `evidenced_by`
- [Knowledge Editing](../maps/knowledge-editing.md) — `part_of`

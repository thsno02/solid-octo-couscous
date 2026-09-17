---
uid: wiki-page:evidence-c31aa5df2cddb49a
title: Claim c16ddfd2ab0e0feb
slug: claims/claim-c16ddfd2ab0e0feb
page_type: evidence
status: review
summary: A broad taxonomy of self-evolving agents organized around what, when, how, and where to evolve, spanning
  model, memory, tool, and architecture changes.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:c16ddfd2ab0e0feb
source_refs: &id001
- arxiv:2507.21046
page_refs:
- wiki-page:source-68be106d4fc61e3b
- wiki-page:map-open-ended-evolution
outgoing_links:
- target: wiki-page:source-68be106d4fc61e3b
  relation: evidenced_by
  claim_refs:
  - claim:c16ddfd2ab0e0feb
  notes: null
- target: wiki-page:map-open-ended-evolution
  relation: part_of
  claim_refs:
  - claim:c16ddfd2ab0e0feb
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:c16ddfd2ab0e0feb
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:c16ddfd2ab0e0feb
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:39419dbd8ad82c9e
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2507.21046@sha256:0b39df03feea2f4d8ac41e35a9247889978a53cb1e7b7d3eafaae76ad97b5602
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
    one_line: A broad taxonomy of self-evolving agents organized around what, when, how, and where to evolve, spanning
      model, memory, tool, and architecture changes.
    short: A broad taxonomy of self-evolving agents organized around what, when, how, and where to evolve, spanning
      model, memory, tool, and architecture changes.
    full: null
  estimated_tokens: 173
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:c16ddfd2ab0e0feb
rights_refs: []
rights_unavailable_source_refs: []
---

# Collection assessment for A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

A broad taxonomy of self-evolving agents organized around what, when, how, and where to evolve, spanning model, memory, tool, and architecture changes.

## Scope

- Claim ID: `claim:c16ddfd2ab0e0feb`
- Scope: `collector assessment, not source-authored scientific fact`
- Domain: [open-ended-evolution](../maps/open-ended-evolution.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:dc841ab6de42ecb3` | `local://raw_data/arxiv/A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence/metadata.yaml#collection.inclusion_reason` | `raw_data/arxiv/A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence/metadata.yaml` | `metadata_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence](../sources/arxiv-2507.21046.md) — `evidenced_by`
- [Open Ended Evolution](../maps/open-ended-evolution.md) — `part_of`

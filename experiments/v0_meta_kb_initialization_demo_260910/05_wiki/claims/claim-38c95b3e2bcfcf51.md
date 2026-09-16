---
uid: wiki-page:evidence-9f274d1678d7b92b
title: Claim 38c95b3e2bcfcf51
slug: claims/claim-38c95b3e2bcfcf51
page_type: evidence
status: review
summary: 'One of the grand challenges of artificial general intelligence is developing agents capable of conducting
  scientific research and discovering new knowledge. While frontier models have already been used as aides to human '
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:38c95b3e2bcfcf51
source_refs: &id001
- arxiv:2408.06292
page_refs:
- wiki-page:source-c1dbc9c2a83a564a
- wiki-page:map-automated-research
outgoing_links:
- target: wiki-page:source-c1dbc9c2a83a564a
  relation: evidenced_by
  claim_refs:
  - claim:38c95b3e2bcfcf51
  notes: null
- target: wiki-page:map-automated-research
  relation: part_of
  claim_refs:
  - claim:38c95b3e2bcfcf51
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:38c95b3e2bcfcf51
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:38c95b3e2bcfcf51
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:487f888f4db7dee3
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2408.06292@sha256:4ddccff8b6e49dec4c7bb219d4330f1faf47255b5b1b33d01f207eae23e119e9
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
    one_line: 'One of the grand challenges of artificial general intelligence is developing agents capable of conducting
      scientific research and discovering new knowledge. While frontier models have already been used as aides to
      human '
    short: 'One of the grand challenges of artificial general intelligence is developing agents capable of conducting
      scientific research and discovering new knowledge. While frontier models have already been used as aides to
      human '
    full: null
  estimated_tokens: 140
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Source assertion from The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

One of the grand challenges of artificial general intelligence is developing agents capable of conducting scientific research and discovering new knowledge. While frontier models have already been used as aides to human scientists, e.g.

## Scope

- Claim ID: `claim:38c95b3e2bcfcf51`
- Scope: `source-reported assertion`
- Domain: [automated-research](../maps/automated-research.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:32355b67bcee3a03` | `local://materialized_sources/corpus/arxiv-2408.06292--522d359c/normalized/document.txt#L573-L574` | `materialized_sources/corpus/arxiv-2408.06292--522d359c/normalized/document.txt` | `full_text` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](../sources/arxiv-2408.06292.md) — `evidenced_by`
- [Automated Research](../maps/automated-research.md) — `part_of`

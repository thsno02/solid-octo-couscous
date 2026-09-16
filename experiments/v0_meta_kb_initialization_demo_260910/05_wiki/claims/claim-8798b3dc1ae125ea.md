---
uid: wiki-page:evidence-638ecd816dce953d
title: Claim 8798b3dc1ae125ea
slug: claims/claim-8798b3dc1ae125ea
page_type: evidence
status: review
summary: End-to-end autonomous scientific discovery without a fixed human-authored template. Iteratively formulates
  hypotheses, designs and executes experiments, analyzes results, and writes papers using an agentic tree-search
  pr
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:8798b3dc1ae125ea
source_refs: &id001
- arxiv:2504.08066
page_refs:
- wiki-page:source-1203e0209022f228
- wiki-page:map-automated-research
outgoing_links:
- target: wiki-page:source-1203e0209022f228
  relation: evidenced_by
  claim_refs:
  - claim:8798b3dc1ae125ea
  notes: null
- target: wiki-page:map-automated-research
  relation: part_of
  claim_refs:
  - claim:8798b3dc1ae125ea
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:8798b3dc1ae125ea
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:8798b3dc1ae125ea
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:6b16cc1e2adf538b
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2504.08066@sha256:53bafd3028e3f8829a3d85220e84dcf0d18934f9b75c092a60de303ff3644bd2
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
    one_line: End-to-end autonomous scientific discovery without a fixed human-authored template. Iteratively formulates
      hypotheses, designs and executes experiments, analyzes results, and writes papers using an agentic tree-search
      pr
    short: End-to-end autonomous scientific discovery without a fixed human-authored template. Iteratively formulates
      hypotheses, designs and executes experiments, analyzes results, and writes papers using an agentic tree-search
      pr
    full: null
  estimated_tokens: 160
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:8798b3dc1ae125ea
rights_refs: []
rights_unavailable_source_refs: []
---

# Collection assessment for The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

End-to-end autonomous scientific discovery without a fixed human-authored template. Iteratively formulates hypotheses, designs and executes experiments, analyzes results, and writes papers using an agentic tree-search process.

## Scope

- Claim ID: `claim:8798b3dc1ae125ea`
- Scope: `collector assessment, not source-authored scientific fact`
- Domain: [automated-research](../maps/automated-research.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:924a40542eeaca58` | `local://raw_data/arxiv/The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search/metadata.yaml#collection.inclusion_reason` | `raw_data/arxiv/The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search/metadata.yaml` | `metadata_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search](../sources/arxiv-2504.08066.md) — `evidenced_by`
- [Automated Research](../maps/automated-research.md) — `part_of`

---
uid: wiki-page:evidence-36c1729b09de22fd
title: Claim ecdd2719fa55751c
slug: claims/claim-ecdd2719fa55751c
page_type: evidence
status: review
summary: LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we
  introduce ~(the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine learning
  pa
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:ecdd2719fa55751c
source_refs: &id001
- arxiv:2602.06855
page_refs:
- wiki-page:source-a264f295a5ce5604
- wiki-page:map-governance-evaluation
outgoing_links:
- target: wiki-page:source-a264f295a5ce5604
  relation: evidenced_by
  claim_refs:
  - claim:ecdd2719fa55751c
  notes: null
- target: wiki-page:map-governance-evaluation
  relation: part_of
  claim_refs:
  - claim:ecdd2719fa55751c
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:ecdd2719fa55751c
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:ecdd2719fa55751c
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
  - arxiv:2602.06855@sha256:ac1ba940f1bdc54e012cc384c428f78bd01d50d7a947f052117944c03e790d9a
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
    one_line: LLM agents hold significant promise for advancing scientific research. To accelerate this progress,
      we introduce ~(the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine
      learning pa
    short: LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we
      introduce ~(the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine
      learning pa
    full: null
  estimated_tokens: 233
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:ecdd2719fa55751c
rights_refs: []
rights_unavailable_source_refs:
- arxiv:2602.06855
---

# Source assertion from AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we introduce ~(the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine learning papers.

## Scope

- Claim ID: `claim:ecdd2719fa55751c`
- Scope: `source-reported assertion`
- Domain: [governance-evaluation](../maps/governance-evaluation.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:3c0c7c9546c2ec15` | `local://materialized_sources/corpus/arxiv-2602.06855--0b517136/normalized/document.txt#L621-L622` | `materialized_sources/corpus/arxiv-2602.06855--0b517136/normalized/document.txt` | `full_text` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents](../sources/arxiv-2602.06855.md) — `evidenced_by`
- [Governance Evaluation](../maps/governance-evaluation.md) — `part_of`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents (`arxiv:2602.06855`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

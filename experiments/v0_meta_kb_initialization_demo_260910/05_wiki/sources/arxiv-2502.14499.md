---
uid: wiki-page:source-3dda2384308efbda
title: 'MLGym: A New Framework and Benchmark for Advancing AI Research Agents'
slug: sources/arxiv-2502.14499
page_type: source
status: review
summary: 'Source page for MLGym: A New Framework and Benchmark for Advancing AI Research Agents with claim/evidence
  expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:4bf5ea8e6b4e37de
- claim:4fd96c70e0c625fd
source_refs: &id002
- arxiv:2502.14499
page_refs:
- wiki-page:map-governance-evaluation
- wiki-page:evidence-973c18c6200bf335
- wiki-page:evidence-d3f9114eb1b08abf
outgoing_links:
- target: wiki-page:map-governance-evaluation
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-973c18c6200bf335
  relation: evidenced_by
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  notes: null
- target: wiki-page:evidence-d3f9114eb1b08abf
  relation: evidenced_by
  claim_refs:
  - claim:4fd96c70e0c625fd
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  source_refs:
  - arxiv:2502.14499
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:4fd96c70e0c625fd
  source_refs:
  - arxiv:2502.14499
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:c186e07607708b1c
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2502.14499@sha256:de8bc15be762914dd2f056f00efe2b83d51ce852a7035d65e866e6cdecbbb65a
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
  source_dependencies: *id002
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: 'Source page for MLGym: A New Framework and Benchmark for Advancing AI Research Agents with claim/evidence
      expansion.'
    short: 'Source page for MLGym: A New Framework and Benchmark for Advancing AI Research Agents with claim/evidence
      expansion.'
    full: null
  estimated_tokens: 295
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:4bf5ea8e6b4e37de
- claim:4fd96c70e0c625fd
rights_refs: []
rights_unavailable_source_refs:
- arxiv:2502.14499
---

# MLGym: A New Framework and Benchmark for Advancing AI Research Agents

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2502.14499`
- Canonical ID: `2502.14499`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:de8bc15be762914dd2f056f00efe2b83d51ce852a7035d65e866e6cdecbbb65a`
- Domain: [governance-evaluation](../maps/governance-evaluation.md)
- Local document: `materialized_sources/corpus/arxiv-2502.14499--a7f1a2e8/normalized/document.txt`

## Source-reported candidate statements

- We introduce Meta and -Bench, a new framework and benchmark for evaluating and developing LLM agents on AI research tasks. This is the first Gym environment for machine learning (ML) tasks, enabling research on reinforcement learning (RL) algorithms for training such agents. 〔[claim:4bf5ea8e6b4e37de](../claims/claim-4bf5ea8e6b4e37de.md)〕

## Collection assessments

- A Gym-style environment and benchmark for training/evaluating agents on open-ended ML research tasks requiring ideation, implementation, experimentation, analysis and iterative improvement. 〔[claim:4fd96c70e0c625fd](../claims/claim-4fd96c70e0c625fd.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:4bf5ea8e6b4e37de` | `evidence:0b3ad94ceb672903` | `local://materialized_sources/corpus/arxiv-2502.14499--a7f1a2e8/normalized/document.txt#L74-L74` | `full_text` |
| `claim:4fd96c70e0c625fd` | `evidence:751adf7b39d39c48` | `local://raw_data/arxiv/MLGym: A New Framework and Benchmark for Advancing AI Research Agents/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Governance Evaluation](../maps/governance-evaluation.md) — `part_of`
- [Claim 4bf5ea8e6b4e37de](../claims/claim-4bf5ea8e6b4e37de.md) — `evidenced_by`
- [Claim 4fd96c70e0c625fd](../claims/claim-4fd96c70e0c625fd.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### MLGym: A New Framework and Benchmark for Advancing AI Research Agents (`arxiv:2502.14499`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

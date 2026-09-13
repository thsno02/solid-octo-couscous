---
uid: wiki-page:source-c29f716871f80314
title: 'Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents'
slug: sources/arxiv-2505.22954
page_type: source
status: review
summary: 'Source page for Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents with claim/evidence
  expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:90ae7352bb085ae8
- claim:ae45b8d667e29552
source_refs: &id002
- arxiv:2505.22954
page_refs:
- wiki-page:map-recursive-self-improvement
- wiki-page:evidence-e923ecfc4b63b02d
- wiki-page:evidence-21eaae99382a895a
outgoing_links:
- target: wiki-page:map-recursive-self-improvement
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-e923ecfc4b63b02d
  relation: evidenced_by
  claim_refs:
  - claim:90ae7352bb085ae8
  notes: null
- target: wiki-page:evidence-21eaae99382a895a
  relation: evidenced_by
  claim_refs:
  - claim:ae45b8d667e29552
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:ae45b8d667e29552
  source_refs:
  - arxiv:2505.22954
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:90ae7352bb085ae8
  source_refs:
  - arxiv:2505.22954
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-13T17:43:07Z'
  updated_at: '2026-09-13T17:43:07Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-13T17:43:07Z'
provenance:
  build_id: build:llm-wiki-v0:196d848b07caf422
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2505.22954@sha256:9ce27273d9175badbb14d1181bc6166c7afd5e7989ac274d3d5187413e19b9ed
  created_at: '2026-09-13T17:43:07Z'
  updated_at: '2026-09-13T17:43:07Z'
  manual_edits_preserved: true
review:
  state: needs_human
  reviewers: []
  decision_ref: null
  checked_claim_refs: []
  unresolved_issues:
  - Scientific, semantic, neutrality, and due-weight review remain required before publication.
freshness:
  status: fresh
  checked_at: '2026-09-13T17:43:07Z'
  max_age_days: 30
  source_dependencies: *id002
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: 'Source page for Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents with claim/evidence
      expansion.'
    short: 'Source page for Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents with claim/evidence
      expansion.'
    full: null
  estimated_tokens: 205
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2505.22954`
- Canonical ID: `2505.22954`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:9ce27273d9175badbb14d1181bc6166c7afd5e7989ac274d3d5187413e19b9ed`
- Domain: [recursive-self-improvement](../maps/recursive-self-improvement.md)
- Local document: `materialized_sources/corpus/arxiv-2505.22954--8a7041cb/normalized/document.txt`

## Source-reported candidate statements

- Most of today's AI systems are constrained by human-designed, fixed architectures and cannot autonomously and continuously improve themselves. The scientific method, on the other hand, is a cumulative and open-ended system, where each innovation builds upon previous artifacts, enabling future discoveries. 〔[claim:ae45b8d667e29552](../claims/claim-ae45b8d667e29552.md)〕

## Collection assessments

- A central modern RSI result: iteratively modifies an agent codebase, empirically validates changes, and preserves a diverse archive/tree of agents so improvement can proceed through multiple open-ended stepping-stone paths. 〔[claim:90ae7352bb085ae8](../claims/claim-90ae7352bb085ae8.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:90ae7352bb085ae8` | `evidence:e71040c37751e493` | `local://raw_data/arxiv/Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents/metadata.yaml#collection-inclusion-reason` | `metadata_capsule` |
| `claim:ae45b8d667e29552` | `evidence:5693bd7ef23242bc` | `local://materialized_sources/corpus/arxiv-2505.22954--8a7041cb/normalized/document.txt#L88-L89` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Recursive Self Improvement](../maps/recursive-self-improvement.md) — `part_of`
- [Claim 90ae7352bb085ae8](../claims/claim-90ae7352bb085ae8.md) — `evidenced_by`
- [Claim ae45b8d667e29552](../claims/claim-ae45b8d667e29552.md) — `evidenced_by`

---
uid: wiki-page:source-18c791741aa4bcd7
title: 'DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents'
slug: sources/arxiv-2406.06769
page_type: source
status: review
summary: 'Source page for DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific
  Discovery Agents with claim/evidence expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:84c91602bd1dfb78
- claim:bde139a533f9483a
source_refs: &id002
- arxiv:2406.06769
page_refs:
- wiki-page:map-governance-evaluation
- wiki-page:evidence-7251138bb2057919
- wiki-page:evidence-6e6d202159e49cd6
outgoing_links:
- target: wiki-page:map-governance-evaluation
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-7251138bb2057919
  relation: evidenced_by
  claim_refs:
  - claim:84c91602bd1dfb78
  notes: null
- target: wiki-page:evidence-6e6d202159e49cd6
  relation: evidenced_by
  claim_refs:
  - claim:bde139a533f9483a
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:84c91602bd1dfb78
  source_refs:
  - arxiv:2406.06769
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:bde139a533f9483a
  source_refs:
  - arxiv:2406.06769
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:0c619e550fe24de2
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2406.06769@sha256:cb1d6ccc88eb66af69e71730a5c488234ff4fe8af04ba04081b5a445f4d39b3e
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
    one_line: 'Source page for DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific
      Discovery Agents with claim/evidence expansion.'
    short: 'Source page for DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific
      Discovery Agents with claim/evidence expansion.'
    full: null
  estimated_tokens: 198
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2406.06769`
- Canonical ID: `2406.06769`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:cb1d6ccc88eb66af69e71730a5c488234ff4fe8af04ba04081b5a445f4d39b3e`
- Domain: [governance-evaluation](../maps/governance-evaluation.md)
- Local document: `materialized_sources/corpus/arxiv-2406.06769--d1971e3b/normalized/document.txt`

## Source-reported candidate statements

- Automated scientific discovery promises to accelerate progress across scientific domains. However, developing and evaluating an AI agent's capacity for end-to-end scientific reasoning is challenging as running real-world experiments is often prohibitively expensive or infeasible. 〔[claim:84c91602bd1dfb78](../claims/claim-84c91602bd1dfb78.md)〕

## Collection assessments

- A benchmark environment for complete novel scientific discovery cycles where agents must form hypotheses, run experiments, analyze results and discover explanatory knowledge. 〔[claim:bde139a533f9483a](../claims/claim-bde139a533f9483a.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:84c91602bd1dfb78` | `evidence:69559f8937311f42` | `local://materialized_sources/corpus/arxiv-2406.06769--d1971e3b/normalized/document.txt#L89-L90` | `full_text` |
| `claim:bde139a533f9483a` | `evidence:fdf8b5c29b9da39e` | `local://raw_data/arxiv/DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Governance Evaluation](../maps/governance-evaluation.md) — `part_of`
- [Claim 84c91602bd1dfb78](../claims/claim-84c91602bd1dfb78.md) — `evidenced_by`
- [Claim bde139a533f9483a](../claims/claim-bde139a533f9483a.md) — `evidenced_by`

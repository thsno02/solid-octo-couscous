---
uid: wiki-page:source-0e32ebb2e855fd30
title: 'Robin: A multi-agent system for automating scientific discovery'
slug: sources/arxiv-2505.13400
page_type: source
status: review
summary: 'Source page for Robin: A multi-agent system for automating scientific discovery with claim/evidence expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:3c6cef89711e89f2
- claim:852bc42ef50e89c7
source_refs: &id002
- arxiv:2505.13400
page_refs:
- wiki-page:map-automated-research
- wiki-page:evidence-f561a2ece83db79d
- wiki-page:evidence-1f89e493aa80fc8b
outgoing_links:
- target: wiki-page:map-automated-research
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-f561a2ece83db79d
  relation: evidenced_by
  claim_refs:
  - claim:3c6cef89711e89f2
  notes: null
- target: wiki-page:evidence-1f89e493aa80fc8b
  relation: evidenced_by
  claim_refs:
  - claim:852bc42ef50e89c7
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:3c6cef89711e89f2
  source_refs:
  - arxiv:2505.13400
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:852bc42ef50e89c7
  source_refs:
  - arxiv:2505.13400
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:f3fea76ebc259510
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2505.13400@sha256:1abd0b99271884b6f1a8fd9db0185e8042f079a61879ec0c9a7febae6a0c942c
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
    one_line: 'Source page for Robin: A multi-agent system for automating scientific discovery with claim/evidence
      expansion.'
    short: 'Source page for Robin: A multi-agent system for automating scientific discovery with claim/evidence
      expansion.'
    full: null
  estimated_tokens: 287
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:3c6cef89711e89f2
- claim:852bc42ef50e89c7
rights_refs: []
rights_unavailable_source_refs:
- arxiv:2505.13400
---

# Robin: A multi-agent system for automating scientific discovery

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2505.13400`
- Canonical ID: `2505.13400`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:1abd0b99271884b6f1a8fd9db0185e8042f079a61879ec0c9a7febae6a0c942c`
- Domain: [automated-research](../maps/automated-research.md)
- Local document: `materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/normalized/document.txt`

## Source-reported candidate statements

- Scientific discovery is driven by the iterative process of background research, hypothesis generation, experimentation, and data analysis. Despite recent advancements in applying artificial intelligence to scientific discovery, no system has yet automated all of these stages in a single workflow. 〔[claim:3c6cef89711e89f2](../claims/claim-3c6cef89711e89f2.md)〕

## Collection assessments

- One of the strongest demonstrations of a lab-in-the-loop discovery cycle: background research, hypothesis generation, experimental planning, human-executed wet-lab experiments, data analysis, and updated hypotheses. 〔[claim:852bc42ef50e89c7](../claims/claim-852bc42ef50e89c7.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:3c6cef89711e89f2` | `evidence:42eb6cb152f003dc` | `local://materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/normalized/document.txt#L96-L96` | `full_text` |
| `claim:852bc42ef50e89c7` | `evidence:876eba3abd8faafc` | `local://raw_data/arxiv/Robin: A multi-agent system for automating scientific discovery/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Automated Research](../maps/automated-research.md) — `part_of`
- [Claim 3c6cef89711e89f2](../claims/claim-3c6cef89711e89f2.md) — `evidenced_by`
- [Claim 852bc42ef50e89c7](../claims/claim-852bc42ef50e89c7.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Robin: A multi-agent system for automating scientific discovery (`arxiv:2505.13400`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

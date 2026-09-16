---
uid: wiki-page:source-11d8f2a43bca42c2
title: SakanaAI/AI-Scientist
slug: sources/github-sakanaai-ai-scientist
page_type: source
status: review
summary: Source page for SakanaAI/AI-Scientist with claim/evidence expansion.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:21bdaa7b130a7cc4
- claim:334565c7ebb30cb5
source_refs: &id002
- github:SakanaAI/AI-Scientist
page_refs:
- wiki-page:map-cross-cutting
- wiki-page:evidence-f683286a0f170b38
- wiki-page:evidence-99cfc321f0f45e32
outgoing_links:
- target: wiki-page:map-cross-cutting
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-f683286a0f170b38
  relation: evidenced_by
  claim_refs:
  - claim:21bdaa7b130a7cc4
  notes: null
- target: wiki-page:evidence-99cfc321f0f45e32
  relation: evidenced_by
  claim_refs:
  - claim:334565c7ebb30cb5
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:334565c7ebb30cb5
  source_refs:
  - github:SakanaAI/AI-Scientist
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:21bdaa7b130a7cc4
  source_refs:
  - github:SakanaAI/AI-Scientist
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:699e317011de119b
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - github:SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb
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
    one_line: Source page for SakanaAI/AI-Scientist with claim/evidence expansion.
    short: Source page for SakanaAI/AI-Scientist with claim/evidence expansion.
    full: null
  estimated_tokens: 239
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:21bdaa7b130a7cc4
- claim:334565c7ebb30cb5
rights_refs: []
rights_unavailable_source_refs:
- github:SakanaAI/AI-Scientist
---

# SakanaAI/AI-Scientist

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `github:SakanaAI/AI-Scientist`
- Canonical ID: `SakanaAI/AI-Scientist`
- Source type: `github`
- Content tier: `semantic_capsule`
- Revision: `1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb`
- Domain: [cross-cutting](../maps/cross-cutting.md)
- Local document: `materialized_sources/corpus/github-SakanaAI-AI-Scientist--2b41a05d/evidence/files/README.md`

## Source-reported candidate statements

- One of the grand challenges of artificial intelligence is developing agents capable of conducting scientific research and discovering new knowledge. 〔[claim:334565c7ebb30cb5](../claims/claim-334565c7ebb30cb5.md)〕

## Collection assessments

- Canonical open implementation of an end-to-end automated research loop where research artifacts become inputs to subsequent iterations. 〔[claim:21bdaa7b130a7cc4](../claims/claim-21bdaa7b130a7cc4.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:21bdaa7b130a7cc4` | `evidence:43f58962b84d0fd8` | `local://raw_data/githubs/SakanaAI--AI-Scientist/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:334565c7ebb30cb5` | `evidence:63f97f6fe4380c7d` | `local://materialized_sources/corpus/github-SakanaAI-AI-Scientist--2b41a05d/evidence/files/README.md#L14-L14` | `semantic_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Cross Cutting](../maps/cross-cutting.md) — `part_of`
- [Claim 21bdaa7b130a7cc4](../claims/claim-21bdaa7b130a7cc4.md) — `evidenced_by`
- [Claim 334565c7ebb30cb5](../claims/claim-334565c7ebb30cb5.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### SakanaAI/AI-Scientist (`github:SakanaAI/AI-Scientist`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

---
uid: wiki-page:source-5b06dbb06d02d1f5
title: 'AutoLabs: Cognitive Multi-Agent Systems with Self-Correction for Autonomous Chemical Experimentation'
slug: sources/arxiv-2509.25651
page_type: source
status: review
summary: 'Source page for AutoLabs: Cognitive Multi-Agent Systems with Self-Correction for Autonomous Chemical Experimentation
  with claim/evidence expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:32d4ab82e7394fa1
- claim:34aa536e34afa87c
source_refs: &id002
- arxiv:2509.25651
page_refs:
- wiki-page:map-cross-cutting
- wiki-page:evidence-1b76c800743833b5
- wiki-page:evidence-d59b262288fdbed0
outgoing_links:
- target: wiki-page:map-cross-cutting
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-1b76c800743833b5
  relation: evidenced_by
  claim_refs:
  - claim:32d4ab82e7394fa1
  notes: null
- target: wiki-page:evidence-d59b262288fdbed0
  relation: evidenced_by
  claim_refs:
  - claim:34aa536e34afa87c
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:32d4ab82e7394fa1
  source_refs:
  - arxiv:2509.25651
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:34aa536e34afa87c
  source_refs:
  - arxiv:2509.25651
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:05e882fced13f0e1
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2509.25651@sha256:14424738e0ad14b8fd5891102b89d9a3e4888beb22605f723e1cc044231eb803
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
    one_line: 'Source page for AutoLabs: Cognitive Multi-Agent Systems with Self-Correction for Autonomous Chemical
      Experimentation with claim/evidence expansion.'
    short: 'Source page for AutoLabs: Cognitive Multi-Agent Systems with Self-Correction for Autonomous Chemical
      Experimentation with claim/evidence expansion.'
    full: null
  estimated_tokens: 298
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:32d4ab82e7394fa1
- claim:34aa536e34afa87c
rights_refs: []
rights_unavailable_source_refs:
- arxiv:2509.25651
---

# AutoLabs: Cognitive Multi-Agent Systems with Self-Correction for Autonomous Chemical Experimentation

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2509.25651`
- Canonical ID: `2509.25651`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:14424738e0ad14b8fd5891102b89d9a3e4888beb22605f723e1cc044231eb803`
- Domain: [cross-cutting](../maps/cross-cutting.md)
- Local document: `materialized_sources/corpus/arxiv-2509.25651--2ba7699b/normalized/document.txt`

## Source-reported candidate statements

- The automation of chemical research through self-driving laboratories (SDLs) promises to accelerate scientific discovery, yet the reliability and granular performance of the underlying AI agents remain critical, under-examined challenges. In this work, we introduce AutoLabs, a self-correcting, multi-agent architecture designed to autonomously translate natural-language instructions into executable protocols for a hig 〔[claim:32d4ab82e7394fa1](../claims/claim-32d4ab82e7394fa1.md)〕

## Collection assessments

- A self-correcting multi-agent architecture that converts scientific instructions into executable experimental protocols and validates/corrects them before hardware execution. 〔[claim:34aa536e34afa87c](../claims/claim-34aa536e34afa87c.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:32d4ab82e7394fa1` | `evidence:8c2fdbc074dbf7d4` | `local://materialized_sources/corpus/arxiv-2509.25651--2ba7699b/normalized/document.txt#L55-L55` | `full_text` |
| `claim:34aa536e34afa87c` | `evidence:51eb00707ccc813c` | `local://raw_data/arxiv/AutoLabs: Cognitive Multi-Agent Systems with Self-Correction for Autonomous Chemical Experimentation/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Cross Cutting](../maps/cross-cutting.md) — `part_of`
- [Claim 32d4ab82e7394fa1](../claims/claim-32d4ab82e7394fa1.md) — `evidenced_by`
- [Claim 34aa536e34afa87c](../claims/claim-34aa536e34afa87c.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### AutoLabs: Cognitive Multi-Agent Systems with Self-Correction for Autonomous Chemical Experimentation (`arxiv:2509.25651`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

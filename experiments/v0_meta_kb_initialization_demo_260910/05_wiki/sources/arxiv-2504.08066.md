---
uid: wiki-page:source-1203e0209022f228
title: 'The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search'
slug: sources/arxiv-2504.08066
page_type: source
status: review
summary: 'Source page for The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search
  with claim/evidence expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:8798b3dc1ae125ea
- claim:9077f46d7f30e565
source_refs: &id002
- arxiv:2504.08066
page_refs:
- wiki-page:map-automated-research
- wiki-page:evidence-638ecd816dce953d
- wiki-page:evidence-caa99c40bb0689a1
outgoing_links:
- target: wiki-page:map-automated-research
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-638ecd816dce953d
  relation: evidenced_by
  claim_refs:
  - claim:8798b3dc1ae125ea
  notes: null
- target: wiki-page:evidence-caa99c40bb0689a1
  relation: evidenced_by
  claim_refs:
  - claim:9077f46d7f30e565
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:9077f46d7f30e565
  source_refs:
  - arxiv:2504.08066
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:8798b3dc1ae125ea
  source_refs:
  - arxiv:2504.08066
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:25971ceacefe068b
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2504.08066@sha256:ea458b4c4212b9e61d909193504485986780026a962727da8669877f6f76740e
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
    one_line: 'Source page for The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree
      Search with claim/evidence expansion.'
    short: 'Source page for The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree
      Search with claim/evidence expansion.'
    full: null
  estimated_tokens: 289
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:8798b3dc1ae125ea
- claim:9077f46d7f30e565
rights_refs: []
rights_unavailable_source_refs:
- arxiv:2504.08066
---

# The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2504.08066`
- Canonical ID: `2504.08066`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:ea458b4c4212b9e61d909193504485986780026a962727da8669877f6f76740e`
- Domain: [automated-research](../maps/automated-research.md)
- Local document: `materialized_sources/corpus/arxiv-2504.08066--22ed15f2/normalized/document.txt`

## Source-reported candidate statements

- AI is increasingly playing a pivotal role in transforming how scientific discoveries are made. We introduce , an end-to-end agentic system capable of producing the first entirely AI-generated peer-review-accepted workshop paper. 〔[claim:9077f46d7f30e565](../claims/claim-9077f46d7f30e565.md)〕

## Collection assessments

- End-to-end autonomous scientific discovery without a fixed human-authored template. Iteratively formulates hypotheses, designs and executes experiments, analyzes results, and writes papers using an agentic tree-search process. 〔[claim:8798b3dc1ae125ea](../claims/claim-8798b3dc1ae125ea.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:8798b3dc1ae125ea` | `evidence:924a40542eeaca58` | `local://raw_data/arxiv/The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:9077f46d7f30e565` | `evidence:85c1017952d003b4` | `local://materialized_sources/corpus/arxiv-2504.08066--22ed15f2/normalized/document.txt#L598-L599` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Automated Research](../maps/automated-research.md) — `part_of`
- [Claim 8798b3dc1ae125ea](../claims/claim-8798b3dc1ae125ea.md) — `evidenced_by`
- [Claim 9077f46d7f30e565](../claims/claim-9077f46d7f30e565.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search (`arxiv:2504.08066`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

---
uid: wiki-page:source-68be106d4fc61e3b
title: 'A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence'
slug: sources/arxiv-2507.21046
page_type: source
status: review
summary: 'Source page for A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence with claim/evidence
  expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:c16ddfd2ab0e0feb
- claim:c776b87484aab5c2
source_refs: &id002
- arxiv:2507.21046
page_refs:
- wiki-page:map-open-ended-evolution
- wiki-page:evidence-c31aa5df2cddb49a
- wiki-page:evidence-1d4cfb868e3ee45c
outgoing_links:
- target: wiki-page:map-open-ended-evolution
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-c31aa5df2cddb49a
  relation: evidenced_by
  claim_refs:
  - claim:c16ddfd2ab0e0feb
  notes: null
- target: wiki-page:evidence-1d4cfb868e3ee45c
  relation: evidenced_by
  claim_refs:
  - claim:c776b87484aab5c2
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:c776b87484aab5c2
  source_refs:
  - arxiv:2507.21046
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:c16ddfd2ab0e0feb
  source_refs:
  - arxiv:2507.21046
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-13T17:38:21Z'
  updated_at: '2026-09-13T17:38:21Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-13T17:38:21Z'
provenance:
  build_id: build:llm-wiki-v0:9406f28f613dfbd5
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2507.21046@sha256:4bace9b0e6528f904932b2502264e47d4c5778660cd378f68e032e5588eae432
  created_at: '2026-09-13T17:38:21Z'
  updated_at: '2026-09-13T17:38:21Z'
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
  checked_at: '2026-09-13T17:38:21Z'
  max_age_days: 30
  source_dependencies: *id002
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: 'Source page for A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence with claim/evidence
      expansion.'
    short: 'Source page for A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence with claim/evidence
      expansion.'
    full: null
  estimated_tokens: 217
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2507.21046`
- Canonical ID: `2507.21046`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:4bace9b0e6528f904932b2502264e47d4c5778660cd378f68e032e5588eae432`
- Domain: [open-ended-evolution](../maps/open-ended-evolution.md)
- Local document: `materialized_sources/corpus/arxiv-2507.21046--f477f5c3/normalized/document.txt`

## Source-reported candidate statements

- Large Language Models (LLMs) have demonstrated remarkable capabilities across diverse tasks but remain fundamentally static, unable to adapt their internal parameters to novel tasks, evolving knowledge domains, or dynamic interaction contexts. As LLMs are increasingly deployed in open-ended, interactive environments, this static nature has become a critical bottleneck, necessitating agents that can adaptively reason, 〔[claim:c776b87484aab5c2](../claims/claim-c776b87484aab5c2.md)〕

## Collection assessments

- A broad taxonomy of self-evolving agents organized around what, when, how, and where to evolve, spanning model, memory, tool, and architecture changes. 〔[claim:c16ddfd2ab0e0feb](../claims/claim-c16ddfd2ab0e0feb.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:c16ddfd2ab0e0feb` | `evidence:dc841ab6de42ecb3` | `local://raw_data/arxiv/A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:c776b87484aab5c2` | `evidence:ed04910f7e6cc17e` | `local://materialized_sources/corpus/arxiv-2507.21046--f477f5c3/normalized/document.txt#L548-L548` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Open Ended Evolution](../maps/open-ended-evolution.md) — `part_of`
- [Claim c16ddfd2ab0e0feb](../claims/claim-c16ddfd2ab0e0feb.md) — `evidenced_by`
- [Claim c776b87484aab5c2](../claims/claim-c776b87484aab5c2.md) — `evidenced_by`

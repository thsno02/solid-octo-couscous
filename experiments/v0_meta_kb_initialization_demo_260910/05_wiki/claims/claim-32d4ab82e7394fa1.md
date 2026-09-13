---
uid: wiki-page:evidence-1b76c800743833b5
title: Claim 32d4ab82e7394fa1
slug: claims/claim-32d4ab82e7394fa1
page_type: evidence
status: review
summary: graphicx multirow amsmath,amssymb,amsfonts amsthm mathrsfs appendix xcolor textcomp manyfoot booktabs algorithm
  algorithmicx algpseudocode listings geometry subcaption lipsum xcolor xcolor
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:32d4ab82e7394fa1
source_refs: &id001
- arxiv:2509.25651
page_refs:
- wiki-page:source-5b06dbb06d02d1f5
- wiki-page:map-cross-cutting
outgoing_links:
- target: wiki-page:source-5b06dbb06d02d1f5
  relation: evidenced_by
  claim_refs:
  - claim:32d4ab82e7394fa1
  notes: null
- target: wiki-page:map-cross-cutting
  relation: part_of
  claim_refs:
  - claim:32d4ab82e7394fa1
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:32d4ab82e7394fa1
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:32d4ab82e7394fa1
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
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
  - arxiv:2509.25651@sha256:14424738e0ad14b8fd5891102b89d9a3e4888beb22605f723e1cc044231eb803
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
  source_dependencies: *id001
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: graphicx multirow amsmath,amssymb,amsfonts amsthm mathrsfs appendix xcolor textcomp manyfoot booktabs
      algorithm algorithmicx algpseudocode listings geometry subcaption lipsum xcolor xcolor
    short: graphicx multirow amsmath,amssymb,amsfonts amsthm mathrsfs appendix xcolor textcomp manyfoot booktabs
      algorithm algorithmicx algpseudocode listings geometry subcaption lipsum xcolor xcolor
    full: null
  estimated_tokens: 127
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Source assertion from AutoLabs: Cognitive Multi-Agent Systems with Self-Correction for Autonomous Chemical Experimentation

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

graphicx multirow amsmath,amssymb,amsfonts amsthm mathrsfs appendix xcolor textcomp manyfoot booktabs algorithm algorithmicx algpseudocode listings geometry subcaption lipsum xcolor xcolor

## Scope

- Claim ID: `claim:32d4ab82e7394fa1`
- Scope: `source-reported assertion`
- Domain: [cross-cutting](../maps/cross-cutting.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:8c2fdbc074dbf7d4` | `local://materialized_sources/corpus/arxiv-2509.25651--2ba7699b/normalized/document.txt#L1-L4` | `materialized_sources/corpus/arxiv-2509.25651--2ba7699b/normalized/document.txt` | `full_text` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [AutoLabs: Cognitive Multi-Agent Systems with Self-Correction for Autonomous Chemical Experimentation](../sources/arxiv-2509.25651.md) — `evidenced_by`
- [Cross Cutting](../maps/cross-cutting.md) — `part_of`

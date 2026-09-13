---
uid: wiki-page:paper-vs-repository-consumption
title: Paper versus repository consumption
slug: comparisons/paper-vs-repository-consumption
page_type: comparison
status: review
summary: A comparison of TeX-first paper materialization and commit-pinned repository semanticization.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:2a05950fe0a0b64d
- claim:9243c79fad41f2cb
- claim:ae45b8d667e29552
- claim:90ae7352bb085ae8
- claim:38c95b3e2bcfcf51
- claim:d3a0d3c2f4fd45d4
- claim:1929edca74fa3fa5
- claim:55eeb2a1683b8804
- claim:ecf45fd3f4ab576a
- claim:f8088669f62de120
- claim:ef04f2ebbd2da425
- claim:419c77c89a471f8e
- claim:d38b49dc4376d4b0
- claim:1b6ae1229c17cacd
- claim:334565c7ebb30cb5
- claim:21bdaa7b130a7cc4
source_refs: &id001
- arxiv:cs/0309048
- arxiv:2505.22954
- arxiv:2408.06292
- arxiv:2402.14207
- arxiv:2502.12110
- arxiv:2501.13956
- github:jennyzzt/dgm
- github:SakanaAI/AI-Scientist
- github:getzep/graphiti
- github:xoai/sage-wiki
- github:linkml/linkml
- github:VectifyAI/OpenKB
- arxiv:2501.04227
- arxiv:2509.25651
- arxiv:2602.06855
- arxiv-2104.00405
- arxiv-1706.08840
- arxiv:2305.14627
- arxiv:2503.18102
- arxiv:2507.21046
- standard:w3c-dcat-3
- arxiv:2505.13400
- arxiv:2408.08435
- arxiv:2502.14499
- arxiv:2405.14768
- arxiv-2306.15626
- arxiv:2305.14251
- standard:apache-ossie
- arxiv:2404.14387
- arxiv:2410.04444
- arxiv:2504.08066
- arxiv:2304.05376
- standard:w3c-odrl-2.2
- arxiv:2410.05779
- arxiv:2408.15232
- arxiv:2406.06769
page_refs: []
outgoing_links: []
sections: []
temporal:
  created_at: '2026-09-13T17:43:07Z'
  updated_at: '2026-09-13T17:43:07Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-13T17:43:07Z'
provenance:
  build_id: build:v0-meta-kb-260910:88936dc16ae2c769
  generated_by_agent: agent:deterministic-v0-builder
  generated_by_model: null
  prompt_or_skill_version: deterministic-v0.1
  compiled_from_revisions: *id001
  created_at: '2026-09-13T17:43:07Z'
  updated_at: '2026-09-13T17:43:07Z'
  manual_edits_preserved: true
review:
  state: needs_human
  reviewers: []
  decision_ref: null
  checked_claim_refs: []
  unresolved_issues:
  - Scientific and semantic review required before publication.
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
    one_line: A comparison of TeX-first paper materialization and commit-pinned repository semanticization.
    short: A comparison of TeX-first paper materialization and commit-pinned repository semanticization.
    full: null
  estimated_tokens: null
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
---

# Paper versus repository consumption

| Source family | Frozen unit | Local evidence | What remains unproven |
|---|---|---|---|
| arXiv paper | source archive hash | TeX files, flattened document, line selectors | correctness and independent replication |
| GitHub repository | commit SHA | selected docs/config/code evidence and repo map | runtime behavior, benchmark claims, production reliability |
| Web/industry source | response hash | full text only when reusable; otherwise bounded excerpt | inaccessible or omitted text and source correctness |

The source adapter is part of epistemic provenance, not an interchangeable parser detail.

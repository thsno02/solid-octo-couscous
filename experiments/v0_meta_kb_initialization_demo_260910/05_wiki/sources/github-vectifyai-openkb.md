---
uid: wiki-page:source-332922100755365f
title: VectifyAI/OpenKB
slug: sources/github-vectifyai-openkb
page_type: source
status: review
summary: Candidate source page for VectifyAI/OpenKB
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:e7026275c099e7e2
- claim:714e301e8b2162bc
source_refs: &id001
- github:VectifyAI/OpenKB
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
    one_line: Candidate source page for VectifyAI/OpenKB
    short: Candidate source page for VectifyAI/OpenKB
    full: null
  estimated_tokens: null
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
---

# VectifyAI/OpenKB

- Source UID: `github:VectifyAI/OpenKB`
- Canonical ID: `VectifyAI/OpenKB`
- Source type: `github`
- Content tier: `semantic_capsule`
- Domain bucket: `ontology-semantic-architecture`
- Local document: `materialized_sources/corpus/github-VectifyAI-OpenKB--fd455ce8/document.md`

## Source-reported assertion

- Commit: `ff54396e575ee6feb0113b631a34caa082b441cc` - Default branch: `main` - Description: VectifyAI/OpenKB - Selected evidence files: 4 of 21 files observed - Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.

## Collection assessment

A CLI knowledge compiler with wiki foundation and downstream generators, hierarchical long-document retrieval, linting, source removal and skill compilation.

## Governance state

Both statements remain candidates. The source assertion is not treated as independently verified, and the collection assessment is not treated as source-authored evidence.

---
uid: wiki-page:source-e3fe88d81aab6499
title: jennyzzt/dgm
slug: sources/github-jennyzzt-dgm
page_type: source
status: review
summary: Source page for jennyzzt/dgm with claim/evidence expansion.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:1b6ae1229c17cacd
- claim:d38b49dc4376d4b0
source_refs: &id002
- github:jennyzzt/dgm
page_refs:
- wiki-page:map-recursive-self-improvement
- wiki-page:evidence-c0dc9e55b2e9b137
- wiki-page:evidence-c7e5f49d25efb6ba
outgoing_links:
- target: wiki-page:map-recursive-self-improvement
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-c0dc9e55b2e9b137
  relation: evidenced_by
  claim_refs:
  - claim:1b6ae1229c17cacd
  notes: null
- target: wiki-page:evidence-c7e5f49d25efb6ba
  relation: evidenced_by
  claim_refs:
  - claim:d38b49dc4376d4b0
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:d38b49dc4376d4b0
  source_refs:
  - github:jennyzzt/dgm
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:1b6ae1229c17cacd
  source_refs:
  - github:jennyzzt/dgm
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:096e2cb4557cf60c
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - github:jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2
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
    one_line: Source page for jennyzzt/dgm with claim/evidence expansion.
    short: Source page for jennyzzt/dgm with claim/evidence expansion.
    full: null
  estimated_tokens: 264
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:1b6ae1229c17cacd
- claim:d38b49dc4376d4b0
rights_refs: []
rights_unavailable_source_refs:
- github:jennyzzt/dgm
---

# jennyzzt/dgm

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `github:jennyzzt/dgm`
- Canonical ID: `jennyzzt/dgm`
- Source type: `github`
- Content tier: `semantic_capsule`
- Revision: `a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2`
- Domain: [recursive-self-improvement](../maps/recursive-self-improvement.md)
- Local document: `materialized_sources/corpus/github-jennyzzt-dgm--c8b75f99/evidence/files/README.md`

## Source-reported candidate statements

- Repository for **Darwin Gödel Machine (DGM)**, a novel self-improving system that iteratively modifies its own code (thereby also improving its ability to modify its own codebase) and empirically validates each change using coding benchmarks. 〔[claim:d38b49dc4376d4b0](../claims/claim-d38b49dc4376d4b0.md)〕

## Collection assessments

- One of the clearest open implementations of a system that edits its own agent code, evaluates variants, and keeps an archive instead of overwriting a single lineage. 〔[claim:1b6ae1229c17cacd](../claims/claim-1b6ae1229c17cacd.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:1b6ae1229c17cacd` | `evidence:1f00e2f956a2afe4` | `local://raw_data/githubs/jennyzzt--dgm/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:d38b49dc4376d4b0` | `evidence:86f2cb90e58dd2e2` | `local://materialized_sources/corpus/github-jennyzzt-dgm--c8b75f99/evidence/files/README.md#L14-L14` | `semantic_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Recursive Self Improvement](../maps/recursive-self-improvement.md) — `part_of`
- [Claim 1b6ae1229c17cacd](../claims/claim-1b6ae1229c17cacd.md) — `evidenced_by`
- [Claim d38b49dc4376d4b0](../claims/claim-d38b49dc4376d4b0.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### jennyzzt/dgm (`github:jennyzzt/dgm`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

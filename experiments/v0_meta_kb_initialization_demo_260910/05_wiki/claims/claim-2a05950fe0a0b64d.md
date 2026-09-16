---
uid: wiki-page:evidence-4f110bd6494e0545
title: Claim 2a05950fe0a0b64d
slug: claims/claim-2a05950fe0a0b64d
page_type: evidence
status: review
summary: 'We present the first class of mathematically rigorous, general, fully self-referential, self-improving,
  optimally efficient problem solvers. Inspired by Kurt G\" o del''s celebrated self-referential formulas (1931),
  such '
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:2a05950fe0a0b64d
source_refs: &id001
- arxiv:cs/0309048
page_refs:
- wiki-page:source-0e73b118b5b15597
- wiki-page:map-recursive-self-improvement
outgoing_links:
- target: wiki-page:source-0e73b118b5b15597
  relation: evidenced_by
  claim_refs:
  - claim:2a05950fe0a0b64d
  notes: null
- target: wiki-page:map-recursive-self-improvement
  relation: part_of
  claim_refs:
  - claim:2a05950fe0a0b64d
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:2a05950fe0a0b64d
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:2a05950fe0a0b64d
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:8d5202830938fe6b
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:cs/0309048@sha256:ab75c69deb1c4b41ae77f5f817735922ad52fc9a8d51ec5184f4978a88b4052e
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
  source_dependencies: *id001
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: 'We present the first class of mathematically rigorous, general, fully self-referential, self-improving,
      optimally efficient problem solvers. Inspired by Kurt G\" o del''s celebrated self-referential formulas (1931),
      such '
    short: 'We present the first class of mathematically rigorous, general, fully self-referential, self-improving,
      optimally efficient problem solvers. Inspired by Kurt G\" o del''s celebrated self-referential formulas (1931),
      such '
    full: null
  estimated_tokens: 281
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:2a05950fe0a0b64d
rights_refs: []
rights_unavailable_source_refs:
- arxiv:cs/0309048
---

# Source assertion from Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

We present the first class of mathematically rigorous, general, fully self-referential, self-improving, optimally efficient problem solvers. Inspired by Kurt G\" o del's celebrated self-referential formulas (1931), such a problem solver rewrites any part of its own code as soon as it has found a proof that the rewrite is useful, where the problem-dependent utility function and the hardware and the entire initial code are described by axioms encoded in an initial proof searcher which is also part of the initial code.

## Scope

- Claim ID: `claim:2a05950fe0a0b64d`
- Scope: `source-reported assertion`
- Domain: [recursive-self-improvement](../maps/recursive-self-improvement.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:fa9cf34a7b9587ca` | `local://materialized_sources/corpus/arxiv-cs-0309048--34c0ca59/normalized/document.txt#L78-L85` | `materialized_sources/corpus/arxiv-cs-0309048--34c0ca59/normalized/document.txt` | `full_text` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements](../sources/arxiv-cs-0309048.md) — `evidenced_by`
- [Recursive Self Improvement](../maps/recursive-self-improvement.md) — `part_of`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements (`arxiv:cs/0309048`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

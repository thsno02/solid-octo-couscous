---
uid: wiki-page:map-open-ended-evolution
title: Open Ended Evolution
slug: maps/open-ended-evolution
page_type: map
status: review
summary: Routing map for open ended evolution sources, questions, and claims.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:2060aa1cdd09f8bd
- claim:c16ddfd2ab0e0feb
- claim:c776b87484aab5c2
- claim:df1b88d18276a319
- claim:ecf45fd3f4ab576a
- claim:f8088669f62de120
source_refs: &id001
- arxiv:2404.14387
- arxiv:2507.21046
- arxiv:2502.12110
page_refs:
- wiki-page:source-50778f95d8e64d2e
- wiki-page:source-68be106d4fc61e3b
- wiki-page:source-1aacba116cbe3c5b
- wiki-page:knowledge-evolution-loop
- wiki-page:knowledge-frontier
outgoing_links:
- target: wiki-page:source-50778f95d8e64d2e
  relation: explains
  claim_refs:
  - claim:df1b88d18276a319
  - claim:2060aa1cdd09f8bd
  notes: null
- target: wiki-page:source-68be106d4fc61e3b
  relation: explains
  claim_refs:
  - claim:c776b87484aab5c2
  - claim:c16ddfd2ab0e0feb
  notes: null
- target: wiki-page:source-1aacba116cbe3c5b
  relation: explains
  claim_refs:
  - claim:ecf45fd3f4ab576a
  - claim:f8088669f62de120
  notes: null
- target: wiki-page:knowledge-evolution-loop
  relation: related
  claim_refs:
  - claim:2060aa1cdd09f8bd
  - claim:c16ddfd2ab0e0feb
  - claim:c776b87484aab5c2
  - claim:df1b88d18276a319
  - claim:ecf45fd3f4ab576a
  - claim:f8088669f62de120
  notes: null
- target: wiki-page:knowledge-frontier
  relation: related
  claim_refs:
  - claim:2060aa1cdd09f8bd
  - claim:c16ddfd2ab0e0feb
  - claim:c776b87484aab5c2
  - claim:df1b88d18276a319
  - claim:ecf45fd3f4ab576a
  - claim:f8088669f62de120
  notes: null
sections:
- heading: Source coverage
  claim_refs: []
  source_refs: *id001
  editorial_intent: Route by source family.
- heading: Source-reported signals
  claim_refs:
  - claim:c776b87484aab5c2
  - claim:df1b88d18276a319
  - claim:ecf45fd3f4ab576a
  source_refs:
  - arxiv:2507.21046
  - arxiv:2404.14387
  - arxiv:2502.12110
  editorial_intent: Preserve source-authored scope.
- heading: Collector assessments
  claim_refs:
  - claim:2060aa1cdd09f8bd
  - claim:c16ddfd2ab0e0feb
  - claim:f8088669f62de120
  source_refs:
  - arxiv:2404.14387
  - arxiv:2507.21046
  - arxiv:2502.12110
  editorial_intent: Preserve collector scope.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:bf1b13c8baaa32ad
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2404.14387@sha256:afd13bcb8ce6f553dec268c0fb17bfb6b8a1ba80a4881a5b46d54b927ca9a418
  - arxiv:2507.21046@sha256:4bace9b0e6528f904932b2502264e47d4c5778660cd378f68e032e5588eae432
  - arxiv:2502.12110@sha256:d112e92606a562a0369e2e8cddadad88ac8d448d66c24ee9b63e808c2c84e42b
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
    one_line: Routing map for open ended evolution sources, questions, and claims.
    short: Routing map for open ended evolution sources, questions, and claims.
    full: null
  estimated_tokens: 650
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:2060aa1cdd09f8bd
- claim:c16ddfd2ab0e0feb
- claim:c776b87484aab5c2
- claim:df1b88d18276a319
- claim:ecf45fd3f4ab576a
- claim:f8088669f62de120
rights_refs: []
rights_unavailable_source_refs:
- arxiv:2404.14387
- arxiv:2502.12110
- arxiv:2507.21046
---

# Open Ended Evolution

Processes that retain diversity, novelty, archives, and expanding repertoires.

## Routing questions

- What varies and what is retained?
- How does an archive prevent destructive forgetting?
- What keeps the process open-ended?

## Source coverage

| Source | Type | Tier | Claims |
|---|---|---|---|
| [A Survey on Self-Evolution of Large Language Models](../sources/arxiv-2404.14387.md) | `arxiv` | `full_text` | 2 |
| [A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence](../sources/arxiv-2507.21046.md) | `arxiv` | `full_text` | 2 |
| [A-MEM: Agentic Memory for LLM Agents](../sources/arxiv-2502.12110.md) | `arxiv` | `full_text` | 2 |

## Source-reported signals

- **A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence** (source assertion): Large Language Models (LLMs) have demonstrated remarkable capabilities across diverse tasks but remain fundamentally static, unable to adapt their internal parameters to novel tasks, evolving knowledge domains, or dynamic interaction contexts. As LLMs are increasingly deployed in open-ended, interactive environments, this static nature has become a critical bottleneck, necessitating agents that can adaptively reason, 〔[claim:c776b87484aab5c2](../claims/claim-c776b87484aab5c2.md)〕
- **A Survey on Self-Evolution of Large Language Models** (source assertion): Large language models (LLMs) have significantly advanced in various fields and intelligent agent applications. However, current LLMs that learn from human or external model supervision are costly and may face performance ceilings as task complexity and diversity increase. 〔[claim:df1b88d18276a319](../claims/claim-df1b88d18276a319.md)〕
- **A-MEM: Agentic Memory for LLM Agents** (source assertion): While large language model (LLM) agents can effectively use external tools for complex real-world tasks, they require memory systems to leverage historical experiences. Current memory systems enable basic storage and retrieval but lack sophisticated memory organization, despite recent attempts to incorporate graph databases. 〔[claim:ecf45fd3f4ab576a](../claims/claim-ecf45fd3f4ab576a.md)〕

## Collector assessments

- **A Survey on Self-Evolution of Large Language Models** (collection assessment): Provides a useful process decomposition of LLM self-evolution into experience acquisition, experience refinement, updating, and evaluation; a natural reference taxonomy for later knowledge self-evolution pipelines. 〔[claim:2060aa1cdd09f8bd](../claims/claim-2060aa1cdd09f8bd.md)〕
- **A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence** (collection assessment): A broad taxonomy of self-evolving agents organized around what, when, how, and where to evolve, spanning model, memory, tool, and architecture changes. 〔[claim:c16ddfd2ab0e0feb](../claims/claim-c16ddfd2ab0e0feb.md)〕
- **A-MEM: Agentic Memory for LLM Agents** (collection assessment): Directly studies memory evolution: newly added memories can update contextual representations and attributes of historical memories, continuously refining the memory network. 〔[claim:f8088669f62de120](../claims/claim-f8088669f62de120.md)〕

## Current synthesis boundary

The map routes candidate evidence; it does not flatten sources into consensus or resolve contradictions automatically.

## Related pages

- [A Survey on Self-Evolution of Large Language Models](../sources/arxiv-2404.14387.md) — `explains`
- [A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence](../sources/arxiv-2507.21046.md) — `explains`
- [A-MEM: Agentic Memory for LLM Agents](../sources/arxiv-2502.12110.md) — `explains`
- [Knowledge evolution loop](../concepts/knowledge-evolution-loop.md) — `related`
- [Knowledge frontier](../research_questions/knowledge-frontier.md) — `related`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### A Survey on Self-Evolution of Large Language Models (`arxiv:2404.14387`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### A-MEM: Agentic Memory for LLM Agents (`arxiv:2502.12110`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence (`arxiv:2507.21046`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

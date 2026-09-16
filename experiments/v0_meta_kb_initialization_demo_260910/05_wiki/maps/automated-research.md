---
uid: wiki-page:map-automated-research
title: Automated Research
slug: maps/automated-research
page_type: map
status: review
summary: Routing map for automated research sources, questions, and claims.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:2f8ebd974fc7b5fd
- claim:38c95b3e2bcfcf51
- claim:3c6cef89711e89f2
- claim:3d07597b1776b0bd
- claim:852bc42ef50e89c7
- claim:8798b3dc1ae125ea
- claim:9077f46d7f30e565
- claim:d3a0d3c2f4fd45d4
source_refs: &id001
- arxiv:2501.04227
- arxiv:2408.06292
- arxiv:2505.13400
- arxiv:2504.08066
page_refs:
- wiki-page:source-5c69a674d903b543
- wiki-page:source-c1dbc9c2a83a564a
- wiki-page:source-0e32ebb2e855fd30
- wiki-page:source-1203e0209022f228
- wiki-page:automation-vs-editorial-review
- wiki-page:knowledge-evolution-loop
outgoing_links:
- target: wiki-page:source-5c69a674d903b543
  relation: explains
  claim_refs:
  - claim:2f8ebd974fc7b5fd
  - claim:3d07597b1776b0bd
  notes: null
- target: wiki-page:source-c1dbc9c2a83a564a
  relation: explains
  claim_refs:
  - claim:38c95b3e2bcfcf51
  - claim:d3a0d3c2f4fd45d4
  notes: null
- target: wiki-page:source-0e32ebb2e855fd30
  relation: explains
  claim_refs:
  - claim:3c6cef89711e89f2
  - claim:852bc42ef50e89c7
  notes: null
- target: wiki-page:source-1203e0209022f228
  relation: explains
  claim_refs:
  - claim:9077f46d7f30e565
  - claim:8798b3dc1ae125ea
  notes: null
- target: wiki-page:automation-vs-editorial-review
  relation: related
  claim_refs:
  - claim:2f8ebd974fc7b5fd
  - claim:38c95b3e2bcfcf51
  - claim:3c6cef89711e89f2
  - claim:3d07597b1776b0bd
  - claim:852bc42ef50e89c7
  - claim:8798b3dc1ae125ea
  notes: null
- target: wiki-page:knowledge-evolution-loop
  relation: related
  claim_refs:
  - claim:2f8ebd974fc7b5fd
  - claim:38c95b3e2bcfcf51
  - claim:3c6cef89711e89f2
  - claim:3d07597b1776b0bd
  - claim:852bc42ef50e89c7
  - claim:8798b3dc1ae125ea
  notes: null
sections:
- heading: Source coverage
  claim_refs: []
  source_refs: *id001
  editorial_intent: Route by source family.
- heading: Source-reported signals
  claim_refs:
  - claim:2f8ebd974fc7b5fd
  - claim:38c95b3e2bcfcf51
  - claim:3c6cef89711e89f2
  - claim:9077f46d7f30e565
  source_refs:
  - arxiv:2501.04227
  - arxiv:2408.06292
  - arxiv:2505.13400
  - arxiv:2504.08066
  editorial_intent: Preserve source-authored scope.
- heading: Collector assessments
  claim_refs:
  - claim:3d07597b1776b0bd
  - claim:852bc42ef50e89c7
  - claim:8798b3dc1ae125ea
  - claim:d3a0d3c2f4fd45d4
  source_refs:
  - arxiv:2501.04227
  - arxiv:2505.13400
  - arxiv:2504.08066
  - arxiv:2408.06292
  editorial_intent: Preserve collector scope.
temporal:
  created_at: '2026-09-13T17:38:21Z'
  updated_at: '2026-09-13T17:38:21Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-13T17:38:21Z'
provenance:
  build_id: build:llm-wiki-v0:9c2a89d879277c9e
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2501.04227@sha256:1b28bfd8ca8a9dcb1930f7fcd49164300a984bd1abf533d3d28b475fe7dd7f85
  - arxiv:2408.06292@sha256:4ddccff8b6e49dec4c7bb219d4330f1faf47255b5b1b33d01f207eae23e119e9
  - arxiv:2505.13400@sha256:1abd0b99271884b6f1a8fd9db0185e8042f079a61879ec0c9a7febae6a0c942c
  - arxiv:2504.08066@sha256:ea458b4c4212b9e61d909193504485986780026a962727da8669877f6f76740e
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
  source_dependencies: *id001
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: Routing map for automated research sources, questions, and claims.
    short: Routing map for automated research sources, questions, and claims.
    full: null
  estimated_tokens: 532
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Automated Research

Automated research systems and their evidence, evaluation, and governance.

## Routing questions

- Which research stages are automated?
- How are experiments and negative results retained?
- What prevents unsupported research narratives?

## Source coverage

| Source | Type | Tier | Claims |
|---|---|---|---|
| [Agent Laboratory: Using LLM Agents as Research Assistants](../sources/arxiv-2501.04227.md) | `arxiv` | `full_text` | 2 |
| [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](../sources/arxiv-2408.06292.md) | `arxiv` | `full_text` | 2 |
| [Robin: A multi-agent system for automating scientific discovery](../sources/arxiv-2505.13400.md) | `arxiv` | `full_text` | 2 |
| [The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search](../sources/arxiv-2504.08066.md) | `arxiv` | `full_text` | 2 |

## Source-reported signals

- **Agent Laboratory: Using LLM Agents as Research Assistants** (source assertion): Historically, scientific discovery has been a lengthy and costly process, demanding substantial time and resources from initial conception to final results. 〔[claim:2f8ebd974fc7b5fd](../claims/claim-2f8ebd974fc7b5fd.md)〕
- **The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery** (source assertion): One of the grand challenges of artificial general intelligence is developing agents capable of conducting scientific research and discovering new knowledge. While frontier models have already been used as aides to human scientists, e.g. 〔[claim:38c95b3e2bcfcf51](../claims/claim-38c95b3e2bcfcf51.md)〕
- **Robin: A multi-agent system for automating scientific discovery** (source assertion): Scientific discovery is driven by the iterative process of background research, hypothesis generation, experimentation, and data analysis. Despite recent advancements in applying artificial intelligence to scientific discovery, no system has yet automated all of these stages in a single workflow. 〔[claim:3c6cef89711e89f2](../claims/claim-3c6cef89711e89f2.md)〕
- **The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search** (source assertion): AI is increasingly playing a pivotal role in transforming how scientific discoveries are made. We introduce , an end-to-end agentic system capable of producing the first entirely AI-generated peer-review-accepted workshop paper. 〔[claim:9077f46d7f30e565](../claims/claim-9077f46d7f30e565.md)〕

## Collector assessments

- **Agent Laboratory: Using LLM Agents as Research Assistants** (collection assessment): A practical end-to-end autonomous research workflow spanning literature review, experimentation and report writing, with explicit human feedback points. 〔[claim:3d07597b1776b0bd](../claims/claim-3d07597b1776b0bd.md)〕
- **Robin: A multi-agent system for automating scientific discovery** (collection assessment): One of the strongest demonstrations of a lab-in-the-loop discovery cycle: background research, hypothesis generation, experimental planning, human-executed wet-lab experiments, data analysis, and updated hypotheses. 〔[claim:852bc42ef50e89c7](../claims/claim-852bc42ef50e89c7.md)〕
- **The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search** (collection assessment): End-to-end autonomous scientific discovery without a fixed human-authored template. Iteratively formulates hypotheses, designs and executes experiments, analyzes results, and writes papers using an agentic tree-search process. 〔[claim:8798b3dc1ae125ea](../claims/claim-8798b3dc1ae125ea.md)〕
- **The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery** (collection assessment): Extends self-evolution from improving an agent to automating the research loop itself: idea generation, implementation, experiment, paper writing, and automated review can be iterated to create new knowledge. 〔[claim:d3a0d3c2f4fd45d4](../claims/claim-d3a0d3c2f4fd45d4.md)〕

## Current synthesis boundary

The map routes candidate evidence; it does not flatten sources into consensus or resolve contradictions automatically.

## Related pages

- [Agent Laboratory: Using LLM Agents as Research Assistants](../sources/arxiv-2501.04227.md) — `explains`
- [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](../sources/arxiv-2408.06292.md) — `explains`
- [Robin: A multi-agent system for automating scientific discovery](../sources/arxiv-2505.13400.md) — `explains`
- [The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search](../sources/arxiv-2504.08066.md) — `explains`
- [Automation versus editorial review](../debates/automation-editorial-review.md) — `related`
- [Knowledge evolution loop](../concepts/knowledge-evolution-loop.md) — `related`

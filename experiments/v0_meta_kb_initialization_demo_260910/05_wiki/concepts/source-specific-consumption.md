---
uid: wiki-page:source-specific-consumption
title: Source-specific consumption
slug: concepts/source-specific-consumption
page_type: concept
status: review
summary: Different source families require different frozen units and selectors.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id002
- claim:2f8ebd974fc7b5fd
- claim:38c95b3e2bcfcf51
- claim:3c6cef89711e89f2
- claim:9077f46d7f30e565
- claim:0d2b54965305cf83
- claim:32d4ab82e7394fa1
- claim:334565c7ebb30cb5
- claim:a7845ddab7913b4f
- claim:4bf5ea8e6b4e37de
- claim:84c91602bd1dfb78
- claim:ecdd2719fa55751c
- claim:4715a4ff3b1706fd
source_refs: &id001
- arxiv:2501.04227
- arxiv:2408.06292
- arxiv:2505.13400
- arxiv:2504.08066
- arxiv:2408.08435
- arxiv:2509.25651
- github:SakanaAI/AI-Scientist
- arxiv:1905.10985
- arxiv:2502.14499
- arxiv:2406.06769
- arxiv:2602.06855
- arxiv-2104.00405
page_refs: []
outgoing_links: []
sections:
- heading: Purpose
  claim_refs: []
  source_refs: *id001
  editorial_intent: State the page's editorial purpose.
- heading: Candidate evidence
  claim_refs: *id002
  source_refs: *id001
  editorial_intent: Expose claim-backed signals without automatic admission.
- heading: Review boundary
  claim_refs: []
  source_refs: *id001
  editorial_intent: Declare unresolved review work.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:487f888f4db7dee3
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2501.04227@sha256:1b28bfd8ca8a9dcb1930f7fcd49164300a984bd1abf533d3d28b475fe7dd7f85
  - arxiv:2408.06292@sha256:4ddccff8b6e49dec4c7bb219d4330f1faf47255b5b1b33d01f207eae23e119e9
  - arxiv:2505.13400@sha256:1abd0b99271884b6f1a8fd9db0185e8042f079a61879ec0c9a7febae6a0c942c
  - arxiv:2504.08066@sha256:ea458b4c4212b9e61d909193504485986780026a962727da8669877f6f76740e
  - arxiv:2408.08435@sha256:9e5b2a49f62b2d5218e018666a195c85fc5d186d3939e0070303fab4fb7622e2
  - arxiv:2509.25651@sha256:14424738e0ad14b8fd5891102b89d9a3e4888beb22605f723e1cc044231eb803
  - github:SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb
  - arxiv:1905.10985@sha256:6afa7771c29f7a9a5659d73e62b83cfefb39516d30ae99172e2ad373dafd45e5
  - arxiv:2502.14499@sha256:de8bc15be762914dd2f056f00efe2b83d51ce852a7035d65e866e6cdecbbb65a
  - arxiv:2406.06769@sha256:cb1d6ccc88eb66af69e71730a5c488234ff4fe8af04ba04081b5a445f4d39b3e
  - arxiv:2602.06855@sha256:ac1ba940f1bdc54e012cc384c428f78bd01d50d7a947f052117944c03e790d9a
  - arxiv-2104.00405@sha256:d9ca19652574908e954b524249d31a8b450830023739ee49797f58d52784dd03
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
    one_line: Different source families require different frozen units and selectors.
    short: Different source families require different frozen units and selectors.
    full: null
  estimated_tokens: 711
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Source-specific consumption

## Purpose

Different source families require different frozen units and selectors.

## Candidate evidence

- **Agent Laboratory: Using LLM Agents as Research Assistants** (source assertion): Historically, scientific discovery has been a lengthy and costly process, demanding substantial time and resources from initial conception to final results. 〔[claim:2f8ebd974fc7b5fd](../claims/claim-2f8ebd974fc7b5fd.md)〕
- **The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery** (source assertion): One of the grand challenges of artificial general intelligence is developing agents capable of conducting scientific research and discovering new knowledge. While frontier models have already been used as aides to human scientists, e.g. 〔[claim:38c95b3e2bcfcf51](../claims/claim-38c95b3e2bcfcf51.md)〕
- **Robin: A multi-agent system for automating scientific discovery** (source assertion): Scientific discovery is driven by the iterative process of background research, hypothesis generation, experimentation, and data analysis. Despite recent advancements in applying artificial intelligence to scientific discovery, no system has yet automated all of these stages in a single workflow. 〔[claim:3c6cef89711e89f2](../claims/claim-3c6cef89711e89f2.md)〕
- **The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search** (source assertion): AI is increasingly playing a pivotal role in transforming how scientific discoveries are made. We introduce , an end-to-end agentic system capable of producing the first entirely AI-generated peer-review-accepted workshop paper. 〔[claim:9077f46d7f30e565](../claims/claim-9077f46d7f30e565.md)〕
- **Automated Design of Agentic Systems** (source assertion): Researchers are investing substantial effort in developing powerful general-purpose agents, wherein Foundation Models are used as modules within agentic systems (e.g. Chain-of-Thought, Self-Reflection, Toolformer). 〔[claim:0d2b54965305cf83](../claims/claim-0d2b54965305cf83.md)〕
- **AutoLabs: Cognitive Multi-Agent Systems with Self-Correction for Autonomous Chemical Experimentation** (source assertion): The automation of chemical research through self-driving laboratories (SDLs) promises to accelerate scientific discovery, yet the reliability and granular performance of the underlying AI agents remain critical, under-examined challenges. In this work, we introduce AutoLabs, a self-correcting, multi-agent architecture designed to autonomously translate natural-language instructions into executable protocols for a hig 〔[claim:32d4ab82e7394fa1](../claims/claim-32d4ab82e7394fa1.md)〕
- **SakanaAI/AI-Scientist** (source assertion): One of the grand challenges of artificial intelligence is developing agents capable of conducting scientific research and discovering new knowledge. 〔[claim:334565c7ebb30cb5](../claims/claim-334565c7ebb30cb5.md)〕
- **AI-GAs: AI-generating algorithms, an alternate paradigm for producing general artificial intelligence** (source assertion): Perhaps the most ambitious scientific quest in human history is the creation of general artificial intelligence, which roughly means AI that is as smart or smarter than humans. The dominant approach in the machine learning community is to attempt to discover each of the pieces that might be required for intelligence, with the implicit assumption that at some point in the future some group will complete the Herculean  〔[claim:a7845ddab7913b4f](../claims/claim-a7845ddab7913b4f.md)〕
- **MLGym: A New Framework and Benchmark for Advancing AI Research Agents** (source assertion): We introduce Meta and -Bench, a new framework and benchmark for evaluating and developing LLM agents on AI research tasks. This is the first Gym environment for machine learning (ML) tasks, enabling research on reinforcement learning (RL) algorithms for training such agents. 〔[claim:4bf5ea8e6b4e37de](../claims/claim-4bf5ea8e6b4e37de.md)〕
- **DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents** (source assertion): Automated scientific discovery promises to accelerate progress across scientific domains. However, developing and evaluating an AI agent's capacity for end-to-end scientific reasoning is challenging as running real-world experiments is often prohibitively expensive or infeasible. 〔[claim:84c91602bd1dfb78](../claims/claim-84c91602bd1dfb78.md)〕
- **AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents** (source assertion): LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we introduce ~(the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine learning papers. 〔[claim:ecdd2719fa55751c](../claims/claim-ecdd2719fa55751c.md)〕
- **Avalanche: an End-to-End Library for Continual Learning** (source assertion): Learning continually from non-stationary data streams is a long-standing goal and a challenging problem in machine learning. Recently, we have witnessed a renewed and fast-growing interest in continual learning, especially within the deep learning community. 〔[claim:4715a4ff3b1706fd](../claims/claim-4715a4ff3b1706fd.md)〕

## Compiled interpretation

This page reorganizes candidate knowledge around a stable reader task. It is not source concatenation and it does not turn retrieval, maintainer claims, preprints, or generated prose into verified truth.

## Review boundary

Check evidence entailment, source independence, contradiction, neutrality, due weight, freshness, and downstream impact before publication.

## Frozen units

| Source family | Frozen unit | Evidence surface | Still unproven |
|---|---|---|---|
| paper | archive/hash | TeX or normalized lines | correctness and replication |
| repository | commit SHA | selected docs/config/code | runtime and benchmark behavior |
| web/industry | response hash | reusable text or bounded excerpt | inaccessible/omitted content |

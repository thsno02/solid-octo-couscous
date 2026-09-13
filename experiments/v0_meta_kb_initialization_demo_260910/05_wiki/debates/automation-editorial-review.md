---
uid: wiki-page:automation-vs-editorial-review
title: Automation versus editorial review
slug: debates/automation-editorial-review
page_type: debate
status: review
summary: Automation accelerates research and writing but requires independent evidence and governance gates.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id002
- claim:2f8ebd974fc7b5fd
- claim:38c95b3e2bcfcf51
- claim:3c6cef89711e89f2
- claim:9077f46d7f30e565
- claim:4bf5ea8e6b4e37de
- claim:dcf2fa8645f61032
- claim:ecdd2719fa55751c
- claim:1929edca74fa3fa5
- claim:b281f7d7bc21b10d
- claim:bed2f056ecd73c69
- claim:d9cc223138eb5da3
- claim:e7ac7da9ac39e47d
source_refs: &id001
- arxiv:2501.04227
- arxiv:2408.06292
- arxiv:2505.13400
- arxiv:2504.08066
- arxiv:2502.14499
- standard:w3c-odrl-2.2
- arxiv:2602.06855
- arxiv:2402.14207
- arxiv:2305.14251
- arxiv:2305.14627
- arxiv:2408.15232
- github:xoai/sage-wiki
page_refs:
- wiki-page:map-automated-research
- wiki-page:map-governance-evaluation
- wiki-page:v0-quality-gates
outgoing_links:
- target: wiki-page:map-automated-research
  relation: related
  claim_refs:
  - claim:2f8ebd974fc7b5fd
  - claim:38c95b3e2bcfcf51
  - claim:3c6cef89711e89f2
  - claim:9077f46d7f30e565
  - claim:4bf5ea8e6b4e37de
  - claim:dcf2fa8645f61032
  notes: null
- target: wiki-page:map-governance-evaluation
  relation: related
  claim_refs:
  - claim:2f8ebd974fc7b5fd
  - claim:38c95b3e2bcfcf51
  - claim:3c6cef89711e89f2
  - claim:9077f46d7f30e565
  - claim:4bf5ea8e6b4e37de
  - claim:dcf2fa8645f61032
  notes: null
- target: wiki-page:v0-quality-gates
  relation: evaluates
  claim_refs:
  - claim:2f8ebd974fc7b5fd
  - claim:38c95b3e2bcfcf51
  - claim:3c6cef89711e89f2
  - claim:9077f46d7f30e565
  - claim:4bf5ea8e6b4e37de
  - claim:dcf2fa8645f61032
  notes: null
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
  - arxiv:2501.04227@sha256:1b28bfd8ca8a9dcb1930f7fcd49164300a984bd1abf533d3d28b475fe7dd7f85
  - arxiv:2408.06292@sha256:4ddccff8b6e49dec4c7bb219d4330f1faf47255b5b1b33d01f207eae23e119e9
  - arxiv:2505.13400@sha256:1abd0b99271884b6f1a8fd9db0185e8042f079a61879ec0c9a7febae6a0c942c
  - arxiv:2504.08066@sha256:ea458b4c4212b9e61d909193504485986780026a962727da8669877f6f76740e
  - arxiv:2502.14499@sha256:de8bc15be762914dd2f056f00efe2b83d51ce852a7035d65e866e6cdecbbb65a
  - standard:w3c-odrl-2.2@sha256:af187a2c26b2429a579039403f34d9a5d5f29a1e01019662043068fa1ca2beaa
  - arxiv:2602.06855@sha256:ac1ba940f1bdc54e012cc384c428f78bd01d50d7a947f052117944c03e790d9a
  - arxiv:2402.14207@sha256:28b57e9821da798bf8ccfa3f144bfa37cd96ff3582c2211c83eff5ffcf0ccfc2
  - arxiv:2305.14251@sha256:57414a8d80031dceed44fb17efa562cab7e1490390ce95d8753480fba9686795
  - arxiv:2305.14627@sha256:6902aae852b39f761a60dc2cf36b7d2ed9e615755f413b7daa8b52f5c1eae3ea
  - arxiv:2408.15232@sha256:19f115dc7b47921012b68ca5b991bf5f63c5b5ca54f3faddf895ea8e963b54fa
  - github:xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d
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
    one_line: Automation accelerates research and writing but requires independent evidence and governance gates.
    short: Automation accelerates research and writing but requires independent evidence and governance gates.
    full: null
  estimated_tokens: 740
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Automation versus editorial review

## Purpose

Automation accelerates research and writing but requires independent evidence and governance gates.

## Candidate evidence

- **Agent Laboratory: Using LLM Agents as Research Assistants** (source assertion): Historically, scientific discovery has been a lengthy and costly process, demanding substantial time and resources from initial conception to final results. To accelerate scientific discovery, reduce research costs, and improve research quality, we introduce Agent Laboratory , an autonomous LLM-based framework capable of completing the entire research process. 〔[claim:2f8ebd974fc7b5fd](../claims/claim-2f8ebd974fc7b5fd.md)〕
- **The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery** (source assertion): One of the grand challenges of artificial general intelligence is developing agents capable of conducting scientific research and discovering new knowledge. While frontier models have already been used as aides to human scientists, e.g. 〔[claim:38c95b3e2bcfcf51](../claims/claim-38c95b3e2bcfcf51.md)〕
- **Robin: A multi-agent system for automating scientific discovery** (source assertion): Scientific discovery is driven by the iterative process of background research, hypothesis generation, experimentation, and data analysis. Despite recent advancements in applying artificial intelligence to scientific discovery, no system has yet automated all of these stages in a single workflow. 〔[claim:3c6cef89711e89f2](../claims/claim-3c6cef89711e89f2.md)〕
- **The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search** (source assertion): AI is increasingly playing a pivotal role in transforming how scientific discoveries are made. We introduce , an end-to-end agentic system capable of producing the first entirely AI-generated peer-review-accepted workshop paper. 〔[claim:9077f46d7f30e565](../claims/claim-9077f46d7f30e565.md)〕
- **MLGym: A New Framework and Benchmark for Advancing AI Research Agents** (source assertion): amssymb amsmath adjustbox soul enumitem booktabs color xcolor bbding listings multicol xspace lmodern tablefootnote 〔[claim:4bf5ea8e6b4e37de](../claims/claim-4bf5ea8e6b4e37de.md)〕
- **ODRL Information Model 2.2** (source assertion): The Open Digital Rights Language (ODRL) is a policy expression language that provides a flexible and interoperable information model, vocabulary, and encoding mechanisms for representing statements about the usage of content and services. The ODRL Information Model describes the underlying concepts, entities, and relationships that form the foundational basis for the semantics of the ODRL policies. 〔[claim:dcf2fa8645f61032](../claims/claim-dcf2fa8645f61032.md)〕
- **AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents** (source assertion): graphicx booktabs makecell subcaption hyperref url array xcolor tikz calc xcolor amssymb comment lipsum enumitem multirow xcolor caption pifont xcolor longtable 〔[claim:ecdd2719fa55751c](../claims/claim-ecdd2719fa55751c.md)〕
- **Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models** (source assertion): We study how to apply large language models to write grounded and organized long-form articles from scratch, with comparable breadth and depth to Wikipedia pages. This underexplored problem poses new challenges at the pre-writing stage, including how to research the topic and prepare an outline prior to writing. 〔[claim:1929edca74fa3fa5](../claims/claim-1929edca74fa3fa5.md)〕
- **FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation** (source assertion): Evaluating the factuality of long-form text generated by large language models (LMs) is non-trivial because (1) generations often contain a mixture of supported and unsupported pieces of information, making binary judgments of quality inadequate, and (2) human evaluation is time-consuming and costly. 〔[claim:b281f7d7bc21b10d](../claims/claim-b281f7d7bc21b10d.md)〕
- **Enabling Large Language Models to Generate Text with Citations** (source assertion): Large language models (LLMs) have emerged as a widely-used tool for information seeking, but their generated outputs are prone to hallucination. In this work, our aim is to allow LLMs to generate text with citations , improving their factual correctness and verifiability. 〔[claim:bed2f056ecd73c69](../claims/claim-bed2f056ecd73c69.md)〕
- **Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations** (source assertion): While language model (LM)-powered chatbots and generative search engines excel at answering concrete queries, discovering information in the terrain of unknown unknowns remains challenging for users. To emulate the common educational scenario where children/students learn by listening to and participating in conversations with their parents/teachers, we create Collaborative STORM ( ). 〔[claim:d9cc223138eb5da3](../claims/claim-d9cc223138eb5da3.md)〕
- **xoai/sage-wiki** (source assertion): - Commit: `ab36031ace701fb1e3c620323d138a90a450f48d` - Default branch: `main` - Description: xoai/sage-wiki - Selected evidence files: 4 of 21 files observed - Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven. 〔[claim:e7ac7da9ac39e47d](../claims/claim-e7ac7da9ac39e47d.md)〕

## Compiled interpretation

This page reorganizes candidate knowledge around a stable reader task. It is not source concatenation and it does not turn retrieval, maintainer claims, preprints, or generated prose into verified truth.

## Review boundary

Check evidence entailment, source independence, contradiction, neutrality, due weight, freshness, and downstream impact before publication.

## Preserved disagreement

Automation is useful for perspective discovery, extraction, planning, drafting, and linting. Independent review remains necessary for identity merges, contested claims, source retractions, policy-sensitive content, and trust promotion.

## Related pages

- [Automated Research](../maps/automated-research.md) — `related`
- [Governance Evaluation](../maps/governance-evaluation.md) — `related`
- [v0 LLM Wiki quality gates](../evaluations/v0-quality-gates.md) — `evaluates`

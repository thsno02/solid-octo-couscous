---
uid: wiki-page:grounded-long-form-synthesis
title: Grounded long-form synthesis
slug: methods/grounded-synthesis
page_type: method
status: review
summary: Research-before-writing, outline-first compilation, citations, and factuality checks.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id002
- claim:1929edca74fa3fa5
- claim:b281f7d7bc21b10d
- claim:bc9a34bd8a9c7154
- claim:bed2f056ecd73c69
- claim:e7026275c099e7e2
- claim:e7ac7da9ac39e47d
- claim:55eeb2a1683b8804
- claim:6f5fa83ca484f664
- claim:714e301e8b2162bc
- claim:9a3b21da11a96956
- claim:9f0a3dc6de4c7f84
- claim:c4f2def09ea56d98
source_refs: &id001
- arxiv:2402.14207
- arxiv:2305.14251
- arxiv:2509.23233
- arxiv:2305.14627
- github:VectifyAI/OpenKB
- github:xoai/sage-wiki
page_refs:
- wiki-page:map-llm-wiki
- wiki-page:epistemic-separation
- wiki-page:v0-quality-gates
outgoing_links:
- target: wiki-page:map-llm-wiki
  relation: part_of
  claim_refs:
  - claim:1929edca74fa3fa5
  - claim:b281f7d7bc21b10d
  - claim:bc9a34bd8a9c7154
  - claim:bed2f056ecd73c69
  - claim:e7026275c099e7e2
  - claim:e7ac7da9ac39e47d
  notes: null
- target: wiki-page:epistemic-separation
  relation: depends_on
  claim_refs:
  - claim:1929edca74fa3fa5
  - claim:b281f7d7bc21b10d
  - claim:bc9a34bd8a9c7154
  - claim:bed2f056ecd73c69
  - claim:e7026275c099e7e2
  - claim:e7ac7da9ac39e47d
  notes: null
- target: wiki-page:v0-quality-gates
  relation: evaluates
  claim_refs:
  - claim:1929edca74fa3fa5
  - claim:b281f7d7bc21b10d
  - claim:bc9a34bd8a9c7154
  - claim:bed2f056ecd73c69
  - claim:e7026275c099e7e2
  - claim:e7ac7da9ac39e47d
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
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:aad2073b7a3459ff
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2402.14207@sha256:28b57e9821da798bf8ccfa3f144bfa37cd96ff3582c2211c83eff5ffcf0ccfc2
  - arxiv:2305.14251@sha256:57414a8d80031dceed44fb17efa562cab7e1490390ce95d8753480fba9686795
  - arxiv:2509.23233@sha256:8570de4224cfc829f7478411feca2ecec5f50d6e7ceb7cc62fd15fa07f20c921
  - arxiv:2305.14627@sha256:6902aae852b39f761a60dc2cf36b7d2ed9e615755f413b7daa8b52f5c1eae3ea
  - github:VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc
  - github:xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d
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
    one_line: Research-before-writing, outline-first compilation, citations, and factuality checks.
    short: Research-before-writing, outline-first compilation, citations, and factuality checks.
    full: null
  estimated_tokens: 993
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:1929edca74fa3fa5
- claim:b281f7d7bc21b10d
- claim:bc9a34bd8a9c7154
- claim:bed2f056ecd73c69
- claim:e7026275c099e7e2
- claim:e7ac7da9ac39e47d
- claim:55eeb2a1683b8804
- claim:6f5fa83ca484f664
- claim:714e301e8b2162bc
- claim:9a3b21da11a96956
- claim:9f0a3dc6de4c7f84
- claim:c4f2def09ea56d98
rights_refs: []
rights_unavailable_source_refs:
- arxiv:2305.14251
- arxiv:2305.14627
- arxiv:2402.14207
- arxiv:2509.23233
- github:VectifyAI/OpenKB
- github:xoai/sage-wiki
---

# Grounded long-form synthesis

## Purpose

Research-before-writing, outline-first compilation, citations, and factuality checks.

## Candidate evidence

- **Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models** (source assertion): We study how to apply large language models to write grounded and organized long-form articles from scratch, with comparable breadth and depth to Wikipedia pages. This underexplored problem poses new challenges at the pre-writing stage, including how to research the topic and prepare an outline prior to writing. 〔[claim:1929edca74fa3fa5](../claims/claim-1929edca74fa3fa5.md)〕
- **FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation** (source assertion): Evaluating the factuality of long-form text generated by large language models (LMs) is non-trivial because (1) generations often contain a mixture of supported and unsupported pieces of information, making binary judgments of quality inadequate, and (2) human evaluation is time-consuming and costly. In this paper, we introduce , a new evaluation that breaks a generation into a series of atomic facts and computes the 〔[claim:b281f7d7bc21b10d](../claims/claim-b281f7d7bc21b10d.md)〕
- **Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models** (source assertion): Wikipedia is the largest open knowledge corpus, widely used worldwide and serving as a key resource for training large language models (LLMs) and retrieval-augmented generation (RAG) systems. Ensuring its accuracy is therefore critical. 〔[claim:bc9a34bd8a9c7154](../claims/claim-bc9a34bd8a9c7154.md)〕
- **Enabling Large Language Models to Generate Text with Citations** (source assertion): Large language models (LLMs) have emerged as a widely-used tool for information seeking, but their generated outputs are prone to hallucination. In this work, our aim is to allow LLMs to generate text with citations , improving their factual correctness and verifiability. 〔[claim:bed2f056ecd73c69](../claims/claim-bed2f056ecd73c69.md)〕
- **VectifyAI/OpenKB** (source assertion): **OpenKB (Open Knowledge Base)** is an open-source system (in CLI) that compiles raw documents into a structured, interlinked wiki-style knowledge base using LLMs, powered by [**PageIndex**](https://github.com/VectifyAI/PageIndex)'s vectorless, reasoning-based retrieval for long documents. 〔[claim:e7026275c099e7e2](../claims/claim-e7026275c099e7e2.md)〕
- **xoai/sage-wiki** (source assertion): **sage-wiki** is a graph memory and knowledge base that AI agents and humans build and query together. Drop in documents; an LLM compiler turns them into an interlinked wiki with a knowledge graph — agents query it through MCP, humans browse it as plain markdown. 〔[claim:e7ac7da9ac39e47d](../claims/claim-e7ac7da9ac39e47d.md)〕
- **Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models** (collection assessment): STORM is a central academic reference for multi-perspective research, outline construction, grounded long-form synthesis, and editor-informed evaluation. 〔[claim:55eeb2a1683b8804](../claims/claim-55eeb2a1683b8804.md)〕
- **Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models** (collection assessment): CLAIRE and WikiCollide make corpus-level inconsistency detection a first-class maintenance task and demonstrate human-editor review as part of the loop. 〔[claim:6f5fa83ca484f664](../claims/claim-6f5fa83ca484f664.md)〕
- **VectifyAI/OpenKB** (collection assessment): A CLI knowledge compiler with wiki foundation and downstream generators, hierarchical long-document retrieval, linting, source removal and skill compilation. 〔[claim:714e301e8b2162bc](../claims/claim-714e301e8b2162bc.md)〕
- **Enabling Large Language Models to Generate Text with Citations** (collection assessment): ALCE provides reproducible citation-quality metrics across correctness, completeness, and fluency, directly applicable to wiki admission gates. 〔[claim:9a3b21da11a96956](../claims/claim-9a3b21da11a96956.md)〕
- **FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation** (collection assessment): Supplies an atomic-fact evaluation primitive needed to assess factual precision of long-form wiki pages rather than judging a page as one block. 〔[claim:9f0a3dc6de4c7f84](../claims/claim-9f0a3dc6de4c7f84.md)〕
- **xoai/sage-wiki** (collection assessment): A graph-aware compiled wiki emphasizing evidenced relations, source spans, bi-temporal edges, review-gated entity resolution, output quarantine and agent access through MCP. 〔[claim:c4f2def09ea56d98](../claims/claim-c4f2def09ea56d98.md)〕

## Compiled interpretation

This page reorganizes candidate knowledge around a stable reader task. It is not source concatenation and it does not turn retrieval, maintainer claims, preprints, or generated prose into verified truth.

## Review boundary

Check evidence entailment, source independence, contradiction, neutrality, due weight, freshness, and downstream impact before publication.

## Method

Discover perspectives, ask questions, retrieve evidence, create a hierarchical outline, check source/viewpoint coverage, then draft. Every factual paragraph must cite; disputed or high-risk statements expand to atomic evidence.

## Related pages

- [Llm Wiki](../maps/llm-wiki.md) — `part_of`
- [Epistemic separation](../concepts/epistemic-separation.md) — `depends_on`
- [v0 LLM Wiki quality gates](../evaluations/v0-quality-gates.md) — `evaluates`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (`arxiv:2305.14251`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Enabling Large Language Models to Generate Text with Citations (`arxiv:2305.14627`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models (`arxiv:2402.14207`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models (`arxiv:2509.23233`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### VectifyAI/OpenKB (`github:VectifyAI/OpenKB`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### xoai/sage-wiki (`github:xoai/sage-wiki`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

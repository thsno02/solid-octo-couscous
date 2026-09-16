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
- claim:84c91602bd1dfb78
- claim:ecdd2719fa55751c
- claim:1929edca74fa3fa5
- claim:b281f7d7bc21b10d
- claim:bc9a34bd8a9c7154
- claim:bed2f056ecd73c69
- claim:e7026275c099e7e2
source_refs: &id001
- arxiv:2501.04227
- arxiv:2408.06292
- arxiv:2505.13400
- arxiv:2504.08066
- arxiv:2502.14499
- arxiv:2406.06769
- arxiv:2602.06855
- arxiv:2402.14207
- arxiv:2305.14251
- arxiv:2509.23233
- arxiv:2305.14627
- github:VectifyAI/OpenKB
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
  - claim:84c91602bd1dfb78
  notes: null
- target: wiki-page:map-governance-evaluation
  relation: related
  claim_refs:
  - claim:2f8ebd974fc7b5fd
  - claim:38c95b3e2bcfcf51
  - claim:3c6cef89711e89f2
  - claim:9077f46d7f30e565
  - claim:4bf5ea8e6b4e37de
  - claim:84c91602bd1dfb78
  notes: null
- target: wiki-page:v0-quality-gates
  relation: evaluates
  claim_refs:
  - claim:2f8ebd974fc7b5fd
  - claim:38c95b3e2bcfcf51
  - claim:3c6cef89711e89f2
  - claim:9077f46d7f30e565
  - claim:4bf5ea8e6b4e37de
  - claim:84c91602bd1dfb78
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
  build_id: build:llm-wiki-v0:6b16cc1e2adf538b
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2501.04227@sha256:67b9543ae1d8e3ad86a65e2a436ddbd12700d7c8f4a66c5b4c2a6fccc1674d75
  - arxiv:2408.06292@sha256:e911f90b0114d5e3fc23a0000177ea670fa9ed79d5f9a664efa2980fdb350507
  - arxiv:2505.13400@sha256:1abd0b99271884b6f1a8fd9db0185e8042f079a61879ec0c9a7febae6a0c942c
  - arxiv:2504.08066@sha256:53bafd3028e3f8829a3d85220e84dcf0d18934f9b75c092a60de303ff3644bd2
  - arxiv:2502.14499@sha256:de8bc15be762914dd2f056f00efe2b83d51ce852a7035d65e866e6cdecbbb65a
  - arxiv:2406.06769@sha256:cb1d6ccc88eb66af69e71730a5c488234ff4fe8af04ba04081b5a445f4d39b3e
  - arxiv:2602.06855@sha256:ac1ba940f1bdc54e012cc384c428f78bd01d50d7a947f052117944c03e790d9a
  - arxiv:2402.14207@sha256:28b57e9821da798bf8ccfa3f144bfa37cd96ff3582c2211c83eff5ffcf0ccfc2
  - arxiv:2305.14251@sha256:57414a8d80031dceed44fb17efa562cab7e1490390ce95d8753480fba9686795
  - arxiv:2509.23233@sha256:8570de4224cfc829f7478411feca2ecec5f50d6e7ceb7cc62fd15fa07f20c921
  - arxiv:2305.14627@sha256:6902aae852b39f761a60dc2cf36b7d2ed9e615755f413b7daa8b52f5c1eae3ea
  - github:VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc
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
    one_line: Automation accelerates research and writing but requires independent evidence and governance gates.
    short: Automation accelerates research and writing but requires independent evidence and governance gates.
    full: null
  estimated_tokens: 2287
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:2f8ebd974fc7b5fd
- claim:38c95b3e2bcfcf51
- claim:3c6cef89711e89f2
- claim:9077f46d7f30e565
- claim:4bf5ea8e6b4e37de
- claim:84c91602bd1dfb78
- claim:ecdd2719fa55751c
- claim:1929edca74fa3fa5
- claim:b281f7d7bc21b10d
- claim:bc9a34bd8a9c7154
- claim:bed2f056ecd73c69
- claim:e7026275c099e7e2
rights_refs:
- source_uid: arxiv:2406.06769
  source_revision: sha256:cb1d6ccc88eb66af69e71730a5c488234ff4fe8af04ba04081b5a445f4d39b3e
  source_version_url: https://arxiv.org/abs/2406.06769v2
  license_spdx: CC-BY-SA-4.0
  license_url: https://creativecommons.org/licenses/by-sa/4.0/
  notice_path: raw_data/licenses/discoveryworld-v2-cc-by-sa-4.0-neurips-corresponding-expression-cc-by-4.0.md
  package_path: materialized_sources/corpus/arxiv-2406.06769--d1971e3b/manifest.yaml#rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:84c91602bd1dfb78
- source_uid: arxiv:2408.06292
  source_revision: sha256:e911f90b0114d5e3fc23a0000177ea670fa9ed79d5f9a664efa2980fdb350507
  source_version_url: https://arxiv.org/pdf/2408.06292v3
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: raw_data/licenses/cc-by-4.0.md
  package_path: materialized_sources/corpus/arxiv-2408.06292--522d359c/manifest.yaml#pdf_supplement.rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:38c95b3e2bcfcf51
- source_uid: arxiv:2501.04227
  source_revision: sha256:67b9543ae1d8e3ad86a65e2a436ddbd12700d7c8f4a66c5b4c2a6fccc1674d75
  source_version_url: https://arxiv.org/pdf/2501.04227v2
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: raw_data/licenses/cc-by-4.0.md
  package_path: materialized_sources/corpus/arxiv-2501.04227--a0515b2c/manifest.yaml#pdf_supplement.rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:2f8ebd974fc7b5fd
- source_uid: arxiv:2504.08066
  source_revision: sha256:53bafd3028e3f8829a3d85220e84dcf0d18934f9b75c092a60de303ff3644bd2
  source_version_url: https://arxiv.org/pdf/2504.08066v1
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: raw_data/licenses/cc-by-4.0.md
  package_path: materialized_sources/corpus/arxiv-2504.08066--22ed15f2/manifest.yaml#pdf_supplement.rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:9077f46d7f30e565
rights_unavailable_source_refs:
- arxiv:2305.14251
- arxiv:2305.14627
- arxiv:2402.14207
- arxiv:2502.14499
- arxiv:2505.13400
- arxiv:2509.23233
- arxiv:2602.06855
- github:VectifyAI/OpenKB
---

# Automation versus editorial review

## Purpose

Automation accelerates research and writing but requires independent evidence and governance gates.

## Candidate evidence

- **Agent Laboratory: Using LLM Agents as Research Assistants** (source assertion): Historically, scientific discovery has been a lengthy and costly process, demanding substantial time and resources from initial conception to final results. To accelerate scientific discovery, reduce research costs, and improve research quality, we introduceAgent Laboratory , an autonomous LLM-based framework capable of completing the entire research process. 〔[claim:2f8ebd974fc7b5fd](../claims/claim-2f8ebd974fc7b5fd.md)〕
- **The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery** (source assertion): One of the grand challenges of artificial general intelligence is developing agents capable of conducting scientific research and discovering new knowledge. While frontier models have already been used as aides to human scientists, e.g. 〔[claim:38c95b3e2bcfcf51](../claims/claim-38c95b3e2bcfcf51.md)〕
- **Robin: A multi-agent system for automating scientific discovery** (source assertion): Scientific discovery is driven by the iterative process of background research, hypothesis generation, experimentation, and data analysis. Despite recent advancements in applying artificial intelligence to scientific discovery, no system has yet automated all of these stages in a single workflow. 〔[claim:3c6cef89711e89f2](../claims/claim-3c6cef89711e89f2.md)〕
- **The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search** (source assertion): AI is increasingly playing a pivotal role in transforming how scientific discoveries are made. We introduce Th e A I Sc i e n t i s t - v 2, an end-to-end agentic system capable of producing the first entirely AI- generatedpeer-review-acceptedworkshoppaper. 〔[claim:9077f46d7f30e565](../claims/claim-9077f46d7f30e565.md)〕
- **MLGym: A New Framework and Benchmark for Advancing AI Research Agents** (source assertion): We introduce Meta and -Bench, a new framework and benchmark for evaluating and developing LLM agents on AI research tasks. This is the first Gym environment for machine learning (ML) tasks, enabling research on reinforcement learning (RL) algorithms for training such agents. 〔[claim:4bf5ea8e6b4e37de](../claims/claim-4bf5ea8e6b4e37de.md)〕
- **DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents** (source assertion): Automated scientific discovery promises to accelerate progress across scientific domains. However, developing and evaluating an AI agent's capacity for end-to-end scientific reasoning is challenging as running real-world experiments is often prohibitively expensive or infeasible. 〔[claim:84c91602bd1dfb78](../claims/claim-84c91602bd1dfb78.md)〕
- **AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents** (source assertion): LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we introduce ~(the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine learning papers. 〔[claim:ecdd2719fa55751c](../claims/claim-ecdd2719fa55751c.md)〕
- **Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models** (source assertion): We study how to apply large language models to write grounded and organized long-form articles from scratch, with comparable breadth and depth to Wikipedia pages. This underexplored problem poses new challenges at the pre-writing stage, including how to research the topic and prepare an outline prior to writing. 〔[claim:1929edca74fa3fa5](../claims/claim-1929edca74fa3fa5.md)〕
- **FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation** (source assertion): Evaluating the factuality of long-form text generated by large language models (LMs) is non-trivial because (1) generations often contain a mixture of supported and unsupported pieces of information, making binary judgments of quality inadequate, and (2) human evaluation is time-consuming and costly. In this paper, we introduce , a new evaluation that breaks a generation into a series of atomic facts and computes the 〔[claim:b281f7d7bc21b10d](../claims/claim-b281f7d7bc21b10d.md)〕
- **Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models** (source assertion): Wikipedia is the largest open knowledge corpus, widely used worldwide and serving as a key resource for training large language models (LLMs) and retrieval-augmented generation (RAG) systems. Ensuring its accuracy is therefore critical. 〔[claim:bc9a34bd8a9c7154](../claims/claim-bc9a34bd8a9c7154.md)〕
- **Enabling Large Language Models to Generate Text with Citations** (source assertion): Large language models (LLMs) have emerged as a widely-used tool for information seeking, but their generated outputs are prone to hallucination. In this work, our aim is to allow LLMs to generate text with citations , improving their factual correctness and verifiability. 〔[claim:bed2f056ecd73c69](../claims/claim-bed2f056ecd73c69.md)〕
- **VectifyAI/OpenKB** (source assertion): **OpenKB (Open Knowledge Base)** is an open-source system (in CLI) that compiles raw documents into a structured, interlinked wiki-style knowledge base using LLMs, powered by [**PageIndex**](https://github.com/VectifyAI/PageIndex)'s vectorless, reasoning-based retrieval for long documents. 〔[claim:e7026275c099e7e2](../claims/claim-e7026275c099e7e2.md)〕

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

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents (`arxiv:2406.06769`)

- Components: `claim:84c91602bd1dfb78`
- Source revision: `sha256:cb1d6ccc88eb66af69e71730a5c488234ff4fe8af04ba04081b5a445f4d39b3e`
- Source version: [pinned upstream version](https://arxiv.org/abs/2406.06769v2)
- License: [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- NOTICE: [raw_data/licenses/discoveryworld-v2-cc-by-sa-4.0-neurips-corresponding-expression-cc-by-4.0.md](../../../../raw_data/licenses/discoveryworld-v2-cc-by-sa-4.0-neurips-corresponding-expression-cc-by-4.0.md)
- Attribution: "DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents", arXiv:2406.06769v2, by Peter Jansen, Marc-Alexandre Côté, Tushar Khot, Erin Bransom, Bhavana Dalvi Mishra, Bodhisattwa Prasad Majumder, Oyvind Tafjord and Peter Clark, https://arxiv.org/abs/2406.06769v2, licensed under CC BY-SA 4.0: https://creativecommons.org/licenses/by-sa/4.0/. source/neurips_data_2024.sty is an independent NeurIPS Data 2024 template component with its original Lora Aroyo credit and attribution to Roman Garnett and the many authors of nips15submit_e.sty, including MK and drstrip@sandia, retained. Its corresponding licensed original template expression is identified in the NeurIPS 2026 Program Chairs' official "Formatting Instructions For NeurIPS 2026", https://www.overleaf.com/latex/templates/formatting-instructions-for-neurips-2026/bjdwqfdkyftc, explicitly declared CC BY 4.0: https://creativecommons.org/licenses/by/4.0/. The corresponding official current source is https://media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip, checked on 2026-09-16. The retained 2024 Data variant is packaged using this corresponding-expression/adaptation path, not a claim that the historical 2024 ZIP declared an overall CC BY 4.0 license. The retained member is also identified by the official 2024 Data bundle, https://media.neurips.cc/Conferences/NeurIPS2024/NeurIPS-Dataset-Styles.zip, linked from https://neurips.cc/Conferences/2024/CallForDatasetsBenchmarks. None of these attributions implies endorsement of this repository.
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. All nine text source members of the fixed v2 archive are retained unchanged, including related_work-v1-old.tex. The existing normalized/document.tex and all 74 selectors are preserved byte-for-byte. The original 94,506-byte normalized/document.txt is preserved as an exact prefix; only the complete attribution, changes, scope and NOTICE link are appended to its end. Compared with the currently reviewed official NeurIPS 2026 style, the retained Data 2024 style has the Lora Aroyo header, its 2024/04/30 package identifier, the anonymous default/option and @submission boolean mapping, and the @submission test in the title block; its meeting identifiers are 38th/2024 and its existing location string is "Vancouver, USA". It retains "Preprint. Under review." and the Datasets and Benchmarks track footer. The lineno/amsmath compatibility block appears earlier in the retained style rather than at the current style's end; its closing-brace layout differs. The retained style uses the 2024 package warning identifier and a space between each checklist answer label and its argument. It lacks the current multi-track, position/eandd/creativeai/education/workshop/nonanonymous options, minimum font-size overrides, acknowledgement-hiding block and justificationTODO command. Long formatting and compatibility expressions correspond to the currently licensed original; version labels, short footer text and routine functional adaptations are separately disclosed. These differences are pre-existing and are not introduced, repaired or attributed to a newly asserted modifier by this repository. No historical template download identity, historical 2024 BY4 declaration or byte-identical correspondence to the complete current style is claimed.
- Scope: 本包仅覆盖固定 arXiv 2406.06769v2 的九个 source 文字成员、normalized/document.tex、normalized/document.txt 与 74 个定位器（selectors）。作者/提交者有权许可的论文源表达及其文本转换，包括保留的旧稿，按 CC BY-SA 4.0 共享；改编材料继续按该许可同方式共享。source/neurips_data_2024.sty 是独立第三方模板，按当前官方模板的对应授权表达及 CC BY 4.0 复制/改编路径分别署名，保留其既存短常规功能适配，不将历史 2024 ZIP 宣称为整体 BY4，也不将模板著作权归论文作者。两许可按组件分别适用，不将整仓库重新许可为 BY-SA4 或 BY4；定位器不改变所定位组件的许可。DiscoveryWorld.bbl 是书目记录，不授权所引作品；未保存的五个非文本媒体、外链代码/模型/数据、商标及专利不在本许可包范围。没有删除任何已保存源文字以回避许可条件，不施加额外限制或暗示上游支持。

### The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery (`arxiv:2408.06292`)

- Components: `claim:38c95b3e2bcfcf51`
- Source revision: `sha256:e911f90b0114d5e3fc23a0000177ea670fa9ed79d5f9a664efa2980fdb350507`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2408.06292v3)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [raw_data/licenses/cc-by-4.0.md](../../../../raw_data/licenses/cc-by-4.0.md)
- Attribution: Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, David Ha. The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery. Fixed arXiv 2408.06292v3, https://arxiv.org/abs/2408.06292v3; original PDF https://arxiv.org/pdf/2408.06292v3. CC BY 4.0, https://creativecommons.org/licenses/by/4.0/; full legal code https://creativecommons.org/licenses/by/4.0/legalcode.en. Title, complete author list, fixed version and article license link checked on the official version page on 2026-09-16. Original credits, notices and AI-generated-paper warnings inside the PDF are retained, not converted into repository endorsements.
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 原官方 PDF 按下载 bytes 原样保存；使用 pypdf 6.18.1 提取逐页文字，加入明确页边界并生成本地页定位；在派生 text 末尾附唯一署名、修改与范围声明及 NOTICE.md 链接。不编辑原 PDF、不执行其中代码或提示词，不把原生文本当 OCR。既有 source、normalized、selectors、archive revision 和旧归属包均保留。本层是有损预处理，不自动晋升 trusted。
- Scope: 仅本次从 https://arxiv.org/pdf/2408.06292v3 取得的固定版本官方 PDF（186页，11731143 bytes）、其页级提取文本与定位器。覆盖论文编译后主文、参考文献和 PDF 实际内嵌附录/图表，不包含外链论文、数据集、模型、代码仓库或新增源模板。作者/提交者可许可的作品表达沿官方固定版本 CC BY 4.0；保留 PDF 内独立署名、图注和警告，不暗示原作者支持本仓库。旧 TeX 包及其独立组件许可原样保留，本附加包不改其授权范围。原 PDF 完整保存不等于原生文本无损，图内文字、数学、图形与阅读顺序损失另列 coverage。

### Agent Laboratory: Using LLM Agents as Research Assistants (`arxiv:2501.04227`)

- Components: `claim:2f8ebd974fc7b5fd`
- Source revision: `sha256:67b9543ae1d8e3ad86a65e2a436ddbd12700d7c8f4a66c5b4c2a6fccc1674d75`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2501.04227v2)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [raw_data/licenses/cc-by-4.0.md](../../../../raw_data/licenses/cc-by-4.0.md)
- Attribution: Samuel Schmidgall, Yusheng Su, Ze Wang, Ximeng Sun, Jialian Wu, Xiaodong Yu, Jiang Liu, Michael Moor, Zicheng Liu, Emad Barsoum. Agent Laboratory: Using LLM Agents as Research Assistants. Fixed arXiv 2501.04227v2, https://arxiv.org/abs/2501.04227v2; original PDF https://arxiv.org/pdf/2501.04227v2. CC BY 4.0, https://creativecommons.org/licenses/by/4.0/; full legal code https://creativecommons.org/licenses/by/4.0/legalcode.en. Title, complete author list, fixed version and article license link checked on the official version page on 2026-09-16. Original credits, notices and AI-generated-paper warnings inside the PDF are retained, not converted into repository endorsements.
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 原官方 PDF 按下载 bytes 原样保存；使用 pypdf 6.18.1 提取逐页文字，加入明确页边界并生成本地页定位；在派生 text 末尾附唯一署名、修改与范围声明及 NOTICE.md 链接。不编辑原 PDF、不执行其中代码或提示词，不把原生文本当 OCR。既有 source、normalized、selectors、archive revision 和旧归属包均保留。本层是有损预处理，不自动晋升 trusted。
- Scope: 仅本次从 https://arxiv.org/pdf/2501.04227v2 取得的固定版本官方 PDF（84页，3644380 bytes）、其页级提取文本与定位器。覆盖论文编译后主文、参考文献和 PDF 实际内嵌附录/图表，不包含外链论文、数据集、模型、代码仓库或新增源模板。作者/提交者可许可的作品表达沿官方固定版本 CC BY 4.0；保留 PDF 内独立署名、图注和警告，不暗示原作者支持本仓库。旧 TeX 包及其独立组件许可原样保留，本附加包不改其授权范围。原 PDF 完整保存不等于原生文本无损，图内文字、数学、图形与阅读顺序损失另列 coverage。

### The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search (`arxiv:2504.08066`)

- Components: `claim:9077f46d7f30e565`
- Source revision: `sha256:53bafd3028e3f8829a3d85220e84dcf0d18934f9b75c092a60de303ff3644bd2`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2504.08066v1)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [raw_data/licenses/cc-by-4.0.md](../../../../raw_data/licenses/cc-by-4.0.md)
- Attribution: Yutaro Yamada, Robert Tjarko Lange, Cong Lu, Shengran Hu, Chris Lu, Jakob Foerster, Jeff Clune, David Ha. The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search. Fixed arXiv 2504.08066v1, https://arxiv.org/abs/2504.08066v1; original PDF https://arxiv.org/pdf/2504.08066v1. CC BY 4.0, https://creativecommons.org/licenses/by/4.0/; full legal code https://creativecommons.org/licenses/by/4.0/legalcode.en. Title, complete author list, fixed version and article license link checked on the official version page on 2026-09-16. Original credits, notices and AI-generated-paper warnings inside the PDF are retained, not converted into repository endorsements. Seven human workshop reviews retain independent anonymous reviewer attribution: compositional regularization Reviewer #1/#2 (source/workshop_papers/compositional_regularization/reviewer_2.txt and reviewer_3.txt); label noise Reviewer #1/#2 (source/workshop_papers/label_noise/reviewer_1.txt and reviewer_3.txt); pest prediction Reviewer #1/#2/#3 (source/workshop_papers/pest_prediction/reviewer_1.txt, reviewer_2.txt, reviewer_3.txt). Their separately established CC BY 4.0 basis is OpenReview Comment/review Terms updated 2024-09-24, https://openreview.net/legal/terms, as documented in the existing source package. Only the two compositional reviews have an explicit inclusion-permission statement; no equivalent consent, reviewer identity or public forum match is invented for the others.
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 原官方 PDF 按下载 bytes 原样保存；使用 pypdf 6.18.1 提取逐页文字，加入明确页边界并生成本地页定位；在派生 text 末尾附唯一署名、修改与范围声明及 NOTICE.md 链接。不编辑原 PDF、不执行其中代码或提示词，不把原生文本当 OCR。既有 source、normalized、selectors、archive revision 和旧归属包均保留。本层是有损预处理，不自动晋升 trusted。
- Scope: 仅本次从 https://arxiv.org/pdf/2504.08066v1 取得的固定版本官方 PDF（69页，8923691 bytes）、其页级提取文本与定位器。覆盖论文编译后主文、参考文献和 PDF 实际内嵌附录/图表，不包含外链论文、数据集、模型、代码仓库或新增源模板。作者/提交者可许可的作品表达沿官方固定版本 CC BY 4.0；保留 PDF 内独立署名、图注和警告，不暗示原作者支持本仓库。旧 TeX 包及其独立组件许可原样保留，本附加包不改其授权范围。原 PDF 完整保存不等于原生文本无损，图内文字、数学、图形与阅读顺序损失另列 coverage。 七份匿名 workshop review 继续按独立 CC BY 4.0 及逐组 Reviewer 标签归属，不冒称论文作者原创。

### FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (`arxiv:2305.14251`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Enabling Large Language Models to Generate Text with Citations (`arxiv:2305.14627`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models (`arxiv:2402.14207`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### MLGym: A New Framework and Benchmark for Advancing AI Research Agents (`arxiv:2502.14499`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Robin: A multi-agent system for automating scientific discovery (`arxiv:2505.13400`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models (`arxiv:2509.23233`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents (`arxiv:2602.06855`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### VectifyAI/OpenKB (`github:VectifyAI/OpenKB`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

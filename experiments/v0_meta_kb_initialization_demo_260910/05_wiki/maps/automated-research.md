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
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:261023893e1f09a1
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2501.04227@sha256:67b9543ae1d8e3ad86a65e2a436ddbd12700d7c8f4a66c5b4c2a6fccc1674d75
  - arxiv:2408.06292@sha256:e911f90b0114d5e3fc23a0000177ea670fa9ed79d5f9a664efa2980fdb350507
  - arxiv:2505.13400@sha256:336d4e3f9065f42918cec8053e020d12c8d8c8031eb4c180764a349d1efa1794
  - arxiv:2504.08066@sha256:53bafd3028e3f8829a3d85220e84dcf0d18934f9b75c092a60de303ff3644bd2
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
    one_line: Routing map for automated research sources, questions, and claims.
    short: Routing map for automated research sources, questions, and claims.
    full: null
  estimated_tokens: 1364
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:2f8ebd974fc7b5fd
- claim:38c95b3e2bcfcf51
- claim:3c6cef89711e89f2
- claim:3d07597b1776b0bd
- claim:852bc42ef50e89c7
- claim:8798b3dc1ae125ea
- claim:9077f46d7f30e565
- claim:d3a0d3c2f4fd45d4
rights_refs:
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
- source_uid: arxiv:2505.13400
  source_revision: sha256:336d4e3f9065f42918cec8053e020d12c8d8c8031eb4c180764a349d1efa1794
  source_version_url: https://arxiv.org/pdf/2505.13400v1
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/pdf-supplement/NOTICE.md
  package_path: materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/manifest.yaml#pdf_supplement.rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:3c6cef89711e89f2
rights_unavailable_source_refs: []
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

- **Agent Laboratory: Using LLM Agents as Research Assistants** (source assertion): Historically, scientific discovery has been a lengthy and costly process, demanding substantial time and resources from initial conception to final results. To accelerate scientific discovery, reduce research costs, and improve research quality, we introduceAgent Laboratory , an autonomous LLM-based framework capable of completing the entire research process. 〔[claim:2f8ebd974fc7b5fd](../claims/claim-2f8ebd974fc7b5fd.md)〕
- **The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery** (source assertion): One of the grand challenges of artificial general intelligence is developing agents capable of conducting scientific research and discovering new knowledge. While frontier models have already been used as aides to human scientists, e.g. 〔[claim:38c95b3e2bcfcf51](../claims/claim-38c95b3e2bcfcf51.md)〕
- **Robin: A multi-agent system for automating scientific discovery** (source assertion): Scientific discovery is driven by the iterative process of background research, hypothesis generation, experimentation, and data analysis. Despite recent advancements in applying artificial intelligence to scientific discovery, no system has yet automated all of these stages in a single workflow. 〔[claim:3c6cef89711e89f2](../claims/claim-3c6cef89711e89f2.md)〕
- **The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search** (source assertion): AI is increasingly playing a pivotal role in transforming how scientific discoveries are made. We introduce Th e A I Sc i e n t i s t - v 2, an end-to-end agentic system capable of producing the first entirely AI- generatedpeer-review-acceptedworkshoppaper. 〔[claim:9077f46d7f30e565](../claims/claim-9077f46d7f30e565.md)〕

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

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

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

### Robin: A multi-agent system for automating scientific discovery (`arxiv:2505.13400`)

- Components: `claim:3c6cef89711e89f2`
- Source revision: `sha256:336d4e3f9065f42918cec8053e020d12c8d8c8031eb4c180764a349d1efa1794`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2505.13400v1)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/pdf-supplement/NOTICE.md](../../../../materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/pdf-supplement/NOTICE.md)
- Attribution: Ali Essam Ghareeb; Benjamin Chang; Ludovico Mitchener; Angela Yiu; Caralyn J. Szostkiewicz; Jon M. Laurent; Muhammed T. Razzak; Andrew D. White; Michaela M. Hinks; Samuel G. Rodriques, Robin: A multi-agent system for automating scientific discovery, arXiv:2505.13400v1 (2025-05-19), https://arxiv.org/abs/2505.13400v1, PDF https://arxiv.org/pdf/2505.13400v1, CC BY4 https://creativecommons.org/licenses/by/4.0/。完整十作者 Ali Essam Ghareeb／Benjamin Chang／Ludovico Mitchener／Angela Yiu／Caralyn J. Szostkiewicz／Jon M. Laurent／Muhammed T. Razzak／Andrew D. White／Michaela M. Hinks／Samuel G. Rodriques；Ghareeb/Chang等贡献，White/Rodriques共同监督FutureHouse，Hinks/Rodriques共同监督本工作，FutureHouse／Oxford机构原样，未造逐作者贡献表。p11 Michael Skarlinski／Mayk Caldas／Tyler Nadolski／James Braza／Siddharth Narayanan与FutureHouse致谢保留。p4 Fig2/p6 Fig3明示部分分析由human为publication readability格式化，不改为无人工。p9 Table1供应商catalog引用与Rapamycin Gift from RetroBio（非Rebio）保留。微镜／flow／RNA-seq在原研究表示内保留，不独立重许可底层数据。S10两处重复原样，不补源88bibabstract或其15copyright旧未决。 既有 R 已核固定v1源payload/保留表达与作品BY4；本次PDF可见v1页标、embedded arXivID与License BY4，C核十作者／30页／全部Supplementary Material至S25，主线明确准入。不发明旧固定archive URL。 以上归属不暗示背书。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 固定版本 PDF 按本次真实响应 bytes 原样保留，不编辑、重导或 OCR；以既有 helper 的 plain 全页提取生成独立 pdf-supplement/document.txt 和真实 PDF revision 的页定位器（page selectors），在文末追加唯一归属、修改／范围附注与同目录 NOTICE.md 链接。NOTICE 自包含本项实际归属、精确范围及现存完整 CC BY 4.0 法条；native text 的逐项损失见 limitations，不声称无损转换或可直接执行的源代码／prompt。旧 root source、normalized TXT／TeX、selectors、NOTICE／README、revision、retrieval 和历史 gate 不改，不将新固定版选择冒称旧 source payload 已被追溯核定。
- Scope: 本独立表示仅覆盖固定 arXiv:2505.13400v1 原 bytes 不改的30页 PDF（33781795 bytes）：固定 arXiv:2505.13400v1 完整30物理页编译PDF：p1–7主文Results／Discussion及四科学图，p8–11 Methods4.1–4.5.5／Acknowledgements／Data and Code Availability，p12–15 References[1]–[69]，p16 Supplementary Material／S1，p17–24完整实验assay／therapeutic候选／judge prompts（p22/p24实际重复S10保留），p25–28 S11–S15 human评估／microscopy／flow／RNA-seq，p29–30 S16–S25十类候选至Chronic Kidney Disease十项INF4E。未取外部RNA-seq/.fcs/code/trajectories。 论文作者可许可表达按本固定作品已证 CC BY4 路径；实际有界引用／图板按原件精确信用与身份保留，不改变底层许可、不独立重许被引全文／数据／代码／模型／媒体／商标／源模板或整个source归档。 此范围也包含该PDF native plain、页selectors及完整BY4 NOTICE；旧 root rights／block／retrieval／revision／source_version键缺省和历史原件／文字缺失不改；无普遍权利保证。

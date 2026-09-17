---
uid: wiki-page:claim-evidence-page-compilation
title: Claim–evidence–page compilation
slug: methods/claim-evidence-page
page_type: method
status: review
summary: Compile pages from atomic claims while preserving selectors and scope.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id002
- claim:4bf5ea8e6b4e37de
- claim:84c91602bd1dfb78
- claim:ecdd2719fa55751c
- claim:1929edca74fa3fa5
- claim:b281f7d7bc21b10d
- claim:bc9a34bd8a9c7154
- claim:bed2f056ecd73c69
- claim:e7026275c099e7e2
- claim:e7ac7da9ac39e47d
- claim:0edb741be0f31f6f
- claim:583280271287ef9c
- claim:fc57f26307cefee3
source_refs: &id001
- arxiv:2502.14499
- arxiv:2406.06769
- arxiv:2602.06855
- arxiv:2402.14207
- arxiv:2305.14251
- arxiv:2509.23233
- arxiv:2305.14627
- github:VectifyAI/OpenKB
- github:xoai/sage-wiki
- arxiv:2511.02824
- methodology:linkml-schema-first
- github:linkml/linkml
page_refs:
- wiki-page:epistemic-separation
- wiki-page:source-specific-consumption
outgoing_links:
- target: wiki-page:epistemic-separation
  relation: depends_on
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:84c91602bd1dfb78
  - claim:ecdd2719fa55751c
  - claim:1929edca74fa3fa5
  - claim:b281f7d7bc21b10d
  - claim:bc9a34bd8a9c7154
  notes: null
- target: wiki-page:source-specific-consumption
  relation: depends_on
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:84c91602bd1dfb78
  - claim:ecdd2719fa55751c
  - claim:1929edca74fa3fa5
  - claim:b281f7d7bc21b10d
  - claim:bc9a34bd8a9c7154
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
  build_id: build:llm-wiki-v0:45bd6c7288326476
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2502.14499@sha256:de8bc15be762914dd2f056f00efe2b83d51ce852a7035d65e866e6cdecbbb65a
  - arxiv:2406.06769@sha256:28793ae05bbb22ed6e02fbdceb697a2b9ea8ebff6932c4dd8fb5b70bba5dde91
  - arxiv:2602.06855@sha256:ac1ba940f1bdc54e012cc384c428f78bd01d50d7a947f052117944c03e790d9a
  - arxiv:2402.14207@sha256:28b57e9821da798bf8ccfa3f144bfa37cd96ff3582c2211c83eff5ffcf0ccfc2
  - arxiv:2305.14251@sha256:57414a8d80031dceed44fb17efa562cab7e1490390ce95d8753480fba9686795
  - arxiv:2509.23233@sha256:8570de4224cfc829f7478411feca2ecec5f50d6e7ceb7cc62fd15fa07f20c921
  - arxiv:2305.14627@sha256:ae9868f07f0f7ffaae5346778f79b7827d9ec6b13b1e6aae4dff6b2ffc37a2e1
  - github:VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc
  - github:xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d
  - arxiv:2511.02824@sha256:bc1d107627c3f81bd551a6180f1d5739db46b2b3902dc2349a382de500f6b0a8
  - methodology:linkml-schema-first@sha256:93a9f00b0006695dab8f1bde801a40e36eed8c236c4c839aff645bec38b5dc6c
  - github:linkml/linkml@0e401cef2711b0f12f5a1870805c5cfa999b0858
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
    one_line: Compile pages from atomic claims while preserving selectors and scope.
    short: Compile pages from atomic claims while preserving selectors and scope.
    full: null
  estimated_tokens: 2231
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:4bf5ea8e6b4e37de
- claim:84c91602bd1dfb78
- claim:ecdd2719fa55751c
- claim:1929edca74fa3fa5
- claim:b281f7d7bc21b10d
- claim:bc9a34bd8a9c7154
- claim:bed2f056ecd73c69
- claim:e7026275c099e7e2
- claim:e7ac7da9ac39e47d
- claim:0edb741be0f31f6f
- claim:583280271287ef9c
- claim:fc57f26307cefee3
rights_refs:
- source_uid: arxiv:2305.14627
  source_revision: sha256:ae9868f07f0f7ffaae5346778f79b7827d9ec6b13b1e6aae4dff6b2ffc37a2e1
  source_version_url: https://aclanthology.org/2023.emnlp-main.398.pdf
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/pdf-supplement/NOTICE.md
  package_path: materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/manifest.yaml#pdf_supplement.rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:bed2f056ecd73c69
- source_uid: arxiv:2406.06769
  source_revision: sha256:28793ae05bbb22ed6e02fbdceb697a2b9ea8ebff6932c4dd8fb5b70bba5dde91
  source_version_url: https://arxiv.org/pdf/2406.06769v2
  license_spdx: CC-BY-SA-4.0
  license_url: https://creativecommons.org/licenses/by-sa/4.0/
  notice_path: raw_data/licenses/p3-pdf-02-discoveryworld-v2.md
  package_path: materialized_sources/corpus/arxiv-2406.06769--d1971e3b/manifest.yaml#pdf_supplement.rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:84c91602bd1dfb78
- source_uid: arxiv:2511.02824
  source_revision: sha256:bc1d107627c3f81bd551a6180f1d5739db46b2b3902dc2349a382de500f6b0a8
  source_version_url: https://arxiv.org/pdf/2511.02824v2
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: materialized_sources/corpus/arxiv-2511.02824--1c218a8e/pdf-supplement/NOTICE.md
  package_path: materialized_sources/corpus/arxiv-2511.02824--1c218a8e/manifest.yaml#pdf_supplement.rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:0edb741be0f31f6f
- source_uid: methodology:linkml-schema-first
  source_revision: sha256:93a9f00b0006695dab8f1bde801a40e36eed8c236c4c839aff645bec38b5dc6c
  source_version_url: https://linkml.io/linkml/
  license_spdx: Apache-2.0
  license_url: https://www.apache.org/licenses/LICENSE-2.0
  notice_path: raw_data/licenses/apache-2.0.md
  package_path: materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/manifest.yaml#rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:583280271287ef9c
rights_unavailable_source_refs:
- arxiv:2305.14251
- arxiv:2402.14207
- arxiv:2502.14499
- arxiv:2509.23233
- arxiv:2602.06855
- github:VectifyAI/OpenKB
- github:linkml/linkml
- github:xoai/sage-wiki
---

# Claim–evidence–page compilation

## Purpose

Compile pages from atomic claims while preserving selectors and scope.

## Candidate evidence

- **MLGym: A New Framework and Benchmark for Advancing AI Research Agents** (source assertion): We introduce Meta and -Bench, a new framework and benchmark for evaluating and developing LLM agents on AI research tasks. This is the first Gym environment for machine learning (ML) tasks, enabling research on reinforcement learning (RL) algorithms for training such agents. 〔[claim:4bf5ea8e6b4e37de](../claims/claim-4bf5ea8e6b4e37de.md)〕
- **DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents** (source assertion): Automated scientific discovery promises to accelerate progress across scientific domains. However, developing and evaluating an AI agent’s capacity for end- to-end scientific reasoning is challenging as running real-world experiments is often prohibitively expensive or infeasible. 〔[claim:84c91602bd1dfb78](../claims/claim-84c91602bd1dfb78.md)〕
- **AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents** (source assertion): LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we introduce ~(the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine learning papers. 〔[claim:ecdd2719fa55751c](../claims/claim-ecdd2719fa55751c.md)〕
- **Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models** (source assertion): We study how to apply large language models to write grounded and organized long-form articles from scratch, with comparable breadth and depth to Wikipedia pages. This underexplored problem poses new challenges at the pre-writing stage, including how to research the topic and prepare an outline prior to writing. 〔[claim:1929edca74fa3fa5](../claims/claim-1929edca74fa3fa5.md)〕
- **FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation** (source assertion): Evaluating the factuality of long-form text generated by large language models (LMs) is non-trivial because (1) generations often contain a mixture of supported and unsupported pieces of information, making binary judgments of quality inadequate, and (2) human evaluation is time-consuming and costly. In this paper, we introduce , a new evaluation that breaks a generation into a series of atomic facts and computes the 〔[claim:b281f7d7bc21b10d](../claims/claim-b281f7d7bc21b10d.md)〕
- **Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models** (source assertion): Wikipedia is the largest open knowledge corpus, widely used worldwide and serving as a key resource for training large language models (LLMs) and retrieval-augmented generation (RAG) systems. Ensuring its accuracy is therefore critical. 〔[claim:bc9a34bd8a9c7154](../claims/claim-bc9a34bd8a9c7154.md)〕
- **Enabling Large Language Models to Generate Text with Citations** (source assertion): Large language models (LLMs) have emerged as a widely-used tool for information seeking, but their generated outputs are prone to halluci- nation. In this work, our aim is to allow LLMs to generate text with citations, improving their factual correctness and verifiability. 〔[claim:bed2f056ecd73c69](../claims/claim-bed2f056ecd73c69.md)〕
- **VectifyAI/OpenKB** (source assertion): **OpenKB (Open Knowledge Base)** is an open-source system (in CLI) that compiles raw documents into a structured, interlinked wiki-style knowledge base using LLMs, powered by [**PageIndex**](https://github.com/VectifyAI/PageIndex)'s vectorless, reasoning-based retrieval for long documents. 〔[claim:e7026275c099e7e2](../claims/claim-e7026275c099e7e2.md)〕
- **xoai/sage-wiki** (source assertion): **sage-wiki** is a graph memory and knowledge base that AI agents and humans build and query together. Drop in documents; an LLM compiler turns them into an interlinked wiki with a knowledge graph — agents query it through MCP, humans browse it as plain markdown. 〔[claim:e7ac7da9ac39e47d](../claims/claim-e7ac7da9ac39e47d.md)〕
- **Kosmos: An AI Scientist for Autonomous Discovery** (source assertion): Data-driven scientific discovery requires iterative cycles of literature search, hypothesis generation, and data analysis. Substantial progress has been made towards AI agents that can automate scientific research, but all such agents remain limited in the number of actions they can take before losing coherence, thus limiting the depthoftheirfindings. 〔[claim:0edb741be0f31f6f](../claims/claim-0edb741be0f31f6f.md)〕
- **LinkML schema-first knowledge modeling** (source assertion): LinkML is a flexible modeling language that allows you to author schemas in YAML that describe the structure of your data. 〔[claim:583280271287ef9c](../claims/claim-583280271287ef9c.md)〕
- **linkml/linkml** (source assertion): LinkML is a linked data modeling language following object-oriented and ontological principles. 〔[claim:fc57f26307cefee3](../claims/claim-fc57f26307cefee3.md)〕

## Compiled interpretation

This page reorganizes candidate knowledge around a stable reader task. It is not source concatenation and it does not turn retrieval, maintainer claims, preprints, or generated prose into verified truth.

## Review boundary

Check evidence entailment, source independence, contradiction, neutrality, due weight, freshness, and downstream impact before publication.

## Compiler contract

Inputs are pinned source revisions, atomic claims, evidence selectors, schema/identity versions, policy, and bounded scope. Outputs are candidate pages, typed links, semantic diff, validation, review queue, and rollback.

## Related pages

- [Epistemic separation](../concepts/epistemic-separation.md) — `depends_on`
- [Source-specific consumption](../concepts/source-specific-consumption.md) — `depends_on`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Enabling Large Language Models to Generate Text with Citations (`arxiv:2305.14627`)

- Components: `claim:bed2f056ecd73c69`
- Source revision: `sha256:ae9868f07f0f7ffaae5346778f79b7827d9ec6b13b1e6aae4dff6b2ffc37a2e1`
- Source version: [pinned upstream version](https://aclanthology.org/2023.emnlp-main.398.pdf)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/pdf-supplement/NOTICE.md](../../../../materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/pdf-supplement/NOTICE.md)
- Attribution: Tianyu Gao; Howard Yen; Jiatong Yu; Danqi Chen, Enabling Large Language Models to Generate Text with Citations. Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pp.6465–6488, December 6–10, 2023; ©2023 Association for Computational Linguistics。实际四作者顺序、Department of Computer Science & Princeton Language and Intelligence, Princeton University、{tianyug,hyen,jiatongy,danqic}@cs.princeton.edu归属保留。Anthology ID 2023.emnlp-main.398；DOI 10.18653/v1/2023.emnlp-main.398为本批已核正式映射，不称PDF正文印出DOI；作品 https://aclanthology.org/2023.emnlp-main.398/，原PDF https://aclanthology.org/2023.emnlp-main.398.pdf，CC BY4 https://creativecommons.org/licenses/by/4.0/。同一canonical UID arxiv:2305.14627/source_type arxiv不变，不伪造arXiv vN。p10独立致谢Princeton NLP group；Alexander Wettig、Nelson Liu、Tianyi Zhang、Yu Meng、Sadhika Malladi、Yangsibo Huang、Zhiyuan Zeng、Dan Friedman；Surge AI/Anna Folinsky/Edwin Chen的人工评估；Tianyu Gao IBM PhD Fellowship、NSF CAREER IIS-2239290、Sloan Research Fellowship、Microsoft Azure经Accelerate Foundation Models Academic Research Initiative提供credits，独立保留而不混为作者/权利转让或背书。p1 https://github.com/princeton-nlp/ALCE链接与ASQA/QAMPARI/ELI5/Wikipedia/Sphere/Common Crawl及References保留被引对象身份，不下载或再许可其独立代码/数据/被引全文/权重。p23–24 Tables30/31内十段实际有限外部检索文字均为100个空白分隔单元，计数不是token/全文长度/独立作品许可。p23实际标题How to Treat and Prevent Food Poisoning - MsPrepper；FDA Issues Warning About Eating Raw Cookie Dough, But Not For Salmonella Risks；It’s Probably OK to Eat Raw Cookie Dough — As Long As You’re Smart About It - The Crux - Very Top Secret Information；两段How Dangerous Is It to Eat Raw Cookie Dough? | Men’s Health，第四段By Katherine Dempsey，末段说明How Bad Is It To Eat Raw Cookie Dough? originally appeared on Prevention.com。p24实际标题Is Snapchat really worth $19 billion? - CSMonitor.com；What Are Venture Capital Investments? – DollarsAndSense.my；Opinion | What Dara Khosrowshahi Must Do to Save Uber - The New York Times；Snapchat raising funding round at $19 billion valuation: Report；Unicorns And Wall Street | MoneyTips。有限片段/题名/署名/来源提示按原论文学术例示保留，不称四作者原创新闻或ACL拥有外部全文全部权利；PDF未提供全部外部URL，不编造/递归取得原网页，不单独许可新闻整篇，不暗示作者/ACL/机构/资助者背书。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 唯一正式GET的481920 bytes/24页原PDF原样保留，不编辑、重导、重排、OCR或修补源作品。现build_pdf_supplement以pypdf plain全页生成独立pdf-supplement/document.txt及新PDF revision绑定的逐页selectors；## Page N边界、定位和唯一归属/修改/范围footer是collector添加的派生表示元数据，不称作者原始文本或无损布局/公式/代码。NOTICE自包含实际四作者/©ACL/会议身份/独立信用/有限外部例示/范围/限制及现存完整CC BY4法条，notice_path自绑定本文件；不新rawlicense。primary_excerpt仅声明native Page1父摘要连续L11–39，不改PDF/native原样层或生产consumer逻辑。旧source/normalized/root selectors/NOTICE/README/files及root revision/retrieval/rights/materialization/generated_at/status/content_tier/source_version键缺省保持，C source_version仍null；正式版不补入旧v2 Open-source Models三段/Stable Beluga2三行，不以新grant整体放行旧包。
- Scope: 本独立新表示仅覆盖固定publisher-vor:doi:10.18653/v1/2023.emnlp-main.398的未改481920 bytes/24页正式EMNLP2023 PDF及同目录有损native plain、revision-bound页selectors和自包含NOTICE；正式DOI 10.18653/v1/2023.emnlp-main.398 / Anthology 2023.emnlp-main.398完整24物理页（印刷页6465–6488）compiled PDF：p1–9主文至Conclusion/四图，p10 Limitations/Acknowledgments及p10–13完整References，p14–17正式A–I附录叙述，p18–20主结果Tables19–21，p21–22 Tables22–29完整prompts，p23–24 Tables30–31两个ELI5 Examples。真尾p24 Table31第三ground-truth claim、表底线/ELI5 example2图注/页码正常结束，不在References/H标题截断。 论文作者/ACL有权许可表达沿已有正式作品BY4路径，原论文已发表的有限图表例示与十段外部passage/题名/署名/来源信用按原件保存，不推导standalone新闻整篇/引用作品/底层素材/代码仓库/数据/权重/模型/商标/专利的一般许可，不另取外链或执行prompt/benchmark，无普遍权利保证，不为已许可权利添加下游限制。新grant不覆盖旧source归档/LaTeX模板/BST/两摘要或旧未对应扩展/normalized/root selectors/历史gate；旧block及对应evidence false保留，C source_version null与root键缺省保留。

### DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents (`arxiv:2406.06769`)

- Components: `claim:84c91602bd1dfb78`
- Source revision: `sha256:28793ae05bbb22ed6e02fbdceb697a2b9ea8ebff6932c4dd8fb5b70bba5dde91`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2406.06769v2)
- License: [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- NOTICE: [raw_data/licenses/p3-pdf-02-discoveryworld-v2.md](../../../../raw_data/licenses/p3-pdf-02-discoveryworld-v2.md)
- Attribution: Peter Jansen; Marc-Alexandre Côté; Tushar Khot; Erin Bransom; Bhavana Dalvi Mishra; Bodhisattwa Prasad Majumder; Oyvind Tafjord; Peter Clark. "DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents". Fixed arXiv 2406.06769v2, https://arxiv.org/abs/2406.06769v2; original PDF https://arxiv.org/pdf/2406.06769v2. Article expression the authors/submitter may license is available under CC BY-SA 4.0, https://creativecommons.org/licenses/by-sa/4.0/; full legal code https://creativecommons.org/licenses/by-sa/4.0/legalcode.en. Fixed article/PDF license checked in this batch on 2026-09-16. PDF p9 致谢与 p13 checklist 的实际信用：作者购买 CuteRPG/PixyMoon 素材并说明 attribution 要求；原论文截图中的 CuteRPG 素材归属 PixyMoon，产品页 https://pixymoon.itch.io/2d-topdown-cute-rpg-world 。本批已核该具体产品页允许 personal/commercial project use、modify/edit，要求 Credit PixyMoon，禁止 resell asset pack。科学主题增改归论文作者及 OpenAI DALL-E。完整论文内已合成截图保留这些实际信用，不提供或授权独立提取、转售或再分发底层 asset pack，不冒称 sprite 素材获得 CC BY-SA 4.0，也不把资产包条款施加到论文作者有权许可的原创 BY-SA 部分。 No endorsement or additional right to external works/models/trademarks is implied.
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 原官方 PDF 按实际下载 bytes 原样保存，不编辑或重导出；复用既有 pypdf plain 提取逐页文字，加入明确页边界并生成独立页定位；在派生 text 末尾附唯一署名、修改、范围声明及完整 NOTICE.md 链接。plain 文字保留原抽取结果，不做 OCR、不运行 TeX、论文代码或提示词，不将图形、数学排版或阅读顺序损失隐藏为完整。旧 source、normalized、default selectors、NOTICE、files、archive revision/retrieval 和旧许可包全部保留，不新增 trusted。 适用论文表达/页文字及后续改编沿 BY-SA4 同方式共享，不重许可整个仓库。
- Scope: 仅本次从 https://arxiv.org/pdf/2406.06769v2 取得的固定 v2 官方完整 PDF（29 页，3054585 bytes）、其 plain 页文字与独立页定位器。范围为完整主文、全部附录、四幅实际科学图（p2/3/18/29），真实末尾 p29 Save failures/Windows autosave 用户数据丢失说明。作者/提交者有权许可的论文表达与本次文字派生沿作品级 CC BY-SA 4.0；PDF p9 致谢与 p13 checklist 的实际信用：作者购买 CuteRPG/PixyMoon 素材并说明 attribution 要求；原论文截图中的 CuteRPG 素材归属 PixyMoon，产品页 https://pixymoon.itch.io/2d-topdown-cute-rpg-world 。本批已核该具体产品页允许 personal/commercial project use、modify/edit，要求 Credit PixyMoon，禁止 resell asset pack。科学主题增改归论文作者及 OpenAI DALL-E。完整论文内已合成截图保留这些实际信用，不提供或授权独立提取、转售或再分发底层 asset pack，不冒称 sprite 素材获得 CC BY-SA 4.0，也不把资产包条款施加到论文作者有权许可的原创 BY-SA 部分。 论文作者有权许可的原创表达/页文字及后续改编继续 BY-SA4；具体资产边界不施于这些原创 BY-SA 部分，不整库重许可。完整 PDF 原有署名、资助、图注、引文、警告和第三方信用原样保留，不授权外部被引作品全文、模型、代码、脚本或数据，不转授商标、专利或许可者无权许可材料。PDF 原字节不编辑/重导出，plain 文字有损、不做 OCR，原件完整不等于 text extraction complete。旧 source/normalized/default selectors/NOTICE/files/archive revision/retrieval/旧组件授权包不变。

### Kosmos: An AI Scientist for Autonomous Discovery (`arxiv:2511.02824`)

- Components: `claim:0edb741be0f31f6f`
- Source revision: `sha256:bc1d107627c3f81bd551a6180f1d5739db46b2b3902dc2349a382de500f6b0a8`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2511.02824v2)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [materialized_sources/corpus/arxiv-2511.02824--1c218a8e/pdf-supplement/NOTICE.md](../../../../materialized_sources/corpus/arxiv-2511.02824--1c218a8e/pdf-supplement/NOTICE.md)
- Attribution: Ludovico Mitchener; Angela Yiu; Benjamin Chang; Mathieu Bourdenx; Tyler Nadolski; Arvis Sulovari; Eric C. Landsness; Dániel L. Barabási; Siddharth Narayanan; Nicky Evans; Shriya Reddy; Martha Foiani; Aizad Kamal; Leah P. Shriver; Fang Cao; Asmamaw T. Wassie; Jon M. Laurent; Edwin Melville-Green; Mayk Caldas; Albert Bou; Kaleigh F. Roberts; Sladjana Zagorac; Timothy C. Orr; Miranda E. Orr; Kevin J. Zwezdaryk; Ali E. Ghareeb; Laurie McCoy; Bruna Gomes; Euan A. Ashley; Karen E. Duff; Tonio Buonassisi; Tom Rainforth; Randall J. Bateman; Michael Skarlinski; Samuel G. Rodriques; Michaela M. Hinks; Andrew D. White, Kosmos: An AI Scientist for Autonomous Discovery, arXiv:2511.02824v2 (2025-11-05), https://arxiv.org/abs/2511.02824v2, PDF https://arxiv.org/pdf/2511.02824v2, CC BY4 https://creativecommons.org/licenses/by/4.0/。完整37作者：Ludovico Mitchener; Angela Yiu; Benjamin Chang; Mathieu Bourdenx; Tyler Nadolski; Arvis Sulovari; Eric C. Landsness; Dániel L. Barabási; Siddharth Narayanan; Nicky Evans; Shriya Reddy; Martha Foiani; Aizad Kamal; Leah P. Shriver; Fang Cao; Asmamaw T. Wassie; Jon M. Laurent; Edwin Melville-Green; Mayk Caldas; Albert Bou; Kaleigh F. Roberts; Sladjana Zagorac; Timothy C. Orr; Miranda E. Orr; Kevin J. Zwezdaryk; Ali E. Ghareeb; Laurie McCoy; Bruna Gomes; Euan A. Ashley; Karen E. Duff; Tonio Buonassisi; Tom Rainforth; Randall J. Bateman; Michael Skarlinski; Samuel G. Rodriques; Michaela M. Hinks; Andrew D. White。前三Mitchener/Yiu/Chang等贡献；Mitchener/Hinks共同监督本工作，Rodriques/White共同监督Edison；20机构及p26完整贡献／funding保留（NIH R01NS133365、UK DRI/MRC/Cure Alzheimer’s Fund、CIFAR/Toyota SARC、EPSRC EP/Y037200/1等）。p5 Fig2真实credit为 a and b reproduced with permission from [9]，不是旧bc，也不含c／Trajectory r2。p27 [9]原印13作者出处：Aizad Kamal; Juan Liu; Ernesto R. Gonzales; Khairunisa Mohamad Ibrahim; Fan Zhang; Hannah E. Skelton; Javier Kelly Cuenca; Carla Yuede; Gary J. Patti; Leah P. Shriver; Jin-Moo Lee; Aaron J. Norris; Eric C. Landsness, Preoptic activation induces a torpor-like hypothermic and hypometabolic state that is cerebroprotective, October 2025; ISSN:2692-8205; Pages:2025.10.24.684192; Section:New Results；未印URL或DOI且Annots无externalURI，不猜其bioRxiv链接／DOI，不GET原作，不给底层图板或全文一般BY4。BioRender独立credit精确保留：https://BioRender.com 的 Fig5a/c、Fig6a、Fig7a、Fig8a/f/g；Fig6g原E2G http://e2g.stanford.edu/variant/6_7231610_G_A 与Fig6h http://twas-hub.org 保留，未访问／重许全站。Fig4与[15]有限比较及p24外部SupplementaryData1–7 availability保持出处身份，不冒称已取得。SI1自身Discovery1 connectome／Discovery3 hypothermia顺序按原件，不手改，p41/42 REFUTED批评与±数据不润色为支持。 既有 R 已核固定v2源payload／保留表达与作品BY4；本次可见v2侧边、embedded arXivID/License BY4，C核实际37作者／42页内嵌SI1–4／Fig2a/b permission与BioRender精确credit，主线明确准入，不搬旧80bibabstract/31copyright gate入新PDF。 以上归属不暗示背书。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 固定版本 PDF 按本次真实响应 bytes 原样保留，不编辑、重导或 OCR；以既有 helper 的 plain 全页提取生成独立 pdf-supplement/document.txt 和真实 PDF revision 的页定位器（page selectors），在文末追加唯一归属、修改／范围附注与同目录 NOTICE.md 链接。NOTICE 自包含本项实际归属、精确范围及现存完整 CC BY 4.0 法条；native text 的逐项损失见 limitations，不声称无损转换或可直接执行的源代码／prompt。旧 root source、normalized TXT／TeX、selectors、NOTICE／README、revision、retrieval 和历史 gate 不改，不将新固定版选择冒称旧 source payload 已被追溯核定。
- Scope: 本独立表示仅覆盖固定 arXiv:2511.02824v2 原 bytes 不改的42页 PDF（8162544 bytes）：固定 arXiv:2511.02824v2 完整42物理页编译PDF：p1–20主文七discoveries／Discussion，p20–24 Methods及p24 Data availability，p26 contributions／funding，p27–33 References[1]–[58]，p34 Supplementary Table1，p35–37内嵌SI1七输入，p38 SI2，p39–40 SI3 rubric，p41–42 SI4 supported/refuted评价至 We just don’t have enough information.；Figure1–8完整，外部SupplementaryData1–7／reports／trajectory／datasets／code未取得且不在合同target。 论文作者可许可表达按本固定作品已证 CC BY4 路径；实际有界引用／图板按原件精确信用与身份保留，不改变底层许可、不独立重许被引全文／数据／代码／模型／媒体／商标／源模板或整个source归档。Fig2仅a/b的原permission与[9]印刷出处、BioRender Fig5a/c/6a/7a/8a/f/g准确保留；外部SD1–7与data/code/trajectory排除。 此范围也包含该PDF native plain、页selectors及完整BY4 NOTICE；旧 root rights／block／retrieval／revision／source_version键缺省和历史原件／文字缺失不改；无普遍权利保证。

### LinkML schema-first knowledge modeling (`methodology:linkml-schema-first`)

- Components: `claim:583280271287ef9c`
- Source revision: `sha256:93a9f00b0006695dab8f1bde801a40e36eed8c236c4c839aff645bec38b5dc6c`
- Source version: [pinned upstream version](https://linkml.io/linkml/)
- License: [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)
- NOTICE: [raw_data/licenses/apache-2.0.md](../../../../raw_data/licenses/apache-2.0.md)
- Attribution: This document includes material copied from or derived from "LinkML Documentation", https://linkml.io/linkml/. Copyright 2021-2026 LinkML Authors. SPDX-License-Identifier: Apache-2.0. Licensed under the Apache License, Version 2.0, https://www.apache.org/licenses/LICENSE-2.0.
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. Converted the captured LinkML HTML landing page to Markdown; navigation, headings, hyperlinks, whitespace, and footnote markers were omitted or normalized, while CSS, JavaScript, theme files, and media were not stored; 164 selector excerpts were generated. The upstream copyright and Apache-2.0 statement are restored in this attribution block.
- Scope: 仅覆盖当前 https://linkml.io/linkml/ 单页经转换后、许可附注前的 7,340-byte 既有 Markdown 正文及其 164 个 selector 摘录；不声称存储或覆盖 LinkML 整个文档站、其他页面正文、主题、JavaScript、CSS、媒体、外链作品、商标或权利人无权许可的第三方材料。

### FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (`arxiv:2305.14251`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models (`arxiv:2402.14207`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### MLGym: A New Framework and Benchmark for Advancing AI Research Agents (`arxiv:2502.14499`)

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

### linkml/linkml (`github:linkml/linkml`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### xoai/sage-wiki (`github:xoai/sage-wiki`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

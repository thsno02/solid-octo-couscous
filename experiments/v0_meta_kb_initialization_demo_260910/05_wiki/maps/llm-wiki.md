---
uid: wiki-page:map-llm-wiki
title: Llm Wiki
slug: maps/llm-wiki
page_type: map
status: review
summary: Routing map for llm wiki sources, questions, and claims.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:1929edca74fa3fa5
- claim:55eeb2a1683b8804
- claim:6f5fa83ca484f664
- claim:714e301e8b2162bc
- claim:9a3b21da11a96956
- claim:9f0a3dc6de4c7f84
- claim:b281f7d7bc21b10d
- claim:bc9a34bd8a9c7154
- claim:bed2f056ecd73c69
- claim:c4f2def09ea56d98
- claim:e7026275c099e7e2
- claim:e7ac7da9ac39e47d
source_refs: &id001
- arxiv:2402.14207
- arxiv:2509.23233
- github:VectifyAI/OpenKB
- arxiv:2305.14627
- arxiv:2305.14251
- github:xoai/sage-wiki
page_refs:
- wiki-page:source-7fabb86557bf2f15
- wiki-page:source-e27d5b13b062021d
- wiki-page:source-332922100755365f
- wiki-page:source-51388aa8e2e8587f
- wiki-page:source-dd60addc5fe69a87
- wiki-page:source-a41aba6e720b278f
- wiki-page:llm-wiki-overview
- wiki-page:grounded-long-form-synthesis
outgoing_links:
- target: wiki-page:source-7fabb86557bf2f15
  relation: explains
  claim_refs:
  - claim:1929edca74fa3fa5
  - claim:55eeb2a1683b8804
  notes: null
- target: wiki-page:source-e27d5b13b062021d
  relation: explains
  claim_refs:
  - claim:bc9a34bd8a9c7154
  - claim:6f5fa83ca484f664
  notes: null
- target: wiki-page:source-332922100755365f
  relation: explains
  claim_refs:
  - claim:e7026275c099e7e2
  - claim:714e301e8b2162bc
  notes: null
- target: wiki-page:source-51388aa8e2e8587f
  relation: explains
  claim_refs:
  - claim:bed2f056ecd73c69
  - claim:9a3b21da11a96956
  notes: null
- target: wiki-page:source-dd60addc5fe69a87
  relation: explains
  claim_refs:
  - claim:b281f7d7bc21b10d
  - claim:9f0a3dc6de4c7f84
  notes: null
- target: wiki-page:source-a41aba6e720b278f
  relation: explains
  claim_refs:
  - claim:e7ac7da9ac39e47d
  - claim:c4f2def09ea56d98
  notes: null
- target: wiki-page:llm-wiki-overview
  relation: related
  claim_refs:
  - claim:1929edca74fa3fa5
  - claim:55eeb2a1683b8804
  - claim:6f5fa83ca484f664
  - claim:714e301e8b2162bc
  - claim:9a3b21da11a96956
  - claim:9f0a3dc6de4c7f84
  notes: null
- target: wiki-page:grounded-long-form-synthesis
  relation: related
  claim_refs:
  - claim:1929edca74fa3fa5
  - claim:55eeb2a1683b8804
  - claim:6f5fa83ca484f664
  - claim:714e301e8b2162bc
  - claim:9a3b21da11a96956
  - claim:9f0a3dc6de4c7f84
  notes: null
sections:
- heading: Source coverage
  claim_refs: []
  source_refs: *id001
  editorial_intent: Route by source family.
- heading: Source-reported signals
  claim_refs:
  - claim:1929edca74fa3fa5
  - claim:b281f7d7bc21b10d
  - claim:bc9a34bd8a9c7154
  - claim:bed2f056ecd73c69
  - claim:e7026275c099e7e2
  - claim:e7ac7da9ac39e47d
  source_refs:
  - arxiv:2402.14207
  - arxiv:2305.14251
  - arxiv:2509.23233
  - arxiv:2305.14627
  - github:VectifyAI/OpenKB
  - github:xoai/sage-wiki
  editorial_intent: Preserve source-authored scope.
- heading: Collector assessments
  claim_refs:
  - claim:55eeb2a1683b8804
  - claim:6f5fa83ca484f664
  - claim:714e301e8b2162bc
  - claim:9a3b21da11a96956
  - claim:9f0a3dc6de4c7f84
  - claim:c4f2def09ea56d98
  source_refs:
  - arxiv:2402.14207
  - arxiv:2509.23233
  - github:VectifyAI/OpenKB
  - arxiv:2305.14627
  - arxiv:2305.14251
  - github:xoai/sage-wiki
  editorial_intent: Preserve collector scope.
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
  - arxiv:2402.14207@sha256:28b57e9821da798bf8ccfa3f144bfa37cd96ff3582c2211c83eff5ffcf0ccfc2
  - arxiv:2509.23233@sha256:8570de4224cfc829f7478411feca2ecec5f50d6e7ceb7cc62fd15fa07f20c921
  - github:VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc
  - arxiv:2305.14627@sha256:ae9868f07f0f7ffaae5346778f79b7827d9ec6b13b1e6aae4dff6b2ffc37a2e1
  - arxiv:2305.14251@sha256:57414a8d80031dceed44fb17efa562cab7e1490390ce95d8753480fba9686795
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
    one_line: Routing map for llm wiki sources, questions, and claims.
    short: Routing map for llm wiki sources, questions, and claims.
    full: null
  estimated_tokens: 1346
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:1929edca74fa3fa5
- claim:55eeb2a1683b8804
- claim:6f5fa83ca484f664
- claim:714e301e8b2162bc
- claim:9a3b21da11a96956
- claim:9f0a3dc6de4c7f84
- claim:b281f7d7bc21b10d
- claim:bc9a34bd8a9c7154
- claim:bed2f056ecd73c69
- claim:c4f2def09ea56d98
- claim:e7026275c099e7e2
- claim:e7ac7da9ac39e47d
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
rights_unavailable_source_refs:
- arxiv:2305.14251
- arxiv:2402.14207
- arxiv:2509.23233
- github:VectifyAI/OpenKB
- github:xoai/sage-wiki
---

# Llm Wiki

Grounded long-form compilation, citation-aware writing, and human-steerable exploration.

## Routing questions

- How should research precede writing?
- How do paragraph citations expand to atomic evidence?
- How are multiple perspectives and unknown unknowns handled?

## Source coverage

| Source | Type | Tier | Claims |
|---|---|---|---|
| [Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models](../sources/arxiv-2402.14207.md) | `arxiv` | `full_text` | 2 |
| [Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models](../sources/arxiv-2509.23233.md) | `arxiv` | `full_text` | 2 |
| [VectifyAI/OpenKB](../sources/github-vectifyai-openkb.md) | `github` | `semantic_capsule` | 2 |
| [Enabling Large Language Models to Generate Text with Citations](../sources/arxiv-2305.14627.md) | `arxiv` | `full_text` | 2 |
| [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](../sources/arxiv-2305.14251.md) | `arxiv` | `full_text` | 2 |
| [xoai/sage-wiki](../sources/github-xoai-sage-wiki.md) | `github` | `semantic_capsule` | 2 |

## Source-reported signals

- **Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models** (source assertion): We study how to apply large language models to write grounded and organized long-form articles from scratch, with comparable breadth and depth to Wikipedia pages. This underexplored problem poses new challenges at the pre-writing stage, including how to research the topic and prepare an outline prior to writing. 〔[claim:1929edca74fa3fa5](../claims/claim-1929edca74fa3fa5.md)〕
- **FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation** (source assertion): Evaluating the factuality of long-form text generated by large language models (LMs) is non-trivial because (1) generations often contain a mixture of supported and unsupported pieces of information, making binary judgments of quality inadequate, and (2) human evaluation is time-consuming and costly. In this paper, we introduce , a new evaluation that breaks a generation into a series of atomic facts and computes the 〔[claim:b281f7d7bc21b10d](../claims/claim-b281f7d7bc21b10d.md)〕
- **Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models** (source assertion): Wikipedia is the largest open knowledge corpus, widely used worldwide and serving as a key resource for training large language models (LLMs) and retrieval-augmented generation (RAG) systems. Ensuring its accuracy is therefore critical. 〔[claim:bc9a34bd8a9c7154](../claims/claim-bc9a34bd8a9c7154.md)〕
- **Enabling Large Language Models to Generate Text with Citations** (source assertion): Large language models (LLMs) have emerged as a widely-used tool for information seeking, but their generated outputs are prone to halluci- nation. In this work, our aim is to allow LLMs to generate text with citations, improving their factual correctness and verifiability. 〔[claim:bed2f056ecd73c69](../claims/claim-bed2f056ecd73c69.md)〕
- **VectifyAI/OpenKB** (source assertion): **OpenKB (Open Knowledge Base)** is an open-source system (in CLI) that compiles raw documents into a structured, interlinked wiki-style knowledge base using LLMs, powered by [**PageIndex**](https://github.com/VectifyAI/PageIndex)'s vectorless, reasoning-based retrieval for long documents. 〔[claim:e7026275c099e7e2](../claims/claim-e7026275c099e7e2.md)〕
- **xoai/sage-wiki** (source assertion): **sage-wiki** is a graph memory and knowledge base that AI agents and humans build and query together. Drop in documents; an LLM compiler turns them into an interlinked wiki with a knowledge graph — agents query it through MCP, humans browse it as plain markdown. 〔[claim:e7ac7da9ac39e47d](../claims/claim-e7ac7da9ac39e47d.md)〕

## Collector assessments

- **Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models** (collection assessment): STORM is a central academic reference for multi-perspective research, outline construction, grounded long-form synthesis, and editor-informed evaluation. 〔[claim:55eeb2a1683b8804](../claims/claim-55eeb2a1683b8804.md)〕
- **Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models** (collection assessment): CLAIRE and WikiCollide make corpus-level inconsistency detection a first-class maintenance task and demonstrate human-editor review as part of the loop. 〔[claim:6f5fa83ca484f664](../claims/claim-6f5fa83ca484f664.md)〕
- **VectifyAI/OpenKB** (collection assessment): A CLI knowledge compiler with wiki foundation and downstream generators, hierarchical long-document retrieval, linting, source removal and skill compilation. 〔[claim:714e301e8b2162bc](../claims/claim-714e301e8b2162bc.md)〕
- **Enabling Large Language Models to Generate Text with Citations** (collection assessment): ALCE provides reproducible citation-quality metrics across correctness, completeness, and fluency, directly applicable to wiki admission gates. 〔[claim:9a3b21da11a96956](../claims/claim-9a3b21da11a96956.md)〕
- **FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation** (collection assessment): Supplies an atomic-fact evaluation primitive needed to assess factual precision of long-form wiki pages rather than judging a page as one block. 〔[claim:9f0a3dc6de4c7f84](../claims/claim-9f0a3dc6de4c7f84.md)〕
- **xoai/sage-wiki** (collection assessment): A graph-aware compiled wiki emphasizing evidenced relations, source spans, bi-temporal edges, review-gated entity resolution, output quarantine and agent access through MCP. 〔[claim:c4f2def09ea56d98](../claims/claim-c4f2def09ea56d98.md)〕

## Current synthesis boundary

The map routes candidate evidence; it does not flatten sources into consensus or resolve contradictions automatically.

## Related pages

- [Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models](../sources/arxiv-2402.14207.md) — `explains`
- [Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models](../sources/arxiv-2509.23233.md) — `explains`
- [VectifyAI/OpenKB](../sources/github-vectifyai-openkb.md) — `explains`
- [Enabling Large Language Models to Generate Text with Citations](../sources/arxiv-2305.14627.md) — `explains`
- [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](../sources/arxiv-2305.14251.md) — `explains`
- [xoai/sage-wiki](../sources/github-xoai-sage-wiki.md) — `explains`
- [LLM Wiki overview](../overviews/llm-wiki.md) — `related`
- [Grounded long-form synthesis](../methods/grounded-synthesis.md) — `related`

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

### FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (`arxiv:2305.14251`)

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

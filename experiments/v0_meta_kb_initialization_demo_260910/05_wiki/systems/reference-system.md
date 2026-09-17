---
uid: wiki-page:llm-wiki-reference-system
title: LLM Wiki reference system
slug: systems/reference-system
page_type: system
status: review
summary: End-to-end architecture from frozen sources to reviewed pages and context packs.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id002
- claim:4bf5ea8e6b4e37de
- claim:84c91602bd1dfb78
- claim:ecdd2719fa55751c
- claim:07439fdff0cc0aa3
- claim:12237a4df4847d59
- claim:a67432ee7afb1535
- claim:bc85c4d0c6801c3a
- claim:ef04f2ebbd2da425
- claim:1929edca74fa3fa5
- claim:b281f7d7bc21b10d
- claim:bc9a34bd8a9c7154
- claim:bed2f056ecd73c69
source_refs: &id001
- arxiv:2502.14499
- arxiv:2406.06769
- arxiv:2602.06855
- arxiv:2503.18102
- arxiv-1706.08840
- arxiv-2306.15626
- github:getzep/graphiti
- arxiv:2501.13956
- arxiv:2402.14207
- arxiv:2305.14251
- arxiv:2509.23233
- arxiv:2305.14627
page_refs:
- wiki-page:claim-evidence-page-compilation
- wiki-page:context-pack-routing
- wiki-page:freshness-versioning-and-rollback
- wiki-page:v0-quality-gates
outgoing_links:
- target: wiki-page:claim-evidence-page-compilation
  relation: depends_on
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:84c91602bd1dfb78
  - claim:ecdd2719fa55751c
  - claim:07439fdff0cc0aa3
  - claim:12237a4df4847d59
  - claim:a67432ee7afb1535
  notes: null
- target: wiki-page:context-pack-routing
  relation: depends_on
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:84c91602bd1dfb78
  - claim:ecdd2719fa55751c
  - claim:07439fdff0cc0aa3
  - claim:12237a4df4847d59
  - claim:a67432ee7afb1535
  notes: null
- target: wiki-page:freshness-versioning-and-rollback
  relation: depends_on
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:84c91602bd1dfb78
  - claim:ecdd2719fa55751c
  - claim:07439fdff0cc0aa3
  - claim:12237a4df4847d59
  - claim:a67432ee7afb1535
  notes: null
- target: wiki-page:v0-quality-gates
  relation: evaluates
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:84c91602bd1dfb78
  - claim:ecdd2719fa55751c
  - claim:07439fdff0cc0aa3
  - claim:12237a4df4847d59
  - claim:a67432ee7afb1535
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
  build_id: build:llm-wiki-v0:4e541384e82b1271
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2502.14499@sha256:de8bc15be762914dd2f056f00efe2b83d51ce852a7035d65e866e6cdecbbb65a
  - arxiv:2406.06769@sha256:28793ae05bbb22ed6e02fbdceb697a2b9ea8ebff6932c4dd8fb5b70bba5dde91
  - arxiv:2602.06855@sha256:ac1ba940f1bdc54e012cc384c428f78bd01d50d7a947f052117944c03e790d9a
  - arxiv:2503.18102@sha256:762045781a10140f714e0f23388014286a50cce79f385d6b4a1475162cce9669
  - arxiv-1706.08840@sha256:330858b30f0963297c9d772fc29aabc8dfcff7d687856d91a2f167847d0fca88
  - arxiv-2306.15626@sha256:5893d0b64b077ec01bee907ead6d94ae8c810abf023c2b4f618250c4fb0b7680
  - github:getzep/graphiti@c035afb7990b6077331a81e98b04efcfd9bf8184
  - arxiv:2501.13956@sha256:d98c3a619caf66173e92e9a21829b32312db83156e30ede9e6bb45c1c6016d51
  - arxiv:2402.14207@sha256:28b57e9821da798bf8ccfa3f144bfa37cd96ff3582c2211c83eff5ffcf0ccfc2
  - arxiv:2305.14251@sha256:57414a8d80031dceed44fb17efa562cab7e1490390ce95d8753480fba9686795
  - arxiv:2509.23233@sha256:8570de4224cfc829f7478411feca2ecec5f50d6e7ceb7cc62fd15fa07f20c921
  - arxiv:2305.14627@sha256:ae9868f07f0f7ffaae5346778f79b7827d9ec6b13b1e6aae4dff6b2ffc37a2e1
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
    one_line: End-to-end architecture from frozen sources to reviewed pages and context packs.
    short: End-to-end architecture from frozen sources to reviewed pages and context packs.
    full: null
  estimated_tokens: 2258
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:4bf5ea8e6b4e37de
- claim:84c91602bd1dfb78
- claim:ecdd2719fa55751c
- claim:07439fdff0cc0aa3
- claim:12237a4df4847d59
- claim:a67432ee7afb1535
- claim:bc85c4d0c6801c3a
- claim:ef04f2ebbd2da425
- claim:1929edca74fa3fa5
- claim:b281f7d7bc21b10d
- claim:bc9a34bd8a9c7154
- claim:bed2f056ecd73c69
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
- source_uid: arxiv:2501.13956
  source_revision: sha256:d98c3a619caf66173e92e9a21829b32312db83156e30ede9e6bb45c1c6016d51
  source_version_url: https://arxiv.org/abs/2501.13956v1
  license_spdx: CC-BY-NC-SA-4.0
  license_url: https://creativecommons.org/licenses/by-nc-sa/4.0/
  notice_path: raw_data/licenses/arxiv-cc-by-nc-sa-4.0-prime-cc-by-4.0-george-kour-mit.md
  package_path: materialized_sources/corpus/arxiv-2501.13956--b93a114f/manifest.yaml#rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:ef04f2ebbd2da425
- source_uid: arxiv:2503.18102
  source_revision: sha256:762045781a10140f714e0f23388014286a50cce79f385d6b4a1475162cce9669
  source_version_url: https://arxiv.org/pdf/2503.18102v1
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: materialized_sources/corpus/arxiv-2503.18102--1133e9d5/pdf-supplement/NOTICE.md
  package_path: materialized_sources/corpus/arxiv-2503.18102--1133e9d5/manifest.yaml#pdf_supplement.rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:07439fdff0cc0aa3
rights_unavailable_source_refs:
- arxiv-1706.08840
- arxiv-2306.15626
- arxiv:2305.14251
- arxiv:2402.14207
- arxiv:2502.14499
- arxiv:2509.23233
- arxiv:2602.06855
- github:getzep/graphiti
---

# LLM Wiki reference system

## Purpose

End-to-end architecture from frozen sources to reviewed pages and context packs.

## Candidate evidence

- **MLGym: A New Framework and Benchmark for Advancing AI Research Agents** (source assertion): We introduce Meta and -Bench, a new framework and benchmark for evaluating and developing LLM agents on AI research tasks. This is the first Gym environment for machine learning (ML) tasks, enabling research on reinforcement learning (RL) algorithms for training such agents. 〔[claim:4bf5ea8e6b4e37de](../claims/claim-4bf5ea8e6b4e37de.md)〕
- **DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents** (source assertion): Automated scientific discovery promises to accelerate progress across scientific domains. However, developing and evaluating an AI agent’s capacity for end- to-end scientific reasoning is challenging as running real-world experiments is often prohibitively expensive or infeasible. 〔[claim:84c91602bd1dfb78](../claims/claim-84c91602bd1dfb78.md)〕
- **AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents** (source assertion): LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we introduce ~(the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine learning papers. 〔[claim:ecdd2719fa55751c](../claims/claim-ecdd2719fa55751c.md)〕
- **AgentRxiv: Towards Collaborative Autonomous Research** (source assertion): Progress in scientific discovery is rarely the result of a single "Eureka" moment, but is rather the product of hundreds of scientists incrementally working together toward a common goal. While existing agent workflows are capable of producing research autonomously, they do so in isolation, without the ability to continuously improve upon prior research results. 〔[claim:07439fdff0cc0aa3](../claims/claim-07439fdff0cc0aa3.md)〕
- **Gradient Episodic Memory for Continual Learning** (source assertion): One major obstacle towards AI is the poor ability of models to solve new problems quicker, and without forgetting previously acquired knowledge. To better understand this issue, we study the problem of continual learning, where the model observes, once and one by one, examples concerning a sequence of tasks. 〔[claim:12237a4df4847d59](../claims/claim-12237a4df4847d59.md)〕
- **LeanDojo: Theorem Proving with Retrieval-Augmented Language Models** (source assertion): Large language models (LLMs) have shown promise in proving formal theorems using proof assistants such as Lean. However, existing methods are difficult to reproduce or build on, due to private code, data, and large compute requirements. 〔[claim:a67432ee7afb1535](../claims/claim-a67432ee7afb1535.md)〕
- **getzep/graphiti** (source assertion): ⭐ *Help us reach more developers and grow the Graphiti community. 〔[claim:bc85c4d0c6801c3a](../claims/claim-bc85c4d0c6801c3a.md)〕
- **Zep: A Temporal Knowledge Graph Architecture for Agent Memory** (source assertion): We introduce Zep, a novel memory layer service for AI agents that outperforms the current state-of-the-art system, MemGPT, in the Deep Memory Retrieval (DMR) benchmark. Additionally, Zep excels in more comprehensive and challenging evaluations than DMR that better reflect real-world enterprise use cases. 〔[claim:ef04f2ebbd2da425](../claims/claim-ef04f2ebbd2da425.md)〕
- **Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models** (source assertion): We study how to apply large language models to write grounded and organized long-form articles from scratch, with comparable breadth and depth to Wikipedia pages. This underexplored problem poses new challenges at the pre-writing stage, including how to research the topic and prepare an outline prior to writing. 〔[claim:1929edca74fa3fa5](../claims/claim-1929edca74fa3fa5.md)〕
- **FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation** (source assertion): Evaluating the factuality of long-form text generated by large language models (LMs) is non-trivial because (1) generations often contain a mixture of supported and unsupported pieces of information, making binary judgments of quality inadequate, and (2) human evaluation is time-consuming and costly. In this paper, we introduce , a new evaluation that breaks a generation into a series of atomic facts and computes the 〔[claim:b281f7d7bc21b10d](../claims/claim-b281f7d7bc21b10d.md)〕
- **Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models** (source assertion): Wikipedia is the largest open knowledge corpus, widely used worldwide and serving as a key resource for training large language models (LLMs) and retrieval-augmented generation (RAG) systems. Ensuring its accuracy is therefore critical. 〔[claim:bc9a34bd8a9c7154](../claims/claim-bc9a34bd8a9c7154.md)〕
- **Enabling Large Language Models to Generate Text with Citations** (source assertion): Large language models (LLMs) have emerged as a widely-used tool for information seeking, but their generated outputs are prone to halluci- nation. In this work, our aim is to allow LLMs to generate text with citations, improving their factual correctness and verifiability. 〔[claim:bed2f056ecd73c69](../claims/claim-bed2f056ecd73c69.md)〕

## Compiled interpretation

This page reorganizes candidate knowledge around a stable reader task. It is not source concatenation and it does not turn retrieval, maintainer claims, preprints, or generated prose into verified truth.

## Review boundary

Check evidence entailment, source independence, contradiction, neutrality, due weight, freshness, and downstream impact before publication.

## Architecture

```text
immutable source revisions
→ normalized artifacts and selectors
→ atomic claims and evidence
→ identity and ontology mapping
→ PagePlan and candidate Markdown
→ deterministic and semantic evaluation
→ review and admission
→ indexes, graph, context packs, and change feed
```

## Related pages

- [Claim–evidence–page compilation](../methods/claim-evidence-page.md) — `depends_on`
- [Context-pack routing](../methods/context-pack-routing.md) — `depends_on`
- [Freshness, versioning, and rollback](../concepts/freshness-versioning-rollback.md) — `depends_on`
- [v0 LLM Wiki quality gates](../evaluations/v0-quality-gates.md) — `evaluates`

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

### Zep: A Temporal Knowledge Graph Architecture for Agent Memory (`arxiv:2501.13956`)

- Components: `claim:ef04f2ebbd2da425`
- Source revision: `sha256:d98c3a619caf66173e92e9a21829b32312db83156e30ede9e6bb45c1c6016d51`
- Source version: [pinned upstream version](https://arxiv.org/abs/2501.13956v1)
- License: [CC-BY-NC-SA-4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- NOTICE: [raw_data/licenses/arxiv-cc-by-nc-sa-4.0-prime-cc-by-4.0-george-kour-mit.md](../../../../raw_data/licenses/arxiv-cc-by-nc-sa-4.0-prime-cc-by-4.0-george-kour-mit.md)
- Attribution: "Zep: A Temporal Knowledge Graph Architecture for Agent Memory", arXiv:2501.13956v1, by Preston Rasmussen; Pavlo Paliychuk; Travis Beauvais; Jack Ryan; and Daniel Chalef. Source: https://arxiv.org/abs/2501.13956v1. The article-author material is licensed under CC BY-NC-SA 4.0: https://creativecommons.org/licenses/by-nc-sa/4.0/. This repository has not yet verified that its intended publication is NonCommercial; this package is not a publication approval. source/PRIMEarxiv.sty corresponds to the Arxiv & PRIME AI Style Template adapted by Moulay A. Akhloufi, https://www.overleaf.com/latex/templates/arxiv-and-prime-ai-style-template/qdnhqytdqzsc, licensed under CC BY 4.0: https://creativecommons.org/licenses/by/4.0/. That adaptation is based on George Kour's arxiv-style, https://github.com/kourgeorge/arxiv-style; its base portions retain Copyright (c) 2020 George Kour and the MIT License. The retained Zep style enables the page footer that the otherwise matching PaperQA2 copy comments out; the modifier of this one-line variant is unknown and is not attributed to the paper authors.
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. The fixed v1 source archive is unpacked and its four text members—source/main.tex, source/main.bbl, source/references.bib, and source/PRIMEarxiv.sty—are retained without modification. main.tex is copied to normalized/document.tex and converted to normalized/document.txt; 29 selectors are generated; the article attribution, Moulay A. Akhloufi template attribution, George Kour MIT notice, modification statement, and NOTICE link are appended to normalized/document.txt. For provenance, the retained Zep PRIMEarxiv.sty is recorded as differing from the otherwise matching PaperQA2 copy only at line 35 by enabling the page footer; this packaging does not identify the author of that pre-existing variant.
- Scope: 本组合包仅覆盖固定 arXiv v1 胶囊实际保存的四个 source 文字成员、normalized/document.tex、normalized/document.txt 与 29 个 selector。论文作者材料及其文本转换和 selector 派生物按 CC BY-NC-SA 4.0 履约，任何共享仅限非商业用途，派生输出须采用同一或兼容许可；当前仓库用途尚未完成非商业核实，故本包不表示发布已获准，未来商业用途须另行取得授权。source/PRIMEarxiv.sty 作为 Moulay A. Akhloufi 改编的 PRIME 模板按 CC BY 4.0 履约，并对其所基于的 George Kour arxiv-style 保留 MIT 版权和许可；Zep 所存版本相对 PaperQA2 对应副本仅启用第 35 行页脚，本包记录该差异但不把修改归给论文作者。main.bbl 与 references.bib 作为排版记录和引用元数据保留，不授权其所引用作品。许可不外推到外链论文、代码、数据或权利人无权许可的第三方材料。

### AgentRxiv: Towards Collaborative Autonomous Research (`arxiv:2503.18102`)

- Components: `claim:07439fdff0cc0aa3`
- Source revision: `sha256:762045781a10140f714e0f23388014286a50cce79f385d6b4a1475162cce9669`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2503.18102v1)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [materialized_sources/corpus/arxiv-2503.18102--1133e9d5/pdf-supplement/NOTICE.md](../../../../materialized_sources/corpus/arxiv-2503.18102--1133e9d5/pdf-supplement/NOTICE.md)
- Attribution: Samuel Schmidgall; Michael Moor, AgentRxiv: Towards Collaborative Autonomous Research, arXiv:2503.18102v1 (2025-03-23), https://arxiv.org/abs/2503.18102v1, PDF https://arxiv.org/pdf/2503.18102v1, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/。实际当前PDF两作者按序Samuel Schmidgall; Michael Moor。1 Department of Electrical & Computer Engineering, Johns Hopkins University；2 Department of Biosystems Science & Engineering, ETH Zurich；Samuel Schmidgall通讯sschmi46@jhu.edu。固定v1侧边日期23 Mar 2025与题名页右上2025-3-25独立保留，不以pagehead或Creation/ModDate覆盖提交事实。p27 National Science Foundation Graduate Research Fellowship, Grant No. DGE 2139757支持信用保留，不暗示NSF/作者/机构背书。p1 Figure1网页列表截图另文Agent Laboratory: Using LLM Agents as Research Assistants，实际九作者按序Samuel Schmidgall、Yusheng Su、Ze Wang、Ximeng Sun、Jialian Wu、Xiaodong Yu、Jiang Liu、Zicheng Liu、Emad Barsoum，不含Michael Moor、不混入当前两作者。图中打印arXiv:2501.04227 [pdf, other]为bare ID、没有vN或完整URL；有限六显示行约52个空白tokens摘要预览起Historically, scientific discovery...，止accepts a human-provide...并有More，是原图已截断预览、非完整摘要/全文。若需定位 https://arxiv.org/abs/2501.04227 只按可见ID生成locator，不称本批核定另文固定版/取得全文；p24书目独立信用、Figures2/3研究上下文按原件保留。当前p1 AgentRxiv.github.io项目链接保留。只保存本PDF中实际有限展示与信用，不单独再许可另篇整文或底层媒体，也不新增抓取/许可函退出条件。以上归属不暗示背书。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 本次唯一固定版GET的2757188 bytes原PDF按字节原样保留，不编辑/重导/重排/OCR。既有helper以plain全页提取生成独立pdf-supplement/document.txt与实际新PDF revision绑定的逐页selectors；页标题/定位和唯一文末归属/修改/范围footer为collector表示元数据，native不是作者另交原始文本或byte-exact executable prompt/code。NOTICE自包含实际署名/独立信用/来源/范围/损失与既有完整CC BY4法律文本，notice_path自绑定本文件，不新rawlicense资产。本primary_excerpt仅声明同一native Page1实际父摘要L9–23，不修改原文。旧root source/normalized/selectors/NOTICE/README/files及revision/retrieval/rights/gate/source_version键缺省不改，不把新选版回溯为旧bare archive GET的已证版次。
- Scope: 本独立表示只覆盖本UID固定arXiv:2503.18102v1原bytes不改的29页compiled PDF（2757188 bytes）：固定arXiv:2503.18102v1完整29物理页编译论文：p1父摘要/Figure1，p2–17主文、六活动图、单/三实验室结果、Failure/Ethics/Discussion/实际Conclusion，p17–27 References，p27 Acknowledgments，p28 A.Algorithms与B.Agent Laboratory configuration，p29配置表/B.3/真实C.Prompts结尾。末句All prompts are the same as in Schmidgall et al. (2025).是正常引用，原件未列另一论文完整prompt，不递归取另文。 论文作者可许可表达依本固定作品已证CC BY4路径；图表/参考文献/实际有限引述保存其原信用，不外推standalone被引作品/素材/程序/代码/数据/媒体/服务/模型/权重/模板的一般许可。范围含该PDF派生有损native plain、revision-bound逐页selectors及完整NOTICE；不执行被审指令、不重新打包外链、不改变底层许可、不为已许可权利添加下游限制，无普遍权利保证，不授商标/专利。当前原图有限另文列表/截图/摘要预览在此出版表示内原样保留并落实九作者与bareID信用，不扩大为另文独立全文或底层图片/角色/程序/数据的一般许可。旧bib LUMI-lab长摘要和competing-interest/patent声明未在此实际PDF出现；p4简短介绍/p18普通书目不等于旧完整摘要，其NC-ND用途/转换条件与旧GDM BY-SA4、ICLR/LPPL等组件/root block保持，不外推到整个新PDF也不因新BY4放行旧source。

### Gradient Episodic Memory for Continual Learning (`arxiv-1706.08840`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### LeanDojo: Theorem Proving with Retrieval-Augmented Language Models (`arxiv-2306.15626`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

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

### getzep/graphiti (`github:getzep/graphiti`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

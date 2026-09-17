---
uid: wiki-page:knowledge-evolution-loop
title: Knowledge evolution loop
slug: concepts/knowledge-evolution-loop
page_type: concept
status: review
summary: Evidence, conflict, review, admission, monitoring, and rollback form one governed loop.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id002
- claim:4bf5ea8e6b4e37de
- claim:84c91602bd1dfb78
- claim:ecdd2719fa55751c
- claim:c776b87484aab5c2
- claim:df1b88d18276a319
- claim:ecf45fd3f4ab576a
- claim:2a05950fe0a0b64d
- claim:ae45b8d667e29552
- claim:b0434511c0c174ad
- claim:d38b49dc4376d4b0
- claim:f810d086e0a4a305
- claim:17c715b34b0f0c68
source_refs: &id001
- arxiv:2502.14499
- arxiv:2406.06769
- arxiv:2602.06855
- arxiv:2507.21046
- arxiv:2404.14387
- arxiv:2502.12110
- arxiv:cs/0309048
- arxiv:2505.22954
- arxiv:2406.04268
- github:jennyzzt/dgm
- arxiv:2410.04444
page_refs:
- wiki-page:map-recursive-self-improvement
- wiki-page:map-open-ended-evolution
- wiki-page:freshness-versioning-and-rollback
outgoing_links:
- target: wiki-page:map-recursive-self-improvement
  relation: related
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:84c91602bd1dfb78
  - claim:ecdd2719fa55751c
  - claim:c776b87484aab5c2
  - claim:df1b88d18276a319
  - claim:ecf45fd3f4ab576a
  notes: null
- target: wiki-page:map-open-ended-evolution
  relation: related
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:84c91602bd1dfb78
  - claim:ecdd2719fa55751c
  - claim:c776b87484aab5c2
  - claim:df1b88d18276a319
  - claim:ecf45fd3f4ab576a
  notes: null
- target: wiki-page:freshness-versioning-and-rollback
  relation: extends
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:84c91602bd1dfb78
  - claim:ecdd2719fa55751c
  - claim:c776b87484aab5c2
  - claim:df1b88d18276a319
  - claim:ecf45fd3f4ab576a
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
  build_id: build:llm-wiki-v0:3c4b53aa61004c0b
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2502.14499@sha256:de8bc15be762914dd2f056f00efe2b83d51ce852a7035d65e866e6cdecbbb65a
  - arxiv:2406.06769@sha256:28793ae05bbb22ed6e02fbdceb697a2b9ea8ebff6932c4dd8fb5b70bba5dde91
  - arxiv:2602.06855@sha256:ac1ba940f1bdc54e012cc384c428f78bd01d50d7a947f052117944c03e790d9a
  - arxiv:2507.21046@sha256:0b39df03feea2f4d8ac41e35a9247889978a53cb1e7b7d3eafaae76ad97b5602
  - arxiv:2404.14387@sha256:afd13bcb8ce6f553dec268c0fb17bfb6b8a1ba80a4881a5b46d54b927ca9a418
  - arxiv:2502.12110@sha256:d112e92606a562a0369e2e8cddadad88ac8d448d66c24ee9b63e808c2c84e42b
  - arxiv:cs/0309048@sha256:ab75c69deb1c4b41ae77f5f817735922ad52fc9a8d51ec5184f4978a88b4052e
  - arxiv:2505.22954@sha256:13ff4abe0c7ad4a7dd3b4876d19a8bf940e39e70dabbf06065aa774a6c3457de
  - arxiv:2406.04268@sha256:151c2d39de074a44985b681977a2a5383b91932b87eb734709948e9eb1607871
  - github:jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2
  - arxiv:2410.04444@sha256:d33fb4b64b53231411e0d14e65e6a3fc4f3dbfbcfe3ab4b5113f8ffa8c16cd52
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
    one_line: Evidence, conflict, review, admission, monitoring, and rollback form one governed loop.
    short: Evidence, conflict, review, admission, monitoring, and rollback form one governed loop.
    full: null
  estimated_tokens: 1882
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:4bf5ea8e6b4e37de
- claim:84c91602bd1dfb78
- claim:ecdd2719fa55751c
- claim:c776b87484aab5c2
- claim:df1b88d18276a319
- claim:ecf45fd3f4ab576a
- claim:2a05950fe0a0b64d
- claim:ae45b8d667e29552
- claim:b0434511c0c174ad
- claim:d38b49dc4376d4b0
- claim:f810d086e0a4a305
- claim:17c715b34b0f0c68
rights_refs:
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
- source_uid: arxiv:2505.22954
  source_revision: sha256:13ff4abe0c7ad4a7dd3b4876d19a8bf940e39e70dabbf06065aa774a6c3457de
  source_version_url: https://arxiv.org/pdf/2505.22954v3
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: raw_data/licenses/cc-by-4.0.md
  package_path: materialized_sources/corpus/arxiv-2505.22954--8a7041cb/manifest.yaml#pdf_supplement.rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:ae45b8d667e29552
- source_uid: arxiv:2507.21046
  source_revision: sha256:0b39df03feea2f4d8ac41e35a9247889978a53cb1e7b7d3eafaae76ad97b5602
  source_version_url: https://arxiv.org/pdf/2507.21046v4
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: raw_data/licenses/cc-by-4.0.md
  package_path: materialized_sources/corpus/arxiv-2507.21046--f477f5c3/manifest.yaml#pdf_supplement.rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:c776b87484aab5c2
rights_unavailable_source_refs:
- arxiv:2404.14387
- arxiv:2406.04268
- arxiv:2410.04444
- arxiv:2502.12110
- arxiv:2502.14499
- arxiv:2602.06855
- arxiv:cs/0309048
- github:jennyzzt/dgm
---

# Knowledge evolution loop

## Purpose

Evidence, conflict, review, admission, monitoring, and rollback form one governed loop.

## Candidate evidence

- **MLGym: A New Framework and Benchmark for Advancing AI Research Agents** (source assertion): We introduce Meta and -Bench, a new framework and benchmark for evaluating and developing LLM agents on AI research tasks. This is the first Gym environment for machine learning (ML) tasks, enabling research on reinforcement learning (RL) algorithms for training such agents. 〔[claim:4bf5ea8e6b4e37de](../claims/claim-4bf5ea8e6b4e37de.md)〕
- **DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents** (source assertion): Automated scientific discovery promises to accelerate progress across scientific domains. However, developing and evaluating an AI agent’s capacity for end- to-end scientific reasoning is challenging as running real-world experiments is often prohibitively expensive or infeasible. 〔[claim:84c91602bd1dfb78](../claims/claim-84c91602bd1dfb78.md)〕
- **AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents** (source assertion): LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we introduce ~(the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine learning papers. 〔[claim:ecdd2719fa55751c](../claims/claim-ecdd2719fa55751c.md)〕
- **A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence** (source assertion): Large Language Models (LLMs) have demonstrated remarkable capabilities across diverse tasks but remain fundamentally static, unable to adapt their internal parameters to novel tasks, evolving knowledge domains, or dynamic interaction contexts. As LLMs are increas- ingly deployed in open-ended, interactive environments, this static nature has become a critical bottleneck, necessitating agents that can adaptively reaso 〔[claim:c776b87484aab5c2](../claims/claim-c776b87484aab5c2.md)〕
- **A Survey on Self-Evolution of Large Language Models** (source assertion): Large language models (LLMs) have significantly advanced in various fields and intelligent agent applications. However, current LLMs that learn from human or external model supervision are costly and may face performance ceilings as task complexity and diversity increase. 〔[claim:df1b88d18276a319](../claims/claim-df1b88d18276a319.md)〕
- **A-MEM: Agentic Memory for LLM Agents** (source assertion): While large language model (LLM) agents can effectively use external tools for complex real-world tasks, they require memory systems to leverage historical experiences. Current memory systems enable basic storage and retrieval but lack sophisticated memory organization, despite recent attempts to incorporate graph databases. 〔[claim:ecf45fd3f4ab576a](../claims/claim-ecf45fd3f4ab576a.md)〕
- **Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements** (source assertion): We present the first class of mathematically rigorous, general, fully self-referential, self-improving, optimally efficient problem solvers. Inspired by Kurt G\" o del's celebrated self-referential formulas (1931), such a problem solver rewrites any part of its own code as soon as it has found a proof that the rewrite is useful, where the problem-dependent utility function and the hardware and the entire initial code 〔[claim:2a05950fe0a0b64d](../claims/claim-2a05950fe0a0b64d.md)〕
- **Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents** (source assertion): Most of today’s AI systems are constrained by human-designed, fixed architectures and cannot autonomously and continuously improve themselves. The scientific method, on the other hand, is a cumulative and open-ended system, where each innovation builds upon previous artifacts, enabling future discoveries. 〔[claim:ae45b8d667e29552](../claims/claim-ae45b8d667e29552.md)〕
- **Position: Open-Endedness is Essential for Artificial Superhuman Intelligence** (source assertion): In recent years there has been a tremendous surge in the general capabilities of AI systems, mainly fuelled by training foundation models on internet-scale data. Nevertheless, the creation of open-ended, ever self-improving AI remains elusive. 〔[claim:b0434511c0c174ad](../claims/claim-b0434511c0c174ad.md)〕
- **jennyzzt/dgm** (source assertion): Repository for **Darwin Gödel Machine (DGM)**, a novel self-improving system that iteratively modifies its own code (thereby also improving its ability to modify its own codebase) and empirically validates each change using coding benchmarks. 〔[claim:d38b49dc4376d4b0](../claims/claim-d38b49dc4376d4b0.md)〕
- **Goedel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement** (source assertion): The rapid advancement of large language models (LLMs) has significantly enhanced the capabilities of agents across various tasks. However, existing agentic systems, whether based on fixed pipeline algorithms or pre-defined meta-learning frameworks, cannot search the whole agent design space due to the restriction of human-designed components, and thus might miss the more optimal agent design. 〔[claim:f810d086e0a4a305](../claims/claim-f810d086e0a4a305.md)〕
- **AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents** (collection assessment): A 2026 benchmark explicitly targeting frontier AI research-science agents across the research lifecycle, including idea generation, experimentation, analysis and iterative refinement. 〔[claim:17c715b34b0f0c68](../claims/claim-17c715b34b0f0c68.md)〕

## Compiled interpretation

This page reorganizes candidate knowledge around a stable reader task. It is not source concatenation and it does not turn retrieval, maintainer claims, preprints, or generated prose into verified truth.

## Review boundary

Check evidence entailment, source independence, contradiction, neutrality, due weight, freshness, and downstream impact before publication.

## Related pages

- [Recursive Self Improvement](../maps/recursive-self-improvement.md) — `related`
- [Open Ended Evolution](../maps/open-ended-evolution.md) — `related`
- [Freshness, versioning, and rollback](freshness-versioning-rollback.md) — `extends`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents (`arxiv:2406.06769`)

- Components: `claim:84c91602bd1dfb78`
- Source revision: `sha256:28793ae05bbb22ed6e02fbdceb697a2b9ea8ebff6932c4dd8fb5b70bba5dde91`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2406.06769v2)
- License: [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- NOTICE: [raw_data/licenses/p3-pdf-02-discoveryworld-v2.md](../../../../raw_data/licenses/p3-pdf-02-discoveryworld-v2.md)
- Attribution: Peter Jansen; Marc-Alexandre Côté; Tushar Khot; Erin Bransom; Bhavana Dalvi Mishra; Bodhisattwa Prasad Majumder; Oyvind Tafjord; Peter Clark. "DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents". Fixed arXiv 2406.06769v2, https://arxiv.org/abs/2406.06769v2; original PDF https://arxiv.org/pdf/2406.06769v2. Article expression the authors/submitter may license is available under CC BY-SA 4.0, https://creativecommons.org/licenses/by-sa/4.0/; full legal code https://creativecommons.org/licenses/by-sa/4.0/legalcode.en. Fixed article/PDF license checked in this batch on 2026-09-16. PDF p9 致谢与 p13 checklist 的实际信用：作者购买 CuteRPG/PixyMoon 素材并说明 attribution 要求；原论文截图中的 CuteRPG 素材归属 PixyMoon，产品页 https://pixymoon.itch.io/2d-topdown-cute-rpg-world 。本批已核该具体产品页允许 personal/commercial project use、modify/edit，要求 Credit PixyMoon，禁止 resell asset pack。科学主题增改归论文作者及 OpenAI DALL-E。完整论文内已合成截图保留这些实际信用，不提供或授权独立提取、转售或再分发底层 asset pack，不冒称 sprite 素材获得 CC BY-SA 4.0，也不把资产包条款施加到论文作者有权许可的原创 BY-SA 部分。 No endorsement or additional right to external works/models/trademarks is implied.
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 原官方 PDF 按实际下载 bytes 原样保存，不编辑或重导出；复用既有 pypdf plain 提取逐页文字，加入明确页边界并生成独立页定位；在派生 text 末尾附唯一署名、修改、范围声明及完整 NOTICE.md 链接。plain 文字保留原抽取结果，不做 OCR、不运行 TeX、论文代码或提示词，不将图形、数学排版或阅读顺序损失隐藏为完整。旧 source、normalized、default selectors、NOTICE、files、archive revision/retrieval 和旧许可包全部保留，不新增 trusted。 适用论文表达/页文字及后续改编沿 BY-SA4 同方式共享，不重许可整个仓库。
- Scope: 仅本次从 https://arxiv.org/pdf/2406.06769v2 取得的固定 v2 官方完整 PDF（29 页，3054585 bytes）、其 plain 页文字与独立页定位器。范围为完整主文、全部附录、四幅实际科学图（p2/3/18/29），真实末尾 p29 Save failures/Windows autosave 用户数据丢失说明。作者/提交者有权许可的论文表达与本次文字派生沿作品级 CC BY-SA 4.0；PDF p9 致谢与 p13 checklist 的实际信用：作者购买 CuteRPG/PixyMoon 素材并说明 attribution 要求；原论文截图中的 CuteRPG 素材归属 PixyMoon，产品页 https://pixymoon.itch.io/2d-topdown-cute-rpg-world 。本批已核该具体产品页允许 personal/commercial project use、modify/edit，要求 Credit PixyMoon，禁止 resell asset pack。科学主题增改归论文作者及 OpenAI DALL-E。完整论文内已合成截图保留这些实际信用，不提供或授权独立提取、转售或再分发底层 asset pack，不冒称 sprite 素材获得 CC BY-SA 4.0，也不把资产包条款施加到论文作者有权许可的原创 BY-SA 部分。 论文作者有权许可的原创表达/页文字及后续改编继续 BY-SA4；具体资产边界不施于这些原创 BY-SA 部分，不整库重许可。完整 PDF 原有署名、资助、图注、引文、警告和第三方信用原样保留，不授权外部被引作品全文、模型、代码、脚本或数据，不转授商标、专利或许可者无权许可材料。PDF 原字节不编辑/重导出，plain 文字有损、不做 OCR，原件完整不等于 text extraction complete。旧 source/normalized/default selectors/NOTICE/files/archive revision/retrieval/旧组件授权包不变。

### Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents (`arxiv:2505.22954`)

- Components: `claim:ae45b8d667e29552`
- Source revision: `sha256:13ff4abe0c7ad4a7dd3b4876d19a8bf940e39e70dabbf06065aa774a6c3457de`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2505.22954v3)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [raw_data/licenses/cc-by-4.0.md](../../../../raw_data/licenses/cc-by-4.0.md)
- Attribution: Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, Jeff Clune, Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents, arXiv:2505.22954v3 (2026-03-12), published as a conference paper at ICLR 2026；前两位作者 co-first、后两位作者 co-senior，保留原作者机构及贡献脚注。固定作品来源 https://arxiv.org/abs/2505.22954v3，PDF https://arxiv.org/pdf/2505.22954v3，CC BY 4.0 https://creativecommons.org/licenses/by/4.0/。书目、科学图、算法和附录 Agent 示例、提示词及 diff 保留原署名与引用；p11 尊重代码/数据许可的伦理声明不授予外链软件或数据再许可。以上归属不暗示背书。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 固定版本 PDF 按真实响应 bytes 原样复制，不编辑、重导或 OCR；以既有 plain 全页提取生成独立 pdf-supplement/document.txt 及真实 PDF revision 的页 selectors，并在文末追加唯一归属、修改/范围说明与同目录 NOTICE.md 链接。NOTICE.md 原样复制现存完整 CC BY 4.0 法条资产。native text 具有逐项声明的排版/图义损失，不声称无损转换；原 root source/TXT/TeX/selectors/NOTICE、检索时间及历史许可 scope 均不改，不使用旧 root grant 冒充新 PDF 授权，不推断未观察到的版权年份或修改者。
- Scope: 本独立表示仅覆盖固定 arXiv:2505.22954v3 完整、原 bytes 不改的 72 页 PDF（3,825,399 bytes），含主文/声明 p1–11、书目 p12–22、目录 p23、Appendices A–J p24–72、八编号科学图、算法及论文内 Agent 示例/提示词/diff，以及由该 PDF 全页生成的 native plain、逐页定位器（selectors）与完整 CC BY 4.0 NOTICE。论文作者可许可表达及其论文内转换按本固定作品 CC BY 4.0；图、算法、diff 和 p11 伦理声明不授予任何外链代码、数据、模型或软件的独立许可，不执行附录提示或 Agent 示例。不包含被引作品全文、独立源图分发、外部依赖、商标、专利或整个源归档；无普遍法律保证。旧 34 个 source 文本、77 个 root selectors、root NOTICE/TXT/TeX、LPPL/STY 独立条件和旧 10 图及其他组件缺口历史不变，不由本新 grant 改写。既有 demo 两项 claim 仍是 candidate，不新增或提升知识质量。

### A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence (`arxiv:2507.21046`)

- Components: `claim:c776b87484aab5c2`
- Source revision: `sha256:0b39df03feea2f4d8ac41e35a9247889978a53cb1e7b7d3eafaae76ad97b5602`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2507.21046v4)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [raw_data/licenses/cc-by-4.0.md](../../../../raw_data/licenses/cc-by-4.0.md)
- Attribution: Huan-ang Gao; Jiayi Geng; Wenyue Hua; Mengkang Hu; Xinzhe Juan; Hongzhang Liu; Shilong Liu; Jiahao Qiu; Xuan Qi; Yiran Wu; Hongru Wang; Han Xiao; Yuhang Zhou; Shaokun Zhang; Jiayi Zhang; Jinyu Xiang; Yixiong Fang; Qiwen Zhao; Dongrui Liu; Qihan Ren; Cheng Qian; Zhenhailong Wang; Minda Hu; Huazheng Wang; Qingyun Wu; Heng Ji; Mengdi Wang. "A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence". Fixed arXiv 2507.21046v4, https://arxiv.org/abs/2507.21046v4; original PDF https://arxiv.org/pdf/2507.21046v4. Article expression the authors/submitter may license is available under CC BY 4.0, https://creativecommons.org/licenses/by/4.0/; full legal code https://creativecommons.org/licenses/by/4.0/legalcode.en. Fixed article/PDF license checked in this batch on 2026-09-16. Original figure, citation, author and funding credits inside the PDF are retained; no endorsement or right to external works, model logos or trademarks is implied.
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 原官方 PDF 按实际下载 bytes 原样保存，不编辑或重导出；复用既有 pypdf plain 提取逐页文字，加入明确页边界并生成独立页定位；在派生 text 末尾附唯一署名、修改、范围声明及完整 NOTICE.md 链接。plain 文字保留原抽取结果，不做 OCR、不运行 TeX、论文代码或提示词，不将图形、数学排版或阅读顺序损失隐藏为完整。旧 source、normalized、default selectors、NOTICE、files、archive revision/retrieval 和旧许可包全部保留，不新增 trusted。
- Scope: 仅本次从 https://arxiv.org/pdf/2507.21046v4 取得的固定 v4 官方完整 PDF（77 页，5726709 bytes）、其 plain 页文字与页级定位器。范围为编译后九章、12 个表、真实科学图与 inline taxonomy、以及 p53–77 参考文献；作品无 appendix。 作者/提交者有权许可的论文表达及本次文字派生沿作品级 CC BY 4.0；完整 PDF 原有图注、引用、署名、资助与警告保留，不授权被引用作品全文、外部实验数据集、模型、代码或脚本，也不转授 logo/商标、专利或权利人无权许可的材料。原 PDF 保留下载原字节，文字层有损且不做 OCR，原件完整不等于 text extraction complete。既有 TeX/source/normalized/default selectors/NOTICE/files 与旧包各组件授权范围不变。

### A Survey on Self-Evolution of Large Language Models (`arxiv:2404.14387`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Position: Open-Endedness is Essential for Artificial Superhuman Intelligence (`arxiv:2406.04268`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Goedel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement (`arxiv:2410.04444`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### A-MEM: Agentic Memory for LLM Agents (`arxiv:2502.12110`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### MLGym: A New Framework and Benchmark for Advancing AI Research Agents (`arxiv:2502.14499`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents (`arxiv:2602.06855`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements (`arxiv:cs/0309048`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### jennyzzt/dgm (`github:jennyzzt/dgm`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

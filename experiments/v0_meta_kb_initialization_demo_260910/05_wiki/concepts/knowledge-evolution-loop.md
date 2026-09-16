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
  build_id: build:llm-wiki-v0:3de65e2db5aac4d8
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2502.14499@sha256:de8bc15be762914dd2f056f00efe2b83d51ce852a7035d65e866e6cdecbbb65a
  - arxiv:2406.06769@sha256:cb1d6ccc88eb66af69e71730a5c488234ff4fe8af04ba04081b5a445f4d39b3e
  - arxiv:2602.06855@sha256:ac1ba940f1bdc54e012cc384c428f78bd01d50d7a947f052117944c03e790d9a
  - arxiv:2507.21046@sha256:4bace9b0e6528f904932b2502264e47d4c5778660cd378f68e032e5588eae432
  - arxiv:2404.14387@sha256:afd13bcb8ce6f553dec268c0fb17bfb6b8a1ba80a4881a5b46d54b927ca9a418
  - arxiv:2502.12110@sha256:d112e92606a562a0369e2e8cddadad88ac8d448d66c24ee9b63e808c2c84e42b
  - arxiv:cs/0309048@sha256:ab75c69deb1c4b41ae77f5f817735922ad52fc9a8d51ec5184f4978a88b4052e
  - arxiv:2505.22954@sha256:9ce27273d9175badbb14d1181bc6166c7afd5e7989ac274d3d5187413e19b9ed
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
  estimated_tokens: 2279
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
- source_uid: arxiv:2505.22954
  source_revision: sha256:9ce27273d9175badbb14d1181bc6166c7afd5e7989ac274d3d5187413e19b9ed
  source_version_url: https://arxiv.org/abs/2505.22954v3
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: raw_data/licenses/dgm-v3-cc-by-4.0-iclr-adaptation-lppl-1.3c-natbib-source.md
  package_path: materialized_sources/corpus/arxiv-2505.22954--8a7041cb/manifest.yaml#rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:ae45b8d667e29552
- source_uid: arxiv:2507.21046
  source_revision: sha256:4bace9b0e6528f904932b2502264e47d4c5778660cd378f68e032e5588eae432
  source_version_url: https://arxiv.org/abs/2507.21046v4
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: raw_data/licenses/arxiv-cc-by-4.0-tmlr-apache-2.0-lppl-1.3c.md
  package_path: materialized_sources/corpus/arxiv-2507.21046--f477f5c3/manifest.yaml#rights.redistribution_package
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
- **DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents** (source assertion): Automated scientific discovery promises to accelerate progress across scientific domains. However, developing and evaluating an AI agent's capacity for end-to-end scientific reasoning is challenging as running real-world experiments is often prohibitively expensive or infeasible. 〔[claim:84c91602bd1dfb78](../claims/claim-84c91602bd1dfb78.md)〕
- **AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents** (source assertion): LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we introduce ~(the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine learning papers. 〔[claim:ecdd2719fa55751c](../claims/claim-ecdd2719fa55751c.md)〕
- **A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence** (source assertion): Large Language Models (LLMs) have demonstrated remarkable capabilities across diverse tasks but remain fundamentally static, unable to adapt their internal parameters to novel tasks, evolving knowledge domains, or dynamic interaction contexts. As LLMs are increasingly deployed in open-ended, interactive environments, this static nature has become a critical bottleneck, necessitating agents that can adaptively reason, 〔[claim:c776b87484aab5c2](../claims/claim-c776b87484aab5c2.md)〕
- **A Survey on Self-Evolution of Large Language Models** (source assertion): Large language models (LLMs) have significantly advanced in various fields and intelligent agent applications. However, current LLMs that learn from human or external model supervision are costly and may face performance ceilings as task complexity and diversity increase. 〔[claim:df1b88d18276a319](../claims/claim-df1b88d18276a319.md)〕
- **A-MEM: Agentic Memory for LLM Agents** (source assertion): While large language model (LLM) agents can effectively use external tools for complex real-world tasks, they require memory systems to leverage historical experiences. Current memory systems enable basic storage and retrieval but lack sophisticated memory organization, despite recent attempts to incorporate graph databases. 〔[claim:ecf45fd3f4ab576a](../claims/claim-ecf45fd3f4ab576a.md)〕
- **Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements** (source assertion): We present the first class of mathematically rigorous, general, fully self-referential, self-improving, optimally efficient problem solvers. Inspired by Kurt G\" o del's celebrated self-referential formulas (1931), such a problem solver rewrites any part of its own code as soon as it has found a proof that the rewrite is useful, where the problem-dependent utility function and the hardware and the entire initial code 〔[claim:2a05950fe0a0b64d](../claims/claim-2a05950fe0a0b64d.md)〕
- **Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents** (source assertion): Most of today's AI systems are constrained by human-designed, fixed architectures and cannot autonomously and continuously improve themselves. The scientific method, on the other hand, is a cumulative and open-ended system, where each innovation builds upon previous artifacts, enabling future discoveries. 〔[claim:ae45b8d667e29552](../claims/claim-ae45b8d667e29552.md)〕
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
- Source revision: `sha256:cb1d6ccc88eb66af69e71730a5c488234ff4fe8af04ba04081b5a445f4d39b3e`
- Source version: [pinned upstream version](https://arxiv.org/abs/2406.06769v2)
- License: [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- NOTICE: [raw_data/licenses/discoveryworld-v2-cc-by-sa-4.0-neurips-corresponding-expression-cc-by-4.0.md](../../../../raw_data/licenses/discoveryworld-v2-cc-by-sa-4.0-neurips-corresponding-expression-cc-by-4.0.md)
- Attribution: "DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents", arXiv:2406.06769v2, by Peter Jansen, Marc-Alexandre Côté, Tushar Khot, Erin Bransom, Bhavana Dalvi Mishra, Bodhisattwa Prasad Majumder, Oyvind Tafjord and Peter Clark, https://arxiv.org/abs/2406.06769v2, licensed under CC BY-SA 4.0: https://creativecommons.org/licenses/by-sa/4.0/. source/neurips_data_2024.sty is an independent NeurIPS Data 2024 template component with its original Lora Aroyo credit and attribution to Roman Garnett and the many authors of nips15submit_e.sty, including MK and drstrip@sandia, retained. Its corresponding licensed original template expression is identified in the NeurIPS 2026 Program Chairs' official "Formatting Instructions For NeurIPS 2026", https://www.overleaf.com/latex/templates/formatting-instructions-for-neurips-2026/bjdwqfdkyftc, explicitly declared CC BY 4.0: https://creativecommons.org/licenses/by/4.0/. The corresponding official current source is https://media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip, checked on 2026-09-16. The retained 2024 Data variant is packaged using this corresponding-expression/adaptation path, not a claim that the historical 2024 ZIP declared an overall CC BY 4.0 license. The retained member is also identified by the official 2024 Data bundle, https://media.neurips.cc/Conferences/NeurIPS2024/NeurIPS-Dataset-Styles.zip, linked from https://neurips.cc/Conferences/2024/CallForDatasetsBenchmarks. None of these attributions implies endorsement of this repository.
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. All nine text source members of the fixed v2 archive are retained unchanged, including related_work-v1-old.tex. The existing normalized/document.tex and all 74 selectors are preserved byte-for-byte. The original 94,506-byte normalized/document.txt is preserved as an exact prefix; only the complete attribution, changes, scope and NOTICE link are appended to its end. Compared with the currently reviewed official NeurIPS 2026 style, the retained Data 2024 style has the Lora Aroyo header, its 2024/04/30 package identifier, the anonymous default/option and @submission boolean mapping, and the @submission test in the title block; its meeting identifiers are 38th/2024 and its existing location string is "Vancouver, USA". It retains "Preprint. Under review." and the Datasets and Benchmarks track footer. The lineno/amsmath compatibility block appears earlier in the retained style rather than at the current style's end; its closing-brace layout differs. The retained style uses the 2024 package warning identifier and a space between each checklist answer label and its argument. It lacks the current multi-track, position/eandd/creativeai/education/workshop/nonanonymous options, minimum font-size overrides, acknowledgement-hiding block and justificationTODO command. Long formatting and compatibility expressions correspond to the currently licensed original; version labels, short footer text and routine functional adaptations are separately disclosed. These differences are pre-existing and are not introduced, repaired or attributed to a newly asserted modifier by this repository. No historical template download identity, historical 2024 BY4 declaration or byte-identical correspondence to the complete current style is claimed.
- Scope: 本包仅覆盖固定 arXiv 2406.06769v2 的九个 source 文字成员、normalized/document.tex、normalized/document.txt 与 74 个定位器（selectors）。作者/提交者有权许可的论文源表达及其文本转换，包括保留的旧稿，按 CC BY-SA 4.0 共享；改编材料继续按该许可同方式共享。source/neurips_data_2024.sty 是独立第三方模板，按当前官方模板的对应授权表达及 CC BY 4.0 复制/改编路径分别署名，保留其既存短常规功能适配，不将历史 2024 ZIP 宣称为整体 BY4，也不将模板著作权归论文作者。两许可按组件分别适用，不将整仓库重新许可为 BY-SA4 或 BY4；定位器不改变所定位组件的许可。DiscoveryWorld.bbl 是书目记录，不授权所引作品；未保存的五个非文本媒体、外链代码/模型/数据、商标及专利不在本许可包范围。没有删除任何已保存源文字以回避许可条件，不施加额外限制或暗示上游支持。

### Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents (`arxiv:2505.22954`)

- Components: `claim:ae45b8d667e29552`
- Source revision: `sha256:9ce27273d9175badbb14d1181bc6166c7afd5e7989ac274d3d5187413e19b9ed`
- Source version: [pinned upstream version](https://arxiv.org/abs/2505.22954v3)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [raw_data/licenses/dgm-v3-cc-by-4.0-iclr-adaptation-lppl-1.3c-natbib-source.md](../../../../raw_data/licenses/dgm-v3-cc-by-4.0-iclr-adaptation-lppl-1.3c-natbib-source.md)
- Attribution: Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, Jeff Clune, Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents, arXiv:2505.22954v3 (2026-03-12), https://arxiv.org/abs/2505.22954v3, CC BY 4.0: https://creativecommons.org/licenses/by/4.0/. ICLR, Template for ICLR 2025 Conference Submission, CC BY 4.0, https://www.overleaf.com/latex/templates/template-for-iclr-2025-conference-submission/gqzkdyycxtvt; retain Hugo Larochelle's NIPS-style adaptation credit. Official ICLR2026 copy at https://github.com/ICLR/Master-Template/commit/067b60c3985bd549c8b1afabb426a007905cea46 changes two year labels; local STY additionally centers the author table (l→c), modifier unknown. BST: Copyright 2010 Hal Daum\'e III, J. Fürnkranz label modifications, Copyright 1993-2007 Patrick W Daly; fancyhdr 3.2: Piet van Oostrum; natbib 8.31: Copyright 1993-2009 Patrick W Daly, 2009/07/16 original source. Components retain independent LPPL version 1 or later, selecting LPPL 1.3c: https://www.latex-project.org/lppl/lppl-1-3c.txt. 完整原 natbib.dtx 随 NOTICE.md 及 raw_data/licenses/components/natbib-8.31/natbib.dtx 提供； 00README.json 是 arXiv 自动编译元数据，按 https://info.arxiv.org/help/policies/submission_agreement.html#metadata-license 的CC0范围单列。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 34份源文本及原版权、归属和历史修改不改；复用现有 TeX 合并与纯文本转换， normalized/document.tex 和77个定位器不改，normalized/document.txt 仅在文末追加唯一署名、 修改/范围说明及 NOTICE.md 链接。ICLR模板的两处年份变化和作者表格l→c是已披露既存差异， 不虚构修改者或本仓库实施历史；完整法律文本及原 natbib.dtx 伴随保存，不声称维护者支持本仓库修改。
- Scope: 仅34份实存 source 文本（390140 bytes）、normalized/document.tex（227665 bytes）、 附注前190099-byte normalized/document.txt 正文和77个定位器。论文作者发布的正文、附录、 Agent代码/提示/差异与模型样例及其转换按论文BY4；ICLR模板表达和已披露改编按原2025模板BY4； BST、fancyhdr、natbib与伴随原dtx独立按LPPL条件，选择1.3c；arXiv编译元数据单列CC0。 main.bib只保留书目字段，没有额外abstract/copyright字段，不授权被引作品全文； 不包括原已省略10份PDF图像、未保存的math_commands/gdm_format组件、整个归档、外链代码/数据或外部依赖。

### A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence (`arxiv:2507.21046`)

- Components: `claim:c776b87484aab5c2`
- Source revision: `sha256:4bace9b0e6528f904932b2502264e47d4c5778660cd378f68e032e5588eae432`
- Source version: [pinned upstream version](https://arxiv.org/abs/2507.21046v4)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [raw_data/licenses/arxiv-cc-by-4.0-tmlr-apache-2.0-lppl-1.3c.md](../../../../raw_data/licenses/arxiv-cc-by-4.0-tmlr-apache-2.0-lppl-1.3c.md)
- Attribution: "A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence", arXiv:2507.21046v4，作者为 Huan-ang Gao; Jiayi Geng; Wenyue Hua; Mengkang Hu; Xinzhe Juan; Hongzhang Liu; Shilong Liu; Jiahao Qiu; Xuan Qi; Yiran Wu; Hongru Wang; Han Xiao; Yuhang Zhou; Shaokun Zhang; Jiayi Zhang; Jinyu Xiang; Yixiong Fang; Qiwen Zhao; Dongrui Liu; Qihan Ren; Cheng Qian; Zhenhailong Wang; Minda Hu; Huazheng Wang; Qingyun Wu; Heng Ji; Mengdi Wang。 来源：https://arxiv.org/abs/2507.21046v4，论文作者材料采用 CC BY 4.0：https://creativecommons.org/licenses/by/4.0/。 source/tmlr.sty 来自 TMLR 官方模板 https://github.com/JmlrOrg/tmlr-style-file/tree/7bf90efe3a0debbba703c05c43f3ff7e4d4a2992， 保留 Hugo Larochelle、Fabian Pedregosa 的改编与 Chris J. Maddison January 2021 的字体修改署名， 采用 Apache 2.0：https://www.apache.org/licenses/LICENSE-2.0。 source/tmlr.bst 保留 Copyright 2010 Hal Daum\'e III、J. Fürnkranz 的标签修改与 Copyright 1993-2007 Patrick W Daly；source/fancyhdr.sty 保留 Copyright (C) 1994-2021 Pieter van Oostrum 及 v4.0.1 身份； 两组件分别保留原 LPPL 授予，本包选择 LPPL 1.3c：https://www.latex-project.org/lppl/lppl-1-3c/。 main.bib 的 tool_tut 摘要来自 "Empowering Large Language Models: Tool Learning for Real-World Interaction"， Hongru Wang; Yujia Qin; Yankai Lin; Jeff Z. Pan; Kam-Fai Wong，SIGIR 2024, pp. 2983-2986， https://doi.org/10.1145/3626772.3661381；ACM 提交的作品记录声明 VOR 按 CC BY 4.0 授权，始于 2024-07-10。 AppBench 摘要来自 "AppBench: Planning of Multiple APIs from Various APPs for Complex User Instruction"， Hongru Wang; Rui Wang; Boyang Xue; Heming Xia; Jingtao Cao; Zeming Liu; Jeff Z. Pan; Kam-Fai Wong， Copyright © 2024 ACL，https://aclanthology.org/2024.emnlp-main.856/，按 CC BY 4.0 授权。 ARIA 摘要来自 "Enabling Self-Improving Agents to Learn at Test Time With Human-In-The-Loop Guidance"， Yufei He; Ruoyu Li; Alex Chen; Yue Liu; Yulin Chen; Yuan Sui; Cheng Chen; Yi Zhu; Luca Luo; Frank Yang; Bryan Hooi，Copyright © 2025 ACL，https://aclanthology.org/2025.emnlp-industry.115/，按 CC BY 4.0 授权。 三段摘要的许可链接同为 https://creativecommons.org/licenses/by/4.0/，不代表授权其描述的代码、数据或其他引用作品。 source/00README.json 为 arXiv 自动处理/编译元数据，其适用 CC0 来源为 https://info.arxiv.org/help/policies/submission_agreement.html#metadata-license。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 固定 v4 源包解包后，原有 19 个 source 文字成员逐字保留；不删除或改写论文、附录、三段额外摘要、 模板代码或组件身份。现有生成器展开主 TeX 的 include/input 至 normalized/document.tex，并转换为 normalized/document.txt、生成 135 个 selector；TeX 命令、结构和数学排版按既有流程归一为纯文本， 图像/PDF 不转换为可读正文。此次仅向 normalized/document.txt 末尾追加唯一分隔标记、论文与组件署名、 修改/范围说明及 NOTICE.md 链接，README 增加 NOTICE 链接，manifest 记录已应用的 package； source、normalized/document.tex 和既有 selector 不改。三段摘要在 main.bib 内保留其原文与引用字段， 未据最新题名改写其内部 "MetaBench" 用语，也不冒称 ACM PDF 或摘要逐字复核。
- Scope: 本包只覆盖固定 arXiv v4 胶囊实际保存的 19 个 source 文字成员（484,027 bytes）、 normalized/document.tex、附注前的既有 normalized/document.txt 与 135 个 selector。 论文作者主文/附录及其文本转换按 CC BY 4.0；source/tmlr.sty 单独按 Apache 2.0； source/tmlr.bst 与 source/fancyhdr.sty 分别按原 LPPL 许可授予、本包选择 LPPL 1.3c 履约。 source/main.bib 只有 tool_tut、AppBench 和 ARIA 三段额外摘要按各自作品级 CC BY 4.0 履约， 其余书目事实与排版引用不授权引用作品；source/00README.json 仅作为适用 CC0 的事实编译元数据。 独立组件仍各自保留原许可，不把整篇论文或整个 Bib 重许可为 Apache/LPPL；本包不是整个 archive 的镜像， 不覆盖原已省略的八个非文本成员、其他外链论文、代码、数据、商标、专利或权利人无权许可的材料。

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

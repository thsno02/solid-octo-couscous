---
uid: wiki-page:map-recursive-self-improvement
title: Recursive Self Improvement
slug: maps/recursive-self-improvement
page_type: map
status: review
summary: Routing map for recursive self improvement sources, questions, and claims.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:1b6ae1229c17cacd
- claim:2a05950fe0a0b64d
- claim:822962fc261c9559
- claim:90ae7352bb085ae8
- claim:9243c79fad41f2cb
- claim:ae45b8d667e29552
- claim:b0434511c0c174ad
- claim:d38b49dc4376d4b0
- claim:f43359e01e4c4b0b
- claim:f810d086e0a4a305
source_refs: &id001
- github:jennyzzt/dgm
- arxiv:cs/0309048
- arxiv:2406.04268
- arxiv:2505.22954
- arxiv:2410.04444
page_refs:
- wiki-page:source-e3fe88d81aab6499
- wiki-page:source-0e73b118b5b15597
- wiki-page:source-13964b2db9a9f793
- wiki-page:source-c29f716871f80314
- wiki-page:source-d04ae5d37f10547b
- wiki-page:knowledge-evolution-loop
- wiki-page:automation-vs-editorial-review
outgoing_links:
- target: wiki-page:source-e3fe88d81aab6499
  relation: explains
  claim_refs:
  - claim:d38b49dc4376d4b0
  - claim:1b6ae1229c17cacd
  notes: null
- target: wiki-page:source-0e73b118b5b15597
  relation: explains
  claim_refs:
  - claim:2a05950fe0a0b64d
  - claim:9243c79fad41f2cb
  notes: null
- target: wiki-page:source-13964b2db9a9f793
  relation: explains
  claim_refs:
  - claim:b0434511c0c174ad
  - claim:822962fc261c9559
  notes: null
- target: wiki-page:source-c29f716871f80314
  relation: explains
  claim_refs:
  - claim:ae45b8d667e29552
  - claim:90ae7352bb085ae8
  notes: null
- target: wiki-page:source-d04ae5d37f10547b
  relation: explains
  claim_refs:
  - claim:f810d086e0a4a305
  - claim:f43359e01e4c4b0b
  notes: null
- target: wiki-page:knowledge-evolution-loop
  relation: related
  claim_refs:
  - claim:1b6ae1229c17cacd
  - claim:2a05950fe0a0b64d
  - claim:822962fc261c9559
  - claim:90ae7352bb085ae8
  - claim:9243c79fad41f2cb
  - claim:ae45b8d667e29552
  notes: null
- target: wiki-page:automation-vs-editorial-review
  relation: related
  claim_refs:
  - claim:1b6ae1229c17cacd
  - claim:2a05950fe0a0b64d
  - claim:822962fc261c9559
  - claim:90ae7352bb085ae8
  - claim:9243c79fad41f2cb
  - claim:ae45b8d667e29552
  notes: null
sections:
- heading: Source coverage
  claim_refs: []
  source_refs: *id001
  editorial_intent: Route by source family.
- heading: Source-reported signals
  claim_refs:
  - claim:2a05950fe0a0b64d
  - claim:ae45b8d667e29552
  - claim:b0434511c0c174ad
  - claim:d38b49dc4376d4b0
  - claim:f810d086e0a4a305
  source_refs:
  - arxiv:cs/0309048
  - arxiv:2505.22954
  - arxiv:2406.04268
  - github:jennyzzt/dgm
  - arxiv:2410.04444
  editorial_intent: Preserve source-authored scope.
- heading: Collector assessments
  claim_refs:
  - claim:1b6ae1229c17cacd
  - claim:822962fc261c9559
  - claim:90ae7352bb085ae8
  - claim:9243c79fad41f2cb
  - claim:f43359e01e4c4b0b
  source_refs:
  - github:jennyzzt/dgm
  - arxiv:2406.04268
  - arxiv:2505.22954
  - arxiv:cs/0309048
  - arxiv:2410.04444
  editorial_intent: Preserve collector scope.
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
  - github:jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2
  - arxiv:cs/0309048@sha256:ab75c69deb1c4b41ae77f5f817735922ad52fc9a8d51ec5184f4978a88b4052e
  - arxiv:2406.04268@sha256:40b1f56033d9b9c2ad82d2aa9dcd2123af637fc2de7e88c96b9dc93477a643a1
  - arxiv:2505.22954@sha256:13ff4abe0c7ad4a7dd3b4876d19a8bf940e39e70dabbf06065aa774a6c3457de
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
    one_line: Routing map for recursive self improvement sources, questions, and claims.
    short: Routing map for recursive self improvement sources, questions, and claims.
    full: null
  estimated_tokens: 1290
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:1b6ae1229c17cacd
- claim:2a05950fe0a0b64d
- claim:822962fc261c9559
- claim:90ae7352bb085ae8
- claim:9243c79fad41f2cb
- claim:ae45b8d667e29552
- claim:b0434511c0c174ad
- claim:d38b49dc4376d4b0
- claim:f43359e01e4c4b0b
- claim:f810d086e0a4a305
rights_refs:
- source_uid: arxiv:2406.04268
  source_revision: sha256:40b1f56033d9b9c2ad82d2aa9dcd2123af637fc2de7e88c96b9dc93477a643a1
  source_version_url: https://arxiv.org/pdf/2406.04268v1
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: materialized_sources/corpus/arxiv-2406.04268--ce5afac4/pdf-supplement/NOTICE.md
  package_path: materialized_sources/corpus/arxiv-2406.04268--ce5afac4/manifest.yaml#pdf_supplement.rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:b0434511c0c174ad
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
rights_unavailable_source_refs:
- arxiv:2410.04444
- arxiv:cs/0309048
- github:jennyzzt/dgm
---

# Recursive Self Improvement

Systems that modify agents, programs, prompts, or search processes under evaluation.

## Routing questions

- What can modify itself?
- What evaluator and archive constrain change?
- How are regressions and unsafe changes detected?

## Source coverage

| Source | Type | Tier | Claims |
|---|---|---|---|
| [jennyzzt/dgm](../sources/github-jennyzzt-dgm.md) | `github` | `semantic_capsule` | 2 |
| [Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements](../sources/arxiv-cs-0309048.md) | `arxiv` | `full_text` | 2 |
| [Position: Open-Endedness is Essential for Artificial Superhuman Intelligence](../sources/arxiv-2406.04268.md) | `arxiv` | `full_text` | 2 |
| [Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents](../sources/arxiv-2505.22954.md) | `arxiv` | `full_text` | 2 |
| [Goedel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement](../sources/arxiv-2410.04444.md) | `arxiv` | `full_text` | 2 |

## Source-reported signals

- **Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements** (source assertion): We present the first class of mathematically rigorous, general, fully self-referential, self-improving, optimally efficient problem solvers. Inspired by Kurt G\" o del's celebrated self-referential formulas (1931), such a problem solver rewrites any part of its own code as soon as it has found a proof that the rewrite is useful, where the problem-dependent utility function and the hardware and the entire initial code 〔[claim:2a05950fe0a0b64d](../claims/claim-2a05950fe0a0b64d.md)〕
- **Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents** (source assertion): Most of today’s AI systems are constrained by human-designed, fixed architectures and cannot autonomously and continuously improve themselves. The scientific method, on the other hand, is a cumulative and open-ended system, where each innovation builds upon previous artifacts, enabling future discoveries. 〔[claim:ae45b8d667e29552](../claims/claim-ae45b8d667e29552.md)〕
- **Position: Open-Endedness is Essential for Artificial Superhuman Intelligence** (source assertion): In recent years there has been a tremendous surge in the general capabilities of AI systems, mainly fuelled by training foundation models on internet- scale data. Nevertheless, the creation of open- ended, ever self-improving AI remains elusive. 〔[claim:b0434511c0c174ad](../claims/claim-b0434511c0c174ad.md)〕
- **jennyzzt/dgm** (source assertion): Repository for **Darwin Gödel Machine (DGM)**, a novel self-improving system that iteratively modifies its own code (thereby also improving its ability to modify its own codebase) and empirically validates each change using coding benchmarks. 〔[claim:d38b49dc4376d4b0](../claims/claim-d38b49dc4376d4b0.md)〕
- **Goedel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement** (source assertion): The rapid advancement of large language models (LLMs) has significantly enhanced the capabilities of agents across various tasks. However, existing agentic systems, whether based on fixed pipeline algorithms or pre-defined meta-learning frameworks, cannot search the whole agent design space due to the restriction of human-designed components, and thus might miss the more optimal agent design. 〔[claim:f810d086e0a4a305](../claims/claim-f810d086e0a4a305.md)〕

## Collector assessments

- **jennyzzt/dgm** (collection assessment): One of the clearest open implementations of a system that edits its own agent code, evaluates variants, and keeps an archive instead of overwriting a single lineage. 〔[claim:1b6ae1229c17cacd](../claims/claim-1b6ae1229c17cacd.md)〕
- **Position: Open-Endedness is Essential for Artificial Superhuman Intelligence** (collection assessment): Provides a modern formal framing of open-endedness via novelty and learnability and argues that open-ended systems are a necessary ingredient for artificial superhuman intelligence. 〔[claim:822962fc261c9559](../claims/claim-822962fc261c9559.md)〕
- **Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents** (collection assessment): A central modern RSI result: iteratively modifies an agent codebase, empirically validates changes, and preserves a diverse archive/tree of agents so improvement can proceed through multiple open-ended stepping-stone paths. 〔[claim:90ae7352bb085ae8](../claims/claim-90ae7352bb085ae8.md)〕
- **Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements** (collection assessment): Foundational formal RSI work: a self-referential problem solver rewrites any part of its own code after proving that the rewrite improves expected utility. 〔[claim:9243c79fad41f2cb](../claims/claim-9243c79fad41f2cb.md)〕
- **Goedel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement** (collection assessment): Modernizes the Goedel-machine idea for LLM agents: the agent dynamically modifies its own logic and behavior under high-level objectives rather than following a fixed human-designed optimization routine. 〔[claim:f43359e01e4c4b0b](../claims/claim-f43359e01e4c4b0b.md)〕

## Current synthesis boundary

The map routes candidate evidence; it does not flatten sources into consensus or resolve contradictions automatically.

## Related pages

- [jennyzzt/dgm](../sources/github-jennyzzt-dgm.md) — `explains`
- [Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements](../sources/arxiv-cs-0309048.md) — `explains`
- [Position: Open-Endedness is Essential for Artificial Superhuman Intelligence](../sources/arxiv-2406.04268.md) — `explains`
- [Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents](../sources/arxiv-2505.22954.md) — `explains`
- [Goedel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement](../sources/arxiv-2410.04444.md) — `explains`
- [Knowledge evolution loop](../concepts/knowledge-evolution-loop.md) — `related`
- [Automation versus editorial review](../debates/automation-editorial-review.md) — `related`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Position: Open-Endedness is Essential for Artificial Superhuman Intelligence (`arxiv:2406.04268`)

- Components: `claim:b0434511c0c174ad`
- Source revision: `sha256:40b1f56033d9b9c2ad82d2aa9dcd2123af637fc2de7e88c96b9dc93477a643a1`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2406.04268v1)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [materialized_sources/corpus/arxiv-2406.04268--ce5afac4/pdf-supplement/NOTICE.md](../../../../materialized_sources/corpus/arxiv-2406.04268--ce5afac4/pdf-supplement/NOTICE.md)
- Attribution: Edward Hughes; Michael Dennis; Jack Parker-Holder; Feryal Behbahani; Aditi Mavalankar; Yuge Shi; Tom Schaul; Tim Rocktäschel, Open-Endedness is Essential for Artificial Superhuman Intelligence, arXiv:2406.04268v1 (2024-06-06), https://arxiv.org/abs/2406.04268v1, PDF https://arxiv.org/pdf/2406.04268v1, CC BY4 https://creativecommons.org/licenses/by/4.0/。可见八作者 Edward Hughes／Michael Dennis／Jack Parker-Holder／Feryal Behbahani／Aditi Mavalankar／Yuge Shi／Tom Schaul／Tim Rocktäschel；Hughes／Dennis等贡献及correspondence，Google DeepMind London、ICML2024／PMLR235／作者版权原样。旧题名Position:前缀、Michael D. Dennis／ASCII Rocktaschel仅是旧署名表达，不冒称本次PDF原字节，不猜中间名。p10明确Noun Project graphics适用CC BY3.0 https://creativecommons.org/licenses/by/3.0/，独立十credit：tick — kareemovic — https://thenounproject.com/browse/icons/term/tick?iconspage=1; Delete — kareemovic — https://thenounproject.com/browse/icons/term/Delete?iconspage=1; alien — Artem Yurov — https://thenounproject.com/browse/icons/term/alien?iconspage=1; girl — Teewara soontorn — https://thenounproject.com/browse/icons/term/girl?iconspage=1; year of rat — DailyPM — https://thenounproject.com/browse/icons/term/year-of-rat?iconspage=1; aircraft — mikicon — https://thenounproject.com/browse/icons/term/aircraft?iconspage=1; concorde — mikicon — https://thenounproject.com/browse/icons/term/concorde?iconspage=1; Plane — CAMB — https://thenounproject.com/browse/icons/term/plane?iconspage=1; humans — Ifanicon — https://thenounproject.com/browse/icons/term/humans?iconspage=1; Robot — Deemak Daksina — https://thenounproject.com/browse/icons/term/robot?iconspage=1。这些browse targets来自PDF实际Annots，未访问；标准BY3法条URL是新增标准链接，不冒称PDF印有该URI。Dave Abel反馈致谢保留。本批未修改图标，不推测论文作者改色／改形，不把图标版权归论文八作者或给全站资产一般BY4。 本批正式 https://arxiv.org/abs/2406.04268v1 的作品 view license 正常到BY4，v1日期2024-06-06；C核实际八作者／20页主文与A–C／十Noun Project BY3独立credit，主线全文读并明确准入。 以上归属不暗示背书。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 固定版本 PDF 按本次真实响应 bytes 原样保留，不编辑、重导或 OCR；以既有 helper 的 plain 全页提取生成独立 pdf-supplement/document.txt 和真实 PDF revision 的页定位器（page selectors），在文末追加唯一归属、修改／范围附注与同目录 NOTICE.md 链接。NOTICE 自包含本项实际归属、精确范围及现存完整 CC BY 4.0 法条；native text 的逐项损失见 limitations，不声称无损转换或可直接执行的源代码／prompt。旧 root source、normalized TXT／TeX、selectors、NOTICE／README、revision、retrieval 和历史 gate 不改，不将新固定版选择冒称旧 source payload 已被追溯核定。
- Scope: 本独立表示仅覆盖固定 arXiv:2406.04268v1 原 bytes 不改的20页 PDF（939555 bytes）：固定 arXiv:2406.04268v1 完整20物理页编译PDF：p1–9主文，p10Impact Statement／Acknowledgements／References至p17左栏，p17–18 A Illustrating Open-Endedness，p18–19 B Alternative Definition，p19–20 C Further Related Work，Figure1–3齐，p20真正末句 restricted by the environment.；不取旧模板／独立图标／外链原作。 论文作者可许可表达按本固定作品已证 CC BY4 路径；实际有界引用／图板按原件精确信用与身份保留，不改变底层许可、不独立重许被引全文／数据／代码／模型／媒体／商标／源模板或整个source归档。十Noun Project图标另保留实际CC BY3.0与完整名／作者／来源，不归给论文BY4。 此范围也包含该PDF native plain、页selectors及完整BY4 NOTICE；旧 root rights／block／retrieval／revision／source_version键缺省和历史原件／文字缺失不改；无普遍权利保证。

### Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents (`arxiv:2505.22954`)

- Components: `claim:ae45b8d667e29552`
- Source revision: `sha256:13ff4abe0c7ad4a7dd3b4876d19a8bf940e39e70dabbf06065aa774a6c3457de`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2505.22954v3)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [raw_data/licenses/cc-by-4.0.md](../../../../raw_data/licenses/cc-by-4.0.md)
- Attribution: Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, Jeff Clune, Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents, arXiv:2505.22954v3 (2026-03-12), published as a conference paper at ICLR 2026；前两位作者 co-first、后两位作者 co-senior，保留原作者机构及贡献脚注。固定作品来源 https://arxiv.org/abs/2505.22954v3，PDF https://arxiv.org/pdf/2505.22954v3，CC BY 4.0 https://creativecommons.org/licenses/by/4.0/。书目、科学图、算法和附录 Agent 示例、提示词及 diff 保留原署名与引用；p11 尊重代码/数据许可的伦理声明不授予外链软件或数据再许可。以上归属不暗示背书。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 固定版本 PDF 按真实响应 bytes 原样复制，不编辑、重导或 OCR；以既有 plain 全页提取生成独立 pdf-supplement/document.txt 及真实 PDF revision 的页 selectors，并在文末追加唯一归属、修改/范围说明与同目录 NOTICE.md 链接。NOTICE.md 原样复制现存完整 CC BY 4.0 法条资产。native text 具有逐项声明的排版/图义损失，不声称无损转换；原 root source/TXT/TeX/selectors/NOTICE、检索时间及历史许可 scope 均不改，不使用旧 root grant 冒充新 PDF 授权，不推断未观察到的版权年份或修改者。
- Scope: 本独立表示仅覆盖固定 arXiv:2505.22954v3 完整、原 bytes 不改的 72 页 PDF（3,825,399 bytes），含主文/声明 p1–11、书目 p12–22、目录 p23、Appendices A–J p24–72、八编号科学图、算法及论文内 Agent 示例/提示词/diff，以及由该 PDF 全页生成的 native plain、逐页定位器（selectors）与完整 CC BY 4.0 NOTICE。论文作者可许可表达及其论文内转换按本固定作品 CC BY 4.0；图、算法、diff 和 p11 伦理声明不授予任何外链代码、数据、模型或软件的独立许可，不执行附录提示或 Agent 示例。不包含被引作品全文、独立源图分发、外部依赖、商标、专利或整个源归档；无普遍法律保证。旧 34 个 source 文本、77 个 root selectors、root NOTICE/TXT/TeX、LPPL/STY 独立条件和旧 10 图及其他组件缺口历史不变，不由本新 grant 改写。既有 demo 两项 claim 仍是 candidate，不新增或提升知识质量。

### Goedel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement (`arxiv:2410.04444`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements (`arxiv:cs/0309048`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### jennyzzt/dgm (`github:jennyzzt/dgm`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

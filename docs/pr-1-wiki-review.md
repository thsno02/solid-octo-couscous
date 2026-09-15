# PR #1 LLM Wiki 自动化与 Agent 编辑审查记录

## 结论

本轮对候选 Wiki 完成了机器校验（machine validation）与 Agent 抽样编辑审查（agent editorial sampling）。最终构建的结构、引用和本地证据链通过确定性校验；抽样页面能够从页面回溯到 claim、evidence selector 和固定来源版本。

这不是人工批准（human approval），也不是科学事实、软件运行表现、中立性、权重分配或公开再分发权利的确认。所有页面仍为 `review`，所有 71 条 claims 仍为 `candidate`，`trusted_claims` 为 0。

## 审查对象

- 审查日期：2026-09-16
- 基础构建：`build:v0-meta-kb-260910:46bee5b1d7a51711`
- Wiki 构建：`build:llm-wiki-v0:d303e0f210b88f64`
- 来源：36
- claims / evidence：71 / 71
- Wiki 页面：134
- typed links：354
- graph nodes / edges：312 / 1370
- context packs：3
- orphan pages：0
- trusted claims：0

机器结果来自：

- [`06_evaluation/validation.yaml`](../experiments/v0_meta_kb_initialization_demo_260910/06_evaluation/validation.yaml)
- [`06_evaluation/compiler_validation.yaml`](../experiments/v0_meta_kb_initialization_demo_260910/06_evaluation/compiler_validation.yaml)
- [`06_evaluation/wiki_metrics.yaml`](../experiments/v0_meta_kb_initialization_demo_260910/06_evaluation/wiki_metrics.yaml)
- [`08_release/wiki_build_manifest.yaml`](../experiments/v0_meta_kb_initialization_demo_260910/08_release/wiki_build_manifest.yaml)

两套 validator 均报告 `passed`、0 warnings、0 errors。完整 demo 连续重建、Wiki-only 重建和只读验证覆盖 168 个生成文件，结果 byte-identical；21 个离线回归测试通过。

## 方法与判定标准

机器校验覆盖全部 71 条 claim/evidence bindings，包括：schema、UID 唯一性、claim/source/page refs、selector 路径与行号范围、excerpt containment、excerpt hash、metadata 字段定位、typed/Markdown links、页面覆盖、review queue、manifest input/output hash，以及禁止自动晋升 trusted claim。

Agent 抽样额外检查页面是否：

1. 清楚区分来源陈述（source-reported assertion）与采集者判断（collector assessment）；
2. 呈现可展开的本地 evidence selector 与固定 source revision；
3. 保持 `candidate` / `review` 治理边界；
4. 提供与页面任务相符的导航、内容组织和风险提示；
5. 不把结构通过误写成科学真值或人工认可。

## 抽样清单

### 入口与领域图

- [`05_wiki/index.md`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/index.md)
- [`05_wiki/maps/llm-wiki.md`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/maps/llm-wiki.md)
- [`05_wiki/maps/recursive-self-improvement.md`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/maps/recursive-self-improvement.md)
- [`05_wiki/maps/ontology-semantic-architecture.md`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/maps/ontology-semantic-architecture.md)
- [`05_wiki/maps/automated-research.md`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/maps/automated-research.md)

入口页按 overview、methods、concepts、comparisons、quality/frontier 和 maps 分流，候选发布提示明确。四个领域图都提供 routing questions、source coverage、分开的 source signals / collector assessments 和 related pages。最终重建使用词边界匹配领域关键词，抽样未再出现 `rsi` 命中 `version`、`owl` 命中 `knowledge`、`rag` 命中 `paragraph` 一类子串误分桶。

### 跨来源比较

- [`05_wiki/comparisons/paper-repository.md`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/comparisons/paper-repository.md)

页面结构、refs 与治理提示有效，但当前 12 条 candidate evidence 主要是自动研究论文信号，repository 样本不足，也没有逐项支撑 TeX-first paper 与 commit-pinned repository 的差异。因此它目前更像候选证据集合，而不是完成的比较论证；需要人工编辑重选双方证据并补充明确的比较维度。

### 来源页与对应 claim 页

本轮选择 5 个来源，每个来源检查其来源陈述与采集者判断，共 10 个 claim 页面。

1. Gödel Machines 论文

   - [`05_wiki/sources/arxiv-cs-0309048.md`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/sources/arxiv-cs-0309048.md)
   - [`05_wiki/claims/claim-2a05950fe0a0b64d.md`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/claims/claim-2a05950fe0a0b64d.md)
   - [`05_wiki/claims/claim-9243c79fad41f2cb.md`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/claims/claim-9243c79fad41f2cb.md)

2. Darwin Gödel Machine 论文

   - [`05_wiki/sources/arxiv-2505.22954.md`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/sources/arxiv-2505.22954.md)
   - [`05_wiki/claims/claim-ae45b8d667e29552.md`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/claims/claim-ae45b8d667e29552.md)
   - [`05_wiki/claims/claim-90ae7352bb085ae8.md`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/claims/claim-90ae7352bb085ae8.md)

3. DGM repository

   - [`05_wiki/sources/github-jennyzzt-dgm.md`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/sources/github-jennyzzt-dgm.md)
   - [`05_wiki/claims/claim-d38b49dc4376d4b0.md`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/claims/claim-d38b49dc4376d4b0.md)
   - [`05_wiki/claims/claim-1b6ae1229c17cacd.md`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/claims/claim-1b6ae1229c17cacd.md)

4. sage-wiki repository

   - [`05_wiki/sources/github-xoai-sage-wiki.md`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/sources/github-xoai-sage-wiki.md)
   - [`05_wiki/claims/claim-e7ac7da9ac39e47d.md`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/claims/claim-e7ac7da9ac39e47d.md)
   - [`05_wiki/claims/claim-c4f2def09ea56d98.md`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/claims/claim-c4f2def09ea56d98.md)

5. LinkML repository

   - [`05_wiki/sources/github-linkml-linkml.md`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/sources/github-linkml-linkml.md)
   - [`05_wiki/claims/claim-fc57f26307cefee3.md`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/claims/claim-fc57f26307cefee3.md)
   - [`05_wiki/claims/claim-3adb88340e0eb2b6.md`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/claims/claim-3adb88340e0eb2b6.md)

这 10 个页面的 claim text 与绑定 excerpt 一致；line selector 或 metadata field selector 均可在本地解析。论文声明来自固定 full-text capsule，repository 声明直接引用 commit-pinned README evidence，而 collector assessment 指向独立 metadata 字段。页面没有把 maintainer 声明当作 runtime、benchmark、可靠性或安全性验证。

### Context packs

- [`05_wiki/context_packs/context-pack-v0-collection-overview.yaml`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/context_packs/context-pack-v0-collection-overview.yaml)
- [`05_wiki/context_packs/context-pack-v0-evidence-and-governance.yaml`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/context_packs/context-pack-v0-evidence-and-governance.yaml)
- [`05_wiki/context_packs/context-pack-v0-research-frontier.yaml`](../experiments/v0_meta_kb_initialization_demo_260910/05_wiki/context_packs/context-pack-v0-research-frontier.yaml)

三个 pack 均绑定当前 Wiki build、固定 `as_of`、页面/claim/source refs、token budget 与 build manifest，结构上适合作为受限上下文入口。当前 claim selection 仍有较多跨 pack 重复，尚未通过任务相关性（task relevance）、召回率或回答质量评测；不能仅凭结构有效就认定 pack 已达到生产检索质量。

## 仍需人工处理的边界

- 科学事实性（scientific factuality）、独立复现与来源间冲突尚未评定。
- 领域图和比较页仍需人工检查语义归类、观点完整性、中立性与 due weight。
- TeX / Markdown 归一化仍可能留下展示瑕疵，例如转义重音、缺失的公式或命令参数；selector 可追溯不等于文本已达到编辑出版质量。
- repository 页面只证明固定 commit 中存在相应 maintainer statement，不证明代码可运行或声明成立。
- `contradictions.jsonl` 仍为空，不能据此推断来源之间没有矛盾。
- 公开再分发（public redistribution）必须通过独立的、fail-closed 权利审计门；本记录不授予许可，也不替代许可证履约或人工法律审查。

## 审查状态

技术候选（technical candidate）可以继续作为 PR 内的可复跑 demo 接受代码审查。编辑与治理状态保持 `needs_human`；没有写入 reviewer、decision、admission 或 trusted 状态，也没有作出人工批准结论。

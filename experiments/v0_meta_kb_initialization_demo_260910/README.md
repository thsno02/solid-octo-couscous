# v0 元知识库初始化与 LLM Wiki Demo — 260910

这个实验是仓库既定 LLM Wiki pipeline 的第一版可执行演示。它只消费已在本地物化并固定版本的 source capsules，不直接从运行时 URL 构建知识。

```text
本地来源版本（SourceRevision）
→ 可解析结构与证据定位器（Evidence）
→ 原子候选声明（Claim）
→ 身份与本体映射
→ 页面规划（PagePlan）
→ 候选 Wiki 页面与 typed links
→ 目录、依赖图、搜索索引与 context packs
→ 确定性验证与固定问题集
→ 评审队列与 WikiChange proposal
→ 候选 release manifest / rollback
```

## 边界

- Source、Claim 和 Page 是三个不同对象；页面是派生视图，不是权威真值记录。
- source-reported assertion、collector assessment 和 generated synthesis 分开保存。
- 每个 claim 都可展开到本地 evidence selector；高风险内容不能只靠页面级 bibliography。
- 自动构建不会把任何科学声明晋升为 `trusted`。当前 candidate release 的 trusted claims 固定为 **0**。
- GitHub repository capsule 表示 commit-pinned 静态证据，不代表运行时、benchmark、可靠性或安全性已经验证。

## 构建

在仓库根目录执行：

```bash
python experiments/v0_meta_kb_initialization_demo_260910/pipeline/build_demo.py
python experiments/v0_meta_kb_initialization_demo_260910/pipeline/build_llm_wiki.py
python experiments/v0_meta_kb_initialization_demo_260910/pipeline/validate_llm_wiki.py
python experiments/v0_meta_kb_initialization_demo_260910/pipeline/validate_demo.py
```

`build_demo.py` 生成基础 claim/evidence layer；`build_llm_wiki.py` 从该层执行 pipeline Stage 8–16 的可确定部分。编译器不调用模型，因此同一组固定输入会得到相同 build key、页面集合、typed-link 图和索引。

## 主要输出

```text
00_inputs/
  wiki_build_request.yaml
  page_plan.yaml
05_wiki/
  index.md
  maps/ overviews/ concepts/ methods/ systems/
  comparisons/ debates/ gaps/ evaluations/ research_questions/
  sources/ claims/
  catalog/ graph/ search/ context_packs/
06_evaluation/
  wiki_metrics.yaml
  questions.yaml
  compiler_validation.yaml
07_review/
  page_queue.yaml
08_release/
  wiki_change.yaml
  wiki_build_manifest.yaml
  change_feed.jsonl
```

所有生成页面均保持 `review` 状态，并带有稳定 ID、claim/source refs、typed outgoing links、section-level claim refs、构建来源、freshness 和 review metadata。

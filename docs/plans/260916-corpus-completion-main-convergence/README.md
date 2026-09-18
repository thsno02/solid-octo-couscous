# 非 repo 正文物化与 `main` 收敛执行计划 — 2026-09-16

> 状态：**规划契约，2026-09-18 已提出统一 ingestion 执行重置**。本目录定义下一阶段如何执行，不代表正文缺口已经补齐，也不代表 PR #1 已经进入 `main`。

## 权威依据

本计划由以下输入共同约束：

- Issue #3：纠正物化 scope 与验收口径，补齐非 GitHub repository 来源的正文获取和预处理缺口；
- Issue #4：建立现有分支与 stacked PR 向 `main` 收敛的整合逻辑；
- 当前远端基线：
  - `main`：`99ce4670be91637209d67792de0962404fa96488`
  - 临时集成分支：`work/v0-meta-kb-initialization-demo-260910`
  - 本次 ingestion reset 基线：`4b179e3c0a932f41db493c95f5e8974dfdb599ae`
  - PR #1：open / Draft，目标为 `main`
  - PR #2：已合入上述临时集成分支，不得重复 cherry-pick

若后续远端状态变化，执行者必须先更新基线台账，再开始新的实现；不得沿用旧 SHA、旧计数或旧 CI 结论。

## 本计划作出的决定

1. **唯一最终目标是 `main`。** 现有 `work/v0-meta-kb-initialization-demo-260910` 只作为 PR #1 生命周期内的临时集成分支。
2. **PR #1 是当前工作进入 `main` 的唯一父 PR。** 后续短期实现 PR 均以最新 work head 为 base，并回流到该 work 分支；不再创建第二条长期总集成分支。
3. **先完成 Issue #3，再收口 PR #1。** 不以“215 条都有 capsule”、许可审计计数、CI 绿灯或 `trusted=0` 中任一单项替代正文物化完成度。
4. **正文获取、文本/结构提取、公开再分发、知识准入是独立维度。** 它们必须分别记录和验收，不能互相充当代理指标。
5. **后续不再按每 10 个 UID 创建一个 PR。** 网络请求仍可内部按不超过 25 UID 的 chunk 限流，但 chunk 不是 PR 边界；执行改为一个 parser benchmark PR、一个统一 engine PR、默认一个 131 条 backfill PR。
6. **共享 parser 问题按 failure class 聚合。** 只修一次通用能力，再对全部受影响来源回放；单 UID PR 默认禁止。
7. **引入统一 Document IR。** 原件、native parser output、统一 IR、selector/provenance 分层保留，不再要求所有 PDF、TeX 和 HTML 使用同一个 parser。
8. **Agent 必须受预算和停止条件约束。** 同一 PR 最多两次修复循环；连续两次迭代无 coverage/failure-class 增量必须停止；同 HEAD 不重复 CI 或 evaluator。
9. **全局生成延迟到输入冻结。** parser-only 变更默认不重建全部 Wiki；index/registry/Wiki 在最终输入冻结后串行重建，避免大量无意义 churn。
10. **不自动删除文件、不重写历史、不删除分支、不修改仓库保护设置。** 任何此类动作都必须有单独、具体、可审阅的授权。
11. **每个 PR 关闭前仍须独立 evaluator PASS。** 但 evaluator 只对新 HEAD 运行一次；不能用重复审核替代真实数据进展。
12. **最终建议使用 squash 将 PR #1 合入 `main`。** 进入 `main` 的是最终验证树；详细执行历史通过 PR、issue、阶段报告和 work 分支保留。该选择仍需在 PR #1 最终放行时确认。

## 目标数据范围

当前 collection 共 215 条来源：

- GitHub repository：84 条，继续走固定 commit 的 repository semanticization 路径，**不进入本次正文抓取分母**；
- 非 repository：131 条，构成本计划的正文获取与预处理范围；
  - 当前标记 `full_text`：90 条；
  - 当前为 excerpt：27 条；
  - 当前为 metadata-only：14 条；
  - 另有 2 条已知解析不完整。

这些标签不是完成度结论。现有 131 条 coverage ledger 是 benchmark 选样、全量 backfill 和 failure class 聚合的输入。

## 2026-09-18 执行重置

此前串行 P3 PR 证明了逐 UID 审计、原件保全和 deterministic replay 可以做得很严格，但也出现了局部最优：PR、审计文字、生成物和验证轮次持续增加，统一解析能力与 `complete_target_consumable` 没有同比增长。

因此，旧的“一个 action bucket、最多 10 UID、合入后再开下一批”不再作为后续 PR 边界。新的主流程是：

```text
P0/P1 已有规划与 131 条 coverage ledger
→ P2 代表性 parser bake-off + Document IR 契约
→ P3-A 统一 acquisition / classifier / parser router / IR / failure ledger
→ P3-B 对 131 条非 repo 一次性 backfill
→ P4 全量对账、受影响派生物重建、PR #1 口径修正
→ P5 PR #1 最终独立检查、合入 main、fresh checkout 验证
```

已在本重置前启动并公开合同的批次可按原精确范围完成；本重置合入后不得再创建新的逐 UID/小批次正文 PR，除非满足 `07` 文档列出的身份、法律、安全或破坏性迁移例外。

## 统一 parser 路由候选

| 表示 | 首选候选 | fallback |
| --- | --- | --- |
| arXiv TeX | LaTeXML | 保守 TeX reading view → PDF 路由 |
| born-digital 论文 PDF | GROBID | Docling |
| 扫描/低 text-layer PDF | Docling OCR | benchmark 后批准的 MinerU |
| 普通文章 HTML | Trafilatura | Docling HTML / 有界 DOM adapter |
| 标准/规范 HTML | 有界 DOM adapter | Docling HTML / Trafilatura |

候选工具只有在 benchmark 记录质量、资源、依赖、许可证和确定性后才能成为生产依赖。

## 文档导航

- [`01-current-state-and-decisions.md`](01-current-state-and-decisions.md)：当前事实、问题判断和不可混淆的决策。
- [`02-scope-and-state-contract.md`](02-scope-and-state-contract.md)：来源范围、目标文档边界、状态模型和完成定义。
- [`03-execution-plan.md`](03-execution-plan.md)：原分阶段实施历史；其 P2/P3 小批次规则由第 07 文档和 `plan.yaml` v3 覆盖。
- [`04-integration-plan.md`](04-integration-plan.md)：分支／PR 台账、stack 生命周期、最终合并与回滚。
- [`05-validation-and-definition-of-done.md`](05-validation-and-definition-of-done.md)：内容、结构、生成物和 `main` 落地验收。
- [`06-codex-execution-contract.md`](06-codex-execution-contract.md)：供 Codex/agent 使用的 MUST、MUST NOT、停止条件、效率字段和报告模板。
- [`07-unified-ingestion-pipeline-and-agent-budget.md`](07-unified-ingestion-pipeline-and-agent-budget.md)：统一 parser router、Document IR、全量 backfill 和 Agent/API 消耗边界。
- [`plan.yaml`](plan.yaml)：机器可读的执行合同，v3 为当前提案。
- [`branch-ledger.yaml`](branch-ledger.yaml)：当前分支、PR、依赖与最终落点。

## 本重置合入后的第一个实现 PR

第一个实现 PR 是 **P2 parser bake-off**，而不是继续处理下一个 UID 小批次。它必须：

- 从 131 条 ledger 中明确列出代表性 benchmark UID；
- 覆盖 TeX、born-digital PDF、扫描/低文本 PDF、普通 HTML、规范 HTML和已知失败类别；
- 对适用样本比较至少两个合理候选；
- 输出统一 Document IR 草案、质量评估和选定路由；
- 不做全量 backfill、不重建整个 Wiki、不为单个 UID 添加 production 特例。

只有 P2 合入后，才开始 P3-A engine；只有 engine 冻结后，才执行 P3-B 全量 backfill。

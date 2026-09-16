# 非 repo 正文物化与 `main` 收敛执行计划 — 2026-09-16

> 状态：**规划契约（planning contract）**。本目录定义下一阶段如何执行，不代表正文缺口已经补齐，也不代表 PR #1 已经进入 `main`。

## 权威依据

本计划由以下输入共同约束：

- Issue #3：纠正物化 scope 与验收口径，补齐非 GitHub repository 来源的正文获取和预处理缺口；
- Issue #4：建立现有分支与 stacked PR 向 `main` 收敛的整合逻辑；
- 当前远端基线：
  - `main`：`99ce4670be91637209d67792de0962404fa96488`
  - 临时集成分支：`work/v0-meta-kb-initialization-demo-260910`
  - 规划基线提交：`568d31de26c918a9251fadf9488a47ae3405c034`
  - PR #1：open / Draft，目标为 `main`
  - PR #2：已合入上述临时集成分支，不得重复 cherry-pick

若后续远端状态变化，执行者必须先更新本计划中的基线台账，再开始新的实现批次；不得沿用旧 SHA、旧计数或旧 CI 结论。

## 本计划作出的决定

1. **唯一最终目标是 `main`。** 现有 `work/v0-meta-kb-initialization-demo-260910` 只作为 PR #1 生命周期内的临时集成分支。
2. **PR #1 是当前工作进入 `main` 的唯一父 PR。** 后续短期实现 PR 均以最新 work head 为 base，并回流到该 work 分支；不再创建第二条长期总集成分支。
3. **先完成 Issue #3，再收口 PR #1。** 不以“215 条都有 capsule”、许可审计计数、CI 绿灯或 `trusted=0` 中任一单项替代正文物化完成度。
4. **正文获取、文本提取、公开再分发、知识准入是四个独立维度。** 它们必须分别记录和验收，不能互相充当代理指标。
5. **一次只允许一个活跃实现批次。** 每个批次最多处理 10 个明确 UID；合入 work 后，下一批才从新的 work head 创建。
6. **本规划 PR 只增加计划与台账。** 不修改 source、manifest、registry、selector、Wiki、pipeline、workflow 或生成物。
7. **最终建议使用 squash 将 PR #1 合入 `main`。** 进入 `main` 的是最终验证树；详细执行历史通过 PR、issue、批次台账和 work 分支保留。该选择仍需在 PR #1 最终放行时确认，当前计划不执行合并。
8. **不自动删除文件、不重写历史、不删除分支、不修改仓库保护设置。** 任何此类动作都必须有单独、具体、可审阅的授权。

## 目标数据范围

当前 collection 共 215 条来源：

- GitHub repository：84 条，继续走固定 commit 的 repository semanticization 路径，**不进入本次正文抓取分母**；
- 非 repository：131 条，构成本计划的正文获取与预处理范围；
  - 当前标记 `full_text`：90 条；
  - 当前为 excerpt：27 条；
  - 当前为 metadata-only：14 条；
  - 另有 2 条已知解析不完整，需要单独修复。

这些是规划基线，不是永久常量。Phase 1 必须从实际 manifest 重新计算并列出全部 131 个 UID。

## 执行顺序

```text
P0 规划契约（本 PR）
→ P1 131 条非 repo 覆盖台账与真实分母
→ P2 两项已知解析修复
→ P3 按 action bucket 顺序补齐正文与预处理（一次一个批次）
→ P4 全量对账、受影响派生物重建、PR #1 口径修正
→ P5 PR #1 最终独立检查、合入 main、全新 checkout 验证
```

禁止跳过 P1 直接按旧的 41 条数字批量抓取；P1 可能发现 `full_text` 标签下仍有错误页、摘要页、目录页、截断文本或版本错配。

## 文档导航

- [`01-current-state-and-decisions.md`](01-current-state-and-decisions.md)：当前事实、问题判断和不可混淆的决策。
- [`02-scope-and-state-contract.md`](02-scope-and-state-contract.md)：来源范围、目标文档边界、状态模型和完成定义。
- [`03-execution-plan.md`](03-execution-plan.md)：分阶段实施顺序、每批文件责任和回流方式。
- [`04-integration-plan.md`](04-integration-plan.md)：分支／PR 台账、stack 生命周期、最终合并与回滚。
- [`05-validation-and-definition-of-done.md`](05-validation-and-definition-of-done.md)：内容、结构、生成物和 `main` 落地验收。
- [`06-codex-execution-contract.md`](06-codex-execution-contract.md)：供 Codex/agent 使用的 MUST、MUST NOT、停止条件和报告模板。
- [`plan.yaml`](plan.yaml)：机器可读的执行合同。
- [`branch-ledger.yaml`](branch-ledger.yaml)：当前分支、PR、依赖与最终落点。

## 计划获批后的第一个实现 PR

第一个实现 PR **只能**完成 P1：从现有 repo 生成 131 条逐项覆盖台账，纠正分母和状态字段，不进行联网抓取、不修改正文、不重建 Wiki。它必须让后续执行者能够回答：

> 对每个非 repo UID，目标文档是什么、当前本地实际有什么、还缺什么、为什么缺、下一步属于哪个 action bucket？

只有 P1 合入 work 后，才开始 P2/P3。

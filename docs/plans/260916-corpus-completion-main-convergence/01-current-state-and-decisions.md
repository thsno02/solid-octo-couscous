# 01 — 当前状态与决策

## 1. 当前远端状态

截至 2026-09-16，本计划使用以下远端事实：

| 对象 | 状态 | 当前值 | 含义 |
| --- | --- | --- | --- |
| `main` | branch | `99ce4670be91637209d67792de0962404fa96488` | 最终共享基线；尚未包含 PR #1 的主要成果 |
| work branch | branch | `568d31de26c918a9251fadf9488a47ae3405c034` | PR #1 的临时集成分支 |
| PR #1 | open / Draft | base=`main` | 物化、meta-KB、LLM Wiki 与后续修复的父 PR；尚未进入 `main` |
| PR #2 | merged | merge commit=`37ccf4e86d106866273c147280fe1d0efe1ba6fb` | 已进入 work branch；不得再次 cherry-pick |
| Issue #3 | open | 非 repo 正文物化纠偏 | 数据范围与验收主线 |
| Issue #4 | open | 分支／PR 收敛 | 整合与落地主线 |

“已 push”“子 PR 已 merged”“work CI 通过”都不等于成果已进入 `main`。

## 2. 当前 corpus 状态

基线计数：

| 范围 | 数量 | 当前解释 |
| --- | ---: | --- |
| 全部来源记录 | 215 | collection 记录总量；有 capsule 不等于有正文 |
| GitHub repository | 84 | 走 commit-pinned repository semanticization；不进入本文正文分母 |
| 非 repository | 131 | 本计划的正文获取与预处理分母 |
| 非 repo 标记 `full_text` | 90 | 标签需逐项验证，不能直接当完整正文覆盖数 |
| 非 repo excerpt | 27 | 仍需尝试取得目标正文或记录精确不可完成原因 |
| 非 repo metadata-only | 14 | 当前没有内容级可消费正文 |
| 已知解析不完整 | 2 | `arxiv:2406.04268` 与 `arxiv:2502.18864` |

已知的两项解析问题：

1. `arxiv:2406.04268`：已有 source 文件，但未正确识别 TeX root；
2. `arxiv:2502.18864`：原始 PDF 已保存，但第 4、20 页没有可提取文本；必须区分原件覆盖与文本提取覆盖，不能伪造 OCR 结果。

## 3. 为什么当前不能直接宣布物化完成

以下命题均不成立：

```text
215 条都有 capsule
⇒ 215 条都有正文

content_tier = full_text
⇒ 目标文档边界和文本提取均完整

publication blocked
⇒ 正文没有取得

CI green
⇒ 获取、解析、许可和知识可信均完成

trusted_claims = 0
⇒ candidate corpus 不允许进入 main
```

CI 目前主要证明结构、hash、selector、生成物和确定性重放在其覆盖范围内通过。它不能替代对正文边界、错误页、摘要页、目录页、截断、缺页和版本一致性的逐项核查。

## 4. 对两个 issue 的判断

### Issue #3 是当前内容主线

优先级最高的工作不是继续扩展许可审计，也不是新增研究来源，而是：

```text
131 条非 repo 来源逐项建账
→ 找出真实正文缺口
→ 修复获取与解析
→ 持久化原件／文本／selectors
→ 验证远程 checkout 可消费
```

许可仍需记录，但它只决定哪些 bytes 可以留在公开 Git 树中，不得充当正文获取完成度的替代指标。

### Issue #4 是执行前置条件

当前 work 分支已经承载 34 个左右的历史提交和大量生成物。继续随意开长期分支会造成：

- 旧 base 上重复修复；
- PR #2 被重复应用；
- 输入与生成物分离；
- 子 PR 绿灯但 `main` 长期不落地；
- Codex 将某个局部 gate 误解成总体目标。

因此后续必须串行、短分支、明确 base、明确 UID、明确回流点。

## 5. 已确定的治理决策

### 5.1 临时集成主线

```text
main
  ↑ PR #1（唯一父 PR）
work/v0-meta-kb-initialization-demo-260910
  ↑ 规划 PR 与后续串行实现 PR
短期 batch branch（一次一个）
```

不得再建立另一条长期“总集成”分支。

### 5.2 最终合并策略

默认建议 PR #1 最终采用 **squash merge**：

- `main` 接收一个最终验证树与一个清晰回滚点；
- 不把 34+ 个试验性和生成物中间提交全部导入主线；
- 详细历史仍由 PR、issue、batch ledger 和临时 work branch 保留；
- squash 后不能仅靠 ancestry 判断 PR #2/子批次是否吸收，必须以最终文件树、build manifest 和 branch ledger 对账。

该策略只在最终放行阶段执行；本计划不授权立即合并或改写历史。

### 5.3 PR #1 的真实完成条件

PR #1 可以进入最终 review 的必要条件是：

1. Issue #3 的 131 条逐项台账与正文／提取口径完成；
2. 可合法持久化的目标正文和必要预处理产物已进入 work；
3. 尚不可完成的条目有具体原因、尝试证据和未决动作，未被静默降级；
4. 原始输入、manifest、registry、selectors 和受影响生成物一致；
5. PR #1 描述与文档不再使用“有 capsule 即完成”的旧口径；
6. 最终 work head 针对实际 `main` base 重新验证；
7. 合入 `main` 后由全新 checkout 复验。

人工 trusted admission 和 branch protection 是独立治理工作，不被擅自新增为 candidate corpus 的内容完成门槛。

## 6. 本规划 PR 不做什么

- 不联网抓取；
- 不修改 215 个 capsule；
- 不重新分类任何具体 source；
- 不重建 meta-KB 或 LLM Wiki；
- 不关闭 Issue #3/#4；
- 不把 PR #1 标为 ready；
- 不合并 PR #1；
- 不删除、迁移或重许可现有文件；
- 不修改 branch protection 或 required checks。

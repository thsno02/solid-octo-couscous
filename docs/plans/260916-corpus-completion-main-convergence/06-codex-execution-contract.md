# 06 — Codex / Agent 执行合同

本文件用于防止上一轮出现的 scope 漂移、代理指标替代、分支误判和“计划被理解成授权执行”问题。

## 1. 唯一主任务

> 对当前 collection 中的 131 条非 GitHub repository 来源，完成可核查的目标正文获取、预处理、本地持久化和可消费验证；然后将既有 work 分支上的全部批准成果经 PR #1 收敛到 `main`。

这句话中的每个限定词都不可省略：

- **当前 collection**：不扩展研究来源；
- **131 条非 GitHub repository**：不是 215，不包括 84 个 repo；
- **目标正文**：不是整个站点、整条引用网络或抓取器碰巧下载的所有组件；
- **获取、预处理、持久化、验证**：四个步骤都要有证据；
- **经 PR #1 收敛到 main**：不能只停留在新分支。

## 2. 开始任何实现前的必读顺序

执行者必须读取并在 PR 中确认：

1. Issue #3；
2. Issue #4；
3. 本目录 `README.md`；
4. `02-scope-and-state-contract.md`；
5. `03-execution-plan.md`；
6. `04-integration-plan.md`；
7. `plan.yaml` 与 `branch-ledger.yaml`；
8. 当前 work branch head、PR #1 状态和上一批 PR 是否已合入。

若其中任一状态与远端不一致，先只更新计划台账，不开始正文修改。

## 3. 每个实现 PR 的启动声明

PR body 第一段必须使用以下结构：

```yaml
execution_contract:
  plan_id: nonrepo-materialization-main-convergence-260916
  phase: P1 | P2 | P3-* | P4 | P5
  base_branch: work/v0-meta-kb-initialization-demo-260910
  base_sha: <exact SHA>
  target_branch: work/v0-meta-kb-initialization-demo-260910
  source_uids: [<complete list>]
  allowed_paths: [<complete list or controlled patterns>]
  generated_paths: [<complete list or none>]
  explicitly_out_of_scope: [<items>]
```

若 UID 列表为空或使用“等”，不得执行。

## 4. MUST

执行者必须：

1. 从最新 work head 创建短期分支；
2. 一次只执行一个 phase 或一个 action bucket；
3. 网络批次不超过 10 个 UID；
4. 先固定 target identity 和 selected version，再下载；
5. 报告真实 URL、响应、错误和时间，不把计划尝试写成已完成；
6. 分开记录 original artifact、text extraction、public redistribution 和 knowledge admission；
7. 保留原始 artifact，normalized/OCR 只能是派生层；
8. 对每个 source 给出 before/after；
9. 只重建受影响生成物；
10. 在当前 head 上运行对应 tests/validators；
11. 让 unresolved 保持显式，不为通过计数而降级或猜测；
12. 合入 work 后再开始下一批；
13. 更新 coverage ledger 和 branch/work-item ledger；
14. 在总结中明确“已完成什么、未完成什么、是否进入 main”。

## 5. MUST NOT

执行者不得：

1. 把“215 条都有 capsule”解释为正文物化完成；
2. 把 `full_text` 标签直接当目标正文完整；
3. 把 rights allow/block 数量当获取缺口数量；
4. 把 CI 绿灯当正文、许可或 trust 完成；
5. 把 `trusted=0` 或人工 Wiki review 新增为 candidate corpus 的实现门槛；
6. 为完成一篇论文递归下载其引用、数据集、模型权重或全部外链；
7. 把 TeX 包中所有 `.sty/.cls/.bst`、旧稿、评审和第三方摘要默认算作用户要求的正文；
8. 为了“更完整”新增 collection 中不存在的 source UID；
9. 绕过登录、付费墙、访问控制、robots 或站点限制；
10. 在公开 repo 中先提交许可状态未知的新增全文，再补审计；
11. 自动删除现有原文、迁移存储、改写 Git 历史或删除分支；
12. 强推共享 work 分支；
13. 重复 cherry-pick PR #2；
14. 创建第二条长期集成分支；
15. 并行开启多个会修改 index/registry/coverage ledger 的 batch；
16. 批量选择 `ours/theirs` 解决生成物冲突；
17. 修改大量派生文件但不更新输入／生成器；
18. 把 OCR 文字冒充 source-authored text；
19. 使用旧 SHA 的 CI 结果替代当前 head 验证；
20. 使用“已全部完成”“端到端完成”等表述，除非 Definition of Done 全部满足并已进入 `main`。

## 6. 允许继续与必须停止的条件

### 6.1 记录后可继续其他 UID

下列情况只阻塞当前 UID，不阻塞批次中其他独立来源：

- 404/403/证书或临时网络失败；
- 付费墙或登录；
- 公开再分发状态未决；
- 某 PDF 页面无法可靠提取；
- canonical URL 失效但身份明确；
- 无法取得作者稿。

必须将该 UID 标为 unresolved，并记录下一步。

### 6.2 整个 PR 必须停止

出现以下任一情况，应停止修改并在 PR/issue 报告：

- base branch 已移动且可能影响相同输入或生成物；
- 一个 UID 对应多个无法判定的目标作品／版本；
- 计划要求删除、迁移或历史重写，但没有明确授权；
- 需要新增长期集成分支；
- 同一 UID 正被另一个活跃 PR 修改；
- 当前 batch 超过 10 个 UID；
- 需要改变 scope 才能继续；
- 生成器改变会重写大量未受影响来源；
- 验证失败但修复会超出本 phase。

停止不等于放弃：提交具体 blocker、受影响 UID、已完成证据和最小决策请求。

## 7. P1 的特殊合同

P1 只能盘点。Codex 不得在 P1：

- 发起网络请求；
- 修复 parser；
- 重写 manifest；
- 重建 Wiki；
- 继续许可逐组件审计；
- 自动把 90 条 `full_text` 判定为 complete。

P1 的唯一成功是：131 条 coverage ledger 准确、可复算、可驱动后续批次。

## 8. P2/P3 的特殊合同

- 只处理 PR body 列出的 UID；
- 每条 source 的下载与解析必须有独立结果；
- 不能因为其中一条失败就把整个批次描述为失败或成功；
- `source package retained` 不等于 `target body verified`；
- 若只是修正 canonical metadata，不得声称已取得正文；
- 若取得完整原件但文本部分缺失，状态必须是 artifact complete + extraction partial；
- 若正文可获取但不能公开持久化，状态必须反映这一事实，不得改写为 unavailable。

## 9. P4/P5 的特殊合同

P4 不再继续抓取新来源。它只做对账、重建和 PR #1 收口。

P5 不允许 agent 自行：

- 标记 PR #1 Ready；
- merge/squash；
- 修改 main 保护；
- 删除分支；
- 关闭 issue。

这些是明确的人工决策点。Agent 可以准备精确状态和执行命令，但不能把计划变成未经授权的动作。

## 10. 汇报模板

每次执行结束必须使用：

```markdown
## Executed scope
- phase:
- base SHA:
- head SHA:
- UIDs:

## Source results
| UID | artifact before→after | extraction before→after | persistence | redistribution | unresolved |

## Files
- handwritten inputs:
- original artifacts:
- derived text/selectors:
- regenerated outputs:

## Verification
- commands actually run:
- local results:
- CI run for this exact head:

## Explicit non-results
- not merged to main
- no trusted promotion
- no branch deletion/history rewrite
- remaining UIDs / blockers
```

若没有 `Explicit non-results`，报告不合格。

## 11. 偏差检测问题

执行者在提交前必须逐项回答“否”：

- 我是否把许可审计当成了正文抓取任务？
- 我是否扩大到 collection 之外？
- 我是否把附带模板／引用材料当成目标正文？
- 我是否用 capsule/full_text/CI/trusted 任一计数替代逐项覆盖？
- 我是否创建了未登记的长期分支？
- 我是否重复应用了 PR #2？
- 我是否修改了未列出的 UID？
- 我是否声称进入 main，但实际只在 work/batch branch？
- 我是否把计划、尝试或推测写成已完成事实？

任何一个答案为“是”，不得提交，应先收缩变更。

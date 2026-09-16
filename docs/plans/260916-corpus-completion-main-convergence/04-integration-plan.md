# 04 — 分支、PR 与 `main` 整合计划

## 1. 当前 stack

```text
main @ 99ce467
  ↑ PR #1（open / Draft）
work/v0-meta-kb-initialization-demo-260910 @ 568d31d
  ├─ 已包含 PR #2 merge commit 37ccf4e
  └─ 后续接收本规划 PR 与串行实现 PR
```

PR #2 已被父分支包含。任何后续执行都不得再次 cherry-pick PR #2 的提交，也不得因为 audit branch 仍存在而推断其修复“尚未进入 work”。

## 2. 分支角色

| 分支类别 | 生命周期 | base | PR target | 允许用途 |
| --- | --- | --- | --- | --- |
| `main` | 长期 | — | — | 最终共享基线 |
| 当前 work branch | PR #1 生命周期 | `main` 的既有后代 | `main` | 唯一临时集成分支 |
| planning branch | 短期 | 最新 work | work | 仅计划、台账和执行合同 |
| implementation batch | 短期、串行 | 最新 work | work | 一个 phase 或最多 10 个明确 UID |
| reconciliation branch | 短期 | 最新 work | work | P4 全量对账与 PR #1 收口 |

禁止：

- 再建长期 `integration/*` 或第二个父 PR；
- 让多个 batch branch 同时修改同一份 index/registry/coverage ledger；
- 直接以 `main` 为 base 开展 Issue #3 的实现，导致 PR #1 的已有成果丢失；
- 将子 PR 直接改 target 为 `main`，绕过 work 的一致输入树；
- 未经授权强推共享 work、重写历史或删除分支。

## 3. 串行执行协议

每个实现 PR 在创建前必须：

1. 确认上一实现 PR 已经合入 work；
2. 重新读取 work head SHA；
3. 从该 SHA 创建新分支；
4. 在 PR body 中写明：
   - `base_sha`；
   - phase / batch ID；
   - 全部 source UID；
   - 允许修改的目录；
   - 明确不做的内容；
   - 预期生成物；
   - 验收命令。

若 work head 在执行期间发生变化：

- 停止新增修改；
- 判断是否触及同一输入或生成物；
- 先同步并重新验证；
- 不使用旧 CI 结果顶替新 base 上的检查。

## 4. 输入与派生物依赖

合并和冲突处理顺序固定为：

```text
canonical metadata / selected version
→ original artifacts
→ normalized text / source maps
→ selectors / hashes
→ capsule manifest
→ materialized_sources/index
→ source registry
→ evidence / claims（仅受影响 selected sources）
→ Wiki / graph / search / context packs
→ validation / review / release manifests
```

冲突处理不得：

- 对生成物批量采用 `ours` 或 `theirs` 后宣称成功；
- 只合入脚本而遗漏该脚本所要求的版本化数据；
- 只合入生成物而不保留对应输入和生成器；
- 手工编辑大量派生文件来掩盖生成器错误。

发生生成物冲突时，先合并上游输入和生成器，再从选定输入重新生成。

## 5. 工作项到最终落点

| 工作项 | 当前／未来 PR | 先进入 | 最终进入 |
| --- | --- | --- | --- |
| CI 通用只读门控 | PR #2，已完成 | work | 通过 PR #1 进入 main |
| 本执行计划 | 本 planning PR | work | 通过 PR #1 进入 main |
| 131 条 coverage ledger | P1 PR | work | 通过 PR #1 进入 main |
| 两项解析修复 | P2 PR | work | 通过 PR #1 进入 main |
| 正文获取批次 | P3 串行 PR | work | 通过 PR #1 进入 main |
| 全量对账与 DoD 修正 | P4 PR | work | 通过 PR #1 进入 main |
| 最终候选 tree | PR #1 | — | main |

此表必须随每次新增实现 PR 更新。没有最终落点的分支或提交不得被称为“完成”。

## 6. PR #1 最终合并策略

### 6.1 推荐方法：squash

原因：

- PR #1 已含多轮试验、自动生成和许可审计中间提交；
- `main` 更需要一个经最终验证的确定树和清晰回滚点；
- 细粒度历史仍可通过 PR、issue 和 work branch 访问；
- 可避免把不再存在于最终树中的中间状态导入 `main` 历史。

### 6.2 squash 前必须完成

- 最终 tree 与 Issue #3 scope 一致；
- branch ledger 列出所有已吸收的 PR/commit/work item；
- PR #2 和各 batch 的实际变更通过文件与 build manifest 对账；
- 无人使用“不是祖先”来错误判断 squash 后的吸收状态；
- 最终 PR #1 描述只保留当前快照，历史长日志可移至单独文档；
- 明确列出未解决来源，不将其隐去。

### 6.3 不在本计划自动执行的动作

- 将 PR #1 标为 Ready；
- squash/merge PR #1；
- 重写 work 历史；
- 删除 work/audit/batch 分支；
- 更改 branch protection；
- 关闭 Issue #3/#4。

以上动作均需要对应阶段的明确决定。

## 7. `main` 落地验收

合并后必须从远端 `main` 做全新 checkout，而不是复用 work 目录：

```text
clone/fetch main
→ 确认 merge/squash commit
→ 检查计划中承诺的关键文件
→ 重新计算 131 条 ledger 计数
→ 运行 tests / validators / reproducibility
→ 抽查原件、normalized text 和 selectors
→ 验证远程续作不依赖本机缓存
→ 记录 main SHA 和结果
```

只有这个步骤通过，Issue #4 的“进入 main”条件才完成。

## 8. 回滚

- 每个短期 PR 可通过其 merge commit 在 work 上回滚；
- PR #1 squash 后，`main` 有单一回滚 commit；
- 原始来源身份和 revision 不因回滚生成物而丢失；
- 不通过删除 Git 历史来伪装回滚；
- 若发现某来源持久化不适合公开保留，先提交受影响 UID、文件、claims/pages 和替代表示的影响分析，再执行移除决策。

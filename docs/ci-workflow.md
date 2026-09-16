# CI 与 Workflow 使用说明

## 两条流程，两个判断

| 流程 | 触发方式 | 成功意味着什么 | 不做什么 |
| --- | --- | --- | --- |
| `CI` → `Quality gate` | 所有 PR（不限目标分支）、合入 main、合并队列（merge group） | 单元测试、已提交产物的确定性重放、结构校验、工作树检查通过 | 不获取来源、不修改远端、不批准发布 |
| `Acquire sources manually` | 人工 workflow_dispatch | 本次网络获取、物化、构建和结构校验执行成功 | 不定时运行、不提交、不上传全文、不发布 |

物化流程的结果只存在于临时 runner，任务结束后不会保留；它目前是诊断入口，不是持久化服务。需要保存物化结果时，在本地运行 `make materialize`，审阅许可和差异后，通过 PR 提交允许发布的内容。来源的 metadata-only、partial 等状态仍需阅读报告，运行成功不保证所有 URL 已获取全文。

**CI green 仅表示代码、结构与确定性重放通过；不表示公开分发许可（publication rights）、人工编辑准入（human editorial admission）或发布批准（release approval）已通过。** 许可检查器 `scripts/validate_publication_rights.py` 保持 fail-closed；当前没有自动发布路径，不能把获取成功当成绕过它的依据。

## 通用质量门控（Quality gate）

执行顺序为：干净检出 → 安装固定依赖 → `make test` → `make reproducibility` → 检查完整工作树。重放命令先记录已提交产物，再首次构建，比较新增、删除、内容变化；随后验证重复构建与只读校验。因此不能在重放之前添加 `make demo` 等预构建步骤。

PR 不使用路径或目标分支过滤，文档 PR、普通 PR、堆叠 PR（stacked PR）都会得到同一项检查。仅 main 的 push 另跑合并后验证，避免 PR 分支 push 重复运行。新提交会取消同一 PR 的旧任务；排查时应看最新提交对应的检查。

两条 workflow 都只申请 `contents: read`，checkout 不保留凭证；不用 `pull_request_target`，不执行自动提交。Python 固定为 3.12.13，直接及传递依赖在 `requirements-materialization.txt` 中固定版本；Actions 固定发布标签，runner 固定 ubuntu-24.04。这减少版本漂移，但不宣称完整供应链不可变：runner 镜像仍更新，发布标签也不是不可变提交。

依赖更新作为普通 PR 一次性修改解析后的版本集合，使用干净 Python 3.12.13 环境安装，重新运行测试和重放。暂不引入缓存、测试矩阵或额外生成脚本。

## 失败时怎么判断

| 现象 | 类型 | 正当处理 |
| --- | --- | --- |
| 安装依赖时超时、runner 未启动 | 平台或安装网络问题 | 查看失败步骤，确认无代码问题后重试最新运行 |
| 单元测试、结构校验失败 | 内容或实现问题 | 本地复现、修复、提交，让新提交重新检查 |
| `committed_tree_replay` 失败 | 已提交生成物与输入不一致 | 本地构建，审阅生成差异并一并提交，不在 CI 里自动修正 |
| 工作树不干净 | 测试或构建产生额外副作用 | 检查列出的路径，修复副作用或补齐应提交产物 |
| 手动物化遭遇 403、限流、超时 | 外部来源访问问题 | 查具体来源和 partial 状态，不归因于离线代码门控 |
| 检查不存在、持续 Pending | 触发配置或必需检查名称不匹配 | 检查最新 PR 事件与 ruleset，不能用旧提交或手动运行的绿灯顶替 |

最小本地复现：

```bash
python -m pip install -r requirements-materialization.txt
make test
make reproducibility
git status --short --untracked-files=all
```

工作树检查对普通未跟踪文件也生效；已忽略的 Python 缓存不属于版本化产物。重放会在本地重新生成文件，运行前先保存自己的工作。

## 仓库设置与剩余门控

Workflow 文件只负责执行，不能自行强制 GitHub 禁止合并。管理员需要另外配置 PR-only、必需检查、禁止强推及禁止 bypass。本轮没有修改仓库设置。

待新的检查在 PR 中成功出现后，从 GitHub 设置里的实际检查列表选择 `Quality gate`（所属 workflow 为 `CI`），不要继续要求已经删除的旧 `build`、`validate` 检查。保持检查名称唯一且稳定。如果启用合并队列，已有 `merge_group` 事件会执行相同门控。

PR #2 的目标是修复工程检查；合入其父分支不会表示 PR #1 已获得公开全文许可或人工编辑批准。公开全文许可仍是候选内容进入公开仓库的门控；人工编辑准入则约束可信晋升或正式知识发布，不自动等同于候选代码 PR 的必需人工审批。不得因此修改 review、admission 或 trusted 状态。

依据：GitHub 官方说明指出，路径/分支过滤导致的未运行检查可能持续 Pending，必需检查应对应最新提交；参见[必需检查排障](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks)。合并队列需要独立的 `merge_group` 事件，参见[Workflow 触发事件](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)。

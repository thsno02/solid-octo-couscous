# CI 与 Workflow 使用说明

## 两条流程，两个判断

| 流程 | 触发方式 | 成功意味着什么 | 不做什么 |
| --- | --- | --- | --- |
| `CI` → `Quality gate` | 所有 PR（不限目标分支）、合入 main、合并队列（merge group） | 单元测试、已提交产物的确定性重放、结构校验、工作树检查通过 | 不获取来源、不修改远端、不批准发布 |
| `Materialize sources and propose repository update` | 人工 workflow_dispatch，所选分支作为 PR base | 无变更，或通过许可/校验的全文与派生产物已写入新提案分支并创建 Draft PR | 不定时运行、不直接写 base/main、不自动批准或合并 |

**GitHub repo 是全文与预处理产物的持久化位置（persistent store）。** 本地或 runner 只是临时工作区；不能用只保留本地、过期的 Actions artifact 或仅 metadata 链接代替文本入库。现有 `materialized_sources/corpus/` 已随工作分支提交，manifest 中的 `local_path` 指 checkout 内的相对路径，不意味着材料仅存在于某台电脑。

物化流水线执行：现有许可预检 → 测试 → 获取/预处理/构建/结构校验 → 重放 → 生成版本的许可检查 → 提案分支 commit/push → Draft PR → 独立 CI 与审查。只有这条人工触发的生产流程申请 `contents: write` 和 `pull-requests: write`；它不直接更新 base/main，不强推，不自动合并。每次运行使用新的 `codex/materialize-<run_id>-<attempt>` 分支，避免覆盖人的工作；无变化时不创建空 PR。普通 CI 仍只读。

公开仓库中的提案分支也公开，因此许可检查必须在 push **之前**执行。已放行来源、尚缺适用公众许可证据与已有许可但待履约的数量，以[当前许可审计](materialization-rights-audit.md)为准；本文不重复维护快照计数。整体生产流程仍会在预检停止，不能把这个预期阻断称为成功上传。Zep 已保存声明包但仍待非商业用途确认，不能把有 NOTICE 等同 allow。新 revision 若不匹配已有许可审计或声明的许可包，生产流程会失败，不会自动改写审计为 allow。来源的 metadata-only、partial 等状态仍需阅读报告，运行成功不保证所有 URL 已获取全文，也不表示已抓取单页来源链接的整个站点。

当前生产入口 `scripts/materialize_all_sources.py` 按响应内容区分 arXiv 的 tar、单文件 TeX、PDF 和错误页，支持 gzip；HTML/XML/JSON 错误页不会被标为 TeX 全文，会尝试备用入口。PDF 保留原件并按页提取文本，无文本页与失败页明确记录，定位器必须对应实际页的文本。未运行 OCR；图示页无可提取文字时状态为 partial。许可门也覆盖所有保留 `source_pdf` 的胶囊，不受文本层级降级影响。本修复不宣称覆盖未被当前 Makefile/workflow 调用的历史物化脚本。

许可附注以 manifest 的实际正文路径为准。TeX 正文位于 `normalized/document.txt` 时，链接指向 `../NOTICE.md`；根目录正文仍使用 `NOTICE.md`。生成器与校验器共用相对路径规则，重复 finalize 不重复追加附注。许可证以实际保存的组件为边界：论文许可不能自动覆盖第三方模板；需要的完整组件声明随同正文入库。

许可履约也可对已存、可追溯的文本快照离线执行：Schema.org 当前 URL 已更新，本次只给 repo 中既有快照加 NOTICE 和 ShareAlike 声明，未伪造网络重抓、命名 release 或替换正文。这不保证旧 URL 能重新返回旧字节；在线刷新仍需针对实际新 revision 重新核验。

**CI green 仅表示代码、结构与确定性重放通过；不表示公开分发许可（publication rights）、人工编辑准入（human editorial admission）或发布批准（release approval）已通过。** 许可检查器 `scripts/validate_publication_rights.py` 保持 fail-closed；文本入库的产品要求不等于自动授予第三方全文许可。

## 远程继续工作（Remote continuation）

### 许可随引用传递（Rights propagation）

来源包的 NOTICE 不是派生内容的自动授权。凡是复制来源表达的 evidence、claim、Wiki 页面或机器索引，都应保留与该来源及其版本对应的归属、许可、NOTICE 位置和摘录/转换说明；机器消费者也需要获得这些信息，不能只拿到匿名文本。混合页面按实际来源片段标示条件，不把某一来源的许可错误套到整个页面、独立作品或整个仓库。收集者自己的纳入理由与评述（collector assessment）不冒充来源正文，也不自动继承来源许可。

许可信息传递与发布放行是两个判断。保存 `CC-BY-NC-SA-4.0` 等条款不表示非商业（NonCommercial）用途已经核实；相同方式共享（ShareAlike）条件也不能在生成 Wiki 或 context pack 时丢失。尚缺实际用途或第三方范围证据的来源继续保持 `block`，工程测试通过不替代这些判断。

实现复用一套 `rights_propagation` 模块，不按来源 UID 写特例。来源实体保存声明包，evidence/claim 保存版本化引用，页面、catalog、graph、search、page plan 与 context pack 继续携带引用。校验器检查来源声明与实际渲染内容、机器视图的一致性；负测覆盖丢失引用、版本错配、把来源摘录伪装成 collector assessment、孤立 evidence 及页面删去许可说明。没有完整包的来源明确标为 `unavailable`，不据此删除现存文本，也不推定获得许可。

新任务 clone 对应的提案或工作分支后即可读取已提交的文本、manifest、registry 与派生候选，不需要依赖此前 runner 的文件，也不需要先重新联网抓取。固定到所需 commit 后运行：

```bash
python -m pip install -r requirements-materialization.txt
make test
make reproducibility
```

需要更新上游来源时才运行物化流程。它提交 `materialized_sources/`、`source_registry/`、物化完整性报告和实验派生产物；出现这些目录之外的未提交副作用会失败，不会顺便上传代码或凭证。

## 手动生产流程的启用条件

- Workflow 需要先进入默认分支，才能按 GitHub 的常规手动触发流程使用；不能用它还只存在于 PR 分支的状态声称已跑通远端上传。
- 仓库 Actions 设置必须允许 GitHub Actions 创建 PR。这里只声明 job 所需最小写权限，不更改仓库设置，不添加长期密钥；设置不允许时明确失败，不退回直推 main。
- 按 GitHub 当前规则，内置 `GITHUB_TOKEN` 创建/更新 PR 的 opened/synchronize/reopened 事件会产生待批准的 CI。具备 write 权限的人需在 PR 上选择 **Approve workflows to run**，然后等待最新提交的 `Quality gate`，而不是把物化任务的绿灯当作 PR 检查。
- 若 branch push 已成功、PR 创建却被设置或权限拒绝，文本仍保存在日志/summary 指明的提案分支；修复权限后从该分支创建 PR 即可，不删除已上传数据，也不强推重跑。

依据：[手动运行 Workflow](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow)、[GITHUB_TOKEN 的触发行为](https://docs.github.com/en/actions/concepts/security/github_token)、[Actions 仓库设置](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository)。

## 通用质量门控（Quality gate）

执行顺序为：干净检出 → 安装固定依赖 → `make test` → `make reproducibility` → 检查完整工作树。重放命令先记录已提交产物，再首次构建，比较新增、删除、内容变化；随后验证重复构建与只读校验。因此不能在重放之前添加 `make demo` 等预构建步骤。

PR 不使用路径或目标分支过滤，文档 PR、普通 PR、堆叠 PR（stacked PR）都会得到同一项检查。仅 main 的 push 另跑合并后验证，避免 PR 分支 push 重复运行。新提交会取消同一 PR 的旧任务；排查时应看最新提交对应的检查。

验证 workflow 只申请 `contents: read`；物化 job 的有限写权限仅用于提案分支与 PR。checkout 不保留凭证，不用 `pull_request_target`；只有生产流程最后的上传步骤配置 Git 身份与凭证，不对 base/main 自提交。Python 固定为 3.12.13，直接及传递依赖在 `requirements-materialization.txt` 中固定版本；Actions 固定发布标签，runner 固定 ubuntu-24.04。这减少版本漂移，但不宣称完整供应链不可变：runner 镜像仍更新，发布标签也不是不可变提交。

依赖更新作为普通 PR 一次性修改解析后的版本集合，使用干净 Python 3.12.13 环境安装，重新运行测试和重放。暂不引入缓存、测试矩阵或额外生成脚本。

## 失败时怎么判断

| 现象 | 类型 | 正当处理 |
| --- | --- | --- |
| 安装依赖时超时、runner 未启动 | 平台或安装网络问题 | 查看失败步骤，确认无代码问题后重试最新运行 |
| 单元测试、结构校验失败 | 内容或实现问题 | 本地复现、修复、提交，让新提交重新检查 |
| `committed_tree_replay` 失败 | 已提交生成物与输入不一致 | 本地构建，审阅生成差异并一并提交，不在 CI 里自动修正 |
| 工作树不干净 | 测试或构建产生额外副作用 | 检查列出的路径，修复副作用或补齐应提交产物 |
| 手动物化遭遇 403、限流、超时 | 外部来源访问问题 | 查具体来源和 partial 状态，不归因于离线代码门控 |
| 许可预检或生成版本检查失败 | 上传前的许可门控 | 完成对应版本的审计与条件，不移除检查、不把 block 改成无依据的 allow |
| 提案 PR 的 CI 等待批准 | 自动化 PR 的执行权限边界 | 由 write 权限用户批准运行，再等待真实 PR 检查 |
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

Workflow 文件只负责执行，不能自行强制 GitHub 禁止合并。建议管理员另外配置 PR-only、必需检查、禁止强推及禁止 bypass，作为持续治理加固（governance hardening）；这不是用户已授权的设置变更，也不是本次候选代码 PR 新增的内容合并门槛。本轮没有修改仓库设置。2026-09-16 的 `branches/main` 查询仍显示 `protected: false`。

`Quality gate` 校验工程测试、产物重放和工作树一致性，不直接运行整库实际许可放行检查。即使把它设为 required，也不能替代全文许可履约；真实许可门由生产流程上传前后检查，当前 PR 合并前仍须核对其完整结果。进入默认分支和允许 Actions 创建 PR，是手动物化生产入口的启用条件，不是它自己获准合并的循环前置条件。

待新的检查在 PR 中成功出现后，从 GitHub 设置里的实际检查列表选择 `Quality gate`（所属 workflow 为 `CI`），不要继续要求已经删除的旧 `build`、`validate` 检查。保持检查名称唯一且稳定。如果启用合并队列，已有 `merge_group` 事件会执行相同门控。

PR #2 的目标是修复工程检查；合入其父分支不会表示 PR #1 已获得公开全文许可或人工编辑批准。公开全文许可仍是候选内容进入公开仓库的门控；人工编辑准入则约束可信晋升或正式知识发布，不自动等同于候选代码 PR 的必需人工审批。不得因此修改 review、admission 或 trusted 状态。

依据：GitHub 官方说明指出，路径/分支过滤导致的未运行检查可能持续 Pending，必需检查应对应最新提交；参见[必需检查排障](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks)。合并队列需要独立的 `merge_group` 事件，参见[Workflow 触发事件](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)。

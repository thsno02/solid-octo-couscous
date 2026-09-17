# 05 — Validation 与 Definition of Done

验收分为五层。任何一层通过都不能替代其他层。

## 1. Coverage ledger 验收

P1 完成时必须满足：

- `non_repo_total = 131`，且可由当前 metadata/manifest 复算；
- `github_repo_excluded = 84`；
- 每个非 repo UID 恰好出现一次；
- 每条都有 selected version、target boundary 和 action bucket；
- 当前 27 个 excerpt、14 个 metadata-only 和 2 个已知 parser issue 全部可查询；
- `full_text` 条目未经过边界核查时只能处于 `needs_boundary_verification`；
- coverage 文件与人类可读报告计数一致；
- 该阶段没有正文 bytes 或生成物变化。

## 2. 单来源验收

### 2.1 Identity

- UID 稳定；
- canonical identifier 对应目标文档；
- selected version 明确；
- alternate URL 不改变文档身份；
- 标题相似但版本／作品不同的来源未被静默合并。

### 2.2 Original artifact

抽查并自动检查：

- 不是 HTML 错误页、登录页、摘要页、目录页或空标题；
- PDF 页数／HTML 章节／TeX include 边界与目标文档相符；
- hash、bytes、retrieved URL 和 retrieval record 一致；
- 原件覆盖缺口被具体列出。

### 2.3 Text extraction

- normalized text 不是导航、模板导言或重复源包拼接；
- TeX root/include graph 合理；
- PDF 页码与文本段落可对齐；
- HTML heading/block 结构可定位；
- OCR 输出标记为 derived；
- 缺页、图像页和不可提取部分不被隐藏。

### 2.4 Selectors

- 每个 selector 指向本地已 hash 文件；
- line/page/block 范围合法；
- preview 在目标文本中存在；
- selector 不越过截断后的本地内容；
- metadata-only 来源不伪造内容 selector；
- selector 数量不是质量代理，抽查必须验证语义范围。

### 2.5 Public persistence

- 公开 repo 中保留的内容有相应表示决策；
- `block/unknown` 不被误写为 `allow`；
- 获取成功不自动触发公开提交；
- 因不能公开保留而未入 repo 的正文，被记录为 `public_persistence_decision` 或 `unresolved`，不伪装成网络失败。

### 2.6 Knowledge state

- materialization 不改变 `trusted`；
- source-reported assertion、collector assessment 和 generated synthesis 继续区分；
- 若 evidence text 改变，受影响 claim/page 重新生成和验证；
- 未受影响来源不产生无关 Wiki diff。

## 3. 每个实现 PR 的必需报告

PR body 必须包含下表，不能只写叙述性总结：

| 字段 | 要求 |
| --- | --- |
| Base | branch + exact SHA |
| Phase / batch | 例如 `P3-B-02` |
| UIDs | 完整列表，不使用“等” |
| Before | 六个状态维度的旧值 |
| After | 六个状态维度的新值 |
| Retrieval attempts | URL、时间、结果、最终选用理由 |
| Files changed | 手写输入与生成物分开 |
| Unresolved | 每个 UID 的具体剩余问题 |
| Generated impact | 是否重建 demo/Wiki，为什么 |
| Tests | 实际执行命令与结果 |
| Non-goals | 明确本 PR 没有做什么 |

禁止使用：

- “基本完成”；
- “已全部 materialize”但没有 131 条复算；
- “CI 通过所以正文完整”；
- “rights blocked 所以没有数据”；
- “已审计所以 trusted”；
- “后续再处理”但没有 UID、原因和 action bucket。

## 4. 必需命令

具体命令可随 repo 变化调整，但每个实现 PR 至少需要运行与其影响范围相符的：

```bash
make test
make validate
make reproducibility
```

正文或 materialization 变化后，还需运行：

```bash
python scripts/validate_materialization_completeness.py
```

coverage ledger 建立后，应增加对应只读复算／校验命令。若 selected demo source 或 claim/evidence 输入变化，还需执行完整：

```bash
make demo
make validate
make reproducibility
```

所有结果必须来自当前 head；不得引用旧 head 的绿色 workflow 作为替代。

## 5. 内容抽查最低要求

### P1

- 所有 131 条机器可读计数；
- 人工抽查至少 10 个当前 `full_text`、全部 14 个 metadata-only、全部 2 个 parser issue；
- 27 个 excerpt 的 target boundary 与 limitation 均可读。

### 每个 P3 batch

- 批次内每个 UID 的原件开头、中部、结尾各检查一处；
- PDF 核对总页数和至少 3 页；
- HTML 核对 heading 层级、正文结尾和无导航污染；
- TeX 核对 root、至少一个 include 和结尾／附录；
- 所有新增 selector 至少抽查首、中、末各一条；
- 批次不超过 10 个 UID，因此不得抽样跳过某个 UID 的基本覆盖检查。

### P4

- 131 条全量复算；
- 逐项确认所有 unresolved 都有实际原因；
- 随机再抽查 20 条 `complete`；
- 检查 5 条跨 source type 的 remote-checkout 消费；
- 核对受影响 Wiki 页与 source/evidence chain。

## 6. Issue #3 Definition of Done

Issue #3 只有在以下条件同时满足时才能关闭：

- [ ] 131 条非 repo 来源具有逐项 coverage ledger；
- [ ] 27 excerpt、14 metadata-only、2 parser incomplete 均已逐项处理；
- [ ] 可合法取得并公开持久化的目标正文已入 repo；
- [ ] 未完成项具有真实尝试证据和明确状态，而不是静默降级；
- [ ] 原件覆盖、文本提取、公开再分发和 trust 四类状态独立；
- [ ] selectors、manifest、registry、index 与本地文件一致；
- [ ] 远程 checkout 可消费所有已声明 locally persisted 的来源；
- [ ] PR #1 和 docs 已改用新口径；
- [ ] 修复已进入 work，并通过 PR #1 实际进入 `main`。

## 7. Issue #4 Definition of Done

Issue #4 只有在以下条件同时满足时才能关闭：

- [ ] 所有活跃分支和 PR 都有 base、依赖、用途和 main 落点；
- [ ] PR #2 不被重复应用；
- [ ] 后续 batch 串行回流到唯一 work；
- [ ] 所有 34+ 个既有提交承载的最终成果有明确去向；
- [ ] 输入与派生物在最终 work tree 中一致；
- [ ] PR #1 针对实际 `main` base 重新验证；
- [ ] PR #1 已实际合入 `main`；
- [ ] 新 checkout 的 main 验证通过；
- [ ] 剩余分支有明确保留理由或经授权清理。

## 8. PR #1 Ready-for-Review 条件

以下条件满足后，才建议将 PR #1 从 Draft 改为 Ready：

1. Issue #3 的合并前数据条件（第 6 节前八项）已满足；最后一项“进入 main”属于合并后的关闭条件，不能倒置为 Ready 的前提；
2. P4 reconciliation 已合入 work；
3. PR #1 body 已清理旧快照和错误完成口径；
4. 最终 head 的 CI、coverage audit 和 reproducibility 全部通过；
5. 进入 `main` 的最终 tree 已明确；
6. 未决来源和公开存储决策清楚列出；
7. 没有把 human trusted admission 或 branch protection 冒充正文物化条件。

## 8.1 每个 PR 的独立关闭门控

适用于 P0、P1、P2、所有 P3 批次、P4 和父 PR #1。默认以正常合并（merge）完成 PR，而不是不合并直接关闭并遗弃工作。

- 规划者（planner）明确用户目标、当前证据、工作假设、候选路径和选择理由；执行者（executor）只实施批准范围；独立评估者（evaluator）不得是该变更的作者。
- evaluator 检查实际差异及证据，分别判断需求满足、agentic 判断链条（目标→判断→行动→验证→纠偏）和核心质量，输出 `PASS` 或 `FAIL` 与具体理由。CI 通过、脚本运行或报告写完都不能单独充当 PASS。
- 每次审核锁定精确 head SHA 和 base SHA；关闭前确认审核覆盖的差异未变化，适用 CI 为当前 head 对当前 base 的结果。任何变化均重新核验，不能沿用旧 PASS。
- `FAIL` 返回 planner → executor 修复 → 独立 evaluator 复审；只有 PASS 且适用门控满足才能合并。agent 审核如发布到 GitHub，标为 agent evaluation / COMMENT，不伪造人类 APPROVE。
- 审核记录保存在对应 PR；记录已执行和明确未执行内容。P0/P1 的 PASS 仅证明本阶段质量，不证明全 corpus 或父 PR 已完成。
- 如拟直接关闭而非合并，必须先证明工作已被其他 PR 吸收或明确被用户取消，独立 evaluator 同样审核，不用关闭隐藏未完成需求。

## 9. Post-merge Definition of Done

PR #1 merge 后必须追加一份落地记录，至少包含：

```yaml
main_commit: ...
merge_method: squash
source_pr: 1
verified_fresh_checkout: true
non_repo_total: 131
coverage_report: ...
ci_run: ...
reproducibility: pass
remaining_unresolved_sources: [...]
retained_branches: [...]
```

没有这份 `main` 验证记录，只能说 PR 已合并，不能说远程交接闭环完成。

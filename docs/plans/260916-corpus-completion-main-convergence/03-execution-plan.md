# 03 — 分阶段执行计划

> **2026-09-18 执行重置：** 本文件保留原始 P0–P5 设计与已发生批次的历史语义。其 P2/P3 中“最多 10 UID、一个小批次一个 PR、合入后再开下一批”的规则，已由 [`07-unified-ingestion-pipeline-and-agent-budget.md`](07-unified-ingestion-pipeline-and-agent-budget.md)、`plan.yaml` v3 和 `06-codex-execution-contract.md` 第 12 节覆盖。后续顺序为 P2 parser bake-off → P3-A 统一 engine → P3-B 131 条 backfill；不得再根据下文旧 P3-A 至 P3-E 自动创建逐 UID PR。

## 总原则

- 后续实现均基于本规划 PR 合入后的最新 work head；
- 一次只允许一个活跃实现 PR；
- 每个 PR 只做一个 phase 或一个 action bucket；
- 每个网络获取批次最多 10 个明确 UID；
- 每个 PR 在开始时固定 `base_sha`，在结束时报告准确的 `head_sha`；
- work 分支变化后，尚未开始的下一批必须从新 head 创建；
- 不并行修改同一 source UID、同一 manifest 或同一生成物集合。

上述“10 UID/批次”只保留为旧阶段记录；新实现以第 07 文档的内部 request chunk 和 PR 边界为准。

## P0 — 规划契约

**当前 PR。**

允许变更：

```text
docs/README.md
docs/plans/260916-corpus-completion-main-convergence/**
```

禁止变更：

```text
raw_data/**
source_registry/**
materialized_sources/**
experiments/**
pipeline/**
scripts/**
.github/workflows/**
```

验收：计划被审阅并合入 work；Issue #3/#4 保持 open。

---

## P1 — 建立 131 条非 repo 覆盖台账

### 目的

建立真实执行分母。该 PR 不联网、不下载、不删除、不修复正文，只从当前 repo 读取并分类。

### 唯一允许的主输出

```text
raw_data/audits/non_repo_materialization_coverage_2026-09-16.yaml
docs/plans/260916-corpus-completion-main-convergence/coverage-baseline.md
```

若需要可复算，允许添加一个小型只读审计脚本；但优先复用现有 manifest/index/registry 读取能力，不建立新的 materialization 框架。

### 台账必须恰好包含

- 131 个非 GitHub repository UID；
- 84 个 GitHub UID 必须明确排除并有排除计数；
- 每条包含：
  - target document identity 和 selected version；
  - source type；
  - manifest / local paths；
  - original artifact coverage；
  - text extraction coverage；
  - local persistence；
  - selector 状态；
  - public redistribution 状态；
  - knowledge admission 状态；
  - exact limitation；
  - `action_bucket`；
  - `next_action`。

### action bucket 受控枚举

```text
complete_verified
needs_boundary_verification
parser_only
canonical_repair
open_fulltext_fetch
author_manuscript_fetch
html_article_snapshot
standard_spec_fetch
ocr_assessment
access_restricted
public_persistence_decision
identity_or_version_ambiguous
```

### P1 验收

- 数量由 repo 实际复算，而不是复制 issue 文本；
- 90 个 `full_text` 条目逐项检查其目标文档边界；
- 27 个 excerpt、14 个 metadata-only、2 个已知解析问题全部出现在台账中；
- 错误页、目录页、摘要页、截断页和版本错配不会被归为 `complete_verified`；
- 无 source bytes 或生成物变化；
- PR body 明确说明“这是 inventory，不是正文补齐”。

---

## P2 — 修复两项已知解析不完整（历史设计，已由新 P2 bake-off 覆盖）

P2 必须在 P1 合入后创建，base 为当时最新 work head。

### P2.1 `arxiv:2406.04268`

目标：

- 从已保存 source 中识别真实 TeX root；
- 正确展开正文 include graph；
- 生成 normalized TeX/text；
- 重新生成真实可解析的 selectors；
- 更新 manifest、registry、index 与 P1 coverage ledger；
- 若该 source 属于当前 demo 选取范围，再重建受影响 demo/Wiki；否则不产生无关 Wiki diff。

不得：

- 将任意最大 `.tex` 文件当 root；
- 用 landing page 摘要替代 source body；
- 为修一篇论文改写所有 source adapter。

### P2.2 `arxiv:2502.18864`

目标：

- 确认原 PDF 版本和页数覆盖；
- 逐页核对文本提取；
- 检查第 4、20 页内容类型；
- 若是实质性图像文字，按 OCR 规则生成带 provenance 的 derived text；
- 若不需要 OCR 或无法可靠 OCR，明确保留 `text_extraction=partial` 及原因；
- 更新 selectors、manifest、registry、index 与 coverage ledger。

不得把“原 PDF 已完整保存”与“文本提取完整”合并成同一状态。

### P2 验收

- 两个 UID 各自有 before/after 状态；
- 原件 hash 不被无故改写；
- selectors 全部本地解析；
- OCR 如发生，原件与 OCR 层分开；
- 不触碰其他 129 个非 repo source 的正文。

> 新 P2 不再把这两个 UID 当作两个独立修复任务，而是把它们作为 TeX root、低文本页/OCR 等 failure class 的 benchmark 样本，与其它代表项共同选择 parser router 和 Document IR。

---

## P3 — 按 action bucket 补齐正文（历史设计，禁止据此继续拆 PR）

P3 使用串行短期 PR。每个批次满足：

- 基于最新 work head；
- 最多 10 个 UID；
- 只包含一个 source adapter family 和一个主要 action bucket；
- PR 标题包含批次编号和 bucket；
- PR body 列出全部 UID，禁止“等”或省略；
- 合入后才创建下一批。

上述批次规则仅描述已发生历史。新的 P3-A/P3-B 由第 07 文档定义：先建统一 engine，再全量 backfill；failure rows 不自动创建 PR。

推荐顺序：

P1 新发现的 `needs_boundary_verification` 先按单一 adapter 的只读边界核验批次处理；新增 `parser_only` / `ocr_assessment` 按 P2 的同类验收规则进入串行 P3 解析批次，不受“仅已知两项”限制。`identity_or_version_ambiguous` 必须先解决身份歧义再获取。每批仍最多 10 个 UID、一个主要 bucket，不能让未核验项在 P4 中消失。

### P3-A：canonical / version repair（历史）

先处理 `canonical_repair` 与 `identity_or_version_ambiguous`，因为错误身份会污染后续下载、hash 和 selectors。

允许的替代入口顺序：

```text
当前 canonical URL
→ 同一发布主体的正式永久 URL / DOI resolution
→ 同一版本的官方开放 PDF/HTML
→ 作者或机构公开稿
```

不得把相似标题、不同版本或二次转载静默当作同一原件。

### P3-B：开放论文与正式作者稿（历史）

处理 `open_fulltext_fetch`、`author_manuscript_fetch`：

- 优先官方 source/PDF；
- 固定版本；
- 保存原件和 normalized text；
- 记录所有 URL 与最终选择理由；
- 不递归抓引用、数据集或权重。

### P3-C：完整网页文章与行业文档（历史）

处理 `html_article_snapshot`：

- 提取正文而不是导航、推荐、cookie 或页脚；
- 证明 snapshot 覆盖目标文章，而不是标题页；
- 保留结构、发布日期、作者、canonical URL；
- 使用 block/heading selector，不把整个页面当一个匿名 chunk。

### P3-D：标准与规范（历史）

处理 `standard_spec_fetch`：

- 区分 specification body 与 landing/catalog page；
- 优先正式公开规范；
- 付费 ISO 等不得绕过访问限制；
- 无法公开取得正文时保留具体未决原因，不将目录页升级为全文。

### P3-E：访问或公开持久化未决（历史）

处理 `access_restricted`、`public_persistence_decision`：

- 记录实际合法尝试和失败证据；
- 不继续反复抓取已确认受限入口；
- 不将未确认可公开保存的 bytes 先提交再补手续；
- 对可获取但不能公开持久化的来源，提交具体的 storage/representation 决策请求，而不是改写为“技术失败”；
- 该项未解决不应阻塞其他 UID 的独立批次。

### 旧 P3 批次的文件责任

对批次 UID，仅修改必要的：

```text
raw_data/<source>/metadata.yaml              # 仅 canonical/version 修正时
materialized_sources/corpus/<capsule>/**
materialized_sources/index.yaml
source_registry/registry.yaml
source_registry/registry.jsonl
raw_data/audits/non_repo_materialization_coverage_2026-09-16.yaml
raw_data/audits/materialization_completeness_2026-09-10.yaml
```

如果选中 source 的 claim/evidence 输入发生变化，才允许重建：

```text
experiments/v0_meta_kb_initialization_demo_260910/**
```

生成器未受影响且 source 未进入 selected set 时，不得制造无关 Wiki churn。

---

## 新 P2/P3 执行摘要

```text
P2 parser bake-off
  - 明确代表性 UID
  - 比较候选 parser
  - 冻结 Document IR 与质量指标
  - 不做全量 backfill

P3-A unified ingestion engine
  - acquisition adapter
  - media classifier
  - parser router
  - native parser sidecar
  - canonical Document IR
  - provenance / coverage validator
  - failure ledger

P3-B full nonrepo backfill
  - 对全部 131 条运行冻结 engine
  - 网络 chunk 只是内部 checkpoint
  - 同类失败按 failure class 聚合
  - 默认一个 backfill PR，最多两个
  - 输入冻结后再做全局生成
```

详细预算、停止条件和验收见第 07 文档与第 06 文档第 12 节。

---

## P4 — 全量对账与 PR #1 收口

当统一 backfill 完成后，创建一个最终 reconciliation PR，base 仍为最新 work。

该 PR 只做：

1. 从 repo 重算 131 条覆盖结果；
2. 检查 excerpt/metadata/partial 是否全部有完成或未决结论；
3. 重新生成受影响的 manifest/index/registry/Wiki；
4. 修正 PR #1 与 docs 中的 Definition of Done；
5. 生成最终 branch/work-item ledger；
6. 给出拟进入 `main` 的精确文件树和未决事项；
7. 对现有 TeX/source 附带组件给出精确 retention proposal，但不未经授权删除或改写历史；
8. 对 failure ledger 给出按类别汇总，不要求每个 unresolved UID 再开 PR。

P4 不新增研究来源，也不开始新的许可调查主题。

---

## P5 — PR #1 最终集成与 `main` 复验

顺序固定为：

```text
P4 合入 work
→ 锁定 PR #1 final head SHA
→ 针对实际 main base 重新运行完整验证
→ 独立检查 source coverage 与生成物一致性
→ 更新 PR #1 最终说明
→ 获得明确 merge 决定
→ squash merge PR #1 到 main
→ 从 main 做全新 checkout
→ 重新运行结构、内容抽查和确定性验证
→ 记录 main commit 与验证结果
```

在 `main` 新 checkout 验证通过之前，不得关闭 Issue #4，不得声称远程交接完成。

分支清理不包含在 P5 默认动作中；需要单独授权。

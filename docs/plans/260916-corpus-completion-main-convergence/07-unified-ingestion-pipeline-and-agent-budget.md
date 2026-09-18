# 07 — 统一论文数据管线与 Agent 预算重置

> 状态：规划变更提案。它不修改任何 source、manifest、selector、Wiki 或公开许可判断；合入后约束后续 P2/P3 实现。

## 1. 为什么需要重置

当前执行已经证明，逐 UID、逐表示、逐许可包装的串行 PR 可以获得很强的可追溯性，但也产生了明显的局部最优：

1. 同一类 PDF、TeX 或 HTML 问题被拆成多个来源专属 PR；
2. 每个 PR 重复执行规划、获取、包装、全局生成、CI、独立 evaluator 和长篇状态同步；
3. `capsule / manifest / selector / deterministic replay` 的工程完备度持续提高，但正文统一解析能力没有以同等速度提高；
4. 原件获取、文本解析、公开持久化、知识准入和 Wiki 生成仍在同一执行循环中相互放大；
5. PR 数量、审计文字和 API 消耗可以增加，而 `complete_target_consumable`、失败类别收敛和可复用 parser 能力没有对应增长。

这不是单个 PDF-to-text bug。更准确的问题是：**缺少统一的 parser router、统一中间表示和面向失败类别的批处理机制，同时执行合同鼓励 Codex 对每个局部异常重新启动完整 PR 生命周期。**

## 2. 本次重置的目标

后续工作从“按来源修复”改为“按能力建设与全量回填”：

```text
来源登记
→ 原件获取与冻结
→ 媒体/来源分类
→ parser router
→ 统一 Document IR
→ 覆盖与质量验证
→ evidence / claim / Wiki 消费
```

统一发生在接口、状态和验证契约，不要求所有文档使用同一个 parser。

### 2.1 必须实现的统一对象

每次 parser run 至少产生：

```yaml
source_uid: <stable UID>
source_revision: <selected version or content hash>
artifact_sha256: <raw artifact hash>
media_type: <pdf|tex|html|xml|...>
parser:
  engine: <name>
  version: <exact version>
  config_hash: <deterministic config hash>
coverage:
  original_artifact_complete: <true|false|unknown>
  total_pages: <int|null>
  parsed_pages: <int|null>
  failed_pages: []
  ocr_pages: []
  text_state: <complete|partial|unavailable|unknown>
  structure_state: <complete|partial|unavailable|unknown>
document:
  title: <value|null>
  authors: []
  abstract: <block ref|null>
  sections: []
  blocks: []
  tables: []
  equations: []
  figures: []
  bibliography: []
warnings: []
errors: []
```

原 parser 输出必须作为 native sidecar 保留；统一 IR 是消费层，不替代原件或 native 输出。

## 3. Parser router

下一实现不得继续把 `pypdf` 文本作为全部论文的唯一正文层。必须先完成代表性 benchmark，再固定生产路由。

| 来源/表示 | 首选候选 | fallback | 说明 |
| --- | --- | --- | --- |
| arXiv TeX/source archive | LaTeXML | 保守 TeX reading view；再回退 PDF | 优先保留章节、公式、引用和 include graph，不先把 TeX 渲染成 PDF 再抽文本 |
| born-digital scholarly PDF | GROBID | Docling | GROBID 负责论文结构、作者、章节、引用和坐标；Docling用于版面、表格及困难文档补充 |
| 扫描或低文本覆盖 PDF | Docling OCR | 经 benchmark 批准的 MinerU | OCR 只作为派生层，逐页记录；不得把 OCR 冒充原生文本 |
| 普通文章/博客 HTML | Trafilatura | Docling HTML / 有界 DOM adapter | 去除导航、cookie、推荐和页脚，保留标题、作者、日期、heading/list/table |
| 标准/规范 HTML | 有界 DOM adapter + Docling/Trafilatura | 原 HTML + selector-only | 规范正文边界、状态、附录、表格和正文资产必须显式验证 |
| GitHub repository | 现有 commit-pinned semanticization | 独立 sandbox lane | 不进入本次 131 条非 repo 全文分母 |

候选工具是 benchmark 输入，不是未经测试的最终依赖承诺。依赖、许可证、资源占用和可重复性必须在 benchmark PR 中记录。

## 4. 新阶段划分

### P2 — Parser bake-off 与 Document IR 契约

只做代表性样本，不做全量 corpus 回填。PR body 必须列出明确 benchmark UID，覆盖至少：

- born-digital 单栏 PDF；
- 双栏 PDF；
- 表格/公式密集 PDF；
- 扫描或空 text-layer 页；
- 多文件 TeX；
- 普通 HTML；
- 标准/规范 HTML；
- 当前已知失败或 partial 的代表项。

同一原件至少比较两个合理候选，输出统一评估表。评估必须包括：

- 原件和页数覆盖；
- 章节层级；
- 阅读顺序；
- 公式、表格、caption 和 bibliography；
- citation/ref linking；
- OCR 页记录；
- block/page/bbox provenance；
- 运行时间、峰值资源、失败模式；
- 确定性与重复运行结果。

P2 的成功是选定路由和 IR，不是把 benchmark UID 各自包装成新的长期特例。

### P3-A — 统一 ingestion engine

只实现通用能力：

- acquisition adapter 与 immutable raw artifact；
- media classifier；
- parser router；
- parser-run manifest；
- canonical Document IR；
- native sidecar；
- coverage validator；
- failure ledger；
- deterministic replay；
- 迁移现有 selector 到 block/page/bbox provenance 的兼容层。

禁止在 production code 中为单个 UID、题名、DOI 或 host 添加仅为通过一个 fixture 的分支。来源差异优先表达为 metadata/config；只有可复用的 source family 行为才进入 adapter。

### P3-B — 131 条非 repo 全量 backfill

使用冻结后的 P3-A engine 对全部 131 条运行。网络请求可以按小 chunk 限流、重试和记录，但 **chunk 不是 PR 边界**。默认只开一个 backfill PR；只有 GitHub 文件大小、明确法律隔离或不同存储决策使一个 PR 技术上不可审阅时，才允许拆为最多两个 backfill PR，并在拆分前写明边界。

每个失败来源进入 failure ledger：

```yaml
uid: <UID>
stage: acquisition | classification | parsing | validation | persistence
failure_class: <controlled value>
parser: <engine/version|null>
retryable: <bool>
next_action: <generic fix or explicit unresolved decision>
```

失败记录不是新 PR 的自动触发器。只有某个失败类别需要通用 engine 修复时，才开修复 PR；修复后对所有同类来源回放。

### P4 / P5

沿用全量对账、PR #1 收口、`main` 合入与 fresh checkout 复验，但 P4 不再接受“还有一批逐 UID PR 未做完”的开放式状态。它只接收：

- 已统一 backfill 的成功结果；
- 显式 failure ledger；
- 需要人工决定的访问/公开持久化边界；
- 已冻结的 parser/IR 版本。

## 5. Agent 行为与预算合同

### 5.1 可衡量增量

每一轮 planner → executor → evaluator 必须至少改善一项：

- `original_artifact_complete` 数量；
- `text_state=complete/partial` 的已验证覆盖；
- failure class 数量或受影响 UID 数量；
- parser family 的通用测试覆盖；
- Document IR schema/validator 的真实能力；
- 未决人工决策数量。

只增加审计文字、重复测试记录、PR 历史叙述或相同结果的另一份 sidecar，不算进展。

### 5.2 硬性预算

- 同一 PR 最多两次“实现失败 → 修复 → 独立复审”循环；第三次仍有 blocker，停止并提交最小 blocker，不继续自动消耗。
- HEAD 未变化时，不重复请求 evaluator，不重复运行同一远端 CI，不把同一结果重新写入 PR body。
- 连续两次 agent 迭代没有改善上述任一增量指标时，必须停止。
- parser/engine PR 不重建整个 Wiki，除非 selected source 的实际语义输入改变；默认只跑 parser、IR、coverage 和最小集成测试。
- backfill PR 在输入冻结前不得反复全量生成；全局 index/registry/Wiki 只在最终冻结后串行重建一次，失败修复后至多再重建一次。
- 不为单个 UID 新建 PR，除非涉及作品身份冲突、访问控制、独立法律决策或无法与同类来源共同审阅的破坏性迁移。
- PR body 保留当前状态、关键决策、验证和未决；逐命令历史放入阶段报告，禁止无限累积“当前状态”副本。

这些限制不是牺牲质量，而是防止验证和叙述成为替代真实数据进展的代理指标。

### 5.3 每个实现 PR 必报的效率字段

```yaml
execution_efficiency:
  agent_iterations: <int>
  repair_cycles: <int>
  source_rows_touched: <int>
  parser_families_changed: []
  coverage_before: {}
  coverage_after: {}
  failure_classes_before: {}
  failure_classes_after: {}
  full_regenerations: <int>
  repeated_ci_on_same_head: 0
  repeated_evaluation_on_same_head: 0
```

无法直接获得 API credit 精确值时，不得猜测；以上字段作为可审计代理。

## 6. 验收标准

### 6.1 Engine / benchmark

- 所有 benchmark 原件逐字节保留并有 hash；
- 每次 parser run 有 engine version/config hash；
- 统一 IR 100% schema-valid；
- parser 失败没有静默回退或被写成 complete；
- 原生文本、OCR、collector-derived text 可区分；
- 同一冻结输入重复运行得到相同 IR 或明确列出允许变化字段；
- benchmark 报告基于内容检查，不以进程退出码或非空文本作为质量结论。

### 6.2 Backfill

- 131 条恰好各有一个当前 acquisition/parsing 结果或显式 unresolved；
- 所有成功来源可从原件追踪到 native output、Document IR 和 selector/provenance；
- 同类失败聚合到 failure class，不制造 UID 专属代码；
- coverage ledger 从实际 parser-run manifest 复算；
- 公开再分发和知识准入继续独立记录，不阻塞本地私有/受限处理状态的诚实表达；
- 未经许可的新增全文不得进入公开树。

## 7. 与现有仓库的兼容

现有 capsule、manifest、rights audit 和 deterministic Wiki 不删除。迁移采用并行层：

```text
raw artifact                  # 现有/新增原件
native parser output          # TEI/XML/Docling JSON/LaTeXML output/...
document_ir.json              # 新统一消费层
selectors/provenance          # 兼容现有 evidence consumer
legacy normalized document    # 迁移期保留，直到对账批准
```

不在本计划 PR 中删除旧 normalized 文本、改写历史或迁移存储。P4 再决定哪些 legacy 表示可以降级为历史层。

## 8. 对 Codex 行为模式的判断

当前 Codex 的问题不是“不会处理 PDF”，而是执行环境给了错误的局部奖励：

- 每个小 PR 都能通过严密 CI 和 evaluator；
- 每个来源都可以通过增加包装和审计获得局部完成感；
- 没有要求共享 parser capability 或 failure-class 收敛；
- 没有无进展停止条件和有限修复循环；
- 大量派生重建与状态同步会消耗上下文，却不一定改善正文覆盖。

因此后续合同必须奖励：**通用修复、批量复用、真实 coverage delta、失败类别减少和最终 `main` 收敛**；不得再奖励 PR 数量、审计长度或重复绿灯。

# 02 — Scope 与状态契约

本文件是正文物化工作的产品范围定义。执行者不得根据抓取器偶然下载到的内容反向扩大需求。

## 1. In scope

### 1.1 来源范围

以 Phase 1 从当前 repo 重新计算出的 **131 条非 GitHub repository 来源**为准，包括现有 collection 中的：

- arXiv / bioRxiv；
- journal / paper；
- blog / industry documentation；
- methodology；
- standard / specification。

每条记录只处理该 UID 所代表的目标文档与选定版本。

### 1.2 每条来源的目标产物

在合法且技术可行时，每条来源应具有：

```text
canonical source identity + selected version
original artifact or complete canonical snapshot
normalized, agent-consumable text
stable local file inventory and hashes
resolvable selectors
manifest / registry / index consistency
coverage and limitation record
```

“agent-consumable text”不要求所有来源使用同一种格式：

- TeX 来源：保留目标正文 TeX 和按 include 关系展开／规范化的文本；
- PDF：保留原始 PDF，并生成带页码边界的文本；
- HTML article/spec：保留完整正文快照及结构化文本；
- GitHub repository：不在本计划中作为正文抓取，继续使用 commit-pinned semantic capsule。

## 2. Out of scope

除非它本身已经是 collection 中的独立 source UID，否则本计划不做：

- 递归收集论文引用的全部作品；
- 下载外链数据集、模型权重、benchmark 数据或实验环境；
- 把整站、整个域名或作者全部文章镜像进 repo；
- 因 TeX source bundle 中偶然出现模板、旧稿、匿名评审、示例或第三方摘要，就自动把它们定义为用户要求的正文；
- 扩展研究 collection 的主题范围；
- 执行 GitHub repository 代码、安装依赖或验证 benchmark；
- 将 candidate claim 晋升为 trusted；
- 为了通过计数而绕过登录、付费墙、robots、访问控制或站点限制。

## 3. 目标文档边界

Phase 1 必须为每条非 repo 来源填写 `target_document`：

```yaml
target_document:
  title: ...
  canonical_id: ...
  selected_version: ...
  source_kind: tex | pdf | html | specification | other
  boundary: 一句话说明什么属于该文档正文
```

### 3.1 TeX source bundle 分类

TeX 包中的文件必须分类，而不是全部默认为“论文全文”：

| 类别 | 定义 | 是否为正文完成必需 |
| --- | --- | --- |
| `target_body` | root TeX、被 root 引用的章节、正文表格和正文附录 | 是 |
| `citation_support` | 正文引用结构所需的 `.bib`/`.bbl` 等 | 通常保留，但不作为正文覆盖的独立页数 |
| `figure_or_table_asset` | 正文明确引用的图表资产 | 原件覆盖需要；纯文本消费可记录不可提取部分 |
| `layout_dependency` | `.sty`、`.cls`、`.bst`、字体和排版模板 | 编译可能需要，但**不是正文获取完成条件** |
| `embedded_third_party_content` | 第三方摘要、评审、示例页面等 | 仅在目标文档明确包含且允许保留时纳入 |
| `historical_or_auxiliary` | 旧稿、备份、demo、构建残留 | 默认不属于目标正文 |

对现有内容的删除、迁移或历史改写不由本分类自动触发；先提交精确差异方案再请求确认。

## 4. 六个正交状态维度

每条来源必须分别记录以下维度，禁止压缩成单一 `materialized=true/false`：

### 4.1 Identity

```text
target UID
canonical identifier
selected version/revision
canonical URL and permitted alternates
```

### 4.2 Original artifact coverage

允许值：

- `unknown`：已有材料或标签，但目标边界／版本尚未核验，不能据此断言完整或缺失；
- `complete`：本地原件覆盖目标文档全部边界；
- `partial`：原件只覆盖部分正文；
- `unavailable`：没有取得原件；
- `metadata_only`：只有身份和目录信息；
- `not_applicable`：原生结构化数据不需要独立 binary 原件。

### 4.3 Text extraction coverage

允许值：

- `unknown`：尚未核验提取结果与目标正文边界的一致性；
- `complete`：所有实质性正文均有可消费文本；
- `partial`：有明确缺页、缺章节、图片文字或解析失败；
- `unavailable`：没有正文文本；
- `not_applicable`：来源本身已是可消费文本。

必须单独列出 `missing_pages`、`missing_sections`、`parser_errors` 和 `ocr_state`。

两个 coverage 维度均须附 `evidence`（repo 路径、页／行／章节及检查结果）与 `verification_state`（`unverified` / `partial_check` / `verified`）。`unknown` 不是失败或不存在，`partial` 必须有具体缺口证据。缺失列表为空但未核验时，不能解释为“无缺失”。现有标签只记录为 `reported_content_tier`，不得直接转换为 `complete`。版本无法由已有记录固定时记录 `selected_version: null` 和具体原因，不编造版本；按身份／版本核验 bucket 后续处理。

`unknown` 必须附具体原因和 `next_action`，不得计入完成数；`complete` 必须同时有已核验的目标边界、选定版本和实际内容证据。

### 4.4 Local persistence

分别记录：

- 原件是否入 repo；
- normalized text 是否入 repo；
- manifest/hash 是否存在；
- selector 是否解析；
- 远程 clone 后是否无需本机缓存即可消费。

### 4.5 Public redistribution

允许值：

- `allow`；
- `allow_with_conditions`；
- `block`；
- `unknown`；
- `not_applicable`。

该状态只决定哪些内容可以保留在公开 Git 树中。它**不等于**获取或解析状态。

### 4.6 Knowledge admission

允许值沿用现有模型：

```text
candidate → review → trusted / rejected / superseded / retracted
```

正文物化完成不会自动改变 claim 的 admission state。

## 5. 完成定义

### 5.1 “原件已获取”

只有在以下条件全部满足时才成立：

- selected version 已固定；
- 本地原件或完整 canonical snapshot 覆盖目标文档边界；
- 文件 hash 与来源 provenance 已记录；
- 原件不是错误页、登录页、摘要页、目录页或截断响应。

### 5.2 “文本预处理已完成”

只有在以下条件全部满足时才成立：

- root／正文结构正确识别；
- normalized text 与原件边界一致；
- 页码／章节／行范围可定位；
- 所有已知缺失明确记录；
- selectors 可在本地解析并命中对应 evidence；
- 未把 parser 输出或 OCR 推测冒充原文。

### 5.3 “来源可在 repo 中消费”

只有在以下条件全部满足时才成立：

- 允许公开保留的必要原件和文本已提交；
- manifest、registry、index 和 selectors 一致；
- 新 checkout 可以仅依赖 repo 文件读取；
- 内容覆盖状态不是由 `content_tier` 标签单独推断。

### 5.4 无法完成的来源

若由于付费墙、登录、404、访问控制、公开再分发限制或技术失败而无法完成：

- 不得伪造正文；
- 不得静默降级为“完成”；
- 必须记录实际尝试的 URL、时间、响应／错误、合法替代入口和下一步；
- 只阻塞该 UID，不阻止其他独立来源继续执行；
- 由最终 coverage ledger 将其标为 `unresolved`。

## 6. OCR 规则

OCR 是最后手段，不是默认步骤。

1. 先确认原始 PDF 页面确实是图像页或文本层不可用；
2. 判断该页是否包含目标正文的实质性文字，而不是纯图形／装饰；
3. 只有实质性文本缺失时才进入 OCR 子任务；
4. OCR 输出必须单独标为 derived text，并记录工具、版本、语言、页码和质量限制；
5. 原 PDF 始终是原件，OCR 文本不能替代或改写原件；
6. 无法可靠 OCR 时保留 `text_extraction=partial`，不得猜测。

对 `arxiv:2502.18864`，Phase 2 先检查第 4、20 页是否含必须恢复的实质性文字，再按上述规则决定是否 OCR。

## 7. 计数规则

后续所有报告必须同时给出：

```text
non_repo_total
original_artifact_complete / partial / unavailable / metadata_only / not_applicable / unknown
text_extraction_complete / partial / unavailable / not_applicable / unknown
locally_persisted_complete
public_redistribution_allow / conditional / block / unknown
knowledge_candidate / trusted
```

禁止再使用下列单一计数表示“物化完成”：

- capsule 数量；
- `full_text` 标签数量；
- rights allow/block 数量；
- selector 数量；
- Wiki 页面数量；
- trusted claim 数量。

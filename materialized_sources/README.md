# 物化来源语料（Materialized Source Corpus）

`corpus/` 为每条 metadata record 保存一个本地胶囊（local capsule）。内容层级（content tier）包括：

- `full_text`：技术上已取得本地全文；该层级本身不证明具备公开再分发许可；
- `semantic_capsule`：GitHub repository 已固定到具体 commit，并根据选定证据生成语义胶囊；
- `excerpt_capsule`：未确认再分发权利时，只保存有边界的本地摘录；
- `metadata_capsule`：仅允许元数据消费；也可能保留抓取失败的标题等诊断性文件，不能作为正文证据。

本地胶囊不自动等于可信知识（trusted knowledge）。

公开存储另受[版权与许可审计](../docs/materialization-rights-audit.md)约束。`full_text_redistribution_assumed` 是历史获取器的假设，不是许可凭据；Git LFS 或公开 release artifact 也不消除再分发义务。摘录有长度边界也不自动代表具备公开再分发权。

离线修复和定位器抽检结果见 `raw_data/audits/`。注册表的 `evidence_role` 将仅目录导航（catalog-only）、有限摘录（bounded-excerpt）、仓库静态证据（static-repository-evidence）与原文（source-text）分开。

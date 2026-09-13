# 物化来源语料（Materialized Source Corpus）

`corpus/` 为每条 metadata record 保存一个本地胶囊（local capsule）。内容层级（content tier）包括：

- `full_text`：已物化开放或来源原生的全文；
- `semantic_capsule`：GitHub repository 已固定到具体 commit，并根据选定证据生成语义胶囊；
- `excerpt_capsule`：未确认再分发权利时，只保存有边界的本地摘录；
- `metadata_capsule`：本地仅保存 metadata 与获取诊断。

本地胶囊不自动等于可信知识（trusted knowledge）。

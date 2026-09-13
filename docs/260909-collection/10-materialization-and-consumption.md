# 来源物化与消费（Materialization and Consumption）

## 目标与不变量

来源记录存在，不代表消费者能够直接使用。论文、repository、标准、网页和受限出版物具有不同的版本语义、证据定位方式、权利边界与失败模式。本层保证：

1. 每条 `raw_data/**/metadata.yaml` 都对应一个本地胶囊（local capsule）；
2. 每个胶囊都记录来源身份、获取状态、本地文件、hash 和降级诊断；
3. 可消费内容具有可解析的证据定位器（evidence selector）；
4. 无法合法或技术性取得全文时，显式降级为摘录或 metadata，不伪装成全文；
5. 物化成功不等于知识已可信（trusted）。

当前分层为：

```text
raw_data/                         来源 metadata 与 provenance
source_registry/                  统一身份、adapter 与物化状态
materialized_sources/corpus/      每条记录一个来源专属胶囊
experiments/v0_meta_kb_.../       从本地胶囊构建的候选知识 demo
```

权威机器入口是 `materialized_sources/index.yaml` 和 `source_registry/registry.yaml`。

## 内容层级（Content Tiers）

| 层级 | 含义 | 可用于什么 |
|---|---|---|
| `full_text` | 开放或来源原生的完整文本已保存在本地 | 结构解析、claim/evidence 抽取 |
| `semantic_capsule` | repository 固定到 commit，并保存预算内的高价值证据文件 | 架构、接口与实现线索分析 |
| `excerpt_capsule` | 因权利或访问约束只保存有边界摘录 | 有限证据与来源发现 |
| `metadata_capsule` | 只保存 metadata 与获取诊断 | 身份、缺口与后续补采计划 |

`partial` 表示胶囊可用但某一步不完整，例如 TeX root detection 失败或只允许保存摘录；它不等于记录缺失。

## arXiv adapter

arXiv 优先获取 source archive，而不是把 PDF 粗略切块：

```text
arXiv ID → source archive → archive hash → 安全解包
→ TeX/include 结构 → normalized document → file/line selectors
```

胶囊保存文本型 source files、文件清单、normalized document 和 selectors。图片等二进制成员不会在文本优先通道中盲目复制，但其省略状态会被记录。

## GitHub adapter

Repository 是可变软件系统，不是线性文档。GitHub adapter 会：

1. 固定默认分支的 commit；
2. 在预算内选择 README、架构文档、接口文档、依赖与构建配置等高价值文件；
3. 将选中证据保存到本地；
4. 生成 commit-pinned file/line selectors；
5. 生成候选 mini-wiki，但不执行第三方代码，也不把 README 声明自动当成实现事实。

正常路径使用 GitHub API 获取 repository tree 和 blob。API token 缺失、失效或触发限额时，adapter 使用 `git ls-remote` 固定 commit，再从 `raw.githubusercontent.com` 探测一组明确的高价值路径。fallback 会标记 `tree_truncated: true`，不会冒充完整 tree inventory。

## 通用文档与网页 adapter

Journal、blog、methodology、standard 等来源按以下顺序处理：

- 根据 canonical URL 和 metadata 构造候选 URL；
- 记录 resolved URL、content type、bytes 与 hash；
- 对开放内容保存全文；
- 未确认再分发权利时只保存 bounded excerpt；
- 全部候选失败时保存 metadata capsule 与错误诊断。

## 运行与增量重建

```bash
make materialize
make validate
```

`make materialize` 执行全量物化、构建 v0 demo，并运行所有验证。也可以分别执行：

```bash
make materialize-all
make build-demo
make validate-materialized
```

单一来源类型可增量重建。例如 GitHub API 状态变化后，只重建 repository 胶囊：

```bash
python scripts/materialize_all_sources.py \
  --config pipeline/materialization_all_260910.yaml \
  --only-source-type github
```

增量模式要求其他记录已经存在本地 manifest；完成后仍会统一重建 registry、index 和 completeness audit。

## 2026-09-14 验收快照

- metadata records：215；
- local manifests：215；
- `full_text`：91；
- `semantic_capsule`：80；
- `excerpt_capsule`：27；
- `metadata_capsule`：17；
- hashed files：2,820；
- selectors：24,841；
- materialization validation errors：0。

`raw_data/audits/materialization_completeness_2026-09-10.yaml` 保存完整审计，实际权威计数仍以最新 `materialized_sources/index.yaml` 为准。

## 信任边界（Trust Boundary）

验证通过只证明本地胶囊、hash、selector、registry 和 index 结构一致。它不证明论文结论已复现、repository 能运行、网页声明为真，或候选 wiki 已获准发布。后续知识层仍必须执行 claim-level evidence binding、冲突检查、风险评审与可回滚准入。

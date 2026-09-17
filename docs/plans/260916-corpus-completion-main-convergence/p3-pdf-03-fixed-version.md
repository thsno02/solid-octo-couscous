---
phase: P3-PDF-03
status: local_validation_passed_exact_pair_review_and_ci_pending
base_sha: 512794e2386898aaaac67a8268cc61e0fe8cb594
base_dependency: PR18_merged_at_512794e
adapter_family: arxiv_latex_v2
action_bucket: open_fulltext_fetch
source_uids:
  - arxiv-1606.04671
  - arxiv:2404.16130
  - arxiv:2505.22954
coverage_summary:
  collection_records: 215
  non_repo_total: 131
  github_repo_excluded: 84
  reported_content_tier_counts:
    excerpt_capsule: 26
    full_text: 93
    metadata_capsule: 12
  source_type_counts:
    arxiv: 73
    biorxiv: 2
    blog: 10
    industry: 2
    journal: 11
    methodology: 7
    paper: 2
    standard: 24
  original_artifact_counts:
    complete: 33
    metadata_only: 14
    partial: 6
    unknown: 78
  text_extraction_counts:
    complete: 6
    partial: 46
    unavailable: 14
    unknown: 65
  action_bucket_counts:
    access_restricted: 7
    author_manuscript_fetch: 2
    canonical_repair: 5
    complete_verified: 6
    html_article_snapshot: 14
    identity_or_version_ambiguous: 2
    needs_boundary_verification: 65
    ocr_assessment: 19
    parser_only: 6
    public_persistence_decision: 3
    standard_spec_fetch: 2
  public_redistribution_counts:
    allow: 29
    block: 65
    unknown: 37
  content_inspected_full_text: 43
  structure_only_full_text: 50
  locally_persisted_complete: 6
  knowledge_candidate_sources: 30
  knowledge_trusted_sources: 0
  knowledge_sources_without_demo_claims: 101
  unresolved_sources: 125
---

# P3-PDF-03 — 三篇同版本官方 PDF 补充

当前状态：PR #19 已发布，三份固定 PDF 已实际取得、完成有界内容审核并包装保存；严格离线重放、183测试、demo/Wiki、稳定树验证及默认coverage audit均通过。三篇编译原件覆盖完整，但原生文本均有具体损失，保持 partial。下列启动合同与第7节取得时状态保留为历史，不代表仍未 GET；精确提交的独立三维终审、CI、merge 与 main 交接尚未完成。

本批启动于最新 work `512794e2386898aaaac67a8268cc61e0fe8cb594`。PR #18 已正常 Ready／merge，HEAD `28f0e595aa262461787f63a3686a6187882de226` / BASE `463b848b0b4abef33df6fa51f6fcf9bd7482a922` 获独立三维 PASS（COMMENT 5229547026）及 CI 35163384395 成功。父 PR #1 仍 Draft，以该 work 为 head、main `99ce4670be91637209d67792de0962404fa96488` 为 base，未进入 main。

启动时，主线已完整读取最新 Issue #3/#4、README、02/03/04、05/06、plan.yaml 与 ledger，复核上一批已合入及无其他 active writer，并接受 planner 的三 UID 有界草案。当时只有启动报告和分支台账修改，无源 GET、正文改动、代码/测试/workflow修改或生成重建；发布启动合同 PR 后才获取三份明确 PDF。当时没有提前宣称新正文完整或许可准入。

## 1. 推荐与范围

采用已有 PDF supplement，一次三 UID、一个 adapter family、一个主要 bucket。目的为持久化同一已选版本的完整编译表示，补齐已实证科学图形／书目／算法阅读缺口；不继续扩写 TeX 解释器，不逐组件重审历史，不获取整个 source archive、外链数据／代码／权重，不默认 OCR。

新原件与派生层统一为各 capsule 的 `pdf-supplement/document.pdf`、`document.txt`、`selectors.jsonl`、`NOTICE.md`。原 PDF 按真实响应 bytes 保存；原生提取采用现有 `plain` 模式。取得 PDF 不代表文字无损，旧 archive 中省略成员也不会因此变成已逐件恢复：可在新 PDF 表示证明完整编译作品，在旧 source 表示继续保留缺图历史。

## 2. 身份、现证据与 before

| UID／作品 | canonical metadata | capsule | 固定版本／唯一正文 GET 目标 |
| --- | --- | --- | --- |
| `arxiv-1606.04671`／Progressive Neural Networks | `raw_data/arxiv/Progressive Neural Networks/metadata.yaml` | `materialized_sources/corpus/arxiv-1606.04671--2b4672cf` | v4／`https://arxiv.org/pdf/1606.04671v4` |
| `arxiv:2404.16130`／From Local to Global: A Graph RAG Approach to Query-Focused Summarization | `raw_data/arxiv/From Local to Global: A Graph RAG Approach to Query-Focused Summarization/metadata.yaml` | `materialized_sources/corpus/arxiv-2404.16130--fe9ed9e5` | v2／`https://arxiv.org/pdf/2404.16130v2` |
| `arxiv:2505.22954`／Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents | `raw_data/arxiv/Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents/metadata.yaml` | `materialized_sources/corpus/arxiv-2505.22954--8a7041cb` | v3／`https://arxiv.org/pdf/2505.22954v3` |

官方身份／许可预核入口分别为上述 ID 的 `https://arxiv.org/abs/<ID>vN`；canonical 现有 `versioning.source_version`、`source_archive_url`、`pdf_url` 均已固定。三旧 manifest 的根 `source_version` 键实际缺省，读取结果为 null，并非显式写入 null；保留缺省，不得填成虚构旧响应或否定现有版本证据。新增 supplement 使用独立 `source_version`。

| UID | 当前 root revision | retained source | 当前 root selectors | coverage 当前记录／已完成 P4 观察 |
| --- | --- | --- | ---: | --- |
| PNN | `sha256:a4914f9b9e6d1652a5f6de990179705cf357621ee5a089d8bd6ca728c3b192ec` | 20 files／76,305 bytes | 41 | original partial；text unknown。观察已证 TXT partial：跨列求和及 `max` 算子损失，49 个不同实引图（21 `figures/*`、28 `figures/app_plots/**`）；130 是原已省略成员，不能统称非文本或全部必需图。 |
| GraphRAG | `sha256:aab5aeef01f6e03ef402c28fcea0c3041337c201af216c1e41f825c59ae7c628` | 19 files／160,932 bytes | 103 | original/text partial；14 import 已展开、七附录节在，`Level0Multihop.jpg`／`Level1Multihop.jpg` 仍缺，已存 `graph_rag.bbl` 未内联。103 包含旧 61 与 PR8 增加的 42，不得退回旧计数。 |
| DGM | `sha256:9ce27273d9175badbb14d1181bc6166c7afd5e7989ac274d3d5187413e19b9ed` | 34 files／390,140 bytes | 77 | original partial；text unknown。观察已证 TXT partial：For／If／赋值／并集／Return 控制关系损失；main 明确引用 10 个被省略科学 PDF 图（含 conceptual、进展／比较／transfer／消融／hallucination）。 |

三项当前 `action_bucket=needs_boundary_verification`、`resolution=unresolved`；selectors 结构 resolved，但 ledger 语义核验 false。旧 root public gate 均 allow 且 current review revision matches；knowledge 为 PNN=null、GraphRAG=null、DGM=candidate（现有 2 claims），不改变 trusted。以上是启动前继承事实，不是本批新公开准入或全文 PASS。PR18 合并后须再读三项，保留不相关 UID 的最新状态。

有界缺口证据：

- PNN：`source/infinite_pong.tex:21` 实引 `figures/transfer_pong.pdf`；`source/progressive.tex:27`／`:33` 为求和／max；`normalized/document.txt:823` 至论文尾 Labyrinth，`:847` 起旧 NOTICE。`/tmp/llm-wiki-p4-observations-X83KZi/arxiv-a.md:13` 已含完整观察，不重做 source inventory。
- GraphRAG：`source/communities_figure.tex:4`／`:5` 为两张社区图；`source/graph_rag.tex:459` 至 `:469` 包含书目／appendix／end；`normalized/document.tex:1687` 结尾。`arxiv-d.md:21` 记录当前展开结果。
- DGM：`source/main.tex:152,238,244,255,256,274,348,355,365,720` 为十图；`:523` 至 `:542` 算法源仍在，但 `normalized/document.txt:646` 至 `:658` 丢控制关系；`:3633` 至 `:3658` 为末尾 safety／future work，`:3660` 起旧 NOTICE。`arxiv-f.md:21` 为已完成观察。

## 3. 许可与公开持久化（public persistence）

三 canonical 均记 `rights.license_spdx=CC-BY-4.0`、license URL `https://creativecommons.org/licenses/by/4.0/`、verified 2026-09-16；固定 abs 页面与 archive payload 已有对应证据。seq1／39／64 当前 machine audit 均 `documented_permission`、旧文字包 allow。新同版本 PDF 可沿已有作品级许可审核，不需要另索作者函，但**旧包只覆盖 retained TeX 文字，不能直接移植其 allow、scope、revision 或取到即公开**。

执行期先在非公开暂存核实际固定 PDF、作品身份、作者、版本边栏／许可链接与可见素材信用，再建立本表示决定；有具体反向声明或扩大引用范围才停止该 UID 的公开持久化，不开启无限第三方历史考古。许可资料预核允许有限官方 abs／license 页查询，不能由此获取其他正文。

- PNN：八作者完整署名；前三位 Andrei A. Rusu、Neil C. Rabinowitz、Guillaume Desjardins 等贡献，不称八位全等贡献。新 PDF 的图注／素材信用实际待核。旧 STY 当前 NeurIPS 授权表达与差异包装原样保留，不重开 2016 历史许可，也不把模板 credit 归给论文作者。
- GraphRAG：十作者完整署名。AFaCTA 短引独立 ACL BY4 与六作者归属保留（`https://aclanthology.org/2024.acl-long.104/`）；约 59-word Fed 新闻段是已记录的有限研究引用情境，不属于论文 BY4 再许可或新闻库权利。新 PDF 只核其引用量／演示用途／可见信用是否仍与当前决定对应；若新增相反声明或显著扩大新闻表达，需本表示具体决定，不取 MortCap／新闻原件。本轮不伪称最初报道作者、非商业使用已核实或合理使用自动豁免。
- DGM：五作者完整署名；新 PDF 内主文／参考文献／附录代码、提示词、diff 和图的作品范围与可见独立声明实际待核，不下载或运行外链 agent 仓库。旧 LPPL／natbib 源代码陪同与 ICLR 适配 package 继续有效但原样保留，不把 LPPL 当 PDF 主文许可，也不重复源码历史追索。

每篇新增 `rights.pdf_supplement`，与 capsule snapshot、`manifest.pdf_supplement.rights`、machine audit 本 UID 的 `pdf_supplement` **四方一致**。包含 license／verified date、独立 `publication_gate` 与完整六字段 package：实际 PDF `source_revision`、固定 **PDF URL** `source_version_url`、`notice_path`、完整 attribution、真实 modifications、精确 scope；`approved_scope` 必须与 scope 一致。默认复用完整 `raw_data/licenses/cc-by-4.0.md`，必要可建立仅本三表示的累积 notice 资产，不改已有共享法条。新 scope 只含实际取得 PDF、页级 TXT／selectors；字节／页数待响应后填写，不编造。原 PDF 不编辑；派生 TXT 保留原生空白、明确页边界、追加唯一末注与 NOTICE 链接。

## 4. 零代码复用与消费（consumer）

现有能力已覆盖全部三 UID，无技术接口缺口需要预先增长框架：

- `scripts/materialize_all_sources.py:2975` 构造 fixed vN PDF URL；`:2984` 同时校验 canonical 与 snapshot 版本；`:3128` `build_pdf_supplement` 只生成新 PDF TXT／页 selectors，不重建 legacy capsule；`:3194` 离线 replay。
- `scripts/validate_publication_rights.py:31` 独立 PDF grant／四方包／真实 PDF revision 与 URL／NOTICE／末注验证。
- `scripts/validate_materialization_completeness.py:388` 保持父论文 Page 1 摘录边界；已有完整 PDF 页／定位器验证。
- `scripts/audit_non_repo_coverage.py:161` 已观测并验证 supplement；`build_demo.py:192` 只在新表示 public allow、完整性与 `body_quality_verified=true` 时选择 PDF，`:218`／`:225` 成对切换 PDF selectors／TXT。

默认 **生产代码、tests、依赖、workflow 零改**，通过现有 API 生成和现有测试验证。若实际响应出现本合同外技术缺口，先修订合同；不换版本、不改 PDF 内容、不降低 validator 来达成绿灯。

三项只有 DGM 当前在 36 selected demo 来源中。DGM 的新父论文 Page 1 摘录须人工核对其摘要、连续行范围、页定位、PDF revision 和 rights chain；必要用现有 `primary_excerpt` 精确连续 Page 1 范围，不扩大到嵌入他作摘要。只重建既有 DGM source／excerpt／evidence／claim 的表示绑定与受影响 Wiki，不新增 claims、collector assessment 或 trusted。PNN／GraphRAG 不新增 demo 选入。但整个 `materialized_sources/index.yaml` 是 build ID 输入（`build_demo.py:533`），三项 local_bytes／inventory 更新仍须 registry、snapshot、release 与 Wiki 必要全局 identity 同步；不能以未 selected 为由交付 stale release。

## 5. 发布前最小验收与串行写入

1. 唯一主 writer 管 canonical／capsule／audit／coverage／registry／生成物；其他 agent 可并行只读三份暂存 PDF 的内容、信用和旧文件保留，不能各自写全局 ledger。
2. 实际只获取本三 fixed PDF；逐项记录 request／resolved URL、响应 type/status/bytes、真实时间与失败。不回退 latest 或正式出版另一版本，不猜页数。失败仅阻塞当前 UID，保留真实 next action。
3. 每篇 PDF 首中末至少三页文本＋必要视觉核验、实际总页数、主文／书目／附录结束、科学图映射与可见 credit。PNN 的 49 个实引图、GraphRAG 两社区图、DGM 十图须核它们是否实际编译进同版 PDF；不把引用数量当 PDF 图编号，不为 omitted 的每个文件制造义务。
4. TXT 按原生页证据记录图内文字、数学、算法／表格／顺序损失；检查提取失败页、空文字页是否有实质内容。首中末页 selector 的 preview 与语义均须实际对应。图视觉可读、原 PDF 完整不要求 OCR 全绿；不能把 header-only 或 parser 无报错当完整 body。
5. 新 public grant 审核闭合后才公开持久化；检查完整 NOTICE、唯一末注、四方包一致。`body_quality_verified` 仅代表本文读取质量核验，不自动使 text complete 或 trusted。
6. 逐件保留旧 73 source files（627,377 bytes）、`files.jsonl`、normalized TeX／TXT（包括旧 NOTICE）、221 root selectors、旧 root NOTICE 字节；旧 manifest 的 root revision、source_version 键缺省、retrieval、rights、materialization 与 selectors 原值保留，仅追加 supplement、必要库存／大小。旧 snapshot 与 canonical 只加独立新表示，不重写其旧许可包与 archive 身份。
7. 两次本地 replay／生成幂等；验证新 PDF／TXT／selectors／NOTICE 库存绑定。运行当前 head 的 `make test`、`make validate`、`make demo`、`make reproducibility`、materialization completeness 与 coverage 校验。重复一次生成不等于重复 GET；报告准确区别。
8. 每 UID 如实 before→after：新 PDF 原件可 complete，native text 可 partial；旧 source 缺图仍显式。现有其他 gate errors／blocked 不由这三 supplement 覆盖或消失，全库 P4 未完成不得宣称 PASS。精确 HEAD／BASE 的独立三维 PASS、当前适用 CI success 后正常合入 work；不是 main 完成证明。

## 6. 当前执行合同（先发布再获取）

路径是后续受控上限；生成目录通配只允许既有生成器输出，不授权手改 production／schema／claim 内容。三项 capsule 仅开放下列新四文件与 manifest／snapshot／README，旧 source、normalized、root selectors／NOTICE／files.jsonl 不开放写入。

```json
{
  "execution_contract": {
    "plan_id": "nonrepo-materialization-main-convergence-260916",
    "phase": "P3-PDF-03",
    "base_branch": "work/v0-meta-kb-initialization-demo-260910",
    "base_sha": "512794e2386898aaaac67a8268cc61e0fe8cb594",
    "target_branch": "work/v0-meta-kb-initialization-demo-260910",
    "execution_branch": "codex/p3-pdf-03-260917",
    "status": "local_validation_passed_exact_pair_review_and_ci_pending",
    "adapter_family": "arxiv_latex_v2",
    "action_bucket": "open_fulltext_fetch",
    "source_uids": [
      "arxiv-1606.04671",
      "arxiv:2404.16130",
      "arxiv:2505.22954"
    ],
    "canonical_source_versions": {
      "arxiv-1606.04671": "v4",
      "arxiv:2404.16130": "v2",
      "arxiv:2505.22954": "v3"
    },
    "fixed_pdf_urls": {
      "arxiv-1606.04671": "https://arxiv.org/pdf/1606.04671v4",
      "arxiv:2404.16130": "https://arxiv.org/pdf/2404.16130v2",
      "arxiv:2505.22954": "https://arxiv.org/pdf/2505.22954v3"
    },
    "allowed_paths": [
      "docs/plans/260916-corpus-completion-main-convergence/p3-pdf-03-fixed-version.md",
      "docs/plans/260916-corpus-completion-main-convergence/branch-ledger.yaml",
      "raw_data/arxiv/Progressive Neural Networks/metadata.yaml",
      "raw_data/arxiv/From Local to Global: A Graph RAG Approach to Query-Focused Summarization/metadata.yaml",
      "raw_data/arxiv/Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents/metadata.yaml",
      "raw_data/licenses/p3-pdf-03-*.md",
      "materialized_sources/corpus/arxiv-1606.04671--2b4672cf/pdf-supplement/document.pdf",
      "materialized_sources/corpus/arxiv-1606.04671--2b4672cf/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-1606.04671--2b4672cf/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-1606.04671--2b4672cf/pdf-supplement/NOTICE.md",
      "materialized_sources/corpus/arxiv-1606.04671--2b4672cf/manifest.yaml",
      "materialized_sources/corpus/arxiv-1606.04671--2b4672cf/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-1606.04671--2b4672cf/README.md",
      "materialized_sources/corpus/arxiv-2404.16130--fe9ed9e5/pdf-supplement/document.pdf",
      "materialized_sources/corpus/arxiv-2404.16130--fe9ed9e5/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-2404.16130--fe9ed9e5/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-2404.16130--fe9ed9e5/pdf-supplement/NOTICE.md",
      "materialized_sources/corpus/arxiv-2404.16130--fe9ed9e5/manifest.yaml",
      "materialized_sources/corpus/arxiv-2404.16130--fe9ed9e5/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-2404.16130--fe9ed9e5/README.md",
      "materialized_sources/corpus/arxiv-2505.22954--8a7041cb/pdf-supplement/document.pdf",
      "materialized_sources/corpus/arxiv-2505.22954--8a7041cb/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-2505.22954--8a7041cb/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-2505.22954--8a7041cb/pdf-supplement/NOTICE.md",
      "materialized_sources/corpus/arxiv-2505.22954--8a7041cb/manifest.yaml",
      "materialized_sources/corpus/arxiv-2505.22954--8a7041cb/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-2505.22954--8a7041cb/README.md",
      "raw_data/audits/materialization_rights_review.yaml",
      "raw_data/audits/non_repo_materialization_coverage_2026-09-16.yaml",
      "raw_data/audits/materialization_completeness_2026-09-10.yaml",
      "materialized_sources/README.md",
      "materialized_sources/index.yaml",
      "source_registry/README.md",
      "source_registry/registry.yaml",
      "source_registry/registry.jsonl",
      "experiments/v0_meta_kb_initialization_demo_260910/00_inputs/materialization_snapshot.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/00_inputs/selected_sources.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/00_inputs/wiki_build_request.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/00_inputs/page_plan.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/01_ontology/meta_kb_ontology.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/01_ontology/schema_bindings.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/02_entities/**",
      "experiments/v0_meta_kb_initialization_demo_260910/03_evidence/**",
      "experiments/v0_meta_kb_initialization_demo_260910/04_claims/**",
      "experiments/v0_meta_kb_initialization_demo_260910/05_wiki/**",
      "experiments/v0_meta_kb_initialization_demo_260910/06_evaluation/**",
      "experiments/v0_meta_kb_initialization_demo_260910/07_review/**",
      "experiments/v0_meta_kb_initialization_demo_260910/08_release/**",
      "experiments/v0_meta_kb_initialization_demo_260910/README.md"
    ],
    "generated_paths": [
      "materialized_sources/corpus/arxiv-1606.04671--2b4672cf/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-1606.04671--2b4672cf/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-1606.04671--2b4672cf/manifest.yaml",
      "materialized_sources/corpus/arxiv-1606.04671--2b4672cf/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-1606.04671--2b4672cf/README.md",
      "materialized_sources/corpus/arxiv-2404.16130--fe9ed9e5/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-2404.16130--fe9ed9e5/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-2404.16130--fe9ed9e5/manifest.yaml",
      "materialized_sources/corpus/arxiv-2404.16130--fe9ed9e5/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-2404.16130--fe9ed9e5/README.md",
      "materialized_sources/corpus/arxiv-2505.22954--8a7041cb/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-2505.22954--8a7041cb/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-2505.22954--8a7041cb/manifest.yaml",
      "materialized_sources/corpus/arxiv-2505.22954--8a7041cb/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-2505.22954--8a7041cb/README.md",
      "raw_data/audits/materialization_completeness_2026-09-10.yaml",
      "materialized_sources/README.md",
      "materialized_sources/index.yaml",
      "source_registry/README.md",
      "source_registry/registry.yaml",
      "source_registry/registry.jsonl",
      "experiments/v0_meta_kb_initialization_demo_260910/00_inputs/materialization_snapshot.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/00_inputs/selected_sources.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/00_inputs/wiki_build_request.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/00_inputs/page_plan.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/01_ontology/meta_kb_ontology.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/01_ontology/schema_bindings.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/02_entities/**",
      "experiments/v0_meta_kb_initialization_demo_260910/03_evidence/**",
      "experiments/v0_meta_kb_initialization_demo_260910/04_claims/**",
      "experiments/v0_meta_kb_initialization_demo_260910/05_wiki/**",
      "experiments/v0_meta_kb_initialization_demo_260910/06_evaluation/**",
      "experiments/v0_meta_kb_initialization_demo_260910/07_review/**",
      "experiments/v0_meta_kb_initialization_demo_260910/08_release/**",
      "experiments/v0_meta_kb_initialization_demo_260910/README.md"
    ],
    "pre_get_gates": {
      "integration": "PR18 merged normally at 512794e2386898aaaac67a8268cc61e0fe8cb594; latest work and PR1 head match; single active implementation batch",
      "identity": "existing_fixed_vN_work_grant_and_exact_three_PDF_targets_only",
      "public_persistence": "actual_PDF_credit_scope_review_and_independent_revision_bound_allow_before_public_commit"
    },
    "explicitly_out_of_scope": [
      "every other UID, source archive recovery, recursively fetched references, external datasets, code repositories, weights or news originals",
      "overwriting legacy source, normalized TeX/TXT, root selectors/NOTICE, files.jsonl, root revision, legacy retrievals or old rights package",
      "latest or different-version PDF fallback, fabricated retrieval times/pages or moving old allow to new representation",
      "production code/tests/dependencies/workflow changes, new adapter framework and template-license archaeology",
      "new demo selected sources, claims, collector assessments, trusted promotion, default full OCR or requiring perfect linear extraction",
      "other UID audit decisions or unexplained whole-corpus generated rewrites",
      "main merge, issue closure, branch deletion, administrator settings or history cleanup"
    ]
  }
}
```

启动时剩余前置（历史）：当时启动 PR 尚待发布、三份 PDF 未取得，新表示尚未准入。现状以第7、8节为准；P3/P4/P5与 PR #1/main 仍未完成。

## 7. 实际取得记录（acquisition，不等于公开准入）

PR #19 启动合同已发布后，三固定PDF于2026-09-16 23:54:35 UTC批次开始，23:54:53 UTC观察全部结束。各URL与请求相同、HTTP200、application/pdf、零redirect、TLS正常；时间为真实批次观察，不冒充每件服务器时间。

| UID／固定PDF | bytes | 实际页数 |
| --- | ---: | ---: |
| arxiv-1606.04671／1606.04671v4 | 4,278,357 | 14 |
| arxiv:2404.16130／2404.16130v2 | 6,893,854 | 26 |
| arxiv:2505.22954／2505.22954v3 | 3,825,399 | 72 |

合计14,997,610 bytes、112页；未重新取得source archive、旧图文件或外部代码/数据。三固定官方abs身份页另作元数据读取，其实际license链接均指CC BY4.0，与既有canonical一致；这些页面不是本批PDF的HTTP取得记录，网络请求统计另分。实际PDF文件尚处非公开临时审读区，正文/图/样例信用与新表示范围未完成前不写入repo。

主线使用PDF技能渲染DGM首/中/末以及全部八编号图（对应十原实引资产）和关键算法页面；两名只读内容reader审其余两篇。实际72页都有原生文本，不代表图义或代码缩进无损。DGM已有source_excerpt默认返回当前PDF摘要L10–13，显式范围override结果相同，所以无需新增配置或生产代码。上述为有界内容事实，不预写正式新表示allow、最终三维PASS或CI通过。

## 8. 实际内容审核与新表示准入（admission）

主线已完整阅读两位只读 reader 的实际内容报告，完成 DGM 有界审读，并核对三个固定 abs 页实际许可链接及现存完整 CC BY 4.0 法条。依据是本版作品许可与实际表示，不是旧 TeX package allow。采纳以下范围供独立 PDF package 落盘：完整、不修改 bytes 的固定版本论文 PDF，包含其内嵌附录、书目和科学图；由该原件生成的 native plain、页 selectors 与明确修改/信用的 NOTICE。不是外链数据、模型、游戏素材、代码仓库、被引作品全文或商标权许可；未观察到本次表示内新增的具体相反声明，不声称穷尽所有底层权利。

| 作品 | 实际审阅与首中末 | 内容边界和旧图缺口 | 新表示判断 |
| --- | --- | --- | --- |
| PNN v4 | 14/14页全文及整页视觉，另高分辨率复核p5；八作者、前三位等贡献、2022-10-22版次明确 | 主文p1–8，24条参考p9，Supplement A–E p10–14；49个 active-root 图引用（21主图资产+28曲线）均对应图1–13。transfer_pong在p5图4；p14图13和打印页5是实际结尾 | 编译原件 complete，body_quality_verified=true；TXT partial |
| GraphRAG v2 | 26页全文；目视1/4/7/8/9/10/12/14/15/17/18/19/20/21/22/26共16页；十作者及2025-02-19版次明确 | 主文p1–12，书目p12–17，附录A–G p18–26。两幅缺失JPEG对应p19图4(a)/(b) MultiHop-RAG两级社区图；真实结尾为G统计表末行 | 编译原件 complete，body_quality_verified=true；TXT partial |
| DGM v3 | 完整读并目视首1/中36/末72，完整读11/22/23/31，另核25/28/32/37/50/60/71，实际目视全部八编号图及算法31；不声称72页逐字人工审读 | 主文/声明p1–11，书目12–22，目录23，A24/B26/C27/D32/E32/F36/G60/H69/I71/J72；旧10实引图对应八编号图，p72四组future work结束完整。五作者、前两co-first/后两co-senior、2026-03-12版次明确 | 编译原件 complete，body_quality_verified=true；TXT partial；knowledge仍candidate |

PNN图资产逐组映射：progressiveNetDepiction2→p2图1；十二任务截图→p5图2；baselineDepiction6→p5图3；transfer_pong→p5图4；pong_results_neil→p6图5；transfer_atari→p7图6；atari3_results_neil→p8图7；transfer_lab→p8图8；appendix_AFS_vs_APS→p10图9；appendix_compression→p11图10；12 Atari曲线→p12图11；8 Pong曲线→p13图12；8 Labyrinth曲线→p14图13。49是实引源图资产数量，不是编号图数，也不等于恢复全部130 omitted成员。

DGM十图映射：conceptual→p2图1；comparisons和comparisons_polyglot→p7图2；archive和progress→p7图3；transfer_model_task→p8图4；wo_selfimprove→p24图5；wo_openended→p24图6；transfer_model_polyglot→p25图7；dgm_halluc→p69图8。原图文件仍未单独恢复，旧source缺口历史保留。

具体提取损失与恢复：PNN的求和/max算子在新PDF native已恢复，但二维公式上下标/分式、架构连接、p5–11图内数据和末三页曲线形状未完整文字化；GraphRAG p21的entity_name/tuple_delimiter/input_text及p22的rating_explanation下划线被提取为空格，不能用TXT作精确可执行prompt，另有图拓扑/曲线/颜色、表分组/bold损失；DGM p31–32的for/foreach/if/箭头/并集/end/return已恢复，但控制作用域、数学和附录diff/代码布局仍扁平。三原件共112页均非空、零提取失败，只证明结构诊断，不证明无损正文。页selector首中末preview与实际页文字对应；DGM重复conference header是真实页起点。

实际信用处理：PNN保留八作者/前三等贡献、Google DeepMind以及论文中的有限benchmark截图/学术出处；p5 River Raid、Seaquest中的ACTIVISION标识可见，不把底层游戏资产、ROM、商标标成论文作者BY4作品。GraphRAG保留十作者/共同贡献、AFaCTA六作者ACL短定义信用；p21 Fed输入与旧system_prompts.tex:37归一化后全等，59词，未增加新闻正文量，仅沿既有科学示例目的/数量限定，不授予新闻全文独立公开权。DGM保留五作者及正确贡献脚注，论文伦理声明不等于外链软件/数据再许可。没有新取新闻、游戏、数据集或源码依赖；没有重开STY历史。

正文消费者（consumer）核对：PNN/GraphRAG不新增demo选入。DGM的既有Page1默认路径准确返回摘要L10–13；显式L10–39 override返回相同结果，故不加无必要配置。包装后需复验PDF/TXT/selectors/revision/NOTICE绑定及既有两claim的派生引用，不新增知识主张、不提升trusted。

以上是实际内容和表示准入决定，不是 PR19 最终独立 evaluator PASS。包装落盘后的四方grant、一致性、旧73文件/221 selectors保留、无fetch重放、生成物、当前CI和精确HEAD/BASE仍各自验收。

## 9. 包装执行与可重放事实（packaging）

三固定原件已按取得 bytes 写入仓库，各自 PDF/TXT/selectors/NOTICE 四文件；canonical、capsule snapshot、manifest、machine audit 的新 grant 完全一致，六字段齐全，approved_scope 与 scope 一致。完整 CC BY 4.0 NOTICE 每篇20,118 bytes，与既有法条资产逐字相同；正文唯一末注保留实际作者、修改与范围。旧root包不被这份补充表示替换。

| 表示 | TXT含末注：行／bytes | 新页selectors | inventory：文件／bytes | 整个capsule含manifest：文件／bytes |
| --- | ---: | ---: | ---: | ---: |
| PNN v4 | 908／46,424 | 14 | 31／4,570,614 | 32／4,599,820 |
| GraphRAG v2 | 1,484／93,708 | 26 | 30／7,448,890 | 31／7,470,848 |
| DGM v3 | 5,107／235,644 | 72 | 45／5,256,188 | 46／5,275,654 |

新增12文件共15,484,184 bytes：PDF14,997,610、TXT375,776、页selectors50,444、NOTICE60,354。三个inventory共106文件17,275,692 bytes；加三个manifest是109文件17,346,322 bytes，两个口径不混用。旧73source／627,377 bytes、221root selectors、旧根NOTICE/TXT/TeX/files.jsonl/README以及旧manifest的非inventory字段原样保留；canonical/snapshot仅新增pdf_supplement，其他97条rights audit原始块不变。原GraphRAG/CoScientist旧包错误不在本批偷改。

包装使用既有 `build_pdf_supplement` 与 `replay_pdf_supplement`。三旧包均无启用的tex_reading_view；直接走已有补充表示重放，不调用会重新取archive的常规入口。每篇两次严格离线重放，分别32/31/46个完整capsule文件逐字节不变，fetch/prepare调用均0。三个PDF表示的publication validator及supplement完整性validator均errors=[]/blocks=[]；这个局部结果不是全库公开门控通过。

环境纠偏如实记录：首次系统Python缺pypdf，没有写TXT/selectors；尝试bundled Python时缺requests，import即失败，也未写派生。随后统一使用与CI一致的现成Python3.12.13环境，首次生成及六次重放成功，不安装依赖、不改生产代码。全库demo运行继续出现此前已知的可选fontTools编码warning；保持原环境和有损文本说明，不以临时换库重写本批或其他原文。

主线调用既有registry/index/audit生成器，沿用2026-09-16T04:30:26Z聚合时间，再构建demo/Wiki。结果仍36sources、72claims、72evidence、135Wiki pages，build ID为 `build:llm-wiki-v0:c01527f77acde651`。DGM默认摘要L10–13由本PDF原生文字提供，两个既有candidate身份不增；PNN/GraphRAG不加入selected。全局identity同步是index输入变化的必要传播，不是新增知识。

本地验证执行中的调度纠偏：主线曾把read-only validate和语义差异读取与repro重建并行，读到了生成目录清空/重建中的瞬态，分别出现BROKEN_DOC_LINK和FileNotFoundError。此失败不删改校验规则；等重放完整结束后串行重跑，最终结果另记。183项单元测试已通过；最终稳定树validate、四阶段repro、coverage与精确HEAD/BASE审核/CI尚待记录，不能将初次失败写成PASS。

## 10. 稳定树验收（validation，最终提交审核另行绑定）

上述瞬态失败后，完整repro进程退出0。committed_tree_replay、full_demo_replay、compiler_only_replay、read_only_validation四阶段各169文件逐字节一致；最后一阶段在重建结束后串行执行完整make validate通过。248 YAML／215 migrated metadata、55 docs／80 links、36sources／72claims／72evidence／135pages均无validator errors。可选字体warning仍存在，不冒称整个运行完全无warning。

稳定树语义比较也重新执行成功：来源、evidence、claim集合及身份都与BASE一致；分别只有1条DGM source、1条正文evidence、1条正文claim对象改变，正文evidence明确绑定新PDF TXT的L10–13与新revision/package。DGM另一条collector-assessment claim不变，其余来源/证据/主张对象不变。全局构建identity传播另计，没有手写知识内容。

完整 `git diff --check HEAD` 实际退出2：5,169个诊断只落在DGM原PDF（5,147；Git把该二进制格式判作text进行空白检查）和忠实native TXT（22）。排除这两个有据文件后的全范围检查通过；不修改PDF bytes、不trim原生文本，也不改Git attributes/关闭检查来隐藏诊断。

全库publication gate实际仍退出1：active_full_text=99、audited=100、blocked=64、errors=2，错误仍是旧GraphRAG/CoScientist package不一致。本批三个新PDF独立包无errors/blocks，但不能据此声称全库可公开发布或PR #1放行。coverage最新对账、提交、精确pair CI和独立三维终审仍待完成。

最后稳定树默认coverage auditor已由主线重新采集当前facts并实际执行，exit0／PASS。三UID目标改为独立PDF表示、original complete/verified、text partial/verified、page selectors语义verified；PNN主桶ocr_assessment，GraphRAG/DGM主桶parser_only，均保留严格complete_target_consumable=false和有界下一步。其余128条coverage原始块及对象、131项knowledge不变，完整ODCS execution与旧三表示观察留作历史。

固定分母仍215=131非repo+84repo；原件complete30→33/partial9→6，文本partial44→46/unknown67→65，本地严格完整6、unresolved125、trusted0不变。summary与本报告frontmatter一致。最终变更189路径，其中160个既有demo/Wiki生成物为DGM绑定与必要全局identity传播；生产代码、tests、依赖、workflow零改。本文中的待执行记录是阶段历史；最终精确提交的CI及独立三维结论应以PR19的commit-bound审核COMMENT为准，不在提交前虚填PASS。

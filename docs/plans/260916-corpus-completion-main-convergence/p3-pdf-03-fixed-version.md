---
phase: P3-PDF-03
status: startup_contract_no_new_source_acquisition_yet
base_sha: 512794e2386898aaaac67a8268cc61e0fe8cb594
base_dependency: PR18_merged_at_512794e
adapter_family: arxiv_latex_v2
action_bucket: open_fulltext_fetch
source_uids:
  - arxiv-1606.04671
  - arxiv:2404.16130
  - arxiv:2505.22954
---

# P3-PDF-03 — 三篇同版本官方 PDF 补充：启动合同

本批启动于最新 work `512794e2386898aaaac67a8268cc61e0fe8cb594`。PR #18 已正常 Ready／merge，HEAD `28f0e595aa262461787f63a3686a6187882de226` / BASE `463b848b0b4abef33df6fa51f6fcf9bd7482a922` 获独立三维 PASS（COMMENT 5229547026）及 CI 35163384395 成功。父 PR #1 仍 Draft，以该 work 为 head、main `99ce4670be91637209d67792de0962404fa96488` 为 base，未进入 main。

主线已完整读取最新 Issue #3/#4、README、02/03/04、05/06、plan.yaml 与 ledger；复核上一批已合入及无其他 active writer。已接受 planner 的三 UID 有界草案；当前只有启动报告和分支台账修改，无源 GET、正文改动、代码/测试/workflow修改或生成重建。发布本启动合同 PR 后才获取三份明确 PDF；当前不宣称新正文完整或许可准入。

## 1. 推荐与范围

采用已有 PDF supplement，一次三 UID、一个 adapter family、一个主要 bucket。目的为持久化同一已选版本的完整编译表示，补齐已实证科学图形／书目／算法阅读缺口；不继续扩写 TeX 解释器，不逐组件重审历史，不获取整个 source archive、外链数据／代码／权重，不默认 OCR。

新原件与派生层统一为各 capsule 的 `pdf-supplement/document.pdf`、`document.txt`、`selectors.jsonl`、`NOTICE.md`。原 PDF 按真实响应 bytes 保存；原生提取采用现有 `plain` 模式。取得 PDF 不代表文字无损，旧 archive 中省略成员也不会因此变成已逐件恢复：可在新 PDF 表示证明完整编译作品，在旧 source 表示继续保留缺图历史。

## 2. 身份、现证据与 before

| UID／作品 | canonical metadata | capsule | 固定版本／唯一正文 GET 目标 |
| --- | --- | --- | --- |
| `arxiv-1606.04671`／Progressive Neural Networks | `raw_data/arxiv/Progressive Neural Networks/metadata.yaml` | `materialized_sources/corpus/arxiv-1606.04671--2b4672cf` | v4／`https://arxiv.org/pdf/1606.04671v4` |
| `arxiv:2404.16130`／From Local to Global: A Graph RAG Approach to Query-Focused Summarization | `raw_data/arxiv/From Local to Global: A Graph RAG Approach to Query-Focused Summarization/metadata.yaml` | `materialized_sources/corpus/arxiv-2404.16130--fe9ed9e5` | v2／`https://arxiv.org/pdf/2404.16130v2` |
| `arxiv:2505.22954`／Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents | `raw_data/arxiv/Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents/metadata.yaml` | `materialized_sources/corpus/arxiv-2505.22954--8a7041cb` | v3／`https://arxiv.org/pdf/2505.22954v3` |

官方身份／许可预核入口分别为上述 ID 的 `https://arxiv.org/abs/<ID>vN`；canonical 现有 `versioning.source_version`、`source_archive_url`、`pdf_url` 均已固定。三旧 manifest 的 `source_version:null` 是历史保存层字段，不得填成虚构旧响应或否定现有版本证据；新增 supplement 使用独立 `source_version`。

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
6. 逐件保留旧 73 source files（627,377 bytes）、`files.jsonl`、normalized TeX／TXT（包括旧 NOTICE）、221 root selectors、旧 root NOTICE 字节；旧 manifest 的 root revision、version=null、retrieval、rights、materialization 与 selectors 原值保留，仅追加 supplement、必要库存／大小。旧 snapshot 与 canonical 只加独立新表示，不重写其旧许可包与 archive 身份。
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
    "status": "startup_contract_no_new_source_acquisition_yet",
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

真实剩余前置：启动 PR 尚待发布；三份目标 PDF 未 GET、页数／bytes／可见信用未读、对应新表示 grant 未作；DGM 实际 Page 1 摘录范围待 PDF。作品级既有版本／授权是有限预核依据，不自动准入新表示。无证据要求新代码或新用户权限；真正相反声明或身份差异按合同停当前受影响项。P3/P4/P5与 PR #1/main 未完成。


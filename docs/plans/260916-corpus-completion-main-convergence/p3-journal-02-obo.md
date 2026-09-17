---
phase: P3-JOURNAL-02
base_sha: 9b6d738ebe9530860235f4c1af3f58928b6c81c8
status: local_validation_complete_pending_exact_head_independent_review_and_ci
coverage_summary: {"collection_records":215,"non_repo_total":131,"github_repo_excluded":84,"reported_content_tier_counts":{"excerpt_capsule":23,"full_text":97,"metadata_capsule":11},"source_type_counts":{"arxiv":73,"biorxiv":2,"blog":10,"industry":2,"journal":11,"methodology":7,"paper":2,"standard":24},"original_artifact_counts":{"complete":52,"metadata_only":12,"partial":4,"unknown":63},"text_extraction_counts":{"complete":8,"partial":59,"unavailable":12,"unknown":52},"action_bucket_counts":{"access_restricted":8,"author_manuscript_fetch":2,"complete_verified":8,"html_article_snapshot":11,"identity_or_version_ambiguous":3,"needs_boundary_verification":51,"ocr_assessment":36,"parser_only":6,"public_persistence_decision":4,"standard_spec_fetch":2},"public_redistribution_counts":{"allow":33,"block":65,"unknown":33},"content_inspected_full_text":59,"structure_only_full_text":38,"locally_persisted_complete":8,"knowledge_candidate_sources":30,"knowledge_trusted_sources":0,"knowledge_sources_without_demo_claims":101,"unresolved_sources":123}
execution_contract:
  plan_id: nonrepo-materialization-main-convergence-260916
  phase: P3-JOURNAL-02
  base_branch: work/v0-meta-kb-initialization-demo-260910
  base_sha: 9b6d738ebe9530860235f4c1af3f58928b6c81c8
  target_branch: work/v0-meta-kb-initialization-demo-260910
  batch_branch: codex/p3-journal-02-obo-260917
  source_uids: ["doi:10.1038/s41587-021-01054-6"]
  adapter_family: generic_web_or_document_v2
  action_bucket: access_restricted
  representation: pdf_supplement
  canonical_id: 10.1093/database/baab069
  canonical_source_version: Version of Record; publisher corrected/typeset edition 2021-10-26
  selected_versions: {"doi:10.1038/s41587-021-01054-6": "publisher-vor:doi:10.1093/database/baab069;pmc:PMC8546234.1"}
  sole_body_get_candidate: https://pmc-oa-opendata.s3.amazonaws.com/PMC8546234.1/PMC8546234.1.pdf
  production_code_changes: minimal_shared_pdf_transport_mime_acceptance_with_signature_and_parse_checks
  body_gets_completed: 1
  body_http_status: 200
  retrieved_at: '2026-09-17T12:42:53Z'
  transport_content_type: binary/octet-stream
  payload_bytes: 1235925
  actual_page_count: 9
  body_quality_verified: true
  startup_only_writes:
    - docs/plans/260916-corpus-completion-main-convergence/p3-journal-02-obo.md
    - docs/plans/260916-corpus-completion-main-convergence/branch-ledger.yaml
  allowed_paths:
    - scripts/materialize_all_sources.py
    - scripts/validate_materialization_completeness.py
    - tests/test_pdf_supplement.py
    - docs/plans/260916-corpus-completion-main-convergence/p3-journal-02-obo.md
    - docs/plans/260916-corpus-completion-main-convergence/branch-ledger.yaml
    - raw_data/journal/OBO Foundry in 2021/metadata.yaml
    - materialized_sources/corpus/doi-10.1038-s41587-021-01054-6--5fa5a2aa/README.md
    - materialized_sources/corpus/doi-10.1038-s41587-021-01054-6--5fa5a2aa/source-metadata.yaml
    - materialized_sources/corpus/doi-10.1038-s41587-021-01054-6--5fa5a2aa/manifest.yaml
    - materialized_sources/corpus/doi-10.1038-s41587-021-01054-6--5fa5a2aa/pdf-supplement/document.pdf
    - materialized_sources/corpus/doi-10.1038-s41587-021-01054-6--5fa5a2aa/pdf-supplement/document.txt
    - materialized_sources/corpus/doi-10.1038-s41587-021-01054-6--5fa5a2aa/pdf-supplement/selectors.jsonl
    - materialized_sources/corpus/doi-10.1038-s41587-021-01054-6--5fa5a2aa/pdf-supplement/NOTICE.md
    - raw_data/audits/materialization_rights_review.yaml
    - raw_data/audits/non_repo_materialization_coverage_2026-09-16.yaml
    - raw_data/audits/materialization_completeness_2026-09-10.yaml
    - materialized_sources/index.yaml
    - materialized_sources/README.md
    - source_registry/registry.yaml
    - source_registry/registry.jsonl
    - source_registry/README.md
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/materialization_snapshot.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/wiki_build_request.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/page_plan.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/01_ontology/meta_kb_ontology.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/02_entities/domains.jsonl
    - experiments/v0_meta_kb_initialization_demo_260910/05_wiki/**
    - experiments/v0_meta_kb_initialization_demo_260910/06_evaluation/**
    - experiments/v0_meta_kb_initialization_demo_260910/07_review/**
    - experiments/v0_meta_kb_initialization_demo_260910/08_release/**
    - experiments/v0_meta_kb_initialization_demo_260910/README.md
  generated_paths:
    - materialized_sources/corpus/doi-10.1038-s41587-021-01054-6--5fa5a2aa/README.md
    - materialized_sources/corpus/doi-10.1038-s41587-021-01054-6--5fa5a2aa/source-metadata.yaml
    - materialized_sources/corpus/doi-10.1038-s41587-021-01054-6--5fa5a2aa/manifest.yaml
    - materialized_sources/corpus/doi-10.1038-s41587-021-01054-6--5fa5a2aa/pdf-supplement/document.txt
    - materialized_sources/corpus/doi-10.1038-s41587-021-01054-6--5fa5a2aa/pdf-supplement/selectors.jsonl
    - raw_data/audits/materialization_completeness_2026-09-10.yaml
    - materialized_sources/index.yaml
    - materialized_sources/README.md
    - source_registry/registry.yaml
    - source_registry/registry.jsonl
    - source_registry/README.md
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/materialization_snapshot.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/wiki_build_request.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/page_plan.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/01_ontology/meta_kb_ontology.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/02_entities/domains.jsonl
    - experiments/v0_meta_kb_initialization_demo_260910/05_wiki/**
    - experiments/v0_meta_kb_initialization_demo_260910/06_evaluation/**
    - experiments/v0_meta_kb_initialization_demo_260910/07_review/**
    - experiments/v0_meta_kb_initialization_demo_260910/08_release/**
    - experiments/v0_meta_kb_initialization_demo_260910/README.md
  explicitly_out_of_scope:
    - other_UIDs_or_new_collection_sources
    - code_or_tests_outside_the_three_explicit_pdf_transport_mime_paths
    - schema_dependency_workflow_new_adapter_or_acquisition_framework_changes
    - root_document_selectors_revision_errors_warnings_retrievals_or_historical_acquisition_replacement
    - XML_TXT_tar_images_SI_ontology_tools_data_references_or_full_bucket_downloads
    - repeated_challenge_requests_access_control_bypass_or_new_author_permission_requests
    - demo_selection_source_evidence_claim_semantic_changes_or_trusted_promotion
    - new_license_text_fetch_or_raw_license_file_changes
    - main_merge_issue_closure_branch_deletion_or_history_rewrite
  independent_evaluation: pending_actual_committed_head_and_base
  final_ci: pending_actual_committed_head_and_base
---

# P3-JOURNAL-02 — OBO 官方开放 PDF 的单 UID 启动合同

## 执行前合同修订（Pre-implementation Contract Amendment）

PR #25 于 `2026-09-17T12:42:26Z` 以 Draft 发布后，唯一批准 PDF 于 `12:42:42Z–12:42:53Z` 完成一次 GET：HTTP 200、无重定向、TLS 校验成功、1235925 bytes。实际响应 `Content-Type: binary/octet-stream`，不得改写为 `application/pdf`。现有构建与验证各有一处严格 HTTP MIME 检查，故先修订合同，才允许实施三文件最小兼容修正：PDF 传输类型接受 `application/pdf`、`application/octet-stream`、`binary/octet-stream`（允许规范化大小写／参数，但保留原始记录）；它们不替代 `%PDF-` 文件签名、真实解析／页检查、准确 URL／字节绑定、四方许可包与 inventory 验证。检测到的表示 `media_type` 仍为 `application/pdf`，不是伪造服务器响应。

修订仅涉及 materializer、completeness validator 和既有 PDF 测试；须覆盖两种二进制 MIME 的真实有效 PDF、非法／缺失 MIME、冒充 PDF 的非 PDF／损坏载荷以及既有 application/pdf 回归。不得添加 UID／域名特例，不改变 publication rights 规则或 workflow，不重取正文。以下启动段落与“未做”保留为启动时历史记录，不代表此修订后的当前状态。实际审读／包装／最终评价仍待完成，未凭 GET 宣称质量通过。

本批从最新 work `9b6d738ebe9530860235f4c1af3f58928b6c81c8` 串行启动；PR #24 已合入 work，父 PR #1 仍为 Draft，成果未进入 main。已按 06 亲读 Issue #3/#4、README、02/03/04、plan 与 ledger，并核本分支及 HEAD。当前仅准备本报告和账本，PR 尚未创建，正文未 GET；计划不是独立验收 PASS。

## 选择与版本（Selection and Version）

工作假设（working hypothesis）是已有 generic journal `pdf_supplement` 足以保留同一作品的官方发表版（Version of Record，VoR），不新增 adapter。相比重复 OUP／PMC 网页挑战或扩写网页抓取器，采用 PMC 官方 Cloud Service 已正常列举出的唯一主 PDF；保留稳定 UID 和 OUP canonical，不重复身份修复。

已完整读取 `/tmp/obo-official-machine-access-preflight.md`。预核于 `2026-09-17T12:32:54Z–12:33:12Z` 完成三次官方目录／JSON 元数据 GET，均 200；没有正文 GET／HEAD。JSON 以 DOI `10.1093/database/baab069`、PMID `34697637`、PMCID `PMC8546234`、完整题名及 `is_manuscript=false` 绑定同作发表版。[官方机器服务](https://pmc.ncbi.nlm.nih.gov/tools/pmcaws/)与其 [README §5.1](https://pmc-oa-opendata.s3.amazonaws.com/README.txt) 支持桶／实际 key 的直接 HTTPS 传输规则，唯一批准地址如上，不转用 JSON `s3:` URI 的 `md5` query。

PMC storage version `1` 不是出版者 v1，也不保证对象不可更新。初选 supplement 版本为 `publisher-vor:doi:10.1093/database/baab069;pmc:PMC8546234.1`；canonical 原 `2021-10-26` VoR 记录可保持，两层不能混用。目录 Size `1235925` 仅为预核值，实际 HTTP／bytes／UTC／payload revision 及 PDF 内部身份、版本仍须取得后记录，不能当作已下载证据。完整 8-key 目录仅列主 PDF／XML／TXT／JSON 和四图，没有列定 SI；结合先前文章核对未观察必需 SI，本合同只获取主 PDF，不宣称出版者全部附件不存在。

## 六维基线与后续判断（Baseline and Later Judgment）

以下直接读取当前 coverage ledger 的本 UID，不重跑全局 facts；本轮所有 after 均保持未执行，不预填 complete。

| 维度 | 当前 before | 本合同约束 |
| --- | --- | --- |
| 身份／版本 | UID 不变；canonical `10.1093/database/baab069`；2021-10-26 VoR 尚未 body-byte 核验 | 取得 PDF 后核同 DOI、题名、25 作者及实物版本／边界 |
| 原件覆盖 | `metadata_only / verified` | 真正完整原 PDF 审读成立后才变更 |
| 文本提取 | `unavailable / verified` | 原生分页提取；公式、图、表缺损照实保留 partial，不默认 OCR |
| 本地持久化 | 2 件 inventory、3668 bytes；无正文／原 PDF；`complete_target_consumable=false` | 恰新增 PDF、页 TXT、页 selectors、NOTICE 四文件；原件不改 |
| 公开再分发 | root `unknown`；文章 `document_permission=allow_with_conditions`、CC-BY-4.0 已证 | unknown 指旧 root 无已存正文表示／版本包，不指作者授权未知；新表示独立实物信用核验后包装 |
| 知识准入 | state `null`、无 demo claims，当前未选中 | 不自动新增选源、candidate claim 或 trusted；source/evidence/claim 语义不变 |

现 `action_bucket=access_restricted`、`resolution=unresolved` 保持为 before。既有 `historical_acquisition`、canonical-entry 旧挑战证据、root `revision=null`、`retrievals=[]`、`selectors=[]`、errors／warnings 保全；不得用新 PDF 覆盖旧 metadata-only root 诊断或伪造 root 文件。取得和审读后才记录独立表示的 body-quality、六维 after、剩余缺损及下一 bucket。

## 包装、顺序与验证（Packaging, Ordering and Verification）

正文边界为此发表定稿的摘要／引言、Results／Discussion、4 图／3 表、致谢／Funding、15 参考项与信用／许可；这些是待实物复核的边界，不是已取得断言。实际 PDF 全部 native 页需审读，并目视首／中／尾、图表信用及正常结尾；全部新 selectors 本地解析且首／中／末语义核对。`body_quality_verified` 只有证据成立后才设置，文本完整性独立判断。

复用已有 CC-BY-4.0 许可证据与 `raw_data/licenses/cc-by-4.0.md`，不新取法条、不另索已证文章的作者授权。新 NOTICE 自包含实际题名、完整 25 作者、©The Author(s)2021／OUP、真实 DOI／PMC 来源、实物全部 credit、许可链接和完整法条、原 PDF 未改与有损页文本／selector 派生说明；遵守 PMC 数据来源声明、不使用标志或暗示 NLM 背书，并注明固定快照不保证当前最新。许可对应 canonical metadata／capsule snapshot／manifest／现有 rights 本 UID 的独立 PDF 表示；rights 已有该 UID，更新而非重复追加。

执行顺序固定为：主线审查／发布本启动 PR → 唯一 PDF GET → 实物身份／版本／覆盖／信用审读 → 既有 helper 包装与断网重放 → C（canonical/capsule）与 R（rights）定稿 → aggregate → K（coverage）依据实际聚合结果对账 → 全部输入冻结 → 主线必要 demo／validate／repro → 只读复核与报告 → 精确 head/base 独立 evaluator 和当前 CI。若最终复核需要再修改 C／R／K，须重新冻结并重建，不能将改输入写成仅更新报告；避免重复 PR #24 的 stale build identity 失败。

后续计划验证使用 `/tmp/llm-wiki-ci-312-260916/bin/python`：定向 PDF-supplement／rights 检查、真实消费者离线读取及两次禁止 fetch／prepare 的 PDF 重放、`make test`、`make validate`、coverage audit 和 `make reproducibility`；全局 identity 受 C/R/K 输入影响时，最后由主线运行 `make demo`。必要生成路径只允许既有 generator 的 build identity／inventory／依赖机械传播，OBO 不新增 demo source，source/evidence/claim 内容保持；未解释的越界或其他来源实质重写即停止。

## 明确未做与停线（Explicit Non-results and Stop Conditions）

本轮未获取正文，未包装 PDF，未修改 metadata／capsule／R／K 或任何代码、测试、workflow／生成物；未声明 artifact／extraction complete、未自评 PASS、未提交／push／创建 PR、未进入 main、未关闭 Issue、未晋升 trusted。当前独立审核和 CI 均待实际提交的精确 head/base。若正式 PDF失败、身份／版本不符、实物 credit 排除、必要 SI 边界改变、现 helper 不适配或 base／同 UID 并发改变，则记录具体证据并停线，不擅自扩大合同、改代码或改用其他下载地址。

## 实际获取与内容审读（Acquisition and Content Inspection）

以上启动历史之后，按已发布合同完成唯一主 PDF GET。实际 requested／resolved URL 均为 `https://pmc-oa-opendata.s3.amazonaws.com/PMC8546234.1/PMC8546234.1.pdf`；HTTP 200、redirect 0、TLS 校验结果 0、1235925 bytes、`binary/octet-stream`。GET 从 `2026-09-17T12:42:42Z` 至 `12:42:53Z`；服务器 Date 为 `12:42:45 GMT`，Last-Modified 为 `2026-02-22T11:18:25Z`，两者不替代获取时间或出版日期。本轮没有第二次 PDF 下载、XML／TXT／图片／SI 请求或挑战重试。

内容 executor `/root/pdf04_content_a` 在缓存实物上读取全部 9 页原生文本，并逐页查看 125 dpi 渲染；主线复核 P1／P5／P7／P8／P9 版面。PDF 1.5、未加密、无 Form／JavaScript；P1 的 DOI、完整题名、25 作者、Database／article ID baab069 与 canonical 对应。P1 仅印收到 2021-05-18、修订 2021-10-05、接受 2021-10-13，不印 2021-10-26 或 storage `.1`；正式出版日仍由既有官方 metadata 证据承担，不用 PDF 创建时间推断版本。

实物完整边界为：P1 摘要／引言；P2 Fig1／Related work；P3 Table1／Results；P4 原则与自动验证；P5–6 跨页横排 Table2；P7 Table3／Fig2／Results 续文及 Discussion；P8 Fig3／Fig4；P9 Discussion 结论、致谢、Funding 和完整 15 参考项。P9 正常结束于 SWEET 文献 `Comput. Geosci., 31, 1119–1125.`。未见必需 SI 标识；该判断只针对主文章，不声称全部出版附件不存在，不递归正文引用对象。

原件覆盖可判 complete，原生文本必须 partial，具体损失不是推测：

- P2 Fig1 内 13 个框内标签与图标未抽出，只有图注。
- P7 Fig2 截图的 ROBOT 1.8.1／OBO Metadata Schema credit、ontology／原则列标签、颜色和状态符号未抽出；原件中的 credit 保留在 NOTICE 说明。图注说 first 15 而截图有 17 行，保留原作，不擅自纠正。
- P8 Fig3／Fig4 仅图注被抽出，轴、柱、类别、图例与二维关系缺失，不从柱长造精确数值。
  独立 evaluator 的先行实物检查还识别 Fig3 图内 legend 为 `11/21/19`，caption 写 `11 November 2019`；这是上游原作字面不一致，原样保存，不擅自统一日期，也不误判成下载／解析错误。
- 三表主体文字、MUST／SHOULD／N/A 仍可读，但二维布局、跨页关系、样式和链接属性有损。P5–6 本来是横排表，不是坏页；没有虚构所有表格或公式均缺失。

P1 实际文章许可为 CC BY 4.0，版权 © The Author(s) 2021，出版者 Oxford University Press；P9 致谢、两项 Funding 与 15 references 保留，Fig2 的软件 credit 单独识别。全文、全部图表／图注及页脚未观察第三方排除或独立许可收窄。Table2 的 ontology 禁止沿用原标识修改再分发条款是论文讨论的 OBO 原则，不是这篇文章的新禁令。文章许可不扩张为外部软件／ontology／网站整体授权。

## Agentic 判断链条（Decision Chain）

规划者比较了重复网页挑战、改写抓取框架、使用已文档化的官方 PMC Cloud 三条路径；选择准确 key 的单 PDF，复用现有 generic journal 表示。原先不改代码的假设被实际 MIME 响应推翻，先公开修订合同再由独立代码 executor `/root/obo_pdf_mime_executor` 实施共享小判定，无 UID／host 特例；运输 MIME 与检测到的 PDF 表示分离，未伪造原始证据。该 executor 的定向测试从 45 项增至 49 项，全部通过，覆盖正常 PDF 与缺失／非法 MIME、二进制头下的非 PDF／损坏 PDF；原签名、解析、许可和 inventory 门控保留。这是执行证据，不是非作者最终评价。

包装 executor `/root/canonical21_packaging_executor` 负责 C／capsule／R；内容 executor 只作内容及覆盖判断；主线负责合同、聚合顺序及最终交付。最终独立 evaluator 不得是以上作者。最终提交、全局验证、精确 HEAD／BASE CI 与独立三维判定结果将在下文另列；没有这些结果不能 Ready 或 merge。

## 来源结果与文件（Source Results and Files）

唯一 UID `doi:10.1038/s41587-021-01054-6`；base work `9b6d738ebe9530860235f4c1af3f58928b6c81c8`。下表是本批真实包装结果，不把 root 历史状态改写为新表示。

| 维度 | Before → After |
| --- | --- |
| 身份／版本 | 同一已修复 DOI／正式版本外证 → PDF 实物身份对应，nested version `publisher-vor:doi:10.1093/database/baab069;pmc:PMC8546234.1`；legacy UID 与 canonical 日期不改 |
| 原件覆盖 | metadata_only → complete：真实 9 页主文章，4 图／3 表／15 参考项 |
| 文本提取 | unavailable → partial：38812 字符／693 行，具体图内与表布局损失如上；无 OCR |
| 本地持久化／定位 | 2 inventory 文件／3668 bytes、0 selector → 6 inventory 文件／1315664 bytes、9 页 selector；含 manifest 全胶囊 7 文件；strict complete 仍 false |
| 公开再分发 | 文章许可已证、无独立 PDF → 新 PDF／派生／NOTICE 四方包独立 allow；旧 root unknown 与 null revision 保留，不是文章许可未知 |
| 知识准入 | 无 demo claims → 仍无；不新增选源、candidate、trusted；全库语义不因本包自行改变 |

恰新增 `pdf-supplement/` 下 4 件：`document.pdf` 1235925 bytes、`document.txt` 39524 bytes、`selectors.jsonl` 4139 bytes、`NOTICE.md` 26564 bytes。原 PDF 与获取缓存逐字节相等；TXT 明确分页与唯一采集器署名末注，NOTICE 完整保留原作 credit 和已有 BY4 法条。现 README 原字节不变；不制造 root 文档／selector。

手写输入是 canonical metadata 的独立版本／权利与实物观察、现有 R 行及 summary、本报告／分支账本／K 判断、三文件通用 MIME 兼容修正及测试。派生文件由既有 helper 生成 snapshot／TXT／selectors／manifest，再由既有 `rebuild_registry` 与 `write_indexes_and_audit` 统一生成 215 条 registry／index／completeness；aggregate 时间固定为 `2026-09-16T04:30:26Z`，不是本次获取时间。R 只改本 UID 行及 summary；其他 107 行保留。实际表示级审阅为 35 main PDF＋5 SI＝40 allow，其中 BY4 37、BY-SA4 2、BY4 AND Apache2 1；旧根计数不变。

局部完整性与四方许可包检查均为 0 errors／0 blocks；两次通过真实 `materialize_generic` 路由、禁止 fetch／prepare 的重放保持全胶囊 7 文件逐字节一致。完整摘要 `primary_excerpt` 为最终 TXT L37–47，真实消费者取 L37–39／307 字符，正确指向父论文摘要而非作者机构／许可／采集器末注；消费者路径与权利链检查无错误。这些是局部结果，不替代全局验证或终审。

全库公开存储检查本批实际运行仍 exit1：`active_full_text=104 audited=108 blocked=64 errors=2`。两个旧错误仍是 GraphRAG `arxiv:2404.16130` 与 AI co-scientist `arxiv:2502.18864` 的审计／派生包不一致，属已登记 P4 待办；64 根级 block 不等于本次或全库“缺少 64 篇数据”，也不否定已独立批准的新 PDF。没有绕过此检查宣称最终 public tree 或父 PR #1 合格。

## 全量对账与生成影响（Reconciliation and Generated Impact）

真实 coverage 复算为 `215 = 131 非 repo + 84 排除`。原件 complete 51→52、metadata_only 13→12；text partial 58→59、unavailable 13→12；action bucket access_restricted 9→8、ocr_assessment 35→36。严格 complete 仍 8、unresolved 仍 123、trusted 仍 0。OBO 的下一步只在需要图内／布局纯文本消费时做有界评估，不自动全量 OCR。

主线独立比较 base，确认其他 130 条 K 整对象及其他 107 条 R 整对象相等；旧 OBO 整行保留于 `historical_pre_pdf_supplement_coverage`，整个旧 execution 精确保留于唯一 `historical_p3_pdf_06_execution`。原根错误／revision／retrieval／selectors／历史继续保全，新表示事实独立记录；K 的后续 validation false/null 是注明时点的输入冻结检查点，不冒充实时执行失败，最终结果在报告与 GitHub 记录，避免事后回写输入破坏重放。

C／R 包装定稿 → R summary 实际复算 → 215 条 aggregate → 新 4 文件纳入 Git 跟踪 → K 真实 facts／人工判断定稿 → 输入冻结后才运行 `make demo`。结果 `build:v0-meta-kb-260910:2eaeaaf3c3b282a9`、`build:llm-wiki-v0:0175f4c78a0341b7`，36 sources／72 claims／72 evidence／135 pages。151 个必要派生文件发生变化；主线逐个核 135 个 Markdown 页面均只有 build identity 更新，selected_sources、sources、evidence、claims 四份原始输入逐字节等 base，没有语义重写或新增选源。总差异 169 文件全部属于已公开 allowed_paths，未改 workflow 或依赖。

## 实际验证与剩余门控（Verification and Remaining Gates）

统一运行时 `/tmp/llm-wiki-ci-312-260916/bin/python`，Python 3.12.13／pypdf 6.18.1；不是系统 Python 的另一次抽取。

| 实际命令／检查 | 本地结果 |
| --- | --- |
| `make test PYTHON=/tmp/llm-wiki-ci-312-260916/bin/python` | exit0；212 tests，其中 PDF supplement 49 tests；4 条故意损坏 fixture 的 EOF 诊断符合负例预期 |
| `make demo PYTHON=/tmp/llm-wiki-ci-312-260916/bin/python` | exit0；构建与内部验证通过，36／72／72／135，warnings=0/errors=0 |
| `make validate PYTHON=/tmp/llm-wiki-ci-312-260916/bin/python` | exit0；215 manifests／3196 inventory hashes／25858 selectors，materialization errors=0；docs 与 Wiki 引用/manifest 校验通过 |
| `python scripts/audit_non_repo_coverage.py`（同一运行时） | exit0；131 完整逐项 observed 与 summary 对账一致 |
| `make reproducibility PYTHON=/tmp/llm-wiki-ci-312-260916/bin/python` | exit0；committed_tree_replay、full_demo_replay、compiler_only_replay、read_only_validation 四关各169生成文件逐字节一致；所有内部validate通过 |
| base 范围与历史比较、`git diff --check` | 其他130 K／107 R保全、旧整行／execution相等、169路径无越界、无whitespace诊断 |

全库 PDF 原生解析仍输出既有 CFF／缺少 fontTools 与复杂 XObject 提示；这些是已有提取局限，不通过安装新依赖或更改已有 source bytes 消除提示，也不把完整性 validator 的结构 errors=0 写成全部图义无损。

独立 evaluator 为非作者 `/root/canonical21_content_evaluator`。其先行核查不替代终审：最终 HEAD 与 BASE 必须在提交后锁定、在 PR #25 发布完整 agent evaluation／COMMENT，并核当前 CI 的测试合并父提交准确对应，三维均 PASS 才正常 merge。此提交内的 pending 只记录提交前时点，实际 head／review／CI／merge 以 PR #25 的不可变提交与公开记录为准，不自写批准。

明确非结果（Explicit Non-results）：本批不代表131来源全部完成、全库public-tree门控通过或进入main；没有trusted晋升、新选源、新claim、额外GET、删除／迁移旧文、历史改写、分支删除或Issue关闭。PR #1 仍须完成 P3剩余有界项、P4两旧包与fresh-checkout可迁移性对账、明确旧内容公开存储决策、P5精确独立审核与真正fresh main验收。正常本地重放不是fresh checkout；不能用本PR的局部PASS代替父PR放行。

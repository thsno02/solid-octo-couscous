---
phase: P3-JOURNAL-02
base_sha: 9b6d738ebe9530860235f4c1af3f58928b6c81c8
status: startup_contract_not_published_no_body_execution
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
  production_code_changes: none_existing_generic_journal_pdf_supplement_only
  body_gets_completed: 0
  body_http_status: null
  retrieved_at: null
  payload_bytes: null
  actual_page_count: null
  body_quality_verified: null
  startup_only_writes:
    - docs/plans/260916-corpus-completion-main-convergence/p3-journal-02-obo.md
    - docs/plans/260916-corpus-completion-main-convergence/branch-ledger.yaml
  allowed_paths:
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
    - code_tests_schema_dependency_workflow_new_adapter_or_acquisition_framework_changes
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

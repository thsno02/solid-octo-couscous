---
phase: P3-PDF-06
status: startup_not_acquired
base_sha: a3dbb1c87db2875c5354cc773199af453d2df7df
coverage_summary: {"collection_records":215,"non_repo_total":131,"github_repo_excluded":84,"reported_content_tier_counts":{"excerpt_capsule":23,"full_text":97,"metadata_capsule":11},"source_type_counts":{"arxiv":73,"biorxiv":2,"blog":10,"industry":2,"journal":11,"methodology":7,"paper":2,"standard":24},"original_artifact_counts":{"complete":50,"metadata_only":13,"partial":4,"unknown":64},"text_extraction_counts":{"complete":8,"partial":57,"unavailable":13,"unknown":53},"action_bucket_counts":{"access_restricted":9,"author_manuscript_fetch":2,"complete_verified":8,"html_article_snapshot":11,"identity_or_version_ambiguous":3,"needs_boundary_verification":52,"ocr_assessment":34,"parser_only":6,"public_persistence_decision":4,"standard_spec_fetch":2},"public_redistribution_counts":{"allow":33,"block":65,"unknown":33},"content_inspected_full_text":58,"structure_only_full_text":39,"locally_persisted_complete":8,"knowledge_candidate_sources":30,"knowledge_trusted_sources":0,"knowledge_sources_without_demo_claims":101,"unresolved_sources":123}
---

# P3-PDF-06 — ALCE 正式出版 PDF 表示启动合同

```yaml
execution_contract:
  plan_id: nonrepo-materialization-main-convergence-260916
  phase: P3-PDF-06
  status: startup_not_acquired
  base_branch: work/v0-meta-kb-initialization-demo-260910
  base_sha: a3dbb1c87db2875c5354cc773199af453d2df7df
  implementation_branch: codex/p3-pdf-06-alce-publisher-260917
  head_sha: null
  target_branch: work/v0-meta-kb-initialization-demo-260910
  pull_request: null
  prerequisite:
    pull_request: 23
    state: closed_merged
    merge_commit: a3dbb1c87db2875c5354cc773199af453d2df7df
  source_uids: ["arxiv:2305.14627"]
  source_type: arxiv
  adapter_family: arxiv_latex_v2
  action_bucket: open_fulltext_fetch
  representation: pdf_supplement
  selected_version: publisher-vor:doi:10.18653/v1/2023.emnlp-main.398
  canonical_source_version: null
  root_source_version_key: absent_preserved
  originating_arxiv_id: '2305.14627'
  publisher_doi: 10.18653/v1/2023.emnlp-main.398
  anthology_id: 2023.emnlp-main.398
  sole_body_get_candidate: https://aclanthology.org/2023.emnlp-main.398.pdf
  supplementary_information: {required: false, source_pdf_url: null}
  publisher_pdf_correspondence:
    originating_arxiv_id: '2305.14627'
    publisher_doi: 10.18653/v1/2023.emnlp-main.398
    reviewed: true
    audit_evidence_kind: bounded_acl_article_content_correspondence
  correspondence_evidence_ref:
    path: raw_data/audits/materialization_rights_review.yaml
    uid: "arxiv:2305.14627"
    kind: bounded_acl_article_content_correspondence
    checked_at: '2026-09-16'
    capsule_root: materialized_sources/corpus/arxiv-2305.14627--6d5b37c6
  grant_consistency: canonical_capsule_metadata_manifest_pdf_supplement_and_rights_review_item_pdf_supplement
  license_packaging: self_contained_pdf_supplement_NOTICE_no_raw_license_change
  license_text_source: raw_data/licenses/cc-by-4.0.md
  production_code_scope: minimal_publisher_declaration_validation_and_existing_supplement_mode_only
  startup_only_writes:
    - docs/plans/260916-corpus-completion-main-convergence/p3-pdf-06-alce-publisher.md
    - docs/plans/260916-corpus-completion-main-convergence/branch-ledger.yaml
  allowed_paths:
    - scripts/materialize_all_sources.py
    - scripts/validate_publication_rights.py
    - scripts/validate_materialization_completeness.py
    - tests/test_pdf_supplement.py
    - docs/plans/260916-corpus-completion-main-convergence/p3-pdf-06-alce-publisher.md
    - docs/plans/260916-corpus-completion-main-convergence/branch-ledger.yaml
    - raw_data/arxiv/Enabling Large Language Models to Generate Text with Citations/metadata.yaml
    - materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/source-metadata.yaml
    - materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/manifest.yaml
    - materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/pdf-supplement/document.pdf
    - materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/pdf-supplement/NOTICE.md
    - materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/pdf-supplement/document.txt
    - materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/pdf-supplement/selectors.jsonl
    - raw_data/audits/materialization_rights_review.yaml
    - raw_data/audits/non_repo_materialization_coverage_2026-09-16.yaml
    - raw_data/audits/materialization_completeness_2026-09-10.yaml
    - materialized_sources/index.yaml
    - materialized_sources/README.md
    - source_registry/registry.yaml
    - source_registry/registry.jsonl
    - source_registry/README.md
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/materialization_snapshot.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/selected_sources.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/wiki_build_request.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/page_plan.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/01_ontology/meta_kb_ontology.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/01_ontology/schema_bindings.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/02_entities/**
    - experiments/v0_meta_kb_initialization_demo_260910/03_evidence/**
    - experiments/v0_meta_kb_initialization_demo_260910/04_claims/**
    - experiments/v0_meta_kb_initialization_demo_260910/05_wiki/**
    - experiments/v0_meta_kb_initialization_demo_260910/06_evaluation/**
    - experiments/v0_meta_kb_initialization_demo_260910/07_review/**
    - experiments/v0_meta_kb_initialization_demo_260910/08_release/**
    - experiments/v0_meta_kb_initialization_demo_260910/README.md
  generated_paths:
    - materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/source-metadata.yaml
    - materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/manifest.yaml
    - materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/pdf-supplement/document.txt
    - materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/pdf-supplement/selectors.jsonl
    - raw_data/audits/materialization_completeness_2026-09-10.yaml
    - materialized_sources/index.yaml
    - materialized_sources/README.md
    - source_registry/registry.yaml
    - source_registry/registry.jsonl
    - source_registry/README.md
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/materialization_snapshot.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/selected_sources.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/wiki_build_request.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/page_plan.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/01_ontology/meta_kb_ontology.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/01_ontology/schema_bindings.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/02_entities/**
    - experiments/v0_meta_kb_initialization_demo_260910/03_evidence/**
    - experiments/v0_meta_kb_initialization_demo_260910/04_claims/**
    - experiments/v0_meta_kb_initialization_demo_260910/05_wiki/**
    - experiments/v0_meta_kb_initialization_demo_260910/06_evaluation/**
    - experiments/v0_meta_kb_initialization_demo_260910/07_review/**
    - experiments/v0_meta_kb_initialization_demo_260910/08_release/**
    - experiments/v0_meta_kb_initialization_demo_260910/README.md
  generated_constraints:
    semantic_source_change_uids: ["arxiv:2305.14627"]
    semantic_source_page: experiments/v0_meta_kb_initialization_demo_260910/05_wiki/sources/arxiv-2305.14627.md
    existing_candidate_claims: ["claim:bed2f056ecd73c69", "claim:9a3b21da11a96956"]
    other_generated_changes: existing_generator_required_build_identity_inventory_and_dependency_propagation_only
    demo_selection_scientific_assertions_collector_assessments_and_admission: unchanged
  retrieval_attempts: []
  body_http_status: null
  retrieved_at: null
  bytes: null
  actual_page_count: null
  authors_verified_from_new_original: null
  tests_actually_run: []
  independent_evaluation: pending_actual_committed_head_and_base
  final_ci: pending_actual_committed_head_and_base
  explicitly_out_of_scope:
    - PR23_PDF05_report_or_any_other_UID
    - source_identity_type_adapter_change_or_new_collection_UID
    - legacy_source_normalized_root_selectors_notice_readme_files_revision_retrievals_rights_materialization_and_source_gate
    - metadata_license_history_old_v2_or_author_repository_PDF_refetch
    - production_UID_DOI_host_URL_whitelist_or_arbitrary_alternate
    - new_adapter_crawler_schema_dependency_workflow_storage_or_default_acquisition
    - materialize_materialize_all_or_default_arxiv_archive_rebuild
    - demo_coverage_production_changes_or_new_selection_claim_assessment_trust
    - raw_license_creation_or_modification
    - default_OCR_lossless_formula_or_all_figure_linearization_as_exit_gate
    - main_PR1_ready_merge_issue_close_branch_delete_force_push_or_history_rewrite
```

## 1. 选择与当前基线（Decision and Current Baseline）

本轮批准 planner 推荐的串行单 UID 后继（serial single-UID successor）：将 ALCE 正式 EMNLP2023 出版表示接入同一 arXiv 记录，不把 source_type 改成 journal，不编 arXiv vN。问题模型是作品身份与表示身份分离（work identity versus representation identity）；备选是在最小接缝无法闭合时明确保留 unresolved，而不是扩写抓取框架或将正式作品误标 unavailable。

主线已完整重读 Issue #3/#4 与必读计划并只读确认：两 issue 仍 open；PR23 已正常 merge／closed；local／remote work 为上述 exact base，随后从 clean 树建立本 implementation branch。PR #1 仍 Draft，head=a3dbb1c87db2875c5354cc773199af453d2df7df、base=main@99ce4670be91637209d67792de0962404fa96488。PR23 终审与 CI 只在 branch-ledger 登记，不是本批 PASS。

frontmatter 是当前 K summary 的快照：215=131+84，original complete=50、text partial=57、strict／locally persisted complete=8、unresolved=123。没有预测 ALCE after；本轮未取得或实施，来源六维仍保持 before。

## 2. 完整六维 Before 与目标边界（Six-dimensional Before and Target Boundary）

C = raw_data/arxiv/Enabling Large Language Models to Generate Text with Citations/metadata.yaml；R = materialized_sources/corpus/arxiv-2305.14627--6d5b37c6；K = raw_data/audits/non_repo_materialization_coverage_2026-09-16.yaml；A = raw_data/audits/materialization_rights_review.yaml。均按精确 UID arxiv:2305.14627 定位，以下记录来自本次只读核对，不是新 PDF 或 fresh-checkout 验收。

| 维度 | 当前 Before 与证据 |
| --- | --- |
| 身份／版本（Identity/version） | C 与 R/source-metadata.yaml 的 uid/source_type/canonical_id/canonical_url 保持 arxiv:2305.14627／arxiv／2305.14627／https://arxiv.org/abs/2305.14627；adapter=arxiv_latex_v2。两份 source_version=null、root manifest 键缺省，无 publisher_pdf／pdf_supplement。K selected_version=null、source_kind=tex、boundary unverified；A.alternate_publisher_version_review 已绑定旧 source payload 为 v2，null 不抹掉该历史。 |
| 原件覆盖（Original artifact） | K unknown／unverified、无本地 PDF；R/manifest.yaml 声明四活动科学图 figs/main.pdf、figs/citation.pdf、figs/ret.pdf、figs/correctness.pdf omitted。既有有界观察的旧表示 partial 独立保留；全部 omitted=7 不等于七个正文缺口，K 空 missing_assets 不表示无缺失。 |
| 文本提取（Text extraction） | K unknown／unverified；R/normalized/document.txt 2041 行／90939 字符、95 root selectors，semantic_boundary_verified=false；missing_pages/sections/parser_errors 为空但未核验，ocr_state=not_applicable。旧 ALCE／Vanilla 宏名损失与题名泄漏观察保留，不将 structural_probe_only 写成全篇核验。 |
| 本地持久化（Local persistence） | R manifest 声明 44 inventory files、38 source 文字成员；K all_declared_files_present/tracked=true、root selectors resolved、index_registry_consistent=true；PDF path=null、fresh_checkout_verified_this_phase=false、complete_target_consumable=null。现有 TXT／manifest 与旧原件留存不证明目标完整或新 checkout。 |
| 公开再分发（Public redistribution） | K state/reported_gate=block、revision_matches=true；A classification=permission_unverified、root publication_gate=block。A.bounded_acl_article_content_correspondence 记录正式 ACL 作品 BY4 路径及主干对应，但旧 v2 未对应扩展、模板／BST／两摘要条件未闭合；原 supports_public_redistribution=false 保留，新 PDF grant 尚不存在。 |
| 知识准入（Knowledge admission） | K candidate=2；现 ALCE selected 来源及 claim:bed2f056ecd73c69、claim:9a3b21da11a96956 保持 candidate，不新增科学断言、claim、collector 判断或 trusted 晋升。 |

本批目标为正式 DOI 10.18653/v1/2023.emnlp-main.398／Anthology ID 2023.emnlp-main.398 的完整主文、正式 A–I 附录、图表、书目与真实结尾；选版标识是 publisher-vor:doi:10.18653/v1/2023.emnlp-main.398，独立存于 publisher_pdf／PDF package，不写入旧 source_version。SI 明确 false，不自动发现或取得额外文件。

旧 v2 R/source/sections/appendix.tex 的 Open-source Models 三段与 Stable Beluga 2 结果行不在已核正式 PDF，不能猜补到出版表示，也不因新 BY4 删除／授权旧扩展。A 的既有 24 页／481,920 bytes／©2023 ACL 和作者仓库另一 PDF 的事实只作为历史对应证据或审读预期，不是本批新 GET 的响应／bytes／pages／retrieved_at。许可及历史已有审核不重抓；实际正文取得只用合同中唯一 ACL URL。

## 3. 最小通用接缝与回归合同（Minimal General Seam and Regression Contract）

批准后续只在三生产文件内实现 planner 的小接口；本轮尚未修改任何代码：

- materialize_all_sources.py：pdf_supplement_version_urls 先校两份显式 publisher_pdf 声明，再走普通 arXiv vN；原记录四字段／规范 originating ID、独立 publisher DOI、唯一 HTTPS URL、publisher-vor 版本和显式 SI 一致，畸形声明拒绝而非回退。build_pdf_supplement／现 _derive_pdf_supplement_part 仅在校验通过后用 publisher 模式，保留 (main_url, si_url) 接口、原 inventory／package.source_version／audited allowance 预检与全部内存检查后才写 derived 的顺序；不改默认获取路由。
- validate_publication_rights.py：按已验证表示判 publisher，声明 correspondence 与 grant.publisher_correspondence 全等；reviewed 必须是真 bool true。按本 UID 引用 A 既有 evidence.kind，要求 checked_at、规范 DOI 相同、正式 URL 是该 evidence 的明确 URL／related_urls 成员；DOI 仅标准前缀去除／大小写比较。四份 grants 同步改坏也不能放行，旧 evidence 的 false 与 root block 不升级。
- validate_materialization_completeness.py：显式支持的 publisher 声明缺 manifest supplement 必须拒绝；已验证模式传到 part retrieval，现页／文本／selector／inventory／rights 检查保持。两 validator 的缺声明检查一致；pdf_supplement_retrieval_url_matches 原样，Nature cookie 特例不扩到 ACL，requested／resolved 都须为批准 URL。

correspondence 使用普通 mapping：originating_arxiv_id、publisher_doi、reviewed、audit_evidence_kind；canonical／capsule 声明相等，PDF package 的 publisher_correspondence 与其相等，不使用跨文件 anchor。四处 grants／package 的 source_version、URL、真实 revision、scope、归属与 NOTICE 必须在实际取得后、builder／公开入库前闭合；代码校结构与审计绑定，作品语义关系仍由独立 reader／evaluator 核实，不凭题名、域名、MIT 或 arXiv nonexclusive 推断。

仅扩 tests/test_pdf_supplement.py 的现 temp fixtures／minimal_pdf_pages，用不同于 ALCE 的 synthetic arXiv ID、DOI、publisher URL 证明泛化（generalization），不设生产 UID／DOI／host／URL 白名单，不为了测试取得真实原件：

| 回归类别 | 后续最低要求；当前未执行 |
| --- | --- |
| 正向／旧路径 | synthetic arxiv→publisher、SI=false 能被 helper／rights／completeness 与现 representation consumer 使用；C/snapshot source_version 仍 null，旧 root revision/retrievals/rights/materialization/selectors/generated_at/status/content_tier 及全部 legacy bytes 保全。现普通 arXiv vN、journal DOI／main+SI、Nature cookie、offline replay 回归保留并实际运行。 |
| 身份／对应负向 | originating ID 不符、两 metadata 不同、缺 correspondence／reviewed 非 true、缺引用 evidence、DOI／声明版本／package 版本／批准 URL／audit URL 不符均拒绝；包括四份 grant 同步改坏的案例。 |
| 安全／履约负向 | 缺自己的 grant、scope 未 allow、package.source_version 缺失／错误、inventory 漂移、未声明 SI、非 HTTPS／query／fragment／userinfo（含空用户名）、错误 requested／错误或外域 resolved 均拒绝；Nature 特例不得适用于 synthetic publisher。 |
| 缺声明／失败不写 | 保留 publisher 声明却移除整个 manifest supplement、即使无本地 PDF，两 validator 报 DECLARATION_MISSING；builder 负向以调用前 snapshot 断言全部 capsule bytes 不变、无 derived 写入。fixture fetch 设为报错，确保无真实采集。 |

若三文件不能闭合对应与安全保全，停止回 planner，不增加第四生产文件、adapter、crawler、全局 schema、依赖、workflow、storage 或 acquisition 框架；demo／coverage 现生产路由已按 representation 工作，禁止修改它们。

## 4. 文件责任与后续验证（File Responsibility and Planned Verification）

手写输入仅 C 的 publisher_pdf 声明与 nested allowance、A/K 本 UID 的新表示／真实核验／必要 summary，以及本报告／ledger；snapshot 保持一致。R 恰新增四份 pdf-supplement 文件：真实原 PDF 不改，NOTICE 自包含实际署名／题名／DOI／正式源／©ACL／可见独立信用、许可链接、原件未修改与 paged text/selectors 有损转换说明及完整 BY4 法条。完整法条复用只读 raw_data/licenses/cc-by-4.0.md，不创建／修改 raw license；同路径 NOTICE 相等不代替独立内容审核。

R 旧 source／normalized／root selectors／NOTICE／README／files.jsonl 与 root revision/retrievals/rights/materialization/generated_at/status/content_tier、source_version 键缺省和 A 的旧 gate/classification/evidence/v2 扩展事实保留；新增 inventory／local_bytes 仅反映实际新文件。K 仅在实际核验后以 pdf_supplement／publisher selected_version 表达新目标，不以 C 的 null 推翻旧 v2，也不把正式 PDF完整等同旧源包全部获许可。

generated_paths 中 00_inputs／01_ontology 已逐文件展开；其余受控 patterns（controlled patterns）仅现 generator 必需范围。语义变化只为现 ALCE 来源页及两 candidate 的 evidence／rights 链，其余只允许 build identity／inventory／依赖机械传播，不新增 selection、scientific assertion、collector 判断或 admission。未解释的无关重写立即停线，不手写派生物掩盖错误。

发布启动合同后才实施／作唯一正式 PDF GET。实际取得后按 05 核总页数、开中尾至少三页、主文／正式 A–I 附录／结尾、四图／关键表与首中末 selectors；具体缺页、失败页、图内／数学／prompt 损失如实列出。artifact complete 与 extraction partial 可以共存；body_quality_verified 不代表无损、旧 source 完成或 trusted，不默认 OCR 或全图线性化。

未来先 python tests/test_pdf_supplement.py 的最小离线回归，再当前 head 的 make test；ALCE 消费输入变化后 make demo、make validate、make reproducibility、python scripts/validate_materialization_completeness.py、python scripts/audit_non_repo_coverage.py 只读对账，并报告实际六维 before→after／检索／差异／未决。这里都是计划命令，本轮 tests_actually_run=[]，没有结果。

独立门控（independent gate）按 05§8.1：非作者 evaluator 锁实际 exact head/base，分别判需求满足、agentic 判断与证据链、核心质量及 overall PASS／FAIL；本批均 pending，适用 CI 同样 pending。CI／报告不替代 PASS；任一相关变化重新评估，满足后正常 merge 回 work，不沿用 PR23 PASS。

## 5. 停线与明确未做（Stop Conditions and Explicit Non-results）

唯一 URL 实际失败／非 PDF／身份或出版版本不符、正式附录缺失或提取失败，记录 arxiv:2305.14627 的具体 unresolved 与最小 next action；不能公开则记录 public_persistence_decision，不冒称网络失败。不得自动换 bare latest、另一版、旧 v2、作者仓库 PDF、SI 或引用网络。base 移动影响同输入／生成物、同 UID 另一 writer、对应／许可无法闭合、需改 source 身份／type、移删旧内容或扩到禁区，整个后继停止并回 planner。

本轮已全文读 startup planner 与八份计划，并只读核 C／R metadata／manifest、K summary／本 UID、A 本 UID 既有对应证据；仅 apply_patch 写本报告与 branch-ledger，PR23 完整报告本身未改。台账移 PR23 至 incorporated，保全既有字段并登记其精确终审／CI／merge，active 改 PDF06；PR/head 保持 null。

本轮未网络／正文 GET、未取得新原件、未实现接缝／测试、未写 raw／capsule／代码／生成物、未跑 tests／validators／generator、未 Git／PR 写入、未自评 PASS、未进入 work／main。未完成 P4/P5、未晋升 trusted、未关闭 issue、未删移内容／分支、未强推或改写历史。新 response／时间／bytes／页数／作者核验仍 null，等待主线发布启动合同后执行。

---
phase: P3-PDF-06
status: materialized_pending_exact_pair_evaluation_and_CI
base_sha: a3dbb1c87db2875c5354cc773199af453d2df7df
coverage_summary: {"collection_records":215,"non_repo_total":131,"github_repo_excluded":84,"reported_content_tier_counts":{"excerpt_capsule":23,"full_text":97,"metadata_capsule":11},"source_type_counts":{"arxiv":73,"biorxiv":2,"blog":10,"industry":2,"journal":11,"methodology":7,"paper":2,"standard":24},"original_artifact_counts":{"complete":51,"metadata_only":13,"partial":4,"unknown":63},"text_extraction_counts":{"complete":8,"partial":58,"unavailable":13,"unknown":52},"action_bucket_counts":{"access_restricted":9,"author_manuscript_fetch":2,"complete_verified":8,"html_article_snapshot":11,"identity_or_version_ambiguous":3,"needs_boundary_verification":51,"ocr_assessment":35,"parser_only":6,"public_persistence_decision":4,"standard_spec_fetch":2},"public_redistribution_counts":{"allow":33,"block":65,"unknown":33},"content_inspected_full_text":59,"structure_only_full_text":38,"locally_persisted_complete":8,"knowledge_candidate_sources":30,"knowledge_trusted_sources":0,"knowledge_sources_without_demo_claims":101,"unresolved_sources":123}
---

# P3-PDF-06 — ALCE 正式出版 PDF 表示：执行合同与结果

```yaml
execution_contract:
  plan_id: nonrepo-materialization-main-convergence-260916
  phase: P3-PDF-06
  status: materialized_pending_exact_pair_evaluation_and_CI
  base_branch: work/v0-meta-kb-initialization-demo-260910
  base_sha: a3dbb1c87db2875c5354cc773199af453d2df7df
  implementation_branch: codex/p3-pdf-06-alce-publisher-260917
  head_sha: null
  target_branch: work/v0-meta-kb-initialization-demo-260910
  pull_request: 24
  startup_head: ad444013963c0937820a3fde4659e80091dcde6b
  startup_published_at: '2026-09-17T10:40:27Z'
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
  retrieval_attempts:
    - requested_url: https://aclanthology.org/2023.emnlp-main.398.pdf
      resolved_url: https://aclanthology.org/2023.emnlp-main.398.pdf
      started_at: '2026-09-17T10:41:07Z'
      completed_at: '2026-09-17T10:41:32Z'
      http_status: 200
      content_type: application/pdf
      bytes: 481920
      redirects: 0
      result: sole_approved_original_acquired_unmodified
  body_http_status: 200
  retrieved_at: '2026-09-17T10:41:32Z'
  bytes: 481920
  actual_page_count: 24
  authors_verified_from_new_original: [Tianyu Gao, Howard Yen, Jiatong Yu, Danqi Chen]
  tests_actually_run:
    - command: /tmp/llm-wiki-ci-312-260916/bin/python -B tests/test_pdf_supplement.py
      result: final_45_tests_OK
      scope: code_executor_offline_regressions_before_real_packaging
    - command: make test PYTHON=/tmp/llm-wiki-ci-312-260916/bin/python
      result: 208_tests_OK
      scope: main_agent_code_regression_before_real_packaging_not_final_CI
    - command: make test PYTHON=/tmp/llm-wiki-ci-312-260916/bin/python
      result: 208_tests_OK
      scope: final_local_after_packaging_demo_and_ledger_reconciliation
    - command: make validate PYTHON=/tmp/llm-wiki-ci-312-260916/bin/python
      result: raw_materialization_docs_demo_release_all_pass_zero_errors
      scope: final_local_after_packaging_demo_and_ledger_reconciliation
    - command: /tmp/llm-wiki-ci-312-260916/bin/python scripts/audit_non_repo_coverage.py
      result: PASS_215_collection_131_nonrepo_84_repo_excluded
      scope: final_local_readonly_coverage_reconciliation
    - command: existing_replay_pdf_supplement_twice_with_fetch_bytes_and_prepare_capsule_forbidden
      result: 49_files_byte_identical_in_each_run
      scope: ALCE_strict_offline_replay_not_full_make_reproducibility
    - command: make demo PYTHON=/tmp/llm-wiki-ci-312-260916/bin/python
      result: PASS_build_llm_wiki_v0_4e541384e82b1271
      scope: correction_after_final_rights_input_freeze
    - command: make reproducibility PYTHON=/tmp/llm-wiki-ci-312-260916/bin/python
      result: PASS_four_checks_of_169_files_byte_identical_exit_0
      scope: corrected_tree_committed_full_demo_compiler_only_and_readonly_validation
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

启动时 K summary 的快照为215=131+84，original complete=50、text partial=57、strict／locally persisted complete=8、unresolved=123；没有预测 ALCE after。报告 frontmatter 在实际物化与复算后同步当前 K，启动六维 before 保留在第2节及K完整历史对象。

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

以下是 startup 时批准的三生产文件最小接口；启动时尚未改代码，后续实际实现与纠偏见第7节：

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

本节末两段记录 startup commit 时刻的历史状态；后续实际执行按第 6 节起追加，不将启动时的未执行描述当作当前状态。

唯一 URL 实际失败／非 PDF／身份或出版版本不符、正式附录缺失或提取失败，记录 arxiv:2305.14627 的具体 unresolved 与最小 next action；不能公开则记录 public_persistence_decision，不冒称网络失败。不得自动换 bare latest、另一版、旧 v2、作者仓库 PDF、SI 或引用网络。base 移动影响同输入／生成物、同 UID 另一 writer、对应／许可无法闭合、需改 source 身份／type、移删旧内容或扩到禁区，整个后继停止并回 planner。

本轮已全文读 startup planner 与八份计划，并只读核 C／R metadata／manifest、K summary／本 UID、A 本 UID 既有对应证据；仅 apply_patch 写本报告与 branch-ledger，PR23 完整报告本身未改。台账移 PR23 至 incorporated，保全既有字段并登记其精确终审／CI／merge，active 改 PDF06；PR/head 保持 null。

本轮未网络／正文 GET、未取得新原件、未实现接缝／测试、未写 raw／capsule／代码／生成物、未跑 tests／validators／generator、未 Git／PR 写入、未自评 PASS、未进入 work／main。未完成 P4/P5、未晋升 trusted、未关闭 issue、未删移内容／分支、未强推或改写历史。新 response／时间／bytes／页数／作者核验仍 null，等待主线发布启动合同后执行。

## 6. 发布与实际取得（Published Contract and Actual Acquisition）

2026-09-17T10:40:27Z，startup ad444013963c0937820a3fde4659e80091dcde6b（仅两份启动文档）已 push 并发布 Draft PR #24，base 保持 a3dbb1c87db2875c5354cc773199af453d2df7df。启动文档校验实际为 60 Markdown／5 YAML examples／80 relative links、errors=0，git diff --check 通过；这不是正文／代码验收。

之后才对唯一批准 URL 作一次普通 HTTPS GET，10:41:07Z 开始、10:41:32Z 完成，HTTP 200、application/pdf、481920 bytes、无重定向、resolved 与 requested 相同。HTTP Date=10:41:10 GMT 是服务器响应日期，实际 retrieved_at 使用完成时间。未 GET metadata／许可／旧 v2／作者仓库／SI，未重导或编辑原 PDF。pdfinfo 核 24 页，p1 印刷页 6465、p24 印刷页 6488，实际四作者与 ©2023 Association for Computational Linguistics 在 p1；时间与 bytes 是本次响应，不沿用历史观察。

主线用 pypdf 逐页诊断标题／图表／字符及正文，亲读 p1／2／12／14／17／24 原生文字，渲染亲看物理 p1／4／12／16／24；核四图 Figure 1–4、Tables 1–31、p14–17 A–I 和 p24 Table31／第三条 ground-truth claim 的真实尾界。独立内容 reader 另外审读完整 24 页和对应图表，具体结论待其完整报告后登记。尝试 pdftotext 时环境无此命令（未执行抽取或写入），使用现有 pypdf 及可用 pdftoppm 完成只读核验，无安装新依赖。

代码 executor 仅获得合同中三生产文件与一个现有测试文件的写权限；主线负责原件 GET、报告／台账与最终集成。此时实现、包装、after 六维、离线重放、最终测试、独立终审与当前 CI 均未完成，不预写 PASS。

## 7. 实际内容判断与最小接口（Content Judgment and Minimal Seam）

主线已全文阅读独立内容 reader 的 128 行报告，采用其逐页全文与 16 个实际渲染页证据；报告误把 manifest 列为四新增文件之一的清单已退回并改为 document.pdf／document.txt／selectors.jsonl／NOTICE.md，既有 root manifest 仅更新。未因脚本非空／页数便作完整判断，也未将 reader 的内容判断冒充最终 evaluator。

所选正式原件的 p1–9 包含摘要与正文至 §8 Conclusion；p10–13 为 Limitations／Acknowledgments／References；p14–17 为 A–I，p18–20 为全结果表19–21，p21–22 为提示词表22–29，p23–24 为例示表30–31，末尾为表31第三条 ground-truth claim、表底线与页码6488。4图、表1–31、实际数学条件及提示词均在场。旧 v2 source/sections/appendix.tex:253、255／258／260 的 Open-source Models 标题／三段，以及 source/tables/asqa_full.tex:74、qampari_full.tex:73、eli5_full.tex:74 的 Stable Beluga2 三行，在正式 PDF 中没有对应；正式 G.6 后直接 H/I、三全结果表止于 LLaMA2-70B-Chat。这是版本边界，不删旧历史、不从旧源猜补正式表示。

新原件覆盖 complete，但 native extraction 为 partial：Figure1–3 的箭头／图标／色彩／引用拓扑和 Figure4 三面板曲线几何／坐标映射未线性化；主要图内标签并未全丢。多层表头／分组／粗体／stddev 对齐、公式上下标／集合布局、双栏／页脚阅读顺序、prompt和例示的颜色角色不保真。p20表21的 `(2.w)`、NLI prompt 的空 `{}`、`volumn` 均为原件已有字面量，保留而不伪报抽取错误。无需以默认 OCR 或无损图面转换作本批退出门槛；严格完整消费仍 false，不提升 trusted。

新表示有既有 ACL 2016后材料 BY4 政策及正式作品对应证据，不重新 GET 许可；R 旧 bounded_acl_article_content_correspondence 的 false 仍指完整旧源包。主线准许有界包装正式 PDF：保留四作者／©ACL／EMNLP2023、真实源／DOI、p10 Princeton/Surge AI讨论者与资助信用，以及表30–31十段各100空白单元的有限外部检索例示及现有标题／byline。NOTICE明确不把例示改列为作者原创新闻，不宣称外部网站整篇、代码、数据、权重、模板或旧扩展的一般许可；保留完整原件，不为有限例示递归 GET。完整署名、信用、具体损失与完整 BY4 法条均落到新增自包含 NOTICE。

实际 plain 原文 L3–9 为提前抽出的出版页脚／题名／作者单位，L11–39 才是连续父摘要；主线和 reader 分别核原文与图面后，使用现有 primary_excerpt={start_line:11,end_line:39}，不改 consumer。唯一父摘要 source=source:51388aa8e2e8587f、evidence=evidence:4527dd12000fe21f、claim=claim:bed2f056ecd73c69；另一 collector assessment claim=claim:9a3b21da11a96956 的判断与文字不变。实际 generator 输出待后续确认，不预报引用字面完全不变。

代码 executor 已只改批准的三生产文件／一个测试文件并停写；主线读完其实际 diff。publisher 声明优先于普通 arXiv vN，声明／四处 grant 的 reviewed 均严格 bool true，避免 Python `True == 1` 使单侧错误声明通过；绑定既有审计的 UID、DOI、批准 URL 与 checked_at。普通 arXiv／journal／Nature 既有边界保留，无 ALCE／DOI／域名白名单，无 workflow、依赖、默认获取或 demo／coverage 改动。

测试纠偏有实际记录：首轮43项／1 failure 是新增测试把 legacy inventory 检查错归给 child-only PDF validator；修正测试职责后44项通过，builder inventory拒绝与失败不写入未放松。随后主线指出 capsule 单侧 reviewed=1 会与 True 被 mapping equality 视同，executor 补双声明各自严格类型及四方 grant 单侧反例，最终45项全部通过。主线再跑 make test 得4＋20＋6＋13＋88＋45＋2＋30＝208项通过。独立 evaluator 正只读预审代码，未最终批准本PR；实际包装、重放和最终冻结 head 的 gate 继续执行。

## 8. 物化结果与离线消费（Materialization and Offline Consumption）

包装 executor 完成后停写，主线读取新增 NOTICE／C grant 和 K 当前内容核验，接手串行集成。独立代码预审另外复跑45项通过且未发现阻塞，但尚非冻结提交的最终三维审核。

| 实际物化指标 | 结果 |
| --- | --- |
| 新原 PDF | 481920 bytes／24物理页；与本次下载逐字节相同 |
| native 未 footer | 97453字符／2103行／98129 UTF-8 bytes |
| 入库 TXT | 101157字符／2115行／103297 bytes；有且仅有一个履约 footer |
| 新 NOTICE | 28440 bytes；主线确认完整现有 CC BY4 法律资产为逐字节原样后缀 |
| 新 selectors | 24个 page 定位；首／中／末 p1／12／24，旧95条root selectors不变 |
| capsule inventory | 48条／1147816 bytes；另有manifest本身，共49个实际文件 |
| 父摘要 | primary 连续L11–39；既有consumer实际返回L11–16，无出版页脚／题名污染 |

主线使用现 replay_pdf_supplement，fetch_bytes／prepare_capsule 均 mock 为立即失败，连续两次实际重放；每次49个胶囊文件全部字节相同。不是调用未修改的默认 arXiv acquisition，也不是未验证的“离线”口头声明。此前逐字节与 BASE 比较43个旧非 snapshot 文件均未变；全部旧 manifest 字段（只排除允许的local_files/local_bytes）原样保全，source_version键仍缺省。新4文件与source-metadata之外无旧内容替换，原GET PDF未重导。

随后仅调用既有 rebuild_registry／write_indexes_and_audit，215条聚合统一沿用确定性时间2026-09-16T04:30:26Z，不把这个时间写成本次GET时间。真实R/K全局汇总、生成消费链及最终tests/validate/coverage将串行对账；全量四轮reproducibility由最终提交的CI运行并读实际日志后登记，不预称通过。

make demo 已实际 exit0，包含 build-demo／validate-demo／build-wiki／validate-wiki；只有现有 ALCE 父摘要的来源／证据／claim链按新表示重绑。72个claim与evidence UID集合保持；对象级比较仅 claim:bed2f056ecd73c69 与 evidence:4527dd12000fe21f 改变，collector评估对象完整未变。字面引用有1处对象变化：新plain保留原断行 `halluci- nation.`，以及 `citations,`（旧TeX派生为 `hallucination.`／`citations ,`）。不手写“纠正”extractor文本，不虚称literal完全相同；这是同一父摘要的表示变化，不新增科学断言或trust。

index与registry各215身份/成员全等，只有ALCE一行变化，其余214对象与BASE全等。36个source页面中，仅ALCE具有消费语义变化；另外35页由主线解析frontmatter后逐项核对，除provenance.build_id外其余frontmatter及整页body与BASE完全相同。其他生成差异必须限现generator依赖/发布inventory传播，不能把文件数当独立来源变更数。

新增TXT的29处尾随空格来自同一现有plain extractor的图内文本排版。git diff --cached --check 实际 exit2并指出这些位置；未将其写成绿色或手工trim破坏字节重放。普通手写／代码与其他派生路径的差异另行校验；最终完整range结果、严格重放与CI证据分别记录，样式诊断不替代内容判断。

## 9. 六维 After 与未决（After and Remaining Limits）

| 维度 | Before → 本批实际 After |
| --- | --- |
| 身份／版本 | 旧C/snapshot source_version=null、root键缺省均保留；目标从未记录版TeX改为显式publisher-vor:doi:10.18653/v1/2023.emnlp-main.398，仍同一arxiv UID/type/adapter。旧v2扩展不纳入正式表示。 |
| 原件覆盖 | unknown/unverified → complete/verified，仅正式24页主文/References/A–I/四图/表1–31/prompts/Examples；未获取独立SI、外部正文或旧扩展。 |
| 文本提取 | unknown/unverified → partial/verified；24页均有native文字，无整页/整节缺失，图形、表格、公式及色彩/阅读顺序损失见§7/NOTICE，不宣称无损。 |
| 本地持久化 | 旧44 inventory／95root selectors → 48 inventory／新增24page selectors、旧95不动；原PDF/TXT/NOTICE/selectors均入repo待最终push。两次49文件离线重放相同。fresh checkout=false、strict complete_target_consumable=false，非main远程验收。 |
| 公开再分发 | 旧root block及历史false保持；正式PDF独立allow，C/snapshot/manifest/R四方新package一致，具体DOI/URL/版权/实际credit/NOTICE绑定。不是源包整体allow。 |
| 知识准入 | 2个现有candidate保持；仅父摘要claim/evidence引用绑定改变，collector评估对象不变，没有新UID、claim、selection或trusted。 |

本UID仍 unresolved／ocr_assessment，含义是明确的有损派生边界，不表示正式原件未取得。精确消费可直接回看已保留PDF；只有具体需求才评估局部OCR、人工转写或parser，不作为本PR关闭前置。旧源包独立许可条件仍保留。全库P4两项包一致性问题、coverage在fresh main的历史对象依赖，以及P5/PR1真正进入main尚未完成；不由本批局部PASS豁免。

## 10. 对账、验证与最终关闭门控（Reconciliation, Validation and Closing Gate）

R/K账务 executor 在无generator运行时调用现collect_facts一次，真实48inventory、tracked/present=true、新PDF package valid/allow、24selectors及candidate2与当前文件一致。只刷新目标observed/限制/实际execution和全局summary：K其他130项、R其他107项完整对象与精确BASE全等；目标R旧字段/evidence前缀保留，K整条before与BASE全等。PR23 execution置入historical_p3_pdf_05_execution且同层全部旧history保留，可完整重构BASE execution，不重写历史为新事件。

复算K仍215=131+84：原件complete 50→51、unknown64→63；text partial57→58、unknown53→52；inspected58→59、structure-only39→38；needs_boundary_verification52→51、ocr_assessment34→35。严格完整8／unresolved123／candidate来源30／trusted0，以及root allow33/block65/unknown33均不变。R独立表示由33main+5SI=38allow到34main+5SI=39allow，CC-BY4 35→36、BY-SA4 2和BY4 AND Apache2 1不变；不是root新增allow。

主线最终再次make test：208项全部通过。全库publication validator实际exit1：active_full_text103／audited108／blocked64／errors2；错误仍为arxiv:2404.16130和arxiv:2502.18864的既有package不一致，没有ALCE新错误。该全库门控并未PASS，不用新表示allow或当前PR的阶段判定放行既有root包；两错误按计划P4处理。

主线对BASE至当前候选的179个差异路径逐项匹配已发布allowed_paths，无越界文件或未跟踪文件；完整range git diff --check 实际exit2，恰29处只在新native TXT的尾随空格。排除此原生派生TXT的全部其他路径diff check为0，未把缩小范围结果冒充完整range通过。严格重放已证明这些字节由现extractor稳定产生。

最终make validate与coverage audit均已exit0：raw metadata215、manifest215；materialization warnings0/errors0；docs60篇、YAML例5、相对链接80、errors0；demo36 sources／189 objects／72 claims／72 evidence／135 pages、warnings0/errors0；release135 pages／72 claims／21 inputs／154 outputs、warnings0/errors0，build:llm-wiki-v0:45bd6c7288326476。coverage以215=131+84的实际台账PASS，并非131项均完整。

全量make reproducibility／clean checkout gate留给最终提交的CI实际执行，未声称本地运行该完整命令。exact head/base终审、最终CI、Ready／merge均未发生，PR保持Draft。最终结果将以该PR中锚定实际head的独立COMMENT和CI日志登记；如相关输入或base改变则重新审核，不在提交自身中填造自指head或预写PASS。

## 11. CI 实际失败与执行顺序纠偏（Observed CI Failure and Ordering Correction）

上述§10是第一次冻结前的实际本地结果，不是最终成功声明。首次冻结head e7e202c65ae5089f635a250af4f934b53c330646 / base a3dbb1c87db2875c5354cc773199af453d2df7df 的 CI [run 35215133030](https://github.com/thsno02/solid-octo-couscous/actions/runs/35215133030) / job105181705572实际失败：208项单元测试通过，但make reproducibility的committed_tree_replay发现已提交生成物过期，后续clean gate未运行。PR保持Draft，不用本地make validate通过替代重放门控。

根因是执行顺序，而不是workflow或跨平台正文随机变化。现有build_demo.py将selected PDF supplement的权利审计文件纳入构建身份；PR23已有AgentRxiv这类selected source，因此不是ALCE首次激活R输入。主线先make demo、随后R/K executor更新了materialization_rights_review.yaml，最终已提交build:llm-wiki-v0:45bd6c7288326476未反映最后R输入；CI同一输入重建得到build:llm-wiki-v0:4e541384e82b1271。R记录虽不改变其他来源语义，其字节仍是已声明构建输入。

纠偏路径：暂停独立evaluator对动态生成物的读取，冻结全部C/R/K/capsule/code输入，调用既有make demo重新生成，再执行本地完整make reproducibility；不手改生成物、不改变身份算法、不移除R输入、不修改workflow或跳过gate。修复后的精确head重新push、重新CI及独立终审；此前head不能合并，新增验证结果待实际完成后登记。

纠偏实际结果：make demo exit0，得到与首次CI重建相同的build:llm-wiki-v0:4e541384e82b1271，底层demo身份为build:v0-meta-kb-260910:7e46969e84b6efca。本地随后make reproducibility exit0：committed_tree_replay、full_demo_replay、compiler_only_replay、read_only_validation四轮各169文件逐字节相同，内含make validate全层0 errors。首次冻结后的修正只涉及151个必要生成文件及本报告／ledger；源材料、C/R/K、index/registry、production/test/workflow全部不变，claim/evidence实体及源页body语义不变。这是本地修复证据，不能替代修正head的远端CI和新独立结论。

首次独立三维FAIL已原文发布为[agent COMMENT 5235028835](https://github.com/thsno02/solid-octo-couscous/pull/24#pullrequestreview-5235028835)：需求FAIL、agentic PASS、核心质量FAIL；没有隐藏失败或把审计者当实现作者。修正后保持Draft，等待新的exact-pair三维终审与适用CI，原先§10的初次build ID及pending状态只属历史快照。

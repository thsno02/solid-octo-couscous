---
phase: P3-PAGE-BODY-02
base_sha: 6705771e53414b941541ed77d7b88aefa89caaa4
status: local_validation_complete_pending_exact_pair_review_and_CI
coverage_summary_state: actual_frozen_K_summary_confirmed_by_handoff
coverage_summary: {"collection_records":215,"non_repo_total":131,"github_repo_excluded":84,"reported_content_tier_counts":{"excerpt_capsule":23,"full_text":97,"metadata_capsule":11},"source_type_counts":{"arxiv":73,"biorxiv":2,"blog":10,"industry":2,"journal":11,"methodology":7,"paper":2,"standard":24},"original_artifact_counts":{"complete":52,"metadata_only":12,"partial":4,"unknown":63},"text_extraction_counts":{"complete":8,"partial":60,"unavailable":12,"unknown":51},"action_bucket_counts":{"access_restricted":8,"author_manuscript_fetch":2,"complete_verified":8,"html_article_snapshot":11,"identity_or_version_ambiguous":3,"needs_boundary_verification":51,"ocr_assessment":36,"parser_only":6,"public_persistence_decision":4,"standard_spec_fetch":2},"public_redistribution_counts":{"allow":33,"block":65,"unknown":33},"content_inspected_full_text":59,"structure_only_full_text":38,"locally_persisted_complete":8,"knowledge_candidate_sources":30,"knowledge_trusted_sources":0,"knowledge_sources_without_demo_claims":101,"unresolved_sources":123}
execution_contract:
  plan_id: nonrepo-materialization-main-convergence-260916
  phase: P3-PAGE-BODY-02
  status: local_validation_complete_pending_exact_pair_review_and_CI
  base_branch: work/v0-meta-kb-initialization-demo-260910
  base_sha: 6705771e53414b941541ed77d7b88aefa89caaa4
  target_branch: work/v0-meta-kb-initialization-demo-260910
  batch_branch: codex/p3-page-body-02-260917
  pull_request: 26
  startup_head_sha: bd6c7382c82e6f38633c623ee67901b17a4ccc1d
  startup_published_at: '2026-09-17T14:19:51Z'
  amendment_head_sha: b8ebf2024d39e484d2ae8b542cf03b6818b785c7
  head_sha: null
  final_head_sha: null
  head_binding: final_commit_and_exact_base_via_PR_review_and_CI_records_no_self_referential_SHA
  prerequisite_pull_request: 25
  prerequisite_merge_commit: 6705771e53414b941541ed77d7b88aefa89caaa4
  source_uids: ["methodology:linkml-schema-first", "vocabulary:schema.org"]
  adapter_family: generic_web_or_document_v2
  action_bucket: html_article_snapshot
  representation: dated_html_response
  canonical_ids: {"methodology:linkml-schema-first": "METHODOLOGY-LINKML", "vocabulary:schema.org": "SCHEMA.ORG"}
  sole_body_get_candidates: {"methodology:linkml-schema-first": "https://linkml.io/linkml/", "vocabulary:schema.org": "https://schema.org/docs/schemas.html"}
  selected_response_versions: {"methodology:linkml-schema-first": "dated-response-2026-09-17T14:20:17Z", "vocabulary:schema.org": "dated-response-2026-09-17T14:20:15Z"}
  selected_version_kind: recorded_single_page_response_snapshot_not_release_or_deployment_commit
  content_selectors: {"methodology:linkml-schema-first": "article#furo-main-content", "vocabulary:schema.org": "article#mainContent"}
  derived_exclude_selectors: {"methodology:linkml-schema-first": ["a.headerlink"], "vocabulary:schema.org": []}
  original_uid_boundaries: unresolved_no_whole_UID_complete_claim
  production_code_changes: four_explicit_paths_implemented_finite_consumer_method_guards_no_producer_renderer_or_facts_changes
  body_acquisition: two_sole_approved_GETs_originals_retained_in_worktree_final_implementation_not_pushed_or_merged
  staged_response_root: /tmp/llm-wiki-page-body-02-bzczN1
  actual_responses:
    methodology:linkml-schema-first:
      requested_url: https://linkml.io/linkml/
      resolved_url: https://linkml.io/linkml/
      started_at: '2026-09-17T14:20:15Z'
      finished_at: '2026-09-17T14:20:17Z'
      http_status: 200
      redirects: 0
      verified_TLS: true
      content_type: text/html; charset=utf-8
      content_encoding: absent
      bytes: 55141
      entity_revision: sha256:93a9f00b0006695dab8f1bde801a40e36eed8c236c4c839aff645bec38b5dc6c
    vocabulary:schema.org:
      requested_url: https://schema.org/docs/schemas.html
      resolved_url: https://schema.org/docs/schemas.html
      started_at: '2026-09-17T14:20:15Z'
      finished_at: '2026-09-17T14:20:15Z'
      http_status: 200
      redirects: 0
      verified_TLS: true
      content_type: text/html
      content_encoding: gzip
      transport_bytes: 4500
      bytes: 12007
      entity_revision: sha256:b5be08b7c47762f190c539e7dcf6ba04c60507c310af960578f2f97623ee5a0d
      transport_sha256: fad84bc7594cbb77a61e06a2dba1d3dbffd096936c4b2bf30939411622c9965c
      decoding: mechanical_gzip_decode_same_HTTP_response_no_second_GET
  license_decisions: {"methodology:linkml-schema-first": "Apache-2.0 AND MIT", "vocabulary:schema.org": "CC-BY-SA-3.0 AND Apache-2.0"}
  license_basis: observed_official_direct_grants_and_matching_embedded_templates
  raw_publication_admission: scoped_allow_four_way_packaged_worktree_not_global_gate_or_final_review_PASS
  startup_checkpoint:
    status: startup_not_acquired
    pull_request: null
    startup_head_sha: null
    head_sha: null
    selected_response_versions: {"methodology:linkml-schema-first": null, "vocabulary:schema.org": null}
    body_acquisition: not_executed
    production_code_changes: none_working_hypothesis_requires_observed_DOM_confirmation
    after: null
  amendment_checkpoint:
    head_sha: b8ebf2024d39e484d2ae8b542cf03b6818b785c7
    status: response_observed_narrow_amendment_pending_implementation
    production_code_changes: authorized_pending_implementation
    raw_publication_admission: pending_license_fulfillment_and_four_way_packaging
    after: null
  second_narrow_amendment:
    reason: observed_CLAIM_EVIDENCE_METHOD_MISMATCH_on_correct_derived_reading_excerpt
    publication_record: actual_PR26_body_update_confirmed
    published_at: '2026-09-17T15:24:39Z'
    publication_authority: GitHub_PR26_updated_at
    published_remote_head_sha: b8ebf2024d39e484d2ae8b542cf03b6818b785c7
    published_base_sha: 6705771e53414b941541ed77d7b88aefa89caaa4
    implementation: two_paths_implemented_code_frozen_focused36_tests_exit0_final_review_pending
    additional_code_paths:
      - experiments/v0_meta_kb_initialization_demo_260910/pipeline/rights_propagation.py
      - experiments/v0_meta_kb_initialization_demo_260910/pipeline/test_rights_propagation.py
    supported_exact_method: deterministic-derived-reading-excerpt
    supported_representations: [retained_html_response, retained_git_text_sources, tex_reading_view]
    guards: exact_producer_transformation_selected_source_and_current_manifest_consumer_binding_existing_rights_and_evidence_gates_preserved
    frozen_source_inputs: C_R_K_capsules_and_carriers_unchanged_no_new_GET
  after:
    methodology:linkml-schema-first:
      whole_UID_original_coverage: unknown_boundary_unresolved
      text_extraction: partial_observed_li_p_blockquote_list_hierarchy_loss
      semantic_boundary_verified: false
      action_bucket: needs_boundary_verification
      resolution: unresolved
      inventory_files: 9
      inventory_bytes: 168130
      selectors_current_and_total: [6, 170]
      public_redistribution: scoped_allow_Apache_2_AND_MIT
      knowledge: two_existing_candidate_chains_rebuilt_derived_source_assertion_and_metadata_assessment_distinct_no_trusted_promotion
      complete_target_consumable: false
    vocabulary:schema.org:
      whole_UID_original_coverage: unknown_boundary_unresolved
      whole_UID_text_extraction: unknown_partial_check
      action_bucket: needs_boundary_verification
      resolution: unresolved
      inventory_files: 10
      inventory_bytes: 121805
      selectors_current_and_total: [5, 39]
      public_redistribution: scoped_allow_BY_SA_3_AND_Apache_2
      knowledge: no_demo_claims_no_new_selection
      complete_target_consumable: false
  local_validation:
    pre_fix_tests: 217_passed_before_derived_method_fix_not_current_fix_verification
    tests: 223_passed_after_fix_Python_3_12_13_including_93_integrity_tests_and_12_rights_tests
    focused_method_tests: 36_passed_rights12_evidence4_excerpt20
    materialization: metadata215_manifests215_hashes3205_selectors25869_errors0_exit0
    two_UID_rights: active2_audited108_errors0_blocks0_exit0
    strict_offline_replay: two_runs_each_UID_bytes_identical_no_fetch_prepare_or_directory_clear
    public_global_gate: exit1_active104_audited108_errors2_blocks64_inherited_not_PASS
    aggregate: records215_hashes3205_local_bytes265851572
    K_freeze: actual_handoff_confirmed_one_facts_run_two_observed_exact_other129_items_equal_BASE
    historical_failed_demo: exit2_validate_demo_one_CLAIM_EVIDENCE_METHOD_MISMATCH_sources36_claims72_evidence72_pages51_resolved_by_finite_method_guard_fix_and_full_rebuild
    make_demo: exit0_sources36_claims72_evidence72_Wiki135pages_357typed_links_3context_packs_errors0_warnings0
    demo_build_id: build:v0-meta-kb-260910:4b5151f25e589cb4
    Wiki_build_id: build:llm-wiki-v0:bdc4c9116985ab25
    Wiki_inputs_and_outputs: [21, 154]
    registry_semantic_reconciliation: members215_YAML_JSONL_equal_only_two_targets_changed_other213_objects_equal_BASE
    generated_semantic_reconciliation: source36_evidence72_claim72_members_equal_BASE_only_LinkML_source_and_source_evidence_b0f_and_source_claim583_changed_other35_sources_71_evidence_71_claims_and_collector_pair_equal_BASE_no_Schema_selection
    fresh_candidate_scoped: exit0_before_rights_method_fix_two_UID_source_packages_only
    coverage_audit: exit0_frozen_K_and_report_summary_consistent_Tpartial60_unknown51_source_summary_gate_only_not_final_PASS
    make_validate: exit0_raw248YAML_metadata215_errors0_materialization215_manifests215_hashes3205_selectors25869_warnings0_errors0_docs62markdown_5examples_86links_errors0_demo36sources_189objects_72claims_72evidence_135pages_errors0_Wiki21inputs_154outputs_errors0
    reproducibility: exit0_committed_tree_replay_full_demo_replay_compiler_only_replay_read_only_validation_each169_generated_files_byte_identical
    changed_paths_contract_check: actual194_changed_paths_out_of_contract0_deletions0_untracked0
    derived_method_code_review: non_author_frozen_diff_no_specific_new_blocker_not_final_pair_three_dimension_PASS
  startup_only_writes:
    - docs/plans/260916-corpus-completion-main-convergence/p3-page-body-02.md
    - docs/plans/260916-corpus-completion-main-convergence/branch-ledger.yaml
  allowed_paths:
    - scripts/materialize_all_sources.py
    - tests/test_materialization_integrity.py
    - experiments/v0_meta_kb_initialization_demo_260910/pipeline/rights_propagation.py
    - experiments/v0_meta_kb_initialization_demo_260910/pipeline/test_rights_propagation.py
    - docs/plans/260916-corpus-completion-main-convergence/p3-page-body-02.md
    - docs/plans/260916-corpus-completion-main-convergence/branch-ledger.yaml
    - raw_data/methodology/LinkML Schema First Knowledge Modeling/metadata.yaml
    - raw_data/standard/Schema.org Vocabulary/metadata.yaml
    - raw_data/audits/materialization_rights_review.yaml
    - raw_data/audits/non_repo_materialization_coverage_2026-09-16.yaml
    - docs/materialization-rights-audit.md
    - raw_data/licenses/linkml-page-body-02-260917.md
    - raw_data/licenses/schemaorg-page-body-02-260917.md
    - materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/source/specification.html
    - materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/normalized/document.md
    - materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/normalized/selectors.jsonl
    - materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/manifest.yaml
    - materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/README.md
    - materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/source-metadata.yaml
    - materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/NOTICE.md
    - materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/history/NOTICE-before-page-body-02.md
    - materialized_sources/corpus/vocabulary-schema.org--c8b3dc95/source/specification.html
    - materialized_sources/corpus/vocabulary-schema.org--c8b3dc95/source/specification.html.gz
    - materialized_sources/corpus/vocabulary-schema.org--c8b3dc95/normalized/document.md
    - materialized_sources/corpus/vocabulary-schema.org--c8b3dc95/normalized/selectors.jsonl
    - materialized_sources/corpus/vocabulary-schema.org--c8b3dc95/manifest.yaml
    - materialized_sources/corpus/vocabulary-schema.org--c8b3dc95/README.md
    - materialized_sources/corpus/vocabulary-schema.org--c8b3dc95/source-metadata.yaml
    - materialized_sources/corpus/vocabulary-schema.org--c8b3dc95/NOTICE.md
    - materialized_sources/corpus/vocabulary-schema.org--c8b3dc95/history/NOTICE-before-page-body-02.md
    - materialized_sources/index.yaml
    - materialized_sources/README.md
    - source_registry/registry.yaml
    - source_registry/registry.jsonl
    - source_registry/README.md
    - raw_data/audits/materialization_completeness_2026-09-10.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/materialization_snapshot.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/selected_sources.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/wiki_build_request.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/page_plan.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/01_ontology/meta_kb_ontology.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/01_ontology/schema_bindings.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/README.md
  generated_paths:
    - materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/normalized/document.md
    - materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/normalized/selectors.jsonl
    - materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/manifest.yaml
    - materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/README.md
    - materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/source-metadata.yaml
    - materialized_sources/corpus/vocabulary-schema.org--c8b3dc95/normalized/document.md
    - materialized_sources/corpus/vocabulary-schema.org--c8b3dc95/normalized/selectors.jsonl
    - materialized_sources/corpus/vocabulary-schema.org--c8b3dc95/manifest.yaml
    - materialized_sources/corpus/vocabulary-schema.org--c8b3dc95/README.md
    - materialized_sources/corpus/vocabulary-schema.org--c8b3dc95/source-metadata.yaml
    - materialized_sources/index.yaml
    - materialized_sources/README.md
    - source_registry/registry.yaml
    - source_registry/registry.jsonl
    - source_registry/README.md
    - raw_data/audits/materialization_completeness_2026-09-10.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/materialization_snapshot.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/selected_sources.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/wiki_build_request.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/page_plan.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/01_ontology/meta_kb_ontology.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/01_ontology/schema_bindings.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/README.md
  controlled_generated_patterns:
    - experiments/v0_meta_kb_initialization_demo_260910/02_entities/**
    - experiments/v0_meta_kb_initialization_demo_260910/03_evidence/**
    - experiments/v0_meta_kb_initialization_demo_260910/04_claims/**
    - experiments/v0_meta_kb_initialization_demo_260910/05_wiki/**
    - experiments/v0_meta_kb_initialization_demo_260910/06_evaluation/**
    - experiments/v0_meta_kb_initialization_demo_260910/07_review/**
    - experiments/v0_meta_kb_initialization_demo_260910/08_release/**
  path_constraints:
    audits: only_two_UIDs_true_summary_and_preserved_execution_history
    other_sources: other_213_source_objects_and_other_129_K_objects_unchanged
    legacy_root_document_and_selectors: read_only_byte_preserved
    notices: exact_old_NOTICE_copy_to_explicit_history_path_before_combined_current_NOTICE
    license_carriers: only_two_explicit_per_item_carriers_full_relevant_legal_texts_and_actual_attributions_after_rights_review_no_shared_text_change
    raw_admission: code_and_NOTICE_preparation_authorized_public_bytes_only_after_component_rights_closure
    generated_changes: existing_LinkML_selected_chains_and_necessary_global_identity_only_no_selection_strategy_change
    new_media_or_additional_history_paths: require_observed_objects_and_prior_exact_path_amendment
  explicitly_out_of_scope:
    - code_or_tests_outside_four_explicit_paths_producer_build_demo_evidence_validation_completeness_validator_dependencies_workflows_new_adapter_or_fetcher
    - full_LinkML_multi_page_docs_or_full_Schema_vocabulary_release_type_property_pages
    - recursive_fetch_theme_assets_external_works_or_media_without_exact_prior_amendment
    - shared_license_text_changes_carriers_outside_two_explicit_per_item_paths_or_old_history_replacement
    - original_UID_complete_verified_claims_count_redefinition_or_not_applicable_count_clearing
    - new_demo_selection_Schema_claims_trusted_promotion_or_other_source_semantic_changes
    - unrelated_dependent_artifacts_main_merge_issue_closure_or_Git_history_changes
  independent_evaluation: pending_actual_final_head_and_base_non_author_three_dimensions
  final_ci: pending_actual_final_head_and_base
---

# P3-PAGE-BODY-02 — 两份既有单页原响应的有界执行记录

## 当前执行结果与剩余门控（Current Results / Remaining Gates）

当前工作树已完成四个精确代码／测试路径、两 capsule、组合许可载体与旧 NOTICE 历史保全。第二窄修订公开后，rights 方法的有限 consumer guard 已实际实现并冻结；主线修复后223 tests及完整 demo／Wiki 重建 exit0，原方法集成阻塞已修复。LinkML 列表层级损失仍诚实 partial；完整重建不等于原 UID complete或最终交付，尚无 exact final HEAD 推送／合入。

C/R/K／capsules在方法修复及重建期间未再变；主线已核215成员、registry YAML／JSONL一致，仅两target记录变、其他213对象等BASE。默认coverage已exit0，217tests及源包fresh保留为修复前历史。现 `make reproducibility` 实际exit0，四阶段各169生成文件逐字节一致（byte-identical），内含正常 `make validate` 也exit0；具体范围见验证表。非作者代码复核完成、未发现具体新代码阻塞，但最终exact-head／base三维review与CI仍pending。主线194个changed paths合同核对为out_of_contract0／deletions0／untracked0；最终HEAD由PR记录绑定，base不变，不据本地验证自评最终PASS。

## 第二次窄修订：派生方法集成阻塞（Second Narrow Amendment / Derived-method Blocker）

历史首轮 `make demo` 实际exit2：36／72／72／51中间产物，validate-demo唯一 `CLAIM_EVIDENCE_METHOD_MISMATCH`，绑定 `claim:583280271287ef9c` → `evidence:b0f0f32b0b4cc957`。producer正确标真实新L24为derived／retained HTML／not-raw，旧rights硬编码raw expected产生错配。本节保留故障与先公开后修复的历史；现已按有限表示绑定修复并完整重建，不改证据装raw、删门控或简单放行两字符串，collector性质不变。

已全文读计划、预审、`/tmp/pr26-derived-method-execution.md` 及非作者代码复核。第二修订先于实现公开：PR26 updated_at=`2026-09-17T15:24:39Z`，当时远端head仍b8ebf202…／base6705771…，不是新commit。随后只改rights_propagation及同目录测试，358 additions／3 deletions；有限表示／精确transformation／selected-source与manifest consumer guard在evidence循环验证，standalone仍走rights，raw／已选PDF／collector及原evidence门控保持。最终聚焦36tests（12rights＋4evidence＋20excerpt）exit0；`/tmp/pr26-derived-method-code-review.md` 未发现具体新代码阻塞，其live-code风险结论不替代final exact-pair三维PASS。

只支持 exact `deterministic-derived-reading-excerpt` 与以下现有三类表示；evidence 与 selected source 的 representation 必须一致，current manifest 明确 opt-in，实际 local_path 必须等于 selected local_document／capsule 内声明 consumer，而非孤立 marker／任意文件：

| 现有 representation | manifest／chosen consumer 绑定 | 精确 producer transformation |
| --- | --- | --- |
| `retained_html_response` | binding=`dated_html_response` 或 `wiki_page_revision_set`；document／normalized_document=`normalized/document.md` | `Collector-derived static HTML structural text; excerpt is not a raw-source quotation.` |
| `retained_git_text_sources` | binding=`git_snapshot`；document／normalized_document=`normalized/document.md` | `Collector assembly of retained Git Markdown/YAML with line anchors and explicit local href routes; excerpt is not a raw-source quotation.` |
| `tex_reading_view` | enabled 严格true／profile=`conservative-v1`；view／document／normalized_document=`normalized/reading.md` | `Collector-derived static TeX reading view; excerpt is not a raw-source quotation.` |

保留 raw（含已选 PDF supplement）、collector scope-method 双向匹配、locator／excerpt／source refs、版本／revision／NOTICE／package／rights refs、candidate／trusted 等现门控。派生声明与 raw method 相矛盾、未知方法／表示／转换、source／manifest／consumer 错配、collector 偷换派生及 standalone derived 无 role／claim 时跳过 rights，均须拒绝。仅在 rights 模块复用已加载 manifest 与实际 capsule-local consumer，不增加 hash 防御层、反向循环 import 或完整 renderer 校验。

实际最小fixture覆盖三表示、HTML dated／wiki、raw／PDF／collector，及exact-method／表示／opt-in／TeX profile／consumer／transformation／standalone rights负例，原定位／文字／source refs／rights／scope／trusted拒绝保持。聚焦回归后主线只用现generator完整重建：36sources／72claims／72evidence；Wiki135pages／357typed links／3context packs，errors0／warnings0，21inputs／154outputs。实际demo build=`build:v0-meta-kb-260910:4b5151f25e589cb4`、Wiki build=`build:llm-wiki-v0:bdc4c9116985ab25`。该方法修补未改producer／当前摘句／两ID／collector判断／selection／trust；新身份传播不等于新知识。非作者代码复核、主线重建与最终pair终审是不同门控。

## 响应与执行前窄修订检查点（Historical Amendment Checkpoint）

本节保留 `b8ebf2024d39e484d2ae8b542cf03b6818b785c7` 修订时事实；“仅暂存／尚未改写／未 packaged／待授权”描述当时状态，当前实现与履约结果见本报告新结果段落。

PR #26 于 `2026-09-17T14:19:51Z` 发布，startup HEAD 为 `bd6c7382c82e6f38633c623ee67901b17a4ccc1d`，base 不变。之后只执行两个批准正文 GET，均 HTTP200、无重定向、TLS 已校验：LinkML 于 `14:20:15Z–14:20:17Z` 取得 55141B、`text/html; charset=utf-8`、无 Content-Encoding；Schema 于 `14:20:15Z–14:20:15Z` 取得 gzip wire 4500B、`text/html`，同一次响应机械解压为 12007B HTML，没有第二 GET。原件目前仅暂存 `/tmp/llm-wiki-page-body-02-bzczN1`，不是公开 repo 已持久化结果。

LinkML 新 entity revision 与旧 `93a9…` 相同；Schema 新 entity 为 `b5be08…`，不等于旧 `f62a65…`，不能因字节数相同宣称正文相同。Schema wire 实际 SHA256 为 `fad84b…`，独立于 entity revision；完整值见合同。提议 snapshot 版本仅为本次单页响应 `dated-response-2026-09-17T14:20:17Z`／`dated-response-2026-09-17T14:20:15Z`，不据此推 release 或部署 commit。当前 C/R/K 尚未改写，六维 before 和全库 summary 仍是原检查点，after 未产生。

现 DOM 分别观察到唯一正文 `article#furo-main-content`／`article#mainContent`，原“默认无新代码”假设因此修正为现接口的小接缝。已完整读 `/tmp/page02-minimal-code-plan.md`；本修订仅授权 `scripts/materialize_all_sources.py` 与 `tests/test_materialization_integrity.py`，不改 completeness validator（现调用既有 preflight 自然覆盖），不引入 fetcher／mode／adapter、UID／host 白名单、依赖或全局采集框架。

已完整读 `/tmp/page02-content-rights-review.md`：官方直接 grant 与实际嵌入模板对应支持 LinkML `Apache-2.0 AND MIT`（作者内容／Furo 2025.12.19 模板）及 Schema `CC-BY-SA-3.0 AND Apache-2.0`（文档／网站模板）的分范围组合，不是任选 OR。仍须履行完整法条、实际 copyright／归属、修改说明及四方包装，未 packaged、未宣称 public allow。本修订允许主线发布后并行小代码修复与 NOTICE／专属载体准备；新增依赖产物尚未生成，最终 CI／非作者评估仍待实际最终 HEAD／BASE。

## 原启动检查点（Historical Startup Checkpoint）

以下两段保留发布前原启动事实；其“本轮／当前／未 GET”只描述该检查点，不是上述实际响应后的现状。初始空 PR／HEAD、未获取与无代码工作假设另存于 frontmatter `startup_checkpoint`，无需重复整个旧合同。

本批采用有界增量（bounded increment）：为两个既有单页补存真实原 HTML、保真结构化消费和现接口的配对重放（paired replay），不把首页改称原 UID 的完整产品。PR #25 已正常合入 work；精确基线（exact base）为 `6705771e53414b941541ed77d7b88aefa89caaa4`，不是规划草案的未合入 HEAD 或旧 base。当前分支为 `codex/p3-page-body-02-260917`；本轮只准备上列两份启动文档，PR／startup HEAD 未产生，正文未 GET。

已完整读取 README、02/03/04/05/06、plan／ledger 及 `/tmp/p3-page-body-02-startup.md`，只读核本两 UID 的 C（canonical metadata／capsule）、R（rights audit）、K（coverage ledger）与完整旧 manifest。既有执行状态保留 Issue #3/#4 open、父 PR #1 Draft、成果未进入 main；发布前由主线按 [执行合同（Execution Contract）](06-codex-execution-contract.md) 复核当前 Issue／远端状态与必读材料，本 executor 不把旧检查点写成新网络核验。许可法条与全库终审沿用 [验证及完成定义（Validation / Definition of Done）](05-validation-and-definition-of-done.md)，本文只固定本批窄合同。

## 选择、价值与边界（Selection / Value / Boundary）

| UID／不变身份 | 唯一正文候选 | 本次单页边界；原 UID 总体边界仍待定 |
| --- | --- | --- |
| `methodology:linkml-schema-first`／`METHODOLOGY-LINKML` | `https://linkml.io/linkml/` | 当前文档首页实际响应；不含 tutorial／specification／其他文档。是否要求完整多页方法文档待决 |
| `vocabulary:schema.org`／`SCHEMA.ORG` | `https://schema.org/docs/schemas.html` | Schemas／Organization of Schemas 本页；不含 type／property 独立页、完整 Vocabulary／release 或外部扩展。总体目标待决 |

真实增量是补上旧包未留存的原 HTML，让远程 agent 能复查正文、结构／链接损失及源→派生定位，并改善既有 LinkML 消费链；不是增加 complete 数量。初始 `selected_response_version` 未赋值，现在已固定本页本次 UTC 响应版本，不冒称 release、部署 commit、HTTP Date 或聚合生成时间。

初始工作假设（working hypothesis）为现 `dated_html_response` 可零代码保真消费；实际 article 容器与 gzip 响应已触发本次窄修订，授权范围见当前合同。若又需不同 URL、其他编码、新媒体或额外 carrier／历史路径，须继续据实修合同再实施。若许可无法闭合、现 helper 无安全连续摘句或必须扩大产品目标／递归多页，该 UID 保留旧包并记录具体 unresolved，不新建框架。

## 六维 before（Observed Baseline）

以下保留启动时 BASE 的实际记录，不把旧 unknown／未存 HTML 改成本轮后验事实。两项 before `action_bucket=needs_boundary_verification`、`resolution=unresolved`；`html_article_snapshot` 是本批执行主桶，不等于完成判断。

| 维度 | LinkML before | Schema.org before |
| --- | --- | --- |
| 身份／版本（Identity / Version） | 身份已核，C／snapshot `source_version=null`；root version 键缺省；revision `sha256:93a9f00b0006695dab8f1bde801a40e36eed8c236c4c839aff645bec38b5dc6c` | 身份已核，C／snapshot `source_version=null`；root version 键缺省；revision `sha256:f62a658dd54f9185572242dd6e97df94b201c73132e744d4f078c66b2f51e0d3` |
| 原件覆盖（Original Coverage） | `unknown / partial_check`；HTML inventory 0；总体多页边界未定 | `unknown / partial_check`；HTML inventory 0；总体 Vocabulary／release 边界未定 |
| 文本提取（Text Extraction） | `unknown / partial_check`；旧 document 351 行／8279 字符、164 root selectors；语义边界未核，OCR not_applicable | `unknown / partial_check`；旧 document 93 行／4576 字符、34 root selectors；语义边界未核，OCR not_applicable |
| 本地持久化（Local Persistence） | 5 件 inventory present／tracked，定位器可解析、index／registry consistent；fresh checkout=false，`complete_target_consumable=null` | 同左：5 件 inventory present／tracked，定位器可解析、index／registry consistent；fresh checkout=false，完整目标消费=null |
| 公开再分发（Redistribution） | 旧文字包 Apache-2.0、documented permission／gate=allow、revision 匹配；不覆盖未来 raw HTML | 旧文字包 CC-BY-SA-3.0、documented permission／gate=allow、revision 匹配；不覆盖未来 raw HTML |
| 知识准入（Knowledge Admission） | 已 selected，2 candidate；不晋升 trusted | 所选 demo 无 claim，state=null；不制造 candidate／selected |

两项 before 的 omitted=0、missing pages／sections／errors 空列表不证明完整无缺口。启动 K summary 为 original complete52、text partial59、strict8、unresolved123；现实际 summarize 已复算 T partial60／unknown51，其他计数不变。总体边界未定继续限制原 UID 完整宣称；LinkML 实际结构损失独立判 partial，不能因原件单页可读升两个 `complete_verified` 或用 not_applicable 清计数。

## 两来源实际六维 after（Observed Per-source After）

| 维度 | LinkML after | Schema.org after |
| --- | --- | --- |
| 身份／版本 | 同 UID／canonical；当前单页 `dated-response-2026-09-17T14:20:17Z`，entity revision93a9…；旧 null／缺省完整入历史 | 同 UID／canonical；当前单页 `dated-response-2026-09-17T14:20:15Z`，新 entity b5be…／wire fad84b…；旧 f62a…／null 历史保全 |
| 原件覆盖 | 真保存完整 55141B 单页响应，article L414–646；原 UID 多页边界仍 unknown／partial_check | 保存 4500B wire 与机械解码12007B entity，article L83–335；原 Vocabulary／release 总体覆盖仍 unknown／partial_check |
| 文本提取 | partial：17092B／16411字符／801行，保留实际文字／href，但 li/p／blockquote 层级及 Indices 列表归属有损 | 9870B／9174字符／218行，恢复 unwrapped 定义／dated 数量和实际 href；总体 T 仍 unknown／partial_check，不冒充完整 Vocabulary |
| 本地持久化／定位 | inventory9件／168130B（另 manifest，共10文件）；6新／170总 selectors，全部新 bounds 已实读；完整目标消费=false，源包 index-export replay通过，不含新 method fix | inventory10件／121805B（另 manifest，共11文件）；5新／39总 selectors；wire 只作独立库存，完整目标消费=false，同一源包 scoped fresh通过 |
| 公开再分发 | 已履约四方 scoped allow，Apache-2.0 AND MIT；载体／当前 NOTICE 同 bytes18634B，旧 prose grant 保留 | 已履约四方 scoped allow，CC-BY-SA-3.0 AND Apache-2.0；载体／NOTICE 同 bytes40802B，旧 prose grant 保留 |
| 知识准入 | 原2候选、原selected、不升trusted；重建两链分别为normalized-derived来源断言及原metadata采集者判断，exact-head终审仍待核 | 不新增selected／claim／candidate；TermFinder仅静态UI，未抓交互结果 |

完整审读／`body_quality_verified=true` 仅覆盖两实际派生及所有新 sidecar，不是 whole-UID semantic complete。无实质 article img／object／视频需增抓；Logo、theme 远程文件、type／property 子页与外链作品不是本次正文资产。两对象 `partial/full_text`、原总体边界未定、`complete_target_consumable=false`／unresolved 不变。

## 实际损失纠偏与选择理由（Observed Limitation / Decision Correction）

内容 reader 实物核到 LinkML 原 HTML L557–565 的 SchemaDefinition 外层 li/p 与 blockquote 内四子 li/p，在 normalized L494–532 出现空 marker、label 未正确缩进；原 Indices L639–641 在新 L771–789 同样丢列表成员归属。词句、URI／href 与顺序仍在，不等于嵌套关系完整。本批不再保留“嵌套列表完整”当前断言，C／snapshot／R／manifest limitations、载体／NOTICE／footer 已同步具体损失；最终纠正后数值采用17092B／18634B／168130B，不沿用早期17015B／18510B／167852B快照。末注前正文、raw、旧历史与 selectors 未因此改写。

非作者代码预审 `/tmp/pr26-code-prereview.md` 未发现两路径阻塞；结构预判 `/tmp/pr26-structure-prereview.md` 认为此真实损失可带明确 partial 限制进入最终审核，无需扩大本批 renderer。理由是原响应可复查、当前安全导语与 metadata assessment 不依赖该父子结构、不据损失区新造关系 claim；若最终消费依赖它，该非阻塞判断不再适用。两者均非最终三维 PASS、CI 或 merge 许可。

包装曾遇旧 EOF／新 package 不符并由现 helper fail-closed；按实际旧 footer 严格验证后替换为当前 package，再正常重放通过，未持久化临时旧包或清目录。早期检查预设“首摘录必为定义句”及 R null→none 统计假设也曾失败，实读安全作者导语／沿用 BASE 既有统计语义后纠正检查，不改数据迎合断言。诚实 partial 和保存原件是这次增量的价值，不是完美抽取宣称。

## 历史、履约与局部重放（History / Fulfillment / Local Replay）

包装 handoff 已实际核 C `history.before_page_body_02`、M `historical_acquisition`、R 新 historical review 分别精确等于 BASE 完整旧 C/M/R；旧生成时间、retrieval、rights、inventory、诊断和 null／缺省版本都保留。两旧 root doc／selectors 仍分别8443B／39002B、4960B／8637B，历史 NOTICE 副本12852B／24271B严格等于旧 bytes。身份、分类、collection／inclusion_reason、evidence／governance 未改；canonical 与 snapshot 当前全对象一致，其他106条 R 对象等 BASE。

两 carrier 完整相关 legal block、实际 credit 与 EOF newline 已核；当前 C／snapshot／manifest／R 包精确一致，组合范围按组件履约而非 OR／全站授权。每 UID 首次 pair 不存在时仅一次 `check_derived=False`；之后正常 `materialize_generic` 各两次 strict offline replay，整 capsule bytes 全等，fetch／prepare／rmtree 调用0、finalize各2。全部新 selectors 首中末 preview／源行对应已读；LinkML L14–35←原414–424、L552–704←570–616、L766–789←637–714；Schema L14–17←83–86、L124–128←273–283、L192–206←324–365。末界至 EOF 是 enclosing provenance bounds，不是 footer 已转换或 article closing-tag 坐标。

## 许可先于公开准入（Rights Before Public Admission）

旧授权是旧范围的真实许可链，不是新完整响应的准入。LinkML 已有 R 的 deployed authored prose／官方文档源对应与 Apache-2.0 无文档例外证据；Schema.org 已有 supporting documentation 的官方 [Terms](https://schema.org/docs/terms.html)／[FAQ #18](https://schema.org/docs/faq.html#18) 的 CC BY-SA 3.0 范围，site software 另按 Apache-2.0。主线已亲读两完整既有许可载体及 Schema 当前许可入口；本报告未做网络请求，也未把历史文档源／许可页 commit 当实际新网页部署版本。旧 grant 排除 theme／scripts／styles／media／其他页面及外部作品。

两 GET 先暂存于公开树外，待有界 rights review 与载体／四方包装闭合后才保存至工作树。已仅新增两个专属载体 `raw_data/licenses/linkml-page-body-02-260917.md`／`raw_data/licenses/schemaorg-page-body-02-260917.md`，收录完整相关法条与实际归属；复用既有 Apache-2.0／CC-BY-SA-3.0 全文，不改共享载体。LinkML 保留 Furo 2025.12.19 MIT 全文／copyright、实际 Sphinx／Furo 署名及 Just the Docs／Feather／Tabler 来源注记，不作无穷依赖全链考古或虚构 notice；Schema 保留四 Sponsors 归属，文档适配物遵守 BY-SA，不把 Apache 模板重许可为 BY-SA。完整来源／修改说明及真实 upstream NOTICE（若有）按既有计划履约，不包外链原作品或未下载资源；局部 scoped allow 不等于全库门控通过或最终公开合入。

许可对应关系可有界复核上述官方入口及 LinkML `https://linkml.io/linkml/_sources/index.rst.txt`，后者只作文档对应证据，不是第二正文。实际 body img／object 逐件判断角色与许可；需要新增媒体或历史 NOTICE 副本时，先列真实 URL／精确 carrier 路径并修合同，不递归取主题／全站资源。许可 unknown 时暂停该 UID 新 bytes 的公开包装、记录 unresolved，旧材料不删、不降级。

## 真实响应、配对重放与历史（Actual Response / Paired Replay / History）

真实 requested／resolved URL、UTC、HTTP／content-type／bytes 已在当前合同记录；历史与本次 attempts 如实保全，不从成功推 HTTP200或拿生成时间充 GET。现 sidecar 的同址200／HTML、entity revision、inventory、四方许可绑定与真实 source→derived selectors 比较不放宽；尚未观察的新 redirect、编码或非静态正文继续先停线修合同。

实际复用现表示：`materialization.document`／`normalized_document` 指向 `normalized/document.md`，`retained_text_binding=dated_html_response`，`retained_text_sources` 恰为单个 `source/specification.html`／`format: html`，分别采用 `content_selector: article#furo-main-content`／`article#mainContent`；LinkML 项仅增 `exclude_selectors: [a.headerlink]`，只在派生 DOM 去 headings 的 ¶ UI 锚符，不改 raw、不删作者 toctree。Schema TermFinder 静态 label 保留但不是事实 claim、不抓交互结果。新 sidecar 为 `normalized/selectors.jsonl`，同时保留旧 root selectors；当前 `status=partial` 不提升完整口径，具体列表层级损失如上。

Schema 只有一条 HTTP retrieval：`local_path: source/specification.html`、`bytes: 12007`／`sha256` 指 decoded entity，增加 `content_encoding: gzip`、`transport_local_path: source/specification.html.gz`、`transport_bytes: 4500`、`transport_sha256: fad84bc7594cbb77a61e06a2dba1d3dbffd096936c4b2bf30939411622c9965c`。manifest revision／许可 `source_revision` 仍指 entity；wire 只进独立 inventory，不加入 retained_text_sources、不分配正文 selector、不重复 retrieval。HTTP Content-Length 4500 不可填 entity bytes。

LinkML entity 就是未编码 wire；Schema 精确保留 4500B gzip wire，并保留机械解压的 12007B entity，不改 HTML 字节／编码／链接，也不在 replay 自动解压覆盖源文件。normalized 是采集器格式转换（collector-derived format conversion），不是 raw quotation；NOTICE／README／package scope 明确 wire／entity／结构 Markdown 与 gzip 解码、article 筛选、collector additions 的处理边界，不笼统说所有文件都是未经处理 wire。

C、snapshot、manifest、R 四方当前包绑定实际 entity 与包含 wire 的许可范围；完整旧 manifest／retrievals／generated_at／null 或缺省版本及全部既有 history 保全。旧 root `document.md`／`selectors.jsonl` 字节只读、不加 footer；在更新当前组合 NOTICE 前，分别逐字节复制旧 NOTICE 至两 capsule 已列定的 `history/NOTICE-before-page-body-02.md`。新 normalized EOF 才有唯一附注；额外历史／媒体路径仍需新合同。

派生边界注记（collector boundary note）及每个 selector transformation 必须注明 declared article filtering。现源行区间是保守包围 provenance bounds，末区间可延伸 entity EOF，不等于每行都转换或精确 article closing-tag；article 后的 footer 不应进入派生正文。不新增 DOM end-line parser 或用行数冒充覆盖完整性。

## 最小接口与失败关闭回归（Minimal Interface / Fail-closed Regressions）

dated source 的 `content_selector` 缺省保留 legacy 行为；若明确出现，必须为非空字符串 CSS，在唯一 body 内恰好匹配一个非空 article。null／数字／空白、非法 CSS、零／多匹配、非 article／空 article 全部失败关闭（fail closed），不回退全 body。preflight 与 derivation 使用同一选中容器；既有 dated UI 排除 allowlist 仅增观察到的 `a.headerlink`，未知排除继续拒绝、不删作者 toctree。容器内未声明资产仍拒绝，wiki 固定规则不变。

dated retrieval 任一 encoding／transport 字段出现即要求四项完整，唯一支持 gzip 与精确 `source/specification.html.gz`。既有 preflight 核 capsule 内普通非 symlink 文件、独立唯一 inventory 的真实 bytes／hash 与声明，验证 `gzip.decompress(wire) == entity`；缺项、unsupported、越界／缺文件、损坏 gzip／decode failure、inventory／bytes／hash 错配或不同 entity，均在 writes 前拒绝。无 fetcher、不改其他 acquisition 路径；现 completeness validator 已调用该 preflight，不需源码修改。

仅既有 integrity fixtures 做最小正负回归：两个不同 article ID 的有限 fixture、正文首中末与外部 nav／footer sentinel、首次派生及两次禁网 replay、source／wire／旧 doc selectors 不变；上述 selector／gzip 失败关闭且失败前后不写、不 fetch／prepare／finalize，article 内资产约束继续成立；无 selector legacy dated 与 wiki 回归不变。保留 entity source ranges 与 wire inventory 区分，验证末 source_end_line 可至 EOF 但 footer 不转换。局部测试完成仍不等于最终 CI／非作者终审。

## 两条既有 LinkML 消费链（Existing Consumer Chains）

| 既有链 | 重建后实际字段；最终 exact-head 终审另行绑定 |
| --- | --- |
| `claim:583280271287ef9c` ← `evidence:b0f0f32b0b4cc957` ← 原 `document.md#L6-L7`；来源报告断言（source-reported assertion） | 新pair仍同ID／candidate，实际文本为新normalized L24／原HTML417–418导语；evidence精确derived方法／retained_html_response／not-raw transformation，local selector L24–L24，rights_refs绑定组合包与entity revision93a9…。claim为source-assertion-extraction-without-model、明确派生限制；不强选L28定义句。provenance pin的是实际revision／消费文件hash，不冒称raw quotation |
| `claim:27f7e77bbaa0d47f` ← `evidence:d3ebb3860ae3f34c` ← C `#collection.inclusion_reason`；采集者判断（collector assessment） | 重建pair仍同ID／candidate，collection-assessment-extraction／collection-metadata-read，metadata field selector与实际原inclusion_reason；source_hash／source_version均null，无source rights继承。没有改成网页来源断言或页面版权授权 |

主线最终完整对象对账确认：36个source UID、72个evidence、72个claim成员集合精确等BASE；仅LinkML source对象、上表来源evidence `b0f0…` 与来源claim `5832…` 内容变。采集者claim `27f7…`／evidence `d3eb…` 完整对象等BASE，其他35source／71evidence／71claim不变，Schema.org未新增selected。新身份传播及全局build变化不等于新知识成员或collector改写。

两条既有 candidate 的实际结果仍须由最终exact-head终审核实；若后续观测显示现摘句器无安全段落，先停并修合同，不强留数量或假旧定位。Schema.org 继续不新增 selected／claim；其他来源知识语义不改。

## 合同顺序与剩余验证（Contract Order / Remaining Verification）

1. 已依序发布 startup → 两暂存 GET → 发布窄修订 → 两路径实现／rights 履约 → 局部包装／严格重放；没有新增正文 GET。影响同一输入的 base 移动须刷新合同，保持唯一 writer。
2. 原件／派生首中末、全部新 selectors、具体列表损失、四方包与旧 bytes／history 局部核验已实际完成；不凭数量推语义完整。首次 pair 不存在时才一次 `check_derived=False`，后续正常 strict replay，无清目录。
3. aggregate已实际重建、时间固定 `2026-09-16T04:30:26Z`；C/R/K/capsules冻结后，demo方法故障先公开修订再修复／聚焦回归／代码冻结／完整重建通过，没有回写K。若后续观测需纠偏输入，必须重新冻结重建，不能留stale build。
4. Python3.12.13；217tests是pre-fix历史，现focused36及主线223tests／完整demo-Wiki均exit0。最终repro四阶段各169文件byte-identical、整体exit0，内含正常validate exit0；current-pair CI与非作者终审另待真实记录。禁默认全库抓取，旧public gate错误仍照实报告。
5. 源包局部重放及两UID index-export已完成，仅证明源包独立消费，不是remote/main验收。方法修补未改摘句／两ID／collector／selection／trust；主线最终生成对象核对仅1个LinkML source、1个来源evidence、1个来源claim变化，其余对象和collector pair等BASE，Schema未新增selected；其他213registry对象、其他129K保全。全部Wiki链与代码冻结复用仍以exact pair终审核实。
6. 真实六维 after／剩余缺损／下一桶最后据实报告，原 UID 总体边界未定与 unresolved 保留。非作者 evaluator 锁最终 exact HEAD／BASE，分别评估需求满足（requirements）、agentic 判断链与证据、核心质量（core quality）；最终三维结论及当前 CI 必须真实取得。相关输入再变须重验，作者本轮不自评 PASS、不授权 merge。

## 实际验证与暂未完成项（Actual Verification / Pending Checks）

| 实际命令／检查 | 当前结果与范围 |
| --- | --- |
| 历史修复前 `make test` | exit0；8组总217，rights6／integrity93；此前未覆盖真实methods阻塞，保留历史、不替代新代码验证 |
| 修复后聚焦／主线 `make test`，Python3.12.13 | focused36 exit0（rights12／evidence4／excerpt20）；主线 `4+20+12+13+93+49+2+30=223` tests exit0，不是最终pair CI |
| 主线 full materialization validation | exit0；metadata215／manifests215／inventory hashes3205／selectors25869／errors0。pypdf 字体／复杂 form 诊断仍存在，不冒充全库无提取限制 |
| 既有 aggregate funcs | 实际215 records／3205 hashes／local bytes265851572；status168 materialized／32 partial／15 metadata |
| 主线三次 cmp | exit0；两 HTML entity 与 Schema gzip wire 等实际 staged response bytes |
| 两 UID scoped publication-rights | exit0；active2／audited108，errors=[]／blocks=[]，只代表本两包 |
| 全库 publication-rights | 实际 exit1；active104／audited108／errors2／blocks64。GraphRAG／AI co-scientist 旧 package 错误未由本批改；不是 PASS，也不是64份正文缺口 |
| 两 UID actual strict replay／历史／四方包／全部新 sidecar | 包装 handoff 最终 exit0；每 UID 两次正常离线 replay 整 capsule byte-identical、无 fetch／prepare／rmtree；局部声明不替代终审 |
| K freeze handoff | 实际一次 facts exit0；两 observed 精确一致，其他129完整 item等 BASE，完整旧 execution／旧两 item及12处 preview保全；summary T partial60／unknown51。K的demo／repro／fresh false-null是冻结时检查点，不冒充后续实时结果或失败 |
| 历史首轮 `make demo` | 实际exit2／唯一methods错配、36／72／72／51中间产物；现已修复并用完整重建替换失败中间树，不删除故障史 |
| 修复后主线 `make demo` | 实际exit0；36sources／72claims／72evidence，完整Wiki135pages／357typed links／3context packs，errors0／warnings0；21inputs／154outputs，实际两build ID见上 |
| 两 UID fresh index-export | 实际 exit0；无.git的 `/tmp/pr26-index-export-VPq83t`，21 capsule文件各两次严格byte-identical；fetch／prepare／rmtree0、finalize各2，受监测26文件全在导出树、树外／网络0；真实摘录L24／L113。仅修复前两源包，非整体demo／final HEAD／remote/main |
| 主线默认 coverage auditor | 实际 exit0／summary PASS；131非repo＋84排除、observed与冻结K／报告summary一致，T partial60／unknown51。检查后C/R/K未变；这是source summary门控，不替代最终审核／CI |
| 第二窄修订公开／新增实现与代码复核 | 先公开15:24:39Z checkpoint，再实际两路径358 additions／3 deletions与focused36；非作者代码复核完成无具体新阻塞，不是final pair三维PASS |
| 最终 `make reproducibility` | 实际exit0；`committed_tree_replay`／`full_demo_replay`／`compiler_only_replay`／`read_only_validation` 四阶段各169生成文件byte-identical，不等于remote或main验收 |
| repro内含正常 `make validate` | 实际exit0：raw248YAML／215metadata／errors0；materialization215metadata／215manifests／3205hashes／25869selectors／warnings0／errors0；docs62markdown／5examples／86links／errors0；demo36sources／189objects／72claims／72evidence／135pages／errors0；Wiki同 `bdc4c9116985ab25`、21inputs／154outputs／errors0 |
| 最终生成语义／合同路径核对 | 成员集合36source／72evidence／72claim等BASE；仅1个LinkML source与来源evidence／claim内容变，其余35／71／71及collector pair完整对象等BASE，Schema未新增selected。194 changed paths、out_of_contract0／deletions0／untracked0 |
| exact final HEAD／BASE 的非作者三维 evaluator、当前 CI | pending；绑定 PR review／评论／CI，不自指伪造新 HEAD |

## 明确非结果与停线（Non-results / Stop Conditions）

当前四代码／测试路径、组合许可与源包／K冻结、聚焦36／全量223tests、完整demo-Wiki重建、四阶段repro及内含validate已实际完成且exit0；旧exit2真实保留且已修复，不再冒充当前失败。仍待current CI／非作者exact-head／base终审，final HEAD保持null／由PR绑定；本地通过不是最终三维PASS。实现待主线commit／push、未merge，本executor只写两文档、无Git／网络／生成操作，不造最终commit／CI／PASS。C/R/K与capsules未再变，原boundary／unresolved／全库旧pub errors2／blocks64仍在；未宣称UID strict complete、多页目标完成、main落地、Issue关闭或trusted晋升。

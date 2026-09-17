---
phase: P3-PAGE-BODY-02
base_sha: 6705771e53414b941541ed77d7b88aefa89caaa4
status: response_observed_narrow_amendment_pending_implementation
coverage_summary: {"collection_records":215,"non_repo_total":131,"github_repo_excluded":84,"reported_content_tier_counts":{"excerpt_capsule":23,"full_text":97,"metadata_capsule":11},"source_type_counts":{"arxiv":73,"biorxiv":2,"blog":10,"industry":2,"journal":11,"methodology":7,"paper":2,"standard":24},"original_artifact_counts":{"complete":52,"metadata_only":12,"partial":4,"unknown":63},"text_extraction_counts":{"complete":8,"partial":59,"unavailable":12,"unknown":52},"action_bucket_counts":{"access_restricted":8,"author_manuscript_fetch":2,"complete_verified":8,"html_article_snapshot":11,"identity_or_version_ambiguous":3,"needs_boundary_verification":51,"ocr_assessment":36,"parser_only":6,"public_persistence_decision":4,"standard_spec_fetch":2},"public_redistribution_counts":{"allow":33,"block":65,"unknown":33},"content_inspected_full_text":59,"structure_only_full_text":38,"locally_persisted_complete":8,"knowledge_candidate_sources":30,"knowledge_trusted_sources":0,"knowledge_sources_without_demo_claims":101,"unresolved_sources":123}
execution_contract:
  plan_id: nonrepo-materialization-main-convergence-260916
  phase: P3-PAGE-BODY-02
  status: response_observed_narrow_amendment_pending_implementation
  base_branch: work/v0-meta-kb-initialization-demo-260910
  base_sha: 6705771e53414b941541ed77d7b88aefa89caaa4
  target_branch: work/v0-meta-kb-initialization-demo-260910
  batch_branch: codex/p3-page-body-02-260917
  pull_request: 26
  startup_head_sha: bd6c7382c82e6f38633c623ee67901b17a4ccc1d
  startup_published_at: '2026-09-17T14:19:51Z'
  head_sha: bd6c7382c82e6f38633c623ee67901b17a4ccc1d
  final_head_sha: null
  prerequisite_pull_request: 25
  prerequisite_merge_commit: 6705771e53414b941541ed77d7b88aefa89caaa4
  source_uids: ["methodology:linkml-schema-first", "vocabulary:schema.org"]
  adapter_family: generic_web_or_document_v2
  action_bucket: html_article_snapshot
  representation: dated_html_response
  canonical_ids: {"methodology:linkml-schema-first": "METHODOLOGY-LINKML", "vocabulary:schema.org": "SCHEMA.ORG"}
  sole_body_get_candidates: {"methodology:linkml-schema-first": "https://linkml.io/linkml/", "vocabulary:schema.org": "https://schema.org/docs/schemas.html"}
  selected_response_versions: {"methodology:linkml-schema-first": "dated-response-2026-09-17T14:20:17Z", "vocabulary:schema.org": "dated-response-2026-09-17T14:20:15Z"}
  selected_version_kind: proposed_single_page_response_snapshot_not_release_or_deployment_commit
  content_selectors: {"methodology:linkml-schema-first": "article#furo-main-content", "vocabulary:schema.org": "article#mainContent"}
  derived_exclude_selectors: {"methodology:linkml-schema-first": ["a.headerlink"], "vocabulary:schema.org": []}
  original_uid_boundaries: unresolved_no_whole_UID_complete_claim
  production_code_changes: authorized_minimal_dated_article_selector_and_gzip_transport_preflight_pending_implementation
  body_acquisition: two_sole_approved_GETs_staged_only_no_public_raw_admission_yet
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
  raw_publication_admission: pending_license_fulfillment_and_four_way_packaging_not_public_allow
  startup_checkpoint:
    status: startup_not_acquired
    pull_request: null
    startup_head_sha: null
    head_sha: null
    selected_response_versions: {"methodology:linkml-schema-first": null, "vocabulary:schema.org": null}
    body_acquisition: not_executed
    production_code_changes: none_working_hypothesis_requires_observed_DOM_confirmation
    after: null
  after: null
  startup_only_writes:
    - docs/plans/260916-corpus-completion-main-convergence/p3-page-body-02.md
    - docs/plans/260916-corpus-completion-main-convergence/branch-ledger.yaml
  allowed_paths:
    - scripts/materialize_all_sources.py
    - tests/test_materialization_integrity.py
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
    - code_or_tests_outside_materializer_and_integrity_tests_completeness_validator_changes_dependencies_workflows_new_adapter_or_fetcher
    - full_LinkML_multi_page_docs_or_full_Schema_vocabulary_release_type_property_pages
    - recursive_fetch_theme_assets_external_works_or_media_without_exact_prior_amendment
    - shared_license_text_changes_carriers_outside_two_explicit_per_item_paths_or_old_history_replacement
    - original_UID_complete_verified_claims_count_redefinition_or_not_applicable_count_clearing
    - new_demo_selection_Schema_claims_trusted_promotion_or_other_source_semantic_changes
    - dependent_artifacts_during_this_amendment_main_merge_issue_closure_or_Git_history_changes
  independent_evaluation: pending_actual_final_head_and_base_non_author_three_dimensions
  final_ci: pending_actual_final_head_and_base
---

# P3-PAGE-BODY-02 — 两份既有单页原响应的启动及窄修订合同

## 当前响应与执行前窄修订（Observed Response / Pre-implementation Amendment）

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

真实增量是补上旧包未留存的原 HTML，让远程 agent 能复查正文、结构／链接损失及源→派生定位，并改善既有 LinkML 消费链；不是增加 complete 数量。初始 `selected_response_version` 未赋值，本次提议只表示已观察本页本次 UTC 响应，不冒称 release、部署 commit、HTTP Date 或聚合生成时间。

初始工作假设（working hypothesis）为现 `dated_html_response` 可零代码保真消费；实际 article 容器与 gzip 响应已触发本次窄修订，授权范围见当前合同。若又需不同 URL、其他编码、新媒体或额外 carrier／历史路径，须继续据实修合同再实施。若许可无法闭合、现 helper 无安全连续摘句或必须扩大产品目标／递归多页，该 UID 保留旧包并记录具体 unresolved，不新建框架。

## 六维 before（Observed Baseline）

以下是当前记录读取，不是复跑全局 facts 或 validator。两项现 `action_bucket=needs_boundary_verification`、`resolution=unresolved`；上述 `html_article_snapshot` 是本批执行主桶，不是已观察 after。

| 维度 | LinkML before | Schema.org before |
| --- | --- | --- |
| 身份／版本（Identity / Version） | 身份已核，C／snapshot `source_version=null`；root version 键缺省；revision `sha256:93a9f00b0006695dab8f1bde801a40e36eed8c236c4c839aff645bec38b5dc6c` | 身份已核，C／snapshot `source_version=null`；root version 键缺省；revision `sha256:f62a658dd54f9185572242dd6e97df94b201c73132e744d4f078c66b2f51e0d3` |
| 原件覆盖（Original Coverage） | `unknown / partial_check`；HTML inventory 0；总体多页边界未定 | `unknown / partial_check`；HTML inventory 0；总体 Vocabulary／release 边界未定 |
| 文本提取（Text Extraction） | `unknown / partial_check`；旧 document 351 行／8279 字符、164 root selectors；语义边界未核，OCR not_applicable | `unknown / partial_check`；旧 document 93 行／4576 字符、34 root selectors；语义边界未核，OCR not_applicable |
| 本地持久化（Local Persistence） | 5 件 inventory present／tracked，定位器可解析、index／registry consistent；fresh checkout=false，`complete_target_consumable=null` | 同左：5 件 inventory present／tracked，定位器可解析、index／registry consistent；fresh checkout=false，完整目标消费=null |
| 公开再分发（Redistribution） | 旧文字包 Apache-2.0、documented permission／gate=allow、revision 匹配；不覆盖未来 raw HTML | 旧文字包 CC-BY-SA-3.0、documented permission／gate=allow、revision 匹配；不覆盖未来 raw HTML |
| 知识准入（Knowledge Admission） | 已 selected，2 candidate；不晋升 trusted | 所选 demo 无 claim，state=null；不制造 candidate／selected |

两项原件 omitted=0、文本 missing pages／sections／errors 的空列表不证明完整无缺口。旧局部首／中／尾检查也不等于原响应比对。报告 frontmatter 是当前 K summary：original complete 52、text partial 59、strict `complete_verified` 8、unresolved 123；未预测 after。总体边界未固定时，A／T 的 unknown 不被本次单页冒充 complete；发现实质缺口才按证据标 partial。后续当前单页可消费也必须保留原 UID `complete_target_consumable=false`／unresolved，不升两个 `complete_verified` 或用 not_applicable 清计数。

## 许可先于公开准入（Rights Before Public Admission）

旧授权是旧范围的真实许可链，不是新完整响应的准入。LinkML 已有 R 的 deployed authored prose／官方文档源对应与 Apache-2.0 无文档例外证据；Schema.org 已有 supporting documentation 的官方 [Terms](https://schema.org/docs/terms.html)／[FAQ #18](https://schema.org/docs/faq.html#18) 的 CC BY-SA 3.0 范围，site software 另按 Apache-2.0。主线已亲读两完整既有许可载体及 Schema 当前许可入口；本报告未做网络请求，也未把历史文档源／许可页 commit 当实际新网页部署版本。旧 grant 排除 theme／scripts／styles／media／其他页面及外部作品。

原 startup 已发布且两 GET 已依约暂存于公开树外。有界 rights review 已支持实际正文／内联模板的组合范围；履约载体和四方包装完成前，不把新增 bytes 放入公开 repo。仅新增两个专属载体 `raw_data/licenses/linkml-page-body-02-260917.md`／`raw_data/licenses/schemaorg-page-body-02-260917.md`，收录各自完整相关法条与实际归属；复用既有 Apache-2.0／CC-BY-SA-3.0 全文，不改共享载体。LinkML 保留 Furo 2025.12.19 MIT 全文／copyright、实际 Sphinx／Furo 署名及 Just the Docs／Feather／Tabler 来源注记，不作无穷依赖全链考古或虚构 notice；Schema 保留 Terms 的四 Sponsors 归属，文档适配物遵守 BY-SA，不把 Apache 模板重许可为 BY-SA。完整来源／修改说明及真实 upstream NOTICE（若有）按既有计划执行，不包外链原作品或未下载远程资源。

许可对应关系可有界复核上述官方入口及 LinkML `https://linkml.io/linkml/_sources/index.rst.txt`，后者只作文档对应证据，不是第二正文。实际 body img／object 逐件判断角色与许可；需要新增媒体或历史 NOTICE 副本时，先列真实 URL／精确 carrier 路径并修合同，不递归取主题／全站资源。许可 unknown 时暂停该 UID 新 bytes 的公开包装、记录 unresolved，旧材料不删、不降级。

## 真实响应、配对重放与历史（Actual Response / Paired Replay / History）

真实 requested／resolved URL、UTC、HTTP／content-type／bytes 已在当前合同记录；历史与本次 attempts 如实保全，不从成功推 HTTP200或拿生成时间充 GET。现 sidecar 的同址200／HTML、entity revision、inventory、四方许可绑定与真实 source→derived selectors 比较不放宽；尚未观察的新 redirect、编码或非静态正文继续先停线修合同。

复用现表示：`materialization.document`／`normalized_document` 指向 `normalized/document.md`，`retained_text_binding=dated_html_response`，`retained_text_sources` 恰为单个 `source/specification.html`／`format: html`，分别增加已观察的 `content_selector: article#furo-main-content`／`article#mainContent`；LinkML 项仅增 `exclude_selectors: [a.headerlink]`，只在派生 DOM 去 headings 的 ¶ UI 锚符，不改 raw、保留 article 内作者 toctree 列表。Schema TermFinder 静态 label 可保留但不是事实 claim、不抓交互结果。新 sidecar 为 `normalized/selectors.jsonl`，同时保留旧 root selectors；`status=partial` 是合同限制，上述仍为待实施接口，不是 after。

Schema 只有一条 HTTP retrieval：`local_path: source/specification.html`、`bytes: 12007`／`sha256` 指 decoded entity，增加 `content_encoding: gzip`、`transport_local_path: source/specification.html.gz`、`transport_bytes: 4500`、`transport_sha256: fad84bc7594cbb77a61e06a2dba1d3dbffd096936c4b2bf30939411622c9965c`。manifest revision／许可 `source_revision` 仍指 entity；wire 只进独立 inventory，不加入 retained_text_sources、不分配正文 selector、不重复 retrieval。HTTP Content-Length 4500 不可填 entity bytes。

LinkML entity 就是未编码 wire；Schema 精确保留 4500B gzip wire，并保留机械解压的 12007B entity，不改 HTML 字节／编码／链接，也不在 replay 自动解压覆盖源文件。normalized 是采集器格式转换（collector-derived format conversion），不是 raw quotation；NOTICE／README／package scope 明确 wire／entity／结构 Markdown 与 gzip 解码、article 筛选、collector additions 的处理边界，不笼统说所有文件都是未经处理 wire。

C、snapshot、manifest、R 四方当前包绑定实际 entity 与包含 wire 的许可范围；完整旧 manifest／retrievals／generated_at／null 或缺省版本及全部既有 history 保全。旧 root `document.md`／`selectors.jsonl` 字节只读、不加 footer；在更新当前组合 NOTICE 前，分别逐字节复制旧 NOTICE 至两 capsule 已列定的 `history/NOTICE-before-page-body-02.md`。新 normalized EOF 才有唯一附注；额外历史／媒体路径仍需新合同。

派生边界注记（collector boundary note）及每个 selector transformation 必须注明 declared article filtering。现源行区间是保守包围 provenance bounds，末区间可延伸 entity EOF，不等于每行都转换或精确 article closing-tag；article 后的 footer 不应进入派生正文。不新增 DOM end-line parser 或用行数冒充覆盖完整性。

## 最小接口与失败关闭回归（Minimal Interface / Fail-closed Regressions）

dated source 的 `content_selector` 缺省保留 legacy 行为；若明确出现，必须为非空字符串 CSS，在唯一 body 内恰好匹配一个非空 article。null／数字／空白、非法 CSS、零／多匹配、非 article／空 article 全部失败关闭（fail closed），不回退全 body。preflight 与 derivation 使用同一选中容器；既有 dated UI 排除 allowlist 仅增观察到的 `a.headerlink`，未知排除继续拒绝、不删作者 toctree。容器内未声明资产仍拒绝，wiki 固定规则不变。

dated retrieval 任一 encoding／transport 字段出现即要求四项完整，唯一支持 gzip 与精确 `source/specification.html.gz`。既有 preflight 核 capsule 内普通非 symlink 文件、独立唯一 inventory 的真实 bytes／hash 与声明，验证 `gzip.decompress(wire) == entity`；缺项、unsupported、越界／缺文件、损坏 gzip／decode failure、inventory／bytes／hash 错配或不同 entity，均在 writes 前拒绝。无 fetcher、不改其他 acquisition 路径；现 completeness validator 已调用该 preflight，不需源码修改。

仅既有 integrity fixtures 做最小正负回归：两个不同 article ID 的有限 fixture、正文首中末与外部 nav／footer sentinel、首次派生及两次禁网 replay、source／wire／旧 doc selectors 不变；上述 selector／gzip 失败关闭且失败前后不写、不 fetch／prepare／finalize，article 内资产约束继续成立；无 selector legacy dated 与 wiki 回归不变。保留 entity source ranges 与 wire inventory 区分，验证末 source_end_line 可至 EOF 但 footer 不转换。局部测试完成仍不等于最终 CI／非作者终审。

## 两条既有 LinkML 消费链（Existing Consumer Chains）

| 既有链 | 后续必须独立复核 |
| --- | --- |
| `claim:583280271287ef9c` ← `evidence:b0f0f32b0b4cc957` ← 旧 `document.md#L6-L7`；来源报告断言（source-reported assertion） | 现消费者改读实际 normalized／sidecar，取连续实际正文，非导航／代码／通知或清理锚点后的伪引文；版本、消费文件 provenance、rights_refs、转换／partial 限制及 Wiki source／claim／map 都对应。新段落未读，不预填 literal，不静默丢链或手造新摘句 |
| `claim:27f7e77bbaa0d47f` ← `evidence:d3ebb3860ae3f34c` ← C `#collection.inclusion_reason`；采集者判断（collector assessment） | 原 inclusion_reason 与 metadata field selector 保留；source_hash／version 的空值语义及 candidate 状态不误标新页面断言或网页许可来源。必要 build ID／依赖传播不改变认识性质 |

两条既有 candidate 的实际结果须完整说明；若现摘句器无安全段落，先停并修合同，不强留数量或假旧定位。Schema.org 继续不新增 selected／claim；其他来源知识语义不改。

## 冻结、验证与独立终审（Freeze / Verification / Independent Review）

1. 原 startup／两获准 GET 已完成；本窄修订由主线审阅发布后，才并行授权两路径小代码修复及 rights／NOTICE 准备，无新增正文 GET。影响同一输入的 base 移动须刷新合同，保持唯一 writer。
2. 每页实物核身份、许可、正文自然首／中／末、heading／列表／表／代码／链接及真实组件；代码局部回归、组件许可与四方包闭合后才公开包装。仅首次两个新派生文件都不存在时用现 replay `check_derived=False` 一次，随后严格正常 replay；核全 inventory／selectors／preview 与原→派生保真，旧 doc／root selectors／NOTICE 历史对照 BASE 保全。
3. 仅现 `rebuild_registry`／`write_indexes_and_audit` 重建必要 index／registry／completeness；确定性聚合时间沿用 `2026-09-16T04:30:26Z`，不是 GET 时间。C、R、K、capsules 及必要已修订代码输入最终冻结后才 `make demo`；若 demo 后实际知识观测需纠偏 K，先重新冻结再 demo／repro，不能最后改 R/K 留 stale build identity。
4. 未来用当前统一运行时 `/tmp/llm-wiki-ci-312-260916/bin/python` 执行 `make test`、`make validate`、`make reproducibility`，以及当前 head 的 materialization completeness、默认 coverage auditor 和 publication-rights 检查；禁止默认全局 materialize-all 取网页。新 scope 错误须为零，全库继承 root blocks／旧错误照实报告，不以两个 allow 宣称全库通过。
5. 各 UID 两次禁网、禁止清目录的正常既有入口 offline replay；fresh candidate checkout／index export 仅依赖 repo，验证原 HTML、normalized、NOTICE 与新旧定位器可读及重复稳定。这不是 remote/main fresh checkout 验收。控制生成路径仅由现 generator 重建必要两 LinkML 链及全局 identity；审查其他213来源对象、其他129 K 对象／其他 R 与知识语义无无关改写。
6. 真实六维 after／剩余缺损／下一桶最后据实报告，原 UID 总体边界未定与 unresolved 保留。非作者 evaluator 锁最终 exact HEAD／BASE，分别评估需求满足（requirements）、agentic 判断链与证据、核心质量（core quality）；最终三维结论及当前 CI 必须真实取得。相关输入再变须重验，作者本轮不自评 PASS、不授权 merge。

## 明确非结果与停线（Non-results / Stop Conditions）

原“未 GET／未创建 PR”仅是 historical startup 非结果；现在已有 PR26 与两暂存响应。当前修订只写报告和 ledger，尚未改 C/R/K、源码／测试、capsule、许可载体或依赖产物；未公开新 raw bytes、未履约包装组合许可、未设置六维 after，未跑 tests／generators／全局 facts，本 executor 未 Git／PR／网络操作。最终 CI 与非作者三维评估仍 pending，不凭 startup CI 或代码计划自评 PASS。未宣称完整 LinkML 文档、完整 Schema.org Vocabulary／release、两个 UID strict complete、全库 public gate PASS、main 落地、Issue #3/#4 关闭或 trusted 晋升。许可单 UID 失败照实 unresolved；新观察需越界时先修合同，不擅自扩大。当前修订供主线发布，完成后停写。

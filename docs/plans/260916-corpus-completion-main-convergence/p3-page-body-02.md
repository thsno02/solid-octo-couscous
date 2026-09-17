---
phase: P3-PAGE-BODY-02
base_sha: 6705771e53414b941541ed77d7b88aefa89caaa4
status: startup_not_acquired
coverage_summary: {"collection_records":215,"non_repo_total":131,"github_repo_excluded":84,"reported_content_tier_counts":{"excerpt_capsule":23,"full_text":97,"metadata_capsule":11},"source_type_counts":{"arxiv":73,"biorxiv":2,"blog":10,"industry":2,"journal":11,"methodology":7,"paper":2,"standard":24},"original_artifact_counts":{"complete":52,"metadata_only":12,"partial":4,"unknown":63},"text_extraction_counts":{"complete":8,"partial":59,"unavailable":12,"unknown":52},"action_bucket_counts":{"access_restricted":8,"author_manuscript_fetch":2,"complete_verified":8,"html_article_snapshot":11,"identity_or_version_ambiguous":3,"needs_boundary_verification":51,"ocr_assessment":36,"parser_only":6,"public_persistence_decision":4,"standard_spec_fetch":2},"public_redistribution_counts":{"allow":33,"block":65,"unknown":33},"content_inspected_full_text":59,"structure_only_full_text":38,"locally_persisted_complete":8,"knowledge_candidate_sources":30,"knowledge_trusted_sources":0,"knowledge_sources_without_demo_claims":101,"unresolved_sources":123}
execution_contract:
  plan_id: nonrepo-materialization-main-convergence-260916
  phase: P3-PAGE-BODY-02
  status: startup_not_acquired
  base_branch: work/v0-meta-kb-initialization-demo-260910
  base_sha: 6705771e53414b941541ed77d7b88aefa89caaa4
  target_branch: work/v0-meta-kb-initialization-demo-260910
  batch_branch: codex/p3-page-body-02-260917
  pull_request: null
  startup_head_sha: null
  head_sha: null
  prerequisite_pull_request: 25
  prerequisite_merge_commit: 6705771e53414b941541ed77d7b88aefa89caaa4
  source_uids: ["methodology:linkml-schema-first", "vocabulary:schema.org"]
  adapter_family: generic_web_or_document_v2
  action_bucket: html_article_snapshot
  representation: dated_html_response
  canonical_ids: {"methodology:linkml-schema-first": "METHODOLOGY-LINKML", "vocabulary:schema.org": "SCHEMA.ORG"}
  sole_body_get_candidates: {"methodology:linkml-schema-first": "https://linkml.io/linkml/", "vocabulary:schema.org": "https://schema.org/docs/schemas.html"}
  selected_response_versions: {"methodology:linkml-schema-first": null, "vocabulary:schema.org": null}
  original_uid_boundaries: unresolved_no_whole_UID_complete_claim
  production_code_changes: none_working_hypothesis_requires_observed_DOM_confirmation
  body_acquisition: not_executed_pending_startup_publication_and_temporary_staging
  actual_responses: {"methodology:linkml-schema-first": null, "vocabulary:schema.org": null}
  after: null
  startup_only_writes:
    - docs/plans/260916-corpus-completion-main-convergence/p3-page-body-02.md
    - docs/plans/260916-corpus-completion-main-convergence/branch-ledger.yaml
  allowed_paths:
    - docs/plans/260916-corpus-completion-main-convergence/p3-page-body-02.md
    - docs/plans/260916-corpus-completion-main-convergence/branch-ledger.yaml
    - raw_data/methodology/LinkML Schema First Knowledge Modeling/metadata.yaml
    - raw_data/standard/Schema.org Vocabulary/metadata.yaml
    - raw_data/audits/materialization_rights_review.yaml
    - raw_data/audits/non_repo_materialization_coverage_2026-09-16.yaml
    - docs/materialization-rights-audit.md
    - materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/source/specification.html
    - materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/normalized/document.md
    - materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/normalized/selectors.jsonl
    - materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/manifest.yaml
    - materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/README.md
    - materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/source-metadata.yaml
    - materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/NOTICE.md
    - materialized_sources/corpus/vocabulary-schema.org--c8b3dc95/source/specification.html
    - materialized_sources/corpus/vocabulary-schema.org--c8b3dc95/normalized/document.md
    - materialized_sources/corpus/vocabulary-schema.org--c8b3dc95/normalized/selectors.jsonl
    - materialized_sources/corpus/vocabulary-schema.org--c8b3dc95/manifest.yaml
    - materialized_sources/corpus/vocabulary-schema.org--c8b3dc95/README.md
    - materialized_sources/corpus/vocabulary-schema.org--c8b3dc95/source-metadata.yaml
    - materialized_sources/corpus/vocabulary-schema.org--c8b3dc95/NOTICE.md
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
    notices: reuse_existing_bytes_if_possible_any_replacement_requires_prior_history_preservation_contract
    generated_changes: existing_LinkML_selected_chains_and_necessary_global_identity_only_no_selection_strategy_change
    new_media_or_history_notice_paths: require_observed_objects_and_prior_exact_path_amendment
  explicitly_out_of_scope:
    - production_code_tests_dependencies_workflows_new_adapter_or_acquisition_framework_without_prior_narrow_amendment
    - full_LinkML_multi_page_docs_or_full_Schema_vocabulary_release_type_property_pages
    - recursive_fetch_theme_assets_external_works_or_media_without_exact_prior_amendment
    - raw_data_licenses_changes_new_shared_license_carriers_or_old_history_replacement
    - original_UID_complete_verified_claims_count_redefinition_or_not_applicable_count_clearing
    - new_demo_selection_Schema_claims_trusted_promotion_or_other_source_semantic_changes
    - global_facts_or_generators_during_startup_main_merge_issue_closure_or_Git_history_changes
  independent_evaluation: pending_actual_final_head_and_base_non_author_three_dimensions
  final_ci: pending_actual_final_head_and_base
---

# P3-PAGE-BODY-02 — 两份既有单页原响应的启动合同

本批采用有界增量（bounded increment）：为两个既有单页补存真实原 HTML、保真结构化消费和现接口的配对重放（paired replay），不把首页改称原 UID 的完整产品。PR #25 已正常合入 work；精确基线（exact base）为 `6705771e53414b941541ed77d7b88aefa89caaa4`，不是规划草案的未合入 HEAD 或旧 base。当前分支为 `codex/p3-page-body-02-260917`；本轮只准备上列两份启动文档，PR／startup HEAD 未产生，正文未 GET。

已完整读取 README、02/03/04/05/06、plan／ledger 及 `/tmp/p3-page-body-02-startup.md`，只读核本两 UID 的 C（canonical metadata／capsule）、R（rights audit）、K（coverage ledger）与完整旧 manifest。既有执行状态保留 Issue #3/#4 open、父 PR #1 Draft、成果未进入 main；发布前由主线按 [执行合同（Execution Contract）](06-codex-execution-contract.md) 复核当前 Issue／远端状态与必读材料，本 executor 不把旧检查点写成新网络核验。许可法条与全库终审沿用 [验证及完成定义（Validation / Definition of Done）](05-validation-and-definition-of-done.md)，本文只固定本批窄合同。

## 选择、价值与边界（Selection / Value / Boundary）

| UID／不变身份 | 唯一正文候选 | 本次单页边界；原 UID 总体边界仍待定 |
| --- | --- | --- |
| `methodology:linkml-schema-first`／`METHODOLOGY-LINKML` | `https://linkml.io/linkml/` | 当前文档首页实际响应；不含 tutorial／specification／其他文档。是否要求完整多页方法文档待决 |
| `vocabulary:schema.org`／`SCHEMA.ORG` | `https://schema.org/docs/schemas.html` | Schemas／Organization of Schemas 本页；不含 type／property 独立页、完整 Vocabulary／release 或外部扩展。总体目标待决 |

真实增量是补上旧包未留存的原 HTML，让远程 agent 能复查正文、结构／链接损失及源→派生定位，并改善既有 LinkML 消费链；不是增加 complete 数量。新 `selected_response_version` 获取前未赋值，后续只表示本页本次 UTC 响应，不冒称 release、部署 commit、HTTP Date 或聚合生成时间。

工作假设（working hypothesis）为现 `dated_html_response` 可零代码保真消费，实际 DOM／许可／重定向仍未观察。若需要正文容器 selector、不同 URL、编码处理、组合 NOTICE 或必要媒体，先据实修订窄合同及精确路径，再实现／包装；无默认代码或测试授权。若许可无法闭合、现 helper 无安全连续摘句或必须扩大产品目标／递归多页，该 UID 保留旧包并记录具体 unresolved，不新建框架。

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

主线审阅并发布 startup 后，唯一正文 allowlist 才允许各页一次获准 GET，先暂存于公开树外。核实际版权／Terms、authored body、内嵌组件及必要媒体；新完整 carrier 的确切范围闭合前，不把新增 bytes 放入公开 repo。条件复用 `raw_data/licenses/apache-2.0.md` 与 `raw_data/licenses/cc-by-sa-3.0.md` 的完整文本，不修改共享法条；完整归属、来源／许可／修改说明、真实 upstream NOTICE（若有）及 BY-SA 适配物的 ShareAlike 义务按既有计划执行，不把集合独立作品或 GS1／Croissant 等外链包进授权。

许可对应关系可有界复核上述官方入口及 LinkML `https://linkml.io/linkml/_sources/index.rst.txt`，后者只作文档对应证据，不是第二正文。实际 body img／object 逐件判断角色与许可；需要新增媒体或历史 NOTICE 副本时，先列真实 URL／精确 carrier 路径并修合同，不递归取主题／全站资源。许可 unknown 时暂停该 UID 新 bytes 的公开包装、记录 unresolved，旧材料不删、不降级。

## 真实响应、配对重放与历史（Actual Response / Paired Replay / History）

后续记录真实 requested／resolved URL、开始／完成 UTC、HTTP status／content-type、bytes／既有 revision 与 attempts；不从成功推 HTTP200，也不把旧响应量或生成时间充当新 GET。现 sidecar 要唯一主响应 requested=resolved=approved、实际 HTTP200／HTML、四方许可绑定和真实 source→derived selectors；发生 redirect、非 UTF-8 或非静态正文先停包装并修合同，不修改原件适配验证。

复用现表示：`materialization.document`／`normalized_document` 指向 `normalized/document.md`，`retained_text_binding=dated_html_response`，`retained_text_sources` 恰为 `{source: source/specification.html, format: html}`，新 sidecar 为 `normalized/selectors.jsonl`；selectors 同时保留旧 `selectors.jsonl`。新当前 `status=partial` 是合同限制，版本／revision 只依据实际响应设置；上述均是待实施接口，不是 after。

原 HTML 字节／编码／链接不改；normalized 是采集器格式转换（collector-derived format conversion），不是 raw quotation。C、capsule snapshot、manifest 与 R 当前包四方绑定真实响应；完整旧 manifest／retrievals／generated_at／null 或缺省版本及全部既有 history 进入历史，旧 root `document.md`／`selectors.jsonl` 字节只读保全，不追加新 footer。新 normalized EOF 才有唯一附注；旧 NOTICE 能复用就保留原 bytes，若需组合／替换，先明确旧实物保全方案与精确新增路径。现 dated helper 只读单一 body，wiki 专用 `content_selector` 不能直接套用；导航污染或容器选择问题须先观察、修窄合同与最小泛化回归，不新增 mode／adapter。

## 两条既有 LinkML 消费链（Existing Consumer Chains）

| 既有链 | 后续必须独立复核 |
| --- | --- |
| `claim:583280271287ef9c` ← `evidence:b0f0f32b0b4cc957` ← 旧 `document.md#L6-L7`；来源报告断言（source-reported assertion） | 现消费者改读实际 normalized／sidecar，取连续实际正文，非导航／代码／通知或清理锚点后的伪引文；版本、消费文件 provenance、rights_refs、转换／partial 限制及 Wiki source／claim／map 都对应。新段落未读，不预填 literal，不静默丢链或手造新摘句 |
| `claim:27f7e77bbaa0d47f` ← `evidence:d3ebb3860ae3f34c` ← C `#collection.inclusion_reason`；采集者判断（collector assessment） | 原 inclusion_reason 与 metadata field selector 保留；source_hash／version 的空值语义及 candidate 状态不误标新页面断言或网页许可来源。必要 build ID／依赖传播不改变认识性质 |

两条既有 candidate 的实际结果须完整说明；若现摘句器无安全段落，先停并修合同，不强留数量或假旧定位。Schema.org 继续不新增 selected／claim；其他来源知识语义不改。

## 冻结、验证与独立终审（Freeze / Verification / Independent Review）

1. 主线核最新 work／唯一 writer，审阅并发布两文档 startup，再执行获准暂存 GET；影响同一输入的 base 移动须刷新合同。
2. 每页实物核身份、许可、正文自然首／中／末、heading／列表／表／代码／链接及真实组件；闭合后单一 writer 包装。仅首次两个新派生文件都不存在时用现 replay `check_derived=False` 一次，随后严格正常 replay。全 inventory／selectors／preview 与原→派生保真核对，旧 doc／root selectors／完整 history 对照 BASE 保全。
3. 仅现 `rebuild_registry`／`write_indexes_and_audit` 重建必要 index／registry／completeness；确定性聚合时间沿用 `2026-09-16T04:30:26Z`，不是 GET 时间。C、R、K、capsules 及必要已修订代码输入最终冻结后才 `make demo`；若 demo 后实际知识观测需纠偏 K，先重新冻结再 demo／repro，不能最后改 R/K 留 stale build identity。
4. 未来用当前统一运行时 `/tmp/llm-wiki-ci-312-260916/bin/python` 执行 `make test`、`make validate`、`make reproducibility`，以及当前 head 的 materialization completeness、默认 coverage auditor 和 publication-rights 检查；禁止默认全局 materialize-all 取网页。新 scope 错误须为零，全库继承 root blocks／旧错误照实报告，不以两个 allow 宣称全库通过。
5. 各 UID 两次禁网、禁止清目录的正常既有入口 offline replay；fresh candidate checkout／index export 仅依赖 repo，验证原 HTML、normalized、NOTICE 与新旧定位器可读及重复稳定。这不是 remote/main fresh checkout 验收。控制生成路径仅由现 generator 重建必要两 LinkML 链及全局 identity；审查其他213来源对象、其他129 K 对象／其他 R 与知识语义无无关改写。
6. 真实六维 after／剩余缺损／下一桶最后据实报告，原 UID 总体边界未定与 unresolved 保留。非作者 evaluator 锁最终 exact HEAD／BASE，分别评估需求满足（requirements）、agentic 判断链与证据、核心质量（core quality）；最终三维结论及当前 CI 必须真实取得。相关输入再变须重验，作者本轮不自评 PASS、不授权 merge。

## 明确非结果与停线（Non-results / Stop Conditions）

本轮未 GET 正文、未留存原 HTML、未设置响应版本／HTTP／UTC／bytes／after，未改 C/R/K、源码、测试、capsule、许可载体或生成物，未跑 tests／generators／全局 facts，未提交／push／创建 PR。独立评估与最终 CI 均 pending；未宣称完整 LinkML 文档、完整 Schema.org Vocabulary／release、两个 UID strict complete、全库 public gate PASS、main 落地、Issue #3/#4 关闭或 trusted 晋升。网络／许可单 UID 失败如实 unresolved；观察所需 selector、redirect、carrier／媒体或总体产品边界改变时先修合同，不擅自扩大。当前仅提交启动状态供主线审阅，到此停写。

---
phase: P3-PDF-05
status: startup_not_acquired
base_sha: d5c6d8882ea2b8a783047ceed0285c652b1bd2cf
coverage_summary: {"collection_records":215,"non_repo_total":131,"github_repo_excluded":84,"reported_content_tier_counts":{"excerpt_capsule":23,"full_text":97,"metadata_capsule":11},"source_type_counts":{"arxiv":73,"biorxiv":2,"blog":10,"industry":2,"journal":11,"methodology":7,"paper":2,"standard":24},"original_artifact_counts":{"complete":47,"metadata_only":13,"partial":4,"unknown":67},"text_extraction_counts":{"complete":8,"partial":54,"unavailable":13,"unknown":56},"action_bucket_counts":{"access_restricted":9,"author_manuscript_fetch":2,"complete_verified":8,"html_article_snapshot":11,"identity_or_version_ambiguous":3,"needs_boundary_verification":55,"ocr_assessment":31,"parser_only":6,"public_persistence_decision":4,"standard_spec_fetch":2},"public_redistribution_counts":{"allow":33,"block":65,"unknown":33},"content_inspected_full_text":55,"structure_only_full_text":42,"locally_persisted_complete":8,"knowledge_candidate_sources":30,"knowledge_trusted_sources":0,"knowledge_sources_without_demo_claims":101,"unresolved_sources":123}
---

# P3-PDF-05 — 三篇固定版本论文 PDF 表示启动合同

```yaml
execution_contract:
  plan_id: nonrepo-materialization-main-convergence-260916
  phase: P3-PDF-05
  status: startup_not_acquired
  base_branch: work/v0-meta-kb-initialization-demo-260910
  base_sha: d5c6d8882ea2b8a783047ceed0285c652b1bd2cf
  implementation_branch: codex/p3-pdf-05-260917
  head_sha: null
  target_branch: work/v0-meta-kb-initialization-demo-260910
  pull_request: null
  prerequisite:
    pull_request: 22
    state: merged
    merge_commit: d5c6d8882ea2b8a783047ceed0285c652b1bd2cf
  adapter_family: arxiv_latex_v2
  action_bucket: open_fulltext_fetch
  source_uids: ["arxiv:2410.07095", "arxiv:2503.18102", "arxiv:2504.01848"]
  selected_versions:
    "arxiv:2410.07095": v6
    "arxiv:2503.18102": v1
    "arxiv:2504.01848": v3
  fixed_authority_urls:
    "arxiv:2410.07095": https://arxiv.org/abs/2410.07095v6
    "arxiv:2503.18102": https://arxiv.org/abs/2503.18102v1
    "arxiv:2504.01848": https://arxiv.org/abs/2504.01848v3
  sole_body_get_candidates:
    "arxiv:2410.07095": https://arxiv.org/pdf/2410.07095v6
    "arxiv:2503.18102": https://arxiv.org/pdf/2503.18102v1
    "arxiv:2504.01848": https://arxiv.org/pdf/2504.01848v3
  production_code_changes: none
  license_packaging: three_self_contained_pdf_supplement_NOTICES_no_new_raw_license_file
  license_text_source: raw_data/licenses/cc-by-4.0.md
  startup_only_writes:
    - docs/plans/260916-corpus-completion-main-convergence/p3-pdf-05-fixed-version.md
    - docs/plans/260916-corpus-completion-main-convergence/branch-ledger.yaml
  allowed_paths:
    - docs/plans/260916-corpus-completion-main-convergence/p3-pdf-05-fixed-version.md
    - docs/plans/260916-corpus-completion-main-convergence/branch-ledger.yaml
    - "raw_data/arxiv/MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering/metadata.yaml"
    - "raw_data/arxiv/AgentRxiv: Towards Collaborative Autonomous Research/metadata.yaml"
    - "raw_data/arxiv/PaperBench: Evaluating AI's Ability to Replicate AI Research/metadata.yaml"
    - materialized_sources/corpus/arxiv-2410.07095--b72cdb8f/source-metadata.yaml
    - materialized_sources/corpus/arxiv-2410.07095--b72cdb8f/manifest.yaml
    - materialized_sources/corpus/arxiv-2410.07095--b72cdb8f/pdf-supplement/document.pdf
    - materialized_sources/corpus/arxiv-2410.07095--b72cdb8f/pdf-supplement/NOTICE.md
    - materialized_sources/corpus/arxiv-2410.07095--b72cdb8f/pdf-supplement/document.txt
    - materialized_sources/corpus/arxiv-2410.07095--b72cdb8f/pdf-supplement/selectors.jsonl
    - materialized_sources/corpus/arxiv-2503.18102--1133e9d5/source-metadata.yaml
    - materialized_sources/corpus/arxiv-2503.18102--1133e9d5/manifest.yaml
    - materialized_sources/corpus/arxiv-2503.18102--1133e9d5/pdf-supplement/document.pdf
    - materialized_sources/corpus/arxiv-2503.18102--1133e9d5/pdf-supplement/NOTICE.md
    - materialized_sources/corpus/arxiv-2503.18102--1133e9d5/pdf-supplement/document.txt
    - materialized_sources/corpus/arxiv-2503.18102--1133e9d5/pdf-supplement/selectors.jsonl
    - materialized_sources/corpus/arxiv-2504.01848--006ccffe/source-metadata.yaml
    - materialized_sources/corpus/arxiv-2504.01848--006ccffe/manifest.yaml
    - materialized_sources/corpus/arxiv-2504.01848--006ccffe/pdf-supplement/document.pdf
    - materialized_sources/corpus/arxiv-2504.01848--006ccffe/pdf-supplement/NOTICE.md
    - materialized_sources/corpus/arxiv-2504.01848--006ccffe/pdf-supplement/document.txt
    - materialized_sources/corpus/arxiv-2504.01848--006ccffe/pdf-supplement/selectors.jsonl
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
    - materialized_sources/corpus/arxiv-2410.07095--b72cdb8f/source-metadata.yaml
    - materialized_sources/corpus/arxiv-2410.07095--b72cdb8f/manifest.yaml
    - materialized_sources/corpus/arxiv-2410.07095--b72cdb8f/pdf-supplement/document.txt
    - materialized_sources/corpus/arxiv-2410.07095--b72cdb8f/pdf-supplement/selectors.jsonl
    - materialized_sources/corpus/arxiv-2503.18102--1133e9d5/source-metadata.yaml
    - materialized_sources/corpus/arxiv-2503.18102--1133e9d5/manifest.yaml
    - materialized_sources/corpus/arxiv-2503.18102--1133e9d5/pdf-supplement/document.txt
    - materialized_sources/corpus/arxiv-2503.18102--1133e9d5/pdf-supplement/selectors.jsonl
    - materialized_sources/corpus/arxiv-2504.01848--006ccffe/source-metadata.yaml
    - materialized_sources/corpus/arxiv-2504.01848--006ccffe/manifest.yaml
    - materialized_sources/corpus/arxiv-2504.01848--006ccffe/pdf-supplement/document.txt
    - materialized_sources/corpus/arxiv-2504.01848--006ccffe/pdf-supplement/selectors.jsonl
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
    semantic_source_change_uids: ["arxiv:2503.18102"]
    semantic_source_page: experiments/v0_meta_kb_initialization_demo_260910/05_wiki/sources/arxiv-2503.18102.md
    other_generated_changes: existing_generator_required_build_identity_inventory_and_dependency_propagation_only
    demo_selection_and_claim_admission: unchanged
  retrieval_attempts: []
  body_http_status: null
  retrieved_at: null
  bytes: null
  actual_page_counts: null
  authors_verified_from_originals: null
  independent_evaluation: pending_actual_committed_head_and_base
  final_ci: pending_actual_committed_head_and_base
  explicitly_out_of_scope:
    - ALCE_arxiv_2305_14627_input_body_and_publisher_adaptation_separate_successor
    - every_other_uid_and_new_collection_source
    - new_raw_data_license_file_or_modification_of_existing_license_text
    - source_archive_history_bare_latest_other_version_or_publisher_fallback
    - legacy_source_normalized_root_selectors_revision_retrievals_rights_and_source_gate
    - recursive_references_datasets_code_weights_or_benchmark_execution
    - production_code_tests_adapter_framework_dependency_workflow_or_global_schema_changes
    - default_OCR_lossless_formula_or_all_figure_linearization_as_exit_gate
    - new_demo_selection_claim_assessment_or_trusted_promotion
    - main_PR1_ready_merge_issue_closure_branch_deletion_force_push_or_history_rewrite
```

## 1. 启动事实与选择（Startup Facts and Decision）

本轮只交付启动文档，不是正文取得或验收报告。主线已全文读取计划、Issue #3/#4 并完成只读预核（read-only preflight）：PR #22 已正常合入 work，远端／本地 work 均为上述 exact base；PR #1 仍 Draft、base 为 main@99ce4670be91637209d67792de0962404fa96488，Issue #3/#4 仍 open。PR #22 的精确审核与 CI 记录只在 branch-ledger 登记，不复用为 PDF05 的审核结果。

工作假设（working hypothesis）是“同一作品增加独立正文表示（representation），不追溯改写旧 source 包”。采用 planner 推荐的串行拆分：MLE-bench v6、AgentRxiv v1、PaperBench v3 由现有 helper 接入，零生产代码修改；备选的四 UID 同批方案需要 publisher 表示接缝，会扩大本批代码范围，因此未采用。ALCE（arxiv:2305.14627）保留为独立后继，正式出版正文有可得／作品授权路径，但接入合同待定；本批不改其身份、材料、许可或消费者正文事实。

主线于 2026-09-17 确认 [MLE-bench v6](https://arxiv.org/abs/2410.07095v6)、[AgentRxiv v1](https://arxiv.org/abs/2503.18102v1)、[PaperBench v3](https://arxiv.org/abs/2504.01848v3) 的官方固定版记录，各实际 view license 均指向 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。这只是身份／作品许可链证据，不是 PDF GET、HTTP 200、实际 PDF 作者／页数／bytes／retrieved_at 或信用核验；这些结果保持未填。

frontmatter 来自当前覆盖台账 K 的 summary，固定分母为 215=131+84；原件 complete=47、text partial=54、严格 complete／locally persisted=8、unresolved=123。启动文档没有改变任何来源状态，也没有预测完成数。

## 2. 六维 Before（Six-dimensional Before）

K = raw_data/audits/non_repo_materialization_coverage_2026-09-16.yaml，按完整 UID 定位；C 为合同列出的 canonical metadata，R 为对应 capsule 根。下表是当前 K 的正式状态与本地记录，不是新语义验收；三份 C/capsule metadata 的 versioning.source_version 均 null，根 manifest source_version 键缺省，均无 pdf_supplement／本地 PDF。

| UID／目标 | 身份与版本（Identity/version） | 原件（Original artifact） | 提取（Text extraction） | 本地持久化（Local persistence） | 公开再分发（Public redistribution） | 知识准入（Knowledge admission） |
| --- | --- | --- | --- | --- | --- | --- |
| arxiv:2410.07095／MLE-bench | K selected_version=null；旧 bare source 未绑定 vN；新选择 v6 尚未持久化 | unknown／unverified；R/manifest.yaml 的 inventory/omitted 是结构证据；无 PDF | unknown／unverified；R/normalized/document.txt 1450 行／89147 字符，53 root selectors；语义边界未核验 | K present/tracked=true；15 inventory files；fresh_checkout=false；complete_target_consumable=null；root selectors resolved | K state/reported_gate=block、revision_matches=true；旧作品 BY4 正向证据不等于新 PDF allowance | state=null、无所选 demo claims，不伪造 candidate |
| arxiv:2503.18102／AgentRxiv | K selected_version=null；旧 bare source 未绑定 vN；新选择 v1 尚未持久化 | unknown／unverified；R/manifest.yaml 的 inventory/omitted 是结构证据；无 PDF | unknown／unverified；R/normalized/document.txt 902 行／64692 字符，52 root selectors；语义边界未核验 | K present/tracked=true；15 files；fresh_checkout=false；complete_target_consumable=null；root selectors resolved | K state/reported_gate=block、revision_matches=true；新 PDF allowance 尚不存在 | candidate=2；保持 candidate，不改变 trust |
| arxiv:2504.01848／PaperBench | 精确 colon UID；K selected_version=null；旧 bare source 未绑定 vN；新选择 v3 尚未持久化 | unknown／unverified；R/manifest.yaml 的 inventory/omitted 是结构证据；无 PDF | unknown／unverified；R/normalized/document.txt 1542 行／101772 字符，56 root selectors；语义边界未核验 | K present/tracked=true；15 files；fresh_checkout=false；complete_target_consumable=null；root selectors resolved | K state/reported_gate=block、revision_matches=true；新 PDF allowance 尚不存在 | state=null、无所选 demo claims，不伪造 candidate |

旧表示的补充观察来自 planner 已读的有限本地证据，独立于 K 的 unknown：MLE-bench 的 R/source/iclr2025_conference.tex 有主文／附录，缺八项实际引用科学图；AgentRxiv 的 R/source/main.tex 有算法／配置／并行实验及末 Prompts，缺六项实际引用图，旧注释 Conclusion 不当作结尾；PaperBench 的 R/source/example_paper.tex 是真实正文，含附录与两段 Task Instructions，缺七项活动图。K 的 omitted=9／9／20 不分别等于九／九／二十个正文缺口；空 missing 列表不表示已核验无缺失。旧 ICLR/GDM/ICML 样式、bib 摘要、LUMI 用途条件等独立限制与 root block 保留，不因新 PDF 一并放行。

## 3. 表示与文件责任（Representation and File Responsibility）

手写输入仅限三份 C 的新选版／嵌套 PDF allowance、对应审计条目与本报告／台账；capsule metadata 保持一致。每个 R 恰新增 pdf-supplement/document.pdf、NOTICE.md、document.txt、selectors.jsonl：原 PDF 不改；NOTICE 自包含该原件实际作者顺序、题名、固定来源／版本、可见归属与独立信用、转换说明、许可链接及完整 BY4 法律文本。完整法条复用现有 raw_data/licenses/cc-by-4.0.md，不重抓许可、不新建 raw_data/licenses 文件，不以跨文档引用代替 NOTICE 自包含履约。

新 allowance 必须在 C、capsule metadata、manifest.pdf_supplement、rights review 四处一致，绑定真实新表示；尚未取得时不预填 revision／inventory／retrieval／allow。旧 source、normalized、root selectors、NOTICE、README、files.jsonl，以及 root revision/retrievals/rights/materialization 和 source_version 键缺省不改。未来 durable 化 C/capsule 的选版仅代表新 PDF 选择，不证明旧 archive GET 曾取得该 vN。

generated_paths 是后续现有 generator 的受控范围（controlled patterns），本轮没有运行。正文／evidence 语义变化只为既有 selected AgentRxiv 及其两个 candidate 的来源链；MLE-bench／PaperBench 不新增 selection。其余范围仅容许必要 build identity／清单／依赖机械传播，不改变未受影响来源的正文、claim 判断或 admission；ALCE 不据此被表述为已接入。若实际路由／差异超出此边界，停止并回 planner，而非扩写生成框架。

## 4. 后续验收与未决（Planned Verification and Unresolved）

每 UID 实际正文 GET 只使用合同中的唯一固定 URL；发布启动合同前不执行。实际尝试后逐项记录 URL、时间、响应／错误、最终选择与 before→after。当前三 UID 的正文 after、原件核验、提取质量与公开新包均未执行；retrieval_attempts=[]，无新 PDF 作者／页数／bytes／retrieved_at 结果。

实际原件逐 UID 核题名／作者／总页数、开中尾至少三页、主文与附录结尾，并核 MLE-bench 结果表／deadline 图、AgentRxiv 六活动图／并行结果／算法与末 Prompts、PaperBench JudgeEval／rubric 图／两段 Task Instructions。新增 selectors 核首中末语义范围；native 缺页、图内文本／数学／字面 prompts 损失具体记录。原件 complete 与 text partial 可以并存；不设全图 OCR、数学无损或全文完美线性化的新退出门槛。

后续在实际 head 按影响执行 make test、make validate、make reproducibility、python scripts/validate_materialization_completeness.py 及 python scripts/audit_non_repo_coverage.py 的只读对账；AgentRxiv 正文 evidence 输入变化需 make demo 后再 validate／reproducibility。这里列的是验收命令，不是本轮实绩。

单 UID 若唯一 URL 失败、身份／选版不符、信用或独立限制未闭合、附录缺失或提取失败，记录具体 unresolved 与最小 next action，可继续其他独立 UID；不自动换 bare latest、其他版本、archive、作者仓库 PDF 或引用网络。合法取得但不能公开，记录 public_persistence_decision，不伪装成网络失败。base 移动影响相同输入／生成物、同 UID 其他 writer、需要新 scope／身份／存储或验证修复超范围时，整批停止。

独立评估门控（independent evaluation gate）仍按 05§8.1：evaluator 不得是作者，锁定最终 exact head/base，分别判需求满足、agentic 判断与证据链、核心质量，三维及 overall 均须 PASS；当前全为 pending。适用 CI 必须属于同一实际 head/base，当前 pending；任何相关变化重新审核。通过后按正常 merge 回 work，不沿用 PR22 的 PASS 或 CI，也不由 executor 自评放行。

## 5. 本轮已做与明确未做（Executed Scope and Explicit Non-results）

已全文读八份计划文件与 planner，定点读取当前 K 三条／summary、既有完整 BY4 文本及 selected AgentRxiv 定位；仅通过 apply_patch 写本报告与 branch-ledger。台账登记 PR22 absorbed，并将唯一 active implementation 改为 PDF05；新 PR 号与 head 保持 null。

本轮未执行任何正文／source archive GET、原件取得、NOTICE 履约写入、source／manifest／audit／registry 变更、generator、tests 或 validators；没有本轮 CI 或独立 evaluator PASS。未 Git／PR 写入、未进入 work 或 main、未完成 P4/P5、未晋升 trusted、未关闭 issue、未删除／迁移文件、未删分支／强推／改写历史。三 UID 仍待真实取得与审读，ALCE 等待独立后继合同。

---
phase: P3-PDF-05
status: implemented_locally_validated_pending_independent_review_and_ci
base_sha: d5c6d8882ea2b8a783047ceed0285c652b1bd2cf
coverage_summary: {"collection_records":215,"non_repo_total":131,"github_repo_excluded":84,"reported_content_tier_counts":{"excerpt_capsule":23,"full_text":97,"metadata_capsule":11},"source_type_counts":{"arxiv":73,"biorxiv":2,"blog":10,"industry":2,"journal":11,"methodology":7,"paper":2,"standard":24},"original_artifact_counts":{"complete":50,"metadata_only":13,"partial":4,"unknown":64},"text_extraction_counts":{"complete":8,"partial":57,"unavailable":13,"unknown":53},"action_bucket_counts":{"access_restricted":9,"author_manuscript_fetch":2,"complete_verified":8,"html_article_snapshot":11,"identity_or_version_ambiguous":3,"needs_boundary_verification":52,"ocr_assessment":34,"parser_only":6,"public_persistence_decision":4,"standard_spec_fetch":2},"public_redistribution_counts":{"allow":33,"block":65,"unknown":33},"content_inspected_full_text":58,"structure_only_full_text":39,"locally_persisted_complete":8,"knowledge_candidate_sources":30,"knowledge_trusted_sources":0,"knowledge_sources_without_demo_claims":101,"unresolved_sources":123}
---

# P3-PDF-05 — 三篇固定版本论文 PDF 表示：启动合同与执行结果

当前：PR23 启动后取得三份固定版原件，审读后按表示级授权保存 PDF／TXT／定位器／NOTICE；原件 complete、文本 partial，未晋升 strict complete／trusted。本地测试、重放与覆盖核验通过，全库公开限制另列；PR仍Draft，最终独立审核与同一head/base的CI均待完成。下方合同及第1–5节保留启动时历史；真实获取、内容判断和执行结果见第6–8节，frontmatter为当前覆盖汇总，不是启动基线。

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

启动时 frontmatter 来自当时覆盖台账 K 的 summary，固定分母为 215=131+84；原件 complete=47、text partial=54、严格 complete／locally persisted=8、unresolved=123。启动文档没有改变任何来源状态，也没有预测完成数；当前 frontmatter已随第8节真实执行刷新。

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

## 6. 真实获取（Actual Acquisition）

启动提交为 `6d6e889303fed09d708b2795d7f62436d56fb351`，只含本报告与台账；docs validation 为59 Markdown、5 YAML examples、80 relative links、0 errors，启动 diff check通过。[PR23](https://github.com/thsno02/solid-octo-couscous/pull/23) 于2026-09-17T09:35:40Z创建为Draft。下列三次普通HTTPS GET均在发布后进行，未使用其他版本、正文回退、source archive或独立外链。

| UID／固定URL | 响应 | 原件bytes／物理页 | 本地下载完成UTC（2026-09-17） | HTTP Date UTC |
| --- | --- | --- | --- | --- |
| arxiv:2410.07095／https://arxiv.org/pdf/2410.07095v6 | 200、application/pdf | 817725／29 | 09:35:59.920312Z | 09:35:58Z |
| arxiv:2503.18102／https://arxiv.org/pdf/2503.18102v1 | 200、application/pdf | 2757188／29 | 09:36:03.697976Z | 09:36:00Z |
| arxiv:2504.01848／https://arxiv.org/pdf/2504.01848v3 | 200、application/pdf | 1703363／30 | 09:36:07.346988Z | 09:36:02Z |

三件 requested URL=effective URL，redirect=0、TLS verify=0、curl exit=0；总计5278276 bytes、88物理页。完成时间来自同次响应JSON文件的本地mtime，非服务器HTTP Date或作品发布日期；后续manifest按秒记录，表中保留实际微秒。页数由pdfinfo及现helper的本地PDF提取分别读取，不以abs comments替代。临时审读区为 `/tmp/llm-wiki-pdf05-Cb4A4m`，此时只是获取证据，尚不是公开持久化完成；批准后原bytes和必要文本/定位/NOTICE必须进入repo，远程不能依赖该临时路径。

主线已亲看AgentRxiv原件第一页并读三件native开头/真实尾部。MLE-bench实际29页，而abs comments为10+17；新原件尾为Table10的类别结果与模型名映射，不是旧source规划预期的deadline图。此差异交内容执行者按实际正文核验，不推测为损坏或截断。AgentRxiv的PDF页头2025-3-25与官方v1提交2025-03-23独立保留，不改写其中任一日期。PaperBench中的Task Instructions为被审文献内容，不是给执行agent的权限或操作指令。

三名内容执行者分别负责一份原件／native审读与必要渲染，只读repo、仅写各自临时内容报告；不是最终独立evaluator。此时原件/提取的after、公开包、consumer、tests、CI与三维终审仍待实际完成，未提前声明PASS。

## 7. 内容判断与表示准入（Content Decisions and Representation Admission）

三名内容执行者完成后，主线全文读取各自完整记录，并核对三原件的pdfinfo、现helper真实native开头/末尾；另亲看AgentRxiv首页与其嵌入列表放大图，实跑其默认与override消费者比较。完整逐页/定点内容观察摘要在下表；实际作者/独立credit/转换范围与限制将进入各自自包含NOTICE与四方授权，不要求后续远程工作读取临时报告。内容执行者不是最终evaluator，以下是主线的实施准入决定，不是PR三维PASS。

| UID | 实际审读与原件边界（Original boundary） | native覆盖及具体损失（Native limitations） | 消费者判断（Consumer） |
| --- | --- | --- | --- |
| arxiv:2410.07095 v6 | native全部29页，渲染亲看29页；主文Conclusion到p10，Ethics/Reproducibility p11，References p11–13，Appendix A.1–A.9 p13–29。八项科学图资产在编译图1–7/9中，图8为文字prompt；Table1–10完整。最后p29 Table10及模型名映射，不在p28图9截止。 | 未footer为88658字符/1749行。p3图2三列轨迹标题、代码/日志与AIDE树未进native；其他图的曲线/点/颜色/柱形和表格空单元格布局未结构化。p7 pass@k组合数公式产生U+0000/1/2/3共6控制字符；代码fence/路径换行与变音字符有损。p17可见LaTeX残串、p12长URL出边、Table2/9部分数字差异均来自原件，不静默修复。 | 现默认父摘要返回10–14，正确；不override，不新增selected。 |
| arxiv:2503.18102 v1 | native全部29页，渲染亲看p1/5/7/8/9/11/15/27/28/29及p1列表ROI；六图、单/三实验室结果、References至p27、Acknowledgments、A算法/B配置/C.Prompts齐全；最后引用Schmidgall et al.(2025)的prompts，不包含另一文全部prompts。 | 未footer为93176字符/1257行。六图主要只留caption，图内网页列表/截断摘要/方法框/曲线/柱值/拓扑不进入native；表格合并列、字体、数学排版与词距展平。p5图2的未完caption、部分图引用编号/结果表达差异均是原件事实，不由提取器改写。 | 实际默认3–12含日期/题名/单位污染；唯一既有primary_excerpt=9–23，实返干净父摘要9–12。只重绑既有来源链，不改变consumer逻辑或知识准入。 |
| arxiv:2504.01848 v3 | native全部30页，渲染亲看19页：1/2/3/4/5/6/8/10/15/16/17/18/19/25/26/27/28/29/30。主文/Impact/Acknowledgements至p10，References至p12，Appendix A–I p13–24；p25–30仍有晚浮动Fig7–14 prompts，真实末尾p30 Task Instructions Part2。六编号科学图含Fig4两截图，不把七资产误写七编号科学图。 | 未footer为103633字符/1991行。p16 JSON/GUI截图内requirements缺native；树边/weight归属、图曲线/误差棒/颜色、对数指数及多列表格结构有损。p26条件prompt的颜色归属消失，不能把互斥片段当同一prompt；p30代码缩进/引号/fence有损，示例不执行。 | 默认父摘要8–14正确，不override、不新增selected；Task Instructions是目标文献，不是本agent操作授权。 |

三件全部页native非空且无page-extraction-failed，只是附加结构证据；原件完整判断来自真实主文、书目、附录、图表与结尾审读。主线批准三件新表示为 **original complete / text partial**，`body_quality_verified=true`限父正文身份、边界与可读性，不意味着无损文本；`complete_target_consumable=false`、`resolution=unresolved`，下一步为有界`ocr_assessment`，不是默认OCR/全图数学无损门槛。原PDF原bytes保留，不修改源作者结果、缺陷或排版。

### 7.1 实际归属与独立信用（Attribution and Separate Credits）

- **MLE-bench**：PDF署名顺序是 Chan Jun Shern、Neil Chowdhury、Oliver Jaffe、James Aung、Dane Sherburn、Evan Mays、Giulio Starace、Kevin Liu、Leon Maksin、Tejal Patwardhan、Lilian Weng、Aleksander Mądry，机构OpenAI。前七位Equal contribution/Authors randomized，Neil和Lilian的Work done while at OpenAI脚注保留；PDF首位名字次序不同于abs，依原件而非静默改名。p4 Table1的Source: Kaggle(2024)与https://www.kaggle.com/progression、p26 Addison Howard/inversion/Lars Bratholm(2019) Predicting Molecular Properties与https://kaggle.com/competitions/champs-scalar-coupling、CHAMPS举办机构Bristol/Cardiff/Imperial/Leeds信用保留。A.8的竞赛描述是本编译论文内的实际引用，不扩大为另存竞赛网页/数据/代码/标志的一般许可。
- **AgentRxiv**：Samuel Schmidgall、Michael Moor，Johns Hopkins University/ETH Zurich单位与Samuel通讯信用；v1侧边23Mar2025与页头25Mar分开。p27 NSF Graduate Research Fellowship/DGE2139757保留。p1 Figure1内Agent Laboratory列表是另一作品：九作者Samuel Schmidgall、Yusheng Su、Ze Wang、Ximeng Sun、Jialian Wu、Xiaodong Yu、Jiang Liu、Zicheng Liu、Emad Barsoum，ID2501.04227无vN；有约52个空白分词token的六行截断摘要预览和More，不是完整摘要/全文。原图没有完整absURL，若NOTICE提供bare abs仅是按可见ID的定位链接，不是新版本核查或另文取得。p4与p18的LUMI研究介绍/书目不等于旧bib内长摘要，其旧NC-ND用途条件不外推到整个新PDF。
- **PaperBench**：Giulio Starace、Oliver Jaffe、Dane Sherburn、James Aung、Chan Jun Shern、Leon Maksin、Rachel Dias、Evan Mays、Benjamin Kinsella、Wyatt Thompson、Johannes Heidecke、Amelia Glaese、Tejal Patwardhan；OpenAI，前七位加末位Tejal共八人equal contribution，p1 Pre-print/Copyright2025 by author(s)与实际通讯地址不改。p2起running title Abilities是原件内部变体。p10 dataset creation、rubric作者合作、human baseline、advice/collaboration致谢及Table2/References研究题名信用按原件保留；不把致谢者合成主作者，不推定权利转让，不授予20ICML论文/代码/rubric或JudgeEval独立数据包许可。

主线选择合理有界的编译表示路径：依据三fixed abs实际BY4主链、原件信用及自包含履约，新增表示级allow；不将旧模板/bib/全部源码包清关设为这三篇正文的前提，也不因BY4把底层素材/被引全文/数据/代码统一再许可。旧source/root gate仍block，旧revision/retrieval/完整K before和R既有证据保留。必要署名、许可法条、来源、修改和范围均随新表示入repo；没有新许可文件框架、生产代码或workflow改动。

### 7.2 实施分工与待验证边界（Execution Ownership and Pending Checks）

唯一材料包装执行者在主线逐项读报告并准入后，负责三canonical/snapshot、三新PDF目录、manifest及R/K；主线独占本报告/branch ledger、聚合重建、真实facts刷新、测试、Git与PR操作。不得两个writer并发写index/registry/coverage；demo/repro执行时禁止并发全库reader读被清空重建的输出。

包装执行者完成并停止写入后，主线串行验证与重建。不能将三份内容报告、主线准入或离线结构校验当作最终独立PASS；最终evaluator将锁定新的已提交HEAD与BASE另行审核。实际已完成检查及保留项见第8节。

## 8. 执行结果与诚实边界（Execution Results and Limitations）

### 8.1 持久化、消费链与历史保全

三份原始 PDF 共5278276 bytes进入各自 `pdf-supplement/`，同时保存自包含NOTICE（含既有完整CC BY4法条）、native TXT和逐页selector，共12个新文件。TXT包含NOTICE footer后的字符/行数分别为MLE-bench 91086/1761、AgentRxiv 95861/1269、PaperBench 106801/2003；新定位器29+29+30=88。canonical、snapshot、manifest及R中三新表示授权一致。这里是新表示的allow，不是旧source包解除block；不存在新增raw license文件、生产代码、测试代码、依赖、workflow或全局schema修改。

新文件加入Git索引后，实际facts确认三份声明文件全部在场且被Git跟踪；没有宣称本轮fresh checkout或最终main交接完成。当前台账的128个非目标observed逐项等于实际facts；128个非目标K条目和105个非目标R条目相对BASE不变。三项K的完整旧条目另存 `historical_pre_pdf_supplement_coverage`，不是用after覆盖before。

主线对照BASE验证42个旧库存文件（不含本次更新的source-metadata快照）逐字节未变；53+52+56=161个旧root selectors保留。旧root manifest的version键仍缺省，原revision、retrieval、source文件、旧normalized正文、错误/警告/限制及旧权利决定保持；仅新增表示及必要local inventory/bytes发生变化。三项R的既有字段与证据前缀保留。

三胶囊各执行两次既有离线重放入口，禁用 `fetch_bytes` 与 `prepare_capsule`，每次包含20个实际文件的前后字节映射相同；没有联网、清空或丢失旧source。第一次诊断尝试因测试patch指向不存在的 `fetch` 而在运行重放前报错；改为真实 `fetch_bytes` 后六次均成功，未掩盖执行路径失败。

聚合使用既有 `write_indexes_and_audit`、`rebuild_registry` 和 `make demo`；保留确定性时间 `2026-09-16T04:30:26Z`，不将其冒充实际下载时间。demo为36 sources、72 evidence、72 claims、135 wiki pages、3 context packs，build为 `build:llm-wiki-v0:e55e8d731fd60066`。输入身份及必要依赖传播由生成器产生，不手改下游文本。

语义diff逐项确认：仅AgentRxiv的 `source:81e58c8add4ce203`、`evidence:3eb5d79a34cdce67`、`claim:07439fdff0cc0aa3` 改变。原有同一父摘要文字保持完全相同（literal quote changed=0），证据定位改为新TXT的L9–L12，并附固定版PDF许可和真实提取限制；一条既有父论文claim重绑，不新增claim。全部72个claim UID、72个evidence UID、36个source UID、collector assessment和candidate/trust状态不变，MLE-bench/PaperBench未加入selected。

### 8.2 六维 After 与全局计数

| 维度 | 本批三项 after | BASE → 当前汇总 |
| --- | --- | --- |
| 原件覆盖（Original artifact） | 三份fixed PDF的实际29/29/30页主文、书目、附录及尾部完整 | complete 47→50；unknown 67→64；partial4、metadata_only13不变 |
| 文本覆盖（Text extraction） | 三项partial；图中文字/布局/数学/条件颜色等具体损失见§7及各NOTICE | partial54→57；unknown56→53；complete8、unavailable13不变 |
| repo持久化（Persistence） | 原bytes/TXT/NOTICE/88selectors全部在场且tracked | 严格complete仍8，三项complete_target_consumable=false |
| 公开使用（Public reuse） | 三新PDF表示allow，旧root block保留 | root allow33/block65/unknown33不变；不是三个来源整体清关 |
| 知识消费（Knowledge） | 仅AgentRxiv既有两candidate中的父正文一项重绑；collector不改 | candidate来源30、trusted0、无demo claim来源101不变 |
| 后续处理（Resolution） | 三项unresolved，有界ocr_assessment，不强制OCR或新增全文GET | unresolved仍123；内容已审读full_text55→58、仅结构full_text42→39 |

固定分母215=131非repo+84排除的GitHub repo不变；97 full_text是reported content tier，不等于97完整全文。行动桶为access_restricted9、author_manuscript_fetch2、complete_verified8、html_article_snapshot11、identity_or_version_ambiguous3、needs_boundary_verification52、ocr_assessment34、parser_only6、public_persistence_decision4、standard_spec_fetch2。

R摘要有一项历史计数修正：以BASE实际条目重新数得30份主PDF+5份SI=35个独立allow（BY4=32/BY-SA4=2/BY4 AND Apache2=1），但旧summary仍写27+5=32、BY4=19。本轮真实新增仅3份主PDF，after为33+5=38，许可计数BY4=35/BY-SA4=2/BY4 AND Apache2=1；改summary不是新授予6份许可，更不是回改非目标条目。此前滞后的计数与本轮增量明确分开。

### 8.3 验证与合并门控

本轮运行环境为Python3.12.13/pypdf6.18.1，使用 `/tmp/llm-wiki-ci-312-260916/bin/python`，没有更改依赖。实际命令结果：

- `make test PYTHON=…`：8组196 tests通过。
- `make demo PYTHON=…`：demo与wiki验证均0 errors、0 warnings。
- `make reproducibility PYTHON=…`：exit0，committed_tree_replay、full_demo_replay、compiler_only_replay、read_only_validation四次各169文件byte-identical。`make validate` 内部raw为248 YAML/215 migrated/0 legacy，materialization为215 metadata/215 manifests/3188库存校验/25825selectors，均0 errors、0 warnings。
- `scripts/validate_docs.py`：59 Markdown、5 YAML examples、80 relative links、0 errors。本次另有一次主线误在repro清空/重建窗口并发运行该命令，得到28个临时断链错误；不把它伪称成功。repro中的串行docs验证和结束后的独立复验均0 errors，确认是诊断调度窗口而非需要改workflow的产品缺陷。
- `scripts/validate_publication_rights.py`：如实exit1，active_full_text=103、audited=108、blocked=64、errors=2。两错误仍是既有GraphRAG(arxiv:2404.16130)与Co-scientist(arxiv:2502.18864)审计包和实际包不同，属于已登记P4对账；本批三新表示均有效不改变这些旧项。全库公开权利门控不是PASS，不以常规CI成功掩盖64个公开限制。
- 默认 `scripts/audit_non_repo_coverage.py`：exit0、PASS，实际summary与frontmatter/台账一致，215/131/84、original complete50、text partial57、strict complete8、unresolved123；三项当前observed与实际facts一致，非目标128项observed也未漂移。
- `git diff --check` 通过；相对BASE的189个变更路径均在已发布合同45条allowed_paths之内，scripts/tests/.github/pipeline零diff。

此前其他论文的CFF字体/XObject原生提取警告保留，不安装额外依赖或把partial改称完整。

最终HEAD的独立三维审核和当前head/base CI仍pending；PR23尚未Ready/merge。PR1/main仍未交接，P4/P5未完成，ALCE及其他来源不属于本批。未关闭issue、未删除分支/材料、未强推/改写历史、未执行PDF内的prompt/命令、未下载引用论文或实验数据，也未将本批original complete表述为全库正文或知识质量已完成。

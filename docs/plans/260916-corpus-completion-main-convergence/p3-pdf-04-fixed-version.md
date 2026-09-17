---
phase: P3-PDF-04
status: local_validation_passed_final_exact_pair_review_and_ci_pending
base_sha: 252fb09236433435a1a07d9e50d10f5f447b60e6
coverage_summary: {"collection_records":215,"non_repo_total":131,"github_repo_excluded":84,"reported_content_tier_counts":{"excerpt_capsule":23,"full_text":97,"metadata_capsule":11},"source_type_counts":{"arxiv":73,"biorxiv":2,"blog":10,"industry":2,"journal":11,"methodology":7,"paper":2,"standard":24},"original_artifact_counts":{"complete":47,"metadata_only":13,"partial":4,"unknown":67},"text_extraction_counts":{"complete":8,"partial":54,"unavailable":13,"unknown":56},"action_bucket_counts":{"access_restricted":9,"author_manuscript_fetch":2,"complete_verified":8,"html_article_snapshot":11,"identity_or_version_ambiguous":3,"needs_boundary_verification":55,"ocr_assessment":31,"parser_only":6,"public_persistence_decision":4,"standard_spec_fetch":2},"public_redistribution_counts":{"allow":33,"block":65,"unknown":33},"content_inspected_full_text":55,"structure_only_full_text":42,"locally_persisted_complete":8,"knowledge_candidate_sources":30,"knowledge_trusted_sources":0,"knowledge_sources_without_demo_claims":101,"unresolved_sources":123}
---

# P3-PDF-04 — 十篇固定版编译论文正文物化

当前：十份原件已获取并完成有界正文/信用核验，均为原件完整、文字部分完整；严格两次离线重放、196项测试、普通demo/Wiki、四阶段169文件逐字节复现、稳定树验证及coverage全部通过。全库公开审计仍有64个旧block及2个旧包不一致，不能冒称全库public PASS。已提交版本CI与独立三维终审尚待完成；PR22仍Draft，未合入work/main。

以下合同于正文获取前发布；阶段历史保留，后续实绩见第8节起。

```json
{
  "execution_contract": {
    "plan_id": "nonrepo-materialization-main-convergence-260916",
    "phase": "P3-PDF-04",
    "status": "local_validation_passed_pending_final_exact_pair_evaluation_and_ci",
    "base_branch": "work/v0-meta-kb-initialization-demo-260910",
    "base_sha": "252fb09236433435a1a07d9e50d10f5f447b60e6",
    "target_branch": "work/v0-meta-kb-initialization-demo-260910",
    "adapter_family": "arxiv_latex_v2",
    "action_bucket": "open_fulltext_fetch",
    "source_uids": [
      "arxiv-1904.05530",
      "arxiv-2110.11309",
      "arxiv-2206.06520",
      "arxiv:2310.16218",
      "arxiv:2402.04624",
      "arxiv:2402.18264",
      "arxiv:2404.07738",
      "arxiv:2406.04268",
      "arxiv:2505.13400",
      "arxiv:2511.02824"
    ],
    "selected_versions": {
      "arxiv-1904.05530": "v4",
      "arxiv-2110.11309": "v2",
      "arxiv-2206.06520": "v1",
      "arxiv:2310.16218": "v4",
      "arxiv:2402.04624": "v2",
      "arxiv:2402.18264": "v2",
      "arxiv:2404.07738": "v2",
      "arxiv:2406.04268": "v1",
      "arxiv:2505.13400": "v1",
      "arxiv:2511.02824": "v2"
    },
    "fixed_authority_urls": {
      "arxiv-1904.05530": "https://arxiv.org/abs/1904.05530v4",
      "arxiv-2110.11309": "https://arxiv.org/abs/2110.11309v2",
      "arxiv-2206.06520": "https://arxiv.org/abs/2206.06520v1",
      "arxiv:2310.16218": "https://arxiv.org/abs/2310.16218v4",
      "arxiv:2402.04624": "https://arxiv.org/abs/2402.04624v2",
      "arxiv:2402.18264": "https://arxiv.org/abs/2402.18264v2",
      "arxiv:2404.07738": "https://arxiv.org/abs/2404.07738v2",
      "arxiv:2406.04268": "https://arxiv.org/abs/2406.04268v1",
      "arxiv:2505.13400": "https://arxiv.org/abs/2505.13400v1",
      "arxiv:2511.02824": "https://arxiv.org/abs/2511.02824v2"
    },
    "fixed_pdf_urls": {
      "arxiv-1904.05530": "https://arxiv.org/pdf/1904.05530v4",
      "arxiv-2110.11309": "https://arxiv.org/pdf/2110.11309v2",
      "arxiv-2206.06520": "https://arxiv.org/pdf/2206.06520v1",
      "arxiv:2310.16218": "https://arxiv.org/pdf/2310.16218v4",
      "arxiv:2402.04624": "https://arxiv.org/pdf/2402.04624v2",
      "arxiv:2402.18264": "https://arxiv.org/pdf/2402.18264v2",
      "arxiv:2404.07738": "https://arxiv.org/pdf/2404.07738v2",
      "arxiv:2406.04268": "https://arxiv.org/pdf/2406.04268v1",
      "arxiv:2505.13400": "https://arxiv.org/pdf/2505.13400v1",
      "arxiv:2511.02824": "https://arxiv.org/pdf/2511.02824v2"
    },
    "allowed_paths": [
      "docs/plans/260916-corpus-completion-main-convergence/p3-pdf-04-fixed-version.md",
      "docs/plans/260916-corpus-completion-main-convergence/branch-ledger.yaml",
      "raw_data/arxiv/Recurrent Event Network for Reasoning over Temporal Knowledge Graphs/metadata.yaml",
      "raw_data/arxiv/Fast Model Editing at Scale/metadata.yaml",
      "raw_data/arxiv/Memory-Based Model Editing at Scale/metadata.yaml",
      "raw_data/arxiv/Knowledge Editing for Large Language Models: A Survey/metadata.yaml",
      "raw_data/arxiv/MEMORYLLM: Towards Self-Updatable Large Language Models/metadata.yaml",
      "raw_data/arxiv/WIKIGENBENCH: Exploring Full-length Wikipedia Generation under Real-World Scenario/metadata.yaml",
      "raw_data/arxiv/ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models/metadata.yaml",
      "raw_data/arxiv/Position: Open-Endedness is Essential for Artificial Superhuman Intelligence/metadata.yaml",
      "raw_data/arxiv/Robin: A multi-agent system for automating scientific discovery/metadata.yaml",
      "raw_data/arxiv/Kosmos: An AI Scientist for Autonomous Discovery/metadata.yaml",
      "raw_data/licenses/p3-pdf-04-compiled-representations.md",
      "materialized_sources/corpus/arxiv-1904.05530--cddfa770/pdf-supplement/document.pdf",
      "materialized_sources/corpus/arxiv-1904.05530--cddfa770/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-1904.05530--cddfa770/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-1904.05530--cddfa770/pdf-supplement/NOTICE.md",
      "materialized_sources/corpus/arxiv-1904.05530--cddfa770/manifest.yaml",
      "materialized_sources/corpus/arxiv-1904.05530--cddfa770/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-2110.11309--d5da3395/pdf-supplement/document.pdf",
      "materialized_sources/corpus/arxiv-2110.11309--d5da3395/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-2110.11309--d5da3395/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-2110.11309--d5da3395/pdf-supplement/NOTICE.md",
      "materialized_sources/corpus/arxiv-2110.11309--d5da3395/manifest.yaml",
      "materialized_sources/corpus/arxiv-2110.11309--d5da3395/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-2206.06520--f7ce3f6e/pdf-supplement/document.pdf",
      "materialized_sources/corpus/arxiv-2206.06520--f7ce3f6e/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-2206.06520--f7ce3f6e/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-2206.06520--f7ce3f6e/pdf-supplement/NOTICE.md",
      "materialized_sources/corpus/arxiv-2206.06520--f7ce3f6e/manifest.yaml",
      "materialized_sources/corpus/arxiv-2206.06520--f7ce3f6e/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-2310.16218--21c4a191/pdf-supplement/document.pdf",
      "materialized_sources/corpus/arxiv-2310.16218--21c4a191/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-2310.16218--21c4a191/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-2310.16218--21c4a191/pdf-supplement/NOTICE.md",
      "materialized_sources/corpus/arxiv-2310.16218--21c4a191/manifest.yaml",
      "materialized_sources/corpus/arxiv-2310.16218--21c4a191/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-2402.04624--c3e9e366/pdf-supplement/document.pdf",
      "materialized_sources/corpus/arxiv-2402.04624--c3e9e366/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-2402.04624--c3e9e366/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-2402.04624--c3e9e366/pdf-supplement/NOTICE.md",
      "materialized_sources/corpus/arxiv-2402.04624--c3e9e366/manifest.yaml",
      "materialized_sources/corpus/arxiv-2402.04624--c3e9e366/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-2402.18264--ebc0e524/pdf-supplement/document.pdf",
      "materialized_sources/corpus/arxiv-2402.18264--ebc0e524/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-2402.18264--ebc0e524/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-2402.18264--ebc0e524/pdf-supplement/NOTICE.md",
      "materialized_sources/corpus/arxiv-2402.18264--ebc0e524/manifest.yaml",
      "materialized_sources/corpus/arxiv-2402.18264--ebc0e524/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-2404.07738--3e68f613/pdf-supplement/document.pdf",
      "materialized_sources/corpus/arxiv-2404.07738--3e68f613/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-2404.07738--3e68f613/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-2404.07738--3e68f613/pdf-supplement/NOTICE.md",
      "materialized_sources/corpus/arxiv-2404.07738--3e68f613/manifest.yaml",
      "materialized_sources/corpus/arxiv-2404.07738--3e68f613/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-2406.04268--ce5afac4/pdf-supplement/document.pdf",
      "materialized_sources/corpus/arxiv-2406.04268--ce5afac4/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-2406.04268--ce5afac4/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-2406.04268--ce5afac4/pdf-supplement/NOTICE.md",
      "materialized_sources/corpus/arxiv-2406.04268--ce5afac4/manifest.yaml",
      "materialized_sources/corpus/arxiv-2406.04268--ce5afac4/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/pdf-supplement/document.pdf",
      "materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/pdf-supplement/NOTICE.md",
      "materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/manifest.yaml",
      "materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-2511.02824--1c218a8e/pdf-supplement/document.pdf",
      "materialized_sources/corpus/arxiv-2511.02824--1c218a8e/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-2511.02824--1c218a8e/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-2511.02824--1c218a8e/pdf-supplement/NOTICE.md",
      "materialized_sources/corpus/arxiv-2511.02824--1c218a8e/manifest.yaml",
      "materialized_sources/corpus/arxiv-2511.02824--1c218a8e/source-metadata.yaml",
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
      "materialized_sources/corpus/arxiv-1904.05530--cddfa770/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-1904.05530--cddfa770/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-1904.05530--cddfa770/manifest.yaml",
      "materialized_sources/corpus/arxiv-1904.05530--cddfa770/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-2110.11309--d5da3395/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-2110.11309--d5da3395/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-2110.11309--d5da3395/manifest.yaml",
      "materialized_sources/corpus/arxiv-2110.11309--d5da3395/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-2206.06520--f7ce3f6e/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-2206.06520--f7ce3f6e/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-2206.06520--f7ce3f6e/manifest.yaml",
      "materialized_sources/corpus/arxiv-2206.06520--f7ce3f6e/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-2310.16218--21c4a191/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-2310.16218--21c4a191/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-2310.16218--21c4a191/manifest.yaml",
      "materialized_sources/corpus/arxiv-2310.16218--21c4a191/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-2402.04624--c3e9e366/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-2402.04624--c3e9e366/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-2402.04624--c3e9e366/manifest.yaml",
      "materialized_sources/corpus/arxiv-2402.04624--c3e9e366/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-2402.18264--ebc0e524/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-2402.18264--ebc0e524/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-2402.18264--ebc0e524/manifest.yaml",
      "materialized_sources/corpus/arxiv-2402.18264--ebc0e524/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-2404.07738--3e68f613/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-2404.07738--3e68f613/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-2404.07738--3e68f613/manifest.yaml",
      "materialized_sources/corpus/arxiv-2404.07738--3e68f613/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-2406.04268--ce5afac4/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-2406.04268--ce5afac4/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-2406.04268--ce5afac4/manifest.yaml",
      "materialized_sources/corpus/arxiv-2406.04268--ce5afac4/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/manifest.yaml",
      "materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/source-metadata.yaml",
      "materialized_sources/corpus/arxiv-2511.02824--1c218a8e/pdf-supplement/document.txt",
      "materialized_sources/corpus/arxiv-2511.02824--1c218a8e/pdf-supplement/selectors.jsonl",
      "materialized_sources/corpus/arxiv-2511.02824--1c218a8e/manifest.yaml",
      "materialized_sources/corpus/arxiv-2511.02824--1c218a8e/source-metadata.yaml",
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
      "integration": "PR21 merged at 252fb09236433435a1a07d9e50d10f5f447b60e6; PR1 remains draft against main 99ce4670be91637209d67792de0962404fa96488; no overlapping implementation",
      "startup": "publish this ten-UID contract and branch-ledger entry in a new implementation PR before any PDF acquisition",
      "identity": "reuse the finite official fixed-version/work-license evidence below; no latest fallback or guessed version",
      "public_persistence": "review actual fixed PDF identity, body boundary and visible independent credits before new representation allowance and public commit"
    },
    "explicitly_out_of_scope": [
      "every other UID including PDF05; entire arXiv source archives, historical versions, recursively fetched references, external data/code/weights",
      "legacy source/**, normalized/**, root selectors.jsonl, NOTICE.md, README.md, files.jsonl and any legacy reading view",
      "overwriting root revision/source_version-key absence/retrievals/rights/materialization/selectors or upgrading legacy publication_gate",
      "latest or other-version/PDF-publisher fallback, fabricated status/bytes/pages/retrieved times or retroactive archive retrieval",
      "production code, tests, dependencies, workflows, schemas, new adapters, new framework or globalgeneratedoutputreader",
      "new demo selected sources, new claims/collector assessments, trusted promotion, default OCR or lossless linear extraction gate",
      "other UID rights/coverage decisions, unexplained generated rewrites, Git history edits/branch deletion/force push",
      "PR1 Ready/main merge, Issue3/Issue4 closure or P4/P5 completion claim"
    ]
  }
}
```

# P3-PDF-04 — 十篇固定版本官方 PDF 正文补充

当前为启动合同：PR21已在独立三维PASS（COMMENT 5232915435）和当前CI 35196904467成功后正常合入work，merge/base为252fb09236433435a1a07d9e50d10f5f447b60e6。当前分支codex/p3-pdf-04-260917，父PR1仍Draft/main基线99ce4670be91637209d67792de0962404fa96488，尚未进入main。本启动提交只改报告及branch ledger，不获取或修改正文。必须发布本合同PR后才取明确的十份PDF。

主线已全文读取Issue3/4、README、02/03/04、05/06、plan.yaml及branch ledger，并复核远端只有父PR1开放、work已同步PR21。planner两轮只读预核给出十UID固定版及合法作品依据，主线已全文阅读本草案和existing PDF helper，选择复用现PDF supplement，不扩写TeX parser，不重新取得archive。六known复用既有真实证据；四null经正式fixed abs及作品许可链定版。正文获取、提取、公开持久化及knowledge分开验收，旧source gate不自动等于新PDF gate。

## 2. 本轮已读事实源（Source of Truth）

主 planner 已完整读取：

- `/tmp/p3-pdf04-local-version-preflight.md`；
- `/tmp/p3-pdf04-fixed-version-preflight.md`；
- `docs/plans/260916-corpus-completion-main-convergence/p3-pdf-03-fixed-version.md`（345 行）；
- `05-validation-and-definition-of-done.md`（215 行）与实际 `06-codex-execution-contract.md`（226 行）。

本地仅做有界 metadata／manifest／coverage／既有 Rights 证据定位，以及现 PDF helper 与 demo／repro 路由阅读；没有重读论文正文或新许可考古。下文的 R 表示 `raw_data/audits/materialization_rights_review.yaml`，K 表示 `raw_data/audits/non_repo_materialization_coverage_2026-09-16.yaml`；以精确 UID＋evidence.kind 定位，不把旧预核行号当永久定位。

十 manifest 均为 `source_type=arxiv`／`adapter=arxiv_latex_v2`，均没有既存 `pdf_supplement`；根 `source_version` 键均缺省（读取结果 null），不是应补写的旧 GET 版本。当前 canonical `versioning.source_version` 与 K `selected_version` 十条均 null。已有源固定证据／既有 fixed-preflight 正式 abs 证据与这些 null 不矛盾：实现时 durable 化新选择，不伪造历史 retrieval。

## 3. 十个完整 UID、固定 URL 与证据来源

下列十个 PDF URL 是下一批唯一计划正文 GET；本轮未取得其 bytes、HTTP 响应、页数或内容。六 known 不需要为确认同一版号重新 GET source bundle／abs。四新版本来自上一份 fixed preflight 的真实正常官方 abs＋各自作品许可链接读取，不是文件名猜测。

| 完整 UID | Selected version | 固定权威 URL | 唯一计划正文 GET URL |
| --- | --- | --- | --- |
| `arxiv-1904.05530` | `v4` | [fixed abs](https://arxiv.org/abs/1904.05530v4) | [唯一计划 PDF](https://arxiv.org/pdf/1904.05530v4) |
| `arxiv-2110.11309` | `v2` | [fixed abs](https://arxiv.org/abs/2110.11309v2) | [唯一计划 PDF](https://arxiv.org/pdf/2110.11309v2) |
| `arxiv-2206.06520` | `v1` | [fixed abs](https://arxiv.org/abs/2206.06520v1) | [唯一计划 PDF](https://arxiv.org/pdf/2206.06520v1) |
| `arxiv:2310.16218` | `v4` | [fixed abs](https://arxiv.org/abs/2310.16218v4) | [唯一计划 PDF](https://arxiv.org/pdf/2310.16218v4) |
| `arxiv:2402.04624` | `v2` | [fixed abs](https://arxiv.org/abs/2402.04624v2) | [唯一计划 PDF](https://arxiv.org/pdf/2402.04624v2) |
| `arxiv:2402.18264` | `v2` | [fixed abs](https://arxiv.org/abs/2402.18264v2) | [唯一计划 PDF](https://arxiv.org/pdf/2402.18264v2) |
| `arxiv:2404.07738` | `v2` | [fixed abs](https://arxiv.org/abs/2404.07738v2) | [唯一计划 PDF](https://arxiv.org/pdf/2404.07738v2) |
| `arxiv:2406.04268` | `v1` | [fixed abs](https://arxiv.org/abs/2406.04268v1) | [唯一计划 PDF](https://arxiv.org/pdf/2406.04268v1) |
| `arxiv:2505.13400` | `v1` | [fixed abs](https://arxiv.org/abs/2505.13400v1) | [唯一计划 PDF](https://arxiv.org/pdf/2505.13400v1) |
| `arxiv:2511.02824` | `v2` | [fixed abs](https://arxiv.org/abs/2511.02824v2) | [唯一计划 PDF](https://arxiv.org/pdf/2511.02824v2) |

| UID | 版本与作品许可（work license）证据来源 | 本批许可解释 |
| --- | --- | --- |
| `arxiv-1904.05530` | R[uid].evidence: `fixed_arxiv_source_and_retained_member_correspondence`（已观察固定 v4）；`alternate_acl_publication_correspondence`：[EMNLP2020 作品](https://aclanthology.org/2020.emnlp-main.541/)、[已观察正式 PDF](https://aclanthology.org/2020.emnlp-main.541.pdf)、[ACL copyright policy](https://aclanthology.org/faq/copyright/)，2026-09-16；本地预核 O-A | arXiv nonexclusive 不是公众 grant；正式 ACL BY4 已对应 v4 作者主文、表图文字、附录 A–G。历史正式表示 15 页不冒充本次 page_count；三处未出版旧稿／组件仍属旧 source 未决 |
| `arxiv-2110.11309` | fixed preflight：正常读取 [v2 abs](https://arxiv.org/abs/2110.11309v2)，该版时间 2022-06-13 23:26:16 UTC，作品 `view license` 实际指向 [CC BY4](https://creativecommons.org/licenses/by/4.0/)，本轮观察日期 2026-09-17；R[uid].`official_article_license_record` 另保留旧 bare abs 证据 | 选本次官方明示当前 v2；新 PDF 作品许可链明确，不声称旧 unversioned payload 已追溯定为 v2 |
| `arxiv-2206.06520` | fixed preflight：[v1 abs](https://arxiv.org/abs/2206.06520v1)，2022-06-13 23:40:34 UTC、唯一列出 v1、该版作品链接 → [CC BY4](https://creativecommons.org/licenses/by/4.0/)，观察日期 2026-09-17；R[uid].`official_article_license_record` | 官方明确 v1，不从 ICML 样式推版；旧模板／算法组件状态不是新 PDF 自动 blocker |
| `arxiv:2310.16218` | R[uid].`fixed_article_version_binding`：[v4 abs](https://arxiv.org/abs/2310.16218v4)＋已观察固定 source 响应／五 retained 成员，官方 2024-09-19、六作者、BY4，checked 2026-09-16；O-C／local preflight | v4 有真实 binding，不取 `arxiv_v2.tex` 文件名中的 v2；旧 modified acmart 身份与组件包未决保留 |
| `arxiv:2402.04624` | R[uid].`fixed_v2_response_and_retained_text_correspondence`：[v2 abs](https://arxiv.org/abs/2402.04624v2)、2024-05-26 BY4、已观察固定 source 17 成员，checked 2026-09-16；O-C／local preflight | 同一已许可 v2 作者作品；两个纯书目 bib 无额外 abstract，不追加不存在的第三方摘要要求 |
| `arxiv:2402.18264` | fixed preflight：[v2 abs](https://arxiv.org/abs/2402.18264v2)，2024-12-17 09:53:41 UTC、COLING2025 Camera Ready、该固定页作品链接 → [CC BY4](https://creativecommons.org/licenses/by/4.0/)，观察日期 2026-09-17 | 选官方明示当前 v2，不以 COLING 文件名猜版或默认旧 source 等于 v2；新 PDF 须实际包含附录 |
| `arxiv:2404.07738` | R[uid].`fixed_arxiv_source_and_retained_member_correspondence`：已观察 `https://arxiv.org/src/2404.07738v2`；`alternate_acl_publication_correspondence`：[NAACL2025 作品](https://aclanthology.org/2025.naacl-long.342/)及[已观察正式 PDF](https://aclanthology.org/2025.naacl-long.342.pdf)，30页、四作者、正文／A/B／16表对应，checked 2026-09-16；O-D | arXiv nonexclusive 不是 grant；ACL BY4 已覆盖对应作者出版表达。表中独立输入与可见 credit 按实际新 PDF 有界核查，不覆盖 source 的额外 bib 摘要 |
| `arxiv:2406.04268` | fixed preflight：[v1 abs](https://arxiv.org/abs/2406.04268v1)，2024-06-06 17:15:02 UTC、唯一列出 v1、该版作品链接 → [CC BY4](https://creativecommons.org/licenses/by/4.0/)，观察日期 2026-09-17；R[uid].`official_article_license_record` | P2 local revision 不是 arXiv vN；旧 DeepMind／ICML 源组件状态保留，实际图中 Noun Project 图标信用独立保留 |
| `arxiv:2505.13400` | R[uid].`official_article_license_record` bare abs BY4＋`fixed_version_archive_binding`：[v1 abs](https://arxiv.org/abs/2505.13400v1)，已观察固定 source 与全部 retained 成员对应，checked 2026-09-16；O-F | fixed archive exact GET URL 没写入现有记录，不补造；引用文献的 88 个源 bib abstract 不是新 PDF 额外必须取得／清算的正文 |
| `arxiv:2511.02824` | R[uid].`official_article_license_record` bare abs BY4＋`fixed_version_archive_binding`：[v2 abs](https://arxiv.org/abs/2511.02824v2)，已观察固定 source 与 retained 成员对应，checked 2026-09-16；O-F | 不补造 archive exact URL；80 个源 bib abstract 未决不移入新 grant。实际 Fig2-bc 可见 reproduced-with-permission 声明须保留对应独立信用，不能写成底层图板改许可 |

四新 abs 的网页工具未暴露原始 HTTP status／headers／bytes，且返回了各自 crawl 提示；本轮不能把工具读取时刻写成 PDF retrieval 或 raw HTTP200。详情保留在 fixed preflight，实施应将真实证据及这些限制写入批准报告／R 的本 UID 新 evidence，不静默改旧事实。

### 精确 capsule／canonical 路径

| UID | Canonical metadata | 既存 capsule 根 |
| --- | --- | --- |
| `arxiv-1904.05530` | `raw_data/arxiv/Recurrent Event Network for Reasoning over Temporal Knowledge Graphs/metadata.yaml` | `materialized_sources/corpus/arxiv-1904.05530--cddfa770` |
| `arxiv-2110.11309` | `raw_data/arxiv/Fast Model Editing at Scale/metadata.yaml` | `materialized_sources/corpus/arxiv-2110.11309--d5da3395` |
| `arxiv-2206.06520` | `raw_data/arxiv/Memory-Based Model Editing at Scale/metadata.yaml` | `materialized_sources/corpus/arxiv-2206.06520--f7ce3f6e` |
| `arxiv:2310.16218` | `raw_data/arxiv/Knowledge Editing for Large Language Models: A Survey/metadata.yaml` | `materialized_sources/corpus/arxiv-2310.16218--21c4a191` |
| `arxiv:2402.04624` | `raw_data/arxiv/MEMORYLLM: Towards Self-Updatable Large Language Models/metadata.yaml` | `materialized_sources/corpus/arxiv-2402.04624--c3e9e366` |
| `arxiv:2402.18264` | `raw_data/arxiv/WIKIGENBENCH: Exploring Full-length Wikipedia Generation under Real-World Scenario/metadata.yaml` | `materialized_sources/corpus/arxiv-2402.18264--ebc0e524` |
| `arxiv:2404.07738` | `raw_data/arxiv/ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models/metadata.yaml` | `materialized_sources/corpus/arxiv-2404.07738--3e68f613` |
| `arxiv:2406.04268` | `raw_data/arxiv/Position: Open-Endedness is Essential for Artificial Superhuman Intelligence/metadata.yaml` | `materialized_sources/corpus/arxiv-2406.04268--ce5afac4` |
| `arxiv:2505.13400` | `raw_data/arxiv/Robin: A multi-agent system for automating scientific discovery/metadata.yaml` | `materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6` |
| `arxiv:2511.02824` | `raw_data/arxiv/Kosmos: An AI Scientist for Autonomous Discovery/metadata.yaml` | `materialized_sources/corpus/arxiv-2511.02824--1c218a8e` |

## 4. 逐 UID 有界正文、已知损失和独立信用核查

下表 known loss 是已有 source／旧 TXT 的事实，不是本轮未 GET 新 PDF 的提取结论。对每篇都核实际新原件首／中／末至少三页、实际页数、全文结束和列定重点；不因某 UID 文件大而跳过，也不要求默认全图 OCR／无损线性化。

| UID | 新 fixed PDF 的目标边界（target boundary） | 已知旧表示损失／本次实际检查点 | 作者及独立信用（independent credit）核查 |
| --- | --- | --- | --- |
| `arxiv-1904.05530` | RE-Net 主文、书目、表1–4／图caption1–8、正式 A–G 附录至 Know-Evolve implementation issues；保留 collection 旧题名与正式副题差异 | O-A:49–59：方法名宏空、事件求和／log／λ 丢失；15 个实际源图引用缺失，legend 重引不重复计件。新 PDF 核编译图面是否在以及 native 概率式，不把15源资产当15编号图 | 四作者 Woojeong Jin／Meng Qu／Xisen Jin／Xiang Ren；保留正式 EMNLP作品与ACL许可归属。新 PDF 核图注／样例／独立声明；三处未出版旧稿和STY／BST归属不移植为新PDF作品credit |
| `arxiv-2110.11309` | MEND 主文、正式补充正文及 Caching 末表；18活动输入对应正式编译作品，不包含旧 revision-history | O-A:73–83：MEND全名／末表标签、∇／求和／δ／外积丢失；4实引图缺。核新摘要名称、梯度式、Caching结束和4源图实际编译映射，记录 native 仍有何数学／表损失 | 五作者按 fixed preflight 完整顺序署名；核贡献脚注及主文／图／补充中的可见credit。旧 main.bib 的11完整摘要不默认在新PDF，也不要求预先清其许可 |
| `arxiv-2206.06520` | SERAC 主文、正式补充及 conversation-sentiment 完整生成prompt表至末；unused multi_model 非必需 | O-A:97–107：β两分支、≥／argmax／模型符号损失；3实引图缺，不是4 omitted都必需。核新PDF分支语义／数学、prompt文字／表尾及图面；TXT不能因字面可读冒称可执行prompt无损 | 五作者按 fixed preflight 顺序署名（Manning在Finn前）；核研究样本／示例原有出处，Sun Public License研究样本不是论文grant。模板／algorithm源组件独立范围留旧包 |
| `arxiv:2310.16218` | 综述主文、taxonomy／category、评价／结论／完整funding、书目；appendix后仅注释模板，不发明独立SI | O-C:59–65：min／∀／集合差／notin删除改变约束；3活动图缺。核新PDF优化／外域约束、Loc、taxonomy图及真实结论末尾，保留图形／公式线性提取限制 | 六作者 Song Wang／Yaochen Zhu／Haochen Liu／Zaiyi Zheng／Chen Chen／Jundong Li；核资助／作者声明／图注原有引用。普通书目不再许可被survey完整作品，旧acmart源码修改条件不自动门控该编译PDF |
| `arxiv:2402.04624` | MEMORYLLM主文、声明、8活动正文／appendix边、伪代码／实验／FT／FT-L／IKE／ROME末基线及实际图件 | O-C:83–89：MemoryLLM宏、静态φ／动态θ、分数／lim和FOR／IF／ELSE损失；方法／longbench／附录图缺。核新数学参数区分、算法作用域及附录结束，不能仅统计非空页 | Canonical现有12作者完整核实际PDF顺序／贡献；核数据／模型／基线引用，不获取weights／code。两个bib无额外摘要；ICML／BST／fancyhdr／algorithm源码包装留旧gate |
| `arxiv:2402.18264` | WIKIGENBENCH主文＋整个正式附录：生成／评估prompts、案例与结果表；main-only不算完成 | O-D:9–11：已存99.appendix未消费、2实引图缺、旧plain混入iffalse摘要。新PDF直接核完整附录及首中末真实结束；不借本批修旧consumer／删除源摘要 | fixed preflight十一作者全署名；核实际新PDF样例／表中独立输入的可见来源／量／用途，尤其旧source记录DOI10.1121/1.2016299摘要与数值是否实际在该版本编译表示；不存在则不把源scope搬进PDF，存在则如实保留来源与有界表示决定，不声称被引独立全文获BY4 |
| `arxiv:2404.07738` | ResearchAgent主文、Sections/8_appendix A/B、16表、完整prompts／criteria／examples和末实验示例；不重复抓已有文字 | O-D:13–15：27边已展开，10实引图缺，旧plain前540行导言污染；旧text仍unknown。新PDF核对应作者表达与图件、完整附录／末表，实际判定native损失，不先承诺text partial或complete | 四作者 Jinheon Baek／Sujay Kumar Jauhar／Silviu Cucerzan／Sung Ju Hwang。核三input样例：两ACL摘要已存在独立BY4路径（2023.matching-1.7／2023.findings-emnlp.1033），分别保留作者／作品归属；FlyWire输入保留可见出处、实际引用量／科学示例用途及具体声明，不借后出版改写版本grant。不获取三个原作或清额外custom.bib Vamathevan摘要 |
| `arxiv:2406.04268` | Open-Endedness主文、三组正式文字附录、3实引图；不重修已成功.txt root，不新添include／别的open-endedness作品 | O-D:33–35／K该UID：P2 root识别已修，0真实include；Figure_1／OE_AIS_Final／rate_distortion_final图缺，旧plain有损。核新图／形式定义／数学和附录末尾，保留旧P2原件／派生历史 | fixed preflight八作者；canonical旧Michael D. Dennis与fixed abs可见Michael Dennis差异以实际PDF署名为准记录、不猜身份。保留各实际Noun Project图标作者、图标出处和CC BY3.0链接／变化说明，只覆盖相应图标；不能把它们归论文作者BY4。源DeepMind／颜色／ICML模板状态留旧包 |
| `arxiv:2505.13400` | Robin单report root主文、Supplementary Materials、全部长实验prompts及末十CKD候选caption；不取RNA实验数据／repo | O-F:11–19：μ单位变L、assay_name花括号删；缺fig3_mmh2-compressed／humanRNAseq_supp_fig-compressed等实引图且omitted未完整列。核新原件剂量／单位／prompt字面、正文与补充结束和实际科学图；不得只用omitted清单证明完整 | Canonical现有十作者完整核PDF署名／贡献／机构；保留研究输入与素材的可见credit，不把源88摘要／15copyright混入PDFgrant。仅核实际编译书目／样例是否出现独立表达及反向声明，不抓实验原件 |
| `arxiv:2511.02824` | Kosmos主文、Methods与正式SI1–4、8实引科学图及末refuted评价；logo不算必需科学图 | O-F:61–69：三组均值±误差被删；source末refuted评价真实保留。核新PDF±／不确定性／批评而不润色为支持，核SI1–4／末尾和8科学图。旧80摘要／31copyright不自动变目标正文 | Canonical作者列表当前为空，不能填et al.冒称完整归属；以实际fixed PDF完整作者／贡献脚注建立新attribution，不需为此再抓source。核Fig2-bc的reproduced-with-permission图板及实际可见原作者／出版出处／限定声明，保留独立credit，不宣布底层图板一般BY4改许可；若新表示有具体反向限制，仅该UID公开持久化unresolved |

以上独立信用核查是对实际新作品表示的正常包装，不以所有引用、样例或可见商标为默认额外许可门槛。只有实际作品身份矛盾、真实正文缺页、具体反向声明／明确范围排除或超出已观察引用范围，才收缩该UID新表示scope／记录其未决；其余独立UID可继续。不自动编辑原PDF，不对有问题页裁剪后伪称完整，也不把作品BY4写成底层软件／数据／图标／商标通用再许可。

### 启动前 before 状态（不能预写 after）

| UID | K旧 original／text | 旧root selectors | 旧public gate | 当前demo知识状态 |
| --- | --- | ---: | --- | --- |
| `arxiv-1904.05530` | unknown／unknown | 39 | block | null；未selected |
| `arxiv-2110.11309` | unknown／unknown | 140 | block | candidate；selected |
| `arxiv-2206.06520` | unknown／unknown | 89 | block | null；未selected |
| `arxiv:2310.16218` | unknown／unknown | 45 | block | candidate；selected |
| `arxiv:2402.04624` | unknown／unknown | 60 | block | null；未selected |
| `arxiv:2402.18264` | unknown／unknown | 39 | block | null；未selected |
| `arxiv:2404.07738` | partial／unknown | 79 | block | null；未selected |
| `arxiv:2406.04268` | partial／partial | 60 | block | candidate；selected |
| `arxiv:2505.13400` | unknown／unknown | 39 | block | candidate；selected |
| `arxiv:2511.02824` | unknown／unknown | 59 | block | candidate；selected |

上述是当前本地K记账值；已有O报告中更具体的旧source partial／损失观察用于驱动检查，不悄悄改写启动before。合入PR21后执行者须重读这十项准确before，其他121条coverage对象／原始块和131条knowledge状态保留。新原件可complete而native text仍partial；partial的实际原因、页面与下一action必须独立记录，不预判、不用非空页数／CI／selector数替代。

## 5. 只用现helper的最小实施流程（Minimal Execution）

1. **等待和合同启动。** PR21正常合入后，执行者按06完整必读順序读取最新Issue3／4、README、02／03／04、plan／ledger、work head和PR1状态，确认无重叠活跃writer，再从实际最新work创建短期codex分支。将下文 `252fb09236433435a1a07d9e50d10f5f447b60e6` 替为真实exact base，核实十UID与路径，先发布新启动PR和台账；启动提交仅合同／ledger，不下载正文，不假填新allow或after。
2. **一次有限新原件获取。** 调用者仅正常请求表中十个fixed PDF URL，在非公开临时审读区保存原响应；逐UID记录真实请求／resolved URL、可观察HTTP status／content-type／bytes、时间、失败与实际选用理由。不回退bare/latest、出版另版、source archive或全历史；挑战／访问限制不绕过。可复用已有 `session()`／`fetch_bytes()` 获取能力；`fetch_bytes`本身只返回payload／resolved URL／headers，没有status返回值，报告不得猜HTTP200或为补status重复GET，status须由同一实际调用层观察。
3. **逐UID有限作品审读。** 原件身份／实际vN／作者对本地已核证据，记录真实页数，逐篇首中末至少三页及第4节关键章／附录／图／表／公式／prompt／credit。按实际原件决定main／SI边界和native损失；arXiv本适配器为单compiled PDF，正式SI若内嵌则在同件中核，不造独立SI URL。未取得／缺正文／新公开scope未决保持该UIDunresolved，不阻塞其余独立合法原件。
4. **独立新表示准入／正常信用包装。** 保留旧rootrights及R旧gate。在真实身份／正文／可见credit核定后，为本UID建立新 `rights.pdf_supplement`：`license_spdx`／URL／verified date、独立gate allow＋reason＋approved_scope、六字段 `redistribution_package`（实际新PDFsource_revision、固定**PDF URL**source_version_url、notice_path、完整attribution、真实modifications、精确scope）。`scope==approved_scope`；原件不编辑，TXT／页定位器为派生层。默认复制已有完整 `raw_data/licenses/cc-by-4.0.md`到新NOTICE；确需累积既有独立credit时只开放合同内一个精确notice资产，不扩大版权考古。
5. **零代码PDF派生。** 新固定选择及出处durable到批准报告／本UID R evidence；canonical与capsule snapshot的 `versioning.source_version`必须一致设为表中vN，`pdf_url`明确fixed URL，verification.notes说明这是新表示选择，四新旧payload不曾追溯核定。旧source_archive_url、旧root缺省source_version／retrievals／revision／materialization／selectors／rights不伪造或替换。以现 `build_pdf_supplement(root, vN, actual_retrieval, new_rights, body_quality_verified=实际结果, limitations=实际限制, primary_excerpt=仅真实需要时)`生成TXT／selectors；它不获取PDF、不写原PDF／NOTICE／manifest／metadata／旧consumer。调用者只追加manifest.pdf_supplement并用现local_file_inventory更新库存／local_bytes，四方新grant（canonical／snapshot／manifest／R）保持逐值一致。
6. **严格离线重放与消费。** 直接用现 `replay_pdf_supplement(record, manifest)`各两次；在调用者用现测试mock禁止fetch／prepare，确认新派生幂等及全部legacy文件保留。不调用常规materialize_one／全族 `--only-source-type arxiv` 或 `make materialize-all`，它们不是本批十UID首次补充的有限入口，可能重新取archive。不新增CLI、adapter、生产code／tests／workflow或新的全局读取框架。
7. **聚合与已有demo。** 调用现 `discover_records()`读取全部既有manifest（仅十条新manifest变化），然后现 `rebuild_registry()`、`write_indexes_and_audit()`；沿用当前已有聚合generated_at，不用新聚合时间冒充retrieval。新source-metadata以该UIDcanonical精确snapshot同步。只以 `make demo`重建既有demo／Wiki和必要build identity，五selected UID可通过现admitted_pdf_supplement选择独立newallow＋完整性＋body_quality_verified后的PDF TXT／selectors。逐个核父论文Page1摘要的真实连续范围，只有默认范围不合实际时用已有primary_excerpt；不让嵌入第三方摘要替代父论文。其余五不新增selected，现claims／collector-assessment／knowledge身份保留，只有必要source／正文evidence／引用绑定与全局identity传播。
8. **稳定树最小必要验证。** 按05实际运行当前树 `make test`、`make demo`、`make validate`、`make reproducibility`及materialization completeness／coverage。本repo实际repro target为reproducibility；repro会清理／重建生成目录，禁止与validator、coverage facts或semantic diff reader并行读，待完成后在稳定树串行复验。十新PDF局部rights／completeness包逐项验证，所有新selector首中末preview及语义逐UID核。现有root／其它UID门控未决另报，不把十新包局部pass冒称全库public PASS。
9. **逐UID记账与独立门控。** K target显式选择representation=pdf_supplement／真实vN／新boundary，observed从当前facts采集；original、text、persistence、selectors、publicredistribution、knowledge各轴before→after独立。保留legacyaxis／retrieval／未决及其他121 raw块，固定215=131非repo+84repo；不预填complete计数。最终按06汇报模板给实际文件、命令、失败／纠偏、remaining与non-results；commit后独立evaluator锁exact HEAD／BASE检查需求满足／agentic过程／核心质量，PASS且该pair当前适用CI门控满足才正常合入work。任何head/base变化重新核验；FAIL回planner→executor→独立复审。本报告不是PASS，不是PR1／main关闭条件达成。

### 现有入口／限制的代码定位

- `scripts/materialize_all_sources.py:3264` fixed vN URL；`:3273` canonical＋snapshot version同值；`:3342`真实retrieval／revision-bound新包／native plain；`:3417`build helper及caller职责；`:3483`独立offline replay；`:399`inventory；`:4023`registry；`:4081`index／既有completeness audit。
- `scripts/validate_publication_rights.py:31`四方新PDF grant、准确scope／notice／末注；旧root gate不被此函数自动升级。
- `scripts/validate_materialization_completeness.py:507`新PDF验证；`scripts/audit_non_repo_coverage.py:27`只对显式validated PDF target选独立version，`:71`collect_facts，默认audit只读。
- `experiments/v0_meta_kb_initialization_demo_260910/pipeline/build_demo.py:192`独立admission、`:218`／`:225`配对selectors／TXT消费、`:336`父论文Page1摘录；`scripts/verify_demo_reproducibility.py:42`起四阶段串行重放。

## 6. 启动合同：完整路径上限

下列路径都相对当前repo根 `/Users/lw/Desktop/GitHub/llm_wiki/solid-octo-couscous`。canonical／capsule路径精确枚举；experiment目录的受控 `**`只允许**已有生成器**输出及必要identity传播，不授权手写schema／entities／claims。为最小范围，十capsule旧README也不开放写：现build helper并不生成supplement README，直接文件链接与批准报告已足够消费，不为导航新增接口。

allowed_paths共95项、generated_paths共60项；其中新PDF／NOTICE是原件／信用包装，不列为generator-produced。可选 `raw_data/licenses/p3-pdf-04-compiled-representations.md`仅在实际新表示信用确需累积notice时建立；默认共享BY4法条只读，不改既有共享资产。十UID之外的任何handwritten／original改变、以及需改production／test／workflow的技术缺口均先停并修订合同，不能用生成通配吞掉。

合同完整JSON已置于文首，不重复列出。

## 7. 验收报告必含内容与明确非结果（Explicit Non-results）

执行者须使用06完整报告模板；至少逐UID提供：
`artifact before→after | extraction before→after | persistence | redistribution | unresolved`，
实际GET尝试／时间／响应／URL、first／middle／last页面与实际总页数、主文／SI／图件／信用边界、selector抽查、native loss与action bucket；手写输入／原件／派生／生成物分列。独立evaluator必须不是作者，三维verdict及exact pair／CI记录保存在该PR，不伪造人类APPROVE，不能以写完报告或CI绿色替代质量PASS。


启动时明确未完成（历史记录）：十份新PDF当时均未GET、页数/原件完整性/native文字质量/实际信用/新公开包均未核；没有新allow、after、coverage晋升或trusted。没有生产code/tests/deps/workflow改动、生成重建、CI或独立终审PASS。未合入work/main，未删除分支/历史/原件，未关闭Issue3/4。后续实际获取、内容决定与验证分别见第8节起；CI与独立exact pair审核均在最终commit后执行。

## 8. 启动后的实际获取（Acquisition after startup）

上述未GET声明为启动历史。启动提交0bbd3c9438f111723f77e29e1745a23ced6ac900已push，[Draft PR22](https://github.com/thsno02/solid-octo-couscous/pull/22)于2026-09-17T08:16:57Z创建。之后主线在08:17:17Z开始本合同十个固定PDF请求，无source/archive/新版本/被引作品GET；十个响应均HTTP200、application/pdf、0 redirects、ssl_verify_result=0，最终URL与合同固定PDF URL相同，服务器HTTP Date均为2026-09-17T08:17:19Z。正常curl、未更换UA/关闭TLS/绕过挑战。

| 固定ID/版本 | 实际bytes | pypdf实际页数 | 下载完成时间UTC（本地响应记录mtime） |
| --- | ---: | ---: | --- |
| 1904.05530v4 | 1066926 | 15 | 2026-09-17T08:17:30.950396Z |
| 2110.11309v2 | 1140371 | 21 | 2026-09-17T08:17:30.708557Z |
| 2206.06520v1 | 1543761 | 15 | 2026-09-17T08:17:32.346648Z |
| 2310.16218v4 | 1768864 | 35 | 2026-09-17T08:17:33.103454Z |
| 2402.04624v2 | 1414691 | 14 | 2026-09-17T08:17:31.526467Z |
| 2402.18264v2 | 880885 | 20 | 2026-09-17T08:17:30.721478Z |
| 2404.07738v2 | 820779 | 30 | 2026-09-17T08:17:28.267446Z |
| 2406.04268v1 | 939555 | 20 | 2026-09-17T08:17:28.751149Z |
| 2505.13400v1 | 33781795 | 30 | 2026-09-17T08:18:13.172050Z |
| 2511.02824v2 | 8162544 | 42 | 2026-09-17T08:17:46.743505Z |

完成时间是同一次curl响应记录的本地时间，不冒充服务器Date或作品发布日期。全部原件当前只在临时审读区，页数/PDF magic/200不能替代正文与信用核验；三组内容executor按逐UID合同看首中末及关键附录/数学/图件，主线另外检查普通consumer入口。采用PDF技能只读渲染与原生文字比较，不编辑原件、不默认OCR；核准前不将新全文提交至公开repo。最终独立evaluator另行调用，内容executor不担任自己变更的最终审核者。

## 9. 正文核验与准入决定（Content inspection and admission）

第8节末段为获取后的阶段记录。此后三个内容执行者完成十件共242页的原生文字结构检查，以及首、中、末、全部编号科学图及关键公式/附录/信用页面的渲染对照；不是声称242页逐字人工校读。主线完整读取三份执行报告后逐组准入。十件均确认所选固定版 compiled PDF 完整、父正文可读，但 native TXT 有实证损失，因此统一采用 original=complete、text=partial、body_quality_verified=true；后者不代表严格完整消费或 trusted。内容执行者不担任本批最终 evaluator。

| 固定作品 | 实际完整边界 | 必须保留的原生文字损失 |
| --- | --- | --- |
| RE-Net v4 | 15页；主文、书目、A–G、4表8图，末段是Know-Evolve同分排名讨论 | P1时间下标编码；P15国旗实体变空槽；图拓扑、曲线、表组及二维数学 |
| MEND v2 | 21页；主文、伦理/复现声明、A–G；Table11之后的Caching末段完整 | 内部架构图未进入plain；P19 Table8粗体edit-label边界丢失；算法/公式/曲线布局 |
| SERAC v1 | 15页；主文、A–D、8表3图；Table8完整prompt后D.2至90-5-5 split | 图中scope/路由/曲线对应及二维数学；prompt大小写/空格排版不保证无损 |
| Knowledge Editing Survey v4 | 35页；4图3表、完整conclusion/funding、书目到[179]，没有独立SI | P7/P8大并集被替为其他符号；P13/P18括号控制字符；P2存在未在可见图面呈现的text object；图树/箭头 |
| MEMORYLLM v2 | 14页；9编号图、Impact/书目、A–C、完整25行Algorithm1，末尾ROME | 分式/极限/上下标、P7括号控制字符、图面和算法缩进 |
| WIKIGENBENCH v2 | 20页；A–G、2图10表、完整prompt/rubric，末表checkpoint至Vicuna epoch10 | P8图轴/legend字体代码；P13 Table6手形/勾叉语义丢失；二维数学 |
| ResearchAgent v2 | 30页；9编号图16表、A/B；完整prompt/criteria及Table16三个输入 | P5乘积/并集符号替换，图面及表格布局；输入摘要本身未缺失 |
| Open-Endedness v1 | 20页；3图、Impact/Ack、书目、A–C到末句 | 图标/勾叉/循环箭头/曲线，二维数学、重音与断词 |
| Robin v1 | 30页；主文、Methods、书目、内嵌Supplementary Material，末尾10个CKD candidates | P4/P7/P28 CFF字体告警与P6/P28 XObject上限造成具体图面缺失；图轴/标签/代码框排版。不是整页提取失败 |
| Kosmos v2 | 42页；8图、Methods、contributions/funding、书目、内嵌SI1–4，末段refuted evaluation完整 | 原生词间空格粘连；图面、表序、二维公式。±数值与负面评价实际保留，不沿用旧损失描述 |

准入范围是未修改的编译论文原件及其有损native/page派生，不包括底层模型、代码、数据、独立被引全文、旧源码模板。Kosmos的独立Supplementary Data1–7、报告/轨迹/数据/code只是外链，明确不在本次42页目标内；不能据此宣称整套科研证据已获取，也不能把外链当内部缺页。原件内正式附录全部保留。旧source/archive版本、旧许可门控和既有retrieval不被新表示追溯覆盖。

### 9.1 实際信用与有界纠偏（Attribution and bounded corrections）

- RE-Net实际v4副题为“Autoregressive Structure Inference over Temporal Knowledge Graphs”，与旧collection副题差异有说明；使用合同已核ACL版本对应，不将arXiv nonexclusive当许可。MEND与SERAC的Finn/Manning作者次序不同，逐件按实际byline。Survey的ACM DOI是placeholder，不补造出版事实。
- WIKIGENBENCH保留P14 Wikipedia 2023 USFL season的有限摘要/截断信息及出处，AL.com新闻标题和6词省略片段；不是整篇新闻或Wikipedia独立授权。旧bib中的IBM摘要不在新PDF，不把旧包疑点迁移成新正文内容。
- ResearchAgent Table16的三个输入确有约180/149/370词完整摘要，不降格为普通书目。主线于2026-09-17进行两次有限官方metadata核查，没有获取被引PDF：KAPING正确记录是[ACL 2023.nlrse-1.7](https://aclanthology.org/2023.nlrse-1.7/)，DOI 10.18653/v1/2023.nlrse-1.7，三作者Jinheon Baek、Alham Fikri Aji、Amir Saffari；旧证据的2023.matching-1.7不是正确绑定，保留其历史并新增更正。Test-Time Self-Adaptive Small Language Models记录为[ACL 2023.findings-emnlp.1033](https://aclanthology.org/2023.findings-emnlp.1033/)，官方五作者逐字为Soyeong Jeong、Jinheon Baek、Sukmin Cho、Sung Hwang、Jong Park。这些额外作者来自官方metadata，不冒充本PDF所印byline；官方页面的2016年后作品CC BY4说明与有限输入范围一并记录。第三项FlyWire输入保留实际标题、既有preprint出处和有界用途，不借后来出版版本或父论文许可证给底层作品整体重新赋权。
- Open-Endedness P10的10个Noun Project图标带CC BY3信用：tick/Delete—kareemovic；alien—Artem Yurov；girl—Teewara soontorn；year of rat—DailyPM；aircraft/concorde—mikicon；Plane—CAMB；humans—Ifanicon；Robot—Deemak Daksina。逐件原出处和许可范围留在新NOTICE；不另行抓取图标。
- Robin原版两处S10重复标签照留；真实资助是RetroBio，不能沿用误拼。旧源包88个bib abstracts不是新PDF的[1]–[69]书目。native字体/图面告警照实披露，不增加依赖或用OCR掩盖。
- Kosmos保留实际37人署名。P5的permission明确仅Fig2 **a/b**，不是旧source文件名暗示的b/c；p27[9]实际13作者、题名“Preoptic activation induces a torpor-like hypothermic and hypometabolic state that is cerebroprotective”及identifier 2025.10.24.684192入NOTICE。PDF没有该引用的可见URL/DOI或外部URI，不猜造，不GET。BioRender信用精确到Fig5 a/c、Fig6 a、Fig7 a、Fig8 a/f/g。保留论文内permission/credit，不宣布底层图板一般BY4或外部作品全文已获权。

### 9.2 普通消费入口（Ordinary consumer）

现有helper的绝对行号（含页标题）核出父摘要连续范围：RE-Net11–35、MEND9–29、SERAC6–32、Survey10–27、Open-Endedness7–27、Robin10–27、Kosmos13–29。仅Survey默认摘录混入题名/作者/机构，故使用已有primary_excerpt=10–27；其余默认父论文摘要正确，不新增解析分支或通过拼接改写内容。最终落盘TXT/selector和五个既有selected UID的消费绑定已在第10节稳定树重建后复核，以上内存核查本身不代替最终验证。没有新增claim、selected UID或trusted晋升。

## 10. 实际落盘、消费和本地验收（Persistence, consumption and local validation）

十项各持久化四件：`pdf-supplement/document.pdf`、`document.txt`、`selectors.jsonl`、自包含`NOTICE.md`；合计PDF 51,520,171 bytes、242物理页/242真实页定位器。既有649条root定位器保持。原件直接复用第8节真实响应，无重复下载、原件编辑、OCR或源码包重新获取。每项新grant在canonical、snapshot、manifest、rights review四处相等，完整法条来自既有BY4资产，没有另造共享资产或新框架。实际许可与信用路径分别见第9节和各NOTICE。

| UID | 原件 before → after | 文字 before → after | 新PDF页/selector |
| --- | --- | --- | ---: |
| arxiv-1904.05530 | unknown → complete | unknown → partial | 15 |
| arxiv-2110.11309 | unknown → complete | unknown → partial | 21 |
| arxiv-2206.06520 | unknown → complete | unknown → partial | 15 |
| arxiv:2310.16218 | unknown → complete | unknown → partial | 35 |
| arxiv:2402.04624 | unknown → complete | unknown → partial | 14 |
| arxiv:2402.18264 | unknown → complete | unknown → partial | 20 |
| arxiv:2404.07738 | partial → complete | unknown → partial | 30 |
| arxiv:2406.04268 | partial → complete | partial → partial | 20 |
| arxiv:2505.13400 | unknown → complete | unknown → partial | 30 |
| arxiv:2511.02824 | unknown → complete | unknown → partial | 42 |

十项新原件/TXT/NOTICE/selectors实际存在并已纳入Git索引；未做本phase fresh checkout。新PDF独立public allow与旧root block并存，K中的`target_representation_state=allow`和`observed.pdf_supplement.public_package_valid=true`明确表示新层；根级公开计数不因新表示改变。十项`complete_target_consumable=false`、resolution=unresolved，下一步均只需对已确认的文字损失作有界parser/图面提取评估；`ocr_assessment`是评估队列，不是默认OCR执行或全图无损门槛。Knowledge仍沿原candidate/不适用状态，零trusted晋升。

主线用现函数两次`replay_pdf_supplement`，同时mock禁止`fetch_bytes`和`prepare_capsule`；每项manifest及所有capsule文件在每轮均字节一致。然后以现`discover_records/rebuild_registry/write_indexes_and_audit`重建215条聚合，沿用确定性时间`2026-09-16T04:30:26Z`，不伪充本次GET时间。使用指定Python3.12.13/pypdf6.18.1，无生产code、tests、deps、schema或workflow修改。

普通`make demo`实际选择仍36个sources、189 objects、72 evidence、72 claims、135 Wiki页、357 typed links、3 context packs。五条正文Evidence确实使用新PDF TXT连续父摘要：MEND9–13、Survey10–13、Open-Endedness7–11、Robin10–12、Kosmos13–16。Kosmos原生词间粘连与Open-Endedness断词空格没有被偷偷修写；完整原件可回看。五个Source对象只更新来源版本/字节及rights，五个既有正文excerpt Claim随来源/rights/limitations重新绑定，其中Kosmos、Open-Endedness、Survey三条literal引用文字随新native内容变化；不是五个新claim，也不是所有claims字节不变。全部UID、collector-assessment、candidate/trust与非目标对象不变。

实际命令和结果（串行，未在demo/repro清理期间读取coverage或派生差异）：

- `make test PYTHON=/tmp/llm-wiki-ci-312-260916/bin/python`：8组共196项全部OK。
- `make demo`：demo/Wiki验证均0错误，build_id=`build:llm-wiki-v0:261023893e1f09a1`。
- `make reproducibility`：committed_tree_replay、full_demo_replay、compiler_only_replay、read_only_validation四阶段均169文件byte-identical；内含完整`make validate`。
- 稳定树完整性：215 metadata/215 manifests、3176库存文件、25737 selectors、0 warnings/0 errors；原始metadata验证248 YAML/215 migrated/0 legacy/0 errors；文档58 Markdown/5 YAML examples/80相对链接/0 errors；demo/Wiki零错误。PDF native字体/XObject告警仍按第9节披露，不能把validator的0 errors解释为无损文本。
- `scripts/audit_non_repo_coverage.py`默认只读复算PASS，前置新文件已stage；固定215=131+84，完整summary见本文frontmatter与K。原件complete37→47，文字partial45→54；严格complete仍8、unresolved仍123，candidate来源30、trusted0、无demo claim来源101。
- 主线与BASE逐项比较：121个非目标K条目、98个非目标R条目、205个非目标index/registry条目不变；十份完整历史K before严格相等；十份旧manifest除获准库存/local_bytes外全部字段保留；旧R全部字段/原evidence序列保留；208个旧非snapshot文件字节不变。不是只比较汇总计数。
- 全库`validate_publication_rights.py`如预期exit1：active_full_text103/audited108/blocked64/errors2。仅既有GraphRAG `arxiv:2404.16130`与CoScientist `arxiv:2502.18864`旧包不一致，仍按已登记P4对账；十个新PDF独立完整性与public package验证均无错误/blocks。不得把局部PASS冒称全库公开完成。

原件/手写输入/派生/聚合边界严格沿合同：新PDF与NOTICE为原件和信用包装；十canonical/snapshot/R/K为表示级状态；TXT/selector/manifest库存及必要index/registry/demo/Wiki均由现helper/generator产生。没有重写旧源码、旧root正文、README/NOTICE/selectors、retrieval或source_archive_url。当前终审阶段不再开启下一实现批次。

明确未做：尚无最终提交pair的CI/独立三维PASS，未Ready/merge PR22，未进入main，未做fresh main checkout；未运行全库在线materialize、未获取被引全文/外部SI报告/数据/模型、未改分支保护或使用bypass、未关闭Issue3/4、未删分支/历史/原件。关闭须最终精确head/base的独立需求/agentic/核心质量三维PASS和当前CI后正常merge，不能使用启动提交的旧CI作为凭据。

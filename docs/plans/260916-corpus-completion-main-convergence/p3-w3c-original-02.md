---
phase: P3-W3C-ORIGINAL-02
status: implementation_validated_pending_exact_pair_independent_review_and_CI
coverage_summary_state: actual_frozen_K_summary
coverage_summary: {"collection_records":215,"non_repo_total":131,"github_repo_excluded":84,"reported_content_tier_counts":{"excerpt_capsule":23,"full_text":97,"metadata_capsule":11},"source_type_counts":{"arxiv":73,"biorxiv":2,"blog":10,"industry":2,"journal":11,"methodology":7,"paper":2,"standard":24},"original_artifact_counts":{"complete":57,"metadata_only":12,"partial":6,"unknown":56},"text_extraction_counts":{"complete":8,"partial":67,"unavailable":12,"unknown":44},"action_bucket_counts":{"access_restricted":8,"author_manuscript_fetch":2,"complete_verified":8,"html_article_snapshot":11,"identity_or_version_ambiguous":3,"needs_boundary_verification":44,"ocr_assessment":36,"parser_only":6,"public_persistence_decision":11,"standard_spec_fetch":2},"public_redistribution_counts":{"allow":33,"block":65,"unknown":33},"content_inspected_full_text":59,"structure_only_full_text":38,"locally_persisted_complete":8,"knowledge_candidate_sources":30,"knowledge_trusted_sources":0,"knowledge_sources_without_demo_claims":101,"unresolved_sources":123}
execution_contract:
  plan_id: nonrepo-materialization-main-convergence-260916
  phase: P3-W3C-ORIGINAL-02
  base_branch: work/v0-meta-kb-initialization-demo-260910
  base_sha: e38cf93b7dbf421126281661bf6e1ff5fc7ee3c1
  target_branch: work/v0-meta-kb-initialization-demo-260910
  source_uids:
    - standard-w3c-prov-o
    - standard:w3c-owl2
    - standard:w3c-r2rml
    - standard:w3c-shacl
    - standard:w3c-skos
    - standard:w3c-sosa-ssn
    - standard:w3c-web-annotation
  allowed_paths:
    - docs/plans/260916-corpus-completion-main-convergence/p3-w3c-original-02.md
    - docs/plans/260916-corpus-completion-main-convergence/branch-ledger.yaml
    - raw_data/standard/PROV-O The PROV Ontology/metadata.yaml
    - raw_data/standard/OWL 2 Web Ontology Language/metadata.yaml
    - raw_data/standard/R2RML RDB to RDF Mapping Language/metadata.yaml
    - raw_data/standard/Shapes Constraint Language SHACL/metadata.yaml
    - raw_data/standard/SKOS Simple Knowledge Organization System/metadata.yaml
    - raw_data/standard/SOSA SSN Ontology/metadata.yaml
    - raw_data/standard/Web Annotation Data Model/metadata.yaml
    - materialized_sources/corpus/standard-w3c-prov-o--6f83f2d8/**
    - materialized_sources/corpus/standard-w3c-owl2--602129ed/**
    - materialized_sources/corpus/standard-w3c-r2rml--b9b6cc67/**
    - materialized_sources/corpus/standard-w3c-shacl--63e18f6d/**
    - materialized_sources/corpus/standard-w3c-skos--02ed3abb/**
    - materialized_sources/corpus/standard-w3c-sosa-ssn--33efc488/**
    - materialized_sources/corpus/standard-w3c-web-annotation--3f6ab1c4/**
    - raw_data/licenses/w3c-original-02-2002-260918.md
    - raw_data/licenses/w3c-original-02-2015-260918.md
    - raw_data/audits/materialization_rights_review.yaml
    - raw_data/audits/non_repo_materialization_coverage_2026-09-16.yaml
    - scripts/materialize_all_sources.py
    - scripts/validate_materialization_completeness.py
    - scripts/validate_publication_rights.py
    - scripts/audit_non_repo_coverage.py
    - tests/test_materialization_integrity.py
  generated_paths:
    - materialized_sources/index.yaml
    - source_registry/registry.yaml
    - source_registry/registry.jsonl
    - raw_data/audits/materialization_completeness_2026-09-10.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/**
  explicitly_out_of_scope:
    - all_other_208_source_UIDs_and_84_repository_body_acquisition
    - new_normalized_W3C_derivatives_or_new_claims_or_demo_selection
    - root_document_selectors_NOTICE_revision_retrieval_or_public_gate_replacement
    - full_site_suite_references_datasets_weights_OCR_or_source_script_execution
    - complete_verified_relaxation_or_native_HTML_as_automatic_preprocessing_completion
    - P4_P5_main_merge_issue_closure_protection_change_force_push_deletion_or_migration
---

# P3-W3C-ORIGINAL-02 — 七份既定规范原件的有界保全

## Executed scope

- Phase：P3-W3C-ORIGINAL-02；adapter family：`generic_web_or_document_v2`；主要 bucket：`standard_spec_fetch`。
- Base：work `e38cf93b7dbf421126281661bf6e1ff5fc7ee3c1`；短期分支：`codex/p3-w3c-original-02-260918`。
- 启动检查点（历史）：仅报告与分支台账，彼时正文GET、原件准入、接缝代码、生成、测试均未执行。当前执行与验证见下文，不以启动状态覆盖已发生事实。
- 当前 HEAD：以本报告所在提交及对应 PR 为准，避免自引用提交号；最终审核必须绑定实际 head/base。
- 已完整读取 Issue #3/#4、README、02/03/04/05/06、plan.yaml、branch-ledger.yaml，并核对远端当前仅父 PR #1 open/Draft。前批 PR26 已于 2026-09-17T16:08:48Z 合入本 base，独立三维 PASS、CI #120 success；父 PR 当前 CI #121 也 success，但非最终放行。

## 用户目标、工作假设与选择

固定范围仍是 215＝131 非 repo 正文目标＋84 repo 排除项。本批补的是已明确缺失的目标原 HTML 及其必要正文素材，不是新增研究来源。旧 Markdown 中已观察到的表格、定义、书目缺口不能仅以 unknown 消失。

考虑三条路径：现有 paired HTML→Markdown；独立保全原件；继续只留旧有损文本。当前实际软件／用途证据不足以闭合七份新重排表示的有限实现用途，不能通过软件标签或 non-normative 声明造 grant；因此选择**独立原件保全（original-only retention）**，不新发布转换文本，不扩大旧 root grant。只留旧文本不能补已知原件缺口。

2002/2015 文档许可及官方格式 FAQ 已实读；复制、派生与技术规范发布分开判断。实际作品版权、STATUS、联合权利／必要媒体仍须随原件核对。相关官方依据：[2002](https://www.w3.org/copyright/document-license-2002/)、[2015](https://www.w3.org/copyright/document-license-2015/)、[格式与注释 FAQ](https://www.w3.org/Consortium/Legal/IPR-FAQ-20000620-new.html#format)。这不是用软件许可替换规范主体许可。

**本选择只交付真实原件增量，不缩小全文预处理目标。** 不把 native HTML 自动写成 `text_extraction=not_applicable`，不修改严格完成判据，不把旧 partial/unknown 转成 complete；保留真实转换缺口及 unresolved。02/05 的结构文本、定位、消费要求仍适用。原件可读不等于已完成整个 pipeline。

## 首轮网络与准入边界

启动 PR 公开后，先在临时目录保存下表的实际 HTTP 响应及 UTC、requested/resolved URL、状态、类型、编码与字节信息。三条 dated URL 来自既有 Rights Audit 的真实记录；另外四条只以当前 canonical 核实真实 This version，再将所见准确 dated URL 公开补入合同后获取，不凭模板推日期。不把 canonical 新版自动当作旧固定版。

| UID | 首轮唯一候选入口 | 已有目标版本／必须核实项 |
| --- | --- | --- |
| `standard-w3c-prov-o` | https://www.w3.org/TR/prov-o/ | 2013-04-30 REC；实核 This version |
| `standard:w3c-owl2` | https://www.w3.org/TR/2012/REC-owl2-overview-20121211/ | 2012-12-11 Overview；不扩整个 OWL suite |
| `standard:w3c-r2rml` | https://www.w3.org/TR/2012/REC-r2rml-20120927/ | 2012-09-27 REC |
| `standard:w3c-shacl` | https://www.w3.org/TR/2017/REC-shacl-20170720/ | 2017-07-20 REC |
| `standard:w3c-skos` | https://www.w3.org/TR/skos-reference/ | 2009-08-18 REC；实核 This version |
| `standard:w3c-sosa-ssn` | https://www.w3.org/TR/vocab-ssn/ | 2017-10-19 REC／2017-12-08纠链关系待核，不选新版本替代 |
| `standard:w3c-web-annotation` | https://www.w3.org/TR/annotation-model/ | 2017-02-23 Data Model；实核 This version，不扩协议／词汇套件 |

原响应不重写链接、不插 footer、不改 STATUS、版权或字符编码。若实际传输压缩，保留实际传输事实及机械解码对应，不把二次请求当同一响应。TLS／HTTP 失败如实记录，不关闭验证或绕访问控制。

初轮不抓素材。先逐 UID 检查原件首中末、章节／附录／引用、实际正文 img/object、信用及源路径；然后公开**有限精确素材 URL→本地路径**和适用范围的补充合同，才取必要原对象。logo／主题／整站 CSS／脚本不是默认正文要求，不执行原脚本、不爬引用。身份歧义停止该批，范围变化先修订合同。

未经准确作品／表示的许可条件闭合，临时响应不进入公开 repo。正文素材未取得时逐件记录 missing/limitations，不能宣称原件 complete。

## Source results（启动前→后）

### 首轮实际观察与固定 URL 修订（固定版 GET 前公开）

PR #27 已公开，启动 HEAD `c6153b0a7da218c4d85812ce9b768bf53acfbbf4`。首次七 GET 观察窗口为 **2026-09-17T16:34:28Z 至 16:34:41Z**；后者是工具确认完成的时刻，不伪称精确网络结束秒。每个响应 Date 均为 `Thu, 17 Sep 2026 16:34:30 GMT`。七请求均 curl exit0、HTTP200、无redirect、TLS verification result0、`text/html; charset=utf-8`，无 Content-Encoding。原始实体和headers仅暂存，未入repo。

| UID | 首轮实际bytes | 真实This version及下一步 |
| --- | ---: | --- |
| `standard-w3c-prov-o` | 464179 | raw L1259 实见 https://www.w3.org/TR/2013/REC-prov-o-20130430/ ；批准下一次仅该固定版GET |
| `standard:w3c-owl2` | 43840 | 已请求固定2012-12-11 Overview；继续离线核读，不重复GET |
| `standard:w3c-r2rml` | 172544 | 已请求固定2012-09-27；继续离线核读，不重复GET |
| `standard:w3c-shacl` | 531275 | 已请求固定2017-07-20；继续离线核读，不重复GET |
| `standard:w3c-skos` | 227150 | raw L28–30 实见 https://www.w3.org/TR/2009/REC-skos-reference-20090818/ ；批准下一次仅该固定版GET |
| `standard:w3c-sosa-ssn` | 673275 | raw L823–826 实见 https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/ ，L923起实见2017-12纠链说明；批准下一次仅该固定版GET，不能省略纠链状态 |
| `standard:w3c-web-annotation` | 284185 | raw L825–828 实见 https://www.w3.org/TR/2017/REC-annotation-model-20170223/ ；批准下一次仅该固定版GET |

此修订只增加上述四个实际发现的固定原件URL，不授权正文素材GET、代码实现或公开原件准入。canonical与dated是否逐字相同须用真实第二响应核对，不预设。源码行号仅定位本次已留临时实体，不是新生成selector。

七项启动时 K 均为 original unknown、text unknown、partial_check、root public block、unresolved；这不是没有正文：旧 `document.md` 与 `selectors.jsonl` 已存在，但当时没有目标原 HTML。各 UID 的版本边界和具体旧文本缺口如下。知识准入不变，不选入 demo、不晋 trusted。

| UID | 具体已有缺口 | 本批 After |
| --- | --- | --- |
| `standard-w3c-prov-o` | §1.3命名空间表、§4.4索引／附录A表、G书目 | 实见原HTML与5SVG；具体提取损失仍在，不补新派生 |
| `standard:w3c-owl2` | Overview图1、§7书目，不能泛称OWL套件完整 | 实见本Overview与1PNG；不扩suite，不宣称T complete |
| `standard:w3c-r2rml` | §2.1数据库表、§10.5词法表、B类属性表、C书目 | 实见原HTML与6PNG；仅5PNG准入，UML总览图ICC未清关 |
| `standard:w3c-shacl` | D规范校验器、H书目、旧代码注释误作标题 | 实见原HTML；唯一箭头PNG的ICC未清关，图形保留partial |
| `standard:w3c-skos` | §3.2/3.3定义、A类属性表、书目 | 实见原HTML无必要外部正文图；§8.6.1文字树图已内嵌，纠正旧“实引图缺”泛称 |
| `standard:w3c-sosa-ssn` | §6.1对齐定义、E书目、旧标题污染；纠链版本需绑定 | 实见纠链原HTML与27PNG；OGC/W3C联合信用保留，旧T缺口仍在 |
| `standard:w3c-web-annotation` | A媒体／selector矩阵、模型表、H书目 | 实见原HTML与1PNG；旧表格/书目未重建，不扩其他套件 |

### 实物驱动的素材获取修订（素材 GET 前公开）

四份额外固定版 GET 已执行：开始观察2026-09-17T16:37:04Z，完成观察16:37:26Z（SOSA 16:37:27Z）；均HTTP200／零redirect／TLS0／UTF-8 HTML，实际bytes分别PROV464179、SKOS227150、SOSA673275、Annotation284185。四组canonical与fixed实体实际cmp均exit0。仅fixed实体作为拟保留原件，canonical不重复包装。

从七份实际固定HTML的body核得 **41个必要媒体＝PROV5 SVG＋OWL1 PNG＋R2RML6 PNG＋SHACL1 PNG＋SOSA27 PNG＋Annotation1 PNG**；SKOS无必要外部正文img/object，内嵌文字图保留于原HTML。下表全部是实际src按所见固定文档URL解析，local_path相对于各UID既有capsule；原HTML固定存source/specification.html，因此原相对图路径无需改写。只批准这41条的临时GET，不批准额外子资源或代码实现。

PROV为术语／示例／qualification关系图，OWL为语法／本体／语义关系图，R2RML为正文UML图（原文§D明确Boris Villazón-Terrazas绘制／更新，原致谢保留），SHACL为图中继承箭头（类框是HTML内联），SOSA为23个figure中的27个本体／对齐图，Annotation为基本三部件模型。SOSA原件保留OGC与W3C联合版权及2017-12纠链STATUS；Figure22/23及OBOE/PROV出处和参考文献原样保留，不递归获取这些外部作品。当前HTML未见这些图的单独排除条款；素材返回后仍核真实格式、信用及SVG依赖，不能预先把媒体allow写入机器记录。

W3C／OGC／ORCID／validator logos、主题CSS与脚本不列入正文媒体；未下载不等于删除原HTML中的引用。原件浏览器完整主题渲染不作为本批保证；不执行源脚本或SVG活动内容。若素材实有外部依赖／独立限制，先列准确对象及影响修订合同，不自动递归。

| UID | 原HTML行 | 准确媒体URL | capsule内路径 |
| --- | ---: | --- | --- |
| `standard-w3c-prov-o` | 1832 | https://www.w3.org/TR/2013/REC-prov-o-20130430/diagrams/starting-points.svg | `source/diagrams/starting-points.svg` |
| `standard-w3c-prov-o` | 1929 | https://www.w3.org/TR/2013/REC-prov-o-20130430/diagrams/starting-points-example.svg | `source/diagrams/starting-points-example.svg` |
| `standard-w3c-prov-o` | 1947 | https://www.w3.org/TR/2013/REC-prov-o-20130430/diagrams/expanded.svg | `source/diagrams/expanded.svg` |
| `standard-w3c-prov-o` | 2143 | https://www.w3.org/TR/2013/REC-prov-o-20130430/diagrams/expanded-terms-example-bundlePost.svg | `source/diagrams/expanded-terms-example-bundlePost.svg` |
| `standard-w3c-prov-o` | 2587 | https://www.w3.org/TR/2013/REC-prov-o-20130430/diagrams/qualified-patterns.svg | `source/diagrams/qualified-patterns.svg` |
| `standard:w3c-owl2` | 152 | https://www.w3.org/TR/2012/REC-owl2-overview-20121211/OWL2-structure2-800.png | `source/OWL2-structure2-800.png` |
| `standard:w3c-r2rml` | 416 | https://www.w3.org/TR/2012/REC-r2rml-20120927/images/uml-overview.png | `source/images/uml-overview.png` |
| `standard:w3c-r2rml` | 1140 | https://www.w3.org/TR/2012/REC-r2rml-20120927/images/logical-table.png | `source/images/logical-table.png` |
| `standard:w3c-r2rml` | 1378 | https://www.w3.org/TR/2012/REC-r2rml-20120927/images/triples-map.png | `source/images/triples-map.png` |
| `standard:w3c-r2rml` | 1537 | https://www.w3.org/TR/2012/REC-r2rml-20120927/images/term-map.png | `source/images/term-map.png` |
| `standard:w3c-r2rml` | 2114 | https://www.w3.org/TR/2012/REC-r2rml-20120927/images/ref-object-map.png | `source/images/ref-object-map.png` |
| `standard:w3c-r2rml` | 2294 | https://www.w3.org/TR/2012/REC-r2rml-20120927/images/graph-map.png | `source/images/graph-map.png` |
| `standard:w3c-shacl` | 1409 | https://www.w3.org/TR/2017/REC-shacl-20170720/images/Class-Diagram-Arrows.png | `source/images/Class-Diagram-Arrows.png` |
| `standard:w3c-sosa-ssn` | 1255 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/modular_ontology.png | `source/images/modular_ontology.png` |
| `standard:w3c-sosa-ssn` | 1419 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/SSN-OntStructure-Overview.png | `source/images/SSN-OntStructure-Overview.png` |
| `standard:w3c-sosa-ssn` | 1426 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/SOSA-OntStructure-Observation.png | `source/images/SOSA-OntStructure-Observation.png` |
| `standard:w3c-sosa-ssn` | 1430 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/SSN-OntStructure-Observation.png | `source/images/SSN-OntStructure-Observation.png` |
| `standard:w3c-sosa-ssn` | 1435 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/SOSA-OntStructure-Actuation.png | `source/images/SOSA-OntStructure-Actuation.png` |
| `standard:w3c-sosa-ssn` | 1439 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/SSN-OntStructure-Actuation.png | `source/images/SSN-OntStructure-Actuation.png` |
| `standard:w3c-sosa-ssn` | 1444 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/SOSA-OntStructure-Sampling.png | `source/images/SOSA-OntStructure-Sampling.png` |
| `standard:w3c-sosa-ssn` | 1448 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/SSN-OntStructure-Sampling.png | `source/images/SSN-OntStructure-Sampling.png` |
| `standard:w3c-sosa-ssn` | 1471 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/SOSA-Observation.png | `source/images/SOSA-Observation.png` |
| `standard:w3c-sosa-ssn` | 1476 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/SSN-Observation.png | `source/images/SSN-Observation.png` |
| `standard:w3c-sosa-ssn` | 2053 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/SOSA-Actuation.png | `source/images/SOSA-Actuation.png` |
| `standard:w3c-sosa-ssn` | 2058 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/SSN-Actuation.png | `source/images/SSN-Actuation.png` |
| `standard:w3c-sosa-ssn` | 2415 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/SOSA-Sampling.png | `source/images/SOSA-Sampling.png` |
| `standard:w3c-sosa-ssn` | 2419 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/SSN-Sampling.png | `source/images/SSN-Sampling.png` |
| `standard:w3c-sosa-ssn` | 2799 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/SSN-Features.png | `source/images/SSN-Features.png` |
| `standard:w3c-sosa-ssn` | 3083 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/SSN-Results.png | `source/images/SSN-Results.png` |
| `standard:w3c-sosa-ssn` | 3280 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/SSN-Procedures.png | `source/images/SSN-Procedures.png` |
| `standard:w3c-sosa-ssn` | 3611 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/SSN-Systems.png | `source/images/SSN-Systems.png` |
| `standard:w3c-sosa-ssn` | 4035 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/SSN-Conditions.png | `source/images/SSN-Conditions.png` |
| `standard:w3c-sosa-ssn` | 4041 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/SSN-System-Properties.png | `source/images/SSN-System-Properties.png` |
| `standard:w3c-sosa-ssn` | 5222 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/sample-relationships.png | `source/images/sample-relationships.png` |
| `standard:w3c-sosa-ssn` | 6458 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/OBOE-core.png | `source/images/OBOE-core.png` |
| `standard:w3c-sosa-ssn` | 6459 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/SOSA-obs-core.png | `source/images/SOSA-obs-core.png` |
| `standard:w3c-sosa-ssn` | 6569 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/prov-o.png | `source/images/prov-o.png` |
| `standard:w3c-sosa-ssn` | 6570 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/observation-prov.png | `source/images/observation-prov.png` |
| `standard:w3c-sosa-ssn` | 6571 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/actuation-prov.png | `source/images/actuation-prov.png` |
| `standard:w3c-sosa-ssn` | 6572 | https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/sampling-prov.png | `source/images/sampling-prov.png` |
| `standard:w3c-web-annotation` | 1060 | https://www.w3.org/TR/2017/REC-annotation-model-20170223/images/intro_model.png | `source/images/intro_model.png` |

上表为 GET 前的有限授权清单，不把获取成功自动当作许可准入。41次 GET 现已完成，均HTTP200／exit0／零redirect／TLS0；观察窗口2026-09-17T16:42:02Z起，各次完成观察记录随获准包保留。5 SVG无外部渲染依赖或活动脚本；36 PNG格式/IEND与尺寸核实。正文图实物核查发现两项嵌入第三方ICC声明：R2RML `images/uml-overview.png` 内Apple Display profile的cprt为Copyright Apple, Inc., 2012；SHACL `images/Class-Diagram-Arrows.png` 内Gray Gamma 2.2的cprt为Copyright (c) 1999 Adobe Systems Incorporated. All Rights Reserved. 当前未闭合这些profile再分发条件，不剥除、不重写原PNG、不自动借用W3C grant。

本批只准入其余39图；上述两图保留临时响应事实，但**不进入公开胶囊**，各自original_retention明确unretained_assets及limitations/status=partial。HTML原字节和相对引用不改。这是公开保留缺口，不是网络失败、原作品无图或wholeUID已完成。PROV qualified-patterns.svg内11个指向不存在#Entity的导航链接是原件自带瑕疵，不捏造补图或修改原SVG。

### 原件保全实施修订（implementation amendment，代码/包装前公开）

准入七HTML原样副本及上述39正文媒体；原版权/STATUS/作者/致谢/书目均随原HTML保留。四份2002许可、三份2015许可分别使用独立完整NOTICE载体；SOSA保留OGC & W3C联合版权和2017-12纠链状态，R2RML保留Boris Villazón-Terrazas绘图信用。通知只覆盖实际列定原件，不扩大旧转换授权，不是软件许可替换文档许可。

采用独立预核建议的最小字段，复用现有PDF层的权利与inventory结构：

- C与snapshot的`versioning.original_retention={source_version, source_version_url}`绑定实际固定TR；旧root version不替换。
- C/snapshot的`rights.original_retention`、M的`original_retention.rights`、R的`original_retention`四方相等。沿用`license_spdx/license_url/license_verified_at/publication_gate/redistribution_package`，包含既有六字段及source_version；`approved_scope`必须等于该独立包scope。license_spdx若为本地LicenseRef只表示真实文档许可ID，不冒充软件SPDX。
- M的`original_retention`声明`source_version/revision/media_type/source/status/retrievals/retained_assets/unretained_assets/limitations/rights`；source固定source/specification.html，media_type为text/html。媒体保留原relative src列表，对应source/<src>及固定版urljoin、真实retrieval和既有inventory；SKOS空媒体列表合法，整个声明null/空/错误类型不合法。两项未留图不参与retained库存或allow scope；保留对应真实GET但明确未准入事实，不能伪称已下载入repo。
- 包装阶段仅写一次完整文件、独立NOTICE、metadata快照、README与manifest库存；可有最小内存builder复用既有inventory/预检，但不添加CLI/适配器/二次派生。正常materialize_one→generic路径只读完整预检并返回现manifest，禁止fetch/prepare/derive/finalize/apply或任何胶囊写入。失败用既有保护异常贯穿normal caller，不降metadata_only。
- 分派采用key presence，覆盖M、C、snapshot声明及sourceNOTICE/原HTML哨兵；paired retained_text/sidecar碰撞失败。已声明保留的文件缺失、篡改或路径重复/逃逸/symlink/alias均失败零写；明确unretained允许partial。独立rights在root tier过滤前验证，root gate保持block。
- coverage仅新增observed.original_retention；target显式representation=original_retention且其独立版本/实际校验相符才匹配，不改严格完成谓词。真实原件证据支持A更新，但旧文本已证明缺表/定义/书目，T仅unknown→partial，resolution继续unresolved。

授权实际修改仍限原合同四个生产文件、一个测试文件和七UID数据/两个通知载体/报告台账及必要派生物；本修订不批准额外网络获取。字段更改只为这类独立原件保全，不引入泛化框架。

### 原件内容实读（content evidence，不以文件存在代替正文核对）

行号均指各胶囊`source/specification.html`原始行；不是新增selector，也不是摘要文本。核读覆盖每份首中末、全部正文img/object引用、原版权／STATUS、既有提取缺口；媒体核查另读实际SVG XML或PNG块，并抽看9张PNG，不声称41图全部视觉详审或全图OCR。

| UID | 首部／中部／末尾的实际核点 | 内容与范围判断 |
| --- | --- | --- |
| PROV-O | L1259–1381身份/STATUS；L1832–2587三类关系/例子/图；L9557–10005索引与profile；L10457–10611致谢/20项书目/body闭合 | §1.3有6行命名空间表；§4.4有81行术语表；附录A两表6/5行。五SVG绘图marker完整；两处Figure4为原编号，不修正。 |
| OWL2 | L20–116身份/STATUS；L147–221图1与6行语法表；L239–336的14行路线图；L353–416致谢/15项书目至结尾 | 文档明确informative only；Overview确为所选目标，其13个suite部件链接不是这次必须抓取的独立正文。 |
| R2RML | L58–152身份/STATUS；L422–457 EMP/DEPT两表；L1534–2110 term-map定义/例子；L2697–2835词法表；L3251–3618词汇/书目/致谢至结尾 | 词法表21个tr含rowspan；附录B三表13/26/6行，C有15项书目。D实署Boris绘图信用；仅总览PNG因ICC未准入，不将缺口写网络失败。 |
| SHACL | L614–715身份/STATUS；L1383–1450类图；L2611–2643 Core/SPARQL区分；L6097–6284规范校验器表；L6303–6384致谢与6规范/2信息书目至结尾 | 类框在HTML、继承箭头在989B PNG；该图尚未公开保留。旧document D2492–2497/H2530–2536仍空缺表/书目。 |
| SKOS | L22–89身份/摘要；L1336–1358 Concept/S1实际表；L2708–2727文字树图；L4333–4611书目/致谢/A类属性表；L6123–6310替代格式/历史至结尾 | 旧document L1174–1180和2274–2283缺表；L1737–1750文字树图已有，不误报缺外图；RDF/XML/OWL替代格式不并入本Reference HTML目标。 |
| SOSA/SSN | L804–945联合署名/2017-12纠链；L1205–1275 modularization；L5380–5525 DUL命名空间/类/复杂OWL对齐表；L6380–6495 OBOE对齐与Figure22；L8326–8332致谢及E书目至body结尾 | 23个figure共27PNG；Figure22有2图、Figure23有4图均保留。旧document L889–905只有类对齐引导没有表，E实际条目缺；不能用原图保留宣称旧文本无损。 |
| Annotation | L824–901身份/规范性/摘要；L1049–1062基本模型；L1223–1271 Term/Type/Description；L2789–2851 TextQuoteSelector exact/prefix/suffix；L3886–4102矩阵；L4569–4792致谢/书目至结尾 | A矩阵7个selector列/11类媒体、A.1五组合及TSV/Turtle脚注均实见；旧document L151–156、869–879、1088–1095缺表/书目。例子中的CC BY/NC是示例数据，不替换规范许可。 |

两嵌入ICC只影响两件PNG的本次公开保留；未观察其他实物额外许可通知，不等于保证全链无权利。HTML中的作者、机构、OGC与W3C联合声明、例子、原科学出处均随原字节保留；不递归获取书目、字体、DTD或来源脚本。

### 六维 Before / After（冻结 K 实际值）

下表知识状态null表示无所选demo claim，不伪造candidate；本批没有新增selector。Local列为已跟踪inventory件数（不含manifest），全部声明文件存在；新导出验证成功，但T缺口使complete_target_consumable=false。七项resolution均unresolved，action_bucket均public_persistence_decision，严格完成不增加。

| UID | 原件 A | 提取 T | Local 库存 | Selectors | 公开权限 P | 知识准入 |
| --- | --- | --- | ---: | --- | --- | --- |
| `standard-w3c-prov-o` | unknown → complete | unknown → partial | 4 → 11 | 989不变，旧定位仍有效 | root block不变；独立原件allow | null不变，无新claim |
| `standard:w3c-owl2` | unknown → complete | unknown → partial | 4 → 7 | 86不变，旧定位仍有效 | root block不变；独立原件allow | null不变，无新claim |
| `standard:w3c-r2rml` | unknown → partial | unknown → partial | 4 → 11 | 616不变，旧定位仍有效 | root block不变；独立原件allow | null不变，无新claim |
| `standard:w3c-shacl` | unknown → partial | unknown → partial | 4 → 6 | 649不变，旧定位仍有效 | root block不变；独立原件allow | null不变，无新claim |
| `standard:w3c-skos` | unknown → complete | unknown → partial | 4 → 6 | 706不变，旧定位仍有效 | root block不变；独立原件allow | null不变，无新claim |
| `standard:w3c-sosa-ssn` | unknown → complete | unknown → partial | 4 → 33 | 755不变，旧定位仍有效 | root block不变；独立原件allow | null不变，无新claim |
| `standard:w3c-web-annotation` | unknown → complete | unknown → partial | 4 → 7 | 434不变，旧定位仍有效 | root block不变；独立原件allow | null不变，无新claim |

## Files 与最小实现边界

启动提交只更改报告与ledger；实际原件、有限许可/素材核查、独立预核与16:51:05Z公开实施修订完成后，现已实施上方四个生产文件和一个既有测试文件的窄opt-in `original_retention`。没有新增builder、adapter、CLI、依赖、schema框架或第二套hash机制。下面是实际遵循的实现边界。

- manifest 独立原件层与 C／snapshot／R 四方权利一致；完整通知独立存放，原 root rights/revision/retrieval/document/selectors/NOTICE 原样保留。
- 正常 materializer 重放必须先只读校验再保全原件；不进入清目录／重抓／派生的 fallback，不误降 metadata-only。未声明原件依旧 fail closed。
- 包装阶段写齐后，重放只读 preflight 并返回现 manifest，不重写 README／manifest、不调用 finalize 或 apply。声明已留的原件／素材缺失或库存不符必须拒绝且零写；明确未留或未准入素材以逐件 missing／limitations 保持 partial，不要求全部外链先清关，但不能计 original-complete 或完整目标可消费。
- 完整性校验只对明确原件层分派；root inventory／selectors 验证不取消。公开检查同时保留 root block，不以新原件 allow 掩盖旧表达。
- coverage 只新增真实原件观察和允许的版本事实，不改 complete_verified 逻辑，不删除旧提取证据。旧未知若由具体缺口证据改成 partial，必须逐项说明，不计完成。
- 仅七个 capsule 的新增原件／必要媒体／source NOTICE及外部包装、七 C/R/K 对象和必要聚合物可变；其余124 K对象、101 R对象（当前R总108）及208来源事实不变。
- 七 UID 不在当前 selected set；不改选源或claim内容。R/K属于既有build输入，若生成器因此需要全局build identity刷新，须在C/R/K冻结后统一生成并核实其他语义对象不变，不手改派生文件。

## Verification（执行记录与剩余门控）

代码与七数据包已冻结。实际7 HTML=2,396,448B、39媒体=2,005,406B、7独立NOTICE=60,656B；七胶囊inventory为81文件/6,450,666B，实际含manifest为88文件，独立retrieval46条。R2RML/SHACL各一图未准入且独立层partial，其余五独立层materialized；这不是whole UID或旧文本complete。

- 主线实际normal `materialize_one`每UID两次，共14次：88个胶囊文件逐byte相等，fetch/prepare/finalize/apply/write_yaml/write_jsonl/write_readme/derive/retained-text-replay/rmtree均0调用。第一次OWL真实重放曾因`content_encoding: null`被误当压缩失败；此失败零写，随后校验只允许缺字段/null，仍拒非null压缩及transport字段，实际14次重跑通过。没有删除真实获取字段来迁就测试。
- 另从当前stage完整导出到全新目录，使用导出repo自身代码和七数据包再次各两次normal replay：14次/88文件byteequal、全部上述副作用0、exit0。运行不引用staging原件或未入repo的两个PNG；这只证明本批七包可离线续作，不冒充最终main fresh checkout或全库已完成。
- 作者最终定向integrity102 tests/12.285s/exit0（原93+新增9），PDF49 tests/3.432s/exit0。主线完整 `make test` 232项通过（4+20+12+13+102+49+2+30）；它们证明接缝和回归，不代替本批原件内容检查或最终CI。
- 主线对exact BASE实际保全核对exit0：七C/snapshot去新增nested keys后对象不变；七M除独立层和库存统计外旧字段不变；root document/selectors逐byte不变、README旧完整前缀保留；七R旧evidence/gate/missing/历史不变、其余101R完整对象及R顶层summary不变。两个未准入PNG在repo中不存在。
- 主线已调用既有aggregate函数，保留确定性stamp `2026-09-16T04:30:26Z`，该stamp不是本批GET时间。215记录、3,258库存文件、270,347,332B，旧root status/tier分布不变；没有全库重抓或重物化。
- 主线实际global materialization validator exit0：metadata215/manifest215/hashed3258/selectors25869/warnings0/errors0。运行期间既有PDF路径输出缺fontTools的pypdf字体warning，不属于本批HTML缺失，也未因此安装或改依赖。
- 主线global publication validator exit1：既有GraphRAG（2404.16130）和CoScientist（2502.18864）两package差异，以及64个root公开blocks仍在；本批七独立原件没有新增package错误，也未让root block消失。这个global结果不是PASS，P4仍需处理真实工程错误和经授权的公开树选择。
- 冻结C/R/K后 `make demo` exit0：build `build:llm-wiki-v0:7825e3978fb6a0ee`，36 sources、72 claims、72 evidence、135 pages、357 typed links、3 context packs；没有新增本批claim或trusted晋升。
- `make reproducibility` exit0：committed_tree_replay、full_demo_replay、compiler_only_replay、read_only_validation四次均169文件逐byte相等；末段串行 `make validate` 全通过，raw248 YAML/215 metadata、完整性215 manifests/3258 inventory/25869 selectors、docs63 Markdown/86 links和Wiki21 inputs/154 outputs均errors0。
- 执行纠偏：主线误将首次独立 `make validate` 和coverage审计与 `make reproducibility` 同时运行；前者在重建临时窗口读缺 `07_review/queue.yaml` exit2，后者读到30项过渡claims状态而报stale observed。这两次不记PASS。已等待唯一重建完成；上述repro末段串行validate成功且169输出未变，coverage另在稳定树重跑。未为瞬时失败修改代码、来源或台账状态。
- 稳定树默认coverage审计重跑exit0：PASS non_repo_coverage，summary与本报告及K完全一致；215=131+84、严格完成8、unresolved123、trusted0。最终代码和七包再次从stage导出全新目录，以导出repo自身代码执行14次正常重放：88文件byteequal、全部副作用0。该导出不是最终main验收。
- 作者代码/文档/数据及生成文件的差异空白检查通过；未修改的外来HTML/SVG原件带有原作者尾空白，完整 `git diff --cached --check` 因这些原字节返回2。保留原件，不为了格式检查改写出版物；该结果与功能/可复现性校验分开。

已经执行的检查与剩余门控严格区分：

1. 每 UID 首中末、许可／STATUS、目标边界及全部实际必要媒体已核查，正文和媒体证据见上；不以 fixture 代替实物。
2. 聚焦测试已完成：正确独立原件重放、坏 grant／缺文件／inventory不符／路径逃逸／冲突声明均失败且不改旧胶囊；无 GET、无 derive、无清目录；普通配对HTML和旧root路径保持回归。
3. 七 UID 两次严格离线重放和候选索引新导出目录消费已完成，旧document/selectors/NOTICE/retrieval字节或对象不变；所有新文件和定位可从repo自身读取。最终提交仍须精确版本复审。
4. 当前最终输入的 `make test`、串行 `make validate`、`make reproducibility`、materialization完整性校验及coverage稳定树默认审计已按上述结果完成；生成前已冻结C/R/K。全库publication的既有2errors/64blocks单独报告，不冒称清零。
5. 精确最终HEAD/base独立 evaluator 三维审核及真实CI通过才正常merge；任何后续变化重审。父PR最终门控另行完成。

## Agentic decisions and independent evaluation

planner `fabric_canonical_planner` 已给出有限启动草案；独立非作者 `canonical21_content_evaluator` 已只读确认四文件接缝的必要性，并指出更小的只读 replay 路线。主线已采纳：排除T=not_applicable及strict-complete放宽；明确当前T是unknown，不能误称既有partial；区分声明已留文件缺失与明确未留媒体；包装完成后重放零写。下一步必须验证null/空/错误类型声明和碰撞失败、不落入metadata-only恢复、normal materialize_one路径成功及失败全胶囊零写；普通文件/无symlink及root tier过滤前独立权利检查也属于实现条件。这些是预核意见，**不是最终代码或三维验收PASS**。最终报告将记录真实取得／未取得、选择与纠偏、独立审核者、精确SHA、三维结论及CI，不预填PASS。

独立预审又实际复现一项阻塞：当manifest YAML损坏且原HTML同时缺失，已有C/snapshot独立标记及source/NOTICE未被最外层异常保护识别，normal materialize_one可能落入通用恢复并调用finalize。仅坏manifest或单缺HTML各自零写，组合fixture的finalize spy却实见1调用（spy阻止真实改写）；因此不能用101项绿色测试替代核心质量。本线已退回executor在manifest加载失败路径补识别并增加normal caller组合负例，修复及复审结果另按最终快照记录，不将此预审当关闭PASS。

该阻塞随后修复并由同一非作者 evaluator 独立复测：9项 OriginalRetentionTests 全部通过，C-only、snapshot-only、NOTICE-only以及null/empty child组合均受保护拒绝，原阻塞消除。evaluator 另对7个真实包执行generic/one各两次（共28调用），88文件逐byte相等，全部副作用spy为0；亲核7 HTML与固定版缓存、39媒体与GET缓存逐byte相等，确认两ICC图未入repo、partial披露及历史保全成立。上述仍是预审；不提前代替精确最终HEAD/base、K/生成树和当前CI的三维终审。

## Explicit non-results

本次提交候选包含7份选定原HTML、39个准入图件和独立通知；两个ICC图从未进入repo。代码、包装、实际七包重放、全局生成和可复现性已完成；最终独立评估及当前HEAD CI须在提交后绑定精确SHA，结果记录于PR，不用自引用SHA制造后继提交。本报告不预称已push/merge，不宣称完成预处理或关闭来源unresolved。没有进入main、没有P4/P5放行、没有trusted晋升、没有文件／分支删除、迁库、历史改写或保护变更。用户的ALCE／NC／宽泛目标决定仍未回答，不从本批授权外推。

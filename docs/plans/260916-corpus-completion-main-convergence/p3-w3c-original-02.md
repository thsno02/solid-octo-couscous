```yaml
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
```

# P3-W3C-ORIGINAL-02 — 七份既定规范原件的有界保全

## Executed scope

- Phase：P3-W3C-ORIGINAL-02；adapter family：`generic_web_or_document_v2`；主要 bucket：`standard_spec_fetch`。
- Base：work `e38cf93b7dbf421126281661bf6e1ff5fc7ee3c1`；短期分支：`codex/p3-w3c-original-02-260918`。
- 启动状态：仅报告与分支台账；正文 GET、原件准入、接缝代码、生成、测试、独立最终审核均未执行。
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

七项当前 K 均为 original unknown、text unknown、partial_check、root public block、unresolved；这不是没有正文：旧 `document.md` 与 `selectors.jsonl` 已存在，但没有目标原 HTML。各 UID 的版本边界和具体旧文本缺口如下。知识准入不变，不选入 demo、不晋 trusted。

| UID | 具体已有缺口 | 本批 After |
| --- | --- | --- |
| `standard-w3c-prov-o` | §1.3名单、§4.4索引／附录A表、G书目 | 未执行；待实物核与逐项结果 |
| `standard:w3c-owl2` | Overview图1、§7书目，不能泛称OWL套件完整 | 未执行；待实物核与逐项结果 |
| `standard:w3c-r2rml` | §2.1数据库表、§10.5词法表、B类属性表、C书目 | 未执行；待实物核与逐项结果 |
| `standard:w3c-shacl` | D规范校验器、H书目、旧代码注释误作标题 | 未执行；待实物核与逐项结果 |
| `standard:w3c-skos` | §3.2/3.3定义、A类属性表、实引图 | 未执行；待实物核与逐项结果 |
| `standard:w3c-sosa-ssn` | §6.1对齐定义、E书目、旧标题污染；纠链版本需绑定 | 未执行；待实物核与逐项结果 |
| `standard:w3c-web-annotation` | A媒体／selector矩阵、模型表、H书目 | 未执行；待实物核与逐项结果 |

## Files 与最小实现边界

本启动提交只更改报告与 ledger。上方四个生产文件、一个既有测试文件是**条件允许范围，不是已实施**：实际原件和许可闭合、独立预核确认必要字段与保全语义、公开补充合同后，才实现窄 opt-in `original_retention`。不新增 adapter、CLI、依赖、schema框架或第二套 hash 机制。

- manifest 独立原件层与 C／snapshot／R 四方权利一致；完整通知独立存放，原 root rights/revision/retrieval/document/selectors/NOTICE 原样保留。
- 正常 materializer 重放必须先只读校验再保全原件；不进入清目录／重抓／派生的 fallback，不误降 metadata-only。未声明原件依旧 fail closed。
- 包装阶段写齐后，重放只读 preflight 并返回现 manifest，不重写 README／manifest、不调用 finalize 或 apply。声明已留的原件／素材缺失或库存不符必须拒绝且零写；明确未留或未准入素材以逐件 missing／limitations 保持 partial，不要求全部外链先清关，但不能计 original-complete 或完整目标可消费。
- 完整性校验只对明确原件层分派；root inventory／selectors 验证不取消。公开检查同时保留 root block，不以新原件 allow 掩盖旧表达。
- coverage 只新增真实原件观察和允许的版本事实，不改 complete_verified 逻辑，不删除旧提取证据。旧未知若由具体缺口证据改成 partial，必须逐项说明，不计完成。
- 仅七个 capsule 的新增原件／必要媒体／source NOTICE及外部包装、七 C/R/K 对象和必要聚合物可变；其余124 K对象、101 R对象（当前R总108）及208来源事实不变。
- 七 UID 不在当前 selected set；不改选源或claim内容。R/K属于既有build输入，若生成器因此需要全局build identity刷新，须在C/R/K冻结后统一生成并核实其他语义对象不变，不手改派生文件。

## Verification（计划，尚未运行）

1. 每 UID 首中末、许可／STATUS、目标边界及全部实际必要媒体核查；不以 fixture 代替实物。
2. 聚焦测试：正确独立原件重放、坏 grant／缺文件／inventory不符／路径逃逸／冲突声明均失败且不改旧胶囊；无 GET、无 derive、无清目录；普通配对HTML和旧root路径保持回归。
3. 七 UID 两次严格离线重放和新导出目录消费，旧document/selectors/NOTICE/retrieval字节或对象不变；所有新文件和定位可从repo自身读取。
4. 当前最终输入执行 `make test`、`make validate`、`make reproducibility`、materialization完整性校验及coverage默认审计；需要生成时先冻结C/R/K再 `make demo`。全库publication的既有2errors/64blocks单独报告，不冒称清零。
5. 精确最终HEAD/base独立 evaluator 三维审核及真实CI通过才正常merge；任何后续变化重审。父PR最终门控另行完成。

## Agentic decisions and independent evaluation

planner `fabric_canonical_planner` 已给出有限启动草案；独立非作者 `canonical21_content_evaluator` 已只读确认四文件接缝的必要性，并指出更小的只读 replay 路线。主线已采纳：排除T=not_applicable及strict-complete放宽；明确当前T是unknown，不能误称既有partial；区分声明已留文件缺失与明确未留媒体；包装完成后重放零写。下一步必须验证null/空/错误类型声明和碰撞失败、不落入metadata-only恢复、normal materialize_one路径成功及失败全胶囊零写；普通文件/无symlink及root tier过滤前独立权利检查也属于实现条件。这些是预核意见，**不是最终代码或三维验收PASS**。最终报告将记录真实取得／未取得、选择与纠偏、独立审核者、精确SHA、三维结论及CI，不预填PASS。

## Explicit non-results

尚未取得本批原件、未新增素材、未实现接缝、未运行本批测试、未完成预处理、未关闭来源unresolved。没有进入main、没有P4/P5放行、没有trusted晋升、没有文件／分支删除、迁库、历史改写或保护变更。用户的ALCE／NC／宽泛目标决定仍未回答，不从本批授权外推。

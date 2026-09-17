---
phase: P3-STANDARD-SPEC-02
status: startup_contract_not_acquired
execution_contract:
  plan_id: nonrepo-materialization-main-convergence-260916
  phase: P3-STANDARD-SPEC-02
  base_branch: work/v0-meta-kb-initialization-demo-260910
  base_sha: 4b179e3c0a932f41db493c95f5e8974dfdb599ae
  target_branch: work/v0-meta-kb-initialization-demo-260910
  source_uids: ['standard:apache-ossie', 'standard:etsi-ngsi-ld']
  allowed_paths:
    - docs/plans/260916-corpus-completion-main-convergence/p3-standard-spec-02.md
    - docs/plans/260916-corpus-completion-main-convergence/branch-ledger.yaml
    - raw_data/standard/Apache Ossie Open Semantic Interchange/metadata.yaml
    - raw_data/standard/ETSI NGSI-LD/metadata.yaml
    - materialized_sources/corpus/standard-apache-ossie--ae9e548a/**
    - materialized_sources/corpus/standard-etsi-ngsi-ld--a1add4e6/**
    - raw_data/licenses/p3-standard-spec-02-apache-ossie.md
    - raw_data/audits/materialization_rights_review.yaml
    - raw_data/audits/non_repo_materialization_coverage_2026-09-16.yaml
  generated_paths:
    - materialized_sources/index.yaml
    - source_registry/registry.yaml
    - source_registry/registry.jsonl
    - raw_data/audits/materialization_completeness_2026-09-10.yaml
    - experiments/v0_meta_kb_initialization_demo_260910/00_inputs/**
    - experiments/v0_meta_kb_initialization_demo_260910/02_entities/**
    - experiments/v0_meta_kb_initialization_demo_260910/03_evidence/**
    - experiments/v0_meta_kb_initialization_demo_260910/04_claims/**
    - experiments/v0_meta_kb_initialization_demo_260910/05_wiki/**
    - experiments/v0_meta_kb_initialization_demo_260910/06_evaluation/**
    - experiments/v0_meta_kb_initialization_demo_260910/07_review/**
    - experiments/v0_meta_kb_initialization_demo_260910/08_release/**
  explicitly_out_of_scope:
    - all_other_213_UIDs_and_84_repository_body_acquisition
    - source_deletion_storage_migration_history_rewrite_force_push_or_branch_deletion
    - workflow_schema_adapter_framework_dependency_or_production_code_changes_without_new_amendment
    - full_site_all_ETSI_editions_repository_tools_external_datasets_or_recursive_references
    - source_script_execution_OCR_trusted_promotion_or_complete_predicate_relaxation
    - P4_P5_main_merge_issue_closure_or_protection_changes
---

# P3-STANDARD-SPEC-02 — 两项规范的有界正文获取

## Executed scope

- 基线（base）：work `4b179e3c0a932f41db493c95f5e8974dfdb599ae`；短期分支 `codex/p3-standard-spec-02-260918`，唯一回流目标仍为work，最终经PR #1进入main。
- Phase：P3-STANDARD-SPEC-02；主要bucket：`standard_spec_fetch`；adapter family：`generic_web_or_document_v2`；仅上方两个UID。
- 前批PR27已正常merge，精确pair独立三维PASS与CI123 success，合并tree与已审HEAD相同。父PR仍Draft，main未变；父PR CI124运行中，不借其未完成状态宣称验收。
- 已完整重读Issue #3/#4、README、02/03/04/05/06执行合同、plan.yaml、完整branch ledger，并核当前仅PR1打开、work工作树clean。本启动提交只写报告与台账，不获取或修改正文。

## 用户目标、候选路径与工作假设

目标是把collection既定规范正文及必要预处理保存在repo，远端可继续消费；不是优化capsule计数。215＝131非repo＋84repo分母不变。

考虑三条路径：继续抓取原Home/目录；扩大到整个repo或所有edition；复用已保留官方指向，固定一个有限正文版本。选择第三条：前两条分别不能补正文或不必要扩大scope。

Apache现有repo胶囊已固定commit `831f48e582731cf1ee2e65380ca5abf8157869c7`，README指向`core-spec/spec.md`；docs/index L50区分current0.2.0.dev0与released0.1.1，L64明确full specification，L377明确包括specification/docs的Apache-2.0。现本地只留README/CONTRIBUTING/index，不含spec。采用该固定snapshot，不冒充正式release或最新版，实读spec后确定其自述版次。

独立预核明确：旧R的official_website_license/license_scope针对`apache/ossie-website`，不能拿来授权`apache/ossie`规范。新作品依据是已存`materialized_sources/corpus/github-apache-ossie--94db39b4/evidence/files/docs/index.md`的ASF头及L377、对应固定commit，加上本批将实读的spec/同commit LICENSE/NOTICE。后续新增准确作品证据，旧网站R完整历史保留，不把两者混用。

ETSI旧document L3实际列出`01.09.01_60`目录；本批工作假设选择该既有1.9.1 edition候选核实，不声称它是最新或由目录日期证明官方批准状态。只有实际PDF身份对应后才固定选版；不抓其余10个目录。

## Before / After（启动快照）

| UID | Identity/version before | 原件A／文本T before | Local／selectors before | P／知识 before | After |
| --- | --- | --- | --- | --- | --- |
| `standard:apache-ossie` | canonical ossie.apache.org；版本未固定 | metadata_only／unavailable | 4文件2239B；document仅7B Home；0selector | root block；无demo claim | 未执行；预期先取得同commit真实spec及履约文件 |
| `standard:etsi-ngsi-ld` | GS CIM 009家族；selected_version=null | metadata_only／unavailable | 4文件3024B；558字符版本目录；2目录selector | unknown；无demo claim | 未执行；先核一个edition正文与实际条件 |

两UID启动时resolution均unresolved。旧R只有Apache一行，ETSI没有专属R行，不能把unknown写成权利人拒绝；现没有API PDF原件，不代表上游不可取得。

## 有限网络合同（获取前公开）

启动PR公开后，仅以下四个请求先进入临时目录；每项记录真实UTC、requested/resolved URL、状态、类型、编码、bytes及错误，不关闭TLS校验、不绕访问控制、不虚构响应。

1. Apache规范：https://raw.githubusercontent.com/apache/ossie/831f48e582731cf1ee2e65380ca5abf8157869c7/core-spec/spec.md
2. 同commit完整LICENSE：https://raw.githubusercontent.com/apache/ossie/831f48e582731cf1ee2e65380ca5abf8157869c7/LICENSE
3. 同commit NOTICE：https://raw.githubusercontent.com/apache/ossie/831f48e582731cf1ee2e65380ca5abf8157869c7/NOTICE
4. ETSI单一edition目录：https://www.etsi.org/deliver/etsi_gs/CIM/001_099/009/01.09.01_60/

ETSI只从该真实目录提取一条正式PDF链接，先公开准确URL修订再临时获取；不猜PDF文件名、不遍历全版本。临时核读PDF首中末、页数、版权/STATUS/复制条件；只有实际作品对应grant闭合才追加精确公开包装与有限消费合同，否则记录permission unresolved，不借用户同意创造许可。

Apache仅实读spec与完整LICENSE/NOTICE，核首中末、表/代码/正文结构、实际必要媒体或include。必要额外文件须真实引用并先列准确同commitURL与范围修订；不抓普通参考链接、JSON schema、validator、converter、TPC-DS、全repo。新全文准入必须实际履约后另记实施修订，不能先上传未知原件再补审计。

## 实施边界（尚未实施）

默认生产代码改动为零。Apache优先复用既有ordered `git_snapshot` retained-text与正常离线replay：原件MD和同commitLICENSE/NOTICE保留，新normalized/document.md与normalized/selectors.jsonl为派生层；旧Home document.md、空selectors.jsonl、旧retrieval/metadata/rights历史完整保留，不删除或回写旧表达授权。四方package按实际新表示绑定，不只改gate凑通过。

ETSI现有PDF抽取能力不等于已支持standard的保留式PDF接缝；generic fresh fetch会prepare旧root，本批不准直接重跑覆盖。无grant时只记录实证；若有grant而确需最小接缝，先修订准确生产/测试路径与失败保全条件，禁止伪装journal或创建万能fetcher。

R/K只改两UID及实际summary/execution，保留完整原对象历史；其余129K/其他R不变。两UID当前不在selected set，不新增claim/trusted。R/K与index若导致既有build identity必然传播，先冻结输入再串行运行既有生成器，核36选源/72claim/evidence语义不变；上方generated_paths不是任意手改授权。

## Verification（待实际结果）

实施后逐UID核首中末、版本/许可/依赖；新增selectors首中末语义解析，原件与临时响应逐byte核对、旧文件和历史保全、正常调用离线重放与新导出目录消费。根据实际变更运行既有定向测试及 `make test`、`make validate`、`make reproducibility`、完整性与coverage默认审计；输入先冻结，生成与验证串行，不读取重建中的过渡树。

全库既有publication两错误及64root blocks单独报告，不冒称本批清零。精确最终HEAD/base独立evaluator按需求、Agentic过程、核心质量三维审核，当前CI通过后才正常merge。任何实质失败退回planner→executor→evaluator，不预填PASS。

## Agentic decisions and independent evaluation

planner已只读核出现有双sidecar可复用和ETSI接缝条件，主线选择S2先补明确规范目标；独立非作者预核指出旧website grant与新spec作品证据必须分开，主线已将该条件写入本合同。实际取得、计划修订、失败纠偏与最终精确pair结论在执行后记录；预核不代替终审。

## Explicit non-results

尚未网络获取、公开准入、实现、生成或测试；没有宣称两规范已完成，没有进入main或P4/P5，没有删除/迁移/历史改写/删分支/保护变更。ALCE、NC用途、RARR及广泛目标边界的未答决定不从此批外推。

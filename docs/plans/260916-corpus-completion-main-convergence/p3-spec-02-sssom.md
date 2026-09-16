---
phase: P3-SPEC-02
base_sha: ca5d6e1272a868668ce6925cdfdf366b3d6eadcf
coverage_summary:
  collection_records: 215
  non_repo_total: 131
  github_repo_excluded: 84
  reported_content_tier_counts: {excerpt_capsule: 27, full_text: 92, metadata_capsule: 12}
  source_type_counts: {arxiv: 73, biorxiv: 2, blog: 10, industry: 2, journal: 11, methodology: 7, paper: 2, standard: 24}
  original_artifact_counts: {complete: 7, metadata_only: 16, partial: 7, unknown: 101}
  text_extraction_counts: {complete: 2, partial: 28, unavailable: 16, unknown: 85}
  action_bucket_counts: {access_restricted: 7, author_manuscript_fetch: 2, canonical_repair: 6, complete_verified: 2, html_article_snapshot: 14, identity_or_version_ambiguous: 2, needs_boundary_verification: 86, ocr_assessment: 4, open_fulltext_fetch: 6, standard_spec_fetch: 2}
  public_redistribution_counts: {allow: 28, block: 65, unknown: 38}
  content_inspected_full_text: 33
  structure_only_full_text: 59
  locally_persisted_complete: 2
  knowledge_candidate_sources: 30
  knowledge_trusted_sources: 0
  knowledge_sources_without_demo_claims: 101
  unresolved_sources: 129
---

# P3-SPEC-02 — SSSOM 1.0 有界规范正文

本批为 PR #11，唯一 UID `standard:sssom`、generic family、`canonical_repair` 桶。PR #10 已在最终 fc3d290／BASE d066fd6 的独立三维 PASS（review 5225063032）和 CI 35117631690 success 后正常合入 work `ca5d6e1272a868668ce6925cdfdf366b3d6eadcf`；父 PR #1 仍 Draft 对 main。

## 规划与判断（planner and decisions）

旧 canonical 仅取得362-byte Redirecting响应，本地只有README与metadata，`1.x family`不是固定版本。比较只修URL、整站镜像、固定正式规范三路线，选择最后一种。DPV虽同属入口修复，但需要HTML规范处理；本批只做SSSOM，不为了多UID引入新框架。

依据官方 [release v1.0.0](https://github.com/mapping-commons/sssom/releases/tag/v1.0.0)，固定提交 `658de421c21a686f1213ff41879c9245ac0b4925`、正式规范1.0（2024-08-09发布）。旧无版本 `w3id.org/sssom/spec` 的HEAD解析到无版本spec-intro后404；版本化1.0入口及所需页面可达。HEAD证据不冒称正文GET；版本身份不从兼容性章节或pyproject动态占位版本推断。

启动合同先于正文获取。第一批六件原生MD实际HTTP200后，内容审查发现不能只拼这六页便称完整：spec-model L3–5明确schema才是模型权威，mkdocs Specification/Data model又列出chaining-rules；TSV L230及L249–250要求canonical顺序按两个Slots表。于是有界补取同tag schema/chaining及两个官方1.0渲染类页，未扩展教程、工具、字段页、数据集或外部标准。

## 获取记录（retrieval）

所有规范原稿均来自 `https://raw.githubusercontent.com/mapping-commons/sssom/658de421c21a686f1213ff41879c9245ac0b4925/`，不是master/latest：

| 上游相对路径 | Bytes | 实际响应与完成时间（UTC） |
| --- | ---: | --- |
| src/docs/spec-intro.md | 1456 | 200 text/plain; charset=utf-8，2026-09-16T15:58:15Z完成 |
| src/docs/spec-model.md | 15584 | 同批200、同完成观察时间 |
| src/docs/spec-formats.md | 369 | 同批200、同完成观察时间 |
| src/docs/spec-formats-tsv.md | 21612 | 同批200、同完成观察时间 |
| src/docs/spec-formats-owl.md | 3782 | 同批200、同完成观察时间 |
| src/docs/spec-formats-json.md | 334 | 同批200、同完成观察时间 |
| src/docs/chaining-rules.md | 4253 | 200 text/plain; charset=utf-8，15:59:42Z开始、15:59:44Z完成 |
| src/sssom_schema/schema/sssom_schema.yaml | 32836 | 同批200、同开始/完成观察时间 |

首批未记录各请求精确开始时间，不补造；此前15:57:55Z只是准备时刻。八件正文原稿共80,226 bytes。另保存同tag LICENSE及mkdocs.yml作为授权／目录依据，不把它们计入正文。

两份有界补证：[Mapping](https://mapping-commons.github.io/sssom/1.0/Mapping/) 63,208 bytes、[MappingSet](https://mapping-commons.github.io/sssom/1.0/MappingSet/) 44,896 bytes，16:02:25Z开始、16:02:27Z完成，均200 text/html; charset=utf-8，canonical为对应1.0地址。它们是访问时的版本化发布快照，不能伪称其HTML bytes来自固定Git tag；对照事实是其Slots表内容/顺序与固定schema完全一致。不抓JS/CSS、banner或全部生成字段页。

## 内容实质与边界

七MD加schema逐件完整审读。开中尾包括：intro L3–10 normative身份、L22–31八prefix表；model L3–5权威schema、L95–107 literal例外、L182–192 extension类型约束；TSV L10–24两块结构、L157–206旧版兼容表、L303–328明标非法示例；OWL L3–11三类规则、L49–62 existential示例、L90–99最后表及示例；chaining L3–9目标、L67–77 role chains、L103–111 generalisation。短JSON页L3明确unspecified，5行原稿完整而非截断。

六份核心MD的6张表、19个完整fenced code blocks和TSV示例80个真实TAB原样保留。七MD没有实际图片、iframe、snippet/include；插件配置不是缺资产证据。示例中的external数据、SEMAPV／ontology／工具链接是引用，不默认作为页面加载资产。

原schema为792行，68个全局slots、8 classes、1个EntityReference类型、3 enum（11/1/6值）。类slots引用无悬空或重复；14个propagated注解与模型正文名单一致。MappingSet的license必填、Mapping四条literal条件、mapping_justification的允许值/regex、完整enum和末尾NoTermFound均保存，不只摘字段名。

**顺序证据**：Mapping HTML L554–829的44行Slots表逐位置等于schema L650–694；MappingSet HTML L523–714的30行逐位置等于schema L617–647。没有缺项、多项、重复或顺序差异。canonical TSV使用类列表顺序，不能误用顶层slots定义顺序或字母排序；metadata中仍按TSV排除mappings项。此检查不是运行或验证一个canonical writer。

原作缺陷独立记录，不静默修复：model用`extension_definition`、TSV/schema用`extension_definitions`；OWL表写`EauivalentClass`；chaining的`owl:equivalentTo`／`owl:subClassOf`与核心模型不同且自身说明只是工具默认语义。JSON未规定的细节不由采集者补写。原稿的四类生成文档链接以本地schema为权威内容替代，不冒称所有生成页已留存；唯一import `linkml:types`是运行时标准依赖，离线正文消费不等于离线编译完整LinkML环境。

## 六维状态与公开包装

| 维度 | before → after |
| --- | --- |
| 身份／版本 | 旧入口、1.x family → 官方1.0、v1.0.0固定tag及版本化规范入口 |
| 原件 | metadata_only → 八件官方正文原稿、二件版本化Slots补证完整保存，complete |
| 文本 | unavailable → 原生七MD和YAML完整保留，单一有出处的组合消费者完整覆盖八原稿，complete |
| 持久化／定位 | 仅README/metadata → 原件、派生、67个定位、manifest／registry／NOTICE进入Git候选树，隔离索引导出离线重放通过 |
| 公开表示 | unknown → 同tag LICENSE及README Copying明确BSD-3-Clause；完整条件随包，banner例外排除 |
| 知识 | 无demo claim → 不新增selected、claim或trusted |

许可只核本批真实规范表示，不延伸为组件考古。schema及TSV示例中的license是模型字段/示例值，不是整个规范的授权。固定README完整Copying与LICENSE足以界定本次正文；版权为Nico Matentzoglu，贡献者归属于SSSOM/Mapping Commons，不把论文作者名单当规范作者。完整BSD三条款随NOTICE，公开包明确固定原稿与版本化补证的区别。

## 验证与独立门控

使用与CI一致的Python 3.12.13／pypdf 6.18.1实际运行 `make demo && make test && make validate && make reproducibility`：110项测试通过；215 manifests、2,889个inventory校验文件、22,136 selectors无错误／警告；47篇文档、80个相对链接通过。构建为 `build:llm-wiki-v0:f3fea76ebc259510`；committed-tree、full-demo、compiler-only、read-only-validation四阶段的169个生成文件逐字节一致。

胶囊共18文件、340,234 bytes；inventory计17件非manifest文件，`local_bytes=322,611`。组合消费者为1,803行／85,254字符，67 selectors由66个MD章节和1个原生YAML全文定位组成。七份MD加schema共8个正文原件，并不是8份派生正文。逐源范围连续覆盖首行到末行；逐段对照原稿，只在非代码的明确href上改写为本地目标，代码／TAB／schema内容逐字保全。最后schema的源1–792行对应消费者999–1790行，之后才闭合围栏并附NOTICE；所有67 preview均真实位于对应范围。

12件source文件与实际获取的临时原件逐字节一致。两次禁网且禁止清空目录的通用入口重放保持18文件不变；另在隔离Git候选索引导出 `/tmp/llm-wiki-pr11-index.VN6d0k` 上重复同样两次重放并确认18文件全部字节一致，原生MD／schema／两个HTML均离线可读。这个检查不是remote clone或main fresh checkout，P5仍待执行。

相对BASE，index及两种registry的其他214 UID对象、原92条rights审阅对象、36 selected／72 claims／72 evidence文件均保持不变。既有全index／rights输入依赖只传播必要全库计数与构建标识；本批未新增selected或更改知识内容。覆盖台账由内容核验与当前文件事实对账，只改变SSSOM判断；默认coverage auditor实际PASS，与本报告frontmatter一致：131非repo中固定目标完整本地消费已证明2项、仍有待办129项，trusted仍0。未知不等于不存在，不把92个full_text标签当完成数。

完整 `git diff --check` 实际退出2，共79处空白诊断，限于原chaining、原TSV、原schema、两个原HTML和忠实派生document六文件。它们是保留的上游行尾空格／TAB／末空行，不改原件或非法示例以取得格式绿灯；其余实现、元数据、许可、文档和生成物的scoped检查通过。不能声称完整空白检查PASS。

全库publication检查仍为active92／audited93、64个继承活跃block、GraphRAG与CoScientist两项继承包不一致错误，SSSOM自身无block/error。新审阅只增加sequence93，未重写历史92对象；同一许可包在canonical／capsule／manifest／audit四方绑定实际固定版本和保存范围。

独立evaluator `/root/pr11_independent_evaluator` 未参与实现，已只读预审边界、许可及Slots排序；预审不是最终PASS。最终三维PASS及精确CI成功后才正常合回work。必要demo变更只能由全index/rights输入依赖传播构建标识，禁止手改pipeline或知识内容。

## 明确未完成（explicit non-results）

未合入main；其他130条不在本批变更；父PR1仍Draft，Issues3/4不关闭，分支不删除、不强推、不改保护、不晋升trusted。P4仍须修复GraphRAG/CoScientist两项继承rights包不一致及coverage工作历史依赖；本批不能声称全库publication gate通过。P5还需main新检出验收。

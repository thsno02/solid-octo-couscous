---
phase: P3-TEX-01
base_sha: 03c2fdcd5b94e684aa54d582f7f966188575cf7d
coverage_summary: {"collection_records":215,"non_repo_total":131,"github_repo_excluded":84,"reported_content_tier_counts":{"excerpt_capsule":27,"full_text":90,"metadata_capsule":14},"source_type_counts":{"arxiv":73,"biorxiv":2,"blog":10,"industry":2,"journal":11,"methodology":7,"paper":2,"standard":24},"original_artifact_counts":{"complete":1,"metadata_only":18,"partial":7,"unknown":105},"text_extraction_counts":{"partial":24,"unavailable":18,"unknown":89},"action_bucket_counts":{"access_restricted":7,"author_manuscript_fetch":2,"canonical_repair":8,"html_article_snapshot":14,"identity_or_version_ambiguous":2,"needs_boundary_verification":90,"open_fulltext_fetch":6,"standard_spec_fetch":2},"public_redistribution_counts":{"allow":26,"block":65,"unknown":40},"content_inspected_full_text":27,"structure_only_full_text":63,"locally_persisted_complete":0,"knowledge_candidate_sources":30,"knowledge_trusted_sources":0,"knowledge_sources_without_demo_claims":101,"unresolved_sources":131}
---

# P3-TEX-01 — GraphRAG 已保留正文的 import 展开

本批为 PR #8，唯一目标 `arxiv:2404.16130`，固定 v2；基于 PR #7 经独立三维 PASS 和 CI 通过后合入的 work `03c2fdcd5b94e684aa54d582f7f966188575cf7d`。一个 arXiv adapter family／一个解析行动桶（parser_only）／一个 UID。P2 报告保留历史，当前覆盖台账会由本报告承接。

## 判断依据与工作边界

规划者实际阅读发现 `source/graph_rag.tex` L181、311、397、399、429、430、455、465 及 `source/appendix.tex` L32、37、51、58、65、72 共 14 个二参 `import`。目标文件全部在 repo，但旧解析器只展开 input/include；normalized 文本末尾只是 `acks.tex`／`appendix.tex` 文件名字面。实际缺失是已有结果表、研究提示词和附录正文进入主要消费层的路径，不是要另取 Wikipedia、新闻/访谈数据集或引用论文全文。

候选路径（options）：沿现存 TeX 做最小 import 修复；或获取同一版本官方 PDF。这里 14 个目标已经保存且边界简单，选择前者，来源网络请求为 0。对于另一些含复杂宏、verbatim、minted 和整篇嵌入 PDF 的论文，后续可以选择同版 PDF 补充表示，不把本 PR 扩写成通用 TeX 引擎，也不把它们纳入本批。

实现语义另查阅 [CTAN import 6.2 官方文档](https://ctan.net/macros/latex/contrib/import/import.pdf)：import 使用主工作目录基准，subimport 扩展当前 import 上下文，实际 LaTeX 还允许逐层搜索路径。此次查询是解析器参考文档，不是目标 corpus 的新增获取。支持范围内须正确定位；不支持的宏／条件／系统路径须明确诊断，不允许为通过解析而读取宿主文件或静默绑定错误同名文件。

原 19 份 source（160,932 bytes）、files.jsonl、retrieval 和 revision 均保留；61 条 source 定位器保留，派生定位追加。只允许更新这一个材料的 normalized／manifest 与精确转换说明，再单 writer 更新完整 215 条聚合及必要生成物。

## Before / After

| 维度 | Before | After |
| --- | --- | --- |
| 身份／版本 | GraphRAG，arXiv:2404.16130v2 | 同版同源，不用 latest 替换 |
| 原件覆盖 | P1 unknown／未作正文核验 | partial：两个实际引用的社区图 JPEG 未保留，不能宣称完整 |
| 文本提取 | P1 unknown；full_text 标签下 import 未展开 | partial：14 条真实导入已展开，仍有书目／图像／有损表达限制 |
| 本地消费 | 19 source、旧 normalized、61 source 定位 | 新派生正文及定位，原 source 保持 |
| 公共持久化 | 继承已有 allow，固定原件 revision | 不改判；包说明只同步派生转换和真实范围 |
| 知识准入 | 未进入 selected demo，无 GraphRAG claim | 不新增该来源 claim，不晋升 trusted |

实现已经冻结：normalized TeX 为 102,241 bytes／1,687 行；normalized text 为 86,085 bytes／1,494 行，其中正文前缀 81,087 bytes／81,068 characters，唯一归属附注 4,998 bytes。同步 metadata 镜像后 capsule 为 424,337 bytes，manifest 的 stored_characters=84,236。定位从 61 条 source 定位增加到 103 条（追加 42 条 derived），原 15,456-byte source 定位前缀逐字节保留。状态由旧 materialized 诚实改为 partial，content tier 的 full_text 标签不代表 complete。

上述正文／附注边界按既有 redistribution_footer 函数计算，归属附注包含 marker 前的两个分隔换行；直接只用 marker 拆分会得到正文多 2 bytes／附注少 2 bytes，不是内容差异。

七节附录实际进入正文：Entity and Relationship Extraction Approach、Example Community Detection、Context Window Selection、Example Answer Comparison、System Prompts、Evaluation Prompts、Statistical Analysis；结果表和致谢也已展开。最终判断依靠实际文字/表格/prompt 抽查，不是只数 include edges。

支持边界：字面花括号 import/subimport；import 相对 root 编译目录，subimport 相对当前 import 上下文，嵌套 import 重置基准。在 import 内的 input/include 只解析可证明的当前目录目标；不跳过祖先目录去选择 root 的同名文件，找不到则保留明确 missing 诊断。不执行宏、条件或 comment 环境，不读取主机路径；不支持的星号／动态／非花括号调用记为 unsupported。另将 TeX 环境标记清理放到通用命令剥离之前，避免新表格定位的 preview 只是环境噪音；不是新增完整 TeX 解释器，也没有重派生其他 UID。

## 已知剩余范围

- `source/communities_figure.tex` L4–5 引用 `Level0Multihop.jpg`、`Level1Multihop.jpg`；这是正文附录的社区结构图，不是可以忽略的模板。图注与层级标签已经在 source，图像原件本批不获取。
- `source/graph_rag.tex` L459–460 使用 bibliography；`graph_rag.bbl` 已保存，但当前 normalized 不展开编译书目。不递归获取被引作品，也不把所有备份书目直接拼入正文。
- 纯文本层对 TeX 表格、数学、TikZ 和 prompt 结构有损；完整 source 与 expanded TeX 仍是核查依据。不以字符数或 selector 数充当核心质量。

## 生成物影响

GraphRAG 不在当前 36-source selected set，但 `build_demo.py` 将整个 `materialized_sources/index.yaml` 纳入 build identity。因此目标 capsule 的 bytes／status 改变后需要完整重放 demo/Wiki 以传播正确构建身份。验收边界是旧 claims/evidence 内容保持、无新增 GraphRAG claim，而不是提交过期 release 来减少 diff。生成器、workflow 与权限设置不改。

实际重建仍为 36 sources／72 claims／72 evidence／135 pages，Wiki build=`build:llm-wiki-v0:3de65e2db5aac4d8`。claims.jsonl、evidence.jsonl、selected_sources.yaml 均与本批 base 逐字节相等；index 只有 GraphRAG 一个条目变化，其他 130 条非 repo 与 84 个 repo 胶囊无改动。

Registry 的 evidence_role 随既有规则从 source-text 变为 bounded-excerpt，因为该规则把 partial 粗粒度映射为此值；本批实际增加了正文，并未做截断或删减以创建 excerpt。真实覆盖以两个 coverage 轴和具体限制为准，不借这一派生标签掩盖文本范围，也不为此扩改全库规则。

## 独立评价与验证

Planner 提供明确缺口与候选路径；executor 独占代码、测试和目标 capsule；主线程在其冻结后接手 metadata、聚合、coverage 和 release。未参与作者工作的独立 evaluator 先确认 before 问题，再对冻结 head/base 评估需求、agentic 判断链和核心质量。任何 FAIL 都返回修复；独立 PASS 和当前 CI success 之前不合并。

已实际执行的本地验证（Python 3.12.13，`PYTHON=/tmp/llm-wiki-ci-312-260916/bin/python`）：

- `make test`：71 项 PASS，其中 materialization 46 项；包括相对 import/subimport、嵌套基准重置、同名错误回退拒绝、注释和不支持语法、缺失／越界／循环／深度、重复合法引用。
- `make demo`、`make validate`：PASS；215 manifests、2,849 个校验文件、21,541 selectors、44 篇 docs，0 warnings／errors；其中包含独立物化完整性命令。
- `make reproducibility`：169 个生成文件的提交树、完整 demo、仅 compiler 和只读验证重放均逐字节一致。
- 19 份 source、files.jsonl、旧 61 条 selectors 前缀直接字节对比一致；14 边、七节附录、结果表和 prompt 内容核验；同步 metadata 镜像之后两次 finalize 整 capsule 字节幂等。
- 全量 `git diff --check` 退出 2，只涉及两份 normalized 文件从源 TeX 带入的行尾空白；不冒充全量 PASS。为保留来源表达而不做 cosmetic trim，排除这两份具体派生文件后的其他差异检查 PASS；CI、内容与定位校验没有关闭。
- 默认 Coverage auditor 已对实际台账与本报告联合验证 PASS（131 条当前结构观测与汇总一致，非内存替身）；文档验证 44 篇／80 相对链接／0 errors。最终 head、CI run 与三维独立结论记录于 PR #8 review/body，未放行前保持 Draft。

本批不表示全 corpus 完成，不进入 main，不关闭 Issues #3/#4，不删除分支或改历史。P4 仍须解决历史审计器在 squash 后的校验合同，P5 仍须真实 main fresh checkout 复验。

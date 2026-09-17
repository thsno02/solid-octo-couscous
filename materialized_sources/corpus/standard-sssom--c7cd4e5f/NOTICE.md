# SSSOM 1.0 固定规范的署名与许可（attribution and license）

本包装仅覆盖 Mapping Commons 官方 SSSOM 1.0／release `v1.0.0`、固定提交 `658de421c21a686f1213ff41879c9245ac0b4925` 的七份规范 Markdown 与权威模型 YAML，以及为核对 canonical TSV 字段排序保留的两份官方 1.0 生成类文档快照。它不是 SSSOM 工具、整个站点或映射数据集的镜像。

## 原作与授权范围

- 著作权：Copyright (c) 2022, Nico Matentzoglu；SSSOM／Mapping Commons contributors。不将关联论文作者名单冒充本版规范的逐文件作者。
- [固定版本 LICENSE](https://github.com/mapping-commons/sssom/blob/658de421c21a686f1213ff41879c9245ac0b4925/LICENSE) 为 BSD-3-Clause；完整原文见下。
- [同版 README 的 Copying](https://github.com/mapping-commons/sssom/blob/658de421c21a686f1213ff41879c9245ac0b4925/README.md#copying) 明示适用范围；唯一列明的 `sssom-banner.png` 例外不在本包装内，也未下载。
- 规范中的示例映射记录含自己的 `license` 值；它是示例数据字段，不被改写成规范整体的许可声明。保留原示例及署名，不抓其外部数据。
- [正式发布记录](https://github.com/mapping-commons/sssom/releases/tag/v1.0.0) 与 [1.0规范入口](https://mapping-commons.github.io/sssom/1.0/spec-intro/) 作为版本/身份依据，旧无版本入口错误另记历史，不冒称版本漂移。

## 文件和派生说明

固定提交原稿：`src/docs/spec-intro.md`、`spec-model.md`、`spec-formats.md`、`spec-formats-tsv.md`、`spec-formats-owl.md`、`spec-formats-json.md`、`chaining-rules.md` 与 `src/sssom_schema/schema/sssom_schema.yaml`。七份 Markdown 和 YAML 原件字节不变；所有表格、制表符、代码、非法示例和上游拼写／命名差异原样保留。

消费者是采集者的确定性组装（collector assembly），不是上游单篇 Markdown：明确来源分界，schema 仍另存原生 YAML，合并视图中用标明 YAML 的代码块表达。只对派生层做本地链接定位与归属说明；不修改规范语义，不补写上游未定义的 JSON serialisation，不把 chaining 的工具规则升级为规范性要求，不执行 LinkML import 或外链代码。

两份官方版本化类文档快照为 [Mapping](https://mapping-commons.github.io/sssom/1.0/Mapping/) 与 [MappingSet](https://mapping-commons.github.io/sssom/1.0/MappingSet/)，仅为对应原生 schema 和 TSV 所引用 Slots 表的有界核验；不是声称已保留全部生成字段页面或网页运行时。正文中的外部标准、工具和数据链接均作为引用，不继续抓取。

本项目不暗示原作者背书。公开包装与正文消费不代表知识晋升为 trusted。

## BSD 3-Clause License — 完整原文

BSD 3-Clause License

Copyright (c) 2022, Nico Matentzoglu
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

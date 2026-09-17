# 图像页派生转录（image-page derived transcription）

- 来源：*Accelerating scientific discovery with Co-Scientist*，arXiv:2502.18864v2，原件 [document.pdf](../source/document.pdf)。
- 本次范围：物理页 4 的图中文字；物理页 20 的八幅散点图标题、横纵轴名称。物理页不是图号。
- 方法（method）：`agent_visual_transcription`；Codex `view_image` 图像理解后人工式逐项转录。服务端模型的确切版本未暴露，不推定其版本。不是 PDF 原生文本，也没有运行传统 OCR 引擎。
- 渲染（rendering）：Poppler `pdftoppm` 26.05.0；页 4 为 240 dpi 分块，页 20 为 180 dpi。渲染仅供检查，原 PDF 不改动，既有 `document.txt` 不替换。
- 转换（modifications）：把图中可读文字按面板分组；消除换行断词、重复图标标签，保留原文措辞。中文标题、列表和本说明属于整理结构，不是论文正文。
- 限制（limitations）：未把布局、箭头、颜色、图形、坐标刻度或散点位置重建成数据。不得用本转录计算实验值，也不得宣称完整无损图像转文本。物理页 5、21 的原生图注仍见既有 `document.txt`。以原 PDF 为最终依据。
- 归属（attribution）：Juraj Gottweis 等作者；完整作者归属见 [source-metadata.yaml](../source-metadata.yaml) 的 `rights.redistribution_package.attribution`。固定版本来源：https://arxiv.org/abs/2502.18864v2 。本派生转录沿用原作品 CC BY 4.0，许可及免责声明见 [NOTICE.md](../NOTICE.md)；不扩展到外链作品或原作者无权许可的第三方材料。

## 物理页 4：面板 (a) — Co-Scientist system design

### 科学家与研究目标

- Scientist
- The scientist interacts with the system by specifying a research goal in natural language. They can also suggest their own ideas and proposals, provide feedback and reviews, and interact via a chat interface to guide Co-Scientist.
- Discuss via chat interface
- Scientist inputs
- Research goal
- Scientist describes a research goal along with preferences, experiment constraints, and other attributes.
- Add idea
- Review idea
- Discuss research
- Research proposals and overview
- Top-ranked research hypotheses and proposals are summarized into a research overview and shared with the scientist.

### 系统内部文字

- Co-Scientist multi-agent system
- Research plan configuration
- Ranking Agent tournaments
- Research hypotheses comparison and ranking with scientific debate in tournaments. Limitations and top win-loss patterns are summarized and provided as feedback to other agents. This enables iterative improvement in quality of research hypothesis generation creating a self-improving loop.
- Generation Agent
- Literature exploration
- Simulated scientific debate
- Reflection Agent
- Full review with web search
- Simulation review
- Tournament review
- Deep verification
- Evolution Agent
- Inspiration from other ideas
- Simplification
- Research extension
- Proximity Check Agent
- Meta-review Agent
- Research overview formulation
- AI
- Co-Scientist
- Co-Scientist continuously generates, reviews, debates, and improves research hypotheses and proposals toward the research goal provided by the scientist.
- Tool Use
- Search
- Additional tools
- Memory
- Co-Scientist system design

## 物理页 4：面板 (b) — Co-Scientist multi-agent architecture

- Scientist
- Research goal
- Configuration
- Supervisor agent
- Research overview with detailed hypotheses
- Assign agents to workers
- Additional feedback
- Generation agent
- Proximity agent
- Reflection agent
- Meta-review agent
- Ranking agent
- Evolution agent
- Worker（图中四个框重复同一标签）
- Context Memory
- AI
- Co-Scientist
- Co-Scientist specialized agents
- Co-Scientist multi-agent architecture

## 物理页 4：面板 (c) — Application / Basic Research

### Drug repurposing for acute myeloid leukemia (AML)

- Application
- Suggest an existing drug that could be repurposed for acute myeloid leukemia (AML) treatment and provide experimentally testable concentrations for an IC50 assay. The drug should inhibit the proliferation of AML cell lines, particularly MOLM13.
- Scientist provides research goal to identify possible drug repurposing candidates for acute myeloid leukemia (AML).
- With preclinical evidence
- Binimetinib, Pacritinib, ...
- Completely novel repurposing
- KIRA6, Leflunomide, ...
- Co-Scientist generates predictions for AML drug repurposing. Scientists review and select candidates for in vitro experiments.
- AML cell activity
- Drug concentration
- Suggested drug
- Suggested novel drug
- IC50
- In vitro experiments show that Co-Scientist proposed drug repurposing candidates inhibit tumor activity in AML cell lines.
- Drug repurposing for acute myeloid leukemia (AML)

### Identifying novel treatment targets for liver fibrosis

- Propose a novel hypothesis about specific epigenetic alterations contributing to myofibroblast formation in liver fibrosis.
- Scientist specify research goal to identify novel epigenetic targets for liver fibrosis.
- Co-Scientist identified 3 epigenetic targets
- Co-Scientist proposes several epigenetic target candidates for in vitro experiments.
- Fibroblast fold change
- Disease progression
- Untreated
- Fibrosis inducer
- Fibrosis inhibitor
- Suggested drug 1
- Suggested drug 2
- FDA-approved
- In vitro experiments show that the drugs based on the proposed epigenetic targets reduce the fibrogenesis in human hepatic organoids.
- Identifying novel treatment targets for liver fibrosis

### Parallel in-silico discovery of bacterial gene transfer mechanism relevant to antimicrobial resistance (AMR)

- Basic Research
- Why are cf-PICIs found in many bacterial species?
- Scientists start exploring the cf-PICI mechanisms in 2015.
- Hypothesis
- Experimental works and results
- New insights submitted to a top journal
- 2015-2024: Scientists create novel hypothesis, and validate experimentally over ~10 years of iterative research
- Independently propose the same hypothesis
- Recapitulate result
- 2024: Co-Scientist generated research hypothesis match the empirical findings in 2 days
- Co-Scientist hypotheses
- Conserved regions on capsids and tails
- Capsid interaction with bacterial membranes
- ...
- Parallel in-silico discovery of bacterial gene transfer mechanism relevant to antimicrobial resistance (AMR)

## 物理页 20：八幅散点图标签

各图横轴为 `Fraction affected (Fa)`，纵轴为 `Combination Index (CI)`。下表仅转录标题；不同图的轴尺度并不一致，不从图点猜测数值或将其视为可复现实验数据。

| 面板 | 左图标题 | 右图标题 |
| --- | --- | --- |
| (a) | JNJ-64619178 + SNDX-5613 (MOLM-13) | JNJ-64619178 + SNDX-5613 (KG-1a) |
| (b) | Palbociclib + Selinexor (MOLM-13) | Palbociclib + Selinexor (KG-1a) |
| (c) | Venetoclax + Pinometastat (MOLM-13) | Venetoclax + Pinometastat (KG-1a) |
| (d) | CB-839 + Sulfasalazine (MOLM-13) | CB-839 + Sulfasalazine (KG-1a) |

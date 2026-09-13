# v0 元知识库初始化 Demo（Meta KB Initialization）— 260910

这个实验是仓库 pipeline 的第一版可执行演示。

它只消费本地物化胶囊（materialized capsules），并生成：

```text
本地来源版本（local source revision）
→ 证据定位器（evidence selector）
→ 候选声明（candidate claim）
→ 本体映射（ontology mapping）
→ 候选 Wiki 页面（candidate wiki page）
→ 确定性评估（deterministic evaluation）
→ 评审队列（review queue）
```

任何科学声明都不会自动晋升为 `trusted`。生成页面属于派生视图（derived view），必须保留指向本地证据和上游来源身份的链接。

## 运行

在仓库根目录执行：

```bash
python experiments/v0_meta_kb_initialization_demo_260910/pipeline/build_demo.py
python experiments/v0_meta_kb_initialization_demo_260910/pipeline/validate_demo.py
```

生成目录按 pipeline 顺序编号。`pipeline/` 和 `config.yaml` 构成可复现实现，其余实验目录均为生成产物。

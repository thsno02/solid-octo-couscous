# Repository semantic capsule: zjunlp/EasyEdit

- Commit: `14cea8245f06715684592ab55184939b99d70784`
- Default branch: `main`
- Description: EasyEdit
- Selected evidence files: 2 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

<div align="center">
<img src="figs/logo.png" width="180px">


![](https://img.shields.io/badge/version-v0.0.1-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![Static Badge](https://img.shields.io/badge/last_commit-May-blue)
![](https://img.shields.io/badge/PRs-Welcome-red)

---
 
<p align="center">
  <a href="#requirements">Installation</a> •
  <a href="#use-easyedit">QuickStart</a> •
    <a href="https://ribbon-muskox-3ac.notion.site/EasyEdit1-0-213e624c1c2680318840d9abbdaa83c5">Doc</a> •
    <a href="https://arxiv.org/abs/2401.01286">Paper</a> •
    <a href="https://huggingface.co/spaces/zjunlp/EasyEdit">Demo</a> •
    <a href="https://huggingface.co/datasets/zjunlp/KnowEdit">Benchmark</a> •
  <a href="#contributors">Contributors</a> •
  <a href="https://github.com/zjunlp/EasyEdit/blob/main/tutorial.pdf">Slides</a> •
    <a href="https://youtu.be/Gm6T0QaaskU", target="_blank">Video</a> •
   <a href="https://twitter.com/_akhaliq/status/1742371655765164133", target="_blank">Featured By AK</a>
</p>
</div>

<h1 style="font-size: 32px; color: #333; text-align: left;">
  <span style="font-size: 30px; color:rgb(180, 148, 61);">⭐</span> Key News
</h1>
<p align="left">
✨ <strong><a href="https://ribbon-muskox-3ac.notion.site/EasyEdit1-0-213e624c1c2680318840d9abbdaa83c5" style="text-decoration: none; "> EasyEdit Beginner's Guide </a></strong> officially published! <br>
 We have written a detailed beginner's guide for EasyEdit, specifically tailored for newcomers to the fields of knowledge editing and model editing. By reading this manual, you can quickly understand and start using EasyEdit.

✨ <strong>EasyEdit blog published!</strong>  <br>
We have also published a blog post titled "[Take Control of What Your LLM Knows and Does — with the EasyEdit Tool Series](https://huggingface.co/blog/xzwnlp/easyedit)", where you can learn more about how EasyEdit empowers you to control and edit your LLM’s knowledge and behavior.
  &nbsp;
</p>

<h1 style="font-size: 32px; color: #333; text-align: left;">
  <span style="font-size: 30px; color:rgb(180, 148, 61);">📢</span> Update
</h1>
<p align="left">
🔥 <strong><a href="README_2.md" style="text-decoration: none; ">EasyEdit 2.0</a></strong> officially published! <br>
 Unlike EasyEdit1.0, which achieves knowledge editing by updating internal parameters or introducing additional parameters, EasyEdit2 enables real-time steering of LLMs during inference. It provides a unified framework for controllability without retraining, seamlessly integrating various steering methods for ease of use and evaluation.
  &nbsp; 👉 <strong><a href="README_2.md" style="text-decoration: none; ">[README]</a></strong> (for more details). 
</p>

## Table of Contents

- [Table of Contents](#table-of-contents)
- [🔔News](#news)
- [Editing Demo](#editing-demo)
- [Knowledge Editing](#knowledge-editing)
  - [Task Definition](#task-definition)
    - [Knowledge insert](#knowledge-insert)
    - [Knowledge update](#knowledge-update)
    - [Knowledge erase](#knowledge-erase)
  - [Comparisons of the different technologies](#comparisons-of-different-technologies)
  - [Evaluation](#evaluation)
- [🌟Overview](#overview)
    - [Current Implementation](#current-implementation)
    - [Quick Start on Some Works](#quick-start-on-some-works)
    - [Tutorial notebook](#tutorial-notebook)
- [Requirements](#requirements)
    - [🔧Pip Installation](#pip-installation)
    - [⚡uv Installation](#uv-installation)
    - [Editing GPU memory usage](#editing-gpu-memory-usage)
- [📌Use EasyEdit](#use-easyedit)
  - [BaseEditor](#baseeditor)
    - [Introduction by a Simple Example](#introduction-by-a-simple-example)
  - [Evaluation](#evaluation-1)
  - [Trainer](#trainer)
- [Use EasyEdit with KnowEdit](#use-easyedit-with-knowedit)
  - [Dataset](#dataset)
  - [Usage](#usage)
- [Editing Performance](#editing-performance)
- [Citation](#citation)
- [🎉Contributors](#contributors)
    - [Other Related Projects](#other-related-projects)

## 🔔News
- 2026-07-13, 🎉 EasyEdit has been selected for the CCF ODTC open source incentive program.
- 2026-07-08, 🚀 EasyEdit has received a major upgrade, bringing Transformers 5.x compatibility, new models support, more reliable multi-GPU editing, enhanced multimodal pipelines, a unified EasyEdit2 steering workflow, expanded vLLM support, and faster multi-worker deployment.
- 2026-03-04, 🎉 [SteerEval](https://github.com/zjunlp/EasyEdit/blob/main/examples/SteerEval.md) is released — a hierarchical benchmark for evaluating LLM controllability across behavioral domains and granularity levels, with an automated data synthesis pipeline.
- 2025-10-12, ⚡ [LightMem](https://github.com/zjunlp/LightMem) is released — a lightweight and efficient memory framework empowering LLMs and AI agents with long-term memory capabilities!
- 2025-10-02, 👑 [SimIE](https://openreview.net/pdf?id=VdEG08ZJCH) has arrived — a general framework for lifelong model editing, which restores the strong performance of parameter-modifying methods from standard model editing in a lifelong context!
- 2025-09-10, 🎉🎉 [EasyEdit2 Paper](https://arxiv.org/abs/2504.15133) has been accepted by the EMNLP 2025 System Demonstration Track.
- 2025-07-24, 🚀🚀the EasyEdit has added three new unstructured long-form knowledge editing datasets [AKEW](https://arxiv.org/abs/2402.18909), [LEME](https://arxiv.org/pdf/2402.09394) and [UNKE](https://arxiv.org/abs/2405.15349). In addition, EasyEdit also incorporated two of the currently most popular unstructured editing methods [UNKE](https://arxiv.org/abs/2405.15349) and [AnyEdit](https://arxiv.org/abs/2502.05628). EasyEdit2 also supports the representation steering method [RePS](https://arxiv.org/abs/2505.20809) and provides initial support for [AxBench-style evaluation](https://arxiv.org/abs/2501.17148).
- 2025-06-07, 👑 [UltraEdit](https://github.com/XiaojieGu/UltraEdit) has arrived — powered by a lifelong normalization strategy that continuously updates feature statistics across turns, it can edit 20K samples on a 7B model in just 5 minutes and scales stably to millions !
- 2025-06-05, 🌟🌟the EasyEdit has added a new model editing algorithm [CORE](https://arxiv.org/abs/2505.23026), designed to strengthen context robustness by minimizing context-sensitive variance in hidden states of the model for edited knowledge. 
- 2025-05-28, 🌟🌟the EasyEdit has added a new model editing algorithm [NAMET](https://arxiv.org/abs/2505.11876), which introduces noise during memory extraction via a one-line modification to MEMIT. Thanks to [@ybdai7](https://github.com/ybdai7) for contribution!
- 2025-05-15, 🚀🚀We released a new blog [Reflection on Knowledge Editing: Charting the Next Steps](https://fish-sorrel-a54.notion.site/Reflection-on-Knowledge-Editing-Charting-the-Next-Steps-1e6ca8e41f3a8098bd14c85ac1db8da6) discussing the next step for knowledge editing research.
- 2025-04-03, 🚀🚀We have upgraded **EasyEdit** and introduced **EasyEdit2**! EasyEdit2 provides an easy-to-use steering framework for editing large language models with **precision and flexibility**. This upgrade enhances the framework’s capabilities, making it more robust and adaptable for various steering methods. More details can be found in our [paper](https://arxiv.org/abs/2504.15133), in the [README](README_2.md) and on our [website](https://zjunlp.github.io/project/EasyEdit2/).


<details>
<summary><b>Previous News</b></summary>

- 2025-03-04, 🌟🌟In addition to the original token-level teacher-forcing paradigm for evaluation, EasyEdit has integrated a new evaluation method, following the paper titled "[The Mirage of Model Editing: Revisiting Evaluation in the Wild](https://arxiv.org/abs/2502.11177)". You can use this [script](https://github.com/zjunlp/EasyEdit/blob/main/examples/run_LLM_evaluation.py) to quickly launch this evaluation approach, which better aligns with real-world requirements. Special thanks to [@WanliYoung](https://github.com/WanliYoung) for contribution!
- 2025-01-03, We have updated the evaluation method in paper "[CKnowEdit: A New Chinese Knowledge Editing Dataset for Linguistics, Facts, and Logic Error Correction in LLMs](https://arxiv.org/abs/2409.05806)", adopting an LLM-as-a-judge approach that is more aligned with real-world scenarios and practical applications. Both the experimental results and the running scripts have been updated accordingly in [readme](https://github.com/zjunlp/EasyEdit/blob/main/examples/CKnowEdit.md).
- 2024-11-19, we update the Table 4 results in the paper "[A Comprehensive Study of Knowledge Editing for Large Language Models](https://arxiv.org/abs/2401.01286)" after optimizing certain methods (related to AdaLoRA) and fixing computational bugs (related to ROME and MEMIT) in the EasyEdit (More details in https://github.com/zjunlp/EasyEdit/issues/427). These improvements have led to better results than before. We will continue updating this paper and welcome everyone to discuss and exchange ideas.
- 2024-11-11, 🎉🎉the paper on model editing for LLMs4Code, "[Model Editing for LLMs4Code: How Far are We?](https://arxiv.org/abs/2411.06638)", has been accepted by ICSE 2025! This work proposes a benchmark for LLMs4Code editing, [CLMEEval](https://github.com/xpq-tech/code-llmedit), which is built upon EasyEdit!
- 2024-11-09, we fixed a bug regarding the [KnowEdit](https://huggingface.co/datasets/zjunlp/KnowEdit) results in the https://github.com/zjunlp/EasyEdit/issues/390. Thanks for the help of [@StarLooo](https://github.com/StarLooo) to help us with it.

- 2024-10-24, EasyEdit has added two new knowledge editing methods, [AlphaEdit](https://github.com/zjunlp/EasyEdit/blob/main/easyeditor/models/alphaedit/README.md). In addition, we have fixed several bugs.
- 2024-10-23, the EasyEdit integrates constrained decoding methods from steering editing to mitigate hallucination in LLM and MLLM, with detailed information available in [DoLa](https://github.com/zjunlp/EasyEdit/tree/main/easyeditor/models/dola) and [DeCo](https://github.com/zjunlp/EasyEdit/tree/main/easyeditor/models/deco).
- 2024-09-26, 🎉🎉 our paper "[WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://arxiv.org/abs/2405.14768)" has been accepted by **NeurIPS 2024**.
- 2024-09-20, 🎉🎉 our papers: "[Knowledge Mechanisms in Large Language Models: A Survey and Perspective](https://arxiv.org/abs/2407.15017)" and "[Editing Conceptual Knowledge for Large Language Models](https://arxiv.org/abs/2403.06259)" have been accepted by **EMNLP 2024 Findings**.
  
- 2024-07-29, the EasyEdit has added a new model editing algorithm [EMMET](https://arxiv.org/abs/2403.14236), which generalizes ROME to the batch setting. This essentially allows making batched edits using the ROME loss function.

- 2024-07-23, we release a new paper: "[Knowledge Mechanisms in Large Language Models: A Survey and Perspective](https://arxiv.org/abs/2407.15017)", which reviews how knowledge is acquired, utilized, and evolves in large language models. This survey may provide the fundamental mechanisms for precisely and efficiently manipulating (editing) knowledge in LLMs.

- 2024-06-04, 🎉🎉 [EasyEdit Paper](https://arxiv.org/abs/2308.07269) has been accepted by the **ACL 2024** System Demonstration Track.

- 2024-06-03, we released a paper titled **["WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models"](https://arxiv.org/abs/2405.14768)**, along with introducing **a new editing task: [Continuous Knowledge Editing](#continuous-knowledge-editing)** and correspondding **lifelong editing method** called [WISE](https://github.com/zjunlp/EasyEdit/blob/main/examples/WISE.md).

- 2024-04-24, EasyEdit announced support for the **ROME method for [Llama3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B)**. Users are advised to update their transformers package to version 4.40.0.

- 2024-03-29, EasyEdit introduced **rollback support for GRACE**. For a detailed introduction, refer to the [EasyEdit documentation](#use-easyedit). Future updates will gradually include rollback support for other methods.

- 2024-03-22, a new paper titled **"[Detoxifying Large Language Models via Knowledge Editing](https://arxiv.org/abs/2403.14472)"** was released, along with a new dataset named [SafeEdit](https://huggingface.co/datasets/zjunlp/SafeEdit) and a new **detoxification method** called [DINM](https://github.com/zjunlp/EasyEdit/blob/main/examples/SafeEdit.md).

- 2024-03-12, another paper titled **"[Editing Conceptual Knowledge for Large Language Models](https://arxiv.org/abs/2403.06259)"** was released, introducing a new dataset named [ConceptEdit](https://huggingface.co/datasets/zjunlp/ConceptEdit).

- 2024-03-01, EasyEdit added support for a new method called **FT-M**. This method involves training a specific MLP layer **using cross-entropy loss on the target answer and masking the original text**. It outperforms the **FT-L** implementation in [ROME](https://github.com/kmeng01/rome). The author of issue https://github.com/zjunlp/EasyEdit/issues/173  is thanked for their advice.

- 2024-02-27, EasyEdit added support for a new method called [InstructEdit](https://github.com/zjunlp/EasyEdit/blob/main/examples/InstructEdit.md), with technical details provided in the paper **"[InstructEdit: Instruction-based Knowledge Editing for Large Language Models](https://arxiv.org/abs/2402.16123)"**.
<!-- - **2024-02-20 The AAAI2024 tutorial "*Knowledge Editing for Large Language Models*" has been canceled since speakers cannot present in person, we make this ppt[[Github](https://github.com/zjunlp/KnowledgeEditingPapers/blob/main/AAAI2024%40Tutorial_Knowledge%20Editing%20for%20LLMs.pdf)] [[Google Drive](https://drive.google.com/file/d/1fkTbVeRJSWmU7fBDeNf1OhHEkLSofQde/view?usp=sharing)] [[Baidu Pan](https://pan.baidu.com/s/1oJYgaMnxWIBE4kIcJuMSKg?pwd=p9j5)] available to the community**. -->
  
- 2024-02-09, the EasyEdit has added the support for the Dynamic LoRA model editing method [MELO'AAAI24](https://arxiv.org/abs/2312.11795).
- 2024-02-06, we release a new paper: "[EasyInstruct: An Easy-to-use Instruction Processing Framework for Large Language Models](https://arxiv.org/abs/2402.03049)" with an HF demo [EasyInstruct](https://huggingface.co/spaces/zjunlp/EasyInstruct).
- 2024-02-06, we release a preliminary tool [EasyDetect](https://github.com/OpenKG-ORG/EasyDetect) for LLM hallucination detection，with a [demo](http://easydetect.openkg.cn/).
- 2024-01-24, the EasyEdit has added the support for editing [Mistral-7B](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1) (manually update transformers==4.34.0), we have also fixed some bugs in evaluating MEND (slightly influence the performance).
- 2024-01-16, the EasyEdit has added the support for the precise model editing method [PMET'AAAI24](https://arxiv.org/abs/2308.08742).
- 2024-01-03, we release a new paper:"[A Comprehensive Study of Knowledge Editing for Large Language Models](https://arxiv.org/abs/2401.01286)" with a new benchmark [KnowEdit](https://huggingface.co/datasets/zjunlp/KnowEdit)! KnowEdit is constructed by re-organizing and cleaning existing datasests including WikiBio, ZsRE, WikiData Counterfact, WikiData Recent, convsent, Sanitation with new train/val/test spliting. Special thanks to the builders and maintainers of the those datasets.We are looking forward to any comments or discussions on this topic :)
- 2023-12-06, the EasyEdit has added the support for the lifelong model editing method [GRACE'NeurIPS24](https://arxiv.org/abs/2211.11031).
- 2023-11-18, our tutorial "Knowledge Editing for Large Language Models" has been accepted by COLING 2024.
- 2023-10-25, our tutorial "Knowledge Editing for Large Language Models" has been accepted by AAAI 2024.
- 2023-10-24, the EasyEdit has added the support for efficient editing of [Baichuan2](https://github.com/baichuan-inc/Baichuan2), [ChatGLM2](https://github.com/THUDM/ChatGLM2-6B), [InternLM](https://github.com/InternLM/InternLM), [QWen](https://github.com/QwenLM/Qwen) and fixed several bugs for a better user experience.
- 2023-10-14, we release the [MultimodalEditor](https://github.com/zjunlp/EasyEdit/blob/main/examples/MMEdit.md) based on the paper "[Can We Edit Multimodal Large Language Models?](https://arxiv.org/abs/2310.08475)".
- 2023-10-13, we release the paper "[Can We Edit Multimodal Large Language Models?](https://arxiv.org/abs/2310.08475)" accepted by EMNLP 2023.
- 2023-10-08, our paper "[Editing Large Language Models: Problems, Methods, and Opportunities](https://arxiv.org/abs/2305.13172)" has been accepted by EMNLP 2023.
- 2023-10-07, the EasyEdit has added the support for editing models with multiple GPUs, using huggingface [`Accelerate`](https://github.com/zjunlp/EasyEdit/blob/main/hparams/ROME/llama-7b.yaml#L24).
- 2023-9-21, the EasyEdit has added the support for Parameter-Efficient Fine-Tuning through AdaLoRA to inject knowledge into the LLM.
- 2023-8-31, the EasyEdit has added the support for official fine-tuning API for gpt-3.5-turbo to customize ChatGPT for your editing cases.
- 2023-8-15, we release the paper "[EasyEdit: An Easy-to-use Knowledge Editing Framework for Large Language Models](https://arxiv.org/abs/2308.07269)."
- 2023-7-12, we release version 0.0.1, supporting several knowledge editing techniques for LLMs. EasyEdit helps to better align LLMs with changing needs and values of users.
- 2023-5-22, we release the paper "[Editing Large Language Models: Problems, Methods, and Opportunities](https://arxiv.org/abs/2305.13172)" and provide a paper list at [PaperList](https://github.com/zjunlp/KnowledgeEditingPapers).
- 2023-3-25, the EasyEdit project has been launched and is under development.

</details>

<!-- **EasyEdit** is now publicly open-sourced, with a [demo video](https://www.youtube.com/watch?v=NaQRvSYuQMo) and long-term maintenance. -->

---

> A Comprehensive Study of Knowledge Editing for Large Language Models [[paper](https://arxiv.org/abs/2401.01286)][[benchmark](https://huggingface.co/datasets/zjunlp/KnowEdit)][[code](https://github.com/zjunlp/EasyEdit)] 

> IJCAI 2024 Tutorial [Google Drive](https://drive.google.com/file/d/1sg3Dy3gQo2bwOoLwWMFh57NfHROf3Ahg/view?usp=sharing)

> COLING 2024 Tutorial [Google Drive](https://drive.google.com/file/d/1vFzRYjnzkuZaNdjdIxQwWbEybCY7YqY9/view?usp=sharing)  

> AAAI 2024 Tutorial [Google Drive](https://drive.google.com/file/d/1fkTbVeRJSWmU7fBDeNf1OhHEkLSofQde/view?usp=sharing) 

> AACL 2023 Tutorial [[Google Drive](https://drive.google.com/file/d/1EW-cusC_llCM0wEshkIdYuYrvfBPCDRz/view?usp=sharing)] [[Baidu Pan](https://pan.baidu.com/s/1NupastGJUzcUIAjI64J1tw?pwd=i5an)]


## Editing Demo

There is a demonstration of editing. The GIF file is created by [Terminalizer](https://github.com/faressoft/terminalizer). <br>

We provide a handy [Jupyter Notebook](https://github.com/zjunlp/EasyEdit/blob/main/tutorial-notebooks/EasyEdit_Example_US_President.ipynb)! It allows you to edit a LLM's knowledge of the US president, switching from Biden to Trump and even back to Biden. This includes methods like [WISE](https://arxiv.org/abs/2405.14768), [AlphaEdit](https://arxiv.org/abs/2410.02355), AdaLoRA, and Prompt-based editing.


<img src="figs/demo_usage_new.gif" width="550" height="470" align=center>

## Knowledge Editing

<div align=center><img src="./figs/ke.png" width="100%" height="80%" /></div>



### Task Definition

Deployed models may still make unpredictable errors. For example, LLMs notoriously _hallucinate_, _perpetuate bias_, and _factually decay_, so we should be able to adjust specific behaviors of pre-trained models.

**Knowledge editing** aims to adjust base model's $(f_\theta)$ behavior on the particular edit descriptor $[x_e, y_e]$​​​ efficiently.

### Multi Setting

#### Single Knowledge Editing

Evaluating the performance of the model after a single edit. The model reloads the original weights (e.g. LoRA discards the adapter weights) after a single edit. You should set **`sequential_edit=False`**

$$\theta' \leftarrow \text{arg} \min\limits_{\theta} (\Vert f_\theta(x_e) - y_e \Vert)$$

#### Continuous Knowledge Editing

This requires **sequentially editing**, and evaluation is performed after all knowledge updates have been applied:

$$\theta' \leftarrow \text{arg} \min\limits_{\theta} \sum_{e=1}^{\Vert X_e \Vert} (\Vert f_\theta(x_e) - y_e \Vert)$$

It makes parameter adjustments for $(x_e, y_e)$, where $x_e \in X_e$ and $f_\theta'(x_e) = y_e$. Here, $X_e$​ represents the whole **edit set**. To enable continuous editing, you can set **`sequential_edit=True`**: [README](https://github.com/zjunlp/EasyEdit/blob/main/examples/WISE.md) (for more details).

### Multi Scenario

<details><summary> <b> Factual Knowledge Editing </b> </summary>

##### Knowledge insert

- Inject knowledge that LLMs have not seen before. such as:
  - *How many times has Messi won the World Cup? 0* $\rightarrow$ **1**:


##### Knowledge update

- Update outdated knowledge. such as:
  - *The president of USA: Donald Trump* $\rightarrow$ **Joe Biden**:



## `Dockerfile`

# Use the official Ubuntu 22.04 image
FROM ubuntu:22.04

# Set working directory
WORKDIR /app

# Set non-interactive mode to avoid issues during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update and install necessary dependencies in a single RUN command
RUN apt-get update && apt-get install -y --no-install-recommends \
  wget \
  git \
  bzip2 \
  libglib2.0-0 \
  libxext6 \
  libsm6 \
  libxrender1 \
  make \
  g++ \
  && rm -rf /var/lib/apt/lists/*

# Install Miniconda
RUN wget -q https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
  && bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda \
  && rm Miniconda3-latest-Linux-x86_64.sh 

# Set PATH to include Miniconda
ENV PATH="/opt/conda/bin:$PATH"

# Clone the EasyEdit project
RUN git clone https://github.com/zjunlp/EasyEdit.git && \
    cd EasyEdit

# Copy environment file and create the Conda environment
COPY environment.yml /app/EasyEdit/
RUN conda env create -f /app/EasyEdit/environment.yml

# Use conda shell for all subsequent commands
SHELL ["conda", "run", "-n", "EasyEdit", "/bin/bash", "-c"]

# Set Conda default environment
RUN echo "source activate EasyEdit" > ~/.bashrc
ENV PATH="/opt/conda/envs/EasyEdit/bin:$PATH"

# Install additional dependencies
COPY requirements.txt /app/EasyEdit/
RUN pip install --no-cache-dir -r /app/EasyEdit/requirements.txt

# Set working directory
WORKDIR /app/EasyEdit

# Expose any required ports (e.g., Jupyter Notebook)
EXPOSE 8888

# Default command
CMD ["bash"]

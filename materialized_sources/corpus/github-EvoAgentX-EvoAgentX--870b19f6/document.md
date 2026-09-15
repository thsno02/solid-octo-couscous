# Repository semantic capsule: EvoAgentX/EvoAgentX

- Commit: `d77fd6b9a3e76c8dd83bebe3374c53a3f5d16f54`
- Default branch: `main`
- Description: EvoAgentX/EvoAgentX
- Selected evidence files: 4 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

<!-- Add logo here -->
<div align="center">
  <a href="https://github.com/EvoAgentX/EvoAgentX">
    <img src="./assets/EAXLoGo.svg" alt="EvoAgentX" width="50%">
  </a>
</div>

<h2 align="center">
    Building a Self-Evolving Ecosystem of AI Agents
</h2>

<div align="center">

[![EvoAgentX Homepage](https://img.shields.io/badge/EvoAgentX-Homepage-blue?logo=homebridge)](https://evoagentx.org/)
[![Docs](https://img.shields.io/badge/-Documentation-0A66C2?logo=readthedocs&logoColor=white&color=7289DA&labelColor=grey)](https://EvoAgentX.github.io/EvoAgentX/)
[![Discord](https://img.shields.io/badge/Chat-Discord-5865F2?&logo=discord&logoColor=white)](https://discord.gg/XWBZUJFwKe)
[![Twitter](https://img.shields.io/badge/Follow-@EvoAgentX-e3dee5?&logo=x&logoColor=white)](https://x.com/EvoAgentX)
[![Wechat](https://img.shields.io/badge/WeChat-EvoAgentX-brightgreen?logo=wechat&logoColor=white)](./assets/wechat_info.md)
[![GitHub star chart](https://img.shields.io/github/stars/EvoAgentX/EvoAgentX?style=social)](https://star-history.com/#EvoAgentX/EvoAgentX)
[![GitHub fork](https://img.shields.io/github/forks/EvoAgentX/EvoAgentX?style=social)](https://github.com/EvoAgentX/EvoAgentX/fork)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?)](https://github.com/EvoAgentX/EvoAgentX/blob/main/LICENSE)
<!-- [![EvoAgentX Homepage](https://img.shields.io/badge/EvoAgentX-Homepage-blue?logo=homebridge)](https://EvoAgentX.github.io/EvoAgentX/) -->
<!-- [![hf_space](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-EvoAgentX-ffc107?color=ffc107&logoColor=white)](https://huggingface.co/EvoAgentX) -->
</div>

<div align="center">

<h3 align="center">

<a href="./README.md" style="text-decoration: underline;">English</a> | <a href="./README-zh.md">简体中文</a>

</h3>

</div>



## What is EvoAgentX
EvoAgentX is an open-source framework for building, evaluating, and evolving LLM-based agents or agentic workflows in an automated, modular, and goal-driven manner. At its core, EvoAgentX enables developers and researchers to move beyond static prompt chaining or manual workflow orchestration. It introduces a self-evolving agent ecosystem, where AI agents can be constructed, assessed, and optimized through iterative feedback loops—much like how software is continuously tested and improved.

### ✨ Key Features

- 🧱 **Agent Workflow Autoconstruction**
  
  From a single prompt, EvoAgentX builds structured, multi-agent workflows tailored to the task.

- 🔍 **Built-in Evaluation**
  
  It integrates automatic evaluators to score agent behavior using task-specific criteria.

- 🔁 **Self-Evolution Engine**
  
  Agents don’t just work—they learn. EvoAgentX improves workflows using self-evolving algorithms.
- 🧩 **Plug-and-Play Compatibility**
  
  Easily integrate original [OpenAI](https://github.com/EvoAgentX/EvoAgentX/blob/main/evoagentx/models/openai_model.py) and [qwen](https://github.com/EvoAgentX/EvoAgentX/blob/main/evoagentx/models/aliyun_model.py) or other popular models, including Claude, Deepseek, kimi models through ([LiteLLM](https://github.com/EvoAgentX/EvoAgentX/blob/main/evoagentx/models/litellm_model.py), [siliconflow](https://github.com/EvoAgentX/EvoAgentX/blob/main/evoagentx/models/siliconflow_model.py) or [openrouter](https://github.com/EvoAgentX/EvoAgentX/blob/main/evoagentx/models/openrouter_model.py)). If you want to use LLMs locally deployed on your own machine, you can try LiteLLM. 

- 🧰 **Comprehensive Built-in Tools**
  
  EvoAgentX ships with a rich set of built-in tools that empower agents to interact with real-world environments.

- 🧠 **Memory Module**
  
  EvoAgentX supports both ephemeral (short-term) and persistent (long-term) memory systems.

- 🧑‍💻 **Human-in-the-Loop (HITL) Interactions**
  
  EvoAgentX supports interactive workflows where humans review, correct, and guide agent behavior.


### 🚀 What You Can Do with EvoAgentX

EvoAgentX isn’t just a framework — it’s your **launchpad for real-world AI agents**.

Whether you're an AI researcher, workflow engineer, or startup team, EvoAgentX helps you **go from a vague idea to a fully functional agentic system** — with minimal engineering and maximum flexibility.

Here’s how:

- 🔍 **Struggling to improve your workflows?**  
  EvoAgentX can **automatically evolve and optimize your agentic workflows** using SOTA self-evolving algorithms, driven by your dataset and goals.
- 🧑‍💻 **Want to supervise the agent and stay in control?**  
  Insert yourself into the loop! EvoAgentX supports **Human-in-the-Loop (HITL)** checkpoints, so you can step in, review, or guide the workflow as needed — and step out again.

- 🧠 **Frustrated by agents that forget everything?**  
  EvoAgentX provides **both short-term and long-term memory modules**, enabling your agents to remember, reflect, and improve across interactions.

- ⚙️ **Lost in manual workflow orchestration?**  
  Just describe your goal — EvoAgentX will **automatically assemble a multi-agent workflow** that matches your intent.

- 🌍 **Want your agents to actually *do* things?**  
  With a rich library of built-in tools (search, code, browser, file I/O, APIs, and more), EvoAgentX empowers agents to **interact with the real world**, not just talk about it.



## 🔥 EAX Latest News

- **[Aug 2025]** 🚀 **New Survey Released!**  
  Our team just published a comprehensive survey on **Self-Evolving AI Agents**—exploring how agents can learn, adapt, and optimize over time.  
  👉 [Read it on arXiv](https://arxiv.org/abs/2508.07407)
  👉 [Check the repo](https://github.com/EvoAgentX/Awesome-Self-Evolving-Agents)

- **[July 2025]** 📚 **EvoAgentX Framework Paper is Live!**  
  We officially published the EvoAgentX framework paper on arXiv, detailing our approach to building evolving agentic workflows.  
  👉 [Check it out](https://arxiv.org/abs/2507.03616)

- **[July 2025]** ⭐️ **1,000 Stars Reached!**  
  Thanks to our amazing community, **EvoAgentX** has surpassed 1,000 GitHub stars!

- **[May 2025]** 🚀 **Official Launch!**  
  **EvoAgentX** is now live! Start building self-evolving AI workflows from day one.  
  🔧 [Get Started on GitHub](https://github.com/EvoAgentX/EvoAgentX)

## ⚡ Get Started
- [🔥 Latest News](#-latest-news)
- [⚡ Get Started](#-get-started)
- [Installation](#installation)
- [LLM Configuration](#llm-configuration)
  - [API Key Configuration](#api-key-configuration)
  - [Configure and Use the LLM](#configure-and-use-the-llm)
- [Automatic WorkFlow Generation](#automatic-workflow-generation)
- [EvoAgentX Built-in Tools Summary](#-evoagentx-built-in-tools-summary)
- [Tool-Enabled Workflows Generation](#tool-enabled-workflows-generation)
- [Demo Video](#demo-video)
  - [✨ Final Results](#-final-results)
- [Evolution Algorithms](#evolution-algorithms)
  - [📊 Results](#-results)
- [Applications](#applications)
- [Tutorial and Use Cases](#tutorial-and-use-cases)
- [🗣️ EvoAgentX TALK](#evoagentx-talk)
- [🎯 Roadmap](#-roadmap)  
- [🙋 Support](#-support)
  - [Join the Community](#join-the-community)
  - [Add the meeting to your calendar](#add-the-meeting-to-your-calendar)
  - [Contact Information](#contact-information)
  - [Community Call](#community-call)
- [🙌 Contributing to EvoAgentX](#-contributing-to-evoagentx)
- [📖 Citation](#-citation)
- [📚 Acknowledgements](#-acknowledgements)
- [📄 License](#-license)



## Installation

We recommend installing EvoAgentX using `pip`:

```bash
pip install evoagentx
```
or install from source:

```bash
pip install git+https://github.com/EvoAgentX/EvoAgentX.git
```

For local development or detailed setup (e.g., using conda), refer to the [Installation Guide for EvoAgentX](./docs/installation.md).

<details>
<summary>Example (optional, for local development):</summary>

```bash
git clone https://github.com/EvoAgentX/EvoAgentX.git
cd EvoAgentX
# Create a new conda environment
conda create -n evoagentx python=3.11

# Activate the environment
conda activate evoagentx

# Install the package
pip install -r requirements.txt
# OR install in development mode
pip install -e .
```
</details>

## LLM Configuration

### API Key Configuration 

To use LLMs with EvoAgentX (e.g., OpenAI), you must set up your API key.

<details>
<summary>Option 1: Set API Key via Environment Variable</summary> 

- Linux/macOS: 
```bash
export OPENAI_API_KEY=<your-openai-api-key>
```

- Windows Command Prompt: 
```cmd 
set OPENAI_API_KEY=<your-openai-api-key>
```

-  Windows PowerShell:
```powershell
$env:OPENAI_API_KEY="<your-openai-api-key>" # " is required 
```

Once set, you can access the key in your Python code with:
```python
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
```
</details>

<details>
<summary>Option 2: Use .env File</summary> 

- Create a .env file in your project root and add the following:
```bash
OPENAI_API_KEY=<your-openai-api-key>
```

Then load it in Python:
```python
from dotenv import load_dotenv 
import os 


## `CONTRIBUTING.md`

# Contributing to EvoAgentX

Thank you for considering contributing to **EvoAgentX** – an automatic agentic workflow generation and evolving framework! We appreciate your interest and contributions to improving the project.

## 🚀 Getting Started for Contributors

If you're interested in contributing code:

1. Clone the repo and set up your Python environment
2. Install dependencies in development mode via `pip install -e .`
3. Make changes in a new branch
4. Submit a Pull Request

📌 New to EvoAgentX? Try the [Quickstart Guide](./docs/quickstart.md)

🔧 To report bugs, request features, or ask questions

Please scroll down to the **Contributing Guide** below 👇 — detailed templates are available there.

## 🛠 How to Contribute

### **1. Reporting Bugs** 🐞

If you encounter a bug, error, or unexpected behavior:
- ✅ First, check our [Issues](https://github.com/EvoAgentX/EvoAgentX/issues) and [Discussions](https://github.com/EvoAgentX/EvoAgentX/discussions) to see if it's already been reported. 

- ✅ Then, use the [🐞 Bug Report Template](https://github.com/EvoAgentX/EvoAgentX/issues/new?template=bug_report.yml) to submit it.

Please make sure to:
- Use a clear title and concise description of the bug.
- Provide environment details (OS, Python version, etc.)
- Include steps to reproduce the issue.
- Include logs, screenshots, and environment details.


### **2. Suggesting Features** 💡
To propose a new feature or enhancement:
- ✅ First, check existing [feature requests](https://github.com/EvoAgentX/EvoAgentX/issues?q=label%3Aenhancement) to see if it's already been requested. 
- ✅ Then, use the [💡 Feature Request Template](https://github.com/EvoAgentX/EvoAgentX/issues/new?template=feature_request.yml) to submit it.  

Please make sure to:
- Use a clear title and concise description of the feature.
- Provide a use case explaining why this feature is beneficial.
- Suggest a possible implementation approach if possible.

### **3. Asking Questions / Getting Help** 🤔 
For usage questions or general help:
- ✅ We encourage you to use the [Discussions](https://github.com/EvoAgentX/EvoAgentX/discussions) area first.
- ✅ If you can't find an answer, use the [🤔 Question Template](https://github.com/EvoAgentX/EvoAgentX/issues/new?template=question.yml) to submit it.

Please make sure to:
- Provide a clear and concise description of your question.
- Include relevant details such as code snippets, configs, links, error messages, or screenshots.

#### ✨ Tip
You can also find links to all issue types when you click “New Issue” on the [Issues tab](https://github.com/EvoAgentX/EvoAgentX/issues).

### **4. Code Contributions** 👨‍💻
#### **Step 1: Create a Branch**
Before making changes, create a new branch:
```bash
git checkout -b feature/your-feature-name
```

#### **Step 2: Implement Your Changes**
- Follow the project’s coding style.
- Write clean, maintainable, and well-documented code.
- Add relevant unit tests for your changes.

#### **Step 3: Commit Your Changes**
- Follow conventional commit messages:
  ```bash
  git commit -m "feat: add new agent workflow module"
  ```
- Use descriptive commit messages.

#### **Step 4: Push Your Changes**
```bash
git push origin feature/your-feature-name
```

#### **Step 5: Submit a Pull Request**
- Navigate to the main repository and create a **Pull Request** (PR).
- Provide a clear description of your changes.
- Reference the related issue if applicable.
- Wait for a review and respond to feedback promptly.

## 📏 Coding Guidelines

### Google-Style Docstring Guidelines

All Python functions, classes, and modules in this project should use **Google-style docstrings**. Below are the guidelines and examples that contributors must follow to maintain consistency and clarity throughout the codebase.

---


#### Basic Structure

A typical Google-style docstring contains:

1. **Short Summary**  
   A brief statement of what the function or class does.
2. **Args**  
   A list of parameters with their types (optional) and descriptions.
3. **Returns** or **Yields**  
   Explains what the function returns or yields, along with types and descriptions.
4. **Raises** (optional)  
   Documents any exceptions that might be raised.
5. **Other sections** (optional)  
   Such as **Example(s)**, **Attributes** (for classes), etc.

**Example Layout**:

```python
class Calculator:
    """A simple calculator class to demonstrate Google-style docstrings.

    This class provides basic arithmetic operations. Advanced features can be
    added as needed.

    Attributes:
        last_result (float): Stores the result of the most recent operation.
    """

    def __init__(self):
        """Initializes the Calculator with a default result of 0."""
        self.last_result = 0

    def add(self, a, b):
        """Adds two numbers and updates `last_result`.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of `a` and `b`.
        """
        self.last_result = a + b
        return self.last_result

    def subtract(self, a, b):
        """Subtracts b from a and updates `last_result`.

        Args:
            a (float): The number to be subtracted from.
            b (float): The number to subtract.

        Returns:
            float: The result of `a - b`.
        """
        self.last_result = a - b
        return self.last_result
```

## 🧪 Testing
Before submitting a PR, ensure that all tests pass:
```bash
pytest tests/
```

## 🔄 Syncing Your Fork
To stay updated with the latest changes:
```bash
git fetch upstream
```
```bash
git merge upstream/main
```

## 🤝 Community Guidelines
- Be respectful and inclusive.
- Provide constructive feedback.
- Keep discussions relevant to the project.

## 📩 Contact
For any questions, feel free to open an issue or reach out to the maintainers.

Happy coding! 🚀

## `pyproject.toml`

[build-system]
requires = ["setuptools>=64", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "evoagentx"
version = "0.1.4"
description = "A framework for evolving agentic workflows with LLMs."
readme = "README.md"
requires-python = ">=3.10"
license = {text = "MIT"}
authors = [{name = "EvoAgentX Team", email = "evoagentx.ai@gmail.com"}]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
]

dependencies = [
    "overdue",
    "tenacity",
    "networkx>=3.3",
    "numpy>=1.26.4",
    "pandas>=2.2.3",
    "pydantic>=2.9.0",
    "loguru>=0.7.3",
    "python-dotenv>=1.0.0",
    "requests>=2.28.0",
    "openai>=1.55.3",
    "litellm>=1.83.10",
    "dashscope>=1.23.4",
    "tree_sitter",
    "tree_sitter_python",
    "PyYAML>=6.0",
    "tqdm>=4.65.0",
    "regex",
    "jsonschema"
]

[project.optional-dependencies]
dev = [
    "pytest",
    "pytest-cov",
    "pytest-mock",
    "pytest-asyncio",
    "pytest-subtests",
    "pytest-json-report",
    "ruff"
]
rag = [
    "llama-index",
    "llama-index-vector-stores-faiss",
    "llama-index-graph-stores-neo4j",
    "llama-index-embeddings-azure-openai",
    "faiss-cpu==1.8.0.post1",
    "sentence-transformers",
    "transformers>=4.41,<5",
    "cryptography<49",
    "neo4j",
    "ollama",
    "docx2txt",
    "python-pptx"
]
tools = [
    "docker>=6.1.2",
    "googlesearch-python",
    "wikipedia",
    "beautifulsoup4",
    "selenium",
    "html2text",
    "fastmcp>=2.2.0,<3.0",
    "cryptography<49",
    "PyPDF2",
    "Pillow",
    "exa-py>=2.0.0",
    "pymongo>=4.6.0",
    "psycopg2-binary>=2.9.0",
    "spacy",
    "selectolax",
    "feedparser",
    "telethon>=1.35.0",
    "ddgs",
    "reportlab>=3.6.0",
    "webdriver-manager>=3.8.0",
    "browser-use; python_version >= \"3.11\"",
    "browser-use-py310x; python_version < \"3.11\"",
    "google-api-python-client>=2.0.0",
    "google-auth-oauthlib>=1.0.0",
    "google-auth-httplib2>=0.1.0"
]
multimodal = [
    "torch",
    "datasets>=3.4.0",
    # Transitive dep of `datasets`; 0.70.18+ resource_tracker raises a harmless
    # AttributeError at shutdown on some Python builds. Pin below it.
    "multiprocess<0.70.18",
    "voyageai"
]
optimizers = [
    "textgrad>=0.1.8",
    "dspy",
    "optuna",
    "cloudpickle",
    "ujson>=5.9.0"
]
benchmarks = [
    "sympy",
    "antlr4-python3-runtime==4.11"
]
viz = [
    "matplotlib>=3.10.0"
]
all = [
    "llama-index",
    "llama-index-vector-stores-faiss",
    "llama-index-graph-stores-neo4j",
    "llama-index-embeddings-azure-openai",
    "faiss-cpu==1.8.0.post1",
    "sentence-transformers",
    "transformers>=4.41,<5",
    "cryptography<49",
    "neo4j",
    "ollama",
    "docx2txt",
    "python-pptx",
    "docker>=6.1.2",
    "googlesearch-python",
    "wikipedia",
    "beautifulsoup4",
    "selenium",
    "html2text",
    "fastmcp>=2.2.0,<3.0",
    "cryptography<49",
    "PyPDF2",
    "Pillow",
    "exa-py>=2.0.0",
    "pymongo>=4.6.0",
    "psycopg2-binary>=2.9.0",
    "spacy",
    "selectolax",
    "feedparser",
    "telethon>=1.35.0",
    "ddgs",
    "reportlab>=3.6.0",
    "webdriver-manager>=3.8.0",
    "browser-use; python_version >= \"3.11\"",
    "browser-use-py310x; python_version < \"3.11\"",
    "google-api-python-client>=2.0.0",
    "google-auth-oauthlib>=1.0.0",
    "google-auth-httplib2>=0.1.0",
    "torch",
    "datasets>=3.4.0",
    "multiprocess<0.70.18",
    "voyageai",
    "textgrad>=0.1.8",
    "dspy",
    "optuna",
    "cloudpickle",
    "ujson>=5.9.0",
    "sympy",
    "antlr4-python3-runtime==4.11",
    "matplotlib>=3.10.0"
]

[project.urls]
Homepage = "https://github.com/EvoAgentX/EvoAgentX"
Documentation = "https://EvoAgentX.github.io/EvoAgentX/"
Repository = "https://github.com/EvoAgentX/EvoAgentX"

[tool.setuptools.packages.find]
where = ["."]

## `docs/index.md`

# **EvoAgentX**

<p align="center" style="font-size: 1.0rem;">
  <em>An automated framework for evaluating and evolving agentic workflows.</em>
</p>

<p align="center">
  <img src="./assets/framework_en.jpg">
</p>


## What is EvoAgentX
EvoAgentX is an open-source framework for building, evaluating, and evolving LLM-based agents or agentic workflows in an automated, modular, and goal-driven manner.

At its core, EvoAgentX enables developers and researchers to move beyond static prompt chaining or manual workflow orchestration. It introduces a self-evolving agent ecosystem, where AI agents can be constructed, assessed, and optimized through iterative feedback loops—much like how software is continuously tested and improved.

### ✨ Key Features

- 🧱 **Agent Workflow Autoconstruction**
  
  From a single prompt, EvoAgentX builds structured, multi-agent workflows tailored to the task.

- 🔍 **Built-in Evaluation**
  
  It integrates automatic evaluators to score agent behavior using task-specific criteria.

- 🔁 **Self-Evolution Engine**
  
  Agents don’t just work—they learn. EvoAgentX evolves workflows using optimization strategies like retrieval augmentation, mutation, and guided search.

- 🧩 **Plug-and-Play Compatibility**
  
  Easily integrate original [OpenAI](https://github.com/EvoAgentX/EvoAgentX/blob/main/evoagentx/models/openai_model.py) and [qwen](https://github.com/EvoAgentX/EvoAgentX/blob/main/evoagentx/models/aliyun_model.py) or other popular models, including Claude, Deepseek, kimi models through ([LiteLLM](https://github.com/EvoAgentX/EvoAgentX/blob/main/evoagentx/models/litellm_model.py), [siliconflow](https://github.com/EvoAgentX/EvoAgentX/blob/main/evoagentx/models/siliconflow_model.py) or [openrouter](https://github.com/EvoAgentX/EvoAgentX/blob/main/evoagentx/models/openrouter_model.py)). If you want to use LLMs locally deployed on your own machine, you can try LiteLLM. 

- 🧰 **Comprehensive Built-in Tools**
  
  EvoAgentX ships with a rich set of built-in tools that empower agents to interact with real-world environments.

- 🧠 **Memory Module**
  
  EvoAgentX supports both ephemeral (short-term) and persistent (long-term) memory systems.

- 🧑‍💻 **Human-in-the-Loop (HITL) Interactions**
  
  EvoAgentX supports interactive workflows where humans review, correct, and guide agent behavior.


### 🚀 What You Can Do with EvoAgentX

EvoAgentX isn’t just a framework — it’s your **launchpad for real-world AI agents**.

Whether you're an AI researcher, workflow engineer, or startup team, EvoAgentX helps you **go from a vague idea to a fully functional agentic system** — with minimal engineering and maximum flexibility.

Here’s how:

- 🔍 **Struggling to find the perfect prompt?**
  
  EvoAgentX can **automatically explore and evolve prompts** using state-of-the-art self-improving algorithms, all guided by your dataset and goal.

- 🧑‍💻 **Want to supervise the agent and stay in control?**
  
  Insert yourself into the loop! EvoAgentX supports **Human-in-the-Loop (HITL)** checkpoints, so you can step in, review, or guide the workflow as needed — and step out again.

- 🧠 **Frustrated by agents that forget everything?**
  
  EvoAgentX provides **both short-term and long-term memory modules**, enabling your agents to remember, reflect, and improve across interactions.

- ⚙️ **Lost in manual workflow orchestration?**
  
  Just describe your goal — EvoAgentX will **automatically assemble a multi-agent workflow** that matches your intent.

- 🌍 **Want your agents to actually *do* things?**
  
  With a rich library of built-in tools (search, code, browser, file I/O, APIs, and more), EvoAgentX empowers agents to **interact with the real world**, not just talk about it.


## 🔥 EAX Latest News

- **[Aug 2025]** 🚀 **New Survey Released!**  
  Our team just published a comprehensive survey on **Self-Evolving AI Agents**—exploring how agents can learn, adapt, and optimize over time.  
  👉 [Read it on arXiv](https://arxiv.org/abs/2508.07407)

- **[July 2025]** 📚 **EvoAgentX Framework Paper is Live!**  
  We officially published the EvoAgentX framework paper on arXiv, detailing our approach to building evolving agentic workflows.  
  👉 [Check it out](https://arxiv.org/abs/2507.03616)

- **[July 2025]** ⭐️ **1,000 Stars Reached!**  
  Thanks to our amazing community, **EvoAgentX** has surpassed 1,000 GitHub stars!

- **[May 2025]** 🚀 **Official Launch!**  
  **EvoAgentX** is now live! Start building self-evolving AI workflows from day one.  
  🔧 [Get Started on GitHub](https://github.com/EvoAgentX/EvoAgentX)


## 🎥 Demo Video

[![Watch on YouTube](https://img.shields.io/badge/-Watch%20on%20YouTube-red?logo=youtube&labelColor=grey)](https://www.youtube.com/watch?v=8ALcspHOe0o)
[![Watch on Bilibili](https://img.shields.io/badge/-Watch%20on%20Bilibili-00A1D6?logo=bilibili&labelColor=white)](https://www.bilibili.com/video/BV1AjahzRECi/?vd_source=02f8f3a7c8865b3af6378d9680393f5a)

<div align="center">
  <iframe width="600" height="338"
          src="https://www.youtube.com/embed/8ALcspHOe0o"
          title="YouTube video player" frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          allowfullscreen>
  </iframe>
</div>


In this demo, we showcase the workflow generation and execution capabilities of EvoAgentX through two examples:

- **Application 1: Financial Information Agentic Workflow**
  In this example, we use a workflow generated by EvoAgentX to collect public information about a company based on a given index.
  
  The collected data includes the overall market index, the company’s current stock price, institutional buy/sell activity, and more.
  
  Finally, the workflow generates an **HTML report** summarizing the information and providing a buy/sell/hold recommendation. This workflow is only an alpha version.
  
  If you're interested in turning it into a **truly practical investment assistant**, you can consider integrating more financial indicators and analytical tools—and let these tools join your workflow through agents! Check [here](https://github.com/EvoAgentX/EvoAgentX/blob/main/examples/workflow/invest/stock_analysis.py) to try this workflow.
  
- **Application 2: ArXiv Research Summarizer Workflow**

  This workflow, generated by EvoAgentX and powered by the ArXiv MCP tool, can retrieve and summarize relevant papers from arXiv based on your provided keywords and selected time range.
   
  If you're interested, you can even **extend this workflow beyond arXiv**, integrating it with other academic search platforms like **Google Scholar**, and turn it into a fully functional research assistant application! Check [here](https://github.com/EvoAgentX/EvoAgentX/blob/main/examples/workflow/arxiv_workflow.py) to play with this workflow. 


## 🧰 EvoAgentX Built-in Tools Overview
EvoAgentX ships with a comprehensive suite of **built-in tools**, enabling agents to interact with code environments, search engines, databases, filesystems, images, and browsers. These modular toolkits form the backbone of multi-agent workflows and are easy to extend, customize, and test.

Categories include:
- 🧮 **Code Interpreters (Python, Docker)**

- 🔍 **Search & HTTP Requests (Google, Wikipedia, arXiv, RSS)**
  
- 🗂️ **Filesystem Utilities (read/write, shell commands)**
  
- 🧠 **Databases (MongoDB, PostgreSQL, FAISS)**
  
- 🖼️ **Image Tools (analysis, generation)**
  
- 🌐 **Browser Automation (low-level & LLM-driven)**

Check [here](https://github.com/EvoAgentX/EvoAgentX/blob/main/docs/tutorial/tools.md) for the full list of available tools.

We actively welcome contributions from the community!  
Feel free to propose or submit new tools via [pull requests](https://github.com/EvoAgentX/EvoAgentX/pulls) or [discussions](https://github.com/EvoAgentX/EvoAgentX/discussions).


## 🎯 Roadmap
- **Modularize Evolution Algorithms**: Abstract optimization algorithms into plug-and-play modules that can be easily integrated into custom workflows. 
- **Develop Task Templates and Agent Modules**: Build reusable templates for typical tasks and standardized agent components to streamline application development.
- **Integrate Self-Evolving Agent Algorithms**: Incorporate more recent and advanced agent self-evolution across multiple dimensions, including prompt tuning, workflow structures, and memory modules. 
- **Enable Visual Workflow Editing Interface**: Provide a visual interface for workflow structure display and editing to improve usability and debugging. 


## 🙋 Support

### Join the Community

📢 Stay connected and be part of the **EvoAgentX** journey!  
🚩 Join our community to get the latest updates, share your ideas, and collaborate with AI enthusiasts worldwide.

- [Discord](https://discord.gg/XWBZUJFwKe) — Chat, discuss, and collaborate in real-time.
- [X (formerly Twitter)](https://x.com/EvoAgentX) — Follow us for news, updates, and insights.
- [WeChat](https://github.com/EvoAgentX/EvoAgentX/blob/main/assets/wechat_info.md) — Connect with our Chinese community.

### Add the meeting to your calendar

📅 Click the link below to add the EvoAgentX Weekly Meeting (Sundays, 16:30–17:30 GMT+8) to your calendar:

👉 [Add to your Google Calendar](https://calendar.google.com/calendar/u/0/r/eventedit?text=EvoAgentX+周会（腾讯会议）&dates=20250629T083000Z/20250629T093000Z&details=会议链接：https://meeting.tencent.com/dm/5UuNxo7Detz0&location=Online&recur=RRULE:FREQ=WEEKLY;BYDAY=SU;UNTIL=20270523T093000Z&ctz=Asia/Shanghai)

👉 [Add to your Tencent Meeting](https://meeting.tencent.com/dm/5UuNxo7Detz0)

👉 [Download the EvoAgentX_Weekly_Meeting.ics file](./EvoAgentX_Weekly_Meeting.ics)

### Contact Information

If you have any questions or feedback about this project, please feel free to contact us. We highly appreciate your suggestions!

- **Email:** evoagentx.ai@gmail.com

We will respond to all questions within 2-3 business days.

### Community Call
- [Bilibili](https://space.bilibili.com/3493105294641286/favlist?fid=3584589186&ftype=create&spm_id_from=333.788.0.0)
- [Youtube](https://studio.youtube.com/playlist/PL_kuPS05qA1hyU6cLX--bJ93Km2-md8AA/edit)
## 🙌 Contributing to EvoAgentX
Thanks go to these awesome contributors

<a href="https://github.com/EvoAgentX/EvoAgentX/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=EvoAgentX/EvoAgentX" />
</a>

We appreciate your interest in contributing to our open-source initiative. We provide a document of [contributing guidelines](https://github.com/EvoAgentX/EvoAgentX/blob/main/CONTRIBUTING.md) which outlines the steps for contributing to EvoAgentX. Please refer to this guide to ensure smooth collaboration and successful contributions. 🤝🚀

[![Star History Chart](https://api.star-history.com/svg?repos=EvoAgentX/EvoAgentX&type=Date)](https://www.star-history.com/#EvoAgentX/EvoAgentX&Date)

## 📖 Citation

Please consider citing our work if you find EvoAgentX helpful:

📄 [EvoAgentX](https://arxiv.org/abs/2507.03616)
📄 [Survey Paper](https://arxiv.org/abs/2508.07407)

```bibtex
@article{wang2025evoagentx,
  title={EvoAgentX: An Automated Framework for Evolving Agentic Workflows},
  author={Wang, Yingxu and Liu, Siwei and Fang, Jinyuan and Meng, Zaiqiao},
  journal={arXiv preprint arXiv:2507.03616},
  year={2025}
}
@article{fang202survey,
      title={A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm Bridging Foundation Models and Lifelong Agentic Systems}, 
      author={Jinyuan Fang and Yanwen Peng and Xi Zhang and Yingxu Wang and Xinhao Yi and Guibin Zhang and Yi Xu and Bin Wu and Siwei Liu and Zihao Li and Zhaochun Ren and Nikos Aletras and Xi Wang and Han Zhou and Zaiqiao Meng},
      year={2025},
      journal={arXiv preprint arXiv:2508.07407},
      url={https://arxiv.org/abs/2508.07407}, 
}

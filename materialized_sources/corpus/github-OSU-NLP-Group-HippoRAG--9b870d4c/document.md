# Repository semantic capsule: OSU-NLP-Group/HippoRAG

- Commit: `1438aba3fc44ff10573e5a5e1e7cc3c7f9794aff`
- Default branch: `main`
- Description: OSU-NLP-Group/HippoRAG
- Selected evidence files: 3 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

<h1 align="center">HippoRAG 2: From RAG to Memory</h1>
<p align="center">
    <img src="https://github.com/OSU-NLP-Group/HippoRAG/raw/main/images/hippo_brain.png" width="55%" style="max-width: 300px;">
</p>

[<img align="center" src="https://colab.research.google.com/assets/colab-badge.svg" />](https://colab.research.google.com/drive/1nuelysWsXL8F5xH6q4JYJI8mvtlmeM9O#scrollTo=TjHdNe2KC81K)

[<img align="center" src="https://img.shields.io/badge/arXiv-2502.14802 HippoRAG 2-b31b1b" />](https://arxiv.org/abs/2502.14802)
[<img align="center" src="https://img.shields.io/badge/🤗 Dataset-HippoRAG 2-yellow" />](https://huggingface.co/datasets/osunlp/HippoRAG_2/tree/main)
[<img align="center" src="https://img.shields.io/badge/arXiv-2405.14831 HippoRAG 1-b31b1b" />](https://arxiv.org/abs/2405.14831)
[<img align="center" src="https://img.shields.io/badge/GitHub-HippoRAG 1-blue" />](https://github.com/OSU-NLP-Group/HippoRAG/tree/legacy)

HippoRAG 2 is a memory framework for LLMs that recognizes and uses connections in new knowledge, mirroring a key function of human long-term memory.

Our experiments show that HippoRAG 2 improves associativity (multi-hop retrieval) and sense-making (the process of integrating large and complex contexts) in even the most advanced RAG systems, without sacrificing their performance on simpler tasks.

Like its predecessor, HippoRAG 2 remains cost and latency efficient in online processes, while using significantly fewer resources for offline indexing compared to other graph-based solutions such as GraphRAG, RAPTOR, and LightRAG.

<p align="center">
  <img align="center" src="https://github.com/OSU-NLP-Group/HippoRAG/raw/main/images/intro.png" />
</p>
<p align="center">
  <b>Figure 1:</b> Evaluation of continual learning capabilities across three key dimensions: factual memory (NaturalQuestions, PopQA), sense-making (NarrativeQA), and associativity (MuSiQue, 2Wiki, HotpotQA, and LV-Eval). HippoRAG 2 surpasses other methods across all
categories, bringing it one step closer to true long-term memory.
</p>

<p align="center">
  <img align="center" src="https://github.com/OSU-NLP-Group/HippoRAG/raw/main/images/methodology.png" />
</p>
<p align="center">
  <b>Figure 2:</b> HippoRAG 2 methodology.
</p>

### Papers

* [**HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models**](https://arxiv.org/abs/2405.14831) [NeurIPS '24].
* [**From RAG to Memory: Non-Parametric Continual Learning for Large Language Models**](https://arxiv.org/abs/2502.14802) [ICML '25].

----

## Installation

Use Conda or `uv` to create a Python 3.10 environment. A project-local `.venv` is recommended for development.

```sh
conda create -n hipporag python=3.10
conda activate hipporag
pip install hipporag
```
Set only the environment variables required by the models you use:

```sh
export CUDA_VISIBLE_DEVICES=0,1,2,3
export HF_HOME=<path to Huggingface home directory>
export OPENAI_API_KEY=<your openai api key>   # if you want to use OpenAI model

conda activate hipporag
```

For a project-local environment managed by `uv`:

```sh
uv venv --python 3.10 .venv
source .venv/bin/activate
uv pip install -e .
```

Install optional local-model support only when needed, for example `uv pip install -e '.[vllm]'` or `uv pip install -e '.[gritlm]'`.

HippoRAG supports `openai>=3.3.1,<4`: compatible 3.x client updates are accepted,
while a new major version requires an explicit compatibility review. To reproduce
the minimum supported SDK baseline, apply the optional constraint without changing
the library's public dependency range:

```sh
uv pip install -r requirements.txt -c constraints/openai-tested.txt
```

SDK compatibility should be checked in separate clean environments against both
the minimum baseline above and the newest allowed release. The latter can be
installed and tested with:

```sh
uv pip install -r requirements.txt --upgrade-package openai
PYTHONPATH=src python -m unittest tests.test_openai_sdk_compat
```

### Upgrading existing indexes

Version 2.0.0a5 binds persisted vectors and OpenIE state to the endpoint, deployment, model, normalization, and component identity that produced them. Existing indexes without an `index_manifest.json`, or indexes whose identity no longer matches the active configuration, are rejected rather than mixed silently. Re-index into a fresh `save_dir`; copying or fabricating only the manifest is not a safe migration. When injecting a custom embedding model, extraction LLM, or text preprocessor, set `index_identity` to a stable version string so configuration changes cannot reuse incompatible state.

## Quick Start

### OpenAI

The complete runnable version is [`examples/demo_openai.py`](examples/demo_openai.py). A minimal workflow is:

Set `OPENAI_API_KEY` before using OpenAI models:

```sh
export OPENAI_API_KEY=<your OpenAI API key>
```

```python
from hipporag import HippoRAG

docs = ["George Rankin is a politician."]
queries = ["What is George Rankin's occupation?"]
with HippoRAG(save_dir="outputs", llm_model_name="gpt-4o-mini", embedding_model_name="text-embedding-3-small") as hipporag:
    hipporag.index(docs=docs)
    results = hipporag.rag_qa(queries=queries)
```

#### OpenAI-compatible endpoints

Pass custom base URLs for OpenAI-compatible LLM and embedding servers:

```sh
export OPENAI_API_KEY=<the API key required by your endpoint>
```

For loopback endpoints that do not require authentication, HippoRAG supplies a client-local placeholder without changing the process-wide `OPENAI_API_KEY` environment variable.

OpenAI-compatible chat and embedding endpoints must return standard `usage` data. HippoRAG fails closed instead of caching a response whose token cost cannot be accounted for.

```python
hipporag = HippoRAG(
    save_dir=save_dir,
    llm_model_name="your-llm",
    llm_base_url="http://localhost:8000/v1",
    embedding_model_name="your-embedding-model",
    embedding_provider="openai",
    embedding_base_url="http://localhost:8001/v1",
)
```

### Amazon Bedrock

Models available through the standard Bedrock Runtime endpoint use the existing LiteLLM route. Prefix the Bedrock model ID with `bedrock/`, as shown in `examples/demo_bedrock.py`.

OpenAI models such as GPT-5.5 use Amazon Bedrock Mantle and its Responses API instead. Create a Bedrock API key, then run:

```sh
export AWS_BEARER_TOKEN_BEDROCK=<your Bedrock API key>
python examples/demo_bedrock_mantle.py
```

The corresponding configuration is:

```python
hipporag = HippoRAG(
    save_dir='outputs/bedrock-mantle',
    llm_model_name='bedrock-mantle/openai.gpt-5.5',
    llm_base_url='https://bedrock-mantle.us-east-2.api.aws/openai/v1',
    embedding_model_name=embedding_model_name,
)
```

The Mantle endpoint and model availability are region-specific. HippoRAG requires an explicit endpoint and raises an error if the Bedrock API key is missing. To use an existing AWS profile instead, construct a `BaseConfig` with `bedrock_mantle_auth='aws_credentials'`, `bedrock_aws_profile='<profile>'`, and `bedrock_region='<region>'`; this explicitly enables SigV4 authentication. Mantle response storage is disabled by default (`store=False`); pass `store=True` to `infer` only when server-side conversation state is required.

### OrcaRouter

OrcaRouter is an OpenAI-compatible AI gateway that routes HippoRAG's requests across models from OpenAI, Anthropic, Google Gemini, DeepSeek, and more through a single endpoint. Prefix the OrcaRouter model ID with `orcarouter/` to use it as a named provider, as shown in `examples/demo_orcarouter.py`:

```sh
export ORCAROUTER_API_KEY=<your OrcaRouter API key>
python examples/demo_orcarouter.py
```

The corresponding configuration is:

```python
hipporag = HippoRAG(
    save_dir='outputs/orcarouter',
    llm_model_name='orcarouter/anthropic/claude-opus-4.8',
    embedding_model_name=embedding_model_name,
)
```

Model names use the `vendor/model` namespace (for example `orcarouter/anthropic/claude-opus-4.8` or `orcarouter/google/gemini-2.5-flash`), and `orcarouter/auto` lets the router pick a live model automatically. HippoRAG uses the default OrcaRouter endpoint `https://api.orcarouter.ai/v1`; set `llm_base_url` explicitly to override it.

### Local Deployment (vLLM)

This simple example will illustrate how to use `hipporag` with any vLLM-compatible locally deployed LLM.

1. Run a local [OpenAI-compatible vLLM server](https://docs.vllm.ai/en/latest/getting_started/quickstart.html#quickstart-online) with specified GPUs (make sure you leave enough memory for your embedding model).

Keep `VLLM_WORKER_MULTIPROC_METHOD=spawn` when running vLLM with multiple GPUs; it makes the required multiprocessing mode explicit and avoids CUDA initialization problems with forked workers.

```sh
export CUDA_VISIBLE_DEVICES=0,1
export VLLM_WORKER_MULTIPROC_METHOD=spawn
export HF_HOME=<path to Huggingface home directory>

conda activate hipporag  # vllm should be in this environment

# Tune gpu-memory-utilization or max_model_len to fit your GPU memory, if OOM occurs
vllm serve meta-llama/Llama-3.3-70B-Instruct --tensor-parallel-size 2 --max_model_len 4096 --gpu-memory-utilization 0.95 
```

2. Now you can use very similar code to the one above to use `hipporag`: 

```python
save_dir = 'outputs'# Define save directory for HippoRAG objects (each LLM/Embedding model combination will create a new subdirectory)
llm_model_name = # Any OpenAI model name
embedding_model_name = # Embedding model name (NV-Embed, GritLM or Contriever for now)
llm_base_url= # Base url for your deployed LLM (i.e. http://localhost:8000/v1)

hipporag = HippoRAG(save_dir=save_dir,
                    llm_model_name=llm_model,
                    embedding_model_name=embedding_model_name,
                    llm_base_url=llm_base_url)

# Same Indexing, Retrieval and QA as running OpenAI models above
```

## Vector Store Backends

HippoRAG stores embeddings in local Parquet files by default. It can also use
Qdrant, ChromaDB, or Milvus through `BaseConfig.vector_store_type`.

## `CONTRIBUTING.md`

# Contributing to HippoRAG

Thank you for your interest in contributing to HippoRAG!
We are happy to welcome contributions from the community to help us improve our project.

## How to Contribute

1. Fork the repository and clone it to your local machine.
2. Create a new branch for your contribution: `git checkout -b my-contribution`.
3. Make your changes and ensure that the code passes our test scripts. More information can be found in the `Testing` section of our `README.md`. 
4. Commit your changes: `git commit -m "Add my contribution"`.
6. Push your changes to your forked repository: `git push origin my-contribution`.
7. Open a pull request to the main repository.

## Before you start, file an issue

Please follow this simple rule to help us eliminate any unnecessary wasted effort & frustration, and ensure an efficient and effective use of everyone's time - yours, ours, and other community members':

> 👉 If you have a question, think you've discovered an issue, would like to propose a new feature, etc., then find/file an issue **BEFORE** starting work to fix/implement it.

### Search existing issues first

Before filing a new issue, search existing open and closed issues first: This project is moving fast! It is likely someone else has found the problem you're seeing, and someone may be working on or have already contributed a fix!

If no existing item describes your issue/feature, great - please file a new issue:

### File a new Issue

- Don't know whether you're reporting an issue or requesting a feature? File an issue
- Have a question that you don't see answered in docs, videos, etc.? File an issue
- Want to know if we're planning on building a particular feature? File an issue
- Got a great idea for a new feature? File an issue/request/idea
- Don't understand how to do something? File an issue
- Found an existing issue that describes yours? Great - upvote and add additional commentary / info / repro-steps / etc.
 
Provide as much detail as possible to help us understand and address the problem.

---

### Credits

This contributing guide was adapted from the [GraphRAG](https://github.com/microsoft/graphrag) project. Many thanks to the team for providing a useful starting point!

---

## Thank you

We appreciate your contributions to HippoRAG!


## `pyproject.toml`

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "hipporag"
version = "2.0.0a5"
description = "A powerful graph-based RAG framework that enables LLMs to identify and leverage connections within new knowledge for improved retrieval."
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "torch==2.5.1",
    "transformers==4.45.2",
    "openai>=3.3.1,<4",
    "litellm==1.73.1",
    "networkx==3.4.2",
    "python_igraph==0.11.8",
    "tiktoken==0.7.0",
    "pydantic==2.10.4",
    "tenacity==8.5.0",
    "einops",
    "tqdm",
    "boto3",
    "nest_asyncio",
    "numpy",
    "pandas",
    "pyarrow",
    "requests",
    "scipy",
    "filelock",
    "httpx>=0.27,<1",
]

[project.optional-dependencies]
milvus = ["pymilvus[milvus_lite]>=2.4.2"]
qdrant = ["qdrant-client>=1.9"]
chroma = ["chromadb>=0.5"]
transformers-embedding = ["sentence-transformers>=3.0"]
gritlm = ["gritlm==1.0.2"]
vllm = ["vllm==0.6.6.post1", "outlines"]

[tool.setuptools.packages.find]
where = ["src"]

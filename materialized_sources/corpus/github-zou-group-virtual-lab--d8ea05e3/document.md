# Repository semantic capsule: zou-group/virtual-lab

- Commit: `8a3a4fd9ccc0cd297bd523751e03bc9527c91832`
- Default branch: `main`
- Description: zou-group/virtual-lab
- Selected evidence files: 2 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

# Virtual Lab

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/virtual-lab)](https://badge.fury.io/py/virtual-lab)
[![PyPI version](https://badge.fury.io/py/virtual-lab.svg)](https://badge.fury.io/py/virtual-lab)
[![Downloads](https://pepy.tech/badge/virtual-lab)](https://pepy.tech/project/virtual-lab)
[![license](https://img.shields.io/github/license/zou-group/virtual-lab.svg)](https://github.com/zou-group/virtual-lab/blob/main/LICENSE.txt)

![Virtual Lab](https://github.com/zou-group/virtual-lab/raw/main/images/virtual_lab_architecture.png)

The **Virtual Lab** is an AI-human collaboration for science research. In the Virtual Lab, a human researcher works with a team of large language model (LLM) **agents** to perform scientific research. Interaction between the human researcher and the LLM agents occurs via a series of **team meetings**, where all the LLM agents discuss a scientific agenda posed by the human researcher, and **individual meetings**, where the human researcher interacts with a single LLM agent to solve a particular scientific task.

Please see our paper [The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies](https://www.nature.com/articles/s41586-025-09442-9) for more details on the Virtual Lab and an application to nanobody design for SARS-CoV-2.

If you use the Virtual Lab, please cite our work as follows:

Swanson, K., Wu, W., Bulaong, N.L. et al. The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies. *Nature* (2025). https://doi.org/10.1038/s41586-025-09442-9


## Virtual Lab for nanobody design

As a real-world demonstration, we applied the Virtual Lab to design nanobodies for one of the latest variants of SARS-CoV-2 (see [nanobody_design](https://github.com/zou-group/virtual-lab/tree/main/nanobody_design)). The Virtual Lab built a computational pipeline consisting of [ESM](https://www.science.org/doi/10.1126/science.ade2574), [AlphaFold-Multimer](https://www.biorxiv.org/content/10.1101/2021.10.04.463034v2), and [Rosetta](https://rosettacommons.org/software/) and used it to design 92 nanobodies that were experimentally validated.

Please see the notebook [nanobody_design/run_nanobody_design.ipynb](https://github.com/zou-group/virtual-lab/blob/main/nanobody_design/run_nanobody_design.ipynb) for an example of how to use the Virtual Lab to create agents and run team and individual meetings.


## Installation

The Virtual Lab can be installed using pip or by cloning the repo and installing the required packages. Installation should only take a couple of minutes.

Optionally, first create a conda environment.

```bash
conda create -y -n virtual_lab python=3.14
conda activate virtual_lab
```

The Virtual Lab can be installed via pip.

```bash
pip install virtual-lab
```

To install the latest version of the Virtual Lab locally, clone the repo and then install the package.

```bash
git clone https://github.com/zou-group/virtual_lab.git
cd virtual_lab
pip install -e .
```


## OpenAI API Key

The Virtual Lab currently uses GPT-5.2 from OpenAI by default. Save your OpenAI API key as the environment variable `OPENAI_API_KEY`. For example, add `export OPENAI_API_KEY=<your_key>` to your `.bashrc` or `.bash_profile`.

## `pyproject.toml`

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "virtual-lab"
dynamic = ["version"]
authors = [
    { name = "Kyle Swanson", email = "swansonk.14@gmail.com" },
]
maintainers = [
    { name = "Kyle Swanson", email = "swansonk.14@gmail.com" },
]
description = "A virtual lab of large language model agents for scientific research."
readme = "README.md"
license = { file = "LICENSE" }
requires-python = ">=3.10"
dependencies = [
    "notebook",
    "openai",
    "requests",
    "tiktoken",
    "tqdm",
    "typed-argument-parser",
]
classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Typing :: Typed",
]
keywords = [
    "virtual lab",
    "large language model",
    "LLM",
    "scientific research",
    "automated science",
]

[project.optional-dependencies]
nanobody-design = [
    "biopython",
    "pandas",
    "seaborn",
    "torch",
    "transformers",
]

[tool.hatch.version]
path = "src/virtual_lab/__about__.py"

[project.urls]
Homepage = "https://github.com/zou-group/virtual-lab"
Issues = "https://github.com/zou-group/virtual-lab/issues"

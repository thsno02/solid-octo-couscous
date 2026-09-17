# Repository semantic capsule: facebookresearch/MLGym

- Commit: `9d40c1b5035202018cd7091fb4e83a9c68b377c0`
- Default branch: `main`
- Description: facebookresearch/MLGym
- Selected evidence files: 5 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

<p align="center">
    <img src="./assets/logos/mlgym_logo.png" height="300" width="600" alt="MLGym Logo">
</p>

<p align="center">
  <a href="https://creativecommons.org/licenses/by-nc/4.0/"><img src="https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg" /></a>
  <!-- Someone else has pypi package with the same name -->
  <!-- <a href="https://pepy.tech/project/mlgym"><img src="https://static.pepy.tech/personalized-badge/minihack?period=total&units=international_system&left_color=black&right_color=red&left_text=Downloads" /></a> -->
  <!-- <a href="https://github.com/facebookresearch/minihack/actions/workflows/test_and_deploy.yml"><img src="https://github.com/facebookresearch/minihack/actions/workflows/test_and_deploy.yml/badge.svg?branch=main" /></a> -->
  <a href="https://arxiv.org/abs/2502.14499"><img src="https://img.shields.io/badge/arXiv-2502.14499-b31b1b.svg"/></a>
  <a href="https://discord.gg/Zep3cyHhjJ"><img src="https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white" /></a>
  <a href="https://sites.google.com/view/mlgym"><img src="https://img.shields.io/badge/Website-MLGym-blue" /></a>
 </p>

## Table of contents

* [Introduction](#introduction)
* [Installation](#installation)
* [Quick Start](#quick-start)
* [Trajectory Visualizer](#trajectory-visualizer)
* [Contributions and Maintenance](#contributions-and-maintenance)
* [License](#license)

## Introduction

This is the first Gym environment for machine learning (ML) tasks, enabling research on reinforcement learning (RL) algorithms for training such agents. <span style="font-variant:small-caps;">MLGym</span>-Bench consists of 13 diverse and open-ended AI research tasks from diverse domains such as computer vision, natural language processing, reinforcement learning, and game theory. Solving these tasks requires real-world AI research skills such as generating new ideas and hypotheses, creating and processing data, implementing ML methods, training models, running experiments, analyzing the results, and iterating through this process to improve on a given task.
![image info](./assets/figs/mlgym.png)

> [!WARNING]
> Meta <span style="font-variant:small-caps;">MLGym</span> is currently an experimental framework intended for benchmarking AI Research Agents. It is under heavy development. Please expect major changes to the design.
>
> The primary goal of <span style="font-variant:small-caps;">MLGym</span> is to expand the selection of AI research tasks for benchmarking the LLM Agents and implementing RL algorithms to train LLMs in a research environment.
> `main` branch will always contain the latest stable release and all breaking changes will be announced in the [release notes](./CHANGELOG.md).

## Installation

1. Clone and install dependencies

    ```bash
    git clone git@github.com:facebookresearch/MLGym.git
    cd MLGym
    conda create -y -n mlgym python=3.11
    conda activate mlgym
    pip install -e .
    ```

2. Create a `.env` file in the MLGym directory (`MLGym/.env`) to save all the environment variables including API keys.

    ```bash
    # Env variables
    MLGYM_CONFIG_ROOT="<path_to_MLGYM_root>/configs"
    MLGYM_TASK_CONFIG_DIR="<path_to_MLGYM_root>/configs/tasks"
    MLGYM_WORKSPACE_PATH="<path_to_MLGYM_root>/workspace"
    MLGYM_ENV_TIMEOUT=10000
    MLGYM_ACTION_SHORT_TIMEOUT=60
    MLGYM_ACTION_LONG_TIMEOUT=10000
    MLGYM_MODEL_MAX_RETRIES=3

    # API keys
    OPENAI_API_KEY=""
    ANTHROPIC_API_KEY=""
    ```

3. You can use either Docker or Podman to run tasks inside a container. Podman is the recommended way to run containers on macOS.

4. Follow the instructions [here](https://docs.docker.com/desktop/) to install docker. Select the appropriate installation command based on your OS.

5. If you are working on a Linux machine, please install the `nvidia-container-runtime`. This is required to start docker containers with GPU support.

    ```bash
    sudo dnf install -y nvidia-container-toolkit
    ```

6. **Please skip to step 9 if you don't want to use Podman**.

7. For Linux:
    a. Follow the instructions [here](https://podman.io/get-started) to install Podman.
    b. Start podman socket. The last command should return a running podman socket:

    ```bash
    systemctl --user enable podman.socket
    systemctl --user start podman.socket
    systemctl --user status podman.socket
    ```

    c. Redirect docker host to podman by exporting docker host env variable in bashrc or current session:

    ```bash
    export DOCKER_HOST=unix:///run/user/$UID/podman/podman.sock
    ```

8. For MacOS:
    a. If you use Homebrew package manager, install Podman with `brew install podman`. Otherwise, follow the instructions [here](https://podman.io/get-started).
    b. Start the podman machine and set the docker host env variable:

    ```bash
    podman machine init
    podman machine start
    export DOCKER_HOST=unix://$(podman machine inspect --format '{{.ConnectionInfo.PodmanSocket.Path}}')
    ```

9. Pull the container image:

    ```bash
    docker pull aigym/mlgym-agent:latest
    ```

    or

    ```bash
    podman pull aigym/mlgym-agent:latest
    ```

10. Test launching a docker/podman container with GPU support

    ```bash
    docker run -it --gpus all --name test aigym/mlgym-agent /bin/bash
    ls -la
    exit
    ```

11. Check that GPUs are available in the docker container using `nvidia-smi`.

### Troubleshooting

If you get Nvidia CDI spec errors on linux (eg. `Error: setting up CDI devices: unresolvable CDI devices nvidia.com/gpu=all`), run these additional commands.

```bash
sudo mkdir /etc/cdi
sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml
sudo touch /etc/containers/nodocker
```

## Quick Start

### Docker

```bash
python run.py \
  --container_type docker \
  --task_config_path tasks/battleOfSexes.yaml \
  --model litellm:claude-3-5-sonnet-20240620 \
  --per_instance_cost_limit 4.00 \
  --agent_config_path configs/agents/default.yaml \
  --temp 1 \
  --gpus 0 \
  --max_steps 50 \
  --aliases_file ./dockerfiles/aliases.sh
```

### Podman

```bash
python run.py \
  --container_type podman \
  --task_config_path tasks/battleOfSexes.yaml \
  --model litellm:claude-3-5-sonnet-20240620 \
  --per_instance_cost_limit 4.00 \
  --agent_config_path configs/agents/default.yaml \
  --temp 1 \
  --gpus 0 \
  --max_steps 50 \
  --aliases_file ./dockerfiles/aliases.sh
```

To see a full list of flags, please run `python run.py --help`.

> [!NOTE]
> A detailed documentation for all parts of the <span style="font-variant:small-caps;">MLGym</span> framework is under construction. Please stay tuned!

## Trajectory Visualizer

<span style="font-variant:small-caps;">MLGym</span> provides a Web UI to inspect the agent trajectories.

```bash
streamlit run demo/trajectory_visualizer.py -- --trajectory_dir <absolute_path_to_trajectories>

# An example
streamlit run demo/trajectory_visualizer.py -- --trajectory_dir $HOME/Projects/MLGym/trajectories/mlgym_bench_v0
```

To run the demo for <span style="font-variant:small-caps;">MLGym</span>, use the following command:

```bash
streamlit run demo/demo.py
```

## Contributions and Maintenance

<span style="font-variant:small-caps;">MLGym</span> was built and is maintained by [GenAI at Meta](https://ai.meta.com/) and [UCSB NLP](http://nlp.cs.ucsb.edu/). We welcome contributions to <span style="font-variant:small-caps;">MLGym</span>. If you are interested in contributing, please see [this document](./CONTRIBUTING.md). Our maintenance plan can be found [here](./MAINTENANCE.md).

## Citation

If you find this work helpful, please consider citing us using the following:

```tex
@misc{nathani2025mlgymnewframeworkbenchmark,
      title={MLGym: A New Framework and Benchmark for Advancing AI Research Agents},
      author={Deepak Nathani and Lovish Madaan and Nicholas Roberts and Nikolay Bashlykov and Ajay Menon and Vincent Moens and Amar Budhiraja and Despoina Magka and Vladislav Vorotilov and Gaurav Chaurasia and Dieuwke Hupkes and Ricardo Silveira Cabral and Tatiana Shavrina and Jakob Foerster and Yoram Bachrach and William Yang Wang and Roberta Raileanu},
      year={2025},
      eprint={2502.14499},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2502.14499},
}
```

## License

The majority of this code is licensed under CC-BY-NC 4.0 (Attribution-NonCommercial 4.0 International) license. However portions of the project are available under separate license terms: [SWE-Agent](https://github.com/SWE-agent/SWE-agent?tab=MIT-1-ov-file) and [Modded-NanoGPT](https://github.com/KellerJordan/modded-nanogpt?tab=MIT-1-ov-file) are released under MIT license; [Gymnax](https://github.com/RobertTLange/gymnax?tab=Apache-2.0-1-ov-file) and [Gymnax-blines](https://github.com/RobertTLange/gymnax-blines?tab=Apache-2.0-1-ov-file) are released under Apache 2.0 License.

## `CLAUDE.md`

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Development Commands

### Environment Setup
```bash
# Create conda environment
conda create -y -n mlgym python=3.11
conda activate mlgym
pip install -e .

# Install development dependencies
pip install -e ".[dev]"
```

### Code Quality and Testing
```bash
# Run linting
ruff check .

# Run type checking
mypy mlgym

# Format code
ruff format .

# Fix linting issues automatically
ruff check --fix .
```

### Container Management
```bash
# Pull the MLGym container image
docker pull aigym/mlgym-agent:latest

# Test GPU container support
docker run -it --gpus all --name test aigym/mlgym-agent /bin/bash
```

### Running Tasks
```bash
# Basic run with Docker
python run.py \
  --container_type docker \
  --task_config_path tasks/battleOfSexes.yaml \
  --model litellm:claude-3-5-sonnet-20240620 \
  --per_instance_cost_limit 4.00 \
  --agent_config_path configs/agents/default.yaml \
  --temp 1 \
  --gpus 0 \
  --max_steps 50 \
  --aliases_file ./dockerfiles/aliases.sh

# Use Podman instead of Docker
python run.py --container_type podman [other args...]

# Replay trajectory visualization
streamlit run demo/trajectory_visualizer.py -- --trajectory_dir <path_to_trajectories>

# Demo interface
streamlit run demo/demo.py
```

## Code Architecture

MLGym is a framework for benchmarking AI research agents on machine learning tasks. Key components:

### Core Architecture
- **Environment (`mlgym/environment/`)**: Container-based task execution environment with Docker/Podman support
- **Agent (`mlgym/agent/`)**: Base agent implementation with history tracking and model interaction
- **Backend (`mlgym/backend/`)**: Model integration layer supporting various LLM APIs via LiteLLM
- **Tools (`mlgym/tools/`)**: Agent toolset for file operations, command execution, and task-specific utilities

### Configuration System
- **Tasks**: YAML configs in `configs/tasks/` define ML tasks (computer vision, NLP, RL, game theory)
- **Agents**: YAML configs in `configs/agents/` define agent behavior and tool access
- **Datasets**: YAML configs in `configs/datasets/` specify data sources and preprocessing

### Task Structure
- Task implementations in `data/` directories contain `evaluate.py`, baseline solutions, and requirements
- Each task has its own containerized environment with specific dependencies
- Results stored in `trajectories/` with detailed logs and metrics

### Key Files
- `run.py`: Main entry point for running experiments
- `run_replay.py`: Replay saved trajectories
- `mlgym/environment/env.py`: Core environment implementation with container management
- `mlgym/agent/base.py`: Base agent with model interaction and history processing
- `mlgym/backend/base.py`: Model API abstractions and cost tracking

### Development Notes
- Uses ruff for linting/formatting with strict type checking via mypy
- Use python with type annotations
- Target python 3.11 or higher
- Use `pathlib` instead of `os.path`. Also use `Path.read_text()` over `with ...open()` constructs
- Use `argparse` to add interfaces
- Keep code comments to a minimum and only highlight particularly logically challenging things
- Do not append to the README unless specifically requested
- Container-first architecture requires Docker/Podman for task execution
- GPU support available for RL and deep learning tasks
- Trajectory files (.traj) contain complete agent interaction history
- All paths in configs should be relative to repository root

## Environment Variables
Required in `.env` file:
```bash
MLGYM_CONFIG_ROOT="<repo_root>/configs"
MLGYM_TASK_CONFIG_DIR="<repo_root>/configs/tasks"
MLGYM_WORKSPACE_PATH="<repo_root>/workspace"
OPENAI_API_KEY=""
ANTHROPIC_API_KEY=""
```

## `CONTRIBUTING.md`

# Contributing to <span style="font-variant:small-caps;">MLGym</span>

We want to make contributing to this project as easy and transparent as
possible.

## Development

We use ruff as linter/formatter and mypy for type checking.

1. Install the developmental dependencies

    `pip install -e .[dev]`
2. Install mypy and ruff extensions in your favorite code editor.

3. Here are some design choices to keep in mind before you start developing
   - **Type Hints**: All functions must have complete type annotations using native Python types (minimal imports from `typing` library)
   - **Docstrings**: Use Google-style docstrings for all functions with proper Args/Returns/Raises sections
   - **Error Handling**: Implement proper exception handling with specific error types
   - **Path Handling**: Use `pathlib.Path` instead of `os.path` for all file/path operations
   - **Code Style**: Follow PEP 8 guidelines and use f-strings for string formatting

For VS Code and Cursor, we use the following workspace settings to streamline the development. This is just one option, and you are free to use your own development config.

```json
"mypy-type-checker.importStrategy": "fromEnvironment",
"mypy-type-checker.reportingScope": "workspace",
"mypy-type-checker.preferDaemon": true,
"[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.formatOnSaveMode": "file",
    "editor.codeActionsOnSave": {
        "source.fixAll": "explicit",
        "source.organizeImports": "explicit"
    },
},
"ruff.nativeServer": "on",
"ruff.enable": true,
"ruff.lint.enable": true,
"ruff.organizeImports": true,
"ruff.fixAll": true,
```

## Pull Requests

We actively welcome your pull requests.

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Make sure your code lints.
5. If you haven't already, complete the Contributor License Agreement ("CLA").

## Contributor License Agreement ("CLA")

In order to accept your pull request, we need you to submit a CLA. You only need
to do this once to work on any of Facebook's open source projects.

Complete your CLA here: <https://code.facebook.com/cla>

## Issues

We use GitHub issues to track public bugs. Please ensure your description is
clear and has sufficient instructions to be able to reproduce the issue.

Facebook has a [bounty program](https://www.facebook.com/whitehat/) for the safe
disclosure of security bugs. In those cases, please go through the process
outlined on that page and do not file a public issue.

## License

By contributing to <span style="font-variant:small-caps;">MLGym</span>, you agree that your contributions will be licensed
under the LICENSE file in the root directory of this source tree.

## `pyproject.toml`

# Choosing a build backend:
[build-system]
requires = ["setuptools"] # REQUIRED if [build-system] table is used
build-backend = "setuptools.build_meta" # If not defined, then legacy behavior can happen.

[project]
name = "mlgym"
dynamic = ["version"]
description = "The official MLGym package - A framework for benchmarking and training AI research agents."
readme = "README.md"
requires-python = ">=3.11"
license = {file = "LICENSE"}
keywords = ["nlp", "agents", "code", "ml"]
authors = [
    {name = "Deepak Nathani", email = "dnathani@ucsb.edu"},
    {name = "Roberta Raileanu", email = "raileanu@meta.com"}
]

# Classifiers help users find your project by categorizing it.
classifiers = [
    # How mature is this project? Common values are
    # 3 - Alpha, 4 - Beta, 5 - Production/Stable
    "Operating System :: OS Independent",
    # Indicate who your project is intended for
    "Intended Audience :: Developers",
    # Pick your license as you wish
    "License :: Creative Commons :: Attribution-NonCommercial 4.0 International",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3 :: Only",
]

dependencies = [
    "config",
    "gymnasium",
    "numpy",
    "openai>=1.0",
    "pandas",
    "simple-parsing",
    "huggingface_hub",
    "matplotlib",
    "seaborn",
    "datasets",
    "tenacity",
    "rich",
    "docker",
    "rich_argparse",
    "litellm",
    "pypdf",
    "pymupdf",
    "pymupdf4llm",
    "streamlit",
    "gputil",
]


[project.optional-dependencies]
dev = [
    "mkdocs-material",
    "mkdocs-include-markdown-plugin",
    "mkdocstrings[python]>=0.18",
    "ruff>=0.12.0",
    "mypy>=1.16.0",
    "types-PyYAML",
    "types-seaborn",
    "types-docker",
]

[tool.setuptools]
include-package-data = true

[tool.setuptools.dynamic]
version = {attr = "mlgym.__version__"}

[tool.setuptools.packages.find]
where = ["."]
namespaces = false

[project.urls]
"Source" = "https://github.com/facebookresearch/MLGym"

[tool.ruff]
# Exclude a variety of commonly ignored directories.
# Same excludes as black
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".git-rewrite",
    ".hg",
    ".ipynb_checkpoints",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".pyenv",
    ".pytest_cache",
    ".pytype",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    ".vscode",
    ".github",
    ".cursorrules",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "site-packages",
    "venv",
    # ---- project specific ----
    # Exclude tools so they don't get the __future__ imports
    "data/**",
    "tools/**",
    "demo/**",
    "scripts/**",
    "notebooks/**",
]

line-length = 120
indent-width = 4
target-version = "py311"

[tool.ruff.lint]
# Enable linters
select = [
    "E",    # pycodestyle errors
    "F",    # pyflakes
    "I",    # isort
    "W",    # pycodestyle warnings
    "C",    # flake8-comprehensions
    "B",    # flake8-bugbear
    "UP",   # pyupgrade (includes UP006 to enforce future annotations)
    "N",    # pep8-naming
    "ANN",  # flake8-annotations
    "PT",   # flake8-pytest-style
    "RUF",  # Ruff-specific rules
    "SIM",  # flake8-simplify
    "TCH",  # flake8-type-checking
    "TRY",  # tryceratops
    "PYI",  # flake8-pyi
]

# Disable specific rules to match pylint configuration
ignore = [
    "E722",  # Equivalent to pylint's broad-except-caught (W0718)
    "B023",  # Roughly equivalent to logging-fstring-interpolation (W1203)
    "E501",  # Line too long (handled by formatter)
    "TRY003",  # Tryceratops: long raise message
]
fixable = ["ALL"]

# Allow unused variables when underscore-prefixed.
dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"

# Add rules to enforce native Python types over typing
extend-select = [
    "UP006",  # Use `__future__.annotations` to postpone evaluation of annotations
    "UP007",  # Use X | Y for type annotations
]

[tool.ruff.lint.isort]
known-first-party = ["mlgym"]
required-imports = ["from __future__ import annotations"]

[tool.ruff.lint.pydocstyle]
convention = "google"

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"

[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
no_implicit_optional = true
strict_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
files = ["mlgym"]
exclude = [
    "data/.*",
    "tools/.*",
    "demo/.*",
    "scripts/.*",
    "notebooks/.*",
    "tests/.*"
]

[dependency-groups]
dev = [
    "jupyter>=1.1.1",
]

## `docs/README.md`

# Docs

Put your docs here. If you'd like to generate sphinx docs, `cd` into this directory and run:

```
pip install sphinx
sphinx-quickstart
make html
```

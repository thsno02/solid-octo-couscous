# Repository semantic capsule: Future-House/robin

- Commit: `4a5cce310f3bc7663a67117db88af43b84733ffe`
- Default branch: `main`
- Description: Future-House/robin
- Selected evidence files: 3 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

# Robin: A multi-agent system for automating scientific discovery

See our [blog](https://www.futurehouse.org/research-announcements/demonstrating-end-to-end-scientific-discovery-with-robin-a-multi-agent-system) or [arXiv](https://arxiv.org/abs/2505.13400) preprint for more info.

## Prerequisites

- **Python:** Version 3.12 or higher.
- **API Keys:**
  - `EDISON_API_KEY`: For accessing Edison platform agents (Crow, Falcon - now called 'Literature'). Obtain from https://platform.edisonscientific.com/profile. You must first create an Edison profile, purchase credits and then create an API key (Account -> Profile -> API Tokens).
  - An API key for your chosen LLM provider (e.g., `OPENAI_API_KEY` if using OpenAI models). Robin uses LiteLLM, so it can support various providers.
  - The data analysis portion of this repo requires access to the Edison platform. Without access, all the hypothesis and experiment generation code can still be run.

## Docker (Alternative Setup)

Docker is a tool that packages software into a self-contained "container" that runs the same way on any computer, regardless of your operating system or what else is installed. It's the recommended approach for Robin as it avoids the most common installation issues.

**Install Docker first:** Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/) for your operating system (Mac or Windows). Once installed, open Docker Desktop and make sure it is running (you should see the Docker icon in your menu bar/system tray) before proceeding.

For a fully self-contained environment that avoids OS-level dependency conflicts, Docker is the recommended approach:

1. **Build the image:**

   ```bash
   docker build -t robin .
   ```

2. **Set up API keys:**

   ```bash
   cp .env.example .env
   # Edit .env and fill in your EDISON_API_KEY and OPENAI_API_KEY
   ```

   Important: do **not** wrap values in quotes (e.g. `OPENAI_API_KEY=sk-abc123`, not `OPENAI_API_KEY="sk-abc123"`). Docker reads the file differently from Python and will include the quotes as part of the key.

3. **Run Jupyter:**
   ```bash
   docker run -p 8888:8888 --env-file .env robin
   ```
   Jupyter will print three URLs — use only the one that starts with `http://127.0.0.1:8888/` (the other two are internal container addresses and will not work). Your URL will look like: `http://127.0.0.1:8888/lab/tree/robin_demo.ipynb?token=...`

---

## Setup Instructions

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/Future-House/robin.git
    cd robin
    ```

2.  **Create and Activate a Virtual Environment (Recommended):**

    ```bash
    uv venv .venv
    source .venv/bin/activate
    ```

    OR

    ```bash
    python3 -m venv .robin_env
    source .robin_env/bin/activate
    ```

3.  **Install Dependencies:**
    The project uses `pyproject.toml` for dependency management. Install the base package and development dependencies (which include Jupyter):

    ```bash
    uv pip install -e '.[dev]'
    ```

    OR

    ```bash
    pip install -e '.[dev]'
    ```

4.  **Set API Keys:**
    Copy the provided template and fill in your keys:
    ```bash
    cp .env.example .env
    # Then edit .env with your actual keys
    ```
    Robin will automatically load this `.env` file at startup. Alternatively, you can export the variables in your shell, or pass them directly when creating the `RobinConfiguration` object.

## Running Robin via `robin_demo.ipynb`

_In order to run Robin as used in the manuscript, only input the name of a disease, with no other text. If you wish to optimize how Robin searches for experimental models and therapeutic candidates, we suggest changing the internal prompts of Robin (via prompts.py), not the initial input to the pipeline._

1.  **Launch Jupyter Notebook or JupyterLab:**
    Navigate to the `robin` directory in your terminal (ensure your virtual environment is activated) and run:

    ```bash
    jupyter notebook
    # OR
    jupyter lab
    ```

2.  **Open the Notebook:**
    In the Jupyter interface, open `robin_demo.ipynb`.

3.  **Configure Robin:**
    Locate the cell where the `RobinConfiguration` object is created:

    ```python
    config = RobinConfiguration(
        disease_name="DISEASE_NAME",  # <-- Customize the disease name here
        # You can also explicitly set API keys here if not using environment variables:
        # edison_api_key="your_edison_api_key_here"
    )
    ```

    - **Modify `disease_name`**: Change `"DISEASE_NAME"` to your target disease.
    - **API Keys**: If you didn't set environment variables, you can provide the keys directly in the `RobinConfiguration` instantiation.
    - **LLM Choice**: The default is `o4-mini`. You can change `llm_name` and `llm_config` in `RobinConfiguration` if you wish to use a different model supported by LiteLLM (ensure you have the corresponding API key set).
    - Other parameters like `num_queries`, `num_assays`, `num_candidates` can also be adjusted here if needed.

4.  **Run the Notebook Cells:**
    Execute the cells in the notebook sequentially. The notebook is structured to guide you through:
    - **Experimental Assay Generation:** Generates and ranks potential experimental assays.
    - **Therapeutic Candidate Generation:** Based on the top assay, generates and ranks therapeutic candidates.
    - **(Optional) Experimental Data Analysis:** If you have experimental data, this section can analyze it and feed insights back into candidate generation. This requires access to the Edison platform data analysis features.

## Expected Output

- **Logs:** Detailed logs will be printed in the notebook output and/or your console, showing the progress of each step (e.g., query generation, literature search, candidate proposal, ranking).

- **Files:** Results are saved in a new subdirectory within `robin_output/`, named after the `disease_name` and a timestamp (e.g., `robin_output/DISEASE_NAME_YYYY-MM-DD_HH-MM/`). This directory contains a structured set of outputs, including:
  - Folders for detailed hypotheses and literature reviews for both experimental assays and therapeutic candidates (e.g., `experimental_assay_detailed_hypotheses/`, `therapeutic_candidate_literature_reviews/`).
  - CSV files for ranking results and final ranked lists (e.g., `experimental_assay_ranking_results.csv`, `ranked_therapeutic_candidates.csv`).
  - Text summaries for proposed assays and candidates (e.g., `experimental_assay_summary.txt`, `therapeutic_candidates_summary.txt`).
  - If the optional data analysis step is run (using the `data_analysis` function), there will be an additional `data_analysis/` subfolder containing outputs from the Finch agent (e.g., `consensus_results.csv`). Correspondingly, some therapeutic candidate-related files generated after this step may have an `_experimental` suffix (e.g., `ranked_therapeutic_candidates_experimental.csv`, `therapeutic_candidate_detailed_hypotheses_experimental/`).

## Overview of `examples` Folder:

The `examples` folder provides practical usage demonstrations of pre-generated output directories from complete Robin runs for 10 diseases:

- Age-Related Hearing Loss
- Celiac Disease
- Charcot-Marie-Tooth Disease
- Chronic Kidney Disease
- Friedreich's Ataxia
- Glaucoma
- Idiopathic Pulmonary Fibrosis
- Non-alcoholic Steatohepatitis
- Polycystic Ovary Syndrome
- Sarcopenia

Each disease-specific subfolder mirrors the exact file and directory structure a user would obtain in their own `robin_output/` directory after a run:

- `experimental_assay_detailed_hypotheses/`: Text files containing detailed reports for each proposed experimental assay.
- `experimental_assay_literature_reviews/`: Text files of literature reviews generated from queries related to assay development.
- `experimental_assay_ranking_results.csv`: CSV file showing pairwise comparison results for assay ranking.
- `experimental_assay_summary.txt`: A textual summary of the proposed experimental assays.
- `ranked_therapeutic_candidates.csv`: CSV file listing the final ranked therapeutic candidates and their strength scores.
- `therapeutic_candidate_detailed_hypotheses/`: Text files with detailed reports for each proposed therapeutic candidate.
- `therapeutic_candidate_literature_reviews/`: Text files of literature reviews for therapeutic candidate queries.
- `therapeutic_candidate_ranking_results.csv`: CSV file of pairwise comparison results for candidate ranking.
- `therapeutic_candidates_summary.txt`: A textual summary of the proposed therapeutic candidates.

These example outputs are provided to help users to understand the depth, format, and typical errors seen in Robin runs across various diseases.

## Advanced Usage

A full example trajectory of both the initial therapeutic candidate generation and experimental data analysis can be found in the `robin_full.ipynb` notebook. This notebook includes the parameters and agents used in the paper.

While this guide focuses on the `robin_demo.ipynb` notebook, the `robin` Python module (in the `robin/` directory) can be imported and its functions (`experimental_assay`, `therapeutic_candidates`, `data_analysis`) can be used programmatically in your own Python scripts for more customized workflows.

## `Dockerfile`

FROM python:3.12-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml .
COPY robin/ robin/
COPY robin_demo.ipynb .
COPY robin_full.ipynb .

RUN SETUPTOOLS_SCM_PRETEND_VERSION=0.0.0 uv pip install --system -e '.[dev]'

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root"]

## `pyproject.toml`

[build-system]
build-backend = "setuptools.build_meta"
requires = ["setuptools>=64", "setuptools_scm>=8"]

[dependency-groups]
dev = ["robin[dev]"]

[project]
authors = [
    {email = "hello@futurehouse.org", name = "FutureHouse technical staff"},
]
# Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
classifiers = [
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python",
]
dependencies = [
    "aiofiles",
    "anthropic",
    "choix",
    "edison-client>=0.11",
    "fhaviary",
    "fhlmi",
    "openai>=1",
    "pandas>=2",
    "pydantic>=2",
    "python-dotenv",
    "tqdm",
]
description = "Multi-agent system for therapeutics development"
dynamic = ["version"]
keywords = ["scientific discovery"]
license = {file = "LICENSE"}
name = "robin"
readme = "README.md"
requires-python = ">=3.12"

[project.optional-dependencies]
dev = [
    "ipykernel>=6.29",  # For running Jupter notebooks, and pin to keep recent
    "ipython>=8",  # Pin to keep recent
    "jupyterlab>=4",  # Pin to keep recent
    "mypy>=1.8",  # Pin for mutable-override
    "pandas-stubs",
    "pre-commit>=3.4",  # Pin to keep recent
    "pylint-pydantic",
    "pylint>=3",
    "refurb>=2",  # Pin to keep recent
    "typeguard",
    "types-aiofiles",
    "types-tqdm",
]

[project.urls]
issues = "https://github.com/Future-House/robin/issues"
repository = "https://github.com/Future-House/robin"

[tool.black]
preview = true

[tool.mypy]
# Type-checks the interior of functions without type annotations.
check_untyped_defs = true
# Allows enabling one or multiple error codes globally. Note: This option will
# override disabled error codes from the disable_error_code option.
enable_error_code = [
    "ignore-without-code",
    "mutable-override",
    "redundant-cast",
    "redundant-expr",
    "redundant-self",
    "truthy-bool",
    "truthy-iterable",
    "unimported-reveal",
    "unreachable",
    "unused-awaitable",
    "unused-ignore",
]
# Shows a short summary line after error messages.
error_summary = false
# A regular expression that matches file names, directory names and paths which mypy
# should ignore while recursively discovering files to check. Use forward slashes (/) as
# directory separators on all platforms.
exclude = [
    "^\\.?venv",  # SEE: https://regex101.com/r/0rp5Br/1
]
# Specifies the OS platform for the target program, for example darwin or win32
# (meaning OS X or Windows, respectively). The default is the current platform
# as revealed by Python’s sys.platform variable.
platform = "linux"
# Comma-separated list of mypy plugins.
plugins = ["pydantic.mypy"]
# Use visually nicer output in error messages: use soft word wrap, show source
# code snippets, and show error location markers.
pretty = true
# Shows column numbers in error messages.
show_column_numbers = true
# Shows error codes in error messages.
# SEE: https://mypy.readthedocs.io/en/stable/error_codes.html#error-codes
show_error_codes = true
# Prefixes each error with the relevant context.
show_error_context = true
# Warns about casting an expression to its inferred type.
warn_redundant_casts = true
# Shows a warning when encountering any code inferred to be unreachable or
# redundant after performing type analysis.
warn_unreachable = true
# Warns about per-module sections in the config file that do not match any
# files processed when invoking mypy.
warn_unused_configs = true
# Warns about unneeded `# type: ignore` comments.
warn_unused_ignores = true

[[tool.mypy.overrides]]
# Suppresses error messages about imports that cannot be resolved.
ignore_missing_imports = true
# Per-module configuration options
module = [
    "choix",
    "futurehouse_client.*",
]

[tool.pylint]

[tool.pylint.design]
# Maximum number of attributes for a class (see R0902).
max-attributes = 12

[tool.pylint.format]
# Maximum number of characters on a single line.
max-line-length = 97  # Match ruff line-length

[tool.pylint.main]
# Use multiple processes to speed up Pylint. Specifying 0 will auto-detect the
# number of processors available to use, and will cap the count on Windows to
# avoid hangs.
jobs = 0
# List of plugins (as comma separated values of python module names) to load,
# usually to register additional checkers.
load-plugins = [
    "pylint_pydantic",
]

[tool.pylint.messages_control]
# Disable the message, report, category or checker with the given id(s).
disable = [
    "bare-except",  # Rely on ruff E722 for this
    "broad-exception-caught",  # Don't care to enforce this
    "broad-exception-raised",  # Rely on ruff TRY002 for this
    "cyclic-import",  # Let Python blow up
    "dangerous-default-value",  # Rely on ruff W0102 for this
    "empty-docstring",  # Let pep257 take care of docstrings
    "expression-not-assigned",  # Rely on mypy func-returns-value for this
    "fixme",  # codetags are useful
    "function-redefined",  # Rely on mypy no-redef for this
    "global-statement",  # Rely on ruff PLW0603 for this
    "global-variable-not-assigned",  # Rely on ruff PLW0602 for this
    "import-outside-toplevel",  # Rely on ruff PLC0415 for this
    "invalid-name",  # Don't care to enforce this
    "keyword-arg-before-vararg",  # Rely on ruff B026 for this
    "line-too-long",  # Rely on ruff E501 for this
    "logging-fstring-interpolation",  # f-strings are convenient
    "logging-too-many-args",  # Rely on ruff PLE1205 for this
    "missing-docstring",  # Let docformatter and ruff take care of docstrings
    "missing-final-newline",  # Rely on ruff W292 for this
    "no-else-return",  # Rely on ruff RET506 for this
    "no-member",  # Buggy, SEE: https://github.com/pylint-dev/pylint/issues/8138
    "no-value-for-parameter",  # Rely on mypy call-arg for this
    "not-callable",  # Don't care to enforce this
    "protected-access",  # Don't care to enforce this
    "raise-missing-from",  # Rely on ruff B904 for this
    "redefined-builtin",  # Rely on ruff A002 for this
    "super-init-not-called",  # Don't care to enforce this
    "too-few-public-methods",  # Don't care to enforce this
    "too-many-ancestors",  # Don't care to enforce this
    "too-many-arguments",  # Don't care to enforce this
    "too-many-boolean-expressions",  # Rely on ruff PLR0916 for this
    "too-many-branches",  # Rely on ruff PLR0912 for this
    "too-many-instance-attributes",  # Don't care to enforce this
    "too-many-lines",  # Don't care to enforce this
    "too-many-locals",  # Rely on ruff PLR0914 for this
    "too-many-nested-blocks",  # Rely on ruff PLR1702 for this
    "too-many-positional-arguments",  # Don't care to enforce this
    "too-many-public-methods",  # Rely on ruff PLR0904 for this
    "too-many-return-statements",  # Rely on ruff PLR0911 for this
    "too-many-statements",  # Rely on ruff PLR0915 for this
    "undefined-loop-variable",  # Don't care to enforce this
    "ungrouped-imports",  # Rely on ruff I001 for this
    "unidiomatic-typecheck",  # Rely on ruff E721 for this
    "unnecessary-dict-index-lookup",  # Rely on ruff PLR1733 for this
    "unreachable",  # Rely on mypy unreachable for this
    "unspecified-encoding",  # Rely on ruff PLW1514 for this
    "unspecified-encoding",  # Don't care to enforce this
    "unsubscriptable-object",  # Buggy, SEE: https://github.com/pylint-dev/pylint/issues/3637
    "unsupported-membership-test",  # Buggy, SEE: https://github.com/pylint-dev/pylint/issues/3045
    "unused-argument",  # Rely on ruff ARG002 for this
    "unused-import",  # Rely on ruff F401 for this
    "unused-variable",  # Rely on ruff F841 for this
    "wrong-import-order",  # Rely on ruff I001 for this
    "wrong-import-position",  # Rely on ruff E402 for this
]
# Enable the message, report, category or checker with the given id(s).
enable = [
    "useless-suppression",  # Print unused `pylint: disable` comments
]

[tool.pylint.reports]
# Set true to activate the evaluation score.
score = false

[tool.pylint.similarities]
# Minimum lines number of a similarity.
min-similarity-lines = 12

[tool.refurb]
enable_all = true
ignore = [

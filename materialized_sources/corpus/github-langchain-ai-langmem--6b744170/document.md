# Repository semantic capsule: langchain-ai/langmem

- Commit: `9d033b47d9ce53e37e92c92241b0496c0278932e`
- Default branch: `main`
- Description: langchain-ai/langmem
- Selected evidence files: 4 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

# LangMem

LangMem helps agents learn and adapt from their interactions over time.

It provides tooling to extract important information from conversations, optimize agent behavior through prompt refinement, and maintain long-term memory.

It offers both functional primitives you can use with any storage system and native integration with LangGraph's storage layer.

This lets your agents continuously improve, personalize their responses, and maintain consistent behavior across sessions.

## Key features

- 🧩 **Core memory API** that works with any storage system
- 🧠 **Memory management tools** that agents can use to record and search information during active conversations "in the hot path"
- ⚙️ **Background memory manager** that automatically extracts, consolidates, and updates agent knowledge
- ⚡ **Native integration with LangGraph's Long-term Memory Store**, available by default in all LangGraph Platform deployments

## Installation

```bash
pip install -U langmem
```

Configure your environment with an API key for your favorite LLM provider:

```bash
export ANTHROPIC_API_KEY="sk-..."  # Or another supported LLM provider
```

## Creating an Agent

Here's how to create an agent that actively manages its own long-term memory in just a few lines:

```python
# Import core components (1)
from langgraph.prebuilt import create_react_agent
from langgraph.store.memory import InMemoryStore
from langmem import create_manage_memory_tool, create_search_memory_tool

# Set up storage (2)
store = InMemoryStore(
    index={
        "dims": 1536,
        "embed": "openai:text-embedding-3-small",
    }
) 

# Create an agent with memory capabilities (3)
agent = create_react_agent(
    "anthropic:claude-3-5-sonnet-latest",
    tools=[
        # Memory tools use LangGraph's BaseStore for persistence (4)
        create_manage_memory_tool(namespace=("memories",)),
        create_search_memory_tool(namespace=("memories",)),
    ],
    store=store,
)
```

1. The memory tools work in any LangGraph app. Here we use [`create_react_agent`](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.create_react_agent) to run an LLM with tools, but you can add these tools to your existing agents or build [custom memory systems](concepts/conceptual_guide.md#functional-core) without agents.

2. [`InMemoryStore`](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.memory.InMemoryStore) keeps memories in process memory—they'll be lost on restart. For production, use the [AsyncPostgresStore](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.AsyncPostgresStore) or a similar DB-backed store to persist memories across server restarts.

3. The memory tools ([`create_manage_memory_tool`](reference/tools.md#langmem.create_manage_memory_tool) and [`create_search_memory_tool`](reference/tools.md#langmem.create_search_memory_tool)) let you control what gets stored. The agent extracts key information from conversations, maintains memory consistency, and knows when to search past interactions. See [Memory Tools](guides/memory_tools.md) for configuration options.

Then use the agent:

```python
# Store a new memory (1)
agent.invoke(
    {"messages": [{"role": "user", "content": "Remember that I prefer dark mode."}]}
)

# Retrieve the stored memory (2)
response = agent.invoke(
    {"messages": [{"role": "user", "content": "What are my lighting preferences?"}]}
)
print(response["messages"][-1].content)
# Output: "You've told me that you prefer dark mode."
```

1. The agent gets to decide what and when to store the memory. No special commands needed—just chat normally and the agent uses [`create_manage_memory_tool`](reference/tools.md#langmem.create_manage_memory_tool) to store relevant details.

2. The agent maintains context between chats. When you ask about previous interactions, the LLM can invoke [`create_search_memory_tool`](reference/tools.md#langmem.create_search_memory_tool) to search for memories with similar content. See [Memory Tools](guides/memory_tools.md) to customize memory storage and retrieval, and see the [hot path quickstart](https://langchain-ai.github.io/langmem/hot_path_quickstart) for a more complete example on how to include memories without the agent having to explicitly search.

The agent can now store important information from conversations, search its memory when relevant, and persist knowledge across conversations.

> [!TIP]
> For developing, debugging, and deploying AI agents and LLM applications, see [LangSmith](https://docs.langchain.com/langsmith/home).

## Next Steps

For more examples and detailed documentation:

- [Hot Path Quickstart](https://langchain-ai.github.io/langmem/hot_path_quickstart) - Learn how to let your LangGraph agent manage its own memory "in the hot path"
- [Background Quickstart](https://langchain-ai.github.io/langmem/background_quickstart) - Learn how to use a memory manager "in the background"
- [Core Concepts](https://langchain-ai.github.io/langmem/concepts/conceptual_guide) - Learn key ideas
- [API Reference](https://langchain-ai.github.io/langmem/reference) - Full function documentation
- Build RSI 🙂 

## `Makefile`

.PHONY: lint-docs format-docs build-docs serve-docs serve-clean-docs clean-docs codespell build-typedoc doctest

build-docs:
	uv run --group docs --with-editable . python -m mkdocs build --clean -f docs/mkdocs.yml --strict

serve-clean-docs: clean-docs
	uv run --group docs --with-editable . python -m mkdocs serve -c -f docs/mkdocs.yml --strict -w ./src/langmem

serve-docs: build-typedoc
	uv run --group docs --with-editable . python -m mkdocs serve -f docs/mkdocs.yml -w ./src/langmem -w README.md

## Run format against the project documentation.
format-docs:
	uv run ruff format docs/docs
	uv run ruff check --fix docs/docs

doctest:
	@echo "Starting langgraph server..."
	uvx --refresh --from "langgraph-cli[inmem]" --with-editable . --python 3.11 langgraph dev --no-browser > /dev/null 2>&1 & echo $$! > .langgraph.pid
	@echo "Waiting for server to start..."
	@sleep 2
	@echo "Running tests..."
	uv run --with-editable . python -m pytest --capture=no tests/test_docstring_examples.py -vvv -n auto $(if $(k),-k "$(k)",) || (kill `cat .langgraph.pid` && rm .langgraph.pid && exit 1)
	@echo "Cleaning up server..."
	@kill `cat .langgraph.pid` && rm .langgraph.pid

doctest-watch:
	@echo "Starting langgraph server..."
	uvx --refresh --from "langgraph-cli[inmem]" --with-editable . --python 3.11 langgraph dev --no-browser > /dev/null 2>&1 & echo $$! > .langgraph.pid
	@echo "Waiting for server to start..."
	@sleep 2
	@echo "Starting test watcher..."
	PYTHONPATH=src uv run --with-editable . ptw tests/test_docstring_examples.py -- -vvv --last-failed --new-first $(if $(k),-k='$(k)',) || (kill `cat .langgraph.pid` && rm .langgraph.pid && exit 1)
	@echo "Cleaning up server..."
	@kill `cat .langgraph.pid` && rm .langgraph.pid


format:
	uv run ruff format ./src
	uv run ruff check --fix ./src

lint:
	uv run ruff format --check ./src
	uv run ruff check ./src

# Check the docs for linting violations
lint-docs:
	uv run ruff format --check docs/docs
	uv run ruff check docs/docs

	uv run ruff format --check docs/docs
	uv run ruff check docs/docs

## `pyproject.toml`

[project]
name = "langmem"
version = "0.0.30"
description = "Prebuilt utilities for memory management and retrieval."
readme = "README.md"
requires-python = ">=3.10"
license = { file = "LICENSE" }
dependencies = [
    "langchain>=0.3.15",
    "langchain-core>=0.3.46",
    "langchain-openai>=0.3.1",
    "trustcall>=0.0.39",
    "langgraph>=0.6.0,<2",
    "langchain-anthropic>=0.3.3",
    "langsmith>=0.3.8",
    "langgraph-checkpoint>=2.0.12",
]

[project.packages]
find = { where = ["src"] }

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[dependency-groups]
dev = [
    "anyio>=4.8.0",
    "langchain-anthropic>=0.3.3",
    "langchain-openai>=0.3.1",
    "langgraph-cli[inmem]>=0.1.70",
    "pytest>=8.3.4",
    "pytest-watch>=4.2.0",
    "pytest-xdist>=3.6.1",
    "langgraph-prebuilt>=0.1.1",
    "ruff>=0.12.12",
]
docs = [
    "markdown-callouts>=0.4.0",
    "markdown-include>=0.8.1",
    "mkdocs>=1.6.1",
    "mkdocs-autorefs>=1.3.0",
    "mkdocs-exclude>=1.0.2",
    "mkdocs-git-committers-plugin-2>=2.5.0",
    "mkdocs-material>=9.6.1",
    "mkdocs-minify-plugin>=0.8.0",
    "mkdocs-redirects>=1.2.2",
    "mkdocs-rss-plugin>=1.17.1",
    "mkdocstrings>=0.27.0",
    "mkdocstrings-python>=1.13.0",
    "nbformat>=5.10.4",
    "nbconvert>=7.16.6",
]

[tool.uv.workspace]
members = ["evals/gen"]

[tool.ruff]
lint.select = ["E", "F", "I", "TID251"]
lint.ignore = ["E501"]
line-length = 88
indent-width = 4
extend-include = ["*.ipynb"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"
docstring-code-format = true
docstring-code-line-length = "dynamic"

[tool.ruff.lint.flake8-tidy-imports.banned-api]
"typing.TypedDict".msg = "Use typing_extensions.TypedDict instead."

[tool.hatch.build]
exclude = [
    "tests/",
    "docs/",
    ".github/",
    "examples.py",
    "examples/",
    ".editorconfig",
    "db/",
    "evals/",
    ".langgraph_api",
    "*.ipynb",
    ".python-version",
    ".editorconfig",
    ".venv*/**",
    "pytest.ini",
]

## `docs/README.md`

# Setup

To setup requirements for building docs you can run:

```bash
poetry install --with test
```

## Serving documentation locally

To run the documentation server locally you can run:

```bash
make serve-docs
```

## Execute notebooks

If you would like to automatically execute all of the notebooks, to mimic the "Run notebooks" GHA, you can run:

```bash
python docs/_scripts/prepare_notebooks_for_ci.py
./docs/_scripts/execute_notebooks.sh
```

**Note**: if you want to run the notebooks without `%pip install` cells, you can run:

```bash
python docs/_scripts/prepare_notebooks_for_ci.py --comment-install-cells
./docs/_scripts/execute_notebooks.sh
```

`prepare_notebooks_for_ci.py` script will add VCR cassette context manager for each cell in the notebook, so that:
* when the notebook is run for the first time, cells with network requests will be recorded to a VCR cassette file
* when the notebook is run subsequently, the cells with network requests will be replayed from the cassettes

**Note**: this is currently limited only to the notebooks in `docs/docs/how-tos`

## Adding new notebooks

If you are adding a notebook with API requests, it's **recommended** to record network requests so that they can be subsequently replayed. If this is not done, the notebook runner will make API requests every time the notebook is run, which can be costly and slow.

To record network requests, please make sure to first run `prepare_notebooks_for_ci.py` script.

Then, run

```bash
jupyter execute <path_to_notebook>
```

Once the notebook is executed, you should see the new VCR cassettes recorded in `docs/cassettes` directory and discard the updated notebook.

## Updating existing notebooks

If you are updating an existing notebook, please make sure to remove any existing cassettes for the notebook in `docs/cassettes` directory (each cassette is prefixed with the notebook name), and then run the steps from the "Adding new notebooks" section above.

To delete cassettes for a notebook, you can run:

```bash
rm docs/cassettes/<notebook_name>*
```

# Repository semantic capsule: aiidateam/aiida-core

- Commit: `e4d99200ab68fc86f84bc1f275856bc7dd640f56`
- Default branch: `main`
- Description: AiiDA Core
- Selected evidence files: 4 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

# <img src="https://raw.githubusercontent.com/aiidateam/aiida-core/main/docs/source/images/aiida-logo.svg" alt="AiiDA" width="200"/>

AiiDA (www.aiida.net) is a workflow manager for computational science with a strong focus on provenance, performance and extensibility.

|    | |
|-----|----------------------------------------------------------------------------|
|Latest release| [![PyPI version](https://badge.fury.io/py/aiida-core.svg)](https://badge.fury.io/py/aiida-core) [![conda-forge](https://img.shields.io/conda/vn/conda-forge/aiida-core.svg?style=flat)](https://anaconda.org/conda-forge/aiida-core) [![PyPI pyversions](https://img.shields.io/pypi/pyversions/aiida-core.svg)](https://pypi.python.org/pypi/aiida-core/) |
|Getting help| [![Docs status](https://readthedocs.org/projects/aiida-core/badge)](http://aiida-core.readthedocs.io/) [![Discourse status](https://img.shields.io/discourse/status?server=https%3A%2F%2Faiida.discourse.group%2F)](https://aiida.discourse.group/)
|Build status| [![Build Status](https://github.com/aiidateam/aiida-core/actions/workflows/ci-code.yml/badge.svg)](https://github.com/aiidateam/aiida-core/actions) [![Coverage Status](https://codecov.io/gh/aiidateam/aiida-core/branch/main/graph/badge.svg)](https://codecov.io/gh/aiidateam/aiida-core) [Benchmarks](https://aiidateam.github.io/aiida-core/dev/bench/ubuntu-22.04/psql_dos/) |
|Activity| [![PyPI-downloads](https://img.shields.io/pypi/dm/aiida-core.svg?style=flat)](https://pypistats.org/packages/aiida-core) [![Commit Activity](https://img.shields.io/github/commit-activity/m/aiidateam/aiida-core.svg)](https://github.com/aiidateam/aiida-core/pulse)
|Community|  [![Discourse](https://img.shields.io/discourse/topics?server=https%3A%2F%2Faiida.discourse.group%2F&logo=discourse)](https://aiida.discourse.group/) [![Affiliated with NumFOCUS](https://img.shields.io/badge/NumFOCUS-affiliated%20project-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](https://numfocus.org/sponsored-projects/affiliated-projects) [![Twitter](https://img.shields.io/twitter/follow/aiidateam.svg?style=social&label=Follow)](https://twitter.com/aiidateam)


## Features

 -   **Workflows:** Write complex, auto-documenting workflows in
     python, linked to arbitrary executables on local and remote
     computers. The event-based workflow engine supports tens of
     thousands of processes per hour with full checkpointing.
 -   **Data provenance:** Automatically track inputs, outputs & metadata
     of all calculations in a provenance graph for full
     reproducibility. Perform fast queries on graphs containing
     millions of nodes.
 -   **HPC interface:** Move your calculations to a different computer
     by changing one line of code. AiiDA is compatible with schedulers
     like [SLURM](https://slurm.schedmd.com), [PBS
     Pro](https://www.pbspro.org/),
     [torque](http://www.adaptivecomputing.com/products/torque/),
     [SGE](http://gridscheduler.sourceforge.net/) or
     [LSF](https://www.ibm.com/support/knowledgecenter/SSETD4/product_welcome_platform_lsf.html)
     out of the box.
 -   **Plugin interface:** Extend AiiDA with [plugins](https://aiidateam.github.io/aiida-registry/) for new simulation codes (input generation & parsing), data types, schedulers, transport modes and more.
 -   **Open Science:** Export subsets of your provenance graph and share them with peers or make them available online for everyone
     on the [Materials Cloud](https://www.materialscloud.org).
 -   **Open source:** AiiDA is released under the [MIT open source license](LICENSE.txt)

## Installation

Please see AiiDA's [documentation](https://aiida-core.readthedocs.io/en/latest/).
**Warning:** Do not use AiiDA directly from the GitHub `main` branch. It changes rapidly and may put your AiiDA storage in an unrecoverable state.

## How to contribute [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub issues by-label](https://img.shields.io/github/issues/aiidateam/aiida-core/good%20first%20issue)](https://github.com/aiidateam/aiida-core/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)

The AiiDA team appreciates help from a wide range of different backgrounds.
Small improvements of the documentation or minor bug fixes are always welcome.

Please see the [Contributor wiki](https://github.com/aiidateam/aiida-core/wiki) on how to get started.

## Frequently Asked Questions

If you are experiencing problems with your AiiDA installation, please refer to the [FAQ page of the documentation](https://aiida-core.readthedocs.io/en/latest/howto/faq.html).
For any other questions, discussion and requests for support, please visit the [Discourse server](https://aiida.discourse.group/).

## How to cite

If you use AiiDA in your research, please consider citing the following publications:

 * S. P. Huber *et al.*, *AiiDA 1.0, a scalable computational infrastructure for automated reproducible workflows and data provenance*, Scientific Data **7**, 300 (2020); DOI: [10.1038/s41597-020-00638-4](https://doi.org/10.1038/s41597-020-00638-4)
 * M. Uhrin *et al.*, *Workflows in AiiDA: Engineering a high-throughput, event-based engine for robust and modular computational workflows*, Computational Materials Science **187**, 110086 (2021); DOI: [10.1016/j.commatsci.2020.110086](https://doi.org/10.1016/j.commatsci.2020.110086)

If the ADES concepts are referenced, please also cite:

* Giovanni Pizzi, Andrea Cepellotti, Riccardo Sabatini, Nicola Marzari,and Boris Kozinsky, *AiiDA: automated interactive infrastructure and database for computational science*, Computational Materials Science **111**, 218-230 (2016); DOI: [10.1016/j.commatsci.2015.09.013](https://doi.org/10.1016/j.commatsci.2015.09.013)

## License

AiiDA is distributed under the MIT open source license (see [`LICENSE.txt`](LICENSE.txt)).
For a list of other open source components included in AiiDA, see [`open_source_licenses.txt`](open_source_licenses.txt).

## Acknowledgements

AiiDA is a [NumFOCUS Affiliated Project](https://www.numfocus.org) and supported by the [MARVEL National Centre of Competence in Research](http://www.marvel-nccr.ch), the [MaX European Centre of Excellence](http://www.max-centre.eu) and by a number of other supporting projects, partners and institutions, whose complete list is available on the [AiiDA website acknowledgements page](http://www.aiida.net/acknowledgements/).

## `AGENTS.md`

# AGENTS.md - AI Coding Assistant Guide for AiiDA Core

This file provides context for AI coding assistants (Claude Code, GitHub Copilot, etc.) working on the `aiida-core` codebase.

**IMPORTANT**: Always use the project's tooling. Use `uv run` to run Python, tests, and tools (e.g., `uv run pytest`, `uv run pre-commit`). Never use bare `python` or `pip`. Check `pyproject.toml` and `.pre-commit-config.yaml` for the full configuration.

## Project overview

AiiDA is a workflow manager for computational science with a strong focus on provenance, performance, and extensibility.
It is written in Python (see `pyproject.toml` for supported versions) and uses PostgreSQL/SQLite for metadata storage, [`disk-objectstore`](https://github.com/aiidateam/disk-objectstore) for file storage, and RabbitMQ as a message broker.

## Key design concepts

- **Provenance:** all data and computations are tracked as nodes in a directed acyclic graph (DAG). Nodes are immutable once stored, except extras (always mutable) and `ProcessNode._updatable_attributes` (process state, exit status, checkpoint, etc., mutable until `seal()`).
- **Process/Node duality:** processes (`CalcJob`, `WorkChain`, `calcfunction`, `workfunction`) define *how* to run; process nodes record *that* something ran.
- **CREATE vs RETURN links:** calculations *create* new data nodes; workflows *return* existing data nodes. Workflows orchestrate but don't create data themselves.
- **Don't break provenance:** never circumvent the link system or modify stored nodes in ways that would break the DAG.
- **Public API:** anything importable from a second-level package (e.g., `from aiida.orm import ...`) is public API with deprecation guarantees. Deeper internal modules may change without notice.
- **Plugin system:** entry points (`pyproject.toml` `[project.entry-points]`) allow extending AiiDA with new calculation types, data types, schedulers, transports, and storage backends.
- **Daemon signal handling:** the daemon captures `SIGINT`/`SIGTERM` for graceful shutdown. Subprocesses in daemon code must pass `start_new_session=True`.

### Process / Node duality

Each process class has a corresponding node class that records its execution:

| Process class | Node class | Link types |
|--------------|------------|------------|
| `@calcfunction` | `CalcFunctionNode` | INPUT_CALC → CREATE |
| `CalcJob` | `CalcJobNode` | INPUT_CALC → CREATE |
| `@workfunction` | `WorkFunctionNode` | INPUT_WORK → RETURN/CALL |
| `WorkChain` | `WorkChainNode` | INPUT_WORK → RETURN/CALL |

## Code style

Code style is enforced via **pre-commit hooks** (`.pre-commit-config.yaml`). Always run `uv run pre-commit` before pushing.
Formatting: `ruff`. Type checking: `mypy`. Write new code following ruff conventions with proper type hints.
Typing is progressively strict: modules listed under `[[tool.mypy.overrides]]` in `pyproject.toml` require full annotations, and a module joins that list once it is fully typed.
Docstrings: Sphinx-style (`:param:`, `:return:`, `:raises:`) required for public API, types in annotations not docstrings.
Comments and docstrings explain *why*, not *what*.
New source files should include the standard copyright header (copy from any existing `.py` file).
In `cmdline/`: delay `aiida` imports to function level (keeps `verdi` CLI responsive, see the `adding-a-cli-command` skill).
See the `linting-and-ci` skill for details.

### Error handling

Use `aiida.common.exceptions` for AiiDA-specific exceptions, `aiida.common.warnings` for non-fatal issues.
Assign exception messages to a variable before raising: `msg = f'...'; raise TypeError(msg)`

## Design principles

Useful frameworks:

- **SOLID:** single responsibility, open/closed, Liskov, interface segregation, dependency inversion.
- **GRASP:** assign each responsibility to the class that already holds the information; low coupling, high cohesion.
- **CUPID:** composable, does one thing well, predictable, idiomatic, domain-based.

Design patterns are deliberately not listed here.
Where a problem genuinely calls for one, fetch [refactoring.guru/design-patterns](https://refactoring.guru/design-patterns) and work from it rather than from memory.
Don't force code into a pattern it does not need.

### Heuristics

- **Reuse what exists:** search the codebase before writing a helper, and call `super()` rather than restating base-class logic.
- **YAGNI:** build what is needed now, not what might be needed later.
- **Redesign rather than document:** logic needing a paragraph of comments to follow is too complex.
- **Chesterton's fence:** don't remove or rewrite code whose purpose you haven't established.
- **Changing observable behaviour is a breaking change** (Hyrum's law), even where the signature stays the same.
- **DRY, but rule of three:** duplication is cheaper than the wrong abstraction, so wait for the third occurrence.
- **Principle of least astonishment:** where two designs are defensible, pick the one the name already implies.

### API design

- **Flat over nested:** re-export at package level. File layout is an implementation detail.
- **Keep dependencies acyclic:** needing a function-level import to break a runtime cycle means the layering is wrong.
- **Don't repeat context in names:** `kpoints.set_mesh()`, not `kpoints.set_kpoints_mesh()`.
- **Keyword-only (`*`) arguments** for several or same-typed parameters, and always for booleans.
- **Progressive disclosure:** simple things simple, complex things possible. Don't front-load complexity.
- **Pit of success:** safe defaults, unsafe behaviour behind explicit opt-in. Make wrong code look wrong.
- **Permissive at the boundary, strict inside:** parse messy external input at the edge; internal code passes domain types, not generic containers.
- **Fail fast:** reject bad input where it enters, naming the offending value.
- **Prefer pure functions:** no side effects, no mutation of inputs, same output for the same arguments.
- **Minimize mutable state:** return new values over mutating inputs, and a copy or read-only view over an alias to your own container.
- **No global mutable state:** keyword arguments with defaults, state on a class instance, or `ContextVar`.
- **Raise exceptions rather than signalling failure with `None` or a sentinel;** status values are for failures that must persist or cross a process boundary.
- **Context managers** for acquire/release and setup/teardown, since cleanup the caller must remember gets skipped.

### Object-oriented design

- **Composition over inheritance:** delegate to a collaborator; inheritance means is-a, and using it to share code risks coupling conceptually unrelated classes.
- **Depend on abstractions:** shape the interface around what callers need, so it does not simply mirror one concrete implementation.
- **Prefer `Protocol`,** where no inheritance should be imposed; use an **ABC** when the contract needs runtime enforcement or shared base behaviour.
- **Liskov substitution:** never narrow a parameter type in a subclass override, and mark overrides with `@override`.
- **Encapsulate:** needing another object's underscore-prefixed members means the API is missing something.
- **Adapt at the boundary:** conversion into our abstractions belongs on the incoming type or in a dedicated adapter, not spread through the consuming code.
- **Command-query separation:** a method either does something or answers something, not both.
- **Law of Demeter:** talk to immediate collaborators, since `a.b.c.d()` couples the caller to the whole chain.
- **Overload an operator** only when a reader can predict what it does from the types involved.
- **Keep attribute access cheap:** attribute syntax reads as free, so an expensive lookup belongs behind a method or a `cached_property`.

### Types

- **Annotate as you write:** a suspiciously broad return type signals a missing abstraction.
- **The signature is the contract:** types and names alone should convey what to pass and what comes back.
- **Avoid `Any`:** it is contagious, and unlike `type: ignore` it leaves no marker that a decision was made.
- **Every `type: ignore` is a decision:** fix the design or record the debt.
- **Make illegal states unrepresentable:** a type should admit exactly the valid values and nothing more, so invalid states and calls cannot be written.
- **`TypedDict`/`dataclass` over plain dicts:** a dict key typo is silent; a field name typo is a type error.
- **`Literal`/`Enum` over bare strings** for constrained value sets. `assert_never` for exhaustiveness.
- **Sensible default values over `None` as a default,** where one exists: `None` hides the real default and widens the type for every caller.
- **Postel's law:** accept broad types (`Sequence`, `Mapping`), return narrow ones (`list`, `dict`).
- **`TypeAlias`** to name any complex type that appears more than once.
- **Generics (`TypeVar`)** to carry type information across function boundaries.
- **`@overload`** to narrow return types statically, **`@singledispatch`** over `isinstance` chains.
- **`Final`** for constants, **`@final`** for classes that must not be subclassed.
- **`TypeGuard`/`TypeIs`** for narrowing in validation functions, **`Self`** for fluent APIs, **`ParamSpec`** to carry signatures through decorators.
- **A type that is hard to write** is a sign the design needs work, not that the annotation needs loosening.

### Python idioms

- **Guard clauses** over deep nesting: edge case first, main path at low indentation.
- **`is None` / `is not None`** over truthiness for optionals, and `isinstance()` rather than `type()`.
- **No mutable default arguments:** default `None`, assign in the body.
- **Modern stdlib idioms:** `pathlib.Path` over `os.path`, f-strings over `.format()`/`%`.
- **Catch specific exceptions,** never bare `except:`, which swallows `KeyboardInterrupt` and `SystemExit`, nor blanket `except Exception:`, which hides genuine bugs.
- **`contextlib.suppress(...)`** over `except ...: pass`.
- **Preserve the cause when re-raising:** `raise ValueError(msg) from err`.
- **Comprehensions** over `map`/`filter` with lambdas, and `itertools` and generators over large materialized lists.
- **Let the container do the work:** `defaultdict`, `Counter`, `deque`, `dict.get(key, default)` over hand-written equivalents.
- **`functools.cached_property` / `lru_cache`** for expensive computed values.
- **Timezone-aware datetimes:** `datetime.now(tz=timezone.utc)`, never naive `datetime.now()`.
- **Monotonic clocks for measuring elapsed time:** use `time.monotonic()` or `time.monotonic_ns()`, never wall-clock time.
- **Never call blocking I/O from async code:** it stalls every other task on that event loop, and in the daemon every AiiDA process the worker is running. Use an async API, or offload the blocking work explicitly.

## Claude Code skills

The following Claude Code skills (under `.claude/skills/`) provide task-specific guidance. Listed here as a reference for all agents:

- `adding-a-cli-command`: `verdi` subcommands and import-time constraints
- `adding-dependencies`: third-party dependency checklist
- `architecture-overview`: codebase structure, key files, ABCs
- `commit-conventions`: branching, commit style, PR requirements
- `debugging-processes`: diagnosing failed or stuck processes and the daemon
- `deprecating-api`: deprecation warnings and removal timeline
- `linting-and-ci`: pre-commit, CI checks
- `running-tests`: pytest cheatsheet, plugins, fixtures
- `writing-and-building-docs`: documentation style and building
- `writing-tests`: test philosophy, markers, parametrization

## AI assistant guidelines

When working on this codebase:

- **Read before writing**: Always read existing code and understand patterns before proposing changes.
  Don't guess how AiiDA works.
- **Match existing style**: Follow patterns you see in surrounding code.
- **Don't modify code you weren't asked to change**: If fixing a bug in function A, don't also "improve" functions B and C nearby.
- **Don't add docstrings/type hints to unchanged code**: Only add to code you're actively modifying.

## Key dependencies

Key dependencies (all under [github.com/aiidateam](https://github.com/aiidateam)): `plumpy` (process state machine), `kiwipy` (message broker interface), `disk-objectstore` (file storage).

## `CLAUDE.md`

@AGENTS.md

## `pyproject.toml`

[build-system]
build-backend = 'flit_core.buildapi'
requires = ["flit_core >=4.0.2,<5"]

# The "dev" dependency group is automatically synced by uv
# and should thus contain all necessary deps for local development.
[dependency-groups]
dev = [
  "aiida-core[atomic_tools,rest,tests,pre-commit,tests,docs]"
]

[project]
authors = [{name = 'The AiiDA team', email = 'developers@aiida.net'}]
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Framework :: AiiDA',
  'License :: OSI Approved :: MIT License',
  'Operating System :: POSIX :: Linux',
  'Operating System :: MacOS :: MacOS X',
  'Programming Language :: Python',
  'Programming Language :: Python :: 3.10',
  'Programming Language :: Python :: 3.11',
  'Programming Language :: Python :: 3.12',
  'Programming Language :: Python :: 3.13',
  'Programming Language :: Python :: 3.14',
  'Topic :: Scientific/Engineering'
]
# NOTE: When updating versions of some packages, such as requests or paramiko,
# you need to also update the versions of corresponding stub packages
# in the 'pre-commit' group e.g. 'types-requests'
dependencies = [
  'aio-pika~=9.5.0',
  'alembic~=1.8',
  'archive-path~=0.4.2',
  "asyncssh~=2.22.0",
  'circus~=0.19.0',
  'click-spinner~=0.1.8',
  'click>=8.1.0,<8.3',
  'dill>=0.3.6,<1',
  'disk-objectstore~=1.5.0',
  'docstring-parser',
  'graphviz~=0.19',
  'greenback~=1.0',
  'greenlet>=3.2.4',
  'importlib-metadata~=6.0',
  'ipython>=7.6',
  'jedi<0.19',
  'jinja2~=3.0',
  'numpy>=1.21,<3',
  'pamqp~=3.2',
  'paramiko~=3.0',
  'pytray>=0.3.4,<0.4.0',
  'pgsu~=0.3.0',
  'psutil~=7.0',
  'psycopg[binary]>=3.0.2,<4',
  'pydantic~=2.12',
  'pytz~=2021.1',
  'pyyaml~=6.0',
  'requests~=2.0',
  'shortuuid',
  'sqlalchemy>=2.0.20,<3',
  'tabulate>=0.9.0,<0.10.0',
  'tqdm~=4.45',
  'typing-extensions~=4.13',
  'upf_to_json~=0.9.2',
  'wrapt~=1.11',
  'chardet~=5.2.0;platform_system=="Windows"'
]
description = 'AiiDA is a workflow manager for computational science with a strong focus on provenance, performance and extensibility.'
dynamic = ['version']  # read from aiida/__init__.py
keywords = ['aiida', 'workflows']
license = {file = 'LICENSE.txt'}
name = 'aiida-core'
readme = 'README.md'
requires-python = '>=3.10'

[project.entry-points.'aiida.brokers']
'core.rabbitmq' = 'aiida.brokers.rabbitmq.broker:RabbitmqBroker'
'core.zeromq' = 'aiida.brokers.zeromq.broker:ZeromqBroker'

[project.entry-points.'aiida.calculations']
'core.arithmetic.add' = 'aiida.calculations.arithmetic.add:ArithmeticAddCalculation'
'core.shell' = 'aiida.calculations.shell:ShellJob'
'core.stash' = 'aiida.calculations.stash:StashCalculation'
'core.templatereplacer' = 'aiida.calculations.templatereplacer:TemplatereplacerCalculation'
'core.transfer' = 'aiida.calculations.transfer:TransferCalculation'
'core.unstash' = 'aiida.calculations.unstash:UnstashCalculation'

[project.entry-points.'aiida.calculations.importers']
'core.arithmetic.add' = 'aiida.calculations.importers.arithmetic.add:ArithmeticAddCalculationImporter'

[project.entry-points.'aiida.calculations.monitors']
'core.always_kill' = 'aiida.calculations.monitors.base:always_kill'

[project.entry-points.'aiida.cmdline.computer.configure']
'core.local' = 'aiida.transports.plugins.local:CONFIGURE_LOCAL_CMD'
'core.ssh' = 'aiida.transports.plugins.ssh:CONFIGURE_SSH_CMD'

[project.entry-points.'aiida.cmdline.data']
'core.array' = 'aiida.cmdline.commands.cmd_data.cmd_array:array'
'core.bands' = 'aiida.cmdline.commands.cmd_data.cmd_bands:bands'
'core.cif' = 'aiida.cmdline.commands.cmd_data.cmd_cif:cif'
'core.dict' = 'aiida.cmdline.commands.cmd_data.cmd_dict:dictionary'
'core.remote' = 'aiida.cmdline.commands.cmd_data.cmd_remote:remote'
'core.singlefile' = 'aiida.cmdline.commands.cmd_data.cmd_singlefile:singlefile'
'core.structure' = 'aiida.cmdline.commands.cmd_data.cmd_structure:structure'
'core.trajectory' = 'aiida.cmdline.commands.cmd_data.cmd_trajectory:trajectory'
'core.upf' = 'aiida.cmdline.commands.cmd_data.cmd_upf:upf'

[project.entry-points.'aiida.cmdline.data.structure.import']

[project.entry-points.'aiida.data']
'core.array' = 'aiida.orm.nodes.data.array.array:ArrayData'
'core.array.bands' = 'aiida.orm.nodes.data.array.bands:BandsData'
'core.array.kpoints' = 'aiida.orm.nodes.data.array.kpoints:KpointsData'
'core.array.projection' = 'aiida.orm.nodes.data.array.projection:ProjectionData'
'core.array.trajectory' = 'aiida.orm.nodes.data.array.trajectory:TrajectoryData'
'core.array.xy' = 'aiida.orm.nodes.data.array.xy:XyData'
'core.base' = 'aiida.orm.nodes.data:BaseType'
'core.bool' = 'aiida.orm.nodes.data.bool:Bool'
'core.cif' = 'aiida.orm.nodes.data.cif:CifData'
'core.code' = 'aiida.orm.nodes.data.code.legacy:Code'
'core.code.abstract' = 'aiida.orm.nodes.data.code.abstract:AbstractCode'
'core.code.containerized' = 'aiida.orm.nodes.data.code.containerized:ContainerizedCode'
'core.code.installed' = 'aiida.orm.nodes.data.code.installed:InstalledCode'
'core.code.installed.shell' = 'aiida.orm.nodes.data.code.shell:ShellCode'
'core.code.portable' = 'aiida.orm.nodes.data.code.portable:PortableCode'
'core.dict' = 'aiida.orm.nodes.data.dict:Dict'
'core.entry_point' = 'aiida.orm.nodes.data.entry_point:EntryPointData'
'core.enum' = 'aiida.orm.nodes.data.enum:EnumData'
'core.float' = 'aiida.orm.nodes.data.float:Float'
'core.folder' = 'aiida.orm.nodes.data.folder:FolderData'
'core.int' = 'aiida.orm.nodes.data.int:Int'
'core.jsonable' = 'aiida.orm.nodes.data.jsonable:JsonableData'
'core.list' = 'aiida.orm.nodes.data.list:List'
'core.numeric' = 'aiida.orm.nodes.data.numeric:NumericType'
'core.orbital' = 'aiida.orm.nodes.data.orbital:OrbitalData'
'core.pickled' = 'aiida.orm.nodes.data.pickled:PickledData'
'core.remote' = 'aiida.orm.nodes.data.remote.base:RemoteData'
'core.remote.stash' = 'aiida.orm.nodes.data.remote.stash.base:RemoteStashData'
'core.remote.stash.compress' = 'aiida.orm.nodes.data.remote.stash.compress:RemoteStashCompressedData'
'core.remote.stash.custom' = 'aiida.orm.nodes.data.remote.stash.custom:RemoteStashCustomData'
'core.remote.stash.folder' = 'aiida.orm.nodes.data.remote.stash.folder:RemoteStashFolderData'
'core.singlefile' = 'aiida.orm.nodes.data.singlefile:SinglefileData'
'core.str' = 'aiida.orm.nodes.data.str:Str'
'core.structure' = 'aiida.orm.nodes.data.structure:StructureData'
'core.upf' = 'aiida.orm.nodes.data.upf:UpfData'

[project.entry-points.'aiida.groups']
'core' = 'aiida.orm.groups:Group'
'core.auto' = 'aiida.orm.groups:AutoGroup'
'core.import' = 'aiida.orm.groups:ImportGroup'
'core.upf' = 'aiida.orm.groups:UpfFamily'

[project.entry-points.'aiida.node']
'data' = 'aiida.orm.nodes.data.data:Data'
'process' = 'aiida.orm.nodes.process.process:ProcessNode'
'process.calculation' = 'aiida.orm.nodes.process.calculation.calculation:CalculationNode'
'process.calculation.calcfunction' = 'aiida.orm.nodes.process.calculation.calcfunction:CalcFunctionNode'
'process.calculation.calcjob' = 'aiida.orm.nodes.process.calculation.calcjob:CalcJobNode'
'process.workflow' = 'aiida.orm.nodes.process.workflow.workflow:WorkflowNode'
'process.workflow.workchain' = 'aiida.orm.nodes.process.workflow.workchain:WorkChainNode'
'process.workflow.workfunction' = 'aiida.orm.nodes.process.workflow.workfunction:WorkFunctionNode'

[project.entry-points.'aiida.orm']
'core.auth_info' = 'aiida.orm.authinfos:AuthInfo'
'core.comment' = 'aiida.orm.comments:Comment'
'core.computer' = 'aiida.orm.computers:Computer'
'core.data' = 'aiida.orm.nodes.data.data:Data'
'core.entity' = 'aiida.orm.entities:Entity'
'core.group' = 'aiida.orm.groups:Group'
'core.log' = 'aiida.orm.logs:Log'
'core.node' = 'aiida.orm.nodes.node:Node'
'core.user' = 'aiida.orm.users:User'

[project.entry-points.'aiida.parsers']
'core.arithmetic.add' = 'aiida.parsers.plugins.arithmetic.add:ArithmeticAddParser'
'core.shell' = 'aiida.parsers.plugins.shell.parser:ShellParser'
'core.templatereplacer' = 'aiida.parsers.plugins.templatereplacer.parser:TemplatereplacerParser'

[project.entry-points.'aiida.schedulers']
'core.direct' = 'aiida.schedulers.plugins.direct:DirectScheduler'
'core.lsf' = 'aiida.schedulers.plugins.lsf:LsfScheduler'
'core.pbspro' = 'aiida.schedulers.plugins.pbspro:PbsproScheduler'
'core.sge' = 'aiida.schedulers.plugins.sge:SgeScheduler'
'core.slurm' = 'aiida.schedulers.plugins.slurm:SlurmScheduler'
'core.torque' = 'aiida.schedulers.plugins.torque:TorqueScheduler'

[project.entry-points.'aiida.storage']
'core.psql_dos' = 'aiida.storage.psql_dos.backend:PsqlDosBackend'
'core.sqlite_dos' = 'aiida.storage.sqlite_dos.backend:SqliteDosStorage'
'core.sqlite_temp' = 'aiida.storage.sqlite_temp.backend:SqliteTempBackend'
'core.sqlite_zip' = 'aiida.storage.sqlite_zip.backend:SqliteZipBackend'

[project.entry-points.'aiida.tools.calculations']

[project.entry-points.'aiida.tools.data.orbitals']
'core.orbital' = 'aiida.tools.data.orbital.orbital:Orbital'
'core.realhydrogen' = 'aiida.tools.data.orbital.realhydrogen:RealhydrogenOrbital'

[project.entry-points.'aiida.tools.dbexporters']

[project.entry-points.'aiida.tools.dbimporters']
'core.cod' = 'aiida.tools.dbimporters.plugins.cod:CodDbImporter'
'core.icsd' = 'aiida.tools.dbimporters.plugins.icsd:IcsdDbImporter'
'core.materialsproject' = 'aiida.tools.dbimporters.plugins.materialsproject:MaterialsProjectImporter'
'core.mpds' = 'aiida.tools.dbimporters.plugins.mpds:MpdsDbImporter'
'core.mpod' = 'aiida.tools.dbimporters.plugins.mpod:MpodDbImporter'
'core.nninc' = 'aiida.tools.dbimporters.plugins.nninc:NnincDbImporter'
'core.oqmd' = 'aiida.tools.dbimporters.plugins.oqmd:OqmdDbImporter'
'core.pcod' = 'aiida.tools.dbimporters.plugins.pcod:PcodDbImporter'
'core.tcod' = 'aiida.tools.dbimporters.plugins.tcod:TcodDbImporter'

[project.entry-points.'aiida.tools.workflows']

[project.entry-points.'aiida.transports']
'core.local' = 'aiida.transports.plugins.local:LocalTransport'
'core.ssh' = 'aiida.transports.plugins.ssh:SshTransport'
'core.ssh_async' = 'aiida.transports.plugins.ssh_async:AsyncSshTransport'


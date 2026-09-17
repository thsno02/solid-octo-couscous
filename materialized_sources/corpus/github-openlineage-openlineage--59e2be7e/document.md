# Repository semantic capsule: OpenLineage/OpenLineage

- Commit: `9ac19298c8ef518ed10c7a3af547c8ac86c2e012`
- Default branch: `main`
- Description: OpenLineage
- Selected evidence files: 5 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

[![CircleCI](https://circleci.com/gh/OpenLineage/OpenLineage/tree/main.svg?style=shield)](https://circleci.com/gh/OpenLineage/OpenLineage/tree/main)
[![status](https://img.shields.io/badge/status-active-brightgreen.svg)](#status)
[![Slack](https://img.shields.io/badge/slack-chat-blue.svg)](https://join.slack.com/t/openlineage/shared_invite/zt-3arpql6lg-Nt~hicnDsnDY_GK_LEX06w)
[![license](https://img.shields.io/badge/license-Apache_2.0-blue.svg)](https://github.com/OpenLineage/OpenLineage/blob/main/LICENSE)
[![maven](https://img.shields.io/maven-central/v/io.openlineage/openlineage-java.svg)](https://search.maven.org/search?q=g:io.openlineage)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/4888/badge)](https://bestpractices.coreinfrastructure.org/projects/4888)

<div align="center">
  <img src="./doc/openlineage-lfai-logo.png" width="754px"/>
</div>

## Overview
OpenLineage is an Open standard for metadata and lineage collection designed to instrument jobs as they are running.
It defines a generic model of run, job, and dataset entities identified using consistent naming strategies.
The core lineage model is extensible by defining specific facets to enrich those entities.

OpenLineage is an [LF AI & Data Foundation](https://lfaidata.foundation/projects/openlineage) Graduate project under active development, and we welcome contributions.

## Problem

### Before

- Duplication of effort: each project has to instrument all jobs
- Integrations are external and can break with new versions

![Before OpenLineage](doc/before-ol.svg)

### With OpenLineage

- The effort of integration is shared
- An integration can be pushed in each project: no need to play catch up

![With OpenLineage](doc/with-ol.svg)

## Scope
OpenLineage defines the metadata for running jobs and the corresponding events.
A configurable backend allows the user to choose what protocol to send the events to.
 ![Scope](doc/scope.svg)

## Core model

 ![Model](doc/datamodel.svg)

 A facet is an atomic piece of metadata attached to one of the core entities.
 See the spec for more details.

## Spec
The [specification](spec/OpenLineage.md) is defined using OpenAPI and allows extension through custom facets.

## Integrations

OpenLineage supports integrations with Spark, Airflow, dbt, Flink, and more. For the most up-to-date and complete list of supported integrations, their capabilities, and matrices, please refer to the official [OpenLineage Integrations Documentation](https://openlineage.io/docs/integrations/).

## Related projects
- [Marquez](https://marquezproject.ai/): Marquez is an [LF AI & DATA](https://lfaidata.foundation/) project to collect, aggregate, and visualize a data ecosystem's metadata. It is the reference implementation of the OpenLineage API.
  - [OpenLineage collection implementation](https://github.com/MarquezProject/marquez/blob/main/api/src/main/java/marquez/api/OpenLineageResource.java)
- [Egeria](https://egeria.odpi.org/): Egeria offers open metadata and governance for enterprises - automatically capturing, managing and exchanging metadata between tools and platforms, no matter the vendor.

## Community
- Website: [openlineage.io](http://openlineage.io)
- Slack: [OpenLineage.slack.com](https://join.slack.com/t/openlineage/shared_invite/zt-3arpql6lg-Nt~hicnDsnDY_GK_LEX06w)
- Twitter: [@OpenLineage](https://twitter.com/OpenLineage)
- Mailing list: [openlineage-tsc](https://lists.lfaidata.foundation/g/openlineage-tsc)
- Wiki: [OpenLineage+Home](https://wiki.lfaidata.foundation/display/OpenLineage/OpenLineage+Home)
- LinkedIn: [13927795](https://www.linkedin.com/groups/13927795/)
- YouTube: [channel](https://www.youtube.com/channel/UCRMLy4AaSw_ka-gNV9nl7VQ)
- Mastodon: [@openlineage@fostodon.org](openlineage@fosstodon.org)

## Talks
- [Flink Forward, October 2024. Data Lineage for Apache Flink with OpenLineage](https://www.flink-forward.org/berlin-2024/agenda#data-lineage-for-apache-flink-with-openlineage)
- [Airflow Summit, September 2024. Activating operational metadata with Airflow, Atlan and OpenLineage](https://airflowsummit.org/sessions/2024/activating-operational-metadata-with-airflow-atlan-and-openlineage/)
- [Kafka Summit, March 2024. OpenLineage for Stream Processing](https://www.confluent.io/events/kafka-summit-london-2024/openlineage-for-stream-processing/)
- [Data Council Austin, March 2024. Data Lineage: We've Come a Long Way](https://www.youtube.com/watch?v=OE1o4D_iWfw)
- [Data+AI Summit June 2023. Cross-Platform Data Lineage with OpenLineage](https://www.databricks.com/dataaisummit/session/cross-platform-data-lineage-openlineage/)
- [Berlin Buzzwords, June 2023. Column-Level Lineage is Coming to the Rescue](https://youtu.be/xFVSZCCbZlY)
- [Berlin Buzzwords, June 2022. Cross-Platform Data Lineage with OpenLineage](https://www.youtube.com/watch?v=pLBVGIPuwEo)
- [Berlin Buzzwords, June 2021. Observability for Data Pipelines with OpenLineage](https://2021.berlinbuzzwords.de/member/julien-le-dem)
- [Data Driven NYC, February 2021. Data Observability and Pipelines: OpenLineage and Marquez](https://mattturck.com/datakin/)
- [Big Data Technology Warsaw Summit, February 2021. Data lineage and Observability with Marquez and OpenLineage](https://bigdatatechwarsaw.eu/edition-2021/)
- [Metadata Day 2020. OpenLineage Lightning Talk](https://www.youtube.com/watch?v=anlV5Er_BpM)
- [Open Core Summit 2020. Observability for Data Pipelines: OpenLineage Project Launch](https://www.coss.community/coss/ocs-2020-breakout-julien-le-dem-3eh4)

## Contributing

See [CONTRIBUTING.md](https://github.com/OpenLineage/OpenLineage/blob/main/CONTRIBUTING.md) for more details about how to contribute.

## Report a Vulnerability

If you discover a vulnerability in the project, please [open an issue](https://github.com/OpenLineage/OpenLineage/issues/new/choose) and attach the "security" label.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=OpenLineage/OpenLineage&type=Date)](https://www.star-history.com/#OpenLineage/OpenLineage&Date)

----
SPDX-License-Identifier: Apache-2.0\
Copyright 2018-2026 contributors to the OpenLineage project

## `AGENTS.md`

# AGENTS.md

Guidelines for AI coding agents contributing to OpenLineage.

## Protected paths

**Do NOT modify these files without explicit user authorization:**

- `spec/OpenLineage.json`
- `spec/OpenLineage.yml`
- `spec/facets/*.json`
- `spec/registry/**/*.json`

Before modifying any spec file, ask: "This change affects the OpenLineage specification. Do you authorize this modification?"

## Spec changes

All spec changes MUST be backwards compatible per [SchemaVer](spec/Versioning.md):

- **Safe**: Adding optional fields, new facets, new enum values
- **Unsafe**: Removing fields, changing types, making fields required, renaming

When changing the spec:
1. Update version in `$id` field appropriately
2. Add test cases in `spec/tests/`
3. run pre-commit
4. Coordinate changes across all clients (Java, Python)

## Setup commands

- Install pre-commit hooks: `prek install`
- Run all checks: `prek run --all-files`

## Build commands

- Java client: `cd client/java && ./gradlew build`
- Python client: `cd client/python && uv sync && uv run pytest`

## Testing

All code changes require tests:

- Spec: `spec/tests/{FacetName}/`
- Java: `client/java/src/test/`
- Python: `client/python/tests/`

## Commit conventions

Always sign off commits (DCO required):

```bash
git commit -s -m "component: description"
```



## AI disclosure

When AI assistants contribute to code, disclose this in commit messages:

```
Co-Authored-By: AI-Assistant-Name <noreply@example.com>
```

Examples:
```
Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: GitHub Copilot <noreply@github.com>
Co-Authored-By: Cursor <noreply@cursor.com>
```

## Code style

- Java: Spotless formatter
- Python: ruff (PEP 8)
- JSON/YAML: prettier

## License headers

All new files need Apache 2.0 headers:
we have .github/header_templates.md for this

## Client coordination

Changes affecting client functionality must be coordinated across all clients:

- `client/java/` - Java client
- `client/python/` - Python client

Examples: new transports, new facet support, API changes, configuration options.

## PR guidelines

follow CONTRIBUTING.md instructions

## Repository structure

```
spec/           # PROTECTED - OpenLineage specification
client/java/    # Java client
client/python/  # Python client
integration/    # Spark, Flink, dbt, Airflow integrations
proposals/      # Design proposals
website/        # Documentation
```

## References

- [CONTRIBUTING.md](CONTRIBUTING.md) - Full contribution guidelines
- [spec/Versioning.md](spec/Versioning.md) - Version numbering rules
- [why-the-dco.md](why-the-dco.md) - DCO explanation

## `CLAUDE.md`

AGENTS.md

## `CONTRIBUTING.md`

# Contributing to OpenLineage

This project welcomes contributors from any organization or background, provided they are
willing to follow the simple processes outlined below, as well as adhere to the 
[Code of Conduct](CODE_OF_CONDUCT.md).

## Joining the community

The community collaborates primarily through  `GitHub` and the instance messaging tool, `Slack`.
There is also a mailing list.
See how to join [here](https://github.com/OpenLineage/OpenLineage#community)

## Reporting an Issue

Please use the [issues][issues] section of the OpenLineage repository and search for a similar problem. If you don't find it, submit your bug, question, proposal or feature request.

Use tags to indicate parts of the OpenLineage that your issue relates to.
For example, in the case of bugs, please provide steps to reproduce it and tag your issue with `bug` and integration that has that bug, for example `integration/spark`.


## Contributing to the project

### Creating Pull Requests
Before sending a Pull Request with significant changes, please use the [issue tracker][issues] to discuss the potential improvements you want to make.

OpenLineage uses [GitHub's fork and pull model](https://help.github.com/articles/about-collaborative-development-models/)
to create a contribution.

Make sure to [sign-off](https://github.com/OpenLineage/OpenLineage/blob/main/why-the-dco.md) your work to say that the contributor has the rights to make the contribution and
agrees with the [Developer Certificate of Origin (DCO)](why-the-dco.md).

To ensure your pull request is accepted, follow these guidelines:

* All changes should be accompanied by tests
* Relevant documentation should be updated.
* Do your best to have a [well-formed commit message](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html) for your change
* Do your best to have a [well-formed pull request description](https://frontside.com/blog/2020-04-15-7-reasons-for-good-pull-request-descriptions) for your change
* [Keep diffs small](https://kurtisnusbaum.medium.com/stacked-diffs-keeping-phabricator-diffs-small-d9964f4dcfa6) and self-contained
* If your change relates to an issue, please [link it](https://help.github.com/articles/closing-issues-using-keywords) in your pull request description
* Your pull request title should be of the form `component: name`, where `component` is the part of openlineage repo that your PR changes. For example: `flink: add Iceberg source visitor`
* Review tags added by a bot after PR creation, they should indicate parts of the repository that your PR refers to
* Changes to the core OpenLineage model or facets require prior discussion and must be versioned according to [SchemaVer](https://docs.snowplowanalytics.com/docs/pipeline-components-and-applications/iglu/common-architecture/schemaver)
* License [header](https://github.com/OpenLineage/OpenLineage/tree/main/.github/header_templates.md) must be present in all files.

### Branching

* Choose _short_ and _descriptive_ branch names
* Use dashes (`-`) to separate _words_ in branch names
* Use _lowercase_ in branch names

## Proposing changes

Create an issue and tag it as `proposal`.

In the description provide the following sections:
 - Purpose (Why?): What is the use case this is for. 
 - Proposed implementation (How?): Quick description of how do you propose to implement it. Are you proposing a new facet?

This can be just a couple paragraphs to start with.

Proposals that change OpenLineage specifications should be tagged as `spec`.
Small changes to the spec, like adding a facet, only require opening an issue describing the new facet.
Larger changes to the spec, changes to the core spec or new integrations require a longer form proposal following [this process](https://github.com/OpenLineage/OpenLineage/blob/main/proposals/336/PROPOSALS.md)

## New Integrations
New integrations should be added under the [./integrations](/integrations) folder. Each module
should have its own build configuration (e.g., `build.gradle` for a Gradle project, `setup.py` for 
python, etc.) with appropriate unit tests and integration tests (when possible).

Adding a new integration requires updating the CI build configuration with a new workflow. Job
definitions, orbs, parameters, etc. should be added to the
[.circleci/continue_config.yml](`continue_config.yml`) file. Workflow definition files are added to
the [.circleci/workflows](.circleci/workflows) directory. Each workflow file adheres to the CircleCI
config.yml schema, including only the workflows subschema (see
[https://circleci.com/docs/2.0/configuration-reference/#workflows](the CircleCI docs) for the schema
specification). Each workflow must include a `workflow_complete` job that `requires` each terminal
required step in the workflow (e.g., you might depend on `run-feature-integration-tests` as the
final step in the workflow). Job names must be unique across all workflows, as ultimately the
workflows are merged into a single config file. See existing workflows for examples.

## First-Time Contributors

If this is your first contribution to open source, you can [follow this tutorial][contributiontutorial] or check out [this video series][contributionvideos] to learn about the contribution workflow with GitHub.

Look for tickets labeled ['good first issue'][goodfirstissues] and ['help wanted'][helpwantedissues]. These are a great starting point if you want to contribute. Don't hesitate to ask questions about the issue if you are not sure about the strategy to follow.


[issues]: https://github.com/OpenLineage/OpenLineage/issues
[contributiontutorial]: https://github.com/firstcontributions/first-contributions#first-contributions
[contributionvideos]: https://egghead.io/courses/how-to-contribute-to-an-open-source-project-on-github
[goodfirstissues]: https://github.com/OpenLineage/OpenLineage/labels/good%20first%20issue
[helpwantedissues]: https://github.com/OpenLineage/OpenLineage/labels/help%20wanted

## Running pre-commit hooks

Before submitting your pull request, make sure to set up and run pre-commit hooks to ensure code quality and consistency. [Pre-commit](pre-commit.com) hooks are automated checks that run before each commit is made. These checks include code formatting, linting and JSON Schema specification validations. To set up the pre-commit hooks for this project, follow these steps:

* Install prek: If you haven't already, install prek on your local machine by running `pip install prek` (or check [installation instructions](https://github.com/j178/prek?tab=readme-ov-file#installation) for your environment).

* Set up hooks: Once prek is installed, navigate to the project's root directory and execute `prek install`. This command will set up the necessary hooks in your local repository.

* Run prek: Now, every time you attempt to make a commit, the prek hooks will automatically run on the staged files. If any issues are detected, the commit process will be halted, allowing you to address the problems before making the commit. Some of the hooks might be configured to fix the issues automatically, in which case you just need to review the applied changes and commit. You can also run `prek run --all-files` to manually trigger the hooks for all files in the repository.

## License header

If contributing changes, additions or fixes, please include an [appropriate header](.github/header_templates.md) in any new files, e.g. for Java files:

```
/*
/* Copyright 2018-2026 contributors to the OpenLineage project
/* SPDX-License-Identifier: Apache-2.0 
*/
```

## Development

To set up your local environment and start developing, check the [Development documentation](https://openlineage.io/docs/development/developing/).

----
SPDX-License-Identifier: Apache-2.0\
Copyright 2018-2026 contributors to the OpenLineage project

## `pyproject.toml`

[tool.ruff]
line-length = 110
target-version = "py310"
exclude = [
    ".git",
    "__pycache__",
    ".venv",
    ".pytest_cache",
    "build",
    "dist",
    "*.egg-info",
    "target",
]

[tool.ruff.lint]
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "UP", # pyupgrade
    "B",  # flake8-bugbear
    "C4", # flake8-comprehensions
    "PIE", # flake8-pie
    "SIM", # flake8-simplify
    "RUF", # ruff-specific rules
]
ignore = [
    "E501",  # line too long (handled by line-length)
    "B904",  # raise from None
    "RUF012", # mutable class attributes
]

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401"]
"*/tests/*" = ["SIM117"]


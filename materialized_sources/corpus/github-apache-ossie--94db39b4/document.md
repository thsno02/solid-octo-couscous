# Repository semantic capsule: apache/ossie

- Commit: `831f48e582731cf1ee2e65380ca5abf8157869c7`
- Default branch: `main`
- Description: apache/ossie
- Selected evidence files: 3 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

<!--
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache License, Version 2.0 (the
 "License"); you may not use this file except in compliance
 with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the License is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the License for the
 specific language governing permissions and limitations
 under the License.
-->

# Apache Ossie (incubating)

Apache Ossie is a collaborative, open-source effort dedicated to standardizing and streamlining semantic model exchange and utilization across the diverse array of tools and platforms within the data analytics, AI, and BI ecosystem. Our shared vision is to establish a common, vendor-agnostic semantic model specification, promoting unparalleled interoperability, efficiency, and collaboration among all participants. By providing a single, consistent source of truth, this vendor-agnostic standard ensures that your data's definitions and value remain consistent as they are interchanged between AI agents, BI platforms, and all other tools in your ecosystem, eliminating inconsistencies across your different tools.

Apache Ossie was formerly known as **Open Semantic Interchange (OSI)**.

Apache Ossie provides a single JSON- and YAML-based specification that any tool can read and write, addressing the semantic fragmentation common across today's data stack: the same KPI defined differently across tools, teams spending significant effort manually reconciling definitions, and AI agents producing unreliable outputs grounded in inconsistent business logic.

## What's in this repository

- [`core-spec/`](core-spec/) — The Ossie core specification (`spec.md`), the machine-readable schema (`spec.yaml`, `ossie-schema.json`), and accompanying documentation.
- [`converters/`](converters/) — Reference converters that translate between Ossie and other semantic formats (e.g., dbt, GoodData, Polaris, Salesforce).
- [`examples/`](examples/) — Example semantic models, including a complete TPC-DS model.
- [`validation/`](validation/) — Tooling for validating semantic models against the Ossie schema.
- [`docs/`](docs/) — Project documentation and overview.

## Get involved

- **Contribute:** See [CONTRIBUTING.md](CONTRIBUTING.md) for how to propose specification changes, contribute code, and participate in the community.
- **Roadmap:** See [ROADMAP.md](ROADMAP.md) for current working groups, future efforts, and planned enhancements informed by community discussion.
- **Discuss:** Join the conversation on [GitHub Discussions](https://github.com/apache/ossie/discussions) and [Issues](https://github.com/apache/ossie/issues).
- **Join the Slack community:** Chat directly with contributors on [Slack](https://join.slack.com/t/apache-ossie/shared_invite/zt-42zw4rflt-Gpve8_NFJq7AsdAQTY~SCg).

## `CONTRIBUTING.md`

<!--
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License.
-->

# Contributing to Apache Ossie (incubating)

Thank you for your interest in contributing to Apache Ossie! We welcome
contributions from everyone — whether you are a developer, a data engineer, a BI
analyst, or simply someone interested in the future of semantic interoperability.

Apache Ossie was formerly known as **Open Semantic Interchange (OSI)**.

> **Apache Ossie is an effort undergoing incubation at the Apache Software
> Foundation (ASF), sponsored by the Apache Incubator.** Incubation is required
> of all newly accepted projects until a further review indicates that the
> infrastructure, communications, and decision making process have stabilized in
> a manner consistent with other successful ASF projects. See the
> [DISCLAIMER](DISCLAIMER) for details.

Apache Ossie is governed by [The Apache Way](https://www.apache.org/theapacheway/),
the ASF's collection of principles and practices for building open, vendor-neutral
communities. If you are new to the ASF, the
[Apache Incubator](https://incubator.apache.org/) and the
[ASF New Committers guide](https://www.apache.org/dev/new-committers-guide.html)
are good starting points.

## Ways to Contribute

- **Specification Feedback**: Review proposed specification changes and share your perspective on the mailing list, GitHub pull requests, and issues.
- **Use Case Discussions**: Share how your organization uses semantic models and what challenges you face — this helps shape the specification to address real-world needs.
- **Code Contributions**: Contribute to validation tooling, converters, examples, or any other part of the project.
- **Documentation**: Help improve and expand the project documentation.
- **Community Support**: Answer questions, participate in discussions, and help onboard new contributors.

## Communication

At the ASF, **the mailing lists are the primary channel** for the project. Consensus
is built and decisions are recorded on the lists, so please bring discussions there.
A guiding principle of the Apache Way is: *if it didn't happen on the mailing list,
it didn't happen.*

- **dev@ossie.apache.org** — development and community discussion. Subscribe by
  emailing `dev-subscribe@ossie.apache.org`, then browse the
  [archives](https://lists.apache.org/list.html?dev@ossie.apache.org).
- **commits@ossie.apache.org** — automated notifications for commits, pull requests.
  Subscribe via `commits-subscribe@ossie.apache.org`.
- **issues@ossie.apache.org** — automated notifications for issues.
  Subscribe via `issues-subscribe@ossie.apache.org`.
- **private@ossie.apache.org** — the Podling Project Management Committee (PPMC)
  private list, used only for confidential matters such as committer nominations.

Secondary, less formal channels (never a substitute for the lists when a decision
is being made):

- [GitHub Issues](https://github.com/apache/ossie/issues) and
  [Discussions](https://github.com/apache/ossie/discussions)
- [Slack](https://join.slack.com/t/apache-ossie/shared_invite/zt-42zw4rflt-Gpve8_NFJq7AsdAQTY~SCg)

## Getting Started

1. **Subscribe to the dev list**: Email `dev-subscribe@ossie.apache.org` and introduce yourself.
2. **Read the Specification**: Familiarize yourself with the [core specification](core-spec/spec.md) to understand the semantic model format.
3. **Explore the Examples**: Review the [TPC-DS example](examples/tpcds_semantic_model.yaml) to see a complete semantic model in practice.
4. **Find something to work on**: Browse the [issues](https://github.com/apache/ossie/issues), or raise a topic on the dev list.
5. **Submit a Pull Request**: Fork the repository, make your changes, and submit a pull request. All contributions go through the review process described below.

## Contributor License Agreement (ICLA)

**No CLA is required to contribute.** All contributions to Apache Ossie are made under
the [Apache License 2.0](LICENSE). By submitting a pull request or patch, you agree that
your contribution is licensed under those terms (see Section 5 of the license). You can
open issues, submit pull requests, and participate in discussions without signing
anything.

An [Individual Contributor License Agreement (ICLA)](https://www.apache.org/licenses/contributor-agreements.html#clas)
is only required once you are elected as a committer: the ICLA must be on file with the
ASF before your Apache account and commit access are set up. A
[Corporate CLA (CCLA)](https://www.apache.org/licenses/contributor-agreements.html#clas)
is likewise not required for contributions, and is only relevant for committers
contributing on behalf of their employer.

Please keep individual commits attributed to the correct author so that provenance is
clear.

## AI-Assisted Contributions

- You remain personally responsible for all code you submit, regardless of how it was produced
- For details, see [ASF Generative Tooling Guidance](https://www.apache.org/legal/generative-tooling.html)

## Contribution Workflow

The project's canonical repository is hosted at
[github.com/apache/ossie](https://github.com/apache/ossie), mirrored from ASF
infrastructure (GitBox).

### Code, Documentation, and Tooling

Non-specification contributions (bug fixes, tooling, documentation, converters,
examples) follow standard GitHub pull request review:

1. Open an issue or start a thread on `dev@` for anything non-trivial, so the
   approach can be discussed before significant work begins.
2. Fork the repository and create a topic branch for your change.
3. Submit a pull request with a clear description of the motivation and the change.
4. A committer reviews and merges once the change has at least one **+1** from a
   committer and no unresolved **-1**. The project follows a review-then-commit (RTC)
   model: changes are merged after review rather than committed first.

### Specification Changes

Changes to the Apache Ossie specification carry a higher bar and follow a structured
process:

1. **Proposal**: Announce the proposal on `dev@ossie.apache.org` and open a GitHub
   pull request with a clear description of the motivation, the change itself, and
   its impact on existing implementations.
2. **Discussion period**: The community has a minimum of 7 days (72 hours for a
   formal `[VOTE]`) to review and discuss. Complex changes may require a longer
   review window.
3. **Vote**: Once discussion has settled, a `[VOTE]` thread is called on the dev
   list. See [Decision Making and Voting](#decision-making-and-voting) below.

## Decision Making and Voting

Apache Ossie strives for **lazy consensus** — proceeding when no one objects — and
falls back to a formal vote when consensus cannot be reached. Votes happen on
`dev@ossie.apache.org` so they are publicly recorded. Voters express:

- **+1**: In favor.
- **0**: Abstain / no strong opinion.
- **-1**: Against. For code and specification changes this is a **veto** and
  **must** be accompanied by a technical justification; a valid veto can only be
  resolved by addressing the stated concern.

Conventions:

- **Code and other changes** pass by lazy consensus: at least one binding **+1** and
  no vetoes.
- **Specification changes** require at least three binding **+1** votes and no
  vetoes.
- **Committer and PPMC nominations** are held on the private list and pass by lazy
  consensus (no **-1** within 72 hours).
- **Procedural votes** (e.g. adopting a policy) pass by simple majority and cannot
  be vetoed.

**Binding votes** on the podling are cast by PPMC members. Everyone is encouraged to
vote; non-binding votes are valued input that informs the outcome.

### Releases

As an incubating project, every release is approved in two stages:

1. A `[VOTE]` on `dev@ossie.apache.org` that passes with at least **three binding
   +1 votes** from the PPMC and more +1 than -1 votes.
2. A second `[VOTE]` on `general@incubator.apache.org` that passes with at least
   three binding +1 votes from the Incubator PMC (IPMC).

Releases are source releases distributed through official ASF channels and must
comply with [ASF release policy](https://www.apache.org/legal/release-policy.html).

## Community Values — The Apache Way

Apache Ossie follows [The Apache Way](https://www.apache.org/theapacheway/), built
on these principles:

- **Community over code**: A healthy, welcoming community is the project's most
  important asset.
- **Meritocracy**: Merit is based on contribution and never expires. Any constructive
  contribution earns merit — code, documentation, testing, community support, and
  specification reviews all count.
- **Peer-based**: Every participant is treated as a peer regardless of employer
  affiliation or seniority. Decisions are made by the community, not by any single
  company or individual.
- **Consensus decision making**: We strive for consensus in all decisions. When full
  consensus cannot be reached, a formal vote may be called.
- **Open Communications**: Technical discussions, design decisions, and specification
  changes happen in the open on the mailing lists and other public resources.
  Decisions are made asynchronously so contributors in every timezone can take part.
- **Responsible oversight**: The community collectively ensures the specification and
  tooling remain high quality, secure, and aligned with the project's mission.
- **Vendor neutrality**: The project operates independently of any single vendor or
  organization.

## Roles and Responsibilities

### Contributors

Anyone who contributes to the project in any form — code, documentation, bug reports,
specification feedback, or community support. Contributors are encouraged to
participate in all discussions and votes; contributor votes are non-binding but valued.

### Committers

Contributors who have earned write access to the repository through sustained,
high-quality contributions. Committers review and merge pull requests and have
binding votes on the project's technical decisions. All committers must have an ICLA
on file.

### Podling Project Management Committee (PPMC)

The PPMC is responsible for the overall direction and health of the podling —
technical direction, community growth, and oversight of releases. PPMC members'
votes are binding. During incubation, PPMC members work alongside the project's
mentors and, upon graduation, the PPMC becomes the project's PMC.


## `docs/index.md`

<!--
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License.
-->

# Apache Ossie

## Overview

The [Apache Ossie](https://ossie.apache.org/) initiative is a collaborative, open-source effort dedicated to standardizing and streamlining semantic model exchange and utilization across the data analytics, AI, and BI ecosystem. Our shared vision is to establish a common, vendor-agnostic semantic model specification, promoting interoperability, efficiency, and collaboration among all participants.

Apache Ossie was formerly known as **Open Semantic Interchange (OSI)**.

By providing a single, consistent source of truth, the Ossie standard ensures that your data's definitions and value remain consistent as they are interchanged between AI agents, BI platforms, and all other tools in your ecosystem — eliminating inconsistencies across your different tools.

### The Problem: Semantic Fragmentation

Today's data ecosystem is fragmented. Organizations rely on a wide array of tools for analytics, business intelligence, data engineering, and AI — each with its own way of defining and interpreting semantic models. This fragmentation leads to:

- **Metric Drift**: The same KPI is defined differently across dashboards and platforms, leading to conflicting numbers and eroded trust in data.
- **Manual Translation**: Teams spend significant effort manually reconciling semantic definitions when data moves between systems — an expensive and error-prone process.
- **AI Hallucinations**: When AI agents encounter conflicting or incomplete business logic across tools, they produce unreliable outputs grounded in inconsistent data definitions.
- **Integration Debt**: Every new tool added to the stack requires custom integration work, creating a web of brittle, point-to-point connectors that are costly to maintain.

### How Apache Ossie Solves It

Ossie addresses semantic fragmentation by providing:

- **Single Source of Truth**: A unified specification for semantic and metric definitions that all tools can read and write, ensuring consistency across the entire data stack.
- **Native Interoperability**: A hub-and-spoke model where tools exchange semantic models through Ossie as a common format — enabling direct platform-to-platform exchange without custom connectors.
- **Trusted AI Grounding**: Consistent business logic and rich AI context annotations ensure that AI agents and LLMs can reliably interpret and query data.
- **Reduced Total Cost of Ownership**: Automated model exchange eliminates manual reconciliation work and reduces the engineering effort needed to integrate new tools.

### Specification at a Glance

The Ossie core specification (current version: **0.2.0.dev0**, latest released: **0.1.1**) defines a YAML-based format for describing semantic models. The key constructs are:

| Construct | Description |
|-----------|-------------|
| **Semantic Model** | The top-level container representing a complete semantic model, including datasets, relationships, and metrics. |
| **Datasets** | Logical datasets representing business entities (fact and dimension tables), with fields, primary keys, and unique keys. |
| **Fields** | Row-level attributes for grouping, filtering, and metric expressions. Fields support multiple SQL dialects for cross-platform compatibility. |
| **Relationships** | Foreign key connections between datasets, supporting both simple and composite keys. |
| **Metrics** | Quantitative measures (sums, averages, ratios, etc.) defined at the model level, capable of spanning multiple datasets. |
| **Custom Extensions** | Vendor-specific metadata stored as JSON, allowing platforms to carry additional information without breaking core compatibility. |
| **AI Context** | Optional annotations at every level (model, dataset, field, relationship, metric) to help AI tools understand business meaning — including instructions, synonyms, and example queries. |

The specification supports multiple SQL dialects (`ANSI_SQL`, `SNOWFLAKE`, `DATABRICKS`, `MDX`, `TABLEAU`) so that expressions can be tailored to each platform while maintaining a common model structure.

For the full specification, see [core-spec/spec.md](../core-spec/spec.md). For validation tooling, see [validation/validate.py](../validation/validate.py). For a complete example, see the [TPC-DS semantic model](../examples/tpcds_semantic_model.yaml).

### Participating Organizations

Ossie is supported by a broad coalition of 50+ organizations across the data ecosystem, including:

Alation, Anomalo, Atlan, AtScale, Bigeye, BlackRock, Blue Yonder, Carto, Cloudera, Coalesce, Collate, Collibra, Cogniti, Count, Credible, Cube, Databricks, DataHub, Denodo, dbt Labs, Dremio, Domo, Elementum AI, Firebolt, GoodData, Hex, Honeydew, Informatica, Instacart, JetBrains, Lightdash, Mistral AI, Omni, Oracle, Preset, Qlik, RelationalAI, Salesforce, Select Star, Sigma, Snowflake, Solid, Starburst Data, Strategy, Sundial, ThoughtSpot, and more.

### Converters

Ossie converters follow a **hub-and-spoke** architecture: the Ossie core specification acts as the central, vendor-neutral format, and each converter handles translation to or from a specific vendor format (e.g., Snowflake, dbt, Salesforce, Databricks). This avoids the need for point-to-point converters between every pair of vendors.

For details on implementing a converter, see the [Converters Guide](../converters/README.md).

---

## Project Governance

We wanted the Ossie project to be a collaborative effort from the start. The purpose is to grow a community of developers, contributors, and users who are actively involved in shaping the Ossie Specification as it moves along.
Apache Ossie project governance is inspired by the governance model from [The ASF](https://www.apache.org).

### The Apache Way

The Apache Way articulates around several values:

1. **Meritocracy**
Merit is based on your contribution, and it never expires. Those with merit get more responsibility.
Any constructive contribution earns merit — code, documentation, testing, community support, and specification reviews all count equally.

2. **Peer-based**
The community involves mutual trust and respect. Every participant is treated as a peer regardless of employer affiliation or seniority. Decisions are made by the community, not by any single company or individual.

3. **Consensus decision making**
We strive for consensus in all decisions. When full consensus cannot be reached, a formal vote may be called. This ensures that all voices are heard and that decisions reflect the broadest possible agreement within the community.

4. **Collaborative development and Open Communications**
All technical discussions, design decisions, and specification changes happen in the open — on GitHub issues, pull requests, discussions. Private decisions are discouraged. If it didn't happen on a public resource, it didn't happen.

5. **Responsible oversight**
The community collectively ensures that the specification and its associated tooling remain high quality, secure, and aligned with the project's mission of vendor-agnostic semantic interoperability.

6. **Independence**
The Ossie project operates independently of any single vendor or organization. While contributors may be employed by companies that have a stake in semantic interoperability, the project's direction is determined by the community as a whole.

### Governing Bodies

As an incubating project, Apache Ossie is governed by its **Podling Project Management Committee (PPMC)**, working alongside the project's **Mentors** and under the oversight of the **Apache Incubator PMC (IPMC)**. See [CONTRIBUTING.md](../CONTRIBUTING.md) for the full description of roles and process.

The **PPMC** is responsible for the overall direction and health of the podling. It:

- Reviews and approves significant changes to the core specification
- Guides the roadmap for new specification features and extensions
- Ensures backward compatibility and coherence across specification versions
- Casts binding votes and votes on committer/PPMC nominations and releases
- Resolves technical disputes that cannot be settled through normal consensus

New committers and PPMC members are nominated and voted on by the PPMC following the standard [ASF process](https://www.apache.org/dev/pmc.html). During incubation, releases are additionally approved by the Incubator PMC.

Current PPMC members and Mentors are listed on the [podling status page](https://incubator.apache.org/projects/ossie.html).

### Roles

- **Contributors**: Anyone who contributes to the project in any form — code, documentation, bug reports, specification feedback, or community support. Contributor votes are non-binding, but everyone is encouraged to participate in all discussions and votes.
- **Committers**: Contributors who have earned write access to the repository through sustained contributions. Committers merge pull requests and have binding votes on the project's technical decisions. All committers have an ICLA on file.
- **PPMC Members**: Committers who also help steer the podling — growing the community, overseeing releases, and mentoring contributors. PPMC votes are binding.
- **Mentors**: Experienced ASF members assigned by the Incubator to guide the podling and shepherd release votes to the IPMC.

### Voting on Specification Changes

Changes to the Apache Ossie specification follow the ASF voting model, held on the `dev@ossie.apache.org` mailing list:

1. **Proposal**: Announce the change on `dev@ossie.apache.org` and open a GitHub pull request describing the motivation, the change, and its impact on existing implementations.
2. **Discussion period**: The community has a minimum of 7 days to review and discuss. Complex changes may require a longer window.
3. **Vote**: A `[VOTE]` thread is called. Voters cast:
   - **+1**: In favor
   - **0**: Abstain / no strong opinion
   - **-1**: Veto — must include a technical justification; a valid veto is resolved only by addressing the stated concern
   PPMC member votes are binding.
4. **Resolution**: A specification change passes with at least **three binding +1 votes** and no vetoes.

### Working Groups

Working groups are focused teams that drive specific areas of the specification forward. Each working group has a designated lead and members drawn from across the participating organizations.

For the full list of working groups, leads, and members, see the [Working Groups page](working_groups.md).

### Community Meetings

Community meetings are open to all participants and provide a forum for discussing specification progress, working group updates, and community-wide topics. Meetings are held at both the global level and within individual working groups.

- **Global Community Meetings**: Regular meetings open to all community members for cross-cutting discussions, roadmap reviews, and community announcements.
- **Working Group Meetings**: Each working group holds its own meetings to drive focused progress on their specific area of the specification.

Meeting schedules, agendas, and notes are published on the [Ossie website](https://ossie.apache.org/) and the project's GitHub repository. All community members are welcome to attend and participate.

**Google Calendar**: _link TBD_

---

## Architecture

### Hub-and-Spoke Model

Ossie is designed around a hub-and-spoke architecture that dramatically simplifies the integration landscape. Instead of requiring every tool to build custom connectors to every other tool, Ossie acts as the universal interchange format at the center.

```
                        ┌─────────────┐
                        │  Snowflake  │
                        └──────┬──────┘
                               │
      ┌─────────────┐    ┌─────┴─────┐    ┌─────────────┐
      │     dbt     ├────┤   Ossie   ├────┤  Salesforce │
      └─────────────┘    └─────┬─────┘    └─────────────┘
                               │
                        ┌──────┴──────┐
                        │  Databricks │
                        └─────────────┘
```

With N vendors, a point-to-point strategy would require **N×(N-1)** converters. With Ossie as the hub, only **2×N** converters are needed (one import and one export per vendor), and interoperability with all other vendors comes for free.

### How It Flows

A typical Ossie-based workflow looks like this:

1. **Author**: A semantic model is authored in one tool (e.g., dbt) or directly in the Ossie YAML format.
2. **Import**: If authored in a vendor tool, the vendor's import converter translates it into an Ossie model, preserving vendor-specific metadata in `custom_extensions`.
3. **Validate**: The Ossie model is validated against the [JSON Schema](../core-spec/ossie-schema.json) and the [validation script](../validation/validate.py) to ensure correctness.
4. **Exchange**: The Ossie model is shared — via Git, a data catalog, or a sync API — with other teams and tools.
5. **Export**: Each consuming tool's export converter translates the Ossie model into its native format, selecting the appropriate SQL dialect and applying vendor-specific extensions.
6. **Round-Trip**: When changes are made in a downstream tool, they can be imported back into the Ossie model, preserving all metadata for lossless round-tripping.

### Multi-Dialect Expression System

A key architectural feature of Ossie is its multi-dialect expression system. Fields and metrics can carry expressions in multiple SQL dialects simultaneously:

```yaml
expression:
  dialects:
    - dialect: ANSI_SQL
      expression: LOWER(email)
    - dialect: SNOWFLAKE
      expression: LOWER(email)::VARCHAR
    - dialect: DATABRICKS
      expression: lower(email)
```

This allows a single semantic model to be consumed natively by different platforms without expression translation. Each converter selects the dialect that matches its target platform, falling back to `ANSI_SQL` when a platform-specific dialect is not available.

---

## Frequently Asked Questions

### General

**What is a semantic model?**
A semantic model is a structured description of business data that defines what datasets exist, what their fields mean, how datasets relate to each other, and what metrics (KPIs) can be computed from the data. It serves as a shared vocabulary between data producers and consumers — whether those consumers are humans using BI tools or AI agents generating queries.

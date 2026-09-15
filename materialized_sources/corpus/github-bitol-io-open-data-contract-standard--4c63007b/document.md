# Repository semantic capsule: bitol-io/open-data-contract-standard

- Commit: `d3e1cb3e69849e05c9a7522abed9b27fb9af50d7`
- Default branch: `main`
- Description: bitol-io/open-data-contract-standard
- Selected evidence files: 3 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

---
title: "Open Data Contract Standard (ODCS)"
description: "Home of Open Data Contract Standard (ODCS) documentation."
image: "https://raw.githubusercontent.com/bitol-io/artwork/main/horizontal/color/Bitol_Logo_color.svg"
---

<!--
Copyright 2026 The Bitol Contributors
SPDX-License-Identifier: Apache-2.0
-->

[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/8149/badge)](https://www.bestpractices.dev/projects/8149)
  <a href="https://github.com/bitol-io/open-data-contract-standard">
    <img alt="Stars" src="https://img.shields.io/github/stars/bitol-io/open-data-contract-standard" /></a>
  <a href="https://jgp.ai/dmlslack" rel="nofollow"><img src="https://img.shields.io/badge/slack-join_chat-white.svg?logo=slack&amp;style=social" alt="Slack Status" data-canonical-src="https://img.shields.io/badge/slack-join_chat-white.svg?logo=slack&amp;style=social" style="max-width: 100%;"></a>

# Open Data Contract Standard (ODCS)

Welcome! 

Thanks for your interest and for taking the time to come here! ❤️

## Executive summary
This standard describes a structure for a **data contract**. Its current version is v3.2.0. It is available for you as an Apache 2.0 license. Contributions are welcome!

## Discover the open standard
A reader-friendly version of the standard can be found on its [dedicated site](https://bitol-io.github.io/open-data-contract-standard/).

Discover the [Open Data Contract Standard](docs/README.md). This file contains some explanations and several examples. More [examples](docs/examples/README.md) can be found here.

## What is a Data Contract?

### The basics of a data contract
A data contract defines the agreement between a data producer and consumers. A data contract contains several sections:

* [Fundamentals](docs/fundamentals.md).
* [Schema](docs/schema.md).
* [References](docs/references.md).
* [Data quality](docs/data-quality.md).
* [Support & communication channels](docs/support-communication-channels.md)
* [Pricing](docs/pricing.md).
* [Team](docs/team.md).
* [Roles](docs/roles.md).
* [Service-level agreement (SLA)](docs/service-level-agreement.md).
* [Infrastructures & servers](docs/infrastructure-servers.md).
* [Authoritative definitions](docs/authoritative-definitions.md).
* [Tags](docs/tags.md).
* [Custom & other properties](docs/custom-other-properties.md).

![Data contract schema](docs/img/data-contract-diagram-latest.png "Data contract schema")

*Figure 1: illustration of a data contract, its principal contributors, sections, and usage.*

### JSON Schema

JSON Schema for ODCS can be found [here](https://github.com/bitol-io/open-data-contract-standard/blob/main/schema/odcs-json-schema-latest.json). You can import this schema into your IDE for validation of your YAML files. Links below show how you can import the schema:

- [IntelliJ](https://www.jetbrains.com/help/idea/json.html#ws_json_schema_add_custom)
- [VS Code](https://code.visualstudio.com/docs/languages/json#_json-schemas-and-settings)

## Articles and Other Resources
Check out the [resources](./resources.md) page.

## Contributing to the project
Check out the [CONTRIBUTING](./CONTRIBUTING.md) page.

## More

### Citation

If you need to cite this standard, you can use the following BibTeX entry:

```bibtex
@manual{ODCS2025,
  title        = {Open Data Contract Standard (ODCS)},
  author       = {{Bitol}},
  organization = {LF AI \& Data Foundation},
  year         = {2025},
  url          = {https://bitol-io.github.io/open-data-contract-standard}
}
```

### Mime/Media Type

The official media (fka mime) type is:

```
application/odcs+yaml;version=3.2.0
```





## `CONTRIBUTING.md`

---
title: "Contributing: Open Data Contract Standard (ODCS)"
description: "How you can contribute to the Open Data Contract Standard (ODCS)."
image: "https://raw.githubusercontent.com/bitol-io/artwork/main/horizontal/color/Bitol_Logo_color.svg"
---

<!--
Copyright 2026 The Bitol Contributors
SPDX-License-Identifier: Apache-2.0
-->

# Contributing to Open Data Contract Standard

Thank you for your interest in contributing to Open Data Contract Standard (ODCS). Please refer to the [TSC contributing guidelines](https://github.com/bitol-io/tsc/blob/main/CONTRIBUTING.md).

## `docs/README.md`

---
title: "Definition: Open Data Contract Standard (ODCS)"
description: "Details of the Open Data Contract Standard (ODCS). Includes fundamentals, datasets, schemas, data quality, pricing, stakeholders, roles, service-level agreements and other properties."
image: "https://raw.githubusercontent.com/bitol-io/artwork/main/horizontal/color/Bitol_Logo_color.svg"
---

<!--
Copyright 2026 The Bitol Contributors
SPDX-License-Identifier: Apache-2.0
-->

# Open Data Contract Standard

## Executive Summary

This document describes the keys and values expected in a YAML data contract, per the **Open Data Contract Standard**. The standard is divided in multiple sections. Each section starts with at least an example, followed by the definition of each field/key. Since v3.1.0, each section has its own page for easier readability.

For more details, see the sections below:

1. [Fundamentals](./fundamentals.md)
2. [Schema](./schema.md)
3. [Context](./context.md)
4. [References](./references.md)
5. [Data Quality](./data-quality.md)
6. [Support & Communication Channels](./support-communication-channels.md)
7. [Pricing](./pricing.md)
8. [Team](./team.md)
9. [Roles](./roles.md)
10. [Service-Level Agreement](./service-level-agreement.md)
11. [Infrastructures & Servers](./infrastructure-servers.md)
12. [Custom & Other Properties](./custom-other-properties.md)
13. [Authoritative Definitions](./authoritative-definitions.md)
14. [Tags](./tags.md)
15. [Variables](./variables.md)

## Notes

* The sections above contain example values. We carefully reviewed the consistency of those values, but we cannot guarantee that there are no errors. If you spot one, please raise an [issue](https://github.com/AIDAUserGroup/open-data-contract-standard/issues).
* Some fields have a `null` value: even if it is equivalent to not having the field in the contract, we wanted to have the field for illustration purposes.
* The contract should be **platform agnostic**. If you think this is not the case, please raise an [issue](https://github.com/AIDAUserGroup/open-data-contract-standard/issues).
* The provided JSON schemas are companions to the standards (ODCS or ODPS), it means that they do not define the standards and may include bugs. In case of conflict between the standard and the JSON Schema, the standard takes precedence.

## Full example

[Check full example here.](examples/all/full-example.odcs.yaml)

All trademarks are the property of their respective owners.

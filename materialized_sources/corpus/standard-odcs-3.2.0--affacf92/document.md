# Open Data Contract Standard


## Executive Summary

This document describes the keys and values expected in a YAML data contract, per the Open Data Contract Standard . The standard is divided in multiple sections. Each section starts with at least an example, followed by the definition of each field/key. Since v3.1.0, each section has its own page for easier readability.

For more details, see the sections below:

Fundamentals

Schema

Context

References

Data Quality

Support & Communication Channels

Pricing

Team

Roles

Service-Level Agreement

Infrastructures & Servers

Custom & Other Properties

Authoritative Definitions

Tags

Variables


## Notes

The sections above contain example values. We carefully reviewed the consistency of those values, but we cannot guarantee that there are no errors. If you spot one, please raise an issue .

Some fields have a null value: even if it is equivalent to not having the field in the contract, we wanted to have the field for illustration purposes.

The contract should be platform agnostic . If you think this is not the case, please raise an issue .

The provided JSON schemas are companions to the standards (ODCS or ODPS), it means that they do not define the standards and may include bugs. In case of conflict between the standard and the JSON Schema, the standard takes precedence.


## Full example

Check full example here.

All trademarks are the property of their respective owners.


<!-- materialization-redistribution-notice -->
## Redistribution notice

This document includes material copied from or derived from "Open Data Contract Standard 3.2.0", https://bitol-io.github.io/open-data-contract-standard/v3.2.0/. Copyright 2026 The Bitol Contributors. SPDX-License-Identifier: Apache-2.0. Licensed under the Apache License, Version 2.0, https://www.apache.org/licenses/LICENSE-2.0.

Changes: Converted from the versioned ODCS HTML definition page to Markdown; navigation, hyperlinks, styling, embedded SVG icons, fonts, and image assets were omitted or normalized; selector excerpts were generated. The upstream copyright and SPDX license statement are restored in this attribution block.

Scope: 仅覆盖从固定 v3.2.0 定义页实际提取的 1,454-byte 原始 Markdown 正文及其 27 个 selector 摘录；不声称存储或覆盖链接的多页标准、示例、schema、Bitol 标识、Font Awesome SVG/图标/字体、外链作品、商标或权利人无权许可的第三方材料。

Full license and original rights links: [NOTICE.md](NOTICE.md).

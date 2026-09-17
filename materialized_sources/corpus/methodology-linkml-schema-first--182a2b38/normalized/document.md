# Retained specification text (collector assembly)

> This consumer Markdown assembles the explicitly retained originals in declared order. Source labels, line anchors and local href rewrites are collector additions; HTML is represented as structural text with ordered table cells and preserved code, without running source scripts.

> Collector representation: declared cell spans are annotations, not an expanded table grid; code br line breaks and NBSP are retained, and image-label whitespace is normalized without dropping label words.

Original HTML: [specification.html](../source/specification.html#L1-L714).

> Collector content boundary: only the article selected by "article#furo-main-content" is represented below. Original-line ranges are enclosing provenance bounds; the final range may extend to HTML entity EOF and does not imply that every line was converted.

<a id="specification-L1"></a>

<a id="specification-L416"></a>
<a id="specification-furo-main-content"></a>


 
<a id="specification-linkml-documentation"></a>


 # LinkML Documentation
 

Everything you need to know about [LinkML](https://linkml.io), the Linked Data Modeling Language.

 

LinkML is a flexible modeling language that allows you to author schemas in YAML that describe the structure of your data. Additionally, it is a framework for working with and validating data in a variety of formats (JSON, RDF, TSV), with generators for compiling LinkML schemas to other frameworks.

 

LinkML is open source (licensed under the Apache-2.0 license) and community-driven. You can find the code on [GitHub](https://github.com/linkml/).

 
<a id="specification-documentation"></a>

<a id="specification-L425"></a>
## Documentation
 

 

Contents:

 

 

- [LinkML at a glance](https://linkml.io/linkml/intro/overview.html)

 

  - [Feature: Easy to author schemas](https://linkml.io/linkml/intro/overview.html#feature-easy-to-author-schemas)

 

  - [Feature: Rich modeling language](https://linkml.io/linkml/intro/overview.html#feature-rich-modeling-language)

 

  - [A bridge between frameworks](https://linkml.io/linkml/intro/overview.html#a-bridge-between-frameworks)

 

  - [Feature: Generation of documentation and websites](https://linkml.io/linkml/intro/overview.html#feature-generation-of-documentation-and-websites)

 

  - [A rapidly growing toolchain](https://linkml.io/linkml/intro/overview.html#a-rapidly-growing-toolchain)

 

  - [We eat our own dogfood!](https://linkml.io/linkml/intro/overview.html#we-eat-our-own-dogfood)

 

  - [More examples](https://linkml.io/linkml/intro/overview.html#more-examples)

 

 

 

- [Quick Install Guide](https://linkml.io/linkml/intro/install.html)

 

  - [Local installation: Use the Python package](https://linkml.io/linkml/intro/install.html#local-installation-use-the-python-package)

 

  - [Alternative: Use the official Docker/OCI image](https://linkml.io/linkml/intro/install.html#alternative-use-the-official-docker-oci-image)

 

  - [Installation for contributors](https://linkml.io/linkml/intro/install.html#installation-for-contributors)

 

 

 

- [Tutorial](https://linkml.io/linkml/intro/tutorial.html)

 

  - [Part 1: Creating your first LinkML schema](https://linkml.io/linkml/intro/tutorial01.html)

 

  - [Part 2: Adding a container object](https://linkml.io/linkml/intro/tutorial02.html)

 

  - [Part 3: Adding constraints and performing validation](https://linkml.io/linkml/intro/tutorial03.html)

 

  - [Part 4: Working with RDF](https://linkml.io/linkml/intro/tutorial04.html)

 

  - [Part 5: Using Python dataclasses](https://linkml.io/linkml/intro/tutorial05.html)

 

  - [Part 6: Enumerations](https://linkml.io/linkml/intro/tutorial06.html)

 

  - [Part 7: Slots and inheritance](https://linkml.io/linkml/intro/tutorial07.html)

 

  - [Part 8: Generating Projects](https://linkml.io/linkml/intro/tutorial08.html)

 

  - [Part 9: Working with SQL databases](https://linkml.io/linkml/intro/tutorial09.html)

 

 

 

- [LinkML Schemas](https://linkml.io/linkml/schemas/index.html)

 

  - [Models](https://linkml.io/linkml/schemas/models.html)

 

  - [Schema Element Metadata](https://linkml.io/linkml/schemas/metadata.html)

 

  - [Inheritance](https://linkml.io/linkml/schemas/inheritance.html)

 

  - [Slots](https://linkml.io/linkml/schemas/slots.html)

 

  - [Arrays](https://linkml.io/linkml/schemas/arrays.html)

 

  - [URIs and Mappings](https://linkml.io/linkml/schemas/uris-and-mappings.html)

 

  - [Semantic Enumerations](https://linkml.io/linkml/schemas/enums.html)

 

  - [Inlining objects](https://linkml.io/linkml/schemas/inlining.html)

 

  - [Adding constraints and rules](https://linkml.io/linkml/schemas/constraints.html)

 

  - [Type designators](https://linkml.io/linkml/schemas/type-designators.html)

 

  - [Subsets](https://linkml.io/linkml/schemas/subsets.html)

 

  - [Imports](https://linkml.io/linkml/schemas/imports.html)

 

  - [Advanced features](https://linkml.io/linkml/schemas/advanced.html)

 

  - [Mapping schemas to other frameworks](https://linkml.io/linkml/schemas/generators.html)

 

  - [Schema Linter](https://linkml.io/linkml/schemas/linter.html)

 

  - [Derived models](https://linkml.io/linkml/schemas/derived-models.html)

 

  - [Annotations](https://linkml.io/linkml/schemas/annotations.html)

 

  - [The metamodel](https://linkml.io/linkml/schemas/metamodel.html)

 

  - [Expression Language](https://linkml.io/linkml/schemas/expression-language.html)

 

 

 

- [Working with Data](https://linkml.io/linkml/data/index.html)

 

  - [Converting between different representations](https://linkml.io/linkml/data/conversion.html)

 

  - [Data Validation](https://linkml.io/linkml/data/validating-data.html)

 

  - [Working with RDF and LinkML](https://linkml.io/linkml/data/rdf.html)

 

  - [CSVs and Tabular Data](https://linkml.io/linkml/data/csvs.html)

 

  - [Python](https://linkml.io/linkml/data/python.html)

 

  - [Working with data in SQL Databases](https://linkml.io/linkml/data/sql-databases.html)

 

 

 

- [Generators](https://linkml.io/linkml/generators/index.html)

 

  - [Schema Frameworks](https://linkml.io/linkml/generators/index.html#schema-frameworks)

 

  - [Linked Data Standards](https://linkml.io/linkml/generators/index.html#linked-data-standards)

 

  - [Documentation Generation](https://linkml.io/linkml/generators/index.html#documentation-generation)

 

  - [Language Specific](https://linkml.io/linkml/generators/index.html#language-specific)

 

  - [Database](https://linkml.io/linkml/generators/index.html#database)

 

  - [Others](https://linkml.io/linkml/generators/index.html#others)

 

  - [Feature Dashboard](https://linkml.io/linkml/generators/index.html#feature-dashboard)

 

  - [Common](https://linkml.io/linkml/generators/index.html#common)

 

 

 

- [How-to Guides](https://linkml.io/linkml/howtos/index.html)

 

  - [LinkML Project Copier Template](https://linkml.io/linkml/howtos/linkml-project-copier.html)

 

  - [How to run a collaborative data modeling project](https://linkml.io/linkml/howtos/collaborative-development.html)

 

  - [How to recognize and work with different structural forms](https://linkml.io/linkml/howtos/recognize-structural-forms.html)

 

  - [Using yq for querying and manipulating schemas](https://linkml.io/linkml/howtos/yq-for-schemas.html)

 

  - [Using JSON-LD](https://linkml.io/linkml/howtos/using-jsonld.html)

 

  - [How to model quantities and measurements](https://linkml.io/linkml/howtos/model-measurements.html)

 

  - [Porting LinkML tools to other programming languages](https://linkml.io/linkml/howtos/port-linkml.html)

 

  - [Multidimensional Arrays](https://linkml.io/linkml/howtos/multidimensional-arrays.html)

 

  - [How to make a property graph schema](https://linkml.io/linkml/howtos/model-property-graphs.html)

 

  - [How to Generate AI prompts](https://linkml.io/linkml/howtos/generate-ai-prompts.html)

 

  - [Deprecating elements while maintaining PURLs and other URIs](https://linkml.io/linkml/howtos/deprecating-elements.html)

 

  - [Using ontology terms as values in data](https://linkml.io/linkml/howtos/ontologies-as-values.html)

 

  - [Implements vs Instantiates vs Inheritance: A Best Practices Guide](https://linkml.io/linkml/howtos/implements-instantiates-guide.html)

 

  - [How to implement skip logic in LinkML](https://linkml.io/linkml/howtos/skip-logic.html)

 

 

 

- [Examples of use](https://linkml.io/linkml/examples.html)

 

  - [Introductory Example](https://linkml.io/linkml/examples.html#introductory-example)

 

  - [Example Models](https://linkml.io/linkml/examples.html#example-models)

 

  - [INCLUDE Data Coordination Center](https://linkml.io/linkml/examples.html#include-data-coordination-center)

 

  - [LinkML Registry](https://linkml.io/linkml/examples.html#linkml-registry)

 

  - [Presentations about LinkML](https://linkml.io/linkml/examples.html#presentations-about-linkml)

 

 

 

- [The LinkML Ecosystem](https://linkml.io/linkml/ecosystem.html)

 

  - [Tools that build off or enhance LinkML](https://linkml.io/linkml/ecosystem.html#tools-that-build-off-or-enhance-linkml)

 

 

 

- [LinkML specification](https://linkml.io/linkml/specifications/linkml-spec.html)

 

- [Get Involved](https://linkml.io/linkml/get-involved/index.html)

 

  - [Community Meetings](https://linkml.io/linkml/get-involved/Community-Meetings.html)

 

  - [Workshops and Presentations](https://linkml.io/linkml/get-involved/workshops-and-presentations.html)

 

  - [Monthly LinkML Office Hours](https://linkml.io/linkml/get-involved/office-hours.html)

 

 

 

- [FAQ](https://linkml.io/linkml/faq/index.html)

 

  - [FAQ: General](https://linkml.io/linkml/faq/general.html)

 

  - [FAQ: Why LinkML](https://linkml.io/linkml/faq/why-linkml.html)

 

  - [FAQ: Modeling](https://linkml.io/linkml/faq/modeling.html)

 

  - [FAQ: Tools](https://linkml.io/linkml/faq/tools.html)

 

  - [FAQ: Python](https://linkml.io/linkml/faq/python.html)

 

  - [FAQ: Getting Help](https://linkml.io/linkml/faq/getting-help.html)

 

  - [FAQ: Contributing](https://linkml.io/linkml/faq/contributing.html)

 

  - [FAQ: Tricky Choices](https://linkml.io/linkml/faq/tricky_choices.html)

 

 

 

 

 

 
<a id="specification-metamodel-reference"></a>

<a id="specification-L550"></a>
## Metamodel Reference
 

The LinkML metamodel is itself described in LinkML. This model is hosted in the [linkml-model](https://github.com/linkml/linkml-model) repository. Each element of the model has a URI of the form `https://w3id.org/linkml/<ELEMENT>`, shortened to the CURIE `linkml:<ELEMENT>`

 

The key schema elements are:

 

 

- 

[linkml:SchemaDefinition](https://w3id.org/linkml/SchemaDefinition)

 

 



 

  - 

[linkml:ClassDefinition](https://w3id.org/linkml/ClassDefinition)



 

  - 

[linkml:SlotDefinition](https://w3id.org/linkml/SlotDefinition)



 

  - 

[linkml:TypeDefinition](https://w3id.org/linkml/TypeDefinition)



 

  - 

[linkml:EnumDefinition](https://w3id.org/linkml/EnumDefinition)



 

 



 

 

 

 
<a id="specification-schema-developers"></a>

<a id="specification-L570"></a>
## Schema Developers
 

If you are a Python developer looking to use LinkML programmatically to build schemas, work with data, or integrate LinkML into your applications, this section is for you:

 

 

Schema Developers Guide:

 

 

- [CLI](https://linkml.io/linkml/cli/index.html)

 

  - [`linkml`](https://linkml.io/linkml/cli/linkml.html)

 

  - [`linkml config`](https://linkml.io/linkml/cli/config.html)

 

  - [`linkml generate`](https://linkml.io/linkml/cli/generate.html)

 

  - [`linkml lint`](https://linkml.io/linkml/cli/lint.html)

 

  - [`linkml validate`](https://linkml.io/linkml/cli/validate.html)

 

  - [Entrypoints](https://linkml.io/linkml/cli/entrypoints.html)

 

 

 

- [Schema Developers Guide](https://linkml.io/linkml/developers/index.html)

 

  - [Jupyter Notebooks](https://linkml.io/linkml/developers/notebooks.html)

 

  - [Manipulating Schemas](https://linkml.io/linkml/developers/manipulating-schemas.html)

 

  - [How to Manage Releases of your LinkML Schema](https://linkml.io/linkml/developers/manage-releases.html)

 

  - [SchemaView](https://linkml.io/linkml/developers/schemaview.html)

 

  - [SchemaBuilder](https://linkml.io/linkml/developers/schemabuilder.html)

 

  - [Data Conversion: Loaders and Dumpers](https://linkml.io/linkml/developers/loaders-and-dumpers.html)

 

  - [Inferring Missing Values](https://linkml.io/linkml/developers/inference.html)

 

  - [Using SQL Databases](https://linkml.io/linkml/developers/using-sql-dbs.html)

 

  - [SQLStore](https://linkml.io/linkml/developers/sqlstore.html)

 

  - [Tool Implementer Guide](https://linkml.io/linkml/developers/tool-developer-guide.html)

 

 

 

- [Code](https://linkml.io/linkml/code/index.html)

 

  - [MetaModel](https://linkml.io/linkml/code/metamodel.html)

 

  - [Utils](https://linkml.io/linkml/code/utils.html)

 

  - [Validator](https://linkml.io/linkml/code/validator.html)

 

  - [Deprecation Log](https://linkml.io/linkml/code/deprecation.html)

 

 

 

- [Configuration](https://linkml.io/linkml/config/index.html)

 

  - [Sources](https://linkml.io/linkml/config/index.html#sources)

 

  - [Keys](https://linkml.io/linkml/config/index.html#keys)

 

  - [CLI](https://linkml.io/linkml/config/index.html#cli)

 

  - [Examples](https://linkml.io/linkml/config/index.html#examples)

 

  - [API](https://linkml.io/linkml/config/index.html#module-linkml.utils.config)

 

 

 

 

 

 
<a id="specification-maintainers"></a>

<a id="specification-L617"></a>
## Maintainers
 

If you want to contribute to the LinkML framework itself, including bug fixes, new features, or documentation improvements:

 

 

Maintainers Guide:

 

 

- [Maintainers Guide](https://linkml.io/linkml/maintainers/index.html)

 

  - [Contribution Guidelines](https://linkml.io/linkml/maintainers/contributing.html)

 

  - [GitHub Organization](https://linkml.io/linkml/maintainers/organization.html)

 

  - [Contributor Hierarchy](https://linkml.io/linkml/maintainers/contributor-hierarchy.html)

 

  - [CODEOWNERS](https://linkml.io/linkml/maintainers/codeowners.html)

 

  - [Deprecations](https://linkml.io/linkml/maintainers/deprecation.html)

 

  - [Code of Conduct](https://linkml.io/linkml/maintainers/code-of-conduct.html)

 

  - [Generator and Validator Governance](https://linkml.io/linkml/maintainers/generator-governance.html)

 

 

 

 

 

 
<a id="specification-indices-and-tables"></a>

<a id="specification-L637"></a>
## Indices and tables
 

 

- 

[Index](https://linkml.io/linkml/genindex.html)



 

- 

[Module Index](https://linkml.io/linkml/py-modindex.html)



 

- 

[Search Page](https://linkml.io/linkml/search.html)


<!-- materialization-redistribution-notice -->
## Redistribution notice

This document includes material copied from or derived from "LinkML Documentation", https://linkml.io/linkml/. Copyright 2021-2026 LinkML Authors. SPDX-License-Identifier: Apache-2.0. Licensed under the Apache License, Version 2.0, https://www.apache.org/licenses/LICENSE-2.0. 原页脚保留Made with Sphinx and @pradyunsg's Furo署名；本原响应实际嵌入Furo2025.12.19模板另按MIT：Copyright (c) 2020 Pradyun Gedam <mail@pradyunsg.me>。完整MIT随NOTICE；保留上游Adapted from Just the Docs以及Feather/Tabler来源线索，不声称各图标全许可链审核或第三方权利担保，不暗示背书。

Changes: 原55141B HTML原字节保存；只在派生DOM消费唯一article#furo-main-content，排除a.headerlink的¶ UI符号，保留作者文字、目录href及URI/CURIE代码词法；li/p/blockquote列表层级在Markdown中部分丢失，原HTML可核。结构Markdown、空白连续化、链接解析、源行锚点/sidecar和边界说明属于collector-derived format conversion，不是raw quotation；保守source bounds可至entity EOF，不证明逐行转换或精确closing-tag，article外nav/footer不混正文。新normalized EOF附唯一归属/范围/修改块和NOTICE；旧root doc/164selectors不改，旧NOTICE复制history/NOTICE-before-page-body-02.md，全旧M/C/R review保全，不执行脚本或补造部署commit。

Scope: 仅本次https://linkml.io/linkml/单页dated-response-2026-09-17T14:20:17Z完整原HTML内作者内容（Apache-2.0）及实际嵌入Furo2025.12.19模板（MIT），并覆盖声明article的normalized/document.md/新sidecar；AND分范围履约不是OR，具体派生bytes/count以manifest为准。旧7340B pre-notice正文/164root selectors和text-only grant另留完整历史。未保存的其他文档页、logo/媒体、远程CSS/JS/依赖/外链作品/代码/数据、商标或无权许可材料不准入；URI引用不是资源已保存/获许可。原UID多页总体边界仍unresolved，partial/full_text不等于whole-UID complete/trusted或离线站点视觉/功能完整。

Full license and original rights links: [NOTICE.md](../NOTICE.md).

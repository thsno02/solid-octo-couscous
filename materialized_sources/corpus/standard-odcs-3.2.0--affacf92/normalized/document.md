# Retained specification text (collector assembly)

> This consumer Markdown assembles the explicitly retained originals in declared order. Source labels, line anchors and local href rewrites are collector additions; YAML below is an unmodified native document displayed in a code fence; an explicitly declared example is not a schema.

Original MD: [README.md](../source/docs/README.md#L1-L47).

<a id="README-L1"></a>

> Collector metadata display: original leading YAML frontmatter, source lines 1–5; not an upstream body heading.


```yaml
---
title: "Definition: Open Data Contract Standard (ODCS)"
description: "Details of the Open Data Contract Standard (ODCS). Includes fundamentals, datasets, schemas, data quality, pricing, stakeholders, roles, service-level agreements and other properties."
image: "https://raw.githubusercontent.com/bitol-io/artwork/main/horizontal/color/Bitol_Logo_color.svg"
---
```


<!--
Copyright 2026 The Bitol Contributors
SPDX-License-Identifier: Apache-2.0
-->


<a id="README-L12"></a>

# Open Data Contract Standard


<a id="README-L14"></a>

## Executive Summary

This document describes the keys and values expected in a YAML data contract, per the **Open Data Contract Standard**. The standard is divided in multiple sections. Each section starts with at least an example, followed by the definition of each field/key. Since v3.1.0, each section has its own page for easier readability.

For more details, see the sections below:

1. [Fundamentals](#fundamentals-L1)
2. [Schema](#schema-L1)
3. [Context](#context-L1)
4. [References](#references-L1)
5. [Data Quality](#data-quality-L1)
6. [Support & Communication Channels](#support-communication-channels-L1)
7. [Pricing](#pricing-L1)
8. [Team](#team-L1)
9. [Roles](#roles-L1)
10. [Service-Level Agreement](#service-level-agreement-L1)
11. [Infrastructures & Servers](#infrastructure-servers-L1)
12. [Custom & Other Properties](#custom-other-properties-L1)
13. [Authoritative Definitions](#authoritative-definitions-L1)
14. [Tags](#tags-L1)
15. [Variables](#variables-L1)


<a id="README-L36"></a>

## Notes

* The sections above contain example values. We carefully reviewed the consistency of those values, but we cannot guarantee that there are no errors. If you spot one, please raise an [issue](https://github.com/AIDAUserGroup/open-data-contract-standard/issues).
* Some fields have a `null` value: even if it is equivalent to not having the field in the contract, we wanted to have the field for illustration purposes.
* The contract should be **platform agnostic**. If you think this is not the case, please raise an [issue](https://github.com/AIDAUserGroup/open-data-contract-standard/issues).
* The provided JSON schemas are companions to the standards (ODCS or ODPS), it means that they do not define the standards and may include bugs. In case of conflict between the standard and the JSON Schema, the standard takes precedence.


<a id="README-L43"></a>

## Full example

[Check full example here.](#full-example-odcs-L1)

All trademarks are the property of their respective owners.

Original MD: [fundamentals.md](../source/docs/fundamentals.md#L1-L62).

<a id="fundamentals-L1"></a>

> Collector metadata display: original leading YAML frontmatter, source lines 1–4; not an upstream body heading.


```yaml
---
title: "Fundamentals"
description: "This section contains general information about the contract."
---
```


<!--
Copyright 2026 The Bitol Contributors
SPDX-License-Identifier: Apache-2.0
-->


<a id="fundamentals-L11"></a>

# Fundamentals

This section contains general information about the contract. Fundamentals were also called demographics in early versions of ODCS.

[Back to TOC](#README-L1)


<a id="fundamentals-L17"></a>

## Example

```YAML
apiVersion: v3.2.0 # Standard version
kind: DataContract

id: 53581432-6c55-4ba2-a65f-72344a91553a
name: seller_payments_v1
version: 1.1.0 # Data Contract Version
status: active
domain: seller
dataProduct: payments
tenant: ClimateQuantumInc

description:
  purpose: Views built on top of the seller tables.
  limitations: Cannot be used in conjunction with days with full moons.
  usage: Twice a day, preferable before meals.

tags: ['finance']
```


<a id="fundamentals-L39"></a>

## Definitions

| Key                                  | Type          | UX label                  | Required | Description                                                                                                                                                                                                                   |
| ------------------------------------ | ------------- | ------------------------- |----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| apiVersion                           | string        | Standard version          | Yes      | Version of the standard used to build data contract. Default value is `v3.2.0`.                                                                                                                                               |
| ~~dataProduct~~                      | string        | Data Product              | No       | Name of the data product. **DEPRECATED since v3.1.0.**                                                                                                                                                                         |
| domain                               | string        | Domain                    | No       | Name of the logical data domain.                                                                                                                                                                                              |
| id                                   | string        | ID                        | Yes      | A unique identifier used to reduce the risk of dataset name collisions, such as a UUID.                                                                                                                                       |
| kind                                 | string        | Kind                      | Yes      | The kind of file this is. Valid value is `DataContract`.                                                                                                                                                                      |
| name                                 | string        | Name                      | No       | Name of the data contract.                                                                                                                                                                                                    |
| status                               | string        | Status                    | No       | Current status of the data contract. Examples are "proposed", "draft", "active", "deprecated", "retired".                                                                                                                     |
| tenant                               | string        | Tenant                    | No       | Indicates the property the data is primarily associated with. Value is case insensitive.                                                                                                                                      |
| version                              | string        | Version                   | Yes      | Current version of the data contract.                                                                                                                                                                                         |
| authoritativeDefinitions             | array<object> | Authoritative Definitions | No       | List of links to sources that provide more details on the data contract.                                                                                                                                                      |
| tags                                 | array<string> | Tags                      | No       | A list of tags applied to the data contract. See [Tags](#tags-L1) for the full specification, recommended usage, and where else `tags` can appear.                                                                           |
| customProperties                     | array<object> | Custom Properties         | No       | Custom properties that are not part of the standard. See [Custom & Other Properties](#custom-other-properties-L1) for the structure of each entry.                                                                           |
| description                          | object        | Description               | No       | Object containing the descriptions.                                                                                                                                                                                           |
| description.limitations              | string        | Limitations               | No       | Technical, compliance, and legal limitations for data use.                                                                                                                                                                    |
| description.purpose                  | string        | Purpose                   | No       | Intended purpose for the provided data.                                                                                                                                                                                       |
| description.usage                    | string        | Usage                     | No       | Recommended usage of the data.                                                                                                                                                                                                |
| description.authoritativeDefinitions | array         | Authoritative Definitions | No       | List of links to sources that provide more details on the dataset; examples would be a link to privacy statement, terms and conditions, license agreements, data catalog, or another tool.                                    |
| description.customProperties         | array         | Custom Properties         | No       | Custom properties that are not part of the standard.                                                                                                                                                                          |

[Back to TOC](#README-L1)

Original MD: [schema.md](../source/docs/schema.md#L1-L554).

<a id="schema-L1"></a>

> Collector metadata display: original leading YAML frontmatter, source lines 1–4; not an upstream body heading.


```yaml
---
title: "Schema"
description: "This section describes the schema of the data contract."
---
```


<!--
Copyright 2026 The Bitol Contributors
SPDX-License-Identifier: Apache-2.0
-->


<a id="schema-L11"></a>

# Schema

This section describes the schema of the data contract. It is the support for data quality, which is detailed in the next section. Schema supports both a business representation of your data and a physical implementation. It allows to tie them together.

In ODCS v3, the schema has evolved from the table and column representation, therefore the schema introduces a new terminology:

* **Objects** are a structure of data: a table in a RDBMS system, a document in a NoSQL database, and so on.
* **Properties** are attributes of an object: a column in a table, a field in a payload, and so on.
* **Elements** are either an object or a property.

Figure 1 illustrates those terms with a basic relational database.

![Schema elements](../source/docs/img/elements-of-schema-odcs-v3.png)

*Figure 1: elements of the schema in ODCS v3.*

[Back to TOC](#README-L1)


<a id="schema-L29"></a>

## Examples


<a id="schema-L31"></a>

### Complete schema

```YAML
schema:
  - id: tbl_obj
    name: tbl
    logicalType: object
    physicalType: table
    physicalName: tbl_1
    description: Provides core payment metrics
    authoritativeDefinitions:
      - url: https://catalog.data.gov/dataset/air-quality
        type: businessDefinition
        description: Business definition for the dataset.
      - url: https://youtu.be/jbY1BKFj9ec
        type: videoTutorial
    tags: ['finance']
    dataGranularityDescription: Aggregation on columns txn_ref_dt, pmt_txn_id
    properties:
      - id: txn_ref_dt_prop
        name: txn_ref_dt
        businessName: transaction reference date
        logicalType: date
        physicalType: date
        description: null
        partitioned: true
        partitionKeyPosition: 1
        criticalDataElement: false
        tags: []
        classification: public
        transformSourceObjects:
          - table_name_1
          - table_name_2
          - table_name_3
        transformLogic: sel t1.txn_dt as txn_ref_dt from table_name_1 as t1, table_name_2 as t2, table_name_3 as t3 where t1.txn_dt=date-3
        transformDescription: Defines the logic in business terms.
        examples:
          - 2022-10-03
          - 2020-01-28
      - id: rcvr_id_prop
        name: rcvr_id
        primaryKey: true
        primaryKeyPosition: 1
        businessName: receiver id
        logicalType: string
        physicalType: varchar(18)
        required: false
        description: A description for column rcvr_id.
        partitioned: false
        partitionKeyPosition: -1
        criticalDataElement: false
        tags: []
        classification: restricted
        encryptedName: enc_rcvr_id
      - id: rcvr_cntry_code_prop
        name: rcvr_cntry_code
        primaryKey: false
        primaryKeyPosition: -1
        businessName: receiver country code
        logicalType: string
        physicalType: varchar(2)
        required: false
        description: null
        partitioned: false
        partitionKeyPosition: -1
        criticalDataElement: false
        tags: []
        classification: public
        authoritativeDefinitions:
          - url: https://zeenea.app/asset/742b358f-71a5-4ab1-bda4-dcdba9418c25
            type: businessDefinition
          - url: https://github.com/myorg/myrepo
            type: transformationImplementation
          - url: jdbc:postgresql://localhost:5432/adventureworks/tbl_1/rcvr_cntry_code
            type: implementation
        encryptedName: rcvr_cntry_code_encrypted
```


<a id="schema-L109"></a>

### Simple Array

```yaml
schema:
  - name: AnObject
    logicalType: object
    properties:
      - name: street_lines
        logicalType: array
        items:
          logicalType: string
```


<a id="schema-L122"></a>

### Array of Objects

```yaml
schema:
  - id: another_obj
    name: AnotherObject
    logicalType: object
    properties:
      - id: x_prop
        name: x
        logicalType: array
        items:
          logicalType: object
          properties:
            - id: id_field
              name: id
              logicalType: string
              physicalType: VARCHAR(40)
            - id: zip_field
              name: zip
              logicalType: string
              physicalType: VARCHAR(15)
```


<a id="schema-L146"></a>

## Definitions


<a id="schema-L148"></a>

### Schema (top level)

| Key    | Type  | UX label | Required | Description                                                  |
| ------ | ----- | -------- | -------- | ------------------------------------------------------------ |
| schema | array | schema   | Yes      | Array. A list of elements within the schema to be cataloged. |


<a id="schema-L154"></a>

### Applicable to Elements (either Objects or Properties)

| Key                      | Type   | UX label                  | Required | Description                                                                                                                                                                                |
| ------------------------ | ------ | ------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| businessName             | string | Business Name             | No       | The business name of the element.                                                                                                                                                          |
| description              | string | Description               | No       | Description of the element.                                                                                                                                                                |
| deprecated               | boolean | Deprecated               | No       | Indicates this element is deprecated and should not be used in new implementations. Defaults to `false`. See [Deprecated](#schema-L530).                                                    |
| id                       | string | ID                        | No       | A unique identifier for the element used to create stable, refactor-safe references. Recommended for elements that will be referenced. See [References](#references-L1) for more details. |
| name                     | string | Name                      | Yes      | Name of the element.                                                                                                                                                                       |
| physicalName             | string | Physical Name             | No       | Physical name.                                                                                                                                                                             |
| physicalType             | string | Physical Type             | No       | The physical element data type in the data source. For objects: `table`, `view`, `topic`, `file`. For properties: `VARCHAR(2)`, `DOUBLE`, `INT`, etc.                                      |
| logicalType              | string | Logical Type              | No       | The logical data type of the element. One of `string`, `date`, `timestamp`, `time`, `number`, `integer`, `object`, `array`, `boolean`, `map`, or `vector`. At the object level this is typically `object` (or `array` for an array of objects); the data-type keywords above apply to properties. |
| quality                  | array  | Quality                   | No       | List of data quality attributes.                                                                                                                                                           |
| synonyms                 | array  | Synonyms                  | No       | A list of alternative names for the element (object or property), helping catalogs, AI/LLM tools, and natural language interfaces resolve business vocabulary to the underlying object. See [Synonyms](#schema-L481).                       |
| authoritativeDefinitions | array  | Authoritative Definitions | No       | List of links to sources that provide more details on the element; examples would be a link to privacy statement, terms and conditions, license agreements, data catalog, or another tool. |
| tags                     | array  | Tags                      | No       | A list of tags applied to the element (object or property). See [Tags](#tags-L1) for the full specification.                                                                              |
| customProperties         | array  | Custom Properties         | No       | Custom properties that are not part of the standard.                                                                                                                                       |


<a id="schema-L172"></a>

### Applicable to Objects

| Key                        | Type   | UX label         | Required | Description                                                                          |
| -------------------------- | ------ | ---------------- | -------- | ------------------------------------------------------------------------------------ |
| dataGranularityDescription | string | Data Granularity | No       | Granular level of the data in the object. Example would be "Aggregation by country." |


<a id="schema-L178"></a>

### Applicable to Properties

Some keys are more applicable when the described property is a column.

| Key                      | Type    | UX label                     | Required | Description                                                                                                                                                                                                                           |
| ------------------------ | ------- | ---------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| classification           | string  | Classification               | No       | Can be anything, like confidential, restricted, and public to more advanced categorization.                                                                                                                                           |
| criticalDataElement      | boolean | Critical Data Element Status | No       | True or false indicator; If element is considered a critical data element (CDE) then true else false.                                                                                                                                 |
| description              | string  | Description                  | No       | Description of the element.                                                                                                                                                                                                           |
| encryptedName            | string  | Encrypted Name               | No       | The element name within the dataset that contains the encrypted element value. For example, unencrypted element `email_address` might have an encryptedName of `email_address_encrypt`.                                               |
| enum                     | array   | Enum                         | No       | Enumeration of allowed values for this property. See [Enumerations](#schema-L425).                                                                                                                                                   |
| examples                 | array   | Example Values               | No       | List of sample element values.                                                                                                                                                                                                        |
| items                    | object  | Items                        | No       | List of items in an array (only applicable when `logicalType: array`).                                                                                                                                                                |
| logicalTypeOptions       | object  | Logical Type Options         | No       | Additional optional metadata to describe the logical type. See [Logical Type Options](#schema-L206) for more details about supported options for each `logicalType`.                                                         |
| map                      | object  | Map                          | No       | Key/value definition (required when `logicalType: map`). See [Maps](#schema-L298).                                                                                                                                                           |
| partitioned              | boolean | Partitioned                  | No       | Indicates if the element is partitioned; possible values are true and false.                                                                                                                                                          |
| partitionKeyPosition     | integer | Partition Key Position       | No       | If element is used for partitioning, the position of the partition element. Starts from 1. Example of `country, year` being partition columns, `country` has partitionKeyPosition 1 and `year` partitionKeyPosition 2. Default to -1. |
| physicalType             | string  | Physical Type                | No       | The physical element data type in the data source. For example, VARCHAR(2), DOUBLE, INT.                                                                                                                                              |
| primaryKey               | boolean | Primary Key                  | No       | Boolean value specifying whether the field is primary or not. Default is false.                                                                                                                                                       |
| primaryKeyPosition       | integer | Primary Key Position         | No       | If field is a primary key, the position of the primary key element. Starts from 1. Example of `account_id, name` being primary key columns, `account_id` has primaryKeyPosition 1 and `name` primaryKeyPosition 2. Default to -1.     |
| required                 | boolean | Required                     | No       | Indicates if the element may contain Null values; possible values are true and false. Default is false.                                                                                                                               |
| semanticType             | string  | Semantic Type                | No       | The semantic role the property plays in the data model. One of `column` (the default, a physical column), `measure` (an aggregated value such as `SUM(revenue)`, with the aggregation expression in `transformLogic`), or `dimension` (a categorical attribute for grouping and filtering). See RFC 0034.                                                                |
| transformDescription     | string  | Transform Description        | No       | Describes the transform logic in very simple terms.                                                                                                                                                                                   |
| transformLogic           | string  | Transform Logic              | No       | Logic used in the column transformation.                                                                                                                                                                                              |
| transformSourceObjects   | array   | Transform Sources            | No       | List of objects in the data source used in the transformation.                                                                                                                                                                        |
| unique                   | boolean | Unique                       | No       | Indicates if the element contains unique values; possible values are true and false. Default is false.                                                                                                                                |
| authoritativeDefinitions | array   | Authoritative Definitions    | No       | List of links to sources that provide more detail on element logic or values; examples would be URL to a git repo, documentation, a data catalog or another tool.                                                                     |


<a id="schema-L206"></a>

## Logical Type Options

Additional metadata options to more accurately define the data type.

| Logical Data Type   | Key              | Type    | UX Label           | Required | Description                                                                                                                                                                                                                                                        |
| ------------------- | ---------------- | ------- | ------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| array               | maxItems         | integer | Maximum Items      | No       | Maximum number of items.                                                                                                                                                                                                                                           |
| array               | minItems         | integer | Minimum Items      | No       | Minimum number of items.                                                                                                                                                                                                                                           |
| array               | uniqueItems      | boolean | Unique Items       | No       | If set to true, all items in the array are unique.                                                                                                                                                                                                                 |
| date/timestamp/time | format           | string  | Format             | No       | Format of the date. Follows the format as prescribed by [JDK DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html). Default value is using ISO 8601: 'YYYY-MM-DDTHH:mm:ss.SSSZ'. For example, format 'yyyy-MM-dd'. |
| date/timestamp/time | exclusiveMaximum | string  | Exclusive Maximum  | No       | All values must be strictly less than this value (values < exclusiveMaximum).                                                                                                                                                                                      |
| date/timestamp/time | exclusiveMinimum | string  | Exclusive Minimum  | No       | All values must be strictly greater than this value (values > exclusiveMinimum).                                                                                                                                                                                   |
| date/timestamp/time | maximum          | string  | Maximum            | No       | All date values are less than or equal to this value (values <= maximum).                                                                                                                                                                                          |
| date/timestamp/time | minimum          | string  | Minimum            | No       | All date values are greater than or equal to this value (values >= minimum).                                                                                                                                                                                       |
| timestamp/time      | timezone         | boolean | Timezone           | No       | Whether the timestamp defines the timezone or not. If true, timezone information is included in the timestamp.                                                                                                                                                     |
| timestamp/time      | defaultTimezone  | string  | Default Timezone   | No       | The default timezone of the timestamp. If timezone is not defined, the default timezone UTC is used.                                                                                                                                                               |
| integer/number      | exclusiveMaximum | number  | Exclusive Maximum  | No       | All values must be strictly less than this value (values < exclusiveMaximum).                                                                                                                                                                                      |
| integer/number      | exclusiveMinimum | number  | Exclusive Minimum  | No       | All values must be strictly greater than this value (values > exclusiveMinimum).                                                                                                                                                                                   |
| integer/number      | format           | string  | Format             | No       | Format of the value in terms of how many bits of space it can use and whether it is signed or unsigned (follows the Rust integer types).                                                                                                                           |
| integer/number      | maximum          | number  | Maximum            | No       | All values are less than or equal to this value (values <= maximum).                                                                                                                                                                                               |
| integer/number      | minimum          | number  | Minimum            | No       | All values are greater than or equal to this value (values >= minimum).                                                                                                                                                                                            |
| integer/number      | multipleOf       | number  | Multiple Of        | No       | Values must be multiples of this number. For example, multiple of 5 has valid values 0, 5, 10, -5.                                                                                                                                                                 |
| object              | maxProperties    | integer | Maximum Properties | No       | Maximum number of properties.                                                                                                                                                                                                                                      |
| object              | minProperties    | integer | Minimum Properties | No       | Minimum number of properties.                                                                                                                                                                                                                                      |
| object              | required         | array   | Required           | No       | Property names that are required to exist in the object.                                                                                                                                                                                                           |
| string              | format           | string  | Format             | No       | Provides extra context about what format the string follows. For example, password, byte, binary, email, uuid, uri, hostname, ipv4, ipv6.                                                                                                                          |
| string              | maxLength        | integer | Maximum Length     | No       | Maximum length of the string.                                                                                                                                                                                                                                      |
| string              | minLength        | integer | Minimum Length     | No       | Minimum length of the string.                                                                                                                                                                                                                                      |
| string              | pattern          | string  | Pattern            | No       | Regular expression pattern to define valid value. Follows regular expression syntax from ECMA-262 (<https://262.ecma-international.org/5.1/#sec-15.10.1>).                                                                                                         |
| vector              | dimensions       | integer | Dimensions         | Yes      | The fixed length of the vector. Positive integer. Examples: `384`, `768`, `1024`, `1536`, `3072`. See [Vectors](#schema-L386).                                                                                                                                        |
| vector              | elementType      | string  | Element Type       | No       | Numeric type of each element. One of `bfloat16`, `binary`, `float16`, `float32` (default), `float64`, `int8`, `uint8`. `binary` means each element is one bit (binary-quantized vectors).                                                                          |
| vector              | distanceMetric   | string  | Distance Metric    | No       | Intended similarity metric. One of `cosine`, `dotProduct`, `euclidean`, `hamming`, `manhattan`. Advisory — the physical index may differ.                                                                                                                          |
| vector              | embeddingModel   | string  | Embedding Model    | No       | Identifier of the model used to produce the vectors (e.g., `openai/text-embedding-3-small`, `cohere/embed-english-v3.0`).                                                                                                                                          |
| vector              | embeddingModelVersion | string | Embedding Model Version | No   | Version or revision of the embedding model, when the model identifier does not already carry one.                                                                                                                                                                 |
| vector              | normalized       | boolean | Normalized         | No       | `true` if vectors are L2-normalized before storage, which makes `cosine` and `dotProduct` equivalent. Default `false`.                                                                                                                                            |


<a id="schema-L242"></a>

### Expressing Date / Datetime / Timezone information

Given the complexity of handling various date and time formats (e.g., date, datetime, time, timestamp, timestamp with and without timezone), the existing `logicalType` options currently support  `date`, `timestamp`, and `time`. To specify additional temporal details, `logicalType` should be used in conjunction with `logicalTypeOptions.format`  or `physicalType` to define the desired format. Using `physicalType` allows for definition of your data-source specific data type.

```yaml
version: 1.0.0
kind: DataContract
id: 53581432-6c55-4ba2-a65f-72344a91553a
status: active
name: date_example
apiVersion: v3.2.0
schema:
  # Date Only
  - name: event_date
    logicalType: date
    logicalTypeOptions:
      format: "yyyy-MM-dd"
    examples:
      - "2024-07-10"

  # Date & Time (UTC)
  - name: created_at
    logicalType: timestamp
    logicalTypeOptions:
      format: "yyyy-MM-ddTHH:mm:ssZ"
    examples:
      - "2024-03-10T14:22:35Z"

  # Date & Time (Australia/Sydney)
  - name: created_at_sydney
    logicalType: timestamp
    logicalTypeOptions:
      format: "yyyy-MM-ddTHH:mm:ssZ"
      timezone: true
      defaultTimezone: "Australia/Sydney"
    examples:
      - "2024-03-10T14:22:35+10:00"

  # Time Only
  - name: event_start_time
    logicalType: time
    logicalTypeOptions:
      format: "HH:mm:ss"
    examples:
      - "08:30:00"

    # Physical Type with Date & Time (UTC)
  - name: event_date
    logicalType: timestamp
    physicalType: DATETIME
    logicalTypeOptions:
      format: "yyyy-MM-ddTHH:mm:ssZ"
    examples:
      - "2024-03-10T14:22:35Z"
```


<a id="schema-L298"></a>

## Maps

A property can declare `logicalType: map` to represent a key/value collection (also called a dictionary). The accompanying `map` block declares the type of the key and the type of the value. Both `key` and `value` are themselves property definitions and can carry the same metadata as any other property — `logicalType`, `description`, `logicalTypeOptions`, nested `properties` (for object values), `items` (for array values), and so on.


<a id="schema-L302"></a>

### Examples

**Simple map (string → string):**

```yaml
schema:
  - name: users
    properties:
      - name: user_preferences
        logicalType: map
        physicalType: "MAP<STRING, STRING>"
        description: User preference key-value pairs.
        map:
          key:
            logicalType: string
            description: Preference name.
          value:
            logicalType: string
            description: Preference value.
```

**Map with numeric values:**

```yaml
- name: daily_counts
  logicalType: map
  physicalType: "MAP<STRING, INT>"
  description: Daily metric counts keyed by metric name.
  map:
    key:
      logicalType: string
    value:
      logicalType: integer
      logicalTypeOptions:
        minimum: 0
```

**Map with object values:**

```yaml
- name: product_details
  logicalType: map
  physicalType: "MAP<STRING, STRUCT>"
  description: Product details keyed by product ID.
  map:
    key:
      logicalType: string
    value:
      logicalType: object
      properties:
        - name: name
          logicalType: string
        - name: price
          logicalType: number
        - name: quantity
          logicalType: integer
```

**Map with array values:**

```yaml
- name: tag_scores
  logicalType: map
  physicalType: "MAP<STRING, ARRAY<DOUBLE>>"
  description: Score arrays keyed by tag name.
  map:
    key:
      logicalType: string
    value:
      logicalType: array
      items:
        logicalType: number
```


<a id="schema-L376"></a>

### Definition

| Key       | Type   | UX label | Required                    | Description                                                                                                                                          |
| --------- | ------ | -------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| map       | object | Map      | Yes when `logicalType: map` | Key/value structure for a map property.                                                                                                              |
| map.key   | object | Key      | Yes                         | Definition of the map's key. Same shape as any property definition (typically `logicalType: string`).                                                |
| map.value | object | Value    | Yes                         | Definition of the map's value. Same shape as any property definition; supports nested `properties` (for objects), `items` (for arrays), `enum`, etc. |

`logicalType: map` was introduced in ODCS v3.2.0 ([RFC 0030](https://github.com/bitol-io/tsc/blob/main/rfcs/approved/odcs-v3.2.0/0030-maps.md)).


<a id="schema-L386"></a>

## Vectors

A property can declare `logicalType: vector` to describe a fixed-dimension dense numeric array used for embeddings and similarity search (RAG, semantic matching). The shape is captured with `logicalTypeOptions`: `dimensions` (required), and the optional `elementType`, `distanceMetric`, `normalized`, `embeddingModel`, and `embeddingModelVersion`. The outer `physicalType` still carries the target system's native column syntax (e.g. `vector(1536)`, `VECTOR(FLOAT, 1536)`).


<a id="schema-L390"></a>

### Examples

**Minimal — a single embedding column:**

```yaml
schema:
  - name: products
    properties:
      - name: description_embedding
        logicalType: vector
        required: true
        logicalTypeOptions:
          dimensions: 1536
```

**Detailed — a normalized OpenAI embedding with cosine similarity:**

```yaml
- name: body_embedding
  logicalType: vector
  physicalType: vector(1536)
  required: true
  logicalTypeOptions:
    dimensions: 1536
    elementType: float32
    distanceMetric: cosine
    normalized: true
    embeddingModel: openai/text-embedding-3-small
    embeddingModelVersion: "2024-01-25"
```

`dimensions` is required whenever `logicalType: vector`. See [Logical Type Options](#schema-L206) for the full list of options.

`logicalType: vector` was introduced in ODCS v3.2.0 ([RFC 0042](https://github.com/bitol-io/tsc/blob/main/rfcs/approved/odcs-v3.2.0/0042-vector-type.md)).


<a id="schema-L425"></a>

## Enumerations

A property can declare an `enum` to constrain its value to a fixed set of allowed entries. Each entry is an object with at least a `value` and may carry a label, identifier, description, tags, custom properties, and authoritative definitions.


<a id="schema-L429"></a>

### Example

```yaml
schema:
  - name: orders
    properties:
      - name: status
        logicalType: string
        enum:
          - value: pending
            label: Pending
            description: The order has been received but not yet processed.
            tags: ['initial']
          - value: processing
            label: Processing
            tags: ['active']
          - value: shipped
            label: Shipped
            tags: ['terminal', 'success']
          - value: cancelled
            label: Cancelled
            tags: ['terminal']

      - name: priority
        logicalType: integer
        required: false
        enum:
          - value: 1
            label: One
            description: Highest ranked
          - value: 2
            label: Two
          - value: 3
            label: Three
            description: Lowest ranked
```


<a id="schema-L466"></a>

### Definition

| Key                             | Type   | UX label                  | Required | Description                                                                                                                                          |
| ------------------------------- | ------ | ------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum                            | array  | Enum                      | No       | Array of allowed values for the property. Must contain at least one entry; entries must be unique.                                                   |
| enum[].description              | string | Description               | No       | Optional description of what this enum value represents.                                                                                             |
| enum[].id                       | string | ID                        | No       | A unique identifier for stable, refactor-safe references. See [References](#references-L1) for more details.                                        |
| enum[].label                    | string | Label                     | No       | Human-readable label for the value, suitable for UI display (e.g., dropdowns).                                                                       |
| enum[].value                    | any    | Value                     | Yes      | The allowed value. Must be a non-collection scalar (string, number, integer, boolean) compatible with the property's `logicalType`.                  |
| enum[].authoritativeDefinitions | array  | Authoritative Definitions | No       | Authoritative definitions for this enum value. Same structure as elsewhere in the standard.                                                          |
| enum[].tags                     | array  | Tags                      | No       | List of tags assigned to this enum value (e.g., `terminal`, `active`, `deprecated`). See [Tags](#tags-L1).                                          |
| enum[].customProperties         | array  | Custom Properties         | No       | Custom properties attached to this enum value (e.g., translations, locale-specific labels). Same structure as the standard `customProperties` block. |

`enum` was introduced in ODCS v3.2.0 ([RFC 0033](https://github.com/bitol-io/tsc/blob/main/rfcs/approved/odcs-v3.2.0/0033-enum.md)).


<a id="schema-L481"></a>

## Synonyms

Any element (a schema object or a property) may declare `synonyms`: alternative names that help catalogs, AI/LLM tools, and natural language interfaces resolve business vocabulary to the underlying object. Each entry is an object carrying the synonymous term and optional metadata (locale, source, lifecycle status). `synonyms` is allowed only on schema objects and properties; tools MUST NOT accept it at other locations.


<a id="schema-L485"></a>

### Example

```yaml
schema:
  - name: turnover
    physicalName: metrics_turnover
    synonyms:
      - synonym: Sales metrics
      - synonym: Chiffre d'affaires
        locale: fr-FR
    properties:
      - name: total_turnover_euros
        semanticType: measure
        logicalType: number
        transformLogic: SUM(turnover_euros)
        businessName: TurnOver (Euros)
        synonyms:
          - synonym: TO
            description: Common abbreviation used by the finance team.
            source: finance-team
          - synonym: Sales
            locale: en-US
          - id: sales-fr
            synonym: Chiffre d'affaires
            locale: fr-FR
            description: French equivalent used in European subsidiaries.
```


<a id="schema-L513"></a>

### Definition

| Key                         | Type   | UX label          | Required | Description                                                                                                                            |
| --------------------------- | ------ | ----------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| synonyms                    | array  | Synonyms          | No       | A list of alternative names for the element.                                                                                           |
| synonyms[].description      | string | Description       | No       | Short human-readable note about when or why this synonym is used.                                                                      |
| synonyms[].id               | string | ID                | No       | Stable identifier for the synonym, useful when referencing or deduplicating synonyms across tools. See [References](#references-L1).  |
| synonyms[].locale           | string | Locale            | No       | [BCP 47](https://datatracker.ietf.org/doc/html/rfc5646) language tag (e.g., `en-US`, `fr-FR`) when the synonym is language-specific.    |
| synonyms[].source           | string | Source            | No       | Origin of the synonym (e.g., `glossary`, `finance-team`, `legacy-system`).                                                             |
| synonyms[].status           | string | Status            | No       | Lifecycle status of the synonym (e.g., `active`, `deprecated`).                                                                        |
| synonyms[].synonym          | string | Synonym           | Yes      | The synonymous term.                                                                                                                   |
| synonyms[].customProperties | array  | Custom Properties | No       | Custom properties attached to this synonym. Same structure as the standard `customProperties` block.                                   |

`synonyms` was introduced in ODCS v3.2.0 ([RFC 0041](https://github.com/bitol-io/tsc/blob/main/rfcs/approved/odcs-v3.2.0/0041-synonyms.md)).

[Back to TOC](#README-L1)


<a id="schema-L530"></a>

## Deprecated

Any element (a schema object or a property, including nested properties) may set the optional `deprecated` boolean to signal that it is no longer recommended for use. It defaults to `false` when not specified. Deprecated elements remain documented and validated for backward compatibility; implementations MAY warn when they are used. Use the `description` field to point to a replacement and provide migration guidance.

```yaml
schema:
  - name: customers
    logicalType: object
    properties:
      - name: email_address
        logicalType: string
        deprecated: true
        description: "DEPRECATED: use 'primary_email' instead. Will be removed in the next major version."
      - name: primary_email
        logicalType: string
        description: "Primary email address for the customer."
```

| Key          | Type    | UX label   | Required | Description                                                                                          |
| ------------ | ------- | ---------- | -------- | ---------------------------------------------------------------------------------------------------- |
| deprecated   | boolean | Deprecated | No       | Indicates this element is deprecated and should not be used in new implementations. Defaults to `false`. |

`deprecated` was introduced in ODCS v3.2.0 ([RFC 0051](https://github.com/bitol-io/tsc/blob/main/rfcs/approved/odcs-v3.2.0/0051-deprecated-flag.md)).

[Back to TOC](#README-L1)

Original MD: [context.md](../source/docs/context.md#L1-L93).

<a id="context-L1"></a>

> Collector metadata display: original leading YAML frontmatter, source lines 1–4; not an upstream body heading.


```yaml
---
title: "Context"
description: "AI and semantic context guidance for the data contract."
---
```


<!--
Copyright 2026 The Bitol Contributors
SPDX-License-Identifier: Apache-2.0
-->


<a id="context-L11"></a>

# Context

Added in **ODCS v3.2.0** (RFC-0038). The `context` block provides structured, human- and machine-readable guidance for AI agents, LLMs, BI tools, and semantic layer platforms. It is optional and additive.

In ODCS, `context` is applicable at two levels:

- **Data contract (top level)** — overall AI context for the contract: domain, purpose, known limitations.
- **Schema object** — guidance on how to use a specific table or API object: join hints, cardinality notes, time-range guidance.

The `context` block may also be provided as a plain string, equivalent to providing only `instructions`.

[Back to TOC](#README-L1)


<a id="context-L24"></a>

## Examples


<a id="context-L26"></a>

### Contract level

```yaml
context:
  instructions: >
    This contract governs the turnover dataset for the EMEA sales domain.
    Use it for revenue analysis, order volume trends, and basket value
    benchmarking. Do not use it for individual customer PII queries.
  verifiedStatements:
    - question: "What was total revenue in France last quarter?"
    - id: revenue-last-year
      question: "What was the total revenue last year?"
      answer: "Query ${total_turnover_euros} grouped by year using ${turnover_ts_dim}."
  constraints:
    - id: no-individual-order-exposure
      constraint: "Do not expose individual order details; aggregate to at least country level."
      tags: ['gdpr', 'pii']
      authoritativeDefinitions:
        - url: https://example.com/MyGlobalAndMarvelousOntology
          type: Ontology
          description: Link to the ontology
        - url: https://example.com/MySpecificAndWonderfulGlossary
          type: Glossary
          description: Link to the glossary
        - url: https://example.com/OneOfManyTaxonomy
          type: Taxonomy
          description: Link to the taxonomy
    - constraint: "Do not join with customer PII tables without explicit data access approval."
```


<a id="context-L56"></a>

### Schema object level

```yaml
schema:
  - name: turnover
    physicalName: metrics_turnover
    context:
      instructions: >
        This table contains pre-aggregated turnover metrics at order granularity.
        Always filter by turnover_ts when querying time ranges.
      verifiedStatements:
        - question: "What is the total revenue for Germany in Q1 2025?"
      constraints:
        - constraint: "Do not query without a date range filter; the table is unbounded."
```


<a id="context-L72"></a>

## Definitions

| Key                                                   | Type   | UX label                  | Required | Description                                                                                                                                                                                                          |
| ----------------------------------------------------- | ------ | ------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| context.instructions                                  | string | Instructions              | No       | Natural language guidance for AI agents and tools on how to use this entity. Equivalent to a system prompt scoped to this level.                                                                                     |
| context.constraints                                   | array  | Constraints               | No       | Negative guidance: what AI agents must NOT do with this entity.                                                                                                                                                      |
| context.constraints[].**constraint**                  | string | Constraint                | Yes      | The constraint text (negative guidance for AI agents).                                                                                                                                                               |
| context.constraints[].id                              | string | ID                        | No       | Stable identifier for the constraint.                                                                                                                                                                                |
| context.constraints[].authoritativeDefinitions        | array  | Authoritative Definitions | No       | Links to policy, regulation, glossary, or other authoritative sources backing this constraint.                                                                                                                       |
| context.constraints[].tags                            | array  | Tags                      | No       | Free-form tags for filtering, grouping, or routing constraints.                                                                                                                                                      |
| context.constraints[].customProperties                | array  | Custom Properties         | No       | Custom properties.                                                                                                                                                                                                   |
| context.verifiedStatements                            | array  | Verified Statements       | No       | Canonical business questions, each with an optional curated answer. Entries with `answer` should be returned verbatim when a query is semantically close; entries without `answer` are sample questions for priming. |
| context.verifiedStatements[].answer                   | string | Answer                    | No       | The expected response or result description.                                                                                                                                                                         |
| context.verifiedStatements[].id                       | string | ID                        | No       | Stable identifier for the entry.                                                                                                                                                                                     |
| context.verifiedStatements[].**question**             | string | Question                  | Yes      | The canonical question.                                                                                                                                                                                              |
| context.verifiedStatements[].authoritativeDefinitions | array  | Authoritative Definitions | No       | Links to glossary, taxonomy, ontology, or other authoritative sources backing this entry.                                                                                                                            |
| context.verifiedStatements[].tags                     | array  | Tags                      | No       | Free-form tags for filtering, grouping, or routing entries.                                                                                                                                                          |
| context.verifiedStatements[].customProperties         | array  | Custom Properties         | No       | Custom properties.                                                                                                                                                                                                   |

For the full normative specification of cascading behavior between levels, see [RFC-0038](https://github.com/bitol-io/tsc/blob/main/rfcs/approved/odcs-v3.2.0/0038-context.md).

[Back to TOC](#README-L1)

Original MD: [references.md](../source/docs/references.md#L1-L416).

<a id="references-L1"></a>

> Collector metadata display: original leading YAML frontmatter, source lines 1–4; not an upstream body heading.


```yaml
---
title: "References"
description: "This section describes how to reference elements within a data contract schema."
---
```


<!--
Copyright 2026 The Bitol Contributors
SPDX-License-Identifier: Apache-2.0
-->


<a id="references-L11"></a>

# References

This section describes how to reference elements within a data contract schema. References enable you to create relationships between different parts of your data contract. This section is new in ODCS v3.1.0.

!!! info

    References are currently only supported for foreign key relationships.


[Back to TOC](#README-L1)


<a id="references-L22"></a>

## Fully Qualified Reference Notation

ODCS uses a fully qualified notation with the `id` field and slash-separated paths for stable, refactor-safe references.

**Format:** `<section>/<id>[/properties/<property_id>]`

**Characteristics:**
- Uses the `id` field (optional, recommended for references)
- Slash-separated path
- Stable across renames and refactoring
- Resilient to array reordering
- Explicit and unambiguous

**When to use:**
- Long-lived production contracts
- Complex contracts with many references
- When refactoring is expected
- Cross-contract references


<a id="references-L41"></a>

### Allowed characters in an `id`

An `id` cannot contain any of the following characters:

```text
. # / \ @ ! % & ^
```

Whitespace is not allowed either. Every other character is legal, including `:`, so namespaced
identifiers such as `fdir:ISU:TAD` or `urn:uuid:0f6d2c11-4a7e-4a1d-9b3f-8c5e2a7d1b40` are valid ids
and may appear in a fully qualified reference.

The three structural characters are denied for a reason: `.` separates the segments of a shorthand
reference (`table_name.column_name`, see
[Reference Notation for Foreign Keys](#references-L147)), `/` separates the
segments of a fully qualified reference, and `#` marks entry into an external contract file.
Allowing them inside an id would make a reference ambiguous to parse.


<a id="references-L59"></a>

## Reference Structure

A fully formatted reference follows this structure:

```yaml
<file><anchor><item-path-within-contract>
```

Where:

* **`<file>`**: Path to the contract file (optional for same-contract references)
* **`<anchor>`**: '#' symbol to mark entry into a contract (optional for same-contract)
* **`<item-path-within-contract>`**: The fully qualified path within the contract


<a id="references-L73"></a>

## External Contract References

To identify a contract, use one of these formats:

```yaml
# Same folder as current contract
data-contract-v1.yaml

# Full path
file:///path/to/data-contract-v1.yaml

# URL
https://example.com/data-contract-v1.yaml

# Relative path
../../path/to/data-contract-v1.yaml
```


<a id="references-L91"></a>

## Reference Examples


<a id="references-L93"></a>

### Same Contract References

```yaml
# Reference to a schema object
'schema/customers_tbl'

# Reference to a property
'schema/customers_tbl/properties/cust_id_pk'

# Reference to a nested property
'schema/accounts_tbl/properties/address_field/properties/street_field'
```

When referencing elements within the same contract, the file component can be omitted.


<a id="references-L108"></a>

### External Contract References

```yaml
# Reference to an element in an external contract
'customer-contract.yaml#/schema/customers_tbl/properties/cust_id_pk'

# Reference to a nested property in an external contract
'external-contract.yaml#/schema/accounts_tbl/properties/address_field/properties/street_field'
```


<a id="references-L118"></a>

## Relationships between properties (Foreign Keys)

Properties can define relationships to other properties, enabling you to specify foreign key constraints and other data relationships.


<a id="references-L122"></a>

### Quick Overview

Relationships can be defined in two ways:

1. **At the property level** - Define relationships directly on a property (the `from` field is implicit and must NOT be specified)
2. **At the schema level** - Define relationships between any properties (both `from` and `to` are required)


<a id="references-L129"></a>

### Important Rules

* **Property-level relationships**: The `from` field is implicit (derived from the property context) and must NOT be specified
* **Schema-level relationships**: Both `from` and `to` fields are required
* **Type consistency**: Both `from` and `to` must be the same type - either both strings (single column) or both arrays (composite keys). Mixing types is not allowed
* **Array length validation**: When using arrays for composite keys, both arrays must have the same number of elements. This is validated at runtime by implementations


<a id="references-L136"></a>

### Field Definitions

| Key                              | Type   | UX Label          | Required          | Description                                                                       |
| -------------------------------- | ------ | ----------------- | ----------------- | --------------------------------------------------------------------------------- |
| relationships                    | array  | Relationships     | No                | Array of relationship definitions                                                 |
| relationships[].from             | string | From              | Context-dependent | Source property reference - Required at schema level, forbidden at property level |
| relationships[].id               | string | ID                | No                | Optional stable identifier for the relationship, unique within its containing `relationships` array. Recommended for elements that will be referenced. Cannot contain: `.` `#` `/` `\` `@` `!` `%` `&` `^` (RFC 0047) |
| relationships[].to               | string | To                | Yes               | Target property reference using `schema.property` notation                        |
| relationships[].type             | string | Type              | No                | Type of relationship (defaults to `foreignKey`)                                   |
| relationships[].customProperties | array  | Custom Properties | No                | Additional metadata about the relationship                                        |


<a id="references-L147"></a>

### Reference Notation for Foreign Keys

Foreign key relationships support two reference notations:

**Fully Qualified Notation**

Uses the `id` field with slash-separated paths for stable references:

* `schema/users_tbl/properties/user_id_pk` - References the property with id `user_id_pk` in schema with id `users_tbl`
* `schema/accounts_tbl/properties/address_field/properties/street_field` - References nested properties

**Shorthand Notation**

For improved readability in foreign key relationships, ODCS also supports shorthand notation using the `name` field with dot-separated paths:

* `users.id` - References the `id` property in the `users` schema
* `accounts.address.street` - References nested properties

!!! note

    Shorthand notation is only supported for foreign key relationships. For all other references, use fully qualified notation.

**When to use each:**
- **Fully qualified**: Production contracts, cross-contract references, when refactoring is expected
- **Shorthand**: Simple contracts, development, when names are stable

**Composite keys**: Use arrays to define composite keys (arrays must have matching lengths)


<a id="references-L175"></a>

## Examples


<a id="references-L177"></a>

### Example 1: Simple Foreign Key (Property Level)

When defining a relationship at the property level, the `from` field is implicit and must NOT be specified:

```yaml
schema:
  - id: users_tbl
    name: users
    properties:
      - id: user_id_field
        name: user_id
        relationships:
          # Fully qualified notation (uses id, stable)
          - to: schema/accounts_tbl/properties/owner_id_field

          # OR shorthand notation (uses name, concise)
          - to: accounts.owner_id
            # Note: DO NOT include 'from' field at property level
```


<a id="references-L197"></a>

### Example 2: Multiple Relationships

A property can have multiple relationships:

```yaml
schema:
  - id: orders_tbl
    name: orders
    properties:
      - id: order_customer_id
        name: customer_id
        relationships:
          # Fully qualified notation
          - to: schema/customers_tbl/properties/cust_id_pk
          - to: schema/loyalty_tbl/properties/member_customer_id

          # OR shorthand notation
          - to: customers.id
          - to: loyalty_members.customer_id
```


<a id="references-L218"></a>

### Example 3: Schema-Level Relationships

Define relationships at the schema level when you need explicit `from` and `to`. Both fields are REQUIRED at this level:

```yaml
schema:
  - id: users_tbl
    name: users
    relationships:
      # Fully qualified notation (stable)
      - from: schema/users_tbl/properties/user_account_id
        to: schema/accounts_tbl/properties/acct_id_pk
        type: foreignKey

      # OR shorthand notation (concise)
      - from: users.account_id
        to: accounts.id
        type: foreignKey
```


<a id="references-L238"></a>

### Example 4: Nested Properties

Reference nested properties:

```yaml
schema:
  - id: users_tbl
    name: users
    properties:
      - id: user_id_pk
        name: id
        relationships:
          # Fully qualified notation
          - to: schema/accounts_tbl/properties/address_field/properties/postal_code_field

          # OR shorthand notation
          - to: accounts.address.postal_code
```


<a id="references-L257"></a>

### Example 5: Composite Keys

For composite foreign keys, use arrays. **Important**: Both `from` and `to` must be arrays with the same number of elements:

```yaml
schema:
  - id: order_items_tbl
    name: order_items
    relationships:
      # Fully qualified notation (stable)
      - type: foreignKey
        from:
          - schema/order_items_tbl/properties/item_order_id
          - schema/order_items_tbl/properties/item_product_id
        to:
          - schema/product_inventory_tbl/properties/inv_order_id
          - schema/product_inventory_tbl/properties/inv_product_id

      # OR shorthand notation (concise)
      - type: foreignKey
        from:
          - order_items.order_id
          - order_items.product_id
        to:
          - product_inventory.order_id
          - product_inventory.product_id
```


<a id="references-L285"></a>

### Example 6: Invalid Configurations

Here are examples of invalid configurations that will be rejected:

```yaml
# INVALID: 'from' specified at property level
schema:
  - name: users
    properties:
      - name: user_id
        relationships:
          - from: users.user_id  # ERROR: 'from' not allowed at property level
            to: accounts.id
```
```yaml
# INVALID: Mismatched array types
schema:
  - name: orders
    relationships:
      - from: orders.id          # ERROR: 'from' is string but 'to' is array
        to:
          - items.order_id
          - items.line_num
```
```yaml
# INVALID: Different array lengths (caught at runtime)
schema:
  - name: orders
    relationships:
      - from:                    # 'from' has 2 elements
          - orders.id
          - orders.customer_id
        to:                      # 'to' has 3 elements (runtime validation will fail)
          - items.order_id
          - items.customer_id
          - items.line_num
```
```yaml
# INVALID: Missing 'from' at schema level
schema:
  - name: orders
    relationships:
      - to: customers.id         # ERROR: 'from' is required at schema level
```


<a id="references-L330"></a>

### Complete Example

Here's a comprehensive example showing various relationship patterns with both notations:

```yaml
schema:
  - id: users_tbl
    name: users
    properties:
      - id: user_id_pk
        name: id
        logicalType: integer
        relationships:
          # Fully qualified notation
          - to: schema/accounts_tbl/properties/acct_user_id
            description: "Fully qualified reference using id fields"

          # Shorthand notation
          - to: accounts.user_id
            description: "Shorthand reference using name fields"

          # With custom properties
          - to: schema/departments_tbl/properties/dept_manager_id
            customProperties:
              - property: cardinality
                value: "one-to-many"
              - property: label
                value: "manages"

          # To external contract (fully qualified)
          - to: https://example.com/data-contract-v1.yaml#/schema/profiles_tbl/properties/profile_user_id
            customProperties:
              - property: description
                value: "Externally referenced contract (fully qualified)"

          # To external contract (shorthand)
          - to: https://example.com/data-contract-v1.yaml#/profiles.user_id
            customProperties:
              - property: description
                value: "Externally referenced contract (shorthand)"

      - id: user_account_number
        name: account_number
        logicalType: string

    # Schema-level composite key relationship
    relationships:
      # Fully qualified notation
      - type: foreignKey
        from:
          - schema/users_tbl/properties/user_id_pk
          - schema/users_tbl/properties/user_account_number
        to:
          - schema/accounts_tbl/properties/acct_user_id
          - schema/accounts_tbl/properties/acct_number

      # OR shorthand notation
      - type: foreignKey
        from:
          - users.id
          - users.account_number
        to:
          - accounts.user_id
          - accounts.account_number

  - id: accounts_tbl
    name: accounts
    properties:
      - id: acct_user_id
        name: user_id
        logicalType: integer
      - id: acct_number
        name: account_number
        logicalType: string
      - id: acct_address
        name: address
        logicalType: object
        properties:
          - id: addr_street
            name: street
            logicalType: string
          - id: addr_postal_code
            name: postal_code
            logicalType: string
```

[Back to TOC](#README-L1)

Original MD: [data-quality.md](../source/docs/data-quality.md#L1-L357).

<a id="data-quality-L1"></a>

> Collector metadata display: original leading YAML frontmatter, source lines 1–4; not an upstream body heading.


```yaml
---
title: "Data Quality"
description: "his section describes data quality rules & parameters."
---
```


<!--
Copyright 2026 The Bitol Contributors
SPDX-License-Identifier: Apache-2.0
-->


<a id="data-quality-L11"></a>

# Data Quality

This section describes data quality rules & parameters. They are tightly linked to the schema described in the previous section.

Data quality rules support different levels/stages of data quality attributes:

* **Text**: A human-readable text that describes the quality of the data.
* **Library** : A maintained library of commonly used quality metrics such as `rowCount`, `nullValues`, `invalidValues`, and more.
* **SQL**: An individual SQL query that returns a value that can be compared.
* **Custom**: Quality attributes that are vendor-specific, such as Soda, Great Expectations, dbt tests, dbx, or Montecarlo monitors.

[Back to TOC](#README-L1)


<a id="data-quality-L24"></a>

## Text

A human-readable text that describes the quality of the data. Later in the development process, these might be translated into an executable check (such as `sql`), a library metric, or checked through an AI engine.

```yaml
quality:
  - id: email_verified_text
    type: text
    description: The email address was verified by the system.
```


<a id="data-quality-L35"></a>

## Library

ODCS provides a set of predefined metrics commonly used in data quality checks, designed to be compatible with all major data quality engines. This simplifies the work for data engineers by eliminating the need to manually write SQL queries. This section has been improved in ODCS v3.1.0.

The type for library metrics is `library`, which can be omitted, if a `metric` property is defined.

These metrics return a numeric value come with an operator to compare if the metric is valid and in the expected range.

Some metrics require additional parameters, which can be defined in the `arguments` property.

Example:

```yaml
properties:
  - name: order_id
    quality:
      - id: order_id_no_nulls
        type: library
        metric: nullValues
        mustBe: 0
        unit: rows
        description: "There must be no null values in the column."
```

is equal to:

```yaml
properties:
  - name: order_id
    quality:
      - id: order_id_no_nulls_simplified
        metric: nullValues
        mustBe: 0
        description: "There must be no null values in the column."
```


<a id="data-quality-L71"></a>

### Metrics

| Metric            | Level    | Description                                                    | Arguments                                                        | Arguments Example                                                    |
|-------------------|----------|----------------------------------------------------------------|------------------------------------------------------------------|----------------------------------------------------------------------|
| `nullValues`      | Property | Counts null values in a column/field                           | None                                                             |                                                                      |
| `missingValues`   | Property | Counts values considered as missing (empty strings, N/A, etc.) | `missingValues`: Array of values considered missing              | `missingValues: [null, '', 'N/A']`                                   |
| `invalidValues`   | Property | Counts values that don't match valid criteria                  | `validValues`: Array of valid values<br>`pattern`: Regex pattern | `validValues: ['pounds', 'kg']`<br>`pattern: '^[A-Z]{2}[0-9]{2}...'` |
| `duplicateValues` | Property | Counts duplicate values in a column                            | None                                                             |                                                                      |
| `duplicateValues` | Schema   | Counts duplicate values across multiple columns                | `properties`: Array of property names                            | `properties: ['tenant_id', 'order_id']`                              |
| `rowCount`        | Schema   | Counts total number of rows in a table/object store            | None                                                             |                                                                      |


<a id="data-quality-L82"></a>

#### Null Values

Check that the count of null values is within range.

```yaml
properties:
  - name: customer_id
    quality:
    - id: customer_id_no_nulls
      metric: nullValues
      mustBe: 0
      description: "There must be no null values in the column."
```

Example with percent:

```yaml
properties:
  - name: order_status
    quality:
    - id: order_status_null_percent
      metric: nullValues
      mustBeLessThan: 1
      unit: percent
      description: "There must be less than 1% null values in the column."
```


<a id="data-quality-L109"></a>

#### Missing Values

Check that the missing values are within range.

In the argument `missingValues`, a list of values that are considered to be missing.

```yaml
properties:
  - name: email_address
    quality:
    - id: email_missing_values
      metric: missingValues
      arguments:
        missingValues: [null, '', 'N/A', 'n/a']
      mustBeLessThan: 100
      unit: rows # rows (default) or percent
```


<a id="data-quality-L127"></a>

#### Invalid Values

Check that the value is within a defined set or matching a pattern.

```yaml
properties:
  - name: line_item_unit
    quality:
      - id: line_item_unit_valid_values
        metric: invalidValues
        arguments:
          validValues: ['pounds', 'kg']
        mustBeLessThan: 5
        unit: rows
```

Using a pattern:

```yaml
properties:
  - name: iban
    quality:
    - id: iban_pattern_check
      metric: invalidValues
      mustBe: 0
      description: "The value must be an IBAN."
      arguments:
      pattern: '^[A-Z]{2}[0-9]{2}[A-Z0-9]{4}[0-9]{7}([A-Z0-9]?){0,16}$'
```


<a id="data-quality-L157"></a>

#### Duplicate Values

No more than 10 duplicate names.

```yaml
properties:
  - name: email_address
    quality:
    - id: email_duplicate_values
      metric: duplicateValues
      mustBeLessThan: 10
      unit: rows
      description: "There must be less than 10 duplicate values in the column."
```

Duplicates should be less than 1%.

```yaml
properties:
  - name: phone_number
    quality:
    - id: phone_duplicate_percent
      metric: duplicateValues
      mustBeLessThan: 1
      unit: percent
```


<a id="data-quality-L184"></a>

#### Row count (Schema-Level)

Calculates the number of rows (usually in a table) and compares it to an absolute operator.

```yaml
schema:
  - name: orders
    quality:
      - id: orders_row_count
        metric: rowCount
        mustBeBetween: [100, 120]
```


<a id="data-quality-L197"></a>

#### Duplicates (Schema-Level)

Checks for duplicate rows based on a combination of properties.
This is useful for validating compound keys where uniqueness is defined not by a single column but by multiple columns together.

```yaml
schema:
  - name: orders
    quality:
      - id: orders_unique_tenant_order
        description: The combination of tenant_id and order_id must be unique
        metric: duplicateValues
        mustBe: 0
        arguments:
          properties: # Properties refer to the property in the schema.
            - tenant_id
            - order_id
```


<a id="data-quality-L216"></a>

## SQL

A single SQL query that returns either a numeric or boolean value for comparison. The query must be written in the SQL dialect specific to the provided server. `{object}` and `{property}` are automatically replaced by the current object (in the case of SQL on a relational database, the table or view name) and the current property name (in the case of SQL on a relational database, the column).

```yaml
quality:
  - id: sql_count_not_null
    type: sql
    query: |
      SELECT COUNT(*) FROM {object} WHERE {property} IS NOT NULL
    mustBeLessThan: 3600
```


<a id="data-quality-L229"></a>

## Custom

Custom rules allow for vendor-specific checks, including tools like Soda, Great Expectations, dbt-tests, Montecarlo, and others. Any format for properties is acceptable, whether it's written in YAML, JSON, XML, or even uuencoded binary. They are an intermediate step before the vendor accepts ODCS natively.


<a id="data-quality-L233"></a>

### Soda Example

```yaml
quality:
- id: soda_duplicate_percent
  type: custom
  engine: soda
  implementation: |
        type: duplicate_percent  # Block
        columns:                 # passed as-is
          - carrier              # to the tool
          - shipment_numer       # (Soda in this situation)
        must_be_less_than: 1.0   #
```


<a id="data-quality-L248"></a>

### Great Expectation Example

```yaml
quality:
- id: row_count_btwn_10_50
  type: custom
  engine: greatExpectations
  implementation: |
    type: expect_table_row_count_to_be_between # Block
    kwargs:                                    # passed as-is
      minValue: 10000                          # to the tool
      maxValue: 50000                          # (Great Expectations in this situation)
```


<a id="data-quality-L262"></a>

## Scheduling

The data contract can contain scheduling information for executing the rules. You can use `schedule` and `scheduler` for those operation. In previous versions of ODCS, the only allowed scheduler was cron and its syntax was `scheduleCronExpression`.

```yaml
quality:
  - id: count_less_than_3600
    type: sql
    query: |
      SELECT COUNT(*) FROM {object} WHERE {property} IS NOT NULL
    mustBeLessThan: 3600
    scheduler: cron
    schedule: 0 20 * * *
```


<a id="data-quality-L277"></a>

## Definitions

Acronyms:

* DQ: data quality.

| Key                                | Type   | UX label                   | Required | Description                                                                                                                                                                                |
| ---------------------------------- | ------ | -------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| quality                            | array  | Quality                    | No       | Quality tag with all the relevant information for rule setup and execution.                                                                                                                |
| quality[].\<operator>              | number | See below                  | No       | Multiple values are allowed for the **property**, the value is the one to compare to.                                                                                                      |
| quality[].arguments                | object | Arguments                  | No       | Additional arguments for the metric, if needed.                                                                                                                                            |
| quality[].businessImpact           | string | Business Impact            | No       | Consequences of the rule failure.                                                                                                                                                          |
| quality[].description              | string | Description                | No       | Describe the quality check to be completed.                                                                                                                                                |
| quality[].dimension                | string | Dimension                  | No       | The key performance indicator (KPI) or dimension for data quality. Valid values are listed after the table.                                                                                |
| quality[].engine                   | string | Third-party DQ Engine      | No       | Required for `custom` DQ rule: name of the third-party engine being used. Any value is authorized here but common values are `soda`, `greatExpectations`, `montecarlo`, etc.               |
| quality[].id                       | string | ID                         | No       | A unique identifier for the element used to create stable, refactor-safe references. Recommended for elements that will be referenced. See [References](#references-L1) for more details. |
| quality[].implementation           | string | Third-party Implementation | No       | A text (non-parsed) block of code required for the third-party DQ engine to run.                                                                                                           |
| quality[].method                   | string | Method                     | No       | Values are open and include `reconciliation`.                                                                                                                                              |
| quality[].metric                   | string | Metric name                | No       | Required for `library`: the name of the metric to be calculated and compared.                                                                                                              |
| quality[].name                     | string | Name                       | No       | A short name for the rule.                                                                                                                                                                 |
| quality[].query                    | string | SQL Query                  | No       | Required for `sql` DQ rules: the SQL query to be executed. Note that it should match the target SQL engine/database, no transalation service are provided here.                            |
| quality[].rule                     | string | Rule name                  | No       | Deprecated, use `metric` instead.                                                                                                                                                          |
| quality[].schedule                 | string | Scheduler Configuration    | No       | Configuration information for the scheduling tool, for `cron` a possible value is `0 20 * * *`.                                                                                            |
| quality[].scheduler                | string | Scheduler                  | No       | Name of the scheduler, can be `cron` or any tool your organization support.                                                                                                                |
| quality[].severity                 | string | Severity                   | No       | The severity of the DQ rule.                                                                                                                                                               |
| quality[].type                     | string | Type                       | No       | Type of DQ rule. Valid values are `library` (default), `text`, `sql`, and `custom`.                                                                                                        |
| quality[].unit                     | string | Unit                       | No       | Unit the rule is using, popular values are `rows` or `percent`.                                                                                                                            |
| quality[].authoritativeDefinitions | array  | Authoritative Definitions  | No       | Authoritative definitions indicate the link to external definition. Follows the same structure as any authoritative definitions block.                                                     |
| quality[].tags                     | array  | Tags                       | No       | Tags applied to the quality rule. See [Tags](#tags-L1).                                                                                                                                   |
| quality[].customProperties         | array  | Custom Properties          | No       | Additional properties required for rule execution. Follows the same structure as any custom properties block.                                                                              |


<a id="data-quality-L308"></a>

### Valid Values for Dimension

Those data quality dimensions are used for classification and reporting in data quality. Valid values are:

* `accuracy` (synonym `ac`),
* `completeness` (synonym `cp`),
* `conformity` (synonym `cf`),
* `consistency` (synonym `cs`),
* `coverage` (synonym `cv`),
* `timeliness` (synonym `tm`),
* `uniqueness` (synonym `uq`).


<a id="data-quality-L320"></a>

### Valid Properties for Operator

The operator specifies the condition to validate a metric or result of a SQL query.

| Operator                 | Type                | Math Symbol | Example                      |
|--------------------------|---------------------|-------------|------------------------------|
| `mustBe`                 | number              | `=`         | `mustBe: 5`                  |
| `mustNotBe`              | number              | `≠`         | `mustNotBe: 3.14`            |
| `mustBeGreaterThan`      | number              | `>`         | `mustBeGreaterThan: 59`      |
| `mustBeGreaterOrEqualTo` | number              | `≥`         | `mustBeGreaterOrEqualTo: 60` |
| `mustBeLessThan`         | number              | `<`         | `mustBeLessThan: 1000`       |
| `mustBeLessOrEqualTo`    | number              | `≤`         | `mustBeLessOrEqualTo: 999`   |
| `mustBeBetween`          | array               | `∈`         | `mustBeBetween: [0, 100]`    |
| `mustNotBeBetween`       | array               | `∉`         | `mustNotBeBetween: [0, 100]` |

`mustBeBetween` is the equivalent to `mustBeGreaterThan` and `mustBeLessThan`.

```yaml
quality:
  - type: sql
    query: |
      SELECT COUNT(*) FROM {table} WHERE {column} IS NOT NULL
    mustBeBetween: [0, 100]
```

is equivalent to:

```yaml
quality:
  - type: sql
    query: |
      SELECT COUNT(*) FROM {table} WHERE {column} IS NOT NULL
    mustBeGreaterThan: 0
    mustBeLessThan: 100
```

[Back to TOC](#README-L1)


Original MD: [support-communication-channels.md](../source/docs/support-communication-channels.md#L1-L75).

<a id="support-communication-channels-L1"></a>

> Collector metadata display: original leading YAML frontmatter, source lines 1–4; not an upstream body heading.


```yaml
---
title: "Support & Communication Channels"
description: "Support and communication channels help consumers find help regarding their use of the data contract."
---
```


<!--
Copyright 2026 The Bitol Contributors
SPDX-License-Identifier: Apache-2.0
-->


<a id="support-communication-channels-L11"></a>

# Support & Communication Channels

Support and communication channels help consumers find help regarding their use of the data contract. They support multiple channels.

[Back to TOC](#README-L1)


<a id="support-communication-channels-L17"></a>

## Examples


<a id="support-communication-channels-L19"></a>

### Minimal example

```yaml
support:
  - channel: "#my-channel" # Simple Slack communication channel
  - channel: channel-name-or-identifier # Simple distribution list
    url: mailto:datacontract-ann@bitol.io
```


<a id="support-communication-channels-L28"></a>

### Full example

```yaml
support:
  - id: interactive_teams
    channel: channel-name-or-identifier
    tool: teams
    scope: interactive
    url: https://bitol.io/teams/channel/my-data-contract-interactive
  - id: announcements_teams
    channel: channel-name-or-identifier
    tool: teams
    scope: announcements
    url: https://bitol.io/teams/channel/my-data-contract-announcements
    invitationUrl: https://bitol.io/teams/channel/my-data-contract-announcements-invit
  - id: all_announcements
    channel: channel-name-or-identifier-for-all-announcement
    description: All announcement for all data contracts
    tool: teams
    scope: announcements
    url: https://bitol.io/teams/channel/all-announcements
  - id: email_announcements
    channel: channel-name-or-identifier
    tool: email
    scope: announcements
    url: mailto:datacontract-ann@bitol.io
  - id: ticket_support
    channel: channel-name-or-identifier
    tool: ticket
    url: https://bitol.io/ticket/my-product
```


<a id="support-communication-channels-L60"></a>

## Definitions

| Key                        | Type   | UX label          | Required | Description                                                                                                                                                                                |
| -------------------------- | ------ | ----------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| support                    | array  | Support           | No       | Top level for support channels.                                                                                                                                                            |
| support[].channel          | string | Channel           | Yes      | Channel name or identifier.                                                                                                                                                                |
| support[].description      | string | Description       | No       | Description of the channel, free text.                                                                                                                                                     |
| support[].id               | string | ID                | No       | A unique identifier for the element used to create stable, refactor-safe references. Recommended for elements that will be referenced. See [References](#references-L1) for more details. |
| support[].invitationUrl    | string | Invitation URL    | No       | Some tools uses invitation URL for requesting or subscribing. Follows the [URL scheme](https://en.wikipedia.org/wiki/URL#Syntax).                                                          |
| support[].scope            | string | Scope             | No       | Scope can be: `interactive`, `announcements`, `issues`, `notifications`.                                                                                                                   |
| support[].tool             | string | Tool              | No       | Name of the tool, value can be `email`, `slack`, `teams`, `discord`, `ticket`, `googlechat`, or `other`.                                                                                   |
| support[].url              | string | Channel URL       | No       | Access URL using normal [URL scheme](https://en.wikipedia.org/wiki/URL#Syntax) (https, mailto, etc.).                                                                                      |
| support[].customProperties | array  | Custom Properties | No       | Any custom properties.                                                                                                                                                                     |

[Back to TOC](#README-L1)


Original MD: [pricing.md](../source/docs/pricing.md#L1-L35).

<a id="pricing-L1"></a>

> Collector metadata display: original leading YAML frontmatter, source lines 1–4; not an upstream body heading.


```yaml
---
title: "Pricing"
description: "This section covers pricing when you bill your customer for using this data product."
---
```


<!--
Copyright 2026 The Bitol Contributors
SPDX-License-Identifier: Apache-2.0
-->


<a id="pricing-L11"></a>

# Pricing

This section covers pricing when you bill your customer for using this data product.

[Back to TOC](#README-L1)


<a id="pricing-L17"></a>

## Example

```YAML
price:
  priceAmount: 9.95
  priceCurrency: USD
  priceUnit: megabyte
```


<a id="pricing-L26"></a>

## Definitions

| Key                 | Type   | UX label           | Required | Description                                                                                                                                                                                |
|---------------------|--------|--------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| price               | object | Price              | No       | Object                                                                                                                                                                                     |
| price.priceAmount   | number | Price Amount       | No       | Subscription price per unit of measure in `priceUnit`.                                                                                                                                     |
| price.priceCurrency | string | Price Currency     | No       | Currency of the subscription price in `price.priceAmount`.                                                                                                                                 |
| price.priceUnit     | string | Price Unit         | No       | The unit of measure for calculating cost. Examples megabyte, gigabyte.                                                                                                                     |

[Back to TOC](#README-L1)

Original MD: [team.md](../source/docs/team.md#L1-L108).

<a id="team-L1"></a>

> Collector metadata display: original leading YAML frontmatter, source lines 1–4; not an upstream body heading.


```yaml
---
title: "Team"
description: "This section lists team members and the history of their relation with this data contract."
---
```


<!--
Copyright 2026 The Bitol Contributors
SPDX-License-Identifier: Apache-2.0
-->

<a id="team-L10"></a>

# Team

This section lists team members and the history of their relation with this data contract. 

!!! note

    In v2.x, this section was called `stakeholders`. Starting with v3.1.0, both the following structure are valid. However, the original v2.x / v3.x structure is deprecated and will be removed in ODCS v4. 

The structure describing `team` is shared between all Bitol standards, matching RFC 0016.

[Back to TOC](#README-L1)


<a id="team-L22"></a>

##  Example

```YAML
team:
  id: tsc_team
  name: TSC
  description: The greatest team ever.
  members:
    - username: ceastwood
      role: Data Scientist
      dateIn: 2022-08-02
      dateOut: 2022-10-01
      replacedByUsername: mhopper
    - id: mhopper_member
      username: mhopper
      role: Data Scientist
      dateIn: 2022-10-01
    - id: daustin
      username: daustin
      role: Owner
      description: Keeper of the grail
      name: David Austin
      dateIn: 2022-10-01
```


<a id="team-L47"></a>

## Definitions

| Key                                     | Type   | UX label                  | Required | Description                                                                                                                                                                                |
| --------------------------------------- | ------ | ------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| team                                    | object | Team                      | No       | Object representing a team.                                                                                                                                                                |
| team.description                        | string | Description               | No       | Team description.                                                                                                                                                                          |
| team.id                                 | string | ID                        | No       | A unique identifier for the element used to create stable, refactor-safe references. Recommended for elements that will be referenced. See [References](#references-L1) for more details. |
| team.name                               | string | Name                      | No       | Team name.                                                                                                                                                                                 |
| team.authoritativeDefinitions           | array  | Authoritative Definitions | No       | Authoritative definitions block.                                                                                                                                                           |
| team.tags                               | array  | Tags                      | No       | Tags applied to the team. See [Tags](#tags-L1).                                                                                                                                           |
| team.customProperties                   | array  | Custom Properties         | No       | Custom properties block.                                                                                                                                                                   |
| team.members                            | array  | Team Members              | No       | List of members.                                                                                                                                                                           |
| team.members[].dateIn                   | string | Date In                   | No       | The date when the user joined the team.                                                                                                                                                    |
| team.members[].dateOut                  | string | Date Out                  | No       | The date when the user ceased to be part of the team.                                                                                                                                      |
| team.members[].description              | string | Description               | No       | A description of the user, such as their responsibilities.                                                                                                                                 |
| team.members[].id                       | string | ID                        | No       | Identifier.                                                                                                                                                                                |
| team.members[].name                     | string | Name                      | No       | The user's name.                                                                                                                                                                           |
| team.members[].replacedByUsername       | string | Replaced By Username      | No       | The username of the user who replaced the previous user.                                                                                                                                   |
| team.members[].role                     | string | Role                      | No       | The user's job role; Examples might be owner, data steward. There is no limit on the role.                                                                                                 |
| team.members[].**username**             | string | Username                  | Yes      | The user's username or email.                                                                                                                                                              |
| team.members[].authoritativeDefinitions | array  | Authoritative Definitions | No       | Authoritative definitions block.                                                                                                                                                           |
| team.members[].tags                     | array  | Tags                      | No       | Tags applied to the team member. See [Tags](#tags-L1).                                                                                                                                    |
| team.members[].customProperties         | array  | Custom Properties         | No       | Custom properties block.                                                                                                                                                                   |


<a id="team-L71"></a>

## Deprecated Structure


<a id="team-L73"></a>

### Deprecated Example

```YAML
team:
  - username: ceastwood
    role: Data Scientist
    dateIn: 2022-08-02
    dateOut: 2022-10-01
    replacedByUsername: mhopper
  - username: mhopper
    role: Data Scientist
    dateIn: 2022-10-01
  - id: daustin_member
    username: daustin
    role: Owner
    description: Keeper of the grail
    name: David Austin
    dateIn: 2022-10-01
```


<a id="team-L93"></a>

### Deprecated Definitions

The UX label is the label used in the UI and other user experiences.

| Key                       | Type   | UX label             | Required | Description                                                                                |
| ------------------------- | ------ | -------------------- | -------- | ------------------------------------------------------------------------------------------ |
| team                      | array  | Team                 | No       | Object                                                                                     |
| team[].dateIn             | string | Date In              | No       | The date when the user joined the team.                                                    |
| team[].dateOut            | string | Date Out             | No       | The date when the user ceased to be part of the team.                                      |
| team[].description        | string | Description          | No       | The user's name.                                                                           |
| team[].name               | string | Name                 | No       | The user's name.                                                                           |
| team[].replacedByUsername | string | Replaced By Username | No       | The username of the user who replaced the previous user.                                   |
| team[].role               | string | Role                 | No       | The user's job role; Examples might be owner, data steward. There is no limit on the role. |
| team[].username           | string | Username             | No       | The user's username or email.                                                              |

[Back to TOC](#README-L1)

Original MD: [roles.md](../source/docs/roles.md#L1-L55).

<a id="roles-L1"></a>

> Collector metadata display: original leading YAML frontmatter, source lines 1–4; not an upstream body heading.


```yaml
---
title: "Roles"
description: "This section lists the roles that a consumer may need to access the dataset, depending on the type of access they require."
---
```


<!--
Copyright 2026 The Bitol Contributors
SPDX-License-Identifier: Apache-2.0
-->


<a id="roles-L11"></a>

# Roles

This section lists the roles that a consumer may need to access the dataset, depending on the type of access they require.

[Back to TOC](#README-L1)


<a id="roles-L17"></a>

## Example

```YAML
roles:
  - role: microstrategy_user_opr
    access: read
    firstLevelApprovers: Reporting Manager
    secondLevelApprovers: 'mandolorian'
  - id: bq_queryman_user_opr
    role: bq_queryman_user_opr
    access: read
    firstLevelApprovers: Reporting Manager
    secondLevelApprovers: na
  - id: risk_data_access_opr
    role: risk_data_access_opr
    access: read
    firstLevelApprovers: Reporting Manager
    secondLevelApprovers: 'dathvador'
  - id: bq_unica_user_opr
    role: bq_unica_user_opr
    access: write
    firstLevelApprovers: Reporting Manager
    secondLevelApprovers: 'mickey'
```


<a id="roles-L42"></a>

## Definitions

| Key                          | Type   | UX label            | Required | Description                                                                                                                                                                                |
| ---------------------------- | ------ | ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| roles                        | array  | Roles               | No       | Array. A list of roles that will provide user access to the dataset.                                                                                                                       |
| roles[].access               | string | Access              | No       | The type of access provided by the IAM role.                                                                                                                                               |
| roles[].description          | string | Description         | No       | Description of the IAM role and its permissions.                                                                                                                                           |
| roles[].firstLevelApprovers  | string | 1st Level Approvers | No       | The name(s) of the first-level approver(s) of the role.                                                                                                                                    |
| roles[].id                   | string | ID                  | No       | A unique identifier for the element used to create stable, refactor-safe references. Recommended for elements that will be referenced. See [References](#references-L1) for more details. |
| roles[].role                 | string | Role                | Yes      | Name of the IAM role that provides access to the dataset.                                                                                                                                  |
| roles[].secondLevelApprovers | string | 2nd Level Approvers | No       | The name(s) of the second-level approver(s) of the role.                                                                                                                                   |
| roles[].customProperties     | array  | Custom Properties   | No       | Any custom properties.                                                                                                                                                                     |

[Back to TOC](#README-L1)

Original MD: [service-level-agreement.md](../source/docs/service-level-agreement.md#L1-L101).

<a id="service-level-agreement-L1"></a>

> Collector metadata display: original leading YAML frontmatter, source lines 1–4; not an upstream body heading.


```yaml
---
title: "Service-Level Agreement"
description: "This section describes the service-level agreements (SLA)."
---
```


<!--
Copyright 2026 The Bitol Contributors
SPDX-License-Identifier: Apache-2.0
-->


<a id="service-level-agreement-L11"></a>

# Service-Level Agreement (SLA)

This section describes the service-level agreements (SLA).

* Use the `Object.Element` to indicate the number to do the checks on, as in `SELECT txn_ref_dt FROM tab1`.
* Separate multiple object.element by a comma, as in `table1.col1`, `table2.col1`, `table1.col2`.
* If there is only one object in the contract, the object name is not required.

[Back to TOC](#README-L1)


<a id="service-level-agreement-L21"></a>

## Example

```YAML
slaProperties:
  - id: latency_4_days
    property: latency # Property, see list of values in Data QoS (see below)
    value: 4
    unit: d # d, day, days for days; y, yr, years for years
    element: tab1.txn_ref_dt
    scheduler: cron
    schedule: 0 30 * * *
  - id: main_ga
    property: generalAvailability
    value: 2022-05-12T09:30:10-08:00
    description: GA at 12.5.22
  - id: eos
    property: endOfSupport
    value: 2032-05-12T09:30:10-08:00
  - id: eol
    property: endOfLife
    value: 2042-05-12T09:30:10-08:00
  - id: retention
    property: retention
    value: 3
    unit: y
    element: tab1.txn_ref_dt
  - id: frequency
    property: frequency
    value: 1
    valueExt: 1
    unit: d
    element: tab1.txn_ref_dt
  - id: reg_toa
    property: timeOfAvailability
    value: 09:00-08:00
    element: tab1.txn_ref_dt
    driver: regulatory # Describes the importance of the SLA: [regulatory|analytics|operational|...]
  - id: analytics_toa
    property: timeOfAvailability
    value: 08:00-08:00
    element: tab1.txn_ref_dt
    driver: analytics
```


<a id="service-level-agreement-L65"></a>

## Definitions

| Key                                | Type   | UX label                | Required                       | Description                                                                                                                                                                                |
| ---------------------------------- | ------ | ----------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ~~slaDefaultElement~~ (Deprecated) | string | Default SLA element(s)  | No                             | Element (using the element path notation) to do the checks on. DEPRECATED SINCE v3.1.0. WILL BE REMOVED IN ODCS v4.0.0.                                                                    |
| slaProperties                      | array  | SLA                     | No                             | A list of key/value pairs for SLA specific properties. There is no limit on the type of properties.                                                                                        |
| slaProperties[].authoritativeDefinitions | array | Authoritative Definitions | No                       | Links to external definitions for this SLA property (e.g. the formal SLA document or measurement method). Same structure as elsewhere in ODCS. (Added in v3.2.0, [RFC 0046](https://github.com/bitol-io/tsc/blob/main/rfcs/approved/odcs-v3.2.0/0046-sla-custom-properties-and-authoritative-definitions.md).) |
| slaProperties[].customProperties   | array  | Custom Properties       | No                             | Vendor- or organization-specific key/value pairs for this SLA property. Same structure as elsewhere in ODCS. (Added in v3.2.0, [RFC 0046](https://github.com/bitol-io/tsc/blob/main/rfcs/approved/odcs-v3.2.0/0046-sla-custom-properties-and-authoritative-definitions.md).) |
| slaProperties[].description        | string | Description             | No                             | Description of the SLA for humans.                                                                                                                                                         |
| slaProperties[].driver             | string | Driver                  | No                             | Describes the importance of the SLA from the list of: `regulatory`, `analytics`, or `operational`.                                                                                         |
| slaProperties[].element            | string | Element(s)              | No                             | Element(s) to check on. Multiple elements should be extremely rare and, if so, separated by commas.                                                                                        |
| slaProperties[].id                 | string | ID                      | No                             | A unique identifier for the element used to create stable, refactor-safe references. Recommended for elements that will be referenced. See [References](#references-L1) for more details. |
| slaProperties[].property           | string | Property                | Yes                            | Specific property in SLA, check the [Data QoS periodic table](https://medium.com/data-mesh-learning/what-is-data-qos-and-why-is-it-critical-c524b81e3cc1). May require units.              |
| slaProperties[].schedule           | string | Scheduler Configuration | No                             | Configuration information for the scheduling tool, for `cron` a possible value is `0 20 * * *`.                                                                                            |
| slaProperties[].scheduler          | string | Scheduler               | No                             | Name of the scheduler, can be `cron` or any tool your organization support.                                                                                                                |
| slaProperties[].unit               | string | Unit                    | No - unless needed by property | **d**, day, days for days; **y**, yr, years for years, etc. Units use the ISO standard.                                                                                                    |
| slaProperties[].value              | string | Value                   | Yes                            | Agreement value. The label will change based on the property itself.                                                                                                                       |
| slaProperties[].valueExt           | string | Extended value          | No - unless needed by property | Extended agreement value. The label will change based on the property itself.                                                                                                              |


<a id="service-level-agreement-L84"></a>

## Valid Values for SLA Properties

Recommend SLA properties follow the [Data QoS periodic table](https://medium.com/data-mesh-learning/what-is-data-qos-and-why-is-it-critical-c524b81e3cc1). Those values are case-insensitive and are:

* `availability` (synonym `av`).
* `throughput` (synonym `th`).
* `errorRate` (synonym `er`).
* `generalAvailability` (synonym `ga`).
* `endOfSupport` (synonym `es`).
* `endOfLife` (synonym `el`).
* `retention` (synonym `re`).
* `frequency` (synonym `fy`) - frequency of update.
* `latency` (synonym `ly`) - preferred to freshness.
* `timeToDetect` (synonym `td`) - time to detect an issue.
* `timeToNotify` (synonym `tn`).
* `timeToRepair` (synonym `tr`).

[Back to TOC](#README-L1)

Original MD: [infrastructure-servers.md](../source/docs/infrastructure-servers.md#L1-L527).

<a id="infrastructure-servers-L1"></a>

> Collector metadata display: original leading YAML frontmatter, source lines 1–4; not an upstream body heading.


```yaml
---
title: "Infrastructures & Servers"
description: "This section describes server structures, properties and types."
---
```


<!--
Copyright 2026 The Bitol Contributors
SPDX-License-Identifier: Apache-2.0
-->


<a id="infrastructure-servers-L11"></a>

# Infrastructure & Servers

The `servers` element describes where the data protected by this data contract is *physically* located. That metadata helps to know where the data is so that a data consumer can discover the data and a platform engineer can automate access.

An entry in `servers` describes a single dataset on a specific environment and a specific technology. The `servers` element can contain multiple servers, each with its own configuration.

The typical ways of using the top level `servers` element are as follows:

* **Single Server:** The data contract protects a specific dataset at a specific location. *Example:* a CSV file on an SFTP server.
* **Multiple Environments:** The data contract makes sure that the data is protected in all environments. *Example:* a data product with data in a **dev**(elopment), UAT, and **prod**(uction) environment on Databricks.

[Back to TOC](#README-L1)


<a id="infrastructure-servers-L24"></a>

## General Server Structure

Each server in the schema has the following structure:

```yaml
servers:
  - id: my_awesome_server
    server: my-server-name
    type: <server-type>
    description: <server-description>
    environment: <server-environment>
    <server-type-specific-fields> # according to the server type, see below
    roles:
      - <role-details>
    customProperties:
      - <custom-properties>
```


<a id="infrastructure-servers-L42"></a>

### Common Server Properties

| Key              | Type   | UX label          | Required | Description                                                                                                                                                                                                                                                                                                                       |
| ---------------- | ------ | ----------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| description      | string | Description       | No       | Description of the server.                                                                                                                                                                                                                                                                                                        |
| environment      | string | Environment       | No       | Environment of the server. Examples includes: prod, preprod, dev, uat.                                                                                                                                                                                                                                                            |
| id               | string | ID                | No       | A unique identifier used to reduce the risk of collisions, such as a UUID.                                                                                                                                                                                                                                                        |
| roles            | array  | Roles             | No       | List of roles that have access to the server. Check [roles](#roles-L1) section for more details.                                                                                                                                                                                                                                 |
| server           | string | Server            | Yes      | Identifier of the server.                                                                                                                                                                                                                                                                                                         |
| type             | string | Type              | Yes      | Type of the server. Can be one of: api, athena, azure, bigquery, btrieve, clickhouse, cloudsql, custom, databricks, db2, denodo, dremio, duckdb, exasol, fastobjects, glue, hive, impala, informix, ingres, kafka, kinesis, local, mysql, oracle, poet, postgres, postgresql, presto, pubsub, redshift, s3, sftp, snowflake, sqlserver, synapse, teradata, trino, vectorwise, versant, vertica, zen. |
| customProperties | array  | Custom Properties | No       | Custom properties that are not part of the standard.                                                                                                                                                                                                                                                                              |


<a id="infrastructure-servers-L54"></a>

## Specific Server Properties

Each server type can be customized with different properties such as `host`, `port`, `database`, and `schema`, depending on the server technology in use. Refer to the specific documentation for each server type for additional configurations.


<a id="infrastructure-servers-L58"></a>

## Specific Server Properties

If your server is not in the list, please use [custom](#infrastructure-servers-L498) and suggest it as an improvement. Possible values for `type` are:


<a id="infrastructure-servers-L62"></a>

### API Server

An API server describes data that is exposed through a network API rather than served from a database or file storage. The endpoint a consumer calls is identified by its URL.

| Key          | Type   | UX Label | Required | Description    |
| ------------ | ------ | -------- | -------- | -------------- |
| **location** | string | Location | Yes      | URL to the API |


<a id="infrastructure-servers-L70"></a>

### Amazon Athena Server

[Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) is an interactive query service that makes it easy to analyze data directly in Amazon Simple Storage Service (Amazon S3) using standard SQL. With a few actions in the AWS Management Console, you can point Athena at your data stored in Amazon S3 and begin using standard SQL to run ad-hoc queries and get results in seconds.

| Key        | Type   | UX Label          | Required | Description                                                                                                                                                      |
| ---------- | ------ | ----------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| catalog    | string | Catalog           | No       | Identify the name of the Data Source, also referred to as a Catalog.                                                                                             |
| regionName | string | Region Name       | No       | The region your AWS account uses.                                                                                                                                |
| schema     | string | Schema            | Yes      | Identify the schema in the data source in which your tables exist.                                                                                               |
| stagingDir | string | Staging Directory | No       | Amazon Athena automatically stores query results and metadata information for each query that runs in a query result location that you can specify in Amazon S3. |
| workgroup  | string | Workgroup         | No       | The Athena workgroup to use. Workgroups can enforce query result location and other client-side settings via the 'Override client-side settings' option.         |


<a id="infrastructure-servers-L82"></a>

### Azure Server

[Azure Blob Storage](https://azure.microsoft.com/en-us/products/storage/blobs) and [Azure Data Lake Storage (ADLS)](https://azure.microsoft.com/en-us/products/storage/data-lake-storage) are the Microsoft Azure object storage services for unstructured data and large-scale analytics workloads.

| Key       | Type   | UX Label  | Required | Description                                                                                           |
| --------- | ------ | --------- | -------- | ----------------------------------------------------------------------------------------------------- |
| delimiter | string | Delimiter | No       | Only for format = json. How multiple json documents are delimited within one file                     |
| encoding  | string | Encoding  | No       | Expected character encoding of the payload, e.g. UTF-8, ISO-8859-1, ASCII, UTF-16. Defaults to UTF-8. |
| format    | string | Format    | Yes      | File format.                                                                                          |
| location  | string | Location  | Yes      | Fully qualified path to Azure Blob Storage or Azure Data Lake Storage (ADLS), supports globs.         |


<a id="infrastructure-servers-L93"></a>

### Google BigQuery

[BigQuery](https://cloud.google.com/bigquery) is a fully managed, AI-ready data analytics platform that helps you maximize value from your data and is designed to be multi-engine, multi-format, and multi-cloud.

| Key     | Type   | UX Label | Required | Description                                   |
| ------- | ------ | -------- | -------- | --------------------------------------------- |
| dataset | string | Dataset  | Yes      | The GCP dataset name.                         |
| project | string | Project  | Yes      | The Google Cloud Platform (GCP) project name. |


<a id="infrastructure-servers-L102"></a>

### ClickHouse Server

[ClickHouse](https://clickhouse.com/) is an open-source column-oriented database management system that allows generating analytical data reports in real-time.

| Key      | Type    | UX Label | Required | Description                        |
| -------- | ------- | -------- | -------- | ---------------------------------- |
| database | string  | Database | Yes      | The name of the database.          |
| host     | string  | Host     | Yes      | The host of the ClickHouse server. |
| port     | integer | Port     | Yes      | The port to the ClickHouse server. |


<a id="infrastructure-servers-L112"></a>

### Google Cloud SQL

[Google Cloud SQL](https://cloud.google.com/sql) is a fully managed, cost-effective relational database service for PostgreSQL, MySQL, and SQL Server.

| Key      | Type    | UX Label | Required | Description                              |
| -------- | ------- | -------- | -------- | ---------------------------------------- |
| database | string  | Database | Yes      | The name of the database.                |
| host     | string  | Host     | Yes      | The host of the Google Cloud SQL server. |
| port     | integer | Port     | Yes      | The port of the Google Cloud SQL server. |
| schema   | string  | Schema   | Yes      | The name of the schema.                  |


<a id="infrastructure-servers-L123"></a>

### Databricks Server

[Databricks](https://www.databricks.com/) is a cloud-based data platform, built on Apache Spark, that unifies data warehousing and data lakes under the lakehouse architecture.

| Key     | Type   | UX Label | Required | Description                           |
| ------- | ------ | -------- | -------- | ------------------------------------- |
| catalog | string | Catalog  | Yes      | The name of the Hive or Unity catalog |
| host    | string | Host     | No       | The Databricks host                   |
| schema  | string | Schema   | Yes      | The schema name in the catalog        |


<a id="infrastructure-servers-L133"></a>

### IBM Db2 Server

[IBM Db2](https://www.ibm.com/products/db2) is a family of relational database management systems for transactional and analytical workloads, available both on cloud and on-premises.

| Key      | Type    | UX Label | Required | Description                     |
| -------- | ------- | -------- | -------- | ------------------------------- |
| database | string  | Database | Yes      | The name of the database.       |
| host     | string  | Host     | Yes      | The host of the IBM DB2 server. |
| port     | integer | Port     | Yes      | The port of the IBM DB2 server. |
| schema   | string  | Schema   | No       | The name of the schema.         |


<a id="infrastructure-servers-L144"></a>

### Denodo Server

[Denodo](https://www.denodo.com/) is a data virtualization platform that provides unified, real-time access to data spread across disparate sources, without replicating it.

| Key      | Type    | UX Label | Required | Description                    |
| -------- | ------- | -------- | -------- | ------------------------------ |
| database | string  | Database | No       | The name of the database.      |
| host     | string  | Host     | Yes      | The host of the Denodo server. |
| port     | integer | Port     | Yes      | The port of the Denodo server. |


<a id="infrastructure-servers-L154"></a>

### Dremio Server

[Dremio](https://www.dremio.com/) is a lakehouse platform that runs SQL queries directly against data lake storage, built on Apache Arrow and Apache Iceberg.

| Key    | Type    | UX Label | Required | Description                    |
| ------ | ------- | -------- | -------- | ------------------------------ |
| host   | string  | Host     | Yes      | The host of the Dremio server. |
| port   | integer | Port     | Yes      | The port of the Dremio server. |
| schema | string  | Schema   | No       | The name of the schema.        |


<a id="infrastructure-servers-L164"></a>

### DuckDB Server

[DuckDB](https://duckdb.org/) supports a feature-rich SQL dialect complemented with deep integrations into client APIs.

| Key      | Type   | UX Label | Required | Description                   |
| -------- | ------ | -------- | -------- | ----------------------------- |
| database | string | Database | Yes      | Path to duckdb database file. |
| schema   | string | Schema   | No       | The name of the schema.       |


<a id="infrastructure-servers-L173"></a>

### Exasol

[Exasol](https://www.exasol.com/) is an in-memory, massively parallel processing (MPP) analytics database used as an enterprise data warehouse. Added in ODCS v3.2.0 ([RFC 0058](https://github.com/bitol-io/tsc/blob/main/rfcs/approved/odcs-v3.2.0/0058-exasol-server-type.md)).

An Exasol cluster runs a single database and the schema is the namespace, so there is no `database` field.

| Key    | Type    | UX Label | Required | Description                                                                            |
| ------ | ------- | -------- | -------- | -------------------------------------------------------------------------------------- |
| host   | string  | Host     | Yes      | Host of the Exasol server. May be a cluster connection range, e.g. `n11..14.acme.com`. |
| port   | integer | Port     | No       | Port of the Exasol server. Defaults to 8563.                                           |
| schema | string  | Schema   | No       | Name of the schema.                                                                    |


<a id="infrastructure-servers-L185"></a>

### Amazon Glue

[AWS Glue](https://aws.amazon.com/glue/) is a serverless data integration service. Its Data Catalog holds the table definitions and schema metadata describing data stored in Amazon S3 and other sources.

| Key      | Type   | UX Label | Required | Description                                                                                           |
| -------- | ------ | -------- | -------- | ----------------------------------------------------------------------------------------------------- |
| account  | string | Account  | Yes      | The AWS Glue account                                                                                  |
| database | string | Database | Yes      | The AWS Glue database name                                                                            |
| encoding | string | Encoding | No       | Expected character encoding of the payload, e.g. UTF-8, ISO-8859-1, ASCII, UTF-16. Defaults to UTF-8. |
| format   | string | Format   | No       | The format of the files                                                                               |
| location | string | Location | No       | The AWS S3 path. Must be in the form of a URL.                                                        |


<a id="infrastructure-servers-L197"></a>

### Hive

[Apache Hive](https://hive.apache.org/) is a distributed, fault-tolerant data warehouse system that enables analytics at massive scale. Built on top of Apache Hadoop, Hive allows users to read, write, and manage petabytes of data using SQL-like queries through HiveQL, with native support for cloud storage systems and enterprise-grade security features.

| Key      | Type    | UX Label | Required | Description                                     |
| -------- | ------- | -------- | -------- | ----------------------------------------------- |
| database | string  | Database | Yes      | The name of the Hive database.                  |
| host     | string  | Host     | Yes      | The host to the Hive server.                    |
| port     | integer | Port     | No       | The port to the Hive server. Defaults to 10000. |


<a id="infrastructure-servers-L207"></a>

### Apache Iceberg

[Apache Iceberg](https://iceberg.apache.org/) is an open table format for large analytic datasets, accessed through the standardized Iceberg REST catalog API (Polaris, S3 Tables, Nessie, Unity Catalog, Glue, etc.). Added in ODCS v3.2.0 ([RFC 0049](https://github.com/bitol-io/tsc/blob/main/rfcs/approved/odcs-v3.2.0/0049-iceberg-server-type.md)).

| Key        | Type   | UX Label    | Required | Description                                                                                                 |
| ---------- | ------ | ----------- | -------- | ----------------------------------------------------------------------------------------------------------- |
| catalog    | string | Catalog     | Yes      | Catalog name as registered in the query engine or catalog service (e.g. `my_catalog`).                      |
| catalogUrl | string | Catalog URL | Yes      | URL of the Iceberg compatible REST catalog service (Polaris, S3 Tables, Nessie, Unity Catalog, Glue, etc.). |
| namespace  | string | Namespace   | No       | Dot-separated namespace path within the catalog (e.g. `db.schema` or just `db`).                            |
| warehouse  | string | Warehouse   | No       | Base storage location of the warehouse (e.g. `s3://my-bucket/warehouse/`).                                  |


<a id="infrastructure-servers-L218"></a>

### Apache Impala

[Apache Impala](https://impala.apache.org/) is a massively parallel processing (MPP) SQL query engine for data stored in Apache Hadoop clusters. Impala provides high-performance, low-latency SQL queries on data stored in HDFS and Apache HBase, enabling interactive exploration and analytics without data movement or transformation.

| Key      | Type    | UX Label | Required | Description                                       |
| -------- | ------- | -------- | -------- | ------------------------------------------------- |
| database | string  | Database | Yes      | The name of the Impala database.                  |
| host     | string  | Host     | Yes      | The host to the Impala server.                    |
| port     | integer | Port     | No       | The port to the Impala server. Defaults to 21050. |


<a id="infrastructure-servers-L228"></a>

### HCL Informix and IBM Informix

[HCL Informix](https://www.hcl-software.com/informix) and [IBM Informix](https://www.ibm.com/products/informix) are high performance, always-on, highly scalable and easily embeddable enterprise-class databases optimized for the most demanding transactional and analytics workloads. As object-relational engines, HCL Informix and IBM Informix seamlessly integrate the best of relational and object-oriented capabilities, enabling the flexible modeling of complex data structures and relationships.

| Key      | Type    | UX Label | Required | Description                                                             |
| -------- | ------- | -------- | -------- | ----------------------------------------------------------------------- |
| database | string  | Database | Yes      | The name of the database.                                               |
| host     | string  | Host     | Yes      | The host to the HCL Informix and IBM Informix server.                   |
| port     | integer | Port     | No       | The port to the HCL Informix and IBM Informix server. Defaults to 9088. |


<a id="infrastructure-servers-L238"></a>

### Actian Ingres

[Actian Ingres](https://www.actian.com/databases/ingres/) is an enterprise relational database for transactional (OLTP) and hybrid workloads. Added in ODCS v3.2.0 ([RFC 0059](https://github.com/bitol-io/tsc/blob/main/rfcs/approved/odcs-v3.2.0/0059-actian-server-types.md)).

The namespace inside an Ingres database is the table owner, resolved from the connecting user, so there is no `schema` field. `port` is derived from the Ingres installation identifier and defaults to the `II7` installation; set it explicitly when a host runs more than one installation.

| Key      | Type    | UX Label | Required | Description                                                                                              |
| -------- | ------- | -------- | -------- | -------------------------------------------------------------------------------------------------------- |
| database | string  | Database | Yes      | Database name to connect to on the Ingres instance.                                                      |
| host     | string  | Host     | Yes      | Hostname or IP address of the Ingres server.                                                             |
| port     | integer | Port     | No       | Connection port for the Ingres Data Access Server (DAS) / SQL connections. Defaults to 21064.            |


<a id="infrastructure-servers-L250"></a>

### Kafka Server

[Apache Kafka](https://kafka.apache.org/) is an open-source distributed event streaming platform used for high-performance data pipelines, streaming analytics, and event-driven applications.

| Key      | Type   | UX Label | Required | Description                                                                                           |
| -------- | ------ | -------- | -------- | ----------------------------------------------------------------------------------------------------- |
| encoding | string | Encoding | No       | Expected character encoding of the payload, e.g. UTF-8, ISO-8859-1, ASCII, UTF-16. Defaults to UTF-8. |
| format   | string | Format   | No       | The format of the messages.                                                                           |
| host     | string | Host     | Yes      | The bootstrap server of the kafka cluster.                                                            |


<a id="infrastructure-servers-L260"></a>

### Amazon Kinesis

[Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/) is a serverless streaming data service for collecting, processing, and analyzing large streams of records in real time.

| Key      | Type   | UX Label | Required | Description                                                                                           |
| -------- | ------ | -------- | -------- | ----------------------------------------------------------------------------------------------------- |
| encoding | string | Encoding | No       | Expected character encoding of the payload, e.g. UTF-8, ISO-8859-1, ASCII, UTF-16. Defaults to UTF-8. |
| format   | string | Format   | No       | The format of the record                                                                              |
| region   | string | Region   | No       | AWS region.                                                                                           |
| stream   | string | Stream   | Yes      | The name of the Kinesis data stream.                                                                  |


<a id="infrastructure-servers-L271"></a>

### Local Files

A local server describes data stored as one or more files on the local file system, addressed by a relative or absolute path. It is typically used for development, testing, and small datasets.

| Key      | Type   | UX Label | Required | Description                                                                                           |
| -------- | ------ | -------- | -------- | ----------------------------------------------------------------------------------------------------- |
| encoding | string | Encoding | No       | Expected character encoding of the payload, e.g. UTF-8, ISO-8859-1, ASCII, UTF-16. Defaults to UTF-8. |
| format   | string | Format   | Yes      | The format of the file(s)                                                                             |
| path     | string | Path     | Yes      | The relative or absolute path to the data file(s).                                                    |


<a id="infrastructure-servers-L281"></a>

### MySQL Server

[MySQL](https://www.mysql.com/) is an open-source relational database management system, widely used for transactional and web applications.

| Key      | Type    | UX Label | Required | Description                                     |
| -------- | ------- | -------- | -------- | ----------------------------------------------- |
| database | string  | Database | Yes      | The name of the database.                       |
| host     | string  | Host     | Yes      | The host of the MySql server.                   |
| port     | integer | Port     | No       | The port of the MySql server. Defaults to 3306. |


<a id="infrastructure-servers-L291"></a>

### Oracle

[Oracle Database](https://www.oracle.com/database/) is a multi-model relational database management system used for transactional and analytical enterprise workloads. Clients connect to a named service rather than directly to a database.

| Key         | Type    | UX Label     | Required | Description                    |
| ----------- | ------- | ------------ | -------- | ------------------------------ |
| host        | string  | Host         | Yes      | The host to the Oracle server  |
| port        | integer | Port         | Yes      | The port to the Oracle server. |
| serviceName | string  | Service Name | Yes      | The name of the service.       |


<a id="infrastructure-servers-L301"></a>

### Actian NoSQL FastObjects

[Actian NoSQL FastObjects](https://www.actian.com/databases/nosql/) is an object database management system (ODBMS) for embedded and client/server applications. Created as POET, renamed FastObjects in 2001. Added in ODCS v3.2.0 ([RFC 0059](https://github.com/bitol-io/tsc/blob/main/rfcs/approved/odcs-v3.2.0/0059-actian-server-types.md)).

The `type` value is the creation name, `poet`. `fastobjects` is an accepted synonym: same fields, same validation, neither value deprecated.

An object database has no SQL schema namespace — classes are scoped by the database — so there is no `schema` field. `LOCAL` is a literal FastObjects sentinel rather than a hostname: it selects the in-process embedded engine, so one `host` field covers both the embedded and the client/server deployment.

| Key      | Type    | UX Label | Required | Description                                                                                     |
| -------- | ------- | -------- | -------- | ------------------------------------------------------------------------------------------------- |
| database | string  | Database | Yes      | Database name to connect to on the FastObjects instance.                                        |
| host     | string  | Host     | No       | Hostname or IP address of the FastObjects server. Defaults to `LOCAL`, the embedded engine.     |
| port     | integer | Port     | No       | Connection port for FastObjects connections. Defaults to 6001.                                  |


<a id="infrastructure-servers-L315"></a>

### PostgreSQL

[PostgreSQL](https://www.postgresql.org/) is a powerful, open source object-relational database system with over 35 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.

| Key      | Type    | UX Label | Required | Description                                          |
| -------- | ------- | -------- | -------- | ---------------------------------------------------- |
| database | string  | Database | Yes      | The name of the database.                            |
| host     | string  | Host     | Yes      | The host to the PostgreSQL server                    |
| port     | integer | Port     | No       | The port to the PostgreSQL server. Defaults to 5432. |
| schema   | string  | Schema   | No       | The name of the schema in the database.              |


<a id="infrastructure-servers-L326"></a>

### Presto Server

[Presto](https://prestodb.io/) is an open-source distributed SQL query engine for running interactive analytic queries against data sources of any size, from gigabytes to petabytes.

| Key     | Type   | UX Label | Required | Description                   |
| ------- | ------ | -------- | -------- | ----------------------------- |
| catalog | string | Catalog  | No       | The name of the catalog.      |
| host    | string | Host     | Yes      | The host to the Presto server |
| schema  | string | Schema   | No       | The name of the schema.       |


<a id="infrastructure-servers-L336"></a>

### Google Pub/Sub

[Google Cloud](https://cloud.google.com/pubsub) service to Ingest events for streaming into BigQuery, data lakes or operational databases.

| Key     | Type   | UX Label | Required | Description           |
| ------- | ------ | -------- | -------- | --------------------- |
| project | string | Project  | Yes      | The GCP project name. |


<a id="infrastructure-servers-L344"></a>

### Amazon Redshift Server

[Amazon Redshift](https://aws.amazon.com/redshift/) is a power data driven decisions with the best price-performance cloud data warehouse.

| Key      | Type   | UX Label | Required | Description                               |
| -------- | ------ | -------- | -------- | ----------------------------------------- |
| account  | string | Account  | No       | The account used by the server.           |
| database | string | Database | Yes      | The name of the database.                 |
| host     | string | Host     | No       | An optional string describing the server. |
| region   | string | Region   | No       | AWS region of Redshift server.            |
| schema   | string | Schema   | Yes      | The name of the schema.                   |


<a id="infrastructure-servers-L356"></a>

### Amazon S3 Server and Compatible Servers

[Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) is an object storage service offering industry-leading scalability, data availability, security, and performance. Millions of customers of all sizes and industries store, manage, analyze, and protect any amount of data for virtually any use case, such as data lakes, cloud-native applications, and mobile apps. Other vendors have implemented a compatible implementation of S3.

| Key         | Type   | UX Label     | Required | Description                                                                                           |
| ----------- | ------ | ------------ | -------- | ----------------------------------------------------------------------------------------------------- |
| delimiter   | string | Delimiter    | No       | Only for format = json. How multiple json documents are delimited within one file                     |
| encoding    | string | Encoding     | No       | Expected character encoding of the payload, e.g. UTF-8, ISO-8859-1, ASCII, UTF-16. Defaults to UTF-8. |
| endpointUrl | string | Endpoint URL | No       | The server endpoint for S3-compatible servers.                                                        |
| format      | string | Format       | No       | File format.                                                                                          |
| location    | string | Location     | Yes      | S3 URL, starting with `s3://`                                                                         |


<a id="infrastructure-servers-L368"></a>

### SAP HANA

[SAP HANA](https://www.sap.com/products/technology-platform/hana.html) is an in-memory, column-oriented relational database used as an enterprise data platform.

| Key      | Type    | UX Label | Required | Description                    |
| -------- | ------- | -------- | -------- | ------------------------------ |
| host     | string  | Host     | Yes      | Host of the HANA server.       |
| port     | integer | Port     | No       | Port of the HANA server.       |
| database | string  | Database | No       | Name of the database (tenant). |
| schema   | string  | Schema   | No       | Name of the schema.            |


<a id="infrastructure-servers-L379"></a>

### SFTP Server

Secure File Transfer Protocol (SFTP) is a network protocol that enables secure and encrypted file transfers between a client and a server.

| Key       | Type   | UX Label  | Required | Description                                                                                           |
| --------- | ------ | --------- | -------- | ----------------------------------------------------------------------------------------------------- |
| delimiter | string | Delimiter | No       | Only for format = json. How multiple json documents are delimited within one file                     |
| encoding  | string | Encoding  | No       | Expected character encoding of the payload, e.g. UTF-8, ISO-8859-1, ASCII, UTF-16. Defaults to UTF-8. |
| format    | string | Format    | No       | File format.                                                                                          |
| location  | string | Location  | Yes      | SFTP URL, starting with `sftp://`. The URL should include the port number.                            |


<a id="infrastructure-servers-L390"></a>

### Snowflake

[Snowflake](https://www.snowflake.com/) is a fully managed cloud data platform that separates storage from compute, where compute is provided by virtual warehouses that can be sized and scaled independently.

| Key       | Type    | UX Label  | Required | Description                                                                 |
| --------- | ------- | --------- | -------- | --------------------------------------------------------------------------- |
| account   | string  | Account   | Yes      | The Snowflake account used by the server.                                   |
| database  | string  | Database  | Yes      | The name of the database.                                                   |
| host      | string  | Host      | Yes      | The host to the Snowflake server                                            |
| port      | integer | Port      | Yes      | The port to the Snowflake server.                                           |
| schema    | string  | Schema    | Yes      | The name of the schema.                                                     |
| warehouse | string  | Warehouse | Yes      | The name of the cluster of resources that is a Snowflake virtual warehouse. |


<a id="infrastructure-servers-L403"></a>

### Microsoft SQL Server

[Microsoft SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads) is a proprietary relational database management system developed by Microsoft.

| Key      | Type    | UX Label | Required | Description                                        |
| -------- | ------- | -------- | -------- | -------------------------------------------------- |
| database | string  | Database | Yes      | The name of the database.                          |
| host     | string  | Host     | Yes      | The host to the database server                    |
| port     | integer | Port     | No       | The port to the database server. Defaults to 1433. |
| schema   | string  | Schema   | Yes      | The name of the schema in the database.            |


<a id="infrastructure-servers-L414"></a>

### Synapse Server

[Azure Synapse Analytics](https://azure.microsoft.com/en-us/products/synapse-analytics) is the Microsoft Azure analytics service that brings together enterprise data warehousing and big data analytics.

| Key      | Type    | UX Label | Required | Description                     |
| -------- | ------- | -------- | -------- | ------------------------------- |
| database | string  | Database | Yes      | The name of the database.       |
| host     | string  | Host     | Yes      | The host of the Synapse server. |
| port     | integer | Port     | Yes      | The port of the Synapse server. |


<a id="infrastructure-servers-L424"></a>

### Teradata

[Teradata Vantage](https://www.teradata.com/) is a widely used enterprise data warehouse for large-scale analytics. Added in ODCS v3.2.0 ([RFC 0057](https://github.com/bitol-io/tsc/blob/main/rfcs/approved/odcs-v3.2.0/0057-teradata-server-type.md)).

In Teradata, the database is the namespace, so there is no `schema` field.

| Key      | Type    | UX Label | Required | Description                                     |
| -------- | ------- | -------- | -------- | ----------------------------------------------- |
| database | string  | Database | No       | Name of the database.                           |
| host     | string  | Host     | Yes      | Host of the Teradata server.                    |
| port     | integer | Port     | No       | Port of the Teradata server. Defaults to 1025.  |


<a id="infrastructure-servers-L436"></a>

### Trino Server

[Trino](https://trino.io/) is an open-source distributed SQL query engine designed to query large datasets across one or more heterogeneous data sources.

| Key     | Type    | UX Label | Required | Description                             |
| ------- | ------- | -------- | -------- | --------------------------------------- |
| catalog | string  | Catalog  | Yes      | The name of the catalog.                |
| host    | string  | Host     | Yes      | The Trino host URL.                     |
| port    | integer | Port     | Yes      | The Trino port.                         |
| schema  | string  | Schema   | Yes      | The name of the schema in the database. |


<a id="infrastructure-servers-L447"></a>

### Actian Analytics Engine

The [Actian Analytics Engine](https://www.actian.com/databases/analytics-engine/) is a columnar analytical DBMS for high-speed SQL and big data processing. Created as VectorWise, later named Actian Vector. Added in ODCS v3.2.0 ([RFC 0059](https://github.com/bitol-io/tsc/blob/main/rfcs/approved/odcs-v3.2.0/0059-actian-server-types.md)).

The `type` value is the creation name, `vectorwise`. Tooling should display the Actian Analytics Engine label and write the enum value.

The namespace inside a database is the table owner, resolved from the connecting user, so there is no `schema` field. `port` is derived from the Ingres installation identifier; set it explicitly when a host runs more than one installation.

| Key      | Type    | UX Label | Required | Description                                                                          |
| -------- | ------- | -------- | -------- | -------------------------------------------------------------------------------------- |
| database | string  | Database | Yes      | Database name to connect to on the Analytics Engine server.                          |
| host     | string  | Host     | Yes      | Hostname or IP address of the Analytics Engine server.                               |
| port     | integer | Port     | No       | Connection port for the Data Access Server (DAS) / SQL connections. Defaults to 21064. |


<a id="infrastructure-servers-L461"></a>

### Actian NoSQL Database

[Actian NoSQL Database](https://www.actian.com/databases/nosql/) is an object database management system (ODBMS) for mission-critical OLTP. Created as the Versant Object Database. Added in ODCS v3.2.0 ([RFC 0059](https://github.com/bitol-io/tsc/blob/main/rfcs/approved/odcs-v3.2.0/0059-actian-server-types.md)).

The `type` value is the creation name, `versant`. Tooling should display the Actian NoSQL Database label and write the enum value.

An object database has no SQL schema namespace — classes are scoped by the database — so there is no `schema` field.

| Key      | Type    | UX Label | Required | Description                                                                |
| -------- | ------- | -------- | -------- | ---------------------------------------------------------------------------- |
| database | string  | Database | Yes      | Database name to connect to on the NoSQL Database instance.                |
| host     | string  | Host     | No       | Hostname or IP address of the NoSQL Database server. Defaults to `localhost`. |
| port     | integer | Port     | No       | Connection port for Actian NoSQL Database connections. Defaults to 5019.   |


<a id="infrastructure-servers-L475"></a>

### Vertica Server

[Vertica](https://docs.vertica.com/) is a column-oriented, massively parallel processing (MPP) analytical database for large-scale data warehousing.

| Key      | Type    | UX Label | Required | Description                     |
| -------- | ------- | -------- | -------- | ------------------------------- |
| database | string  | Database | Yes      | The name of the database.       |
| host     | string  | Host     | Yes      | The host of the Vertica server. |
| port     | integer | Port     | Yes      | The port of the Vertica server. |
| schema   | string  | Schema   | Yes      | The name of the schema.         |


<a id="infrastructure-servers-L486"></a>

### Actian Zen Server

Actian Zen (formerly Btrieve, later named Pervasive PSQL until version 13) is an ACID-compliant, zero-DBA, embedded, nano-footprint, multi-model, Multi-Platform database management system (DBMS).

Since ODCS v3.2.0 ([RFC 0059](https://github.com/bitol-io/tsc/blob/main/rfcs/approved/odcs-v3.2.0/0059-actian-server-types.md)), `btrieve` is an accepted synonym of `zen`: same fields, same validation, neither value deprecated.

| Key      | Type    | UX Label | Required | Description                                        |
| -------- | ------- | -------- | -------- | -------------------------------------------------- |
| database | string  | Database | Yes      | Database name to connect to on the Zen server.     |
| host     | string  | Host     | Yes      | Hostname or IP address of the Zen server.          |
| port     | integer | Port     | No       | Zen server SQL connections port. Defaults to 1583. |


<a id="infrastructure-servers-L498"></a>

### Custom Server

A custom server describes any technology that does not have a dedicated type in ODCS yet. It accepts the union of the properties defined by the other server types, so connection details can still be expressed in a structured way.

| Key         | Type    | UX Label          | Required | Description                                                                                           |
| ----------- | ------- | ----------------- | -------- | ----------------------------------------------------------------------------------------------------- |
| account     | string  | Account           | No       | Account used by the server.                                                                           |
| catalog     | string  | Catalog           | No       | Name of the catalog.                                                                                  |
| database    | string  | Database          | No       | Name of the database.                                                                                 |
| dataset     | string  | Dataset           | No       | Name of the dataset.                                                                                  |
| delimiter   | string  | Delimiter         | No       | Delimiter.                                                                                            |
| encoding    | string  | Encoding          | No       | Expected character encoding of the payload, e.g. UTF-8, ISO-8859-1, ASCII, UTF-16. Defaults to UTF-8. |
| endpointUrl | string  | Endpoint URL      | No       | Server endpoint.                                                                                      |
| format      | string  | Format            | No       | File format.                                                                                          |
| host        | string  | Host              | No       | Host name or IP address.                                                                              |
| location    | string  | Location          | No       | A URL to a location.                                                                                  |
| path        | string  | Path              | No       | Relative or absolute path to the data file(s).                                                        |
| port        | integer | Port              | No       | Port to the server. No default value is assumed for custom servers.                                   |
| project     | string  | Project           | No       | Project name.                                                                                         |
| region      | string  | Region            | No       | Cloud region.                                                                                         |
| regionName  | string  | Region Name       | No       | Region name.                                                                                          |
| schema      | string  | Schema            | No       | Name of the schema.                                                                                   |
| serviceName | string  | Service Name      | No       | Name of the service.                                                                                  |
| stagingDir  | string  | Staging Directory | No       | Staging directory.                                                                                    |
| stream      | string  | Stream            | No       | Name of the data stream.                                                                              |
| warehouse   | string  | Warehouse         | No       | Name of the cluster or warehouse.                                                                     |

If you need another property, use [custom properties](#custom-other-properties-L1).

[Back to TOC](#README-L1)

Original MD: [custom-other-properties.md](../source/docs/custom-other-properties.md#L1-L73).

<a id="custom-other-properties-L1"></a>

> Collector metadata display: original leading YAML frontmatter, source lines 1–4; not an upstream body heading.


```yaml
---
title: "Custom & Other Properties"
description: "This section covers custom properties you may find in a data contract."
---
```


<!--
Copyright 2026 The Bitol Contributors
SPDX-License-Identifier: Apache-2.0
-->


<a id="custom-other-properties-L11"></a>

# Custom & Other Properties

This section covers other properties you may find in a data contract.

[Back to TOC](#README-L1)


<a id="custom-other-properties-L17"></a>

## Custom Properties

This section covers custom properties you can use to add non-standard properties. This block is available in many
sections.


<a id="custom-other-properties-L22"></a>

### Example

```YAML
customProperties:
  - id: rfc_ruleset_name
    property: refRulesetName
    value: gcsc.ruleset.name
  - id: some_property_name
    property: somePropertyName
    value: property.value
  - id: data_proc_cluster_name
    property: dataprocClusterName # Used for specific applications
    value: [ cluster name ]
    description: Cluster name for specific applications
```


<a id="custom-other-properties-L38"></a>

### Definitions

| Key                            | Type   | UX label          | Required | Description                                                                                                                                                                                |
| ------------------------------ | ------ | ----------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| customProperties               | array  | Custom Properties | No       | A list of key/value pairs for custom properties. Initially created to support the REF ruleset property.                                                                                    |
| customProperties[].description | string | Description       | No       | Description for humans.                                                                                                                                                                    |
| customProperties[].id          | string | ID                | No       | A unique identifier for the element used to create stable, refactor-safe references. Recommended for elements that will be referenced. See [References](#references-L1) for more details. |
| customProperties[].property    | string | Property          | No       | The name of the key. Names should be in camel case–the same as if they were permanent properties in the contract.                                                                          |
| customProperties[].value       | any    | Value             | No       | The value of the key. It can be an array.                                                                                                                                                  |
| customProperties[].vendor      | string | Vendor            | No       | Identifies the vendor, provider, or external system associated with this custom property. SHOULD be a stable, lowercase identifier matching `^[a-z0-9][a-z0-9-]*$` (e.g. `confluent`, `zeenea`). Tools MUST preserve unknown vendor values. (Added in v3.2.0, [RFC 0035](https://github.com/bitol-io/tsc/blob/main/rfcs/approved/odcs-v3.2.0/0035-extensions.md).) |

Avis: With version 3.2.0 the Description of 'customProperties.property' will be updated to "The name of the key. Could be in any notation. If this field is used for referencing it should be in camel case–the same as if they were permanent properties in the contract. Note that since ODCS version 3.1 the field 'customProperties.id' should be used for referencing purposes. In this case the name of the key could be human-readable and self-explanatory to the greatest extent."


<a id="custom-other-properties-L51"></a>

## Authoritative Definitions

Authoritative Definitions allow you to delegate definitions to a third-party system such as an enterprise catalog, repository, or knowledge base. The block is shared across all Bitol standards and is available in many sections of a data contract.

See the dedicated [Authoritative Definitions](#authoritative-definitions-L1) page for the full specification, examples, and the recommended values for the `type` field.


<a id="custom-other-properties-L57"></a>

## Other Properties

This section covers other properties you may find in a data contract.


<a id="custom-other-properties-L61"></a>

### Example

```YAML
contractCreatedTs: 2024-09-17T11:58:08Z
```


<a id="custom-other-properties-L67"></a>

### Other properties definition

| Key               | Type   | UX label             | Required | Description                                                             |
|-------------------|--------|----------------------|----------|-------------------------------------------------------------------------|
| contractCreatedTs | string | Contract Created UTC | No       | Timestamp in UTC of when the data contract was created, using ISO 8601. |

[Back to TOC](#README-L1)

Original MD: [authoritative-definitions.md](../source/docs/authoritative-definitions.md#L1-L61).

<a id="authoritative-definitions-L1"></a>

> Collector metadata display: original leading YAML frontmatter, source lines 1–4; not an upstream body heading.


```yaml
---
title: "Authoritative Definitions"
description: "Reference external sources of truth from a data contract."
---
```


<!--
Copyright 2026 The Bitol Contributors
SPDX-License-Identifier: Apache-2.0
-->


<a id="authoritative-definitions-L11"></a>

# Authoritative Definitions

Authoritative Definitions are an essential part of the contract. They allow to delegate the definition or authority to a third party system like an enterprise catalog, repository, etc. The structure describing "Authoritative Definitions" is shared between all Bitol standards. This block is available in many sections.

[Back to TOC](#README-L1)


<a id="authoritative-definitions-L17"></a>

## Example

```yaml
    authoritativeDefinitions:
      - url: https://catalog.data.gov/dataset/air-quality
        type: businessDefinition
        description: Business definition for the dataset.
      - id: vid-001
        url: https://www.youtube.com/watch?v=Iq6SxdsIHHE
        type: videoTutorial
        description: Discover what a data contract is.
      - url: https://github.com/bitol-io/open-data-contract-standard/blob/main/docs/examples/all/full-example.odcs.yaml
        type: canonicalUrl
        description: Data contract's latest version.
```


<a id="authoritative-definitions-L33"></a>

## Definitions

| Key                                    | Type   | UX label          | Required | Description                                                                                                                                                                                |
| -------------------------------------- | ------ | ----------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| authoritativeDefinitions               | array  | Link              | No       | A list of type/link pairs for authoritative definitions.                                                                                                                                   |
| authoritativeDefinitions[].description | string | Description       | No       | Optional description.                                                                                                                                                                      |
| authoritativeDefinitions[].id          | string | ID                | No       | A unique identifier for the element used to create stable, refactor-safe references. Recommended for elements that will be referenced. See [References](#references-L1) for more details. |
| authoritativeDefinitions[].type        | string | Definition type   | Yes      | Type of definition for authority. See the recommended values below.                                                                                                                        |
| authoritativeDefinitions[].url         | string | URL to definition | Yes      | URL to the authority.                                                                                                                                                                      |


<a id="authoritative-definitions-L43"></a>

## Recommended values for `type`

The `type` field is open (any string is technically valid), but the following values are recommended for interoperability across tools:

| Value                          | Where allowed | Description                                                                                                                                 |
| ------------------------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `businessDefinition`           | Any section   | Link to a business glossary entry, ontology, or other source describing the business meaning of the element.                                |
| `canonicalUrl`                 | Root only     | At the root level of a data contract, marks a reference to the canonical/latest version of the data contract itself (e.g., its source URL). |
| `glossary`                     | Any section   | Link to a business glossary entry defining the term or concept (RFC-0038).                                                                  |
| `implementation`               | Any section   | Link to a code-level implementation, library, or reference that fulfils or interprets the element.                                          |
| `ontology`                     | Any section   | Link to an ontology describing the concept and its relationships (RFC-0038).                                                                |
| `taxonomy`                     | Any section   | Link to a taxonomy classifying the element (RFC-0038).                                                                                      |
| `transformationImplementation` | Any section   | Link to the implementation that produces the data (e.g., a dbt model, Spark job, SQL view definition, or pipeline reference).               |
| `tutorial`                     | Any section   | Link to a written tutorial, walkthrough, or how-to guide.                                                                                   |
| `videoTutorial`                | Any section   | Link to a recorded video that explains the element or how to use it.                                                                        |

Custom `type` values are allowed; tooling that does not recognise a custom value should treat the entry as an opaque link with a description.

[Back to TOC](#README-L1)

Original MD: [tags.md](../source/docs/tags.md#L1-L61).

<a id="tags-L1"></a>

> Collector metadata display: original leading YAML frontmatter, source lines 1–4; not an upstream body heading.


```yaml
---
title: "Tags"
description: "Lightweight, free-form classification labels attached to elements of a data contract."
---
```


<!--
Copyright 2026 The Bitol Contributors
SPDX-License-Identifier: Apache-2.0
-->


<a id="tags-L11"></a>

# Tags

Tags are lightweight, free-form classification labels that can be attached to many elements of a data contract. The structure is shared across the Bitol standards and follows the same shape everywhere it appears.

[Back to TOC](#README-L1)


<a id="tags-L17"></a>

## What tags are for

Tags are intended for **categorization** — making elements easier to find, filter, group, and route through tooling. Common uses include:

- **Domain or topic**: `finance`, `marketing`, `iot`
- **Sensitivity / compliance**: `pii`, `phi`, `gdpr`, `pci`, `sensitive`
- **Lifecycle**: `experimental`, `deprecated`, `terminal`
- **Audience**: `internal`, `external`, `partner`
- **Operational hint**: `hot`, `cold`, `archive`

Tags are deliberately not a controlled vocabulary in ODCS: your organisation defines what each tag means. For richer, governed metadata, prefer [authoritative definitions](#authoritative-definitions-L1) or [custom properties](#custom-other-properties-L1).


<a id="tags-L29"></a>

## Structure

A `tags` value is always an **array of strings**. Empty arrays are allowed; duplicate strings within the same array should be avoided.

```yaml
tags: ['finance', 'sensitive']
```

The same structure applies wherever `tags` is permitted.


<a id="tags-L39"></a>

## Where tags can appear

`tags` is available in the following places:

| Location                  | Notes                                                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Top-level (data contract) | Tags applied to the contract as a whole. See [Fundamentals](#fundamentals-L1).                                          |
| Schema element (object)   | Tags applied to a table/topic/file. See [Schema](#schema-L1).                                                           |
| Schema element (property) | Tags applied to an individual column/field. See [Schema](#schema-L1).                                                   |
| Enum value                | Tags applied to a specific enumeration entry (e.g., `terminal`, `active`). See [Enumerations](#schema-L425). |
| Data quality check        | Tags applied to a quality rule. See [Data Quality](#data-quality-L1).                                                   |
| Team                      | Tags applied to the team block. See [Team](#team-L1).                                                                   |
| Team member               | Tags applied to an individual team member. See [Team](#team-L1).                                                        |


<a id="tags-L53"></a>

## Recommendations

- **Lowercase, snake_case or single words.** Mixed casing makes filtering brittle.
- **Be consistent.** A tag `pii` in one contract and `PII` in another defeats the purpose. Document your tag taxonomy organisation-wide.
- **Prefer specific over generic.** `customer_pii` is more useful than `sensitive` once you have many contracts.
- **Avoid encoding hierarchy in tag strings.** `finance/regulatory` is harder for tooling than two separate tags `finance`, `regulatory`.
- **Keep tags small in number.** A handful per element is plenty; long tag lists become noise.

[Back to TOC](#README-L1)

Original MD: [variables.md](../source/docs/variables.md#L1-L60).

<a id="variables-L1"></a>

> Collector metadata display: original leading YAML frontmatter, source lines 1–4; not an upstream body heading.


```yaml
---
title: "Variables"
description: "Variable interpolation in ODCS: keep secrets and environment-specific values out of the data contract with ${VAR_NAME} references resolved at runtime by tooling."
---
```


<!--
Copyright 2026 The Bitol Contributors
SPDX-License-Identifier: Apache-2.0
-->


<a id="variables-L11"></a>

# Variables

Any string value in a data contract MAY contain one or more variable references of the form `${VAR_NAME}`, resolved at runtime by tooling ([RFC 0050](https://github.com/bitol-io/tsc/blob/main/rfcs/approved/odcs-v3.2.0/0050-variables.md), shared with ODPS and OORS). This keeps secrets and environment-specific values — hostnames, bucket paths, credentials — out of the contract itself, so the same contract works across environments and is safe to store in version control.

References MAY appear as a whole value or as a substring. A reference MAY carry an inline default using the POSIX `${VAR_NAME:-default}` form: the text between `:-` and the closing `}` is used verbatim when the variable is unset or empty.

`VAR_NAME` is an identifier chosen by the contract author. Resolution is intentionally left to tooling; common sources include OS environment variables, `.env` files, secret managers, and CI/CD pipeline variables.


<a id="variables-L19"></a>

## Example

```yaml
servers:
  - server: prod_db
    environment: prod
    type: postgresql
    host: ${DB_HOST}
    port: ${DB_PORT:-5432}
    database: ${DB_NAME:-orders}
    schema: ${DB_SCHEMA:-public}
```

A variable reference is valid in any string value, not just `servers`, and MAY appear as a substring of a larger value — for example in a quality rule query:

```yaml
quality:
  - type: sql
    query: "SELECT COUNT(*) FROM ${TARGET_TABLE} WHERE created_at > ${CUTOFF_DATE}"
```


<a id="variables-L40"></a>

## Syntax

| Form                    | Behavior when the variable is set | Behavior when the variable is unset or empty |
|-------------------------|-----------------------------------|----------------------------------------------|
| `${VAR_NAME}`           | Replaced by the variable's value. | Tooling SHOULD surface an error; it MUST NOT silently substitute an empty string. |
| `${VAR_NAME:-default}`  | Replaced by the variable's value. | Replaced by `default`, verbatim.             |


<a id="variables-L47"></a>

## Tooling behavior

* Tools MUST resolve `${VAR_NAME}` references before using the value for any purpose.
* If a referenced variable cannot be resolved (and no default is supplied), tools SHOULD surface an error and MUST NOT silently substitute an empty string.
* Tools MUST preserve unresolved `${VAR_NAME}` and `${VAR_NAME:-default}` tokens verbatim when serializing a contract back to YAML (round-trip safety).
* Tools MAY define their own resolution order across sources (for example, OS environment variable before `.env` file).


<a id="variables-L54"></a>

## Notes

* Interpolation applies to **string** values only. A field typed as an integer or boolean in the JSON schema cannot hold a variable reference: the unresolved token is a string and the schema rejects it.
* The server `port` is an exception: the schema accepts an integer or a string, so it can hold a variable reference such as `${DB_PORT}` or `${DB_PORT:-5432}`.
* No new section or field is added to the standard: a contract using variables validates against the standard JSON schema as-is.

[Back to TOC](#README-L1)

Original YAML: [full-example.odcs.yaml](../source/docs/examples/all/full-example.odcs.yaml#L1-L362).

<a id="full-example-odcs-L1"></a>

## Native YAML example (collector display, not upstream Markdown)

```yaml
# Copyright 2026 The Bitol Contributors
# SPDX-License-Identifier: Apache-2.0

# What's this data contract about?
domain: seller # Domain
dataProduct: my quantum # Data product name
version: 1.1.0 # Version (follows semantic versioning)
status: active
id: 53581432-6c55-4ba2-a65f-72344a91553a

authoritativeDefinitions:
- type: canonical
  url: https://github.com/bitol-io/open-data-contract-standard/blob/main/docs/examples/all/full-example.odcs.yaml
  description: Canonical URL to the latest version of the contract.
  
# Lots of information
description:
  purpose: Views built on top of the seller tables.
  limitations: Data based on seller perspective, no buyer information
  usage: Predict sales over time
  authoritativeDefinitions:
    - type: privacy-statement
      url: https://example.com/gdpr.pdf
tenant: ClimateQuantumInc

kind: DataContract
apiVersion: v3.2.0 # Standard version (follows semantic versioning)

# Infrastructure & servers
servers:
  - server: my-postgres
    type: postgres
    host: localhost
    port: 5432
    database: pypl-edw
    schema: pp_access_views

# Dataset, schema, and quality
schema:
  - id: tbl_obj
    name: tbl
    physicalName: tbl_1
    physicalType: table
    businessName: Core Payment Metrics
    description: Provides core payment metrics
    authoritativeDefinitions:
      - url: https://catalog.data.gov/dataset/air-quality
        type: businessDefinition
      - url: https://youtu.be/jbY1BKFj9ec
        type: videoTutorial
    tags: [ 'finance', 'payments']
    dataGranularityDescription: Aggregation on columns txn_ref_dt, pmt_txn_id
    # Schema-level relationships (for composite keys)
    relationships:
      - type: foreignKey
        from:
          - tbl.rcvr_id
          - tbl.rcvr_cntry_code
        to:
          - receivers.id
          - receivers.country_code
        customProperties:
          - property: description
            value: "Composite key linking to receivers table"
          - property: cardinality
            value: "many-to-one"
    properties:
      - id: txn_ref_dt_prop
        name: transaction_reference_date
        physicalName: txn_ref_dt
        primaryKey: false
        primaryKeyPosition: -1
        businessName: transaction reference date
        logicalType: date
        physicalType: date
        required: false
        description: Reference date for transaction
        partitioned: true
        partitionKeyPosition: 1
        criticalDataElement: false
        tags: [ ]
        classification: public
        transformSourceObjects:
          - table_name_1
          - table_name_2
          - table_name_3
        transformLogic: sel t1.txn_dt as txn_ref_dt from table_name_1 as t1, table_name_2 as t2, table_name_3 as t3 where t1.txn_dt=date-3
        transformDescription: defines the logic in business terms; logic for dummies
        examples:
          - "2022-10-03"
          - "2020-01-28"
        customProperties:
          - property: anonymizationStrategy
            value: none
      - id: rcvr_id_prop
        name: rcvr_id
        primaryKey: true
        primaryKeyPosition: 1
        businessName: receiver id
        logicalType: string
        physicalType: varchar(18)
        required: false
        description: A description for column rcvr_id.
        partitioned: false
        partitionKeyPosition: -1
        criticalDataElement: false
        tags: [ 'uid' ]
        classification: restricted
        # Property-level relationship (from is implicit)
        relationships:
          - to: receivers.id
            type: foreignKey
            customProperties:
              - property: description
                value: "Links to receiver master data"
      - id: rcvr_cntry_code_prop
        name: rcvr_cntry_code
        primaryKey: false
        primaryKeyPosition: -1
        businessName: receiver country code
        logicalType: string
        physicalType: varchar(2)
        required: false
        description: Country code
        partitioned: false
        partitionKeyPosition: -1
        criticalDataElement: false
        tags: [ ]
        classification: public
        # Enumeration of allowed values (RFC 0033, ODCS v3.2.0+)
        enum:
          - value: US
            label: United States
            description: ISO 3166-1 alpha-2 code for the United States.
          - value: CA
            label: Canada
          - value: MX
            label: Mexico
            customProperties:
              - property: languageEs
                value: México
        authoritativeDefinitions:
          - url: https://collibra.com/asset/742b358f-71a5-4ab1-bda4-dcdba9418c25
            type: businessDefinition
          - url: https://github.com/myorg/myrepo
            type: transformationImplementation
          - url: jdbc:postgresql://localhost:5432/adventureworks/tbl_1/rcvr_cntry_code
            type: implementation
        encryptedName: rcvr_cntry_code_encrypted
        quality:
          - metric: nullValues
            mustBe: 0
            description: column should not contain null values
            dimension: completeness
            type: library
            severity: error
            businessImpact: operational
            schedule: 0 20 * * *
            scheduler: cron
            customProperties:
              - property: FIELD_NAME
                value:
              - property: COMPARE_TO
                value:
              - property: COMPARISON_TYPE
                value: Greater than
    quality:
      - metric: rowCount
        mustBeGreaterThan: 1000000
        type: library
        description: Ensure row count is within expected volume range
        dimension: completeness
        method: reconciliation
        severity: error
        businessImpact: operational
        schedule: 0 20 * * *
        scheduler: cron
    customProperties:
      - property: business-key
        value:
          - txn_ref_dt
          - rcvr_id

  # Receivers master table
  - id: receivers_obj
    name: receivers
    physicalName: receivers_master
    physicalType: table
    businessName: Receivers Master Data
    description: Master data for all receivers
    tags: [ 'master-data', 'receivers' ]
    properties:
      - id: receiver_id_prop
        name: id
        primaryKey: true
        primaryKeyPosition: 1
        businessName: receiver identifier
        logicalType: string
        physicalType: varchar(18)
        required: true
        description: Unique identifier for receiver
        unique: true
        classification: restricted
      - id: country_code_prop
        name: country_code
        primaryKey: true
        primaryKeyPosition: 2
        businessName: receiver country
        logicalType: string
        physicalType: varchar(2)
        required: true
        description: Country code of the receiver
        classification: public
      - id: receiver_name_prop
        name: receiver_name
        businessName: receiver name
        logicalType: string
        physicalType: varchar(255)
        required: true
        description: Name of the receiver
        classification: restricted
      - id: receiver_type_prop
        name: receiver_type
        businessName: receiver type
        logicalType: string
        physicalType: varchar(20)
        required: false
        description: Type of receiver (individual, business, etc.)
        classification: public
        # Example of nested reference
        relationships:
          - to: receiver_types.type_code
            customProperties:
              - property: description
                value: "Links to receiver type definitions"
      # Map-typed property (RFC 0030, ODCS v3.2.0+)
      - id: receiver_attributes_prop
        name: receiver_attributes
        businessName: receiver attributes
        logicalType: map
        physicalType: "MAP<STRING, STRING>"
        required: false
        description: Free-form attributes attached to a receiver, keyed by attribute name.
        classification: restricted
        map:
          key:
            logicalType: string
            description: Attribute name.
          value:
            logicalType: string
            description: Attribute value.


# Pricing
price:
  priceAmount: 9.95
  priceCurrency: USD
  priceUnit: megabyte


# Team
team:
  name: my-team
  description: The team owning the data contract
  members:
    - username: ceastwood
      role: Data Scientist
      dateIn: "2022-08-02"
      dateOut: "2022-10-01"
      replacedByUsername: mhopper
    - username: mhopper
      role: Data Scientist
      dateIn: "2022-10-01"
    - username: daustin
      role: Owner
      description: Keeper of the grail
      dateIn: "2022-10-01"


# Roles
roles:
  - role: microstrategy_user_opr
    access: read
    firstLevelApprovers: Reporting Manager
    secondLevelApprovers: 'mandolorian'
  - role: bq_queryman_user_opr
    access: read
    firstLevelApprovers: Reporting Manager
    secondLevelApprovers: na
  - role: risk_data_access_opr
    access: read
    firstLevelApprovers: Reporting Manager
    secondLevelApprovers: 'dathvador'
  - role: bq_unica_user_opr
    access: write
    firstLevelApprovers: Reporting Manager
    secondLevelApprovers: 'mickey'

# SLA
slaProperties:
  - property: latency # Property, see list of values in DP QoS
    value: 4
    unit: d # d, day, days for days; y, yr, years for years
    element: tab1.txn_ref_dt # This would not be needed as it is the same table.column as the default one
  - property: generalAvailability
    value: "2022-05-12T09:30:10-08:00"
  - property: endOfSupport
    value: "2032-05-12T09:30:10-08:00"
  - property: endOfLife
    value: "2042-05-12T09:30:10-08:00"
  - property: retention
    value: 3
    unit: y
    element: tab1.txn_ref_dt
  - property: frequency
    value: 1
    valueExt: 1
    unit: d
    element: tab1.txn_ref_dt
  - property: timeOfAvailability
    value: 09:00-08:00
    element: tab1.txn_ref_dt
    driver: regulatory # Describes the importance of the SLA: [regulatory|analytics|operational|...]
  - property: timeOfAvailability
    value: 08:00-08:00
    element: tab1.txn_ref_dt
    driver: analytics


# Support
support:
  - channel: '#product-help' # Simple Slack communication channel
    tool: slack
  - channel: datacontract-ann # Simple distribution list
    tool: email
    url: mailto:datacontract-ann@bitol.io
  - channel: Feedback  # Product Feedback
    description: General Product Feedback (Public)
    url: https://product-feedback.com
  - channel: 'product-issues'
    tool: teams
    scope: issues
    customProperties:
    - property: servicehours
      value: 9-5 CET


# Tags
tags:
  - transactions


# Custom properties
customProperties:
  - property: refRulesetName
    value: gcsc.ruleset.name
  - property: somePropertyName
    value: property.value
  - property: dataprocClusterName # Used for specific applications like Elevate
    value: [ cluster name ]

contractCreatedTs: "2022-11-15T02:59:43+00:00"
```


<!-- materialization-redistribution-notice -->
## Redistribution notice

This collector assembly includes material copied from or derived from "Open Data Contract Standard 3.2.0", https://github.com/bitol-io/open-data-contract-standard/tree/f0bdad95346905d500be5ef4b2c2d9b1d95223b7. Copyright 2026 The Bitol Contributors. SPDX-License-Identifier: Apache-2.0. Licensed under the Apache License, Version 2.0, https://www.apache.org/licenses/LICENSE-2.0. Original copyright, SPDX and trademark notices are retained; no endorsement or trademark license is claimed.

Changes: 原件逐字节复制，未修改或执行；从固定 Git commit 的 README、15个 Markdown 章节与完整 YAML 示例按声明顺序装配 collector Markdown，新增来源标签、真实行锚点、有限本地 href/正文图路由及唯一归属/修改说明末注，保留原表格、Required 条件、围栏、版权/SPDX及商标提示。完整 YAML 原文仅放入标明 example 的代码围栏，不称 schema。Fig1 PNG 保持原像素，图内标签/关系未全部线性化；外部 RFC 和其他外链只保留原链接，不补抓。旧 root document.md、27个 selectors 与完整旧 manifest 字典不变；完整旧 NOTICE 原字节前缀保留，本次说明仅累积追加。

Scope: 仅覆盖固定 Git commit f0bdad95346905d500be5ef4b2c2d9b1d95223b7 的19件实际原件：docs/README.md、docs/fundamentals.md、docs/schema.md、docs/context.md、docs/references.md、docs/data-quality.md、docs/support-communication-channels.md、docs/pricing.md、docs/team.md、docs/roles.md、docs/service-level-agreement.md、docs/infrastructure-servers.md、docs/custom-other-properties.md、docs/authoritative-definitions.md、docs/tags.md、docs/variables.md、docs/examples/all/full-example.odcs.yaml、LICENSE、docs/img/elements-of-schema-odcs-v3.png，以及按 README→15章→完整 YAML 示例顺序生成的 normalized/document.md 与 normalized/selectors.jsonl。LICENSE 和 Fig1 PNG 为明确原件；YAML 是完整数据合同示例而非 JSON Schema。旧网页首页文字及27个根 selectors 仅保留既有历史许可包，不把新 grant 追认到其他旧材料。本范围不包括整个仓库/站点、resources.md、其他 examples、JSON Schema companion、Bitol 品牌图、外部 RFC（包括 RFC-0038 完整 cascading 规范）、外链作品/数据/runtime、商标权或权利人无权许可的第三方材料。

Full license and original rights links: [NOTICE.md](../NOTICE.md).

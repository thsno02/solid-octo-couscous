# Retained documentation text (collector assembly)

> This consumer Markdown assembles the explicitly retained originals in declared order. Source labels, line anchors and local href rewrites are collector additions; only explicitly declared one-level DocFX include bodies are expanded in place, with fixed source reference URLs; include frontmatter is not body text.

Original MD: [overview.md](../source/docs/iq/ontology/overview.md#L1-L75).

<a id="overview-L1"></a>

> Collector metadata display: original leading YAML frontmatter, source lines 1–7; not an upstream body heading.



```yaml
---
title: What Is Ontology (Preview)?
description: Learn about core concepts and features of the ontology (preview) item.
ms.date: 10/06/2025
ms.topic: overview
ms.search.form: Ontology Overview
---
```



<a id="overview-L9"></a>

# What is ontology (preview)?

The *ontology (preview)* item (part of the [Fabric IQ (preview) workload](https://raw.githubusercontent.com/MicrosoftDocs/fabric-docs/91971feb08d699c09c20125faccae35effd60166/docs/iq/overview.md)) digitally represents the enterprise vocabulary and semantic layer that unifies meaning across domains and OneLake sources. It defines enterprise concepts as *entity types* (like *Customer*), *properties* (like a Customer's *name* and *email*), and *relationships* (like *Customer places Order*), while clarifying the constraints of these terms. After defining your ontology, bind the entity type definitions to real data, so downstream tools can share the same language. Both humans and AI agents can use this language for cross-domain reasoning and decision-ready actions.

Ontology in Fabric provides a scaled, secure, and governed shared business model used across teams, agents, and workflows in Fabric IQ. It provides a shared context layer that can be consumed by Fabric agents and Real-Time Intelligence components for consistent reasoning and actions. Ontology works well in situations where you need cross-domain consistency, governance, or AI agent grounding, and you want to reason across processes.


> Collector include: [feature-preview-note.md](../source/docs/includes/feature-preview-note.md#L9-L10), called at [overview.md line 15](../source/docs/iq/ontology/overview.md#L15-L15); original Markdown retained unchanged.

<a id="feature-preview-note-at-overview-L15-L9"></a>

> [!IMPORTANT]
> This feature is in [preview](https://raw.githubusercontent.com/MicrosoftDocs/fabric-docs/91971feb08d699c09c20125faccae35effd60166/docs/fundamentals/preview.md).


<a id="overview-L17"></a>

## Ontology overview

An *ontology* is a shared, machine-understandable vocabulary of your business. It's made up of the **things** in your environment (represented as *entity types*), their **facts** (represented as *properties* on entity types), and the ways they **connect** (represented as *relationships*), while offering constraints and rules that keep representations consistent. 

You can also think of an ontology like a business context layer, containing:

* A catalog of concepts (like *Product*, *Order*, *Plant*, *Sensor*, *Route*), defined once and reused everywhere
* Data bindings, or connections that link those concepts to your actual data sources in OneLake
* A graph representation that links related concepts for richer navigation, lineage, and reasoning
* A query surface that lets you ask questions about concepts (not just tables), supporting federated queries across sources


<a id="overview-L28"></a>

## Core concepts: Defining an ontology

An ontology consists of [entity types](#entity-type), [entity instances](#entity-instance), [properties](#property), and [relationships](#relationship). This section describes each of these core concepts.


<a id="overview-L32"></a>

### Entity type

An *entity type* is the reusable logical model of a real world concept (like *Shipment*, *Product*, or *Sensor*). It standardizes the name, description, identifiers, properties, and constraints for that item, so that every team in your business means the same thing when they use a term like "shipment." By elevating the concept above any single table, entity types eliminate conflicting column level definitions across sources. They provide a single point to attach properties, relationships, and labels that downstream tools can use to improve semantics across tables and models.


<a id="overview-L36"></a>

### Entity instance

An *entity instance* is a concrete occurrence of an entity type, populated from data bindings (like a semantic row). Entity instances keep track of which source created them and when they were true, and can participate in relationships. Entity instances turn your raw data into standardized business objects that all your tools and AI agents can understand in the same way.


<a id="overview-L40"></a>

### Property

A *property* is a named fact about an entity, with a declared data type. It can contain bindings to source data and semantic annotations (like an *identifier* or metadata attributes). Properties improve semantics by enforcing consistent types, units, and naming, and by enabling rules and quality checks at the concept level.


<a id="overview-L44"></a>

### Relationship

A *relationship* is a typed, directional link between entity types or instances. Relationships can have attributes (like *distance*, *confidence*, or *effectiveAt*) and cardinality rules defining how many items can be related (for example, one *Customer* having many *Orders*). Relationships make context explicit and reusable for how things connect, enabling traversal, dependency analysis, rule based inference, and clearer answers to business questions without custom join logic.


<a id="overview-L48"></a>

## Core concepts: Your data in the ontology

After you define an ontology, you can [bind it to your data](https://raw.githubusercontent.com/MicrosoftDocs/fabric-docs/91971feb08d699c09c20125faccae35effd60166/docs/iq/ontology/how-to-bind-data.md) to visualize and query the data in the context of your ontology. Read about each core data concept in the following sections.


<a id="overview-L52"></a>

### Data binding

*Data binding* connects your ontology's definitions (including entity types, properties, and relationships) to concrete data living in OneLake, including lakehouse tables, eventhouse streams, and Power BI semantic models. A data binding describes data types, identity keys, how columns map to properties, and how keys map to relationships across multiple data sources. By enabling schema evolution rules, data quality checks (based on things like nullability, ranges, and uniqueness), and provenance at the concept layer, bindings turn raw rows and events into governed business objects. Data binding ensures your data has consistent meaning, follows the same rules, and tracks where it came from across different data sources.


> Collector include: [refresh-graph-model.md](../source/docs/iq/ontology/includes/refresh-graph-model.md#L7-L9), called at [overview.md line 56](../source/docs/iq/ontology/overview.md#L56-L56); original Markdown retained unchanged.

<a id="refresh-graph-model-at-overview-L56-L7"></a>


>[!NOTE]
> Any updates in upstream data sources (like new rows) need to be manually refreshed before they're visible in the ontology item. For more information, see [refresh the graph model](https://raw.githubusercontent.com/MicrosoftDocs/fabric-docs/91971feb08d699c09c20125faccae35effd60166/docs/iq/ontology/how-to-view-entity-type-details.md#refresh-the-graph-model).


<a id="overview-L58"></a>

### Ontology graph

The *ontology graph* is a queryable instance graph built from your data bindings and relationship definitions, provided within ontology by [Graph in Microsoft Fabric](https://raw.githubusercontent.com/MicrosoftDocs/fabric-docs/91971feb08d699c09c20125faccae35effd60166/docs/graph/overview.md). You can see the graph in the [entity type details](https://raw.githubusercontent.com/MicrosoftDocs/fabric-docs/91971feb08d699c09c20125faccae35effd60166/docs/iq/ontology/how-to-view-entity-type-details.md). 

In the graph, nodes are entity instances, and edges are links (either asserted or derived) with metadata attributes. Each node or edge keeps data source lineage and follows a scheduled data refresh. Graphs enable visual exploration of business context, execution of graph algorithms (like paths, centrality, and communities), and rule‑driven inferences. Graphs improve semantics by making relationships first‑class, so context is explicit, queryable, and governed (not buried in join logic).


> Collector include: [refresh-graph-model.md](../source/docs/iq/ontology/includes/refresh-graph-model.md#L7-L9), called at [overview.md line 64](../source/docs/iq/ontology/overview.md#L64-L64); original Markdown retained unchanged.

<a id="refresh-graph-model-at-overview-L64-L7"></a>


>[!NOTE]
> Any updates in upstream data sources (like new rows) need to be manually refreshed before they're visible in the ontology item. For more information, see [refresh the graph model](https://raw.githubusercontent.com/MicrosoftDocs/fabric-docs/91971feb08d699c09c20125faccae35effd60166/docs/iq/ontology/how-to-view-entity-type-details.md#refresh-the-graph-model).


<a id="overview-L66"></a>

### Querying your ontology

*Ontology querying* lets you ask business-level questions over bound data sources through ontology terminology. Queries start with entity types and allow filtering by properties, traversing relationships, aggregating by time, and other constraints. The ontology layer automatically sends your queries to the most efficient system to get results quickly (such as GQL for Graph in Microsoft Fabric and KQL for Eventhouse). It also includes a Natural Language to Ontology (NL2Ontology) query layer, which converts your natural language questions into structured queries and returns relevant results. This enables you to ask questions using business terms, instead of needing to know the details of how your data is stored in different systems. NL2Ontology queries ensure that filters, joins, units, and validity windows align with the definitions that are published in your ontology.


<a id="overview-L70"></a>

## Next steps

* Prepare your tenant for ontology (preview) by enabling required tenant settings in [Ontology (preview) required tenant settings](https://raw.githubusercontent.com/MicrosoftDocs/fabric-docs/91971feb08d699c09c20125faccae35effd60166/docs/iq/ontology/overview-tenant-settings.md).
* Get started with the [Ontology (preview) tutorial](https://raw.githubusercontent.com/MicrosoftDocs/fabric-docs/91971feb08d699c09c20125faccae35effd60166/docs/iq/ontology/tutorial-0-introduction.md).
* Skip ahead to instructions for [generating an ontology from a semantic model](https://raw.githubusercontent.com/MicrosoftDocs/fabric-docs/91971feb08d699c09c20125faccae35effd60166/docs/iq/ontology/tutorial-1-create-ontology.md?pivots=semantic-model#generating-an-ontology-from-a-semantic-model).



<!-- materialization-redistribution-notice -->
## Redistribution notice

Microsoft Fabric Ontology (Preview), public native documentation at commit 91971feb08d699c09c20125faccae35effd60166; Microsoft and contributors. Include feature-preview-note.md credits snehagunda / sngun. The documentation is licensed under CC BY 4.0; full license, original Legal Notices, source URLs and trademark reservation are retained in NOTICE. No endorsement is implied.

Changes: Three official native Markdown files are retained byte-identically, including their original frontmatter. The collector-derived consumer removes frontmatter from body, expands the two explicitly declared DocFX includes at their three original positions, resolves relative document links to the same fixed public commit without fetching those links, and adds source boundaries, real line selectors and one attribution/modification footer. No source prose, preview/refresh warning, code or upstream dates are corrected; no OCR, source execution or Learn website skin is included.

Scope: Only docs/iq/ontology/overview.md (7686 bytes), docs/includes/feature-preview-note.md (403 bytes) and docs/iq/ontology/includes/refresh-graph-model.md (447 bytes) at public commit 91971feb08d699c09c20125faccae35effd60166; corresponding normalized/document.md and normalized/selectors.jsonl, complete NOTICE and provenance. Two literal include dependencies occur once and twice respectively. Other product pages, tutorials, graphs/assets, model/data downloads, private deployment repositories, website HTML/skin/scripts, external works, patents and trademarks are excluded. Historical metadata-only facts remain preserved and are not new body evidence.

Full license and original rights links: [NOTICE.md](../NOTICE.md).

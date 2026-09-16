# Retained specification text (collector assembly)

This consumer Markdown assembles the explicitly retained originals in declared order. Source labels, line anchors and local href rewrites are collector additions; YAML below is an unmodified native schema displayed in a code fence.

Original MD: [spec-intro.md](../source/src/docs/spec-intro.md#L1-L31).

<a id="spec-intro-L1"></a>

# Specification of the SSSOM standard

This document is the official specification for the SSSOM standard.

It is divided in two sections covering the two different components of the standard:

* the specification for the [data model](#spec-model-L1), to manipulate SSSOM mappings and mapping sets in your programs;
* the specification for the [serialisation formats](#spec-formats-L1), to read, write, and exchange SSSOM mapping sets.

Both sections are _normative_.


<a id="spec-intro-L12"></a>

## Conventions used in this document


<a id="spec-intro-L14"></a>

### Key words

Throughout the specification, the key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “NOT RECOMMENDED”, “MAY”, and “OPTIONAL” are to be interpreted as described in [BCP 14](https://datatracker.ietf.org/doc/html/bcp14) when, and only when, they appear in all capitals, as shown here.


<a id="spec-intro-L18"></a>

### IRI prefixes

Throughout the specification, the following IRI prefix names are used:

| Prefix name | IRI prefix |
| ----------- | ---------- |
| owl         | http://www.w3.org/2002/07/owl# |
| rdf         | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs        | http://www.w3.org/2000/01/rdf-schema# |
| semapv      | https://w3id.org/semapv/vocab/ |
| skos        | http://www.w3.org/2004/02/skos/core# |
| sssom       | https://w3id.org/sssom/ |
| xsd         | http://www.w3.org/2001/XMLSchema# |
| linkml      | https://w3id.org/linkml/ |

Original MD: [spec-model.md](../source/src/docs/spec-model.md#L1-L192).

<a id="spec-model-L1"></a>

# The SSSOM data model

The SSSOM data model (hereafter “the model”) defines the data structure to represent and manipulate SSSOM concepts. The model is formally described as a [LinkML](https://linkml.io/) schema, from which the [documentation](../source/src/sssom_schema/schema/sssom_schema.yaml#L1-L792) is derived.

This section provides an overview of the model and supplementary informations that may not be found in the schema (and its derived documentation) itself. Of note, the schema, not this section, is always the authoritative source of truth for all questions pertaining to the model.


<a id="spec-model-L7"></a>

## Overview

The model consists in a handful of classes, the most important of them being the [`Mapping` class](../source/src/sssom_schema/schema/sssom_schema.yaml#L648-L730) and the [`MappingSet` class](../source/src/sssom_schema/schema/sssom_schema.yaml#L612-L647). Any SSSOM implementation MUST support those two classes and all their slots; support for the other classes is OPTIONAL.

The `Mapping` class represents an individual mapping. Fundamental slots in that class are:

* `subject_id` and `object_id`, referring to the entities being mapped to each other;
* `predicate_id`, referring to the relationship between the mapped entities;
* `mapping_justification`, which should provide the justification for the mapping.

Those slots are mandatory (including the `mapping_justification` slot: the SSSOM standard posits that there can be no mapping without some form of justification) and an implementation MUST NOT allow the creation of a mapping object that does not have a value for any one of them.

Other slots are intended to provide further details about a mapping. Those “further details” are sometimes referred to as “mapping metadata”, though the SSSOM standard makes no formal distinction between “data” and “metadata” – there are only “data about a mapping”.

The `MappingSet` class represents, well, a set of individual mappings, which are contained in the `mappings` slot (a list of `Mapping` instances). Other slots in that class are intended either to provide further details about the set itself (sometimes referred to as “mapping set metadata”, with the same caveat as above regarding the data/metadata distinction), or to provide common details for all the mappings in the set (see the [Propagation of mapping set slots](#spec-model-L35) section further below for details).

Of note, within a set, a mapping may not necessarily be uniquely identified by the combination of its four mandatory slots (`subject_id`, `predicate_id`, `object_id`, and `mapping_justification`). A set may very well contain several mappings with the same subject, predicate, object, and justification, but that differ on some of the other, complementary slots.



<a id="spec-model-L26"></a>

## Identifiers

Throughout the model, identifiers to external resources are represented using the custom type [`EntityReference`](../source/src/sssom_schema/schema/sssom_schema.yaml#L71-L79) (based on the LinkML type [`uriorcurie`](https://w3id.org/linkml/Uriorcurie)), which accepts both full-length IRIs and [CURIEs](https://www.w3.org/TR/curie/) as possible identifier formats. (Note however that serialisation formats may mandate the use of one identifier format over the other; for example, the [SSSOM/TSV](#spec-formats-tsv-L1) format requires the systematic use of CURIEs, whereas the [OWL/RDF](#spec-formats-owl-L1) format conversely requires the systematic use of IRIs).

Whenever the CURIE syntax is used in a mapping set (whether this is by choice of the SSSOM producer, or because it is mandated by the serialisation format), all CURIEs MUST be unambiguously resolvable into corresponding full-length IRIs without requiring any external resources. This means that any prefix name used MUST be properly declared in the set’s `curie_map` slot, which is a dictionary associating a prefix name to an IRI prefix.

By exception, prefix names listed in the table found in the [IRI prefixes](#spec-intro-L18) section are considered “built-in”. As such, they MAY be omitted from the `curie_map`. If they are not omitted, they MUST point to the same IRI prefixes as in the aforementioned table.



<a id="spec-model-L35"></a>

## Propagation of mapping set slots

As mentioned briefly above, there are two different types of slots in the `MappingSet` class:

* slots that provide informations about the set itself;
* slots that provide informations about all the mappings in the set.

The latter are called “propagatable slots”. In the LinkML model, they are marked with a `propagated` annotation whose value is set to `true`.

For convenience, here is the current list of propagatable slots:

* `mapping_date`,
* `mapping_provider`,
* `mapping_tool`,
* `mapping_tool_version`,
* `object_match_field`,
* `object_preprocessing`,
* `object_source`,
* `object_source_version`,
* `object_type`,
* `subject_match_field`,
* `subject_preprocessing`,
* `subject_source`,
* `subject_source_version`,
* `subject_type`.

When a mapping set object has a value in one of its propagatable slots, this MUST be interpreted as if all mappings within the set had that same value in their corresponding slot. For example, if a set has the value _foo_ in its `mapping_tool` slot, all the mappings in that set MUST be treated as if they had the value _foo_ in their `mapping_tool` slot.

This mechanism is intended as a convenience, so that a slot which has the same value for all mappings in a set can be specified only once at the level of the set rather than for each individual mapping.

Slots that are not in the above list (“non-propagatable slots”) describe the mapping set itself, not the mappings it contains, even if the slot also exists on the `Mapping` class. For example, the `creator_id` slot, when used in the `MappingSet` class, is intended to refer to the creators of the set, _not_ the creators of the individual mappings (which may be different, and which are listed in the `creator_id` slot of every mapping).



<a id="spec-model-L68"></a>

## Allowed and common mapping predicates

Implementations MUST accept any arbitrary predicate in the `predicate_id` slot.

The following mapping predicates are considered common, and implementations MAY encourage users to use them:

| Predicate | Description |
| --------- | ----------- |
| owl:sameAs | The subject and the object are instances (OWL individuals), and the two instances are the same. |
| owl:equivalentClass | The subject and the object are OWL classes, and the two classes are the same. |
| owl:equivalentProperty | The subject and the object are OWL object, data, or annotation properties, and the two properties are the same. |
| rdfs:subClassOf | The subject and the object are OWL classes, and the subject is a subclass of the object. |
| rdfs:subPropertyOf | The subject and the object are OWL object, data, or annotation properties, and the subject is a subproperty of the object. |
| skos:relatedMatch | The subject and the object are associated in some unspecified way. |
| skos:closeMatch | The subject and the object are sufficiently similar that they can be used interchangeably in some information retrieval applications. |
| skos:exactMatch | The subject and the object can, with a high degree of confidence, be used interchangeably across a wide range of information retrieval applications. |
| skos:narrowMatch | The object is a narrower concept than the subject. |
| skos:broadMatch | The object is a broader concept than the subject. |
| oboInOwl:hasDbXref | Two terms are related in some way. The meaning is frequently consistent across a single set of mappings. Note this property is often overloaded even where the terms are of a different nature (e.g. interpro2go). |
| rdfs:seeAlso | The subject and the object are associated in some unspecified way. The object IRI often resolves to a resource on the web that provides additional information. |

In addition, predicates from the following sources MAY also be encouraged:

* any relation from the [Relation Ontology (RO)](https://obofoundry.org/ontology/ro.html);
* any relation under [skos:mappingRelation](http://www.w3.org/2004/02/skos/core#mappingRelation) in the [Semantic Mapping Vocabulary](https://mapping-commons.github.io/semantic-mapping-vocabulary/).



<a id="spec-model-L95"></a>

## Literal mappings

<a id="literal-mappings"></a>

The SSSOM model is primarily intended to represent mappings between semantic entities. However, it may also be used to represent mappings where at least one side is a literal string that does not have an identifier of its own. Any such mapping is henceforth called a _literal mapping_.

To represent a mapping whose subject (resp. object) is a literal:

* the `subject_type` (resp. `object_type`) slot MUST be set to `rdfs literal`;
* the `subject_label` (resp. `object_label`) slot MUST be set to the literal itself;
* the `subject_id` (resp. `object_id`) slot MAY be left empty.

The last point is an exception to the normal rules about required slots, which state that a mapping must always have a `subject_id` and an `object_id`. Implementations MUST accept a mapping without a `subject_id` (resp. `object_id`) _if and only if_ the `subject_type` (resp. `object_type`) slot is set to `rdfs literal`.

All other slots in the `Mapping` class may be used normally in a literal mapping, with the same meaning as for a non-literal mapping.

When computing the cardinality of mappings in a set (e.g. to set the value of the `mapping_cardinality` slot), if the mapping has a literal subject (resp. object), then the `subject_label` (resp. `object_label`) slot must be used for determining the number of occurrences of the subject (resp. object) in the set.



<a id="spec-model-L114"></a>

## Representing unmapped entities

The special value `sssom:NoTermFound` MAY be used as the `object_id` of a mapping to explicitly state that the subject of said mapping cannot be mapped to any entity in the domain represented by the `object_source` slot.

Likewise, the `sssom:NoTermFound` value MAY be used as the `subject_id` of a mapping to state that the object of said mapping cannot be mapped to any entity in the domain represented by the `subject_source` slot.

When that special value is used as the `subject_id` (respectively `object_id`), the `subject_source` (respectively `object_source`) slot SHOULD be defined.

The `sssom:NoTermFound` value MUST NOT be used in any other slot than `subject_id` or `object_id`.

The meaning of the NOT predicate modifier in a mapping that refers to `sssom:NoTermFound` is unspecified.

When computing cardinality values (to fill the `mapping_cardinality` slot), mappings that refer to `sssom:NoTermFound` MUST be ignored.



<a id="spec-model-L129"></a>

## Non-standard slots

<a id="non-standard-slots"></a>

Implementations are only REQUIRED to support the standard metadata slots defined in the SSSOM LinkML schema.

However, implementations MAY support the use of supplementary, non-standard slots (hereafter called _extension slots_ or simply _extensions_). There are two types of extension slots: _defined_ extension slots and _undefined_ extension slots.


<a id="spec-model-L137"></a>

### Defined extensions

Defined extensions are non-standard slots that are explicitly declared (or, _defined_) before being used. Implementations SHOULD support the use of defined extensions.

Extensions are defined in the `extension_definition` slot of the `MappingSet` object. Each definition is comprised of three elements:

* the name of the slot, as it will appear when used in a mapping set (`slot_name`);
* a property intended to specify the meaning of the slot (`property`);
* the type of values expected by the slot (`type_hint`).

A definition MUST have at least a `slot_name`. The name MUST be a XML “non-colonized name” (“NCName”, see [Namespaces in XML, §2](https://www.w3.org/TR/1999/REC-xml-names-19990114/#NT-NCName)). The name MUST NOT match the name of an existing standard slot.

To avoid any conflicy with a future version of the SSSOM specification (which could introduce new standard slot names), implementations are strongly encouraged to craft extension slot names that start with the `ext_` prefix. No new standard slot with a name starting with `ext_` will ever be introduced in any future version of the standard. (This is an advice for SSSOM producers only; SSSOM consumers MUST NOT reject an extension slot solely on the basis that its name does not start with `ext`.)

A definition SHOULD have a `property`. If it does not, implementations MUST automatically construct a default property by concatenating the prefix `http://sssom.invalid/` with the name of the extension.

The slot name and the property MUST be unique to each definition. No two definitions can share the same name and/or the same property.

A definition MAY have a `type_hint`. If it does not, a default type of `http://www.w3.org/2001/XMLSchema#string` is assumed.

Once defined, an extension slot may be used as a supplementary slot in either the `Mapping` class or the `MappingSet` class (or both), as if it was a normal, standard slot. How those slots are represented internally and provided to client code is left at the discretion of the implementations.


<a id="spec-model-L159"></a>

### Undefined extensions

Undefined extensions are non-standard slots that are not explicitly defined as described in the previous section. Implementations MAY support undefined extensions.

Upon encountering a non-standard slot that is not a defined extension, an implementation that supports undefined extensions MUST behave as if the slot had been defined with:

* a `property` constructed by catenating the prefix `http://sssom.invalid/` to the name of the slot;
* a `type_hint` of `http://www.w3.org/2001/XMLSchema#string`.


<a id="spec-model-L168"></a>

### Restrictions on the values of extension slots


<a id="spec-model-L170"></a>

#### General restrictions

The following restrictions apply to all extension slots, regardless of whether they are defined or undefined.

Each mapping set and each mapping can have at most _one_ value for each extension slot. The expected behaviour upon encountering a repeated extension slot is unspecified.

An extension value MUST be either a string or an instance of a simple data type such as a numerical value (integer or floating point), a boolean value, or a date or datetime value. In particular, composite data structures (e.g. lists or dictionaries) MUST NOT be used as extension values.

It is always possible to use arbitrarily complex values by encoding them as literal strings. However, how complex values would be encoded is out of scope of this specification; implementations MUST treat such values as opaque strings.


<a id="spec-model-L180"></a>

#### Further restrictions for typed defined extensions

If a defined extension slot has a `type_hint` other than `http://www.w3.org/2001/XMLSchema#string`, implementations MAY enforce further constraints on extension values based on the type hint, according to the following table:

| Type hint | Constraints |
| --------- | ----------- |
| http://www.w3.org/2001/XMLSchema#integer  | Implementations MAY check that the value is an integer |
| http://www.w3.org/2001/XMLSchema#double   | Implementations MAY check that the value is a floating number |
| http://www.w3.org/2001/XMLSchema#boolean  | Implementations MAY check that the value is either `true` or `false` |
| http://www.w3.org/2001/XMLSchema#date     | Implementations MAY check that the value is a date in the ISO 8601 format (`yyyy-mm-dd`) |
| http://www.w3.org/2001/XMLSchema#datetime | Implementations MAY check that the value is a date and time value in the ISO 8601 format (`yyyy-mm-ddThh:mm:ssTZ`) |

Implementations MAY decide to recognise more types and to enforce type-specific constraints. For example, an implementation could recognise the type `http://www.w3.org/2001/XMLSchema#negativeInteger` and check that the value starts with a minus sign.

Original MD: [chaining-rules.md](../source/src/docs/chaining-rules.md#L1-L111).

<a id="chaining-rules-L1"></a>

## SSSOM Mapping Chains

The goal of this document is to capture all obvious mapping chaining rules that could be applied to SSSOM, 
and later delivered as part of `sssom toolkit`. 
This is all structural, and should not be confused with proper reasoning or mapping reconciliation ala 
[boomer](https://github.com/INCATools/boomer).

The idea is to provide the functionality to apply these chaining rules over a given mapping set, and record
the appropriate metadata for that rule.

Rules:

- [Transitivity Rule](#transitivity)
- [Role chains over exact/equivalent matches](#rce)
- [Inverse Rule](#inverse)
- [Generalisation Rule](#generalisation)

<a id="transitivity"></a>


<a id="chaining-rules-L20"></a>

## Transitivity Rule

Transitivity of a relation `R` implies that if an entity `A` is `R`-related to an entity `B` which in turn is 
`R`-related to an entity `C`, `A` is also `R`-related to `C`. 


<a id="chaining-rules-L25"></a>

### Predicates applicable in transitivity rules

We consider the following predicates transitive:

- skos:exactMatch
- skos:narrowMatch
- skos:broadMatch
- owl:equivalentClass / owl:equivalentProperty
- rdfs:subClassOf / rdfs:subPropertyOf	
- owl:sameAs

Note that technically speaking `skos:narrowMatch` and `skos:broadMatch` are not considered transitive 
(`skos:broaderTransitive` would be), but we are not defining a new semantics here, 
just a reasonable default for a mapping tool, which will nearly always hold true.

Predicates we do not consider transitive include: `skos:relatedMatch` (for practical reasons), `oboInOwl:hasDbXref`, 
`skos:closeMatch`, `rdfs:seeAlso` (weakest form of a mapping link), `rdf:type`.


<a id="chaining-rules-L43"></a>

### Rules

- T1: `(:A)-[predicate_id]->(:B)-[predicate_id]->(:C)` -> `(:A)-[predicate_id]->(:C)`


<a id="chaining-rules-L47"></a>

### Examples

- T1-EX: `(:A)-[skos:broadMatch]->(:B)-[skos:broadMatch]->(:C)` -> `(:A)-[skos:broadMatch]->(:C)`

<a id="rce"></a>


<a id="chaining-rules-L53"></a>

## Role chains over exact/equivalent matches

Role chains are rules that allow us to bridge across mappings across multiple different properties.
Role chains over exact are simple to define, so we start with these


<a id="chaining-rules-L58"></a>

### Predicates applicable in transitity rules

- skos:narrowMatch
- skos:broadMatch
- skos:closeMatch
- skos:relatedMatch


<a id="chaining-rules-L65"></a>

### Rules for SKOS

- RCE1: `(:A)-[skos:exactMatch|owl:equivalentClass]->(:B)-[predicate_id]->(:C)` -> `(:A)-[predicate_id]->(:C)`
- RCE2: `(:A)-[predicate_id]->(:B)-[skos:exactMatch]->(:C)` -> `(:A)-[predicate_id]->(:C)`


<a id="chaining-rules-L70"></a>

### Rules that should probably not be inferred (OWL)

The following rules hold true, but will be left to a reasoner to be inferred:

- RCE-N1: `(:A)-[owl:equivalentClass]->(:B)-[rdfs:subClassOf]->(:C)` -> `(:A)-[rdfs:subClassOf]->(:C)`
- RCE-N2: `(:A)-[rdfs:subClassOf]->(:B)-[owl:equivalentClass]->(:C)` -> `(:A)-[rdfs:subClassOf]->(:C)`
- RCE-N3: `(:A)-[owl:equivalentProperty]->(:B)-[rdfs:subPropertyOf]->(:C)` -> `(:A)-[rdfs:subPropertyOf]->(:C)`
- RCE-N4: `(:A)-[rdfs:subPropertyOf]->(:B)-[owl:equivalentProperty]->(:C)` -> `(:A)-[rdfs:subPropertyOf]->(:C)`

<a id="inverse"></a>


<a id="chaining-rules-L81"></a>

## Inverse Rules

`R` inverse of `S` implies that if an entity `A` is `R`-related to an entity `B` then `B` is also `S`-related to `A`. 
We like to call the output of an inverse rule a `walk-back`. A command that applies an inverse rule could be called `flip`. 


<a id="chaining-rules-L86"></a>

### Predicates applicable in inverse rules

This excludes the exact predicates for which inverse rules are redundant.


<a id="chaining-rules-L90"></a>

### Rules for SKOS

- RI1: `(:A)-[skos:narrowMatch]->(:B)` -> `(:B)-[skos:broadMatch]->(:A)`
- RI2: `(:A)-[skos:broadMatch]->(:B)` -> `(:B)-[skos:narrowMatch]->(:A)`


<a id="chaining-rules-L95"></a>

### Rules for SEMAPV

- RI3: `(:A)-[semapv:crossSpeciesExactMatch]->(:B)` -> `(:B)-[semapv:crossSpeciesExactMatch]->(:A)`
- RI4: `(:A)-[semapv:crossSpeciesNarrowMatch]->(:B)` -> `(:B)-[semapv:crossSpeciesBroadMatch]->(:A)`
- RI5: `(:A)-[semapv:crossSpeciesBroadMatch]->(:B)` -> `(:B)-[semapv:crossSpeciesNarrowMatch]->(:A)`

<a id="generalisation"></a>


<a id="chaining-rules-L103"></a>

## Generalisation Rules

Generalisation rules are rules that can be applied to weaken a mapping deliberately. This is sometimes useful, for example when
combining strong OWL-Semantics mappings with weaker SKOS-based ones.


<a id="chaining-rules-L108"></a>

## Rules

- RG1: `(:A)-[owl:equivalentTo]->(:B)` -> `(:A)-[skos:exactMatch]->(:B)`
- RG2: `(:A)-[owl:subClassOf]->(:B)` -> `(:A)-[skos:broadMatch]->(:B)`

Original MD: [spec-formats.md](../source/src/docs/spec-formats.md#L1-L9).

<a id="spec-formats-L1"></a>

# SSSOM serialisation formats

The SSSOM standard defines the following serialisation formats for storing and exchanging mapping sets:

* the [SSSOM/TSV](#spec-formats-tsv-L1) format;
* the [SSSOM JSON](#spec-formats-json-L1) format;
* and the [OWL/RDF](#spec-formats-owl-L1) format.

Implementations MUST support the SSSOM/TSV format. They MAY support the other formats.

Original MD: [spec-formats-tsv.md](../source/src/docs/spec-formats-tsv.md#L1-L328).

<a id="spec-formats-tsv-L1"></a>

# The SSSOM/TSV serialisation format

The SSSOM/TSV format is intended as the main format for exchanging SSSOM mapping set objects.

The RECOMMENDED filename extension for a SSSOM/TSV file is `.sssom.tsv`, but SSSOM/TSV parsers MUST accept SSSOM/TSV files regardless of their extension.



<a id="spec-formats-tsv-L8"></a>

## Structure

A SSSOM/TSV file contains one, and only one, mapping set object. It is made of two different parts:

* the _metadata block_, which contains essentially all the slots of the [`MappingSet` class](../source/src/sssom_schema/schema/sssom_schema.yaml#L612-L647) except the `mappings` slot;
* the _mappings block_ (also called the _TSV section_), which contains the individual mappings.

A SSSOM/TSV file MUST NOT contain anything other than those two blocks.



<a id="spec-formats-tsv-L18"></a>

### Metadata block

The metadata block is written as the [YAML 1.2](https://yaml.org/spec/1.2.2/) serialisation of the `MappingSet` object, except that the `mappings` slot is _not_ included (since it contains the mappings, that are serialised in the mappings block instead).

The metadata block MUST appear at the beginning of the file. Every line of the block MUST be preceded by a `#` character; the `#` character MAY be followed by one or several space characters (U+0020) before the YAML content – if so, every line MUST have the same number of space characters.

The metadata block ends with the first line that does not begin with a `#` character, which marks the beginning of the mappings block.

The metadata block SHOULD only contain the slots that do have a value. SSSOM/TSV writers SHOULD skip slots with no value when serialising the mapping set object.


<a id="spec-formats-tsv-L28"></a>

#### Multi-valued slots with a single value

As an exception to the standard YAML rules regarding the serialisation of sequences, a multi-valued slot that happens to contain a single value MAY be serialised as a scalar value rather than as sequence containing only one item.

For example, a `creator_id` slot with the single value `ORCID:1111-2222-3333-4444` MAY be serialised as

```yaml
creator_id: "ORCID:1111-2222-3333-4444"
```

This is, strictly speaking, invalid according the YAML specification; the correct serialisation would be either

```yaml
creator_id: [ "ORCID:1111-2222-3333-4444" ]
```

or

```yaml
creator_id:
  - "ORCID:1111-2222-3333-4444"
```

but the scalar form is frequently found in existing SSSOM/TSV files, so SSSOM/TSV parsers SHOULD accept it. SSSOM/TSV writers SHOULD favour one of the correct YAML serialisations, however.


<a id="spec-formats-tsv-L53"></a>

#### Forbidden YAML features

The following features of the YAML 1.2 specification MUST NOT be used within the metadata block:

* YAML directives ([YAML 1.2 §6.8.1](https://yaml.org/spec/1.2.2/#681-yaml-directives));
* TAG directives ([YAML 1.2 §6.8.2](https://yaml.org/spec/1.2.2/#682-tag-directives));
* Node tags ([YAML 1.2 §6.9.1](https://yaml.org/spec/1.2.2/#691-node-tags));
* Node anchors ([YAML 1.2 §6.9.2](https://yaml.org/spec/1.2.2/#692-node-anchors));
* Alias nodes ([YAML 1.2 §7.1](https://yaml.org/spec/1.2.2/#71-alias-nodes)).

SSSOM/TSV writers MUST NOT generate any of those when writing the metadata block. The expected behaviour of SSSOM/TSV parsers upon encountering them is unspecified.



<a id="spec-formats-tsv-L66"></a>

### Mappings block

The mappings block contains the mappings, serialised as a matrix where each line represents an individual mapping and each column (separated by tab characters, U+0009) represents one of the slots of the [`Mapping` class](../source/src/sssom_schema/schema/sssom_schema.yaml#L648-L730).

The mappings block MUST follow immediately the metadata block within a SSSOM/TSV file. It starts with a header line containing the column names, which are the names of the slots in the `Mapping` class.

There SHOULD be no empty columns. If none of the mappings in a set has a value for a given slot, that slot SHOULD be skipped when writing the header line and the individual mappings.

Multi-valued slots MUST be serialised as a list of values separated by `|` characters.


<a id="spec-formats-tsv-L76"></a>

#### Quoting

Within the mappings block, the following quoting rules, adapted from [RFC 4180](https://datatracker.ietf.org/doc/html/rfc4180), apply:

1. Any value MAY be enclosed in double quotes (`"`).
2. Values containing line breaks, double quotes, or tabs (U+0009) MUST be enclosed in double quotes.
3. When a value is enclosed in double quotes, a double quote appearing within the value MUST be escaped by preceding it with another double quote.

SSSOM/TSV parsers MUST strip any enclosing double quotes and escaping double quotes before passing the parsed objects to the application code.



<a id="spec-formats-tsv-L87"></a>

## External metadata mode

The metadata block MAY be stored in a separate file from the TSV section, instead of preceding it in the same file as described above. This is called the _external metadata mode_ (by contrast, when the two blocks are in the same file, this is called the _embedded metadata mode_).

In external mode, the metadata block follows the same rules as described in the [Metadata block](#spec-formats-tsv-L18) section above, except that lines MUST NOT start with a `#` character.

It is RECOMMENDED that the file containing the metadata block has the same basename as the file containing the TSV section, with a `.sssom.yml` extension.

When an external metadata file is used, the file containing the TSV section MUST NOT contain anything else than the TSV section. That is, the first line of that file MUST be the header line containing the column names.

Implementations SHOULD support reading SSSOM/TSV files in external metadata mode; they MAY support writing SSSOM/TSV files in that mode.



<a id="spec-formats-tsv-L100"></a>

## Encoding

SSSOM/TSV files MUST be encoded in UTF-8 ([RFC 3629](https://datatracker.ietf.org/doc/html/rfc3629#section-13)). They MUST NOT start with a byte order mark (U+FEFF). This applies to external metadata files as well, when the [external metadata mode](#spec-formats-tsv-L87) is used.



<a id="spec-formats-tsv-L105"></a>

## Identifiers

All identifiers in a SSSOM/TSV file, that is, all the values of slots typed as [EntityReference](../source/src/sssom_schema/schema/sssom_schema.yaml#L71-L79), MUST be serialised in [CURIE syntax](https://www.w3.org/TR/curie/). SSSOM/TSV parsers SHOULD reject files containing identifiers serialised as IRIs.

As stated in the description of the model ([Identifiers section](#spec-model-L26)), all prefix names used in CURIEs MUST be declared in the `curie_map` slot of the mapping set object, unless the prefix is a “built-in” prefix (in which case it MAY be omitted). SSSOM/TSV parsers MUST reject a file with undeclared, non-built-in prefix names.

A SSSOM/TSV writer SHOULD refuse to serialise a mapping set that contains IRIs that cannot be contracted into CURIEs because there is no suitable prefix declaration in its CURIE map. The use of a custom, ad-hoc logic to infer a possible prefix name where none has been provided (e.g., “if the IRI ends with a `ZZZ_NNNNNNN` pattern, turn it into a `ZZZ:NNNNNNN` CURIE”) is strongly discouraged.



<a id="spec-formats-tsv-L114"></a>

## Propagatable slots

As [explained in another section](#spec-model-L35), some slots in the `MappingSet` class are intended, not to describe the mapping set itself, but to store values that are shared by all mappings in the set. These slots are called the “propagatable slots”, because their values should be “propagated” from the mapping set down to the individual mappings.


<a id="spec-formats-tsv-L118"></a>

### Propagation

“Propagation” is the operation of assigning to individual mappings in a set the values from the propagatable slots of the set. That operation SHOULD be performed by a SSSOM/TSV parser before passing the parsed objects to the application code.

For any given propagatable slot, propagation is only allowed if none of the individual mappings already have their own value in that slot. If any mapping (even only one mapping) has a value in that slot, then the slot MUST be considered as non-propagatable. Otherwise, a propagating SSSOM/TSV parser MUST (1) copy over the value of the propagatable slot on the `MappingSet` object to the corresponding slot of every individual `Mapping` objects, and (2) remove the propagated value from the `MappingSet` object.

Implementations that support propagation MUST also support condensation.


<a id="spec-formats-tsv-L126"></a>

### Condensation

“Condensation” is the opposite of “propagation”. It is the operation of assigning common values to the propagatable slots of the set, based on the values of these slots on individual mappings. That operation SHOULD be performed by a SSSOM/TSV writer prior to writing a set into a SSSOM/TSV file, but that behaviour, if available, MUST be deactivatable.

For any given propagatable slot, condensation is only allowed if (1) all mappings in the set have the same value, and (2) the mapping set does not already have a value in the slot, unless that value happens to be the same as the value in all mappings. If those two conditions are met, then a condensating SSSOM/TSV writer MUST (1) set the value of the slot on the `MappingSet` object to the common value of the slot in all mappings, and (2) remove the condensed value from the individual `Mapping` object.

Implementations that support condensation MUST also support propagation.



<a id="spec-formats-tsv-L135"></a>

## Non-standard slots

If an implementation does not support [non-standard slots](#spec-model-L129), then:

* a SSSOM/TSV reader MUST discard any unknown top-level YAML key in the metadata block, and any unknown TSV column in the TSV section;
* a SSSOM/TSV writer MUST NOT write any unknown top-level YAML key in the metadata block, or any unknown TSV column in the TSV section.


<a id="spec-formats-tsv-L142"></a>

### Support for defined extensions

This section applies to implementations that supports defined extensions.

A SSSOM/TSV reader MUST check the validity of the extension definitions listed in the `extension_definitions` slot in the YAML metadata block:

* definitions with no `slot_name`, or with a `slot_name` that is not a XML non-colonized name, MUST be ignored;
* definitions with any unexpected content (e.g. other keys than just `slot_name`, `property`, and `type_hint`) MUST be ignored;
* the `property` and `type_hint` values for a given definition, if present, MUST be CURIEs and MUST be resolvable using the mapping set’s `curie_map`, otherwise the definition MUST be ignored.

A SSSOM/TSV reader MUST, upon encountering a non-standard YAML key in the metadata block or an unknown TSV column, check that the name of the key or of the column matches the `slot_name` of one of the extension definitions listed in the mapping set’s `extension_definitions` slot. If there is no match, the non-standard slot MUST be discarded.

Upon encountering a non-standard slot whose corresponding definition has a `type_hint` of `https://w3id.org/linkml/Uriorcurie`, the reader SHOULD check that the value is a CURIE and is resolvable using the mapping set’s `curie_map`.



<a id="spec-formats-tsv-L157"></a>

## Compatibility with previous versions of the specification

Implementations MUST support the current version of the specification. However, SSSOM/TSV parsers MAY additionally accept to parse files that were compliant to a previous version. This section provides advice for implementations willing to support older versions.


<a id="spec-formats-tsv-L161"></a>

### Compatibility with pre-1.0 versions


<a id="spec-formats-tsv-L163"></a>

#### `match_type` slot

Initial versions of this specification defined a `match_type` slot on the `Mapping` class. The slot was intended to describe the kind of match that led to the mapping, and accepted values from a specific enumeration. In SSSOM 0.9.1, this slot was replaced by the `mapping_justification` slot, and the enumeration was replaced by terms from the [SEMAPV vocabulary](https://mapping-commons.github.io/semantic-mapping-vocabulary/).

Upon encountering a `match_type` slot, implementations supporting pre-1.0 versions MUST silently transform it into a `mapping_justification` slot and convert the enumeration values using the following table:

| `match_type` value | `mapping_justification` value |
| ------------------ | ----------------------------- |
| Lexical            | semapv:LexicalMatching        |
| Logical            | semapv:LogicalMatching        |
| HumanCurated       | semapv:ManualMappingCuration  |
| Complex            | semapv:CompositeMatching      |
| Unspecified        | semapv:UnspecifiedMatching    |
| SemanticSimilarity | semapv:SemanticSimilarityThresholdMatching |

Any other value in the `match_type` slot MUST be treated as an error.

If the set contains both `match_type` and `mapping_justification` slots, it is advised to simply ignore the former.



<a id="spec-formats-tsv-L183"></a>

#### `match_term_type` slot

Initial versions of this specification defined a `match_term_type` slot on the `Mapping` class. The slot was intended to describe what was being matched. In SSSOM 0.9.1, this slot was replaced by two distinct slots called `subject_type` and `object_type` (this notably allowed for the case where the subject and the object are of a different type, something the `match_term_type` slot did not support).

Upon encountering a `match_term_type` slot, implementations supporting pre-1.0 versions MUST silently transform it into a pair of `subject_type` and `object_type` slots, both slots having the same value derived from the original value using the following table:

| `match_term_type` value | `subject_type` and `object_type` value |
| ----------------------- | -------------------------------------- |
| ConceptMatch            | skos concept                           |
| ClassMatch              | owl class                              |
| ObjectPropertyMatch     | owl object property                    |
| IndividualMatch         | owl named individual                   |
| DataPropertyMatch       | owl data property                      |
| TermMatch               | rdfs literal                           |

Any other value in the `match_term_type` slot MUST be treated as an error.

If the set already contains `subject_type` and `object_type` slots, any `match_term_type` slot can be silently ignored.


<a id="spec-formats-tsv-L202"></a>

#### semantic_similarity_score and semantic_similarity_measure

Initial versions of this specification defined a `semantic_similarity_score` slot to store the semantic similarity, and a `semantic_similarity_measure` slot to describe how the the semantic similarity is assessed. In SSSOM 1.0, those slots were replaced by more generic `similarity_score` and `similarity_measure` slots.

Upon encountering a `semantic_similarity_score` (respectively `semantic_similarity_measure`) slot, implementations supporting pre-1.0 versions MUST silently transform it into a `similarity_score` (respectively `similarity_measure`) slot. No changes on the value of the slot are required.


<a id="spec-formats-tsv-L208"></a>

## Canonical SSSOM/TSV format

This section defines a “canonical” variant of the SSSOM/TSV format, which has stricter serialisation rules. The purpose of the canonical SSSOM/TSV format is to minimise differences across SSSOM/TSV files that would be induced by small diverging behaviours between different SSSOM/TSV implementations.

The rules in this section apply to SSSOM/TSV writers only. SSSOM/TSV writers SHOULD write files in the canonical format, but SSSOM/TSV readers MUST NOT reject a file solely because it does not follow the canonical rules.


<a id="spec-formats-tsv-L214"></a>

### General rules

A canonical SSSOM/TSV writer:

* MUST use line breaks made of only the U+000A character (no U+000D, and no U+000D + U+000A sequences);
* MUST condense the slots whenever possible, as described in the [Condensation](#spec-formats-tsv-L126) section.



<a id="spec-formats-tsv-L222"></a>

### Rules for the metadata block

When writing the metadata block, a canonical SSSOM/TSV writer:

* MUST embed the metadata block in the same file as the TSV section (no external metadata);
* MUST NOT insert additional space characters between the initial `#` character and the YAML content;
* MUST serialise multi-valued slots as YAML “block sequences” ([YAML Specification §8.2.1](https://yaml.org/spec/1.2.2/#821-block-sequences)) – even when the list of values contains only one item;
* MUST serialise scalar values in YAML “plain style” ([YAML Specification §7.3.3](https://yaml.org/spec/1.2.2/#733-plain-style)) whenever possible, otherwise in “double-quoted style” ([YAML Specification §7.3.1](https://yaml.org/spec/1.2.2/#731-double-quoted-style));
* MUST serialise the slots in the order they appear in the [“Slots” table](../source/rendered/1.0/MappingSet.html#slots), in the documentation for the `MappingSet` class;
* MUST NOT include in the CURIE map the prefix names that are considered “built-in”;
* MUST NOT include in the CURIE map any prefix name that is not used anywhere in the set;
* MUST sort the prefix names in the CURIE map in lexicographical order.

In addition, if [extension slots](#spec-model-L129) are supported, the writer:

* MUST write any extension slot in the mapping set _after_ the standard slots;
* MUST sort the extension slots lexicographically on the `property` of their corresponding extension definitions;
* MUST sort extension definitions on their `property` value;
* MUST not include an extension definition if the corresponding extension is not used anywhere in the set.



<a id="spec-formats-tsv-L243"></a>

### Rules for the mappings block

When writing the mappings block, a canonical SSSOM/TSV writer:

* MUST quote values only when needed, as per the rules in the [Quoting](#spec-formats-tsv-L76) section;
* MUST serialise floating point values with up to three digits as needed after the decimal point, rounding the last digit to the nearest neighbour (rounding up if both neighbours are equidistant);
* MUST write the columns in the order the slots appear in the [“Slots” table](../source/rendered/1.0/Mapping.html#slots), in the documentation for the `Mapping` class;
* MUST sort the mappings in lexicographical order on all their slots, in the order the slots appear in the [“Slots” table](../source/rendered/1.0/Mapping.html#slots).

In addition, if [extension slots](#spec-model-L129) are supported, the writer:

* MUST write any non-standard column _after_ the standard columns;
* MUST sort the non-standard column lexicographically on the `property` of their corresponding extension definitions.



<a id="spec-formats-tsv-L258"></a>

## Examples

This section is _non-normative_.

A SSSOM/TSV file in embedded metadata mode:

```
#curie_map:
#  FOODON: http://purl.obolibrary.org/obo/FOODON_
#  KF_FOOD: https://kewl-foodie.inc/food/
#  orcid: https://orcid.org/
#mapping_set_id: https://w3id.org/sssom/tutorial/example1.sssom.tsv
#mapping_set_description: Manually curated alignment of KEWL FOODIE INC internal food and nutrition database with Food Ontology (FOODON). Intended to be used for ontological analysis and grouping of KEWL FOODIE INC related data.
#license: https://creativecommons.org/licenses/by/4.0/
#mapping_date: 2022-05-02
subject_id	subject_label	predicate_id	object_id	object_label	mapping_justification	author_id	confidence	comment
KF_FOOD:F001	apple	skos:exactMatch	FOODON:00002473	apple (whole)	semapv:ManualMappingCuration	orcid:0000-0002-7356-1779	0.95	"We could map to FOODON:03310788 instead to cover sliced apples, but only ""whole"" apple types exist."
KF_FOOD:F002	gala	skos:exactMatch	FOODON:00003348	Gala apple (whole)	semapv:ManualMappingCuration	orcid:0000-0002-7356-1779	1	
KF_FOOD:F003	pink	skos:exactMatch	FOODON:00004186	Pink apple (whole)	semapv:ManualMappingCuration	orcid:0000-0002-7356-1779	0.9	"We could map to FOODON:00004187 instead which more specifically refers to ""raw"" Pink apples. Decided against to be consistent with other mapping choices."
KF_FOOD:F004	braeburn	skos:broadMatch	FOODON:00002473	apple (whole)	semapv:ManualMappingCuration	orcid:0000-0002-7356-1779	1	
```

The same set in external metadata mode: first the file containing the metadata block:

```yaml
curie_map:
  FOODON: http://purl.obolibrary.org/obo/FOODON_
  KF_FOOD: https://kewl-foodie.inc/food/
  orcid: https://orcid.org/
mapping_set_id: https://w3id.org/sssom/tutorial/example1.sssom.tsv
mapping_set_description: Manually curated alignment of KEWL FOODIE INC internal food and nutrition database with Food Ontology (FOODON). Intended to be used for ontological analysis and grouping of KEWL FOODIE INC related data.
license: https://creativecommons.org/licenses/by/4.0/
mapping_date: 2022-05-02
```

then the file containing the mappings block:

```
subject_id	subject_label	predicate_id	object_id	object_label	mapping_justification	author_id	confidence	comment
KF_FOOD:F001	apple	skos:exactMatch	FOODON:00002473	apple (whole)	semapv:ManualMappingCuration	orcid:0000-0002-7356-1779	0.95	"We could map to FOODON:03310788 instead to cover sliced apples, but only ""whole"" apple types exist."
KF_FOOD:F002	gala	skos:exactMatch	FOODON:00003348	Gala apple (whole)	semapv:ManualMappingCuration	orcid:0000-0002-7356-1779	1	
KF_FOOD:F003	pink	skos:exactMatch	FOODON:00004186	Pink apple (whole)	semapv:ManualMappingCuration	orcid:0000-0002-7356-1779	0.9	"We could map to FOODON:00004187 instead which more specifically refers to ""raw"" Pink apples. Decided against to be consistent with other mapping choices."
KF_FOOD:F004	braeburn	skos:broadMatch	FOODON:00002473	apple (whole)	semapv:ManualMappingCuration	orcid:0000-0002-7356-1779	1	
```


<a id="spec-formats-tsv-L303"></a>

### Invalid examples

Illegal case 1: the metadata block cannot contains comments that are not part of the metadata.

```
# This is a comment that does not belong here.
#curie_map:
#  HP: "http://purl.obolibrary.org/obo/HP_"
#  MP: "http://purl.obolibrary.org/obo/MP_"
#  orcid: "https://orcid.org/"
# This is another comment that also does not belong here.
#creator_id:
#  - "orcid:0000-0002-7356-1779"
```

Illegal case 2: there should be no empty lines.

```
#curie_map:
#  HP: "http://purl.obolibrary.org/obo/HP_"
#  MP: "http://purl.obolibrary.org/obo/MP_"
#  orcid: "https://orcid.org/"

#creator_id:
#  - "orcid:0000-0002-7356-1779"
```

Original MD: [spec-formats-owl.md](../source/src/docs/spec-formats-owl.md#L1-L99).

<a id="spec-formats-owl-L1"></a>

# The OWL/RDF serialisation format

This section defines a way to serialise SSSOM mappings as _reified OWL axioms_. This has the advantage that any mapping set can be simply merged with an ontology in the usual way, for example using [ROBOT merge](https://robot.obolibrary.org/merge).

The OWL/RDF serialisation rules deal with three types of reified OWL axioms, and a few sub-types:

1. Predicate is an annotation property
2. Predicate is an object property and
   1. Object/Subject are classes
   2. Object/Subject are individuals
3. Predicate is language relational construct of RDFS or OWL (`rdfs:subClassOf`, `owl:equivalentClass`)


<a id="spec-formats-owl-L13"></a>

## Predicate is an annotation property:

If the predicate corresponds to an annotation property, the mapping `<S,P,O, meta>` gets converted to an OWLAnnotationAssertion axiom: `OWLAnnotationAssertion(P,S,O)`. All mapping level metadata (`meta`) gets converted into OWLAnnotation objects which are materialised as axiom annotations on the mapping annotation assertion, see [OWL 2 Structural Specification](https://www.w3.org/TR/owl2-syntax/#Annotations):

```
AnnotationAssertion(meta P, S, O)
```

Where `meta` is a sequence of OWL Annotations objects like:

```
Annotation(Q1,V1) Annotation(Q2,V2) ... Annotation(Qn,Vn)
```

where `Qi` is a SSSOM metadata slot and `Vi` is an annotation value.

Note that if a SSSOM metadata element value is a list `L` (i.e. can have multiple elements, such as creator and others), individual annotations are created for each of them:

```
Annotation(Q,V) for all V in L.
```

Example:

```
AnnotationAssertion(Annotation(sssom:creator_id <https://orcid.org/0000-0002-7356-1779>) Annotation(sssom:mapping_justification semapv:LexicalMatching) skos:exactMatch <http://purl.obolibrary.org/obo/HP_0009894> <http://purl.obolibrary.org/obo/MP_0000019>)
```

Mapping set level annotations are manifested as Ontology annotation in the usual way, according to the [OWL 2 Structural Specification](https://www.w3.org/TR/owl2-syntax/#Annotations).


<a id="spec-formats-owl-L43"></a>

## Predicate is an object property


<a id="spec-formats-owl-L45"></a>

### Case 1: Object and Subject are classes.

The mapping `<S,P,O>` gets translated into an existential restriction:

```
SubclassOf(S, P some O)
```

All metadata slots are added as OWLAnnotation objects and added to SubclassOf axiom as axiom annotations:

```
SubclassOf(meta, S, P some O)
```

Example:

```
SubClassOf(Annotation(sssom:creator_id <https://orcid.org/0000-0002-7356-1779>) Annotation(sssom:mapping_justification semapv:LexicalMatching) <http://example.org/AA> ObjectSomeValuesFrom(<http://example.org/x> <http://example.org/BB>))
```


<a id="spec-formats-owl-L65"></a>

### Case 2: Object and Subject are individuals

The mapping `<S,P,O>` gets translated into an object property assertion:

```
ObjectPropertyAssertion(P, S, O)
```

All metadata slots are added as OWLAnnotation objects and added to ObjectPropertyAssertion axiom as axiom annotations:

```
ObjectPropertyAssertion(meta, P, S, O)
```

Example:

```
ObjectPropertyAssertion(Annotation(sssom:creator_id <https://orcid.org/0000-0002-7356-1779>) Annotation(sssom:mapping_justification semapv:LexicalMatching) <http://www.example.org/x> <http://www.example.org/a> <http://www.example.org/b>)
```



<a id="spec-formats-owl-L86"></a>

### Predicate is language relational construct of RDFS or OWL

The mapping `<S,P,O, meta>` gets translated into an annotated axiom using the following table:

| Mapping predicate   | Generated axiom             |
| ------------------- | --------------------------- |
| owl:equivalentClass | EauivalentClass(meta, S, O) |
| rdfs:subClassOf     | SubClassOf(meta, S, O)      |

Example:

```
SubClassOf(Annotation(sssom:creator_id <https://orcid.org/0000-0002-7356-1779>) Annotation(sssom:mapping_justification semapv:LexicalMatching) <http://www.example.org/a> <http://www.example.org/b>)
```

Original MD: [spec-formats-json.md](../source/src/docs/spec-formats-json.md#L1-L5).

<a id="spec-formats-json-L1"></a>

# The JSON serialisation format

The JSON serialisation format is currently unspecified.

It is intended as a more-or-less direct serialisation of the `MappingSet` class into the JSON format as specified by [RFC 8259](https://datatracker.ietf.org/doc/html/rfc8259), but many details of the serialisation are left unspecified for now.

Original YAML: [sssom_schema.yaml](../source/src/sssom_schema/schema/sssom_schema.yaml#L1-L792).

<a id="sssom_schema-L1"></a>

## Native YAML schema (collector display, not upstream Markdown)

```yaml
id: https://w3id.org/sssom/schema/
name: sssom
description: Datamodel for Simple Standard for Sharing Ontological Mappings (SSSOM)
imports:
- linkml:types
prefixes:
  dcterms: http://purl.org/dc/terms/
  linkml: https://w3id.org/linkml/
  sssom: https://w3id.org/sssom/
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
  oboInOwl: http://www.geneontology.org/formats/oboInOwl#
  pav: http://purl.org/pav/
  prov: http://www.w3.org/ns/prov#
  skos: http://www.w3.org/2004/02/skos/core#
  xsd: http://www.w3.org/2001/XMLSchema#
  semapv: https://w3id.org/semapv/vocab/
see_also:
- https://github.com/mapping-commons/sssom
- https://mapping-commons.github.io/sssom/home/
default_curi_maps:
- semweb_context
- obo_context
default_prefix: sssom
default_range: string

enums:
  entity_type_enum:
    permissible_values:
      owl class:
        meaning: owl:Class
      owl object property:
        meaning: owl:ObjectProperty
      owl data property:
        meaning: owl:DataProperty
      owl annotation property:
        meaning: owl:AnnotationProperty
      owl named individual:
        meaning: owl:NamedIndividual
      skos concept:
        meaning: skos:Concept
      rdfs resource:
        meaning: rdfs:Resource
      rdfs class:
        meaning: rdfs:Class
      rdfs literal:
        meaning: rdfs:Literal
        description: This value indicate that the entity being mapped is not a semantic entity with a distinct identifier, but is instead represented entirely by its literal label. This value MUST NOT be used in the predicate_type slot.
        see_also:
        - https://mapping-commons.github.io/sssom/spec-model/#literal-mappings
        - https://github.com/mapping-commons/sssom/issues/234
        - https://github.com/mapping-commons/sssom/blob/master/examples/schema/literals.sssom.tsv
      rdfs datatype:
        meaning: rdfs:Datatype
      rdf property:
        meaning: rdf:Property
        
  predicate_modifier_enum:
    permissible_values:
      Not: Negating the mapping predicate. The meaning of the triple becomes subject_id is not a predicate_id match to object_id.
  mapping_cardinality_enum:
    permissible_values:
      "1:1": One-to-one mapping
      "1:n": One-to-many mapping
      "n:1": Many-to-one mapping
      "1:0": One-to-none mapping
      "0:1": None-to-one mapping
      "n:n": Many-to-many mapping

types:
 EntityReference:
    typeof: uriorcurie
    description: |
      A reference to an entity involved in the mapping.
    base: str
    uri: rdfs:Resource
    see_also:
      - https://mapping-commons.github.io/sssom/spec/#tsv

slots:
  prefix_name:
    key: true
    range: ncname
  prefix_url:
    range: uri
  curie_map:
    description: A dictionary that contains prefixes as keys and their URI expansions as values.
    range: prefix
    multivalued: true
    inlined: true
    see_also:
      - https://github.com/mapping-commons/sssom/issues/225
      - https://github.com/mapping-commons/sssom/pull/349
      - https://github.com/mapping-commons/sssom/blob/master/examples/schema/curie_map.sssom.tsv
  mirror_from:
    description: A URL location from which to obtain a resource, such as a mapping set.
    range: uri
  registry_confidence:
    description: This value is set by the registry that indexes the mapping set. It reflects the confidence the registry has in the correctness of the mappings in the mapping set.
    range: double
  last_updated:
    description: The date this reference was last updated.
    range: date
  local_name:
    description: The local name assigned to file that corresponds to the downloaded mapping set.
    range: string
  mapping_set_references:
    description: A list of mapping set references.
    range: mapping set reference
    multivalued: true
    recommended: true
  mapping_registry_id:
    description: The unique identifier of a mapping registry.
    range: EntityReference
    required: true
  mapping_registry_title:
    description: The title of a mapping registry.
    range: string
  mapping_registry_description:
    description: The description of a mapping registry.
    range: string
  imports:
    description: A list of registries that should be imported into this one.
    multivalued: true
    range: uri
  documentation:
    description: A URL to the documentation of this mapping commons.
    range: uri
  homepage:
    description: A URL to a homepage of this mapping commons.
    range: uri
  mappings:
    description: Contains a list of mapping objects
    range: mapping
    multivalued: true
    inlined_as_list: true
    recommended: true
  subject_id:
    description: The ID of the subject of the mapping.
    range: EntityReference
    mappings:
    - owl:annotatedSource
    slot_uri: owl:annotatedSource
    examples:
      - value: HP:0009894
        description: The CURIE denoting the Human Phenotype Ontology concept of 'Thickened ears'
  subject_label:
    description: The label of subject of the mapping
    range: string
    examples:
      - value: Thickened ears
    recommended: true
  subject_category:
    description: The conceptual category to which the subject belongs to. This can
      be a string denoting the category or a term from a controlled vocabulary.
      This slot is deliberately underspecified. Conceptual categories can range from
      those that are found in general upper ontologies such as BFO (e.g. process, temporal region, etc) to those that serve
      as upper ontologies in specific domains, such as COB or BioLink (e.g. gene, disease, chemical entity). The purpose of this
      optional field is documentation for human reviewers - when a category is known
      and documented clearly, the cost of interpreting and evaluating the mapping decreases.
    range: string
    see_also:
      - https://github.com/mapping-commons/sssom/issues/13
      - https://github.com/mapping-commons/sssom/issues/256
    examples:
      - value: UBERON:0001062
        description: (The CURIE of the Uberon term for "anatomical entity".)
      - value: anatomical entity
        description: (A string, rather than ID, describing the "anatomical entity" category. This is possible, but less preferred than using an ID.)
      - value: biolink:Gene
        description: (The CURIE of the biolink class for genes.)
  subject_type:
    description: The type of entity that is being mapped.
    range: entity_type_enum
    instantiates: sssom:Propagatable
    annotations:
      propagated: true
    examples:
      - value: owl:Class
  predicate_id:
    description: The ID of the predicate or relation that relates the subject and
      object of this match.
    mappings:
    - owl:annotatedProperty
    range: EntityReference
    required: true
    slot_uri: owl:annotatedProperty
    
    examples:
      - value: owl:sameAs
        description: The subject and the object are instances (owl individuals), and the two instances are the same.
      - value: owl:equivalentClass
        description: The subject and the object are classes (owl class), and the two classes are the same.
      - value: owl:equivalentProperty
        description: The subject and the object are properties (owl object, data, annotation properties), and the two properties are the same.
      - value: rdfs:subClassOf
        description: The subject and the object are classes (owl class), and the subject is a subclass of the object.
      - value: rdfs:subPropertyOf
        description: The subject and the object are properties (owl object, data, annotation properties), and the subject is a subproperty of the object.
      - value: skos:relatedMatch
        description: The subject and the object are associated in some unspecified way.
      - value: skos:closeMatch
        description: The subject and the object are sufficiently similar that they can be used interchangeably in some information retrieval applications.
      - value: skos:exactMatch
        description: The subject and the object can, with a high degree of confidence, be used interchangeably across a wide range of information retrieval applications.
      - value: skos:narrowMatch
        description: "From the SKOS primer: A triple skos:narrower (and skos:narrowMatch) asserts that , the object of the triple, is a narrower concept than , the subject of the triple."
      - value: skos:broadMatch
        description: "From the SKOS primer: A triple skos:broader (and skos:broadMatch) asserts that , the object of the triple, is a broader concept than , the subject of the triple."
      - value: oboInOwl:hasDbXref
        description: Two terms are related in some way. The meaning is frequently consistent across a single set of mappings. Note this property is often overloaded even where the terms are of a different nature (e.g. interpro2go)
      - value: rdfs:seeAlso
        description: The subject and the object are associated in some unspecified way. The object IRI often resolves to a resource on the web that provides additional information.
  predicate_modifier:
    description: A modifier for negating the predicate. See https://github.com/mapping-commons/sssom/issues/40 for discussion
    range: predicate_modifier_enum
    see_also:
      - https://github.com/mapping-commons/sssom/issues/107
    examples:
      - value: Not
        description: Negates the predicate, see documentation of predicate_modifier_enum
  predicate_label:
    description: The label of the predicate/relation of the mapping
    range: string
    examples:
      - value: has cross-reference
        description: The label of the oboInOwl:hasDbXref property to represent cross-references.
  predicate_type:
    description: The type of entity that is being mapped.
    range: entity_type_enum
    examples:
      - value: owl:AnnotationProperty
      - value: owl:ObjectProperty
  object_id:
    description: The ID of the object of the mapping.
    mappings:
    - owl:annotatedTarget
    range: EntityReference
    slot_uri: owl:annotatedTarget
    examples:
      - value: HP:0009894
        description: The CURIE denoting the Human Phenotype Ontology concept of 'Thickened ears'
  object_label:
    description: The label of object of the mapping
    range: string
    examples:
      - value: Thickened ears
    recommended: true
  object_category:
    description: The conceptual category to which the subject belongs to. This can
      be a string denoting the category or a term from a controlled vocabulary.
      This slot is deliberately underspecified. Conceptual categories can range from
      those that are found in general upper ontologies such as BFO (e.g. process, temporal region, etc) to those that serve
      as upper ontologies in specific domains, such as COB or BioLink (e.g. gene, disease, chemical entity). The purpose of this
      optional field is documentation for human reviewers - when a category is known
      and documented clearly, the cost of interpreting and evaluating the mapping decreases.
    range: string
    see_also:
      - https://github.com/mapping-commons/sssom/issues/13
      - https://github.com/mapping-commons/sssom/issues/256
    examples:
      - value: UBERON:0001062
        description: (The CURIE of the Uberon term for "anatomical entity".)
      - value: anatomical entity
        description: (A string, rather than ID, describing the "anatomical entity" category. This is possible, but less preferred than using an ID.)
      - value: biolink:Gene
        description: (The CURIE of the biolink class for genes.)
  mapping_justification:
    description: A mapping justification is an action (or the written representation of that action) of showing a mapping to be right or reasonable.
    range: EntityReference
    pattern: "^semapv:(MappingReview|ManualMappingCuration|LogicalReasoning|LexicalMatching|CompositeMatching|UnspecifiedMatching|SemanticSimilarityThresholdMatching|LexicalSimilarityThresholdMatching|MappingChaining)$"
    required: true
    any_of:
      - equals_string: semapv:LexicalMatching
      - equals_string: semapv:LogicalReasoning
      - equals_string: semapv:CompositeMatching
      - equals_string: semapv:UnspecifiedMatching
      - equals_string: semapv:SemanticSimilarityThresholdMatching
      - equals_string: semapv:LexicalSimilarityThresholdMatching
      - equals_string: semapv:MappingChaining
      - equals_string: semapv:MappingReview
      - equals_string: semapv:ManualMappingCuration
    examples:
      - value: semapv:LexicalMatching
      - value: semapv:ManualMappingCuration
  object_type:
    description: The type of entity that is being mapped.
    range: entity_type_enum
    instantiates: sssom:Propagatable
    annotations:
      propagated: true
    examples:
      - value: owl:Class
  mapping_set_id:
    description: A globally unique identifier for the mapping set (not each individual
      mapping). Should be IRI, ideally resolvable.
    required: true
    range: uri
    examples:
      - value: http://purl.obolibrary.org/obo/mondo/mappings/mondo_exactmatch_ncit.sssom.tsv
        description: (A persistent URI pointing to the latest version of the Mondo - NCIT mapping in the Mondo namespace.)
  mapping_set_version:
    description: A version string for the mapping.
    range: string
    slot_uri: owl:versionInfo
    examples:
      - value: "2020-01-01"
        description: (A date-based version that indicates that the mapping was published on the 1st January in 2021.)
      - value: "1.2.1"
        description: "(A semantic version tag that indicates that this is the 1st major, 2nd minor version, patch 1 (https://semver.org/).)"
  mapping_set_group:
    description: Set by the owners of the mapping registry. A way to group .
    range: string
  mapping_set_title:
    description: The display name of a mapping set.
    range: string
    slot_uri: dcterms:title
    examples:
      - value: "The Mondo-OMIM mappings by Monarch Initiative."
  mapping_set_description:
    description: A description of the mapping set.
    range: string
    slot_uri: dcterms:description
    examples:
      - value: "This mapping set was produced to integrate human and mouse phenotype data at the IMPC. It is primarily used for making mouse phenotypes searchable by human synonyms at https://mousephenotype.org/."
  creator_id:
    description: Identifies the persons or groups responsible for the creation of
      the mapping. The creator is the agent that put the mapping in its published form, 
      which may be different from the author, which is a person that was actively involved
      in the assertion of the mapping.
      Recommended to be a list of ORCIDs or otherwise
      identifying URIs.
    slot_uri: dcterms:creator
    range: EntityReference
    multivalued: true
  creator_label:
    description: A string identifying the creator of this mapping. In the spirit of
      provenance, consider using creator_id instead.
    range: string
    multivalued: true
  author_id:
    description: Identifies the persons or groups responsible for asserting the mappings.
      Recommended to be a list of ORCIDs or otherwise
      identifying URIs.
    slot_uri: pav:authoredBy
    range: EntityReference
    multivalued: true
  author_label:
    description: A string identifying the author of this mapping. In the spirit of
      provenance, consider using author_id instead.
    range: string
    multivalued: true
  reviewer_id:
    description: Identifies the persons or groups that reviewed and confirmed the mapping.
      Recommended to be a list of ORCIDs or otherwise
      identifying URIs.
    range: EntityReference
    multivalued: true
  reviewer_label:
    description: A string identifying the reviewer of this mapping. In the spirit of
      provenance, consider using reviewer_id instead.
    range: string
    multivalued: true
  license:
    description: A url to the license of the mapping. In absence of a license we assume
      no license.
    range: uri
    slot_uri: dcterms:license
  subject_source:
    description: URI of vocabulary or identifier source for the subject.
    range: EntityReference
    instantiates: sssom:Propagatable
    annotations:
      propagated: true
    examples:
      - value: obo:mondo.owl
        description: A persistent OBO CURIE pointing to the latest version of the Mondo ontology.
      - value: wikidata:Q7876491
        description: A Wikidata identifier for the Uberon ontology resource.
  subject_source_version:
    description: Version IRI or version string of the source of the subject term.
    range: string
    instantiates: sssom:Propagatable
    annotations:
      propagated: true
    examples:
      - value: http://purl.obolibrary.org/obo/mondo/releases/2021-01-30/mondo.owl
        description: (A persistent Version IRI pointing to the Mondo version '2021-01-30')
  object_source:
    description: URI of vocabulary or identifier source for the object.
    range: EntityReference
    instantiates: sssom:Propagatable
    annotations:
      propagated: true
    examples:
      - value: obo:mondo.owl
        description: A persistent OBO CURIE pointing to the latest version of the Mondo ontology.
      - value: wikidata:Q7876491
        description: A Wikidata identifier for the Uberon ontology resource.
  object_source_version:
    description: Version IRI or version string of the source of the object term.
    range: string
    instantiates: sssom:Propagatable
    annotations:
      propagated: true
    examples:
      - value: http://purl.obolibrary.org/obo/mondo/releases/2021-01-30/mondo.owl
        description: (A persistent Version IRI pointing to the Mondo version '2021-01-30')
  mapping_provider:
    description: URL pointing to the source that provided the mapping, for example
      an ontology that already contains the mappings, or a database from which it was derived.
    range: uri
    instantiates: sssom:Propagatable
    annotations:
      propagated: true
  mapping_set_source:
    description: A mapping set or set of mapping set that was used to derive the mapping set.
    slot_uri: prov:wasDerivedFrom
    range: uri
    multivalued: true
    examples:
      - value: http://purl.obolibrary.org/obo/mondo/mappings/2022-05-20/mondo_exactmatch_ncit.sssom.tsv
        description: A persistent, ideally versioned, link to the mapping set from which the current mapping set is derived.
  mapping_source:
    description: The mapping set this mapping was originally defined in. mapping_source is used for example when merging multiple
      mapping sets or deriving one mapping set from another.
    range: EntityReference
    examples:
      - value: MONDO_MAPPINGS:mondo_exactmatch_ncit.sssom.tsv
  mapping_cardinality:
    description: A string indicating whether this mapping is from a 1:1 (the subject_id
      maps to a single object_id), 1:n (the subject maps to more than one object_id), 
      n:1, 1:0, 0:1 or n:n group. Note that this is a convenience field that should be derivable 
      from the mapping set.
    range: mapping_cardinality_enum
  mapping_tool:
    description: A reference to the tool or algorithm that was used to generate the
      mapping. Should be a URL pointing to more info about it, but can be free text.
    range: string
    instantiates: sssom:Propagatable
    annotations:
      propagated: true
    examples:
      - value: https://github.com/AgreementMakerLight/AML-Project
  mapping_tool_version:
    description: Version string that denotes the version of the mapping tool used.
    range: string
    instantiates: sssom:Propagatable
    annotations:
      propagated: true
    examples:
      - value: v3.2
  mapping_date:
    description: The date the mapping was asserted. This is different from the date the mapping was published or compiled in a SSSOM file.
    slot_uri: pav:authoredOn
    range: date
    instantiates: sssom:Propagatable
    annotations:
      propagated: true
  publication_date:
    description: The date the mapping was published. This is different from the date the mapping was asserted.
    slot_uri: dcterms:created
    range: date
  confidence:
    description: A score between 0 and 1 to denote the confidence or probability that
      the match is correct, where 1 denotes total confidence.
    range: double
    minimum_value: 0.0
    maximum_value: 1.0
  subject_match_field:
    description: A list of properties (term annotations on the subject) that was used
      for the match.
    range: EntityReference
    multivalued: true
    instantiates: sssom:Propagatable
    annotations:
      propagated: true
  object_match_field:
    description: A list of properties (term annotations on the object) that was used
      for the match.
    range: EntityReference
    multivalued: true
    instantiates: sssom:Propagatable
    annotations:
      propagated: true
  match_string:
    description: String that is shared by subj/obj. It is recommended to indicate the 
      fields for the match using the object and subject_match_field slots.
    range: string
    multivalued: true
  subject_preprocessing:
    description: Method of preprocessing applied to the fields of the subject. 
      If different preprocessing steps were performed on different fields, it is
      recommended to store the match in separate rows.
    range: EntityReference
    multivalued: true
    instantiates: sssom:Propagatable
    annotations:
      propagated: true
    examples:
      - value: semapv:Stemming
      - value: semapv:StopWordRemoval
  object_preprocessing:
    description: Method of preprocessing applied to the fields of the object. 
      If different preprocessing steps were performed on different fields, it is
      recommended to store the match in separate rows.
    range: EntityReference
    multivalued: true
    instantiates: sssom:Propagatable
    annotations:
      propagated: true
    examples:
      - value: semapv:Stemming
      - value: semapv:StopWordRemoval
  curation_rule:
    description: A curation rule is a (potentially) complex condition executed by an agent that led to the establishment of a mapping. 
      Curation rules often involve complex domain-specific considerations, which are hard to capture in an automated fashion. The curation
      rule is captured as a resource rather than a string, which enables higher levels of transparency and sharing across mapping sets.
      The URI representation of the curation rule is expected to be a resolvable identifier which provides details about the nature of the curation rule.
    range: EntityReference
    multivalued: true
    see_also: 
      - https://github.com/mapping-commons/sssom/issues/166
      - https://github.com/mapping-commons/sssom/pull/258
      - https://github.com/mapping-commons/sssom/blob/master/examples/schema/curation_rule.sssom.tsv
  curation_rule_text:
    description: A curation rule is a (potentially) complex condition executed by an agent that led to the establishment of a mapping. 
      Curation rules often involve complex domain-specific considerations, which are hard to capture in an automated fashion. The curation
      rule should be captured as a resource (entity reference) rather than a string (see curation_rule element), which enables higher levels of transparency and sharing across mapping sets.
      The textual representation of curation rule is intended to be used in cases where (1) the creation of a resource is not practical from the
      perspective of the mapping_provider and (2) as an additional piece of metadata to augment the curation_rule element with a human readable text.
    range: string
    multivalued: true
    see_also:
      - https://github.com/mapping-commons/sssom/issues/166
      - https://github.com/mapping-commons/sssom/pull/258
      - https://github.com/mapping-commons/sssom/blob/master/examples/schema/curation_rule_text.sssom.tsv
  similarity_score:
    description: A score between 0 and 1 to denote the similarity between two entities, where
      1 denotes equivalence, and 0 denotes disjointness. The score is meant to be used in conjunction 
      with the similarity_measure field, to document, for example, the lexical or semantic match
      of a matching algorithm.
    range: double
    minimum_value: 0.0
    maximum_value: 1.0
    see_also:
      - https://github.com/mapping-commons/sssom/issues/385
      - https://github.com/mapping-commons/sssom/pull/386
      - https://github.com/mapping-commons/sssom/blob/master/examples/schema/similarity_score.sssom.tsv
  similarity_measure:
    description: The measure used for computing a similarity score.
      This field is meant to be used in conjunction with the similarity_score field, to document,
      for example, the lexical or semantic match of a matching algorithm.
      To make processing this field as unambiguous as possible, we recommend using 
      wikidata CURIEs, but the type of this field is deliberately unspecified.
    range: string
    examples:
      - value: https://www.wikidata.org/entity/Q865360
        description: (the Wikidata IRI for the Jaccard index measure).
      - value: wikidata:Q865360
        description: (the Wikidata CURIE for the Jaccard index measure).
      - value: Levenshtein distance
        description: (a score to measure the distance between two character sequences).
    see_also:
      - https://github.com/mapping-commons/sssom/issues/385
      - https://github.com/mapping-commons/sssom/pull/386
      - https://github.com/mapping-commons/sssom/blob/master/examples/schema/similarity_score.sssom.tsv
  issue_tracker_item:
    description: The issue tracker item discussing this mapping.
    range: EntityReference
    examples:
      - value: SSSOM_GITHUB_ISSUE:166
        description: (A URL resolving to an issue discussing a new SSSOM element request)
    see_also: 
      - https://github.com/mapping-commons/sssom/issues/78
      - https://github.com/mapping-commons/sssom/pull/259
      - https://github.com/mapping-commons/sssom/blob/master/examples/schema/issue_tracker_item.sssom.tsv
  issue_tracker:
    description: A URL location of the issue tracker for this entity.
    range: uri
    examples:
      - value: https://github.com/mapping-commons/mh_mapping_initiative/issues
        description: (A URL resolving to the issue tracker of the Mouse-Human mapping initiative)
    see_also: 
      - https://github.com/mapping-commons/sssom/issues/78
      - https://github.com/mapping-commons/sssom/pull/259
      - https://github.com/mapping-commons/sssom/blob/master/examples/schema/issue_tracker.sssom.tsv
  see_also:
    description: A URL specific for the mapping instance. E.g. for kboom we have a
      per-mapping image that shows surrounding axioms that drive probability. Could
      also be a github issue URL that discussed a complicated alignment
    slot_uri: rdfs:seeAlso
    range: string
    multivalued: true
  other:
    description: Pipe separated list of key value pairs for properties not part of
      the SSSOM spec. Can be used to encode additional provenance data.
    range: string
  comment:
    description: Free text field containing either curator notes or text generated
      by tool providing additional informative information.
    slot_uri: rdfs:comment
    range: string
  extension_definitions:
    description: A list that defines the extension slots used in the mapping set.
    range: extension definition
    multivalued: true
    see_also:
      - https://github.com/mapping-commons/sssom/issues/328
      - https://github.com/mapping-commons/sssom/blob/master/examples/schema/extension-slots.sssom.tsv
classes:
  mapping set:
    description: Represents a set of mappings
    slot_usage:
      license:
        required: true
    slots:
    - curie_map
    - mappings
    - mapping_set_id
    - mapping_set_version
    - mapping_set_source
    - mapping_set_title
    - mapping_set_description
    - creator_id
    - creator_label
    - license
    - subject_type
    - subject_source
    - subject_source_version
    - object_type
    - object_source
    - object_source_version
    - mapping_provider
    - mapping_tool
    - mapping_tool_version
    - mapping_date
    - publication_date
    - subject_match_field
    - object_match_field
    - subject_preprocessing
    - object_preprocessing
    - see_also
    - issue_tracker
    - other
    - comment
    - extension_definitions
  mapping:
    description: Represents an individual mapping between a pair of entities
    slots:
    - subject_id
    - subject_label
    - subject_category
    - predicate_id
    - predicate_label
    - predicate_modifier
    - object_id
    - object_label
    - object_category
    - mapping_justification
    - author_id
    - author_label
    - reviewer_id
    - reviewer_label
    - creator_id
    - creator_label
    - license
    - subject_type
    - subject_source
    - subject_source_version
    - object_type
    - object_source
    - object_source_version
    - mapping_provider
    - mapping_source
    - mapping_cardinality
    - mapping_tool
    - mapping_tool_version
    - mapping_date
    - publication_date
    - confidence
    - curation_rule
    - curation_rule_text
    - subject_match_field
    - object_match_field
    - match_string
    - subject_preprocessing
    - object_preprocessing
    - similarity_score
    - similarity_measure
    - see_also
    - issue_tracker_item
    - other
    - comment
    class_uri: owl:Axiom
    rules:
      - preconditions:
          slot_conditions:
            subject_type: 
              equals_string: "rdfs literal"
        postconditions:
          slot_conditions:
            subject_label:
              required: true
      - preconditions:
          slot_conditions:
            subject_type:
              none_of:
                equals_string: "rdfs literal"
        postconditions:
          slot_conditions:
            subject_id:
              required: true
      - preconditions:
          slot_conditions:
            object_type: 
              equals_string: "rdfs literal"
        postconditions:
          slot_conditions:
            object_label:
              required: true
      - preconditions:
          slot_conditions:
            object_type:
              none_of:
                equals_string: "rdfs literal"
        postconditions:
          slot_conditions:
            object_id:
              required: true
  mapping registry:
    description: A registry for managing mapping sets. It holds a set of 
      mapping set references, and can import other registries.
    slots:
      - mapping_registry_id
      - mapping_registry_title
      - mapping_registry_description
      - imports
      - mapping_set_references
      - documentation
      - homepage
      - issue_tracker
  mapping set reference:
    description: A reference to a mapping set. It allows to augment mapping 
      set metadata from the perspective of the registry, for example, providing 
      confidence, or a local filename or a grouping.
    slots:
      - mapping_set_id
      - mirror_from
      - registry_confidence
      - mapping_set_group
      - last_updated
      - local_name
  prefix:
    slots:
      - prefix_name
      - prefix_url
  extension definition:
    description: A definition of an extension (non-standard) slot.
    attributes:
      slot_name:
        description: The name of the extension slot.
        range: ncname
        required: true
      property:
        description: The property associated with the extension slot. It is
          intended to provide a non-ambiguous meaning to the slot (contrary
          to the slot_name, which for brevity reasons may be ambiguous).
        range: uriorcurie
      type_hint:
        description: Expected type of the values of the extension slot.
        range: uriorcurie
  Propagatable:
    class_uri: sssom:Propagatable
    description: Metamodel extension class to describe slots whose value can be
      propagated down from the MappingSet class to the Mapping class.
    see_also:
      - https://github.com/mapping-commons/sssom/issues/305
    attributes:
      propagated:
        description: Indicates whether a slot can be propagated from a mapping
          down to individual mappings.
        range: boolean
  NoTermFound:
    class_uri: sssom:NoTermFound
    description: sssom:NoTermFound can be used in place of a subject_id or object_id
      when the corresponding entity could not be found. It SHOULD be used in conjuction with
      a corresponding subject_source or object_source to signify where the term was not found.
    see_also:
      - https://github.com/mapping-commons/sssom/issues/28
      - https://github.com/mapping-commons/sssom/blob/master/examples/schema/no_term_found.sssom.tsv

```


<!-- materialization-redistribution-notice -->
## Redistribution notice

SSSOM 1.0 specification, release v1.0.0; Mapping Commons / SSSOM contributors. Copyright (c) 2022, Nico Matentzoglu. BSD 3-Clause License; full copyright, conditions and disclaimer retained in NOTICE. Fixed upstream README Copying covers this distribution except sssom-banner.png, which is not included. No author endorsement is implied.

Changes: Seven official Markdown originals and authoritative schema YAML retained byte-identically. Collector assembly explicitly separates original files, retains schema as YAML and represents its complete text in a labelled YAML fence; only derived local link routing, source boundaries, selectors and attribution are added. Two versioned official class HTML snapshots retained as bounded Slots-order corroboration, not merged navigation or website runtime. No prose, tabs, code, invalid examples or upstream inconsistencies corrected; no OCR or LinkML execution.

Scope: Fixed commit 658de421c21a686f1213ff41879c9245ac0b4925: src/docs/spec-intro.md, spec-model.md, spec-formats.md, spec-formats-tsv.md, spec-formats-owl.md, spec-formats-json.md, chaining-rules.md, src/sssom_schema/schema/sssom_schema.yaml; provenance LICENSE/mkdocs.yml, plus official versioned 1.0 Mapping and MappingSet HTML snapshots for the normative Slots order; derived local assembly and selectors. Excludes banner, tutorials, mapping datasets, tools, other versions, external LinkML runtime/types and recursive references.

Full license and original rights links: [NOTICE.md](../NOTICE.md).

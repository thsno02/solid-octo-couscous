# Retained specification text (collector assembly)

> This consumer Markdown assembles the explicitly retained originals in declared order. Source labels, line anchors and local href rewrites are collector additions; HTML is represented as structural text with ordered table cells and preserved code, without running source scripts.

> Collector representation: declared cell spans are annotations, not an expanded table grid; code br line breaks and NBSP are retained, and image-label whitespace is normalized without dropping label words.

Original HTML: [specification.html](../source/specification.html#L1-L8264).

<a id="specification-L1"></a>
[](https://www.w3.org/)

<a id="specification-L1679"></a>
<a id="specification-title"></a>
# RDF 1.2 Concepts and Abstract Data Model
 
<a id="specification-w3c-state"></a>


[W3C Candidate Recommendation Snapshot](https://www.w3.org/standards/types#CR) 07 April 2026

  More details about this document 

 

This version:



 [https://www.w3.org/TR/2026/CR-rdf12-concepts-20260407/](https://www.w3.org/TR/2026/CR-rdf12-concepts-20260407/) 

 

Latest published version:



 [https://www.w3.org/TR/rdf12-concepts/](https://www.w3.org/TR/rdf12-concepts/) 

 

Latest editor's draft:



[https://w3c.github.io/rdf-concepts/spec/](https://w3c.github.io/rdf-concepts/spec/)

 

History:



 [https://www.w3.org/standards/history/rdf12-concepts/](https://www.w3.org/standards/history/rdf12-concepts/) 



 [Commit history](https://github.com/w3c/rdf-concepts/commits/) 

 

Test suite:



[https://w3c.github.io/rdf-tests/rdf/rdf12/](https://w3c.github.io/rdf-tests/rdf/rdf12/)

 

Implementation report:



 [https://w3c.github.io/rdf-tests/rdf/rdf12/reports/](https://w3c.github.io/rdf-tests/rdf/rdf12/reports/) 

 

Latest Recommendation:



[https://www.w3.org/TR/rdf11-concepts](https://www.w3.org/TR/rdf11-concepts)

 

Editors:



 Gregg Kellogg (until 2025-09-06), in memoriam 



 Olaf Hartig 



 Pierre-Antoine Champin 



 Andy Seaborne 

 

 Former editors: 



 Richard Cyganiak (RDF 1.1) 



 David Wood (RDF 1.1, Chair) 



 Markus Lanthaler (RDF 1.1) 



 Graham Klyne (RDF 1.0) 



 Jeremy J. Carroll (RDF 1.0) 



 Brian McBride (RDF 1.0, Chair) 

 

Feedback:



 [GitHub w3c/rdf-concepts](https://github.com/w3c/rdf-concepts/) ([pull requests](https://github.com/w3c/rdf-concepts/pulls/), [new issue](https://github.com/w3c/rdf-concepts/issues/new/choose), [open issues](https://github.com/w3c/rdf-concepts/issues/)) 



[public-rdf-star-wg@w3.org](mailto:public-rdf-star-wg@w3.org?subject=%5Brdf12-concepts%5D%20YOUR%20TOPIC%20HERE) with subject line [rdf12-concepts] … message topic … ([archives](https://lists.w3.org/Archives/Public/public-rdf-star-wg))

 

  

 [Copyright](https://www.w3.org/policies/#copyright) © 2004-2026 [World Wide Web Consortium](https://www.w3.org/). W3C® [liability](https://www.w3.org/policies/#Legal_Disclaimer), [trademark](https://www.w3.org/policies/#W3C_Trademarks) and [permissive document license](https://www.w3.org/copyright/software-license-2023/) rules apply. 

  

 
<a id="specification-abstract"></a>

<a id="specification-L1753"></a>
## Abstract
 

The Resource Description Framework (RDF) is a framework for representing information on the Web. This document defines an abstract data model which serves to link all RDF-based languages and specifications. The abstract data model has two key data structures:

 

 

- RDF graphs are sets of subject-predicate-object triples, where the elements may be IRIs, blank nodes, datatyped literals, or triple terms. They are used to express descriptions of resources.

 

- RDF datasets are used to organize collections of RDF graphs, and consist of a default graph and zero or more named graphs.

 

 

Compared to RDF 1.1, RDF 1.2 introduces the ability to use an 
<a id="specification-ref-for-dfn-rdf-triple-1"></a>
[RDF triple](#specification-dfn-rdf-triple) as a 
<a id="specification-ref-for-dfn-triple-term-1"></a>
[triple term](#specification-dfn-triple-term), in the 
<a id="specification-ref-for-dfn-object-1"></a>
[object](#specification-dfn-object) position of another 
<a id="specification-ref-for-dfn-rdf-triple-2"></a>
[triple](#specification-dfn-rdf-triple). RDF 1.2 also introduces 
<a id="specification-ref-for-dfn-dir-lang-string-1"></a>
[directional language-tagged strings](#specification-dfn-dir-lang-string), which contain a 
<a id="specification-ref-for-dfn-base-direction-1"></a>
[base direction](#specification-dfn-base-direction) component that allows the initial text direction to be specified for presentation by a user agent. Finally, to ease the transition from RDF 1.1 to RDF 1.2, this specification introduces a mechanism for [explicitly conveying](#specification-section-version-announcement) the version of RDF that is used by a given piece of data. 

 

This specification introduces key concepts and terminology for RDF 1.2, and subsequently discusses datatyping and the handling of 
<a id="specification-ref-for-dfn-fragment-identifier-1"></a>
[fragment identifiers](#specification-dfn-fragment-identifier) in IRIs within RDF graphs.

 

 
<a id="specification-sotd"></a>

<a id="specification-L1783"></a>
## Status of This Document


This section describes the status of this document at the time of its publication. A list of current W3C publications and the latest revision of this technical report can be found in the [W3C standards and drafts index](https://www.w3.org/TR/).

 

This document is part of the RDF 1.2 document suite. It is the central RDF 1.2 specification and defines the core RDF concepts. Test suites and implementation reports of a number of RDF 1.2 specifications that build on this document are available from the [rdf-tests](https://github.com/w3c/rdf-tests/) repository under [rdf-tests/rdf/rdf12](https://github.com/w3c/rdf-tests/tree/main/rdf/rdf12) as referenced in each of the specifications. 

 

RDF 1.2 Concepts (this specification) describes an abstract data model, and does not have an independant test suite, as it is not directly implemented in software. Instead, it is implemented by [the specifications which build on top of it](#specification-related). As a consequence, to exit the W3C Candidate Recommendation phase, the W3C [RDF & SPARQL Working Group](https://www.w3.org/groups/wg/rdf-star) requires that [[RDF12-SEMANTICS](#specification-bib-rdf12-semantics)] and at least one specification for a concrete syntax (e.g. [[RDF12-N-TRIPLES](#specification-bib-rdf12-n-triples)]) have met their own exit criteria for the W3C Candidate Recommendation phase. 

 

RDF 1.2 Concepts is an update to [[RDF11-CONCEPTS](#specification-bib-rdf11-concepts)], which was itself, an update to [[RDF-CONCEPTS-20040210](#specification-bib-rdf-concepts-20040210)].

 

 This document was published by the [RDF & SPARQL Working Group](https://www.w3.org/groups/wg/rdf-star) as a Candidate Recommendation Snapshot using the [Recommendation track](https://www.w3.org/policies/process/20250818/#recs-and-notes). 



Publication as a Candidate Recommendation does not imply endorsement by W3C and its Members. A Candidate Recommendation Snapshot has received [wide review](https://www.w3.org/policies/process/20250818/#dfn-wide-review), is intended to gather [implementation experience](https://w3c.github.io/rdf-tests/rdf/rdf12/reports/), and has commitments from Working Group members to [royalty-free licensing](https://www.w3.org/policies/patent-policy/#sec-Requirements) for implementations.

Future updates to this upcoming Recommendation may incorporate [new features](https://www.w3.org/policies/process/20250818/#allow-new-features).

 This Candidate Recommendation is not expected to advance to Recommendation any earlier than 05 May 2026. 



 This document was produced by a group operating under the [W3C Patent Policy](https://www.w3.org/policies/patent-policy/). W3C maintains a [public list of any patent disclosures](https://www.w3.org/groups/wg/rdf-star/ipr) made in connection with the deliverables of the group; that page also includes instructions for disclosing a patent. An individual who has actual knowledge of a patent that the individual believes contains [Essential Claim(s)](https://www.w3.org/policies/patent-policy/#def-essential) must disclose the information in accordance with [section 6 of the W3C Patent Policy](https://www.w3.org/policies/patent-policy/#sec-Disclosure). 



 This document is governed by the 
<a id="specification-w3c_process_revision"></a>
[18 August 2025 W3C Process Document](https://www.w3.org/policies/process/20250818/). 


<a id="specification-related"></a>

<a id="specification-L1845"></a>
<a id="specification-set-of-documents"></a>
### Set of Documents
[](#specification-related)

 

This document is one of eleven RDF 1.2 and twelve SPARQL 1.2 documents produced by the [RDF & SPARQL Working Group](https://www.w3.org/groups/wg/rdf-star).

  List of documents 

RDF 1.2 Documents:

 

 

1. [What’s New in RDF 1.2](https://w3c.github.io/rdf-new/spec/)

 

2. RDF 1.2 Concepts and Abstract Data Model (this document)

 

3. [RDF 1.2 N-Quads](https://www.w3.org/TR/rdf12-n-quads/)

 

4. [RDF 1.2 N-Triples](https://www.w3.org/TR/rdf12-n-triples/)

 

5. [RDF 1.2 Primer](https://www.w3.org/TR/rdf12-primer/)

 

6. [RDF 1.2 Schema](https://www.w3.org/TR/rdf12-schema/)

 

7. [RDF 1.2 Semantics](https://www.w3.org/TR/rdf12-semantics/)

 

8. [RDF 1.2 TriG](https://www.w3.org/TR/rdf12-trig/)

 

9. [RDF 1.2 Turtle](https://www.w3.org/TR/rdf12-turtle/)

 

10. [RDF 1.2 XML Syntax](https://www.w3.org/TR/rdf12-xml/)

 

11. [RDF 1.2 Interoperability](https://w3c.github.io/rdf-interop/spec/)

 

 

SPARQL 1.2 Documents:

 

 

1. [What’s New in SPARQL 1.2](https://w3c.github.io/sparql-new/spec/)

 

2. [SPARQL 1.2 Concepts](https://w3c.github.io/sparql-concepts/spec/)

 

3. [SPARQL 1.2 Query Language](https://www.w3.org/TR/sparql12-query/)

 

4. [SPARQL 1.2 Update](https://www.w3.org/TR/sparql12-update/)

 

5. [SPARQL 1.2 Service Description](https://www.w3.org/TR/sparql12-service-description/)

 

6. [SPARQL 1.2 Federated Query](https://www.w3.org/TR/sparql12-federated-query/)

 

7. [SPARQL 1.2 Query Results JSON Format](https://www.w3.org/TR/sparql12-results-json/)

 

8. [SPARQL 1.2 Query Results CSV and TSV Formats](https://www.w3.org/TR/sparql12-results-csv-tsv/)

 

9. [SPARQL 1.2 Query Results XML Format](https://www.w3.org/TR/sparql12-results-xml/)

 

10. [SPARQL 1.2 Entailment Regimes](https://www.w3.org/TR/sparql12-entailment/)

 

11. [SPARQL 1.2 Protocol](https://www.w3.org/TR/sparql12-protocol/)

 

12. [SPARQL 1.2 Graph Store Protocol](https://www.w3.org/TR/sparql12-graph-store-protocol/)

 

  

 

 
<a id="specification-section-Introduction"></a>

<a id="specification-L1884"></a>
<a id="specification-x1-introduction"></a>
## 1. Introduction
[](#specification-section-Introduction)



This section is non-normative.

 

The Resource Description Framework (RDF) is a framework for representing information on the Web.

 

This document defines an abstract data model which serves to link all RDF-based languages and specifications, including the following:

 

 

- the formal model-theoretic semantics for RDF [[RDF12-SEMANTICS](#specification-bib-rdf12-semantics)]

 

- serialization syntaxes for storing and exchanging RDF such as [RDF 1.2 N-Triples](https://www.w3.org/TR/rdf12-n-triples/) [[RDF12-N-TRIPLES](#specification-bib-rdf12-n-triples)], [RDF 1.2 Turtle](https://www.w3.org/TR/rdf12-turtle/) [[RDF12-TURTLE](#specification-bib-rdf12-turtle)], and [JSON-LD 1.1](https://www.w3.org/TR/json-ld11/) [[JSON-LD11](#specification-bib-json-ld11)]

 

- the [SPARQL 1.2 Query Language](https://www.w3.org/TR/sparql12-query/) [[SPARQL12-QUERY](#specification-bib-sparql12-query)]

 

- the [RDF 1.2 Schema](https://www.w3.org/TR/rdf12-schema/) [[RDF12-SCHEMA](#specification-bib-rdf12-schema)]

 

 
<a id="specification-data-model"></a>

<a id="specification-L1905"></a>
<a id="specification-x1-1-graph-based-abstract-data-model"></a>
### 1.1 Graph-based Abstract Data Model
[](#specification-data-model)

 

The core structure of the abstract data model is a set of 
<a id="specification-ref-for-dfn-rdf-triple-3"></a>
[triples](#specification-dfn-rdf-triple), each consisting of a 
<a id="specification-ref-for-dfn-subject-1"></a>
[subject](#specification-dfn-subject), a 
<a id="specification-ref-for-dfn-predicate-1"></a>
[predicate](#specification-dfn-predicate) and an 
<a id="specification-ref-for-dfn-object-2"></a>
[object](#specification-dfn-object). A set of such triples is called an 
<a id="specification-ref-for-dfn-rdf-graph-1"></a>
[RDF graph](#specification-dfn-rdf-graph). An RDF graph can be visualized as a node and directed-arc diagram, in which each triple is represented as a node-arc-node link.

 
<a id="specification-fig-rdf-graph"></a>


  

![An RDF graph with two nodes (Subject and Object) and an arc (Predicate) connecting them](../source/rdf-graph.svg)



 
[Enclosing object link](../source/rdf-graph.svg)
 

[Figure 1](#specification-fig-rdf-graph) An RDF graph with two nodes (Subject and Object) and an arc (Predicate) connecting them.

 

 

There are four kinds of 
<a id="specification-ref-for-dfn-node-1"></a>
[nodes](#specification-dfn-node) that can be in an 
<a id="specification-ref-for-dfn-rdf-graph-2"></a>
[RDF graph](#specification-dfn-rdf-graph): 
<a id="specification-ref-for-dfn-iri-1"></a>
[IRIs](#specification-dfn-iri), 
<a id="specification-ref-for-dfn-literal-1"></a>
[literals](#specification-dfn-literal), 
<a id="specification-ref-for-dfn-blank-node-1"></a>
[blank nodes](#specification-dfn-blank-node), and 
<a id="specification-ref-for-dfn-triple-term-2"></a>
[triple terms](#specification-dfn-triple-term).

 

From this definition, it follows that when one term appears in multiple triples, these are simply multiple occurrences of that same term. For example, in a graph containing two triples (here expressed in common [set](https://en.wikipedia.org/wiki/Set_(mathematics)) and [tuple](https://en.wikipedia.org/wiki/Tuple) notation, and using abstract names as distinct terms):

 

```
{ (R1, P1, R3),
  (R2, P2, R3) }
```

 

the term R3 is the same single term used twice, and there are five terms in total. This is more readily shown in two-dimensional graph diagrams, where one single node can simply be connected from or to multiple other nodes using labelled arcs.

 
<a id="specification-fig-rdf-graph-arcs"></a>


  

![An RDF graph with three nodes (R1, R2, and R3) and two arcs (P1 and P2), the arcs respectively connecting R1 and R2 to R3](../source/rdf-graph-arcs.svg)



 
[Enclosing object link](../source/rdf-graph-arcs.svg)
 

[Figure 2](#specification-fig-rdf-graph-arcs) An RDF graph with three nodes (R1, R2, and R3) and two arcs (P1 and P2), the arcs respectively connecting R1 and R2 to R3.

 

 

This abstract data model can be encoded in different ways while preserving the same stucture, as described in [1.9 RDF Documents and Syntaxes](#specification-rdf-documents).

 
<a id="specification-issue-container-generatedID"></a>



<a id="specification-h-note"></a>


Note

 The graph structure of the abstract data model is not a conceptual model. It is a symbolic, structural basis for such modelling, enabling definition and use of 
<a id="specification-ref-for-dfn-rdf-vocabulary-1"></a>
[RDF vocabularies](#specification-dfn-rdf-vocabulary), and semantic 
<a id="specification-dfn-interpretation"></a>

<a id="specification-ref-for-index-term-interpretation-1"></a>
[interpretation](https://www.w3.org/TR/rdf12-semantics/#dfn-interpretation) [[RDF12-SEMANTICS](#specification-bib-rdf12-semantics)]. Practical examples are given in the [RDF 1.2 Primer](https://www.w3.org/TR/rdf12-primer/) [[RDF12-PRIMER](#specification-bib-rdf12-primer)]. 

 

 
<a id="specification-resources-and-statements"></a>

<a id="specification-L1959"></a>
<a id="specification-x1-2-resources-and-statements"></a>
### 1.2 Resources and Statements
[](#specification-resources-and-statements)

 

Any 
<a id="specification-ref-for-dfn-iri-2"></a>
[IRI](#specification-dfn-iri) or 
<a id="specification-ref-for-dfn-literal-2"></a>
[literal](#specification-dfn-literal) 
<a id="specification-dfn-denote"></a>
denotes something in the world (the "universe of discourse"). These things are called 
<a id="specification-dfn-resources"></a>
 
<a id="specification-dfn-resource"></a>
resources. Anything can be a resource, including physical things, documents, abstract concepts, numbers and strings; the term is synonymous with "entity" as it is used in [RDF 1.2 Semantics](https://www.w3.org/TR/rdf12-semantics/) [[RDF12-SEMANTICS](#specification-bib-rdf12-semantics)]. The resource denoted by an IRI is called its 
<a id="specification-ref-for-dfn-referent-1"></a>
[referent](#specification-dfn-referent), and the resource denoted by a literal is called its 
<a id="specification-ref-for-dfn-literal-value-1"></a>
[literal value](#specification-dfn-literal-value). Literals have 
<a id="specification-ref-for-dfn-datatype-1"></a>
[datatypes](#specification-dfn-datatype) that define the range of possible values, such as strings, numbers, and dates. Special kinds of literals — 
<a id="specification-ref-for-dfn-language-tagged-string-1"></a>
[language-tagged strings](#specification-dfn-language-tagged-string) and 
<a id="specification-ref-for-dfn-dir-lang-string-2"></a>
[directional language-tagged strings](#specification-dfn-dir-lang-string) — respectively denote plain-text strings in a natural language and plain-text strings in a natural language including an initial text direction.

 

Asserting an 
<a id="specification-ref-for-dfn-rdf-triple-4"></a>
[RDF triple](#specification-dfn-rdf-triple) says that some relationship, indicated by the 
<a id="specification-ref-for-dfn-predicate-2"></a>
[predicate](#specification-dfn-predicate), holds between the 
<a id="specification-ref-for-dfn-resource-1"></a>
[resources](#specification-dfn-resource) 
<a id="specification-ref-for-dfn-denote-1"></a>
[denoted](#specification-dfn-denote) by the 
<a id="specification-ref-for-dfn-subject-2"></a>
[subject](#specification-dfn-subject) and 
<a id="specification-ref-for-dfn-object-3"></a>
[object](#specification-dfn-object) (as explained [below](#specification-section-triple-terms-reification), not all triples are asserted). This statement corresponding to an RDF triple is known as an 
<a id="specification-dfn-rdf-statement"></a>
RDF statement. The predicate itself is an 
<a id="specification-ref-for-dfn-iri-3"></a>
[IRI](#specification-dfn-iri) and denotes a 
<a id="specification-dfn-property"></a>
property, that is, a 
<a id="specification-ref-for-dfn-resource-2"></a>
[resource](#specification-dfn-resource) that can be thought of as a binary relation. (Relations that involve more than two entities can only be 
<a id="specification-ref-for-index-term-indirectly-expressed-in-rdf-1"></a>
[indirectly expressed in RDF](https://www.w3.org/TR/swbp-n-aryRelations/#) [[SWBP-N-ARYRELATIONS](#specification-bib-swbp-n-aryrelations)].)

 

Unlike 
<a id="specification-ref-for-dfn-iri-4"></a>
[IRIs](#specification-dfn-iri) and 
<a id="specification-ref-for-dfn-literal-3"></a>
[literals](#specification-dfn-literal), 
<a id="specification-ref-for-dfn-blank-node-2"></a>
[blank nodes](#specification-dfn-blank-node) do not identify specific 
<a id="specification-ref-for-dfn-resource-3"></a>
[resources](#specification-dfn-resource). 
<a id="specification-ref-for-dfn-rdf-statement-1"></a>
[Statements](#specification-dfn-rdf-statement) involving blank nodes say that something with the given relationships exists, without explicitly naming it.

 

 
<a id="specification-referents"></a>

<a id="specification-L1999"></a>
<a id="specification-x1-3-the-referent-of-an-iri"></a>
### 1.3 The Referent of an IRI
[](#specification-referents)

 

The 
<a id="specification-ref-for-dfn-resource-4"></a>
[resource](#specification-dfn-resource) 
<a id="specification-ref-for-dfn-denote-2"></a>
[denoted](#specification-dfn-denote) by an 
<a id="specification-ref-for-dfn-iri-5"></a>
[IRI](#specification-dfn-iri) is also called its 
<a id="specification-dfn-referent"></a>
referent. For some IRIs with particular meanings, such as those identifying XSD datatypes, the referent is fixed by this specification. For all other IRIs, what exactly is 
<a id="specification-ref-for-dfn-denote-3"></a>
[denoted](#specification-dfn-denote) by any given IRI is not defined by this specification. Other specifications may fix IRI referents, or apply other constraints on what may be the referent of any IRI.

 

Guidelines for determining the 
<a id="specification-ref-for-dfn-referent-2"></a>
[referent](#specification-dfn-referent) of an 
<a id="specification-ref-for-dfn-iri-6"></a>
[IRI](#specification-dfn-iri) are provided in other documents, like [Architecture of the World Wide Web, Volume One](https://www.w3.org/TR/webarch/) [[WEBARCH](#specification-bib-webarch)] and [Cool URIs for the Semantic Web](https://www.w3.org/TR/cooluris/) [[COOLURIS](#specification-bib-cooluris)]. A very brief, informal, and partial account follows:

 

 

- By design, IRIs have global scope. Thus, two different appearances of an IRI 
<a id="specification-ref-for-dfn-denote-4"></a>
[denote](#specification-dfn-denote) the same 
<a id="specification-ref-for-dfn-resource-5"></a>
[resource](#specification-dfn-resource). Violating this principle constitutes an 
<a id="specification-ref-for-index-term-iri-collision-1"></a>
[IRI collision](https://www.w3.org/TR/webarch/#URI-collision) [[WEBARCH](#specification-bib-webarch)].

 

- By social convention, the 
<a id="specification-ref-for-index-term-iri-owner-1"></a>
[IRI owner](https://www.w3.org/TR/webarch/#uri-ownership) [[WEBARCH](#specification-bib-webarch)] gets to say what the intended (or usual) referent of an 
<a id="specification-ref-for-dfn-iri-7"></a>
[IRI](#specification-dfn-iri) is. Applications and users need not abide by this intended denotation, but there may be a loss of interoperability with other applications and users if they do not do so.

 

- The IRI owner can establish the intended 
<a id="specification-ref-for-dfn-referent-3"></a>
[referent](#specification-dfn-referent) by means of a specification or other document that explains what is denoted. For example, the [The Organization Ontology](https://www.w3.org/TR/vocab-org/) [[VOCAB-ORG](#specification-bib-vocab-org)] specifies the intended referents of various IRIs that start with `http://www.w3.org/ns/org#`.

 

- A good way of communicating the intended referent is to set up the IRI so that it 
<a id="specification-ref-for-index-term-dereferences-1"></a>
[dereferences](https://www.w3.org/TR/webarch/#uri-dereference) [[WEBARCH](#specification-bib-webarch)] to such a document.

 

- Such a document can, in fact, be an 
<a id="specification-ref-for-dfn-rdf-document-1"></a>
[RDF document](#specification-dfn-rdf-document) that describes the denoted resource by means of 
<a id="specification-ref-for-dfn-rdf-statement-2"></a>
[RDF statements](#specification-dfn-rdf-statement).

 

 

Perhaps the most important characteristic of 
<a id="specification-ref-for-dfn-iri-8"></a>
[IRIs](#specification-dfn-iri) in web architecture is that they can be 
<a id="specification-ref-for-index-term-dereferences-2"></a>
[dereferenced](https://www.w3.org/TR/webarch/#uri-dereference), and hence serve as starting points for interactions with a remote server. This specification is not concerned with such interactions. It does not define an interaction model. It only treats IRIs as globally unique identifiers in a graph data model that describes resources. However, those interactions are critical to the concept of [Linked Data Design Issues](https://www.w3.org/DesignIssues/LinkedData.html), [[LINKED-DATA](#specification-bib-linked-data)], which uses the RDF 
<a id="specification-ref-for-dfn-abstract-syntax-1"></a>
[abstract syntax](#specification-dfn-abstract-syntax) and 
<a id="specification-ref-for-dfn-concrete-rdf-syntax-1"></a>
[concrete RDF syntaxes](#specification-dfn-concrete-rdf-syntax), the latter also referred to as serialization formats.

 

 
<a id="specification-vocabularies"></a>

<a id="specification-L2059"></a>
<a id="specification-x1-4-rdf-vocabularies-and-namespace-iris"></a>
### 1.4 RDF Vocabularies and Namespace IRIs
[](#specification-vocabularies)

 

An 
<a id="specification-dfn-rdf-vocabulary"></a>
RDF vocabulary is a collection of 
<a id="specification-ref-for-dfn-iri-9"></a>
[IRIs](#specification-dfn-iri) intended for use in 
<a id="specification-ref-for-dfn-rdf-graph-3"></a>
[RDF graphs](#specification-dfn-rdf-graph). For example, the IRIs documented in [[RDF12-SCHEMA](#specification-bib-rdf12-schema)] are the RDF Schema vocabulary. RDF Schema can itself be used to define and document additional RDF vocabularies. Some such vocabularies are mentioned in the [RDF 1.2 Primer](https://www.w3.org/TR/rdf12-primer/) [[RDF12-PRIMER](#specification-bib-rdf12-primer)].

 

The 
<a id="specification-ref-for-dfn-iri-10"></a>
[IRIs](#specification-dfn-iri) in an 
<a id="specification-ref-for-dfn-rdf-vocabulary-2"></a>
[RDF vocabulary](#specification-dfn-rdf-vocabulary) often begin with a common substring known as a 
<a id="specification-dfn-namespace-iri"></a>
namespace IRI. Some namespace IRIs are associated by convention with a short name known as a 
<a id="specification-dfn-namespace-prefix"></a>
namespace prefix. 


<a id="specification-tab-vocab-ns"></a>


- Some namespace prefixes and IRIs used in this specification
- Namespace prefix | Namespace IRI | RDF vocabulary
- rdf | [`http://www.w3.org/1999/02/22-rdf-syntax-ns#`](https://www.w3.org/1999/02/22-rdf-syntax-ns#) | The RDF built-in vocabulary [[RDF12-SCHEMA](#specification-bib-rdf12-schema)]
- rdfs | [`http://www.w3.org/2000/01/rdf-schema#`](https://www.w3.org/2000/01/rdf-schema#) | The RDF Schema vocabulary [[RDF12-SCHEMA](#specification-bib-rdf12-schema)]
- xsd | [`http://www.w3.org/2001/XMLSchema#`](https://www.w3.org/2001/XMLSchema#) | The 
<a id="specification-ref-for-dfn-rdf-compatible-xsd-types-1"></a>
[RDF-compatible XSD types](#specification-dfn-rdf-compatible-xsd-types)

 

In some serialization formats, it is common to associate some 
<a id="specification-ref-for-dfn-namespace-iri-1"></a>
[namespace IRIs](#specification-dfn-namespace-iri) with arbitrary 
<a id="specification-ref-for-dfn-namespace-prefix-1"></a>
[namespace prefixes](#specification-dfn-namespace-prefix), and to improve readability by abbreviating 
<a id="specification-ref-for-dfn-iri-11"></a>
[IRIs](#specification-dfn-iri) that start with one of those 
<a id="specification-ref-for-dfn-namespace-iri-2"></a>
[namespace IRIs](#specification-dfn-namespace-iri) by using the corresponding 
<a id="specification-ref-for-dfn-namespace-prefix-2"></a>
[namespace prefix](#specification-dfn-namespace-prefix). For example, based on the prefix mapping in [the table above](#specification-tab-vocab-ns), the IRI `http://www.w3.org/1999/02/22-rdf-syntax-ns#XMLLiteral` would be abbreviated as `rdf:XMLLiteral`. Note however that such abbreviations are not meant to be processed directly as IRIs, and are not to be used in syntactic contexts where IRIs are expected. Note also that 
<a id="specification-ref-for-dfn-namespace-iri-3"></a>
[namespace IRIs](#specification-dfn-namespace-iri) and 
<a id="specification-ref-for-dfn-namespace-prefix-3"></a>
[namespace prefixes](#specification-dfn-namespace-prefix) are not a formal part of the RDF abstract data model. They are merely a syntactic convenience for abbreviating IRIs; for processing, the actual IRIs are reconstructed by replacing each namespace prefix with the corresponding namespace IRI. 

 

The term “
<a id="specification-dfn-namespace"></a>
namespace” on its own does not have a well-defined meaning in the context of RDF, but is sometimes informally used to mean “
<a id="specification-ref-for-dfn-namespace-iri-4"></a>
[namespace IRI](#specification-dfn-namespace-iri)” or “
<a id="specification-ref-for-dfn-rdf-vocabulary-3"></a>
[RDF vocabulary](#specification-dfn-rdf-vocabulary)”.

 

 
<a id="specification-section-triple-terms-reification"></a>

<a id="specification-L2116"></a>
<a id="specification-x1-5-triple-terms-and-reification"></a>
### 1.5 Triple Terms and Reification
[](#specification-section-triple-terms-reification)

 

A 
<a id="specification-ref-for-dfn-triple-term-3"></a>
[triple term](#specification-dfn-triple-term) is an 
<a id="specification-ref-for-dfn-rdf-triple-5"></a>
[RDF triple](#specification-dfn-rdf-triple) used as an 
<a id="specification-ref-for-dfn-rdf-term-1"></a>
[RDF term](#specification-dfn-rdf-term) within another triple. Being an 
<a id="specification-ref-for-dfn-rdf-triple-6"></a>
[RDF triple](#specification-dfn-rdf-triple), it denotes a 
<a id="specification-ref-for-dfn-proposition-1"></a>
[proposition](#specification-dfn-proposition). 



 A 
<a id="specification-dfn-reifying-triple"></a>
reifying triple is a triple where the 
<a id="specification-ref-for-dfn-predicate-3"></a>
[predicate](#specification-dfn-predicate) is `rdf:reifies` and the 
<a id="specification-ref-for-dfn-object-4"></a>
[object](#specification-dfn-object) is a 
<a id="specification-ref-for-dfn-triple-term-4"></a>
[triple term](#specification-dfn-triple-term). The 
<a id="specification-ref-for-dfn-subject-3"></a>
[subject](#specification-dfn-subject) of that triple is called a 
<a id="specification-dfn-reifier"></a>
reifier, and it can be the subject or object of other triples. 

 

 A 
<a id="specification-ref-for-dfn-reifier-1"></a>
[reifier](#specification-dfn-reifier) may denote a variety of things that are related to the triple term's 
<a id="specification-ref-for-dfn-proposition-2"></a>
[proposition](#specification-dfn-proposition), such as a statement or belief that the 
<a id="specification-ref-for-dfn-proposition-3"></a>
[proposition](#specification-dfn-proposition) holds. It is expected that the 
<a id="specification-ref-for-dfn-reifier-2"></a>
[reifiers](#specification-dfn-reifier) (rather than the 
<a id="specification-ref-for-dfn-triple-term-5"></a>
[triple terms](#specification-dfn-triple-term)) will be used in further statements. This section briefly describes this common usage. For more examples, refer to the [RDF 1.2 Primer](https://www.w3.org/TR/rdf12-primer/) [[RDF12-PRIMER](#specification-bib-rdf12-primer)]. 

 

 For example, the following diagram represents a 
<a id="specification-ref-for-dfn-reifying-triple-1"></a>
[reifying triple](#specification-dfn-reifying-triple) of a 
<a id="specification-ref-for-dfn-triple-term-6"></a>
[triple term](#specification-dfn-triple-term), together with a 
<a id="specification-ref-for-dfn-rdf-triple-7"></a>
[triple](#specification-dfn-rdf-triple) that includes the 
<a id="specification-ref-for-dfn-reifier-3"></a>
[reifier](#specification-dfn-reifier) as the 
<a id="specification-ref-for-dfn-subject-4"></a>
[subject](#specification-dfn-subject). The latter describes the reifier as a claim, made by `:Bob`, that the proposition denoted by the reified triple term holds. In other words, `:Bob` claims that `:Alice`'s family name is "Liddell". 

 
<a id="specification-fig-triple-term"></a>


  

![An RDF graph containing a triple that references an unasserted triple term (with grey dashed arc) via a reifier](../source/triple-term.svg)

[aria-describedby: fig-triple-term-alt](#specification-fig-triple-term-alt)

 
[Enclosing object link](../source/triple-term.svg)
 
<a id="specification-fig-triple-term-alt"></a>


[Figure 3](#specification-fig-triple-term)  An 
<a id="specification-ref-for-dfn-rdf-graph-4"></a>
[RDF graph](#specification-dfn-rdf-graph) containing a 
<a id="specification-ref-for-dfn-reifying-triple-2"></a>
[reifying triple](#specification-dfn-reifying-triple) that references a 
<a id="specification-ref-for-dfn-triple-term-7"></a>
[triple term](#specification-dfn-triple-term) (which is unasserted, depicted using a grey, dashed arc) from a 
<a id="specification-ref-for-dfn-reifier-4"></a>
[reifier](#specification-dfn-reifier); and a triple describing this reifier. 

 

 

 In this example, the 
<a id="specification-ref-for-dfn-proposition-4"></a>
[proposition](#specification-dfn-proposition) denoted by the 
<a id="specification-ref-for-dfn-triple-term-8"></a>
[triple term](#specification-dfn-triple-term) (i.e., the proposition that `:Alice`'s family name is `"Liddell"`) is not claimed to be true. That would only be the case if the triple used as a triple term was also an 
<a id="specification-ref-for-dfn-asserted-triple-1"></a>
[asserted triple](#specification-dfn-asserted-triple) in the RDF graph. By using non-asserted triple terms, as in the figure, one can make statements about unasserted statements; for example, if one is unsure whether `:Alice`'s family name is actually `"Liddell"`. 

 

Here is a variation on the graph shown in [Figure 3](#specification-fig-triple-term). This represents a graph where an 
<a id="specification-ref-for-dfn-asserted-triple-2"></a>
[asserted triple](#specification-dfn-asserted-triple) corresponds to the 
<a id="specification-ref-for-dfn-triple-term-9"></a>
[triple term](#specification-dfn-triple-term) object of a 
<a id="specification-ref-for-dfn-reifying-triple-3"></a>
[reifying triple](#specification-dfn-reifying-triple). In this case, the subset of triples including the 
<a id="specification-ref-for-dfn-reifier-5"></a>
[reifier](#specification-dfn-reifier) as subject—as illustrated in these examples— is called a 
<a id="specification-dfn-triple-annotation"></a>
triple annotation. 

 
<a id="specification-fig-asserted-triple-term"></a>


  

![An RDF graph containing a triple annotation, where the triple term of a reifying triple corresponds to an asserted triple](../source/asserted-triple-term.svg)

[aria-describedby: fig-asserted-triple-term-alt](#specification-fig-asserted-triple-term-alt)

 
[Enclosing object link](../source/asserted-triple-term.svg)
 
<a id="specification-fig-asserted-triple-term-alt"></a>


[Figure 4](#specification-fig-asserted-triple-term)  An 
<a id="specification-ref-for-dfn-rdf-graph-5"></a>
[RDF graph](#specification-dfn-rdf-graph) containing a 
<a id="specification-ref-for-dfn-triple-annotation-1"></a>
[triple annotation](#specification-dfn-triple-annotation), where the 
<a id="specification-ref-for-dfn-triple-term-10"></a>
[triple term](#specification-dfn-triple-term) of a 
<a id="specification-ref-for-dfn-reifying-triple-4"></a>
[reifying triple](#specification-dfn-reifying-triple) corresponds to an 
<a id="specification-ref-for-dfn-asserted-triple-3"></a>
[asserted triple](#specification-dfn-asserted-triple). Due to the asserted triple, the diagram represents the proposition as a fact, meaning that the relationship holds. 

 

 

 Concrete syntaxes, such as Turtle [[RDF12-TURTLE](#specification-bib-rdf12-turtle)], may have shortcuts for specifying 
<a id="specification-ref-for-dfn-reifying-triple-5"></a>
[reifying triples](#specification-dfn-reifying-triple) and 
<a id="specification-ref-for-dfn-triple-annotation-2"></a>
[triple annotations](#specification-dfn-triple-annotation) more succinctly. 

 

Finally, 
<a id="specification-ref-for-dfn-rdf-term-2"></a>
[RDF terms](#specification-dfn-rdf-term) that 
<a id="specification-ref-for-dfn-appear-1"></a>
[appear](#specification-dfn-appear) in a 
<a id="specification-ref-for-dfn-triple-term-11"></a>
[triple term](#specification-dfn-triple-term) have the same 
<a id="specification-ref-for-dfn-denote-5"></a>
[denotation](#specification-dfn-denote) as when they appear in an 
<a id="specification-ref-for-dfn-asserted-triple-4"></a>
[asserted triple](#specification-dfn-asserted-triple) in the 
<a id="specification-ref-for-dfn-rdf-graph-6"></a>
[graph](#specification-dfn-rdf-graph). For example, the term `:Alice` from a 
<a id="specification-ref-for-dfn-triple-term-12"></a>
[triple term](#specification-dfn-triple-term) and `:Alice` in an 
<a id="specification-ref-for-dfn-asserted-triple-5"></a>
[asserted triple](#specification-dfn-asserted-triple) both denote the same resource. For this reason, we say that triple terms are 
<a id="specification-dfn-transparent"></a>
transparent.

 
<a id="specification-issue-container-generatedID-0"></a>



<a id="specification-h-note-0"></a>


Note



 

 As already stated, 
<a id="specification-ref-for-dfn-reifier-6"></a>
[reifiers](#specification-dfn-reifier) are meant to serve a broad range of use cases: statements or beliefs that a proposition is true, situations in which the proposition is true, events that caused the proposition to become true, etc. Because of this diversity, the meaning of the `rdf:reifies` property is deliberately generic.

 

 There can be multiple, distinct reifiers related to the same abstract proposition, such as statements with different sources, or situations with different characteristics. One reifier may also be used to reify multiple, distinct propositions, expressing for example the fact that the same situation could stem from different propositions.

 

Since a proposition that is reified does not have to hold, it is possible to make statements about any kind of statement, including an unasserted statement that contradicts another statement, whether asserted or not.

 



 

 
<a id="specification-change-over-time"></a>

<a id="specification-L2210"></a>
<a id="specification-x1-6-rdf-and-change-over-time"></a>
### 1.6 RDF and Change over Time
[](#specification-change-over-time)

 

The RDF abstract data model is atemporal: 
<a id="specification-ref-for-dfn-rdf-graph-7"></a>
[RDF graphs](#specification-dfn-rdf-graph) are static snapshots of information.

 

However, 
<a id="specification-ref-for-dfn-rdf-graph-8"></a>
[RDF graphs](#specification-dfn-rdf-graph) can express information about events and about temporal aspects of other entities, given appropriate 
<a id="specification-ref-for-dfn-rdf-vocabulary-4"></a>
[vocabulary](#specification-dfn-rdf-vocabulary) terms.

 

Since 
<a id="specification-ref-for-dfn-rdf-graph-9"></a>
[RDF graphs](#specification-dfn-rdf-graph) are defined as mathematical sets, adding or removing 
<a id="specification-ref-for-dfn-rdf-triple-8"></a>
[triples](#specification-dfn-rdf-triple) from an RDF graph yields a different RDF graph.

 

We informally use the term 
<a id="specification-dfn-rdf-source"></a>
RDF source to refer to a persistent yet mutable source or container of 
<a id="specification-ref-for-dfn-rdf-graph-10"></a>
[RDF graphs](#specification-dfn-rdf-graph). An RDF source is a 
<a id="specification-ref-for-dfn-resource-6"></a>
[resource](#specification-dfn-resource) that may be said to have a state that can change over time. A snapshot of the state can be expressed as an RDF graph. For example, any web document that has an RDF-bearing representation may be considered an RDF source. Like all resources, RDF sources may be named with 
<a id="specification-ref-for-dfn-iri-12"></a>
[IRIs](#specification-dfn-iri) and therefore described in other RDF graphs.

 

Intuitively speaking, changes in the universe of discourse can be reflected in the following ways:

 

 

- An 
<a id="specification-ref-for-dfn-iri-13"></a>
[IRI](#specification-dfn-iri), once minted, should never change its intended 
<a id="specification-ref-for-dfn-referent-4"></a>
[referent](#specification-dfn-referent). (See 
<a id="specification-ref-for-index-term-uri-persistence-1"></a>
[URI persistence](https://www.w3.org/TR/webarch/#URI-persistence) [[WEBARCH](#specification-bib-webarch)].)

 

- 
<a id="specification-ref-for-dfn-literal-4"></a>
[Literals](#specification-dfn-literal), by design, are constants and never change their 
<a id="specification-ref-for-dfn-literal-value-2"></a>
[value](#specification-dfn-literal-value).

 

- A relationship that holds between two 
<a id="specification-ref-for-dfn-resource-7"></a>
[resources](#specification-dfn-resource) at one time may not hold at another time.

 

- 
<a id="specification-ref-for-dfn-rdf-source-1"></a>
[RDF sources](#specification-dfn-rdf-source) may change their state over time. That is, they may provide different 
<a id="specification-ref-for-dfn-rdf-graph-11"></a>
[RDF graphs](#specification-dfn-rdf-graph) at different times.

 

- Some 
<a id="specification-ref-for-dfn-rdf-source-2"></a>
[RDF sources](#specification-dfn-rdf-source) may, however, be immutable snapshots of another RDF source, archiving its state at some point in time.

 

 

 
<a id="specification-managing-graphs"></a>

<a id="specification-L2255"></a>
<a id="specification-x1-7-working-with-multiple-rdf-graphs"></a>
### 1.7 Working with Multiple RDF Graphs
[](#specification-managing-graphs)

 

As RDF graphs are sets of triples, they can be combined easily, supporting the use of data from multiple sources. Nevertheless, it is sometimes desirable to work with multiple RDF graphs while keeping their contents separate. 
<a id="specification-ref-for-dfn-rdf-dataset-1"></a>
[RDF datasets](#specification-dfn-rdf-dataset) support this requirement.

 

An 
<a id="specification-ref-for-dfn-rdf-dataset-2"></a>
[RDF dataset](#specification-dfn-rdf-dataset) is a collection of 
<a id="specification-ref-for-dfn-rdf-graph-12"></a>
[RDF graphs](#specification-dfn-rdf-graph). All but one of these graphs have an associated 
<a id="specification-ref-for-dfn-iri-14"></a>
[IRI](#specification-dfn-iri) or blank node. They are called 
<a id="specification-ref-for-dfn-named-graph-1"></a>
[named graphs](#specification-dfn-named-graph), and the IRI or blank node is called the 
<a id="specification-ref-for-dfn-graph-name-1"></a>
[graph name](#specification-dfn-graph-name). The remaining graph does not have an associated IRI, and is called the 
<a id="specification-ref-for-dfn-default-graph-1"></a>
[default graph](#specification-dfn-default-graph) of the RDF dataset.

 

There are many possible uses for 
<a id="specification-ref-for-dfn-rdf-dataset-3"></a>
[RDF datasets](#specification-dfn-rdf-dataset). One such use is to hold snapshots of multiple 
<a id="specification-ref-for-dfn-rdf-source-3"></a>
[RDF sources](#specification-dfn-rdf-source).

 

 
<a id="specification-entailment"></a>

<a id="specification-L2277"></a>
<a id="specification-x1-8-equivalence-entailment-and-inconsistency"></a>
### 1.8 Equivalence, Entailment and Inconsistency
[](#specification-entailment)

 

An 
<a id="specification-ref-for-dfn-rdf-triple-9"></a>
[RDF triple](#specification-dfn-rdf-triple) denotes a 
<a id="specification-dfn-proposition"></a>
proposition — a simple logical expression, describing a relationship between two entities. An 
<a id="specification-ref-for-dfn-asserted-triple-6"></a>
[asserted triple](#specification-dfn-asserted-triple) is a claim that the corresponding proposition is true. An 
<a id="specification-ref-for-dfn-rdf-graph-13"></a>
[RDF graph](#specification-dfn-rdf-graph) is the conjunction (logical AND) of all the claims made by its 
<a id="specification-ref-for-dfn-asserted-triple-7"></a>
[asserted triples](#specification-dfn-asserted-triple). The precise details of this meaning of 
<a id="specification-ref-for-dfn-rdf-triple-10"></a>
[RDF triples](#specification-dfn-rdf-triple) and 
<a id="specification-ref-for-dfn-rdf-graph-14"></a>
[RDF graphs](#specification-dfn-rdf-graph) are the subject of [RDF 1.2 Semantics](https://www.w3.org/TR/rdf12-semantics/) [[RDF12-SEMANTICS](#specification-bib-rdf12-semantics)], which yields the following relationships between 
<a id="specification-ref-for-dfn-rdf-graph-15"></a>
[RDF graphs](#specification-dfn-rdf-graph):

 

 


<a id="specification-dfn-entailment"></a>
Entailment

 

An 
<a id="specification-ref-for-dfn-rdf-graph-16"></a>
[RDF graph](#specification-dfn-rdf-graph) A entails another RDF graph B if every possible arrangement of the world that makes A true also makes B true. When A entails B, if the truth of A is presumed or demonstrated then the truth of B is established. 

 


<a id="specification-dfn-equivalence"></a>
Equivalence

 

Two 
<a id="specification-ref-for-dfn-rdf-graph-17"></a>
[RDF graphs](#specification-dfn-rdf-graph) A and B are equivalent if they make the same claim about the world. A is equivalent to B if and only if A 
<a id="specification-ref-for-dfn-entailment-1"></a>
[entails](#specification-dfn-entailment) B and B entails A. 

 


<a id="specification-dfn-inconsistent"></a>
Inconsistency
<a id="specification-dfn-inconsistency"></a>


 

An 
<a id="specification-ref-for-dfn-rdf-graph-18"></a>
[RDF graph](#specification-dfn-rdf-graph) is inconsistent if it contains an internal contradiction. There is no possible arrangement of the world that would make the expression true.

 

 

An 
<a id="specification-dfn-entailment-regime"></a>

<a id="specification-dfn-entailment-regime-0"></a>

<a id="specification-ref-for-index-term-entailment-regime-1"></a>
[entailment regime](https://www.w3.org/TR/rdf12-semantics/#dfn-entailment-regime) [[RDF12-SEMANTICS](#specification-bib-rdf12-semantics)] is a specification that defines precise conditions that make these relationships hold. RDF itself recognizes only some basic cases of entailment, 
<a id="specification-ref-for-dfn-equivalence-1"></a>
[equivalence](#specification-dfn-equivalence) and inconsistency. Other specifications, such as [RDF 1.2 Schema](https://www.w3.org/TR/rdf12-schema/) [[RDF12-SCHEMA](#specification-bib-rdf12-schema)] and 
<a id="specification-ref-for-index-term-owl-2-1"></a>
[OWL 2](https://www.w3.org/TR/owl2-overview/#) [[OWL2-OVERVIEW](#specification-bib-owl2-overview)], add more powerful entailment regimes, as do some domain-specific 
<a id="specification-ref-for-dfn-rdf-vocabulary-5"></a>
[vocabularies](#specification-dfn-rdf-vocabulary).

 

This specification does not constrain how implementations use the logical relationships defined by 
<a id="specification-ref-for-index-term-entailment-regime-2"></a>
[entailment regimes](https://www.w3.org/TR/rdf12-semantics/#dfn-entailment-regime). Implementations may or may not detect 
<a id="specification-ref-for-dfn-inconsistent-1"></a>
[inconsistencies](#specification-dfn-inconsistent), and may make all, some or no 
<a id="specification-ref-for-dfn-entailment-2"></a>
[entailed](#specification-dfn-entailment) information available to users.

 

 
<a id="specification-rdf-documents"></a>

<a id="specification-L2330"></a>
<a id="specification-x1-9-rdf-documents-and-syntaxes"></a>
### 1.9 RDF Documents and Syntaxes
[](#specification-rdf-documents)

 

An 
<a id="specification-dfn-rdf-document"></a>
RDF document is a document that encodes an 
<a id="specification-ref-for-dfn-rdf-graph-19"></a>
[RDF graph](#specification-dfn-rdf-graph) or 
<a id="specification-ref-for-dfn-rdf-dataset-4"></a>
[RDF dataset](#specification-dfn-rdf-dataset) in a 
<a id="specification-dfn-concrete-rdf-syntax"></a>
concrete RDF syntax, such as N-Triples [[RDF12-N-TRIPLES](#specification-bib-rdf12-n-triples)], Turtle [[RDF12-TURTLE](#specification-bib-rdf12-turtle)], RDFa [[RDFA-CORE](#specification-bib-rdfa-core)], JSON-LD [[JSON-LD11](#specification-bib-json-ld11)], or TriG [[RDF12-TRIG](#specification-bib-rdf12-trig)]. RDF documents enable the exchange of RDF graphs and RDF datasets between systems.

 

A 
<a id="specification-ref-for-dfn-concrete-rdf-syntax-2"></a>
[concrete RDF syntax](#specification-dfn-concrete-rdf-syntax) may offer many different ways to encode the same 
<a id="specification-ref-for-dfn-rdf-graph-20"></a>
[RDF graph](#specification-dfn-rdf-graph) or 
<a id="specification-ref-for-dfn-rdf-dataset-5"></a>
[RDF dataset](#specification-dfn-rdf-dataset), for example through the use of 
<a id="specification-ref-for-dfn-namespace-prefix-4"></a>
[namespace prefixes](#specification-dfn-namespace-prefix), 
<a id="specification-ref-for-dfn-iri-reference-1"></a>
[IRI references](#specification-dfn-iri-reference), 
<a id="specification-ref-for-dfn-blank-node-identifier-1"></a>
[blank node identifiers](#specification-dfn-blank-node-identifier), and different ordering of triples. While these aspects can have great effect on the convenience of working with the 
<a id="specification-ref-for-dfn-rdf-document-2"></a>
[RDF document](#specification-dfn-rdf-document), they are not significant for its meaning.

 

The basis for 
<a id="specification-ref-for-dfn-concrete-rdf-syntax-3"></a>
[concrete RDF syntaxes](#specification-dfn-concrete-rdf-syntax) is the structure of the [abstract data model](#specification-data-model), called the 
<a id="specification-dfn-abstract-syntax"></a>
abstract syntax; summarized in the following two tables.

 
<a id="specification-tab-graph-abstract-syntax"></a>


- The abstract syntax of
- <a id="specification-ref-for-dfn-rdf-graph-21"></a>
[RDF graphs](#specification-dfn-rdf-graph)
- Production | Defined as
- RDF graph | a set of zero or more 
<a id="specification-ref-for-dfn-rdf-triple-11"></a>
[triples](#specification-dfn-rdf-triple)
- triple | a 3-tuple of a 
<a id="specification-ref-for-dfn-subject-5"></a>
[subject](#specification-dfn-subject), a 
<a id="specification-ref-for-dfn-predicate-4"></a>
[predicate](#specification-dfn-predicate), and an 
<a id="specification-ref-for-dfn-object-5"></a>
[object](#specification-dfn-object)
- subject | either an 
<a id="specification-ref-for-dfn-iri-15"></a>
[IRI](#specification-dfn-iri) or a 
<a id="specification-ref-for-dfn-blank-node-3"></a>
[Blank node](#specification-dfn-blank-node)
- predicate | an 
<a id="specification-ref-for-dfn-iri-16"></a>
[IRI](#specification-dfn-iri)
- object | either an 
<a id="specification-ref-for-dfn-iri-17"></a>
[IRI](#specification-dfn-iri) or a 
<a id="specification-ref-for-dfn-blank-node-4"></a>
[Blank node](#specification-dfn-blank-node) or a 
<a id="specification-ref-for-dfn-literal-5"></a>
[Literal](#specification-dfn-literal) or a 
<a id="specification-ref-for-dfn-rdf-triple-12"></a>
[triple](#specification-dfn-rdf-triple)

 
 
<a id="specification-tab-dataset-abstract-syntax"></a>


- The abstract syntax of
- <a id="specification-ref-for-dfn-rdf-dataset-6"></a>
[RDF datasets](#specification-dfn-rdf-dataset)
- Production | Defined as
- RDF dataset | a pair of a 
<a id="specification-ref-for-dfn-default-graph-2"></a>
[default graph](#specification-dfn-default-graph) and a set of zero or more 
<a id="specification-ref-for-dfn-named-graph-2"></a>
[named graphs](#specification-dfn-named-graph)
- default graph | an 
<a id="specification-ref-for-dfn-rdf-graph-22"></a>
[RDF graph](#specification-dfn-rdf-graph)
- named graph | a pair of a 
<a id="specification-ref-for-dfn-graph-name-2"></a>
[graph name](#specification-dfn-graph-name) and an 
<a id="specification-ref-for-dfn-rdf-graph-23"></a>
[RDF graph](#specification-dfn-rdf-graph)
- graph name | either an 
<a id="specification-ref-for-dfn-iri-18"></a>
[IRI](#specification-dfn-iri) or a 
<a id="specification-ref-for-dfn-blank-node-5"></a>
[Blank node](#specification-dfn-blank-node)

 

 
<a id="specification-section-version-announcement"></a>

<a id="specification-L2413"></a>
<a id="specification-x1-10-rdf-version-announcement"></a>
### 1.10 RDF Version Announcement
[](#specification-section-version-announcement)

 

To allow RDF parsers to error or warn about unsupported RDF versions as early as possible, RDF serialization formats are expected to allow a version to be specified, via either a media-type parameter, a version announcement in a format-specific syntax, or both.

 

When the version is indicated both in a media-type parameter and in syntax, they are expected to be the same. If they differ, parsers use the version from the media-type parameter and might emit a warning about the mismatch.

 

To retain compability that is as broad as possible with older parsers, only RDF documents that make use of RDF 1.2-specific functionality are encouraged to announce their version (i.e., for RDF documents that do not make use of RDF 1.2-specific functionality it is discouraged to announce a version).

 

To announce the version in the HTTP responses using the `Content-Type` header, the server is expected to use the `version` parameter, as illustrated in the following example response.

 

```
HTTP/1.1 200 OK
Content-Type: text/turtle; version=1.2
Location: http://example.com/document.ttl
```

 

Servers are also expected to announce the version in-line, when the format supports in-line version announcement (such as [RDF 1.2 Turtle](https://www.w3.org/TR/rdf12-turtle/) [[RDF12-TURTLE](#specification-bib-rdf12-turtle)]).

 

When requesting an RDF document from an HTTP server, a client can use the `version` parameter during 
<a id="specification-ref-for-index-term-content-negotiation-1"></a>
[content negotiation](https://www.w3.org/TR/webarch/#frag-coneg) [[WEBARCH](#specification-bib-webarch)], by including it in the `Accept` request header, as illustrated in the following example request.

 

```
GET /document.ttl HTTP/1.1
Host: example.com
Accept: text/turtle; version=1.2
```

 

 Section [2.1 Version Labels](#specification-defined-version-labels) defines 
<a id="specification-ref-for-dfn-version-label-1"></a>
[version labels](#specification-dfn-version-label) to be used with the `version` parameter and in 
<a id="specification-ref-for-dfn-concrete-rdf-syntax-4"></a>
[concrete RDF syntax](#specification-dfn-concrete-rdf-syntax). 

 
<a id="specification-issue-container-generatedID-1"></a>



<a id="specification-h-note-1"></a>


Note



As HTTP 
<a id="specification-ref-for-index-term-content-negotiation-2"></a>
[content negotiation](https://www.w3.org/TR/webarch/#frag-coneg) is advisory, clients receiving a document should be prepared to properly handle a document of the requested media type but potentially having a `version` other than what was requested. Clients may consider down-grading the content to an appropriate version themselves as discussed in [2.1.1 Server Considerations](#specification-server-considerations).



 

 

 
<a id="specification-conformance"></a>

<a id="specification-L2467"></a>
<a id="specification-x2-conformance"></a>
## 2. Conformance
[](#specification-conformance)



As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.



 The key words MAY, MUST, MUST NOT, RECOMMENDED, SHOULD, and SHOULD NOT in this document are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [[RFC2119](#specification-bib-rfc2119)] [[RFC8174](#specification-bib-rfc8174)] when, and only when, they appear in all capitals, as shown here. 

 

This specification, RDF 1.2 Concepts and Abstract Data Model, defines an abstract data model and related vocabulary for use in other specifications, such as 
<a id="specification-ref-for-dfn-concrete-rdf-syntax-5"></a>
[concrete RDF syntaxes](#specification-dfn-concrete-rdf-syntax), API specifications, and query languages. Implementations cannot directly conform to RDF 1.2 Concepts and Abstract Data Model, but can conform to such other specifications that normatively reference terms defined here.

 

This specification establishes two conformance levels:

 

 

- 
<a id="specification-dfn-full"></a>
Full conformance supports 
<a id="specification-ref-for-dfn-rdf-graph-24"></a>
[graphs](#specification-dfn-rdf-graph) and 
<a id="specification-ref-for-dfn-rdf-dataset-7"></a>
[datasets](#specification-dfn-rdf-dataset) with 
<a id="specification-ref-for-dfn-rdf-triple-13"></a>
[triples](#specification-dfn-rdf-triple) that contain 
<a id="specification-ref-for-dfn-triple-term-13"></a>
[triple terms](#specification-dfn-triple-term). 

 

- 
<a id="specification-dfn-basic"></a>
Basic conformance only supports 
<a id="specification-ref-for-dfn-rdf-graph-25"></a>
[graphs](#specification-dfn-rdf-graph) and/or 
<a id="specification-ref-for-dfn-rdf-dataset-8"></a>
[datasets](#specification-dfn-rdf-dataset) with 
<a id="specification-ref-for-dfn-rdf-triple-14"></a>
[triples](#specification-dfn-rdf-triple) that only contain 
<a id="specification-ref-for-dfn-basic-rdf-term-1"></a>
[basic RDF terms](#specification-dfn-basic-rdf-term) — i.e., they do not contain 
<a id="specification-ref-for-dfn-triple-term-14"></a>
[triple terms](#specification-dfn-triple-term).

 

 
<a id="specification-defined-version-labels"></a>

<a id="specification-L2498"></a>
<a id="specification-x2-1-version-labels"></a>
### 2.1 Version Labels
[](#specification-defined-version-labels)

 

 A 
<a id="specification-dfn-version-label"></a>
version label is a string that identifies the syntax and semantics conformance for the RDF data. 

 
<a id="specification-tab-version-labels"></a>


- Version Labels
- Version Label | Syntax | Semantics
- "1.2" | RDF 1.2 syntax | [RDF 1.2 Semantics](https://www.w3.org/TR/rdf12-semantics/)
- "1.2-basic" | RDF 1.2 syntax without triple terms | [RDF 1.2 Semantics](https://www.w3.org/TR/rdf12-semantics/)
- "1.1" | RDF 1.1 syntax except for use of a version directive | [RDF 1.1 Semantics](https://www.w3.org/TR/rdf11-semantics/)

 

 Data conforming to version "1.1" is valid as data with version "1.2-basic", and data conforming to version "1.2-basic" is valid as data with version "1.2". Data conforming to version "1.1" has the same semantics under [RDF 1.1 Semantics](https://www.w3.org/TR/rdf11-mt/) and under [RDF 1.2 Semantics](https://www.w3.org/TR/rdf12-semantics/). 

 

 See [RDF 1.2 Interoperability](https://www.w3.org/TR/rdf12-interop/) for details of encoding "1.2" as "1.2-basic". 

 

 For serializations supporting in-line version announcement, the version announcement SHOULD be made early in the document and certainly before serializing any feature depending on that version. 

 
<a id="specification-server-considerations"></a>

<a id="specification-L2549"></a>
<a id="specification-x2-1-1-server-considerations"></a>
#### 2.1.1 Server Considerations
[](#specification-server-considerations)



This section is non-normative.

 

When serializing a graph or dataset which uses features incompatible with a requested version, servers can consider different alternatives:

 

 

1. Eliminate 
<a id="specification-ref-for-dfn-triple-term-15"></a>
[triple terms](#specification-dfn-triple-term) by using an algorithm such as basic encoding as defined in [RDF 1.2 Interoperability](https://www.w3.org/TR/rdf12-interop/) (downgrading from version "1.2" to "1.2-basic"). 

 

2. Replace 
<a id="specification-ref-for-dfn-dir-lang-string-3"></a>
[directional language-tagged strings](#specification-dfn-dir-lang-string) by 
<a id="specification-ref-for-dfn-literal-6"></a>
[literals](#specification-dfn-literal) with a 
<a id="specification-ref-for-dfn-datatype-iri-1"></a>
[datatype IRI](#specification-dfn-datatype-iri) that uses the 
<a id="specification-ref-for-index-term-i18n-namespace-1"></a>
[`i18n` namespace](https://www.w3.org/TR/json-ld11/#the-i18n-namespace), as defined in [[JSON-LD11](#specification-bib-json-ld11)] (downgrading from version "1.2" or "1.2-basic" to "1.1").

 

3. Return `406 "Not Acceptable"`.

 

4. Ignore the requested version and return a native representation.

 

 
<a id="specification-issue-container-generatedID-2"></a>



<a id="specification-h-note-2"></a>


Note



The suggestion here is to follow the [Robustness principle](https://en.wikipedia.org/wiki/Robustness_principle) (also known as Postel's Law): servers should be conservative in what they send, be liberal in what they accept.



 

 
<a id="specification-client-considerations"></a>

<a id="specification-L2572"></a>
<a id="specification-x2-1-2-client-considerations"></a>
#### 2.1.2 Client Considerations
[](#specification-client-considerations)



This section is non-normative.

 

If a document has no stated `version` (either by HTTP header or internal), systems can assume the version is `"1.2"`, which continues to support all prior RDF versions.

 

When parsing a document with conflicting versions, or when parsing a document using unsupported versions, a parser may do any of the following:

 

 

- Ignore the version directive.

 

- Raise an error and abort.

 

- Issue a warning and ignore the triple.

 

- Parse the structure and only emit triples consistent with the declared version.

 

 

 

 
<a id="specification-rdf-strings"></a>

<a id="specification-L2589"></a>
<a id="specification-x2-2-strings-in-rdf"></a>
### 2.2 Strings in RDF
[](#specification-rdf-strings)

 

RDF uses Unicode [[Unicode](#specification-bib-unicode)] as the fundamental representation for string values. Within this and related specifications, the term 
<a id="specification-dfn-rdf-string"></a>
RDF string, or simply 
<a id="specification-ref-for-dfn-rdf-string-1"></a>
[string](#specification-dfn-rdf-string), is used to describe an ordered sequence of zero or more 
<a id="specification-ref-for-index-term-unicode-code-points-1"></a>
[Unicode code points](https://www.w3.org/TR/i18n-glossary/#dfn-code-point) which are 
<a id="specification-ref-for-index-term-unicode-scalar-values-1"></a>
[Unicode scalar values](https://www.w3.org/TR/i18n-glossary/#dfn-scalar-value). Unicode scalar values do not include the 
<a id="specification-ref-for-index-term-surrogate-code-points-1"></a>
[surrogate code points](https://www.w3.org/TR/i18n-glossary/#dfn-surrogate). Note that most 
<a id="specification-ref-for-dfn-concrete-rdf-syntax-6"></a>
[concrete RDF syntaxes](#specification-dfn-concrete-rdf-syntax) require the use of the UTF-8 character encoding [[RFC3629](#specification-bib-rfc3629)], and use the `\u0000` or `\U00000000` forms to express certain non-character values. 

 

A string is identical to another string if it consists of the same sequence of code points. An implementation MAY determine string equality by comparing the 
<a id="specification-ref-for-index-term-code-units-1"></a>
[code units](https://www.w3.org/TR/i18n-glossary/#dfn-code-unit) of two strings that use the same 
<a id="specification-ref-for-index-term-unicode-character-encoding-1"></a>
[Unicode character encoding](https://www.w3.org/TR/i18n-glossary/#dfn-character-encoding) (UTF-8 or UTF-16) without decoding the string into a 
<a id="specification-ref-for-index-term-unicode-code-points-2"></a>
[Unicode code point](https://www.w3.org/TR/i18n-glossary/#dfn-code-point) sequence.

 

 

 
<a id="specification-section-rdf-graph"></a>

<a id="specification-L2614"></a>
<a id="specification-x3-rdf-graphs"></a>
## 3. RDF Graphs
[](#specification-section-rdf-graph)

 

An 
<a id="specification-dfn-rdf-graph"></a>
RDF graph is a set of 
<a id="specification-ref-for-dfn-rdf-triple-15"></a>
[RDF triples](#specification-dfn-rdf-triple).

 

An 
<a id="specification-ref-for-dfn-rdf-triple-16"></a>
[RDF triple](#specification-dfn-rdf-triple) that is an element of an 
<a id="specification-ref-for-dfn-rdf-graph-26"></a>
[RDF graph](#specification-dfn-rdf-graph) is also said to be 
<a id="specification-dfn-asserted-triple"></a>
asserted in that 
<a id="specification-ref-for-dfn-rdf-graph-27"></a>
[RDF graph](#specification-dfn-rdf-graph). 

 
<a id="specification-section-triples"></a>

<a id="specification-L2622"></a>
<a id="specification-x3-1-triples"></a>
### 3.1 Triples
[](#specification-section-triples)

 

An 
<a id="specification-dfn-rdf-triple"></a>
RDF triple (often simply called "triple") is a 3-tuple that is defined inductively as follows:

 

 

-  If s is an 
<a id="specification-ref-for-dfn-iri-19"></a>
[IRI](#specification-dfn-iri) or a 
<a id="specification-ref-for-dfn-blank-node-6"></a>
[blank node](#specification-dfn-blank-node), p is an 
<a id="specification-ref-for-dfn-iri-20"></a>
[IRI](#specification-dfn-iri), and o is an 
<a id="specification-ref-for-dfn-iri-21"></a>
[IRI](#specification-dfn-iri), a 
<a id="specification-ref-for-dfn-blank-node-7"></a>
[blank node](#specification-dfn-blank-node), or a 
<a id="specification-ref-for-dfn-literal-7"></a>
[literal](#specification-dfn-literal), then (s, p, o) is an 
<a id="specification-ref-for-dfn-rdf-triple-17"></a>
[RDF triple](#specification-dfn-rdf-triple). 

 

-  If s is an 
<a id="specification-ref-for-dfn-iri-22"></a>
[IRI](#specification-dfn-iri) or a 
<a id="specification-ref-for-dfn-blank-node-8"></a>
[blank node](#specification-dfn-blank-node), p is an 
<a id="specification-ref-for-dfn-iri-23"></a>
[IRI](#specification-dfn-iri), and o is an 
<a id="specification-ref-for-dfn-rdf-triple-18"></a>
[RDF triple](#specification-dfn-rdf-triple), then (s, p, o) is an 
<a id="specification-ref-for-dfn-rdf-triple-19"></a>
[RDF triple](#specification-dfn-rdf-triple). 

 

 

The three components (s, p, o) of an 
<a id="specification-ref-for-dfn-rdf-triple-20"></a>
[RDF triple](#specification-dfn-rdf-triple) are respectively called the 
<a id="specification-dfn-subject"></a>
subject, 
<a id="specification-dfn-predicate"></a>
predicate and 
<a id="specification-dfn-object"></a>
object of the triple.

 
<a id="specification-issue-container-generatedID-3"></a>



<a id="specification-h-note-3"></a>


Note



The definition of 
<a id="specification-ref-for-dfn-rdf-triple-21"></a>
[triple](#specification-dfn-rdf-triple) is recursive. That is, a 
<a id="specification-ref-for-dfn-rdf-triple-22"></a>
[triple](#specification-dfn-rdf-triple) can itself have an 
<a id="specification-ref-for-dfn-object-6"></a>
[object](#specification-dfn-object) component which is another 
<a id="specification-ref-for-dfn-rdf-triple-23"></a>
[triple](#specification-dfn-rdf-triple). However, by this definition, cycles of 
<a id="specification-ref-for-dfn-rdf-triple-24"></a>
[triples](#specification-dfn-rdf-triple) cannot be created.



 

The set of 
<a id="specification-dfn-rdf-node"></a>

<a id="specification-dfn-nodes"></a>

<a id="specification-dfn-node"></a>
nodes of an 
<a id="specification-ref-for-dfn-rdf-graph-28"></a>
[RDF graph](#specification-dfn-rdf-graph) is the set of 
<a id="specification-ref-for-dfn-subject-6"></a>
[subjects](#specification-dfn-subject) and 
<a id="specification-ref-for-dfn-object-7"></a>
[objects](#specification-dfn-object) of the 
<a id="specification-ref-for-dfn-asserted-triple-8"></a>
[asserted triples](#specification-dfn-asserted-triple) of the graph. It is possible for a 
<a id="specification-ref-for-dfn-predicate-5"></a>
[predicate](#specification-dfn-predicate) 
<a id="specification-ref-for-dfn-iri-24"></a>
[IRI](#specification-dfn-iri) to also occur as a 
<a id="specification-ref-for-dfn-node-2"></a>
[node](#specification-dfn-node) in the same graph.

 


<a id="specification-dfn-triple-equality"></a>
Triple equality: Two triples (s, p, o) and (s', p', o') are equal (the same 
<a id="specification-ref-for-dfn-rdf-triple-25"></a>
[RDF triple](#specification-dfn-rdf-triple)) if and only if all of the following three conditions hold.

 

 

- s and s' are 
<a id="specification-ref-for-dfn-rdf-term-equality-1"></a>
[equal](#specification-dfn-rdf-term-equality).

 

- p and p' are 
<a id="specification-ref-for-dfn-rdf-term-equality-2"></a>
[equal](#specification-dfn-rdf-term-equality).

 

- o and o' are 
<a id="specification-ref-for-dfn-rdf-term-equality-3"></a>
[equal](#specification-dfn-rdf-term-equality).

 

 

 
<a id="specification-section-terms"></a>

<a id="specification-L2669"></a>
<a id="specification-x3-2-rdf-terms"></a>
### 3.2 RDF Terms
[](#specification-section-terms)

 


<a id="specification-ref-for-dfn-iri-25"></a>
[IRIs](#specification-dfn-iri), 
<a id="specification-ref-for-dfn-literal-8"></a>
[literals](#specification-dfn-literal), 
<a id="specification-ref-for-dfn-blank-node-9"></a>
[blank nodes](#specification-dfn-blank-node), and 
<a id="specification-ref-for-dfn-triple-term-16"></a>
[triple terms](#specification-dfn-triple-term) are collectively known as 
<a id="specification-dfn-rdf-terms"></a>

<a id="specification-dfn-rdf-term"></a>
RDF terms.

 

 
<a id="specification-ref-for-dfn-iri-26"></a>
[IRIs](#specification-dfn-iri), 
<a id="specification-ref-for-dfn-literal-9"></a>
[literals](#specification-dfn-literal) and 
<a id="specification-ref-for-dfn-blank-node-10"></a>
[blank nodes](#specification-dfn-blank-node) are said to be 
<a id="specification-dfn-basic-rdf-term"></a>
basic RDF terms. 

 


<a id="specification-dfn-rdf-term-equality"></a>
RDF term equality: Two 
<a id="specification-ref-for-dfn-rdf-term-3"></a>
[RDF terms](#specification-dfn-rdf-term) t and t' are equal (the same 
<a id="specification-ref-for-dfn-rdf-term-4"></a>
[RDF term](#specification-dfn-rdf-term)) if and only if one of the following four conditions holds:

 

 

- t and t' are 
<a id="specification-ref-for-dfn-iri-27"></a>
[IRIs](#specification-dfn-iri) that are 
<a id="specification-ref-for-dfn-iri-equality-1"></a>
[equal](#specification-dfn-iri-equality) (per 
<a id="specification-ref-for-dfn-iri-equality-2"></a>
[IRI equality](#specification-dfn-iri-equality)).

 

- t and t' are 
<a id="specification-ref-for-dfn-literal-10"></a>
[literals](#specification-dfn-literal) that are 
<a id="specification-ref-for-dfn-literal-term-equality-1"></a>
[equal](#specification-dfn-literal-term-equality) (per 
<a id="specification-ref-for-dfn-literal-term-equality-2"></a>
[literal term equality](#specification-dfn-literal-term-equality)).

 

- t and t' are 
<a id="specification-ref-for-dfn-blank-node-11"></a>
[blank nodes](#specification-dfn-blank-node) that are 
<a id="specification-ref-for-dfn-blank-node-equality-1"></a>
[equal](#specification-dfn-blank-node-equality) (per 
<a id="specification-ref-for-dfn-blank-node-equality-2"></a>
[blank node equality](#specification-dfn-blank-node-equality)).

 

- t and t' are 
<a id="specification-ref-for-dfn-triple-term-17"></a>
[triple terms](#specification-dfn-triple-term) that are 
<a id="specification-ref-for-dfn-triple-equality-1"></a>
[equal](#specification-dfn-triple-equality) (per 
<a id="specification-ref-for-dfn-triple-equality-2"></a>
[triple equality](#specification-dfn-triple-equality)).

 

 
<a id="specification-issue-container-generatedID-4"></a>



<a id="specification-h-note-4"></a>


Note

 From the above definition of RDF term equality, it follows that terms of different kinds (
<a id="specification-ref-for-dfn-iri-28"></a>
[IRI](#specification-dfn-iri), 
<a id="specification-ref-for-dfn-literal-11"></a>
[literal](#specification-dfn-literal), 
<a id="specification-ref-for-dfn-blank-node-12"></a>
[blank node](#specification-dfn-blank-node), or 
<a id="specification-ref-for-dfn-triple-term-18"></a>
[triple term](#specification-dfn-triple-term)) are always distinguishable, even if they are otherwise based on the same 
<a id="specification-ref-for-dfn-rdf-string-2"></a>
[string](#specification-dfn-rdf-string). For example, the IRI `http://example.org/` is not equal to a literal whose 
<a id="specification-ref-for-dfn-lexical-form-1"></a>
[lexical form](#specification-dfn-lexical-form) is `http://example.org/`. 

 

The set of 
<a id="specification-ref-for-dfn-rdf-term-5"></a>
[RDF terms](#specification-dfn-rdf-term) 
<a id="specification-dfn-appear"></a>
appearing in an 
<a id="specification-ref-for-dfn-rdf-triple-26"></a>
[RDF triple](#specification-dfn-rdf-triple) t is defined inductively as follows:

 

 

- The 
<a id="specification-ref-for-dfn-subject-7"></a>
[subject](#specification-dfn-subject), 
<a id="specification-ref-for-dfn-predicate-6"></a>
[predicate](#specification-dfn-predicate) and 
<a id="specification-ref-for-dfn-object-8"></a>
[object](#specification-dfn-object) of t 
<a id="specification-ref-for-dfn-appear-2"></a>
[appear](#specification-dfn-appear) in t. 



- If the 
<a id="specification-ref-for-dfn-object-9"></a>
[object](#specification-dfn-object) of t is an 
<a id="specification-ref-for-dfn-rdf-triple-27"></a>
[RDF triple](#specification-dfn-rdf-triple) t2, then any 
<a id="specification-ref-for-dfn-rdf-term-6"></a>
[RDF term](#specification-dfn-rdf-term) 
<a id="specification-ref-for-dfn-appear-3"></a>
[appearing](#specification-dfn-appear) in t2 also 
<a id="specification-ref-for-dfn-appear-4"></a>
[appears](#specification-dfn-appear) in t. 



 

By extension, an 
<a id="specification-ref-for-dfn-rdf-term-7"></a>
[RDF term](#specification-dfn-rdf-term) is said to 
<a id="specification-ref-for-dfn-appear-5"></a>
[appear](#specification-dfn-appear) in an 
<a id="specification-ref-for-dfn-rdf-graph-29"></a>
[RDF graph](#specification-dfn-rdf-graph) if it appears in an 
<a id="specification-ref-for-dfn-asserted-triple-9"></a>
[asserted triple](#specification-dfn-asserted-triple) of that graph. An 
<a id="specification-ref-for-dfn-rdf-triple-28"></a>
[RDF triple](#specification-dfn-rdf-triple) is said to 
<a id="specification-ref-for-dfn-appear-6"></a>
[appear](#specification-dfn-appear) in an 
<a id="specification-ref-for-dfn-rdf-graph-30"></a>
[RDF graph](#specification-dfn-rdf-graph) if it is either an 
<a id="specification-ref-for-dfn-asserted-triple-10"></a>
[asserted triple](#specification-dfn-asserted-triple) of that graph or a 
<a id="specification-ref-for-dfn-triple-term-19"></a>
[triple term](#specification-dfn-triple-term) 
<a id="specification-ref-for-dfn-appear-7"></a>
[appearing](#specification-dfn-appear) in that graph.

 

 An 
<a id="specification-ref-for-dfn-rdf-term-8"></a>
[RDF term](#specification-dfn-rdf-term) is said to be 
<a id="specification-dfn-ground"></a>
ground if any of the following three conditions holds: 

 

 

- It is an 
<a id="specification-ref-for-dfn-iri-29"></a>
[IRI](#specification-dfn-iri).

 

- It is a 
<a id="specification-ref-for-dfn-literal-12"></a>
[literal](#specification-dfn-literal).

 

- It is a 
<a id="specification-ref-for-dfn-triple-term-20"></a>
[triple term](#specification-dfn-triple-term) (s, p, o) such that s, p, and o are all 
<a id="specification-ref-for-dfn-ground-1"></a>
[ground](#specification-dfn-ground).

 

 

 By extension, an 
<a id="specification-ref-for-dfn-rdf-triple-29"></a>
[RDF triple](#specification-dfn-rdf-triple) is said to be 
<a id="specification-ref-for-dfn-ground-2"></a>
[ground](#specification-dfn-ground) if its 
<a id="specification-ref-for-dfn-subject-8"></a>
[subject](#specification-dfn-subject), 
<a id="specification-ref-for-dfn-predicate-7"></a>
[predicate](#specification-dfn-predicate), and 
<a id="specification-ref-for-dfn-object-10"></a>
[object](#specification-dfn-object) are all ground. An 
<a id="specification-ref-for-dfn-rdf-graph-31"></a>
[RDF graph](#specification-dfn-rdf-graph) is said to be 
<a id="specification-ref-for-dfn-ground-3"></a>
[ground](#specification-dfn-ground) if all its 
<a id="specification-ref-for-dfn-asserted-triple-11"></a>
[asserted](#specification-dfn-asserted-triple) triples are 
<a id="specification-ref-for-dfn-ground-4"></a>
[ground](#specification-dfn-ground). 

 

 
<a id="specification-section-IRIs"></a>

<a id="specification-L2727"></a>
<a id="specification-x3-3-iris"></a>
### 3.3 IRIs
[](#specification-section-IRIs)

 

An 
<a id="specification-dfn-iri"></a>
IRI (Internationalized Resource Identifier) within an RDF graph is a 
<a id="specification-ref-for-dfn-rdf-string-3"></a>
[string](#specification-dfn-rdf-string) that conforms to the syntax defined in RFC 3987 [[RFC3987](#specification-bib-rfc3987)].

 

An IRI in the RDF 
<a id="specification-ref-for-dfn-abstract-syntax-2"></a>
[abstract syntax](#specification-dfn-abstract-syntax) MUST be 
<a id="specification-ref-for-index-term-resolved-1"></a>
[resolved](https://www.rfc-editor.org/rfc/rfc3986#section-5) per [[RFC3986](#specification-bib-rfc3986)] and MUST NOT be a 
<a id="specification-ref-for-index-term-relative-reference-1"></a>
[relative reference](https://www.rfc-editor.org/rfc/rfc3986#section-4.2). An IRI MAY contain a 
<a id="specification-ref-for-index-term-fragment-identifier-1"></a>
[fragment identifier](https://www.rfc-editor.org/rfc/rfc3986#section-3.5). An IRI SHOULD follow rules defined by the 
<a id="specification-ref-for-index-term-iri-scheme-1"></a>
[IRI scheme](https://www.rfc-editor.org/rfc/rfc3986#section-3.1). 

 


<a id="specification-dfn-iri-equality"></a>
IRI equality: Two IRIs are equal if and only if they consist of the same sequence of 
<a id="specification-ref-for-index-term-unicode-code-points-3"></a>
[Unicode code points](https://www.w3.org/TR/i18n-glossary/#dfn-code-point), as in Simple String Comparison in 
<a id="specification-ref-for-index-term-section-5-3-1-1"></a>
[section 5.3.1](https://www.rfc-editor.org/rfc/rfc3987#section-5.3.1) of [[RFC3987](#specification-bib-rfc3987)]. (This is done in the abstract syntax, so the IRIs are resolved IRIs with no escaping or encoding.) Further normalization MUST NOT be performed before this comparison. 

 
<a id="specification-issue-container-generatedID-5"></a>



<a id="specification-h-note-5"></a>


Note



For convenience, a complete [[ABNF](#specification-bib-abnf)] grammar from [[RFC3987](#specification-bib-rfc3987)] is provided in [F. IRI Grammar](#specification-iri-abnf).



 
<a id="specification-issue-container-generatedID-6"></a>



<a id="specification-h-note-6"></a>


Note



 

URIs and IRIs: IRIs are a generalization of 
<a id="specification-dfn-uri"></a>
URIs [[RFC3986](#specification-bib-rfc3986)] that permits a wider range of Unicode characters [[UNICODE](#specification-bib-unicode)]. Every URI and URL is an IRI, but not every IRI is an URI. In RDF, IRIs are used as 
<a id="specification-dfn-iri-reference"></a>
IRI references, as defined in [[RFC3987](#specification-bib-rfc3987)] 
<a id="specification-ref-for-index-term-section-1-3-1"></a>
[section 1.3](https://www.rfc-editor.org/rfc/rfc3987#section-1.3). An IRI reference is common usage of an Internationalized Resource Identifier. An IRI reference refers to either a resolved 
<a id="specification-ref-for-dfn-iri-30"></a>
[IRI](#specification-dfn-iri) or 
<a id="specification-ref-for-dfn-relative-iri-1"></a>
[relative IRI reference](#specification-dfn-relative-iri), as described by the IRI-reference production in [F. IRI Grammar](#specification-iri-abnf). The abstract syntax uses only fully resolved 
<a id="specification-ref-for-dfn-iri-31"></a>
[IRIs](#specification-dfn-iri). When IRIs are used in operations that are only defined for URIs, they must first be converted according to the mapping defined in 
<a id="specification-ref-for-index-term-section-3-1-1"></a>
[section 3.1](https://www.rfc-editor.org/rfc/rfc3987#section-3.1) of [[RFC3987](#specification-bib-rfc3987)]. A notable example is retrieval over the HTTP protocol. The mapping involves UTF-8 encoding of non-ASCII characters, %-encoding of octets not allowed in URIs, and Punycode-encoding of domain names.

 

URLs: The [URL Standard](https://url.spec.whatwg.org/) is largely compatible with [[RFC3987](#specification-bib-rfc3987)] IRIs, but is based on a processing model important for implementation within web browsers and are not described using an [[ABNF](#specification-bib-abnf)] grammar. 

 



 
<a id="specification-reference-iris"></a>

<a id="specification-L2782"></a>
<a id="specification-x3-3-1-rdf-reference-iris"></a>
#### 3.3.1 RDF Reference IRIs
[](#specification-reference-iris)



This section is non-normative.

 

 This section provides advice to data publishers. 

 

 
<a id="specification-ref-for-dfn-iri-32"></a>
[IRIs](#specification-dfn-iri) are used to denote 
<a id="specification-ref-for-dfn-resource-8"></a>
[resources](#specification-dfn-resource), and each IRI should identify the same resource regardless of where that IRI is used. Note that the general syntax for IRIs, defined by [[RFC3987](#specification-bib-rfc3987)], can express IRIs which do not meet the requirement of being a global reference. Some URI schemes add additional requirements; for example, the 
<a id="specification-ref-for-index-term-http-uri-scheme-1"></a>
[HTTP URI scheme](https://httpwg.org/specs/rfc7230.html#section-2.7.1) defines 
<a id="specification-ref-for-index-term-http-uri-1"></a>
[`http-URI`](https://httpwg.org/specs/rfc7230.html#http-URI), which requires the presence of a non-empty host name, and, as a consequence, the path component will start with `/`. The [[RFC3987](#specification-bib-rfc3987)] syntax permits IRIs such as `http:abcd` and `http:///abcd`, but these are invalid because they do not satisfy the HTTP URI scheme definition. 

 

 An 
<a id="specification-dfn-rdf-reference"></a>
RDF Reference IRI, sometimes called simply 
<a id="specification-ref-for-dfn-rdf-reference-1"></a>
[RDF Reference](#specification-dfn-rdf-reference), is an 
<a id="specification-ref-for-dfn-iri-33"></a>
[IRI](#specification-dfn-iri) that is suitable for use as a global reference. 

 

 Reference Resolution: An 
<a id="specification-ref-for-dfn-rdf-reference-2"></a>
[RDF Reference IRI](#specification-dfn-rdf-reference) is unchanged by 
<a id="specification-ref-for-index-term-resolved-2"></a>
[reference resolution](https://www.rfc-editor.org/rfc/rfc3986#section-5). In URI schemes such as `http` and `https`, the 
<a id="specification-ref-for-index-term-path-component-1"></a>
[path component](https://www.rfc-editor.org/rfc/rfc3986#section-3.3) is part of the hierarchy visible to the resolution algorithm. When resolved, the 
<a id="specification-ref-for-index-term-path-component-2"></a>
[path component](https://www.rfc-editor.org/rfc/rfc3986#section-3.3) starts with a `/` character and does not contain `.` or `..` segments. For example, `https://example/data` resolved against any base IRI is `https://example/data` (unchanged), whereas `https://example/path/../data` resolved against an arbitrary base IRI is `https://example.com/data`. 

 

 Relative IRI references: Some 
<a id="specification-ref-for-dfn-concrete-rdf-syntax-7"></a>
[concrete RDF syntaxes](#specification-dfn-concrete-rdf-syntax) permit 
<a id="specification-dfn-relative-iris"></a>
 
<a id="specification-dfn-relative-iri"></a>
relative IRI references (see the `irelative-ref` production in the [IRI Grammar](#specification-iri-abnf)) as a convenient shorthand that allows RDF documents to be authored without knowing their final publishing location. Relative IRI references must be 
<a id="specification-ref-for-index-term-resolved-against-1"></a>
[resolved against](https://www.rfc-editor.org/rfc/rfc3986#section-5.2) a 
<a id="specification-dfn-base-iri"></a>
base IRI. Therefore, the RDF graph serialized in such syntaxes is well-defined only if a 
<a id="specification-ref-for-index-term-base-iri-can-be-established-1"></a>
[base IRI can be established](https://www.rfc-editor.org/rfc/rfc3986#section-5.1) [[RFC3986](#specification-bib-rfc3986)]. 

 

 URI Schemes: Implementations are encouraged to follow the scheme-specific rules of the common schemes, such as the 
<a id="specification-ref-for-index-term-scheme-rules-for-http-https-1"></a>
[scheme rules for HTTP/HTTPS](https://httpwg.org/specs/rfc7230.html#section-2.7) and the 
<a id="specification-ref-for-index-term-did-syntax-1"></a>
[DID syntax](https://www.w3.org/TR/did-core/#identifier). Implementations ignore URI scheme rules for schemes they do not recognize. 

 

 IRI normalization: Interoperability problems can be avoided by minting only IRIs that are normalized according to 
<a id="specification-ref-for-index-term-section-5-1"></a>
[Section 5](https://www.rfc-editor.org/rfc/rfc3987#section-5) of [[RFC3987](#specification-bib-rfc3987)]. 

 

 

- Use lowercase characters in scheme names.

 

- Only use percent-encoding of characters where required by the IRI syntax.

 

- Omit the HTTP or HTTPS default port; `http://example/` is preferred over `http://example:80/`.

 

- Use uppercase hexadecimal letters within percent-encoding triplets;"`%3F`" is preferred over "`%3f`".

 

- An empty path in an HTTP IRI `http://example/` is preferred over having no path `http://example`.

 

- Normalize IRIs to remove "`/./`" and "`/../`" in the path component of an IRI.

 

- Use lowercase characters in domain names. Note that, while ASCII characters in domain names are case-insensitive, non-ASCII characters in domain names are case-sensitive [[RFC5890](#specification-bib-rfc5890)]. Domains are generally only registered with lowercase letters [[RFC5892](#specification-bib-rfc5892)].

 

- Avoid using the [A-label](https://datatracker.ietf.org/doc/html/rfc5890#section-2.3.2.1) (ASCII, punycode-encoded name]) for Internationalized Domain Names [[RFC5890](#specification-bib-rfc5890)] in IRIs.

 

- Use IRIs in Unicode 
<a id="specification-ref-for-index-term-normalization-form-c-1"></a>
[Normalization Form C](https://www.w3.org/TR/i18n-glossary/#dfn-unicode-normalization-form-c) [[I18N-Glossary](#specification-bib-i18n-glossary)].

 

 

 

 
<a id="specification-section-Graph-Literal"></a>

<a id="specification-L2874"></a>
<a id="specification-x3-4-literals"></a>
### 3.4 Literals
[](#specification-section-Graph-Literal)

 

Literals are used for values such as strings, numbers, and dates.

 

A 
<a id="specification-dfn-rdf-literal"></a>

<a id="specification-dfn-literal"></a>
literal consists of two, three, or four components, as below:

 

 

1. A 
<a id="specification-dfn-lexical-form"></a>
lexical form, being an 
<a id="specification-ref-for-dfn-rdf-string-4"></a>
[RDF string](#specification-dfn-rdf-string).

 

2. A 
<a id="specification-dfn-datatype-iri"></a>
datatype IRI, being an 
<a id="specification-ref-for-dfn-iri-34"></a>
[IRI](#specification-dfn-iri) identifying a datatype that determines how the lexical form maps to a 
<a id="specification-ref-for-dfn-literal-value-3"></a>
[literal value](#specification-dfn-literal-value).

 

3. If and only if the 
<a id="specification-ref-for-dfn-datatype-iri-2"></a>
[datatype IRI](#specification-dfn-datatype-iri) is `http://www.w3.org/1999/02/22-rdf-syntax-ns#langString` or `http://www.w3.org/1999/02/22-rdf-syntax-ns#dirLangString`, there is a non-empty 
<a id="specification-dfn-language-tag"></a>
language tag as defined by [[BCP47](#specification-bib-bcp47)]. The language tag MUST be well-formed according to 
<a id="specification-ref-for-index-term-section-2-2-9-1"></a>
[section 2.2.9](https://www.rfc-editor.org/rfc/rfc5646#section-2.2.9) of [[BCP47](#specification-bib-bcp47)], and MUST be treated accordingly, that is, in a case-insensitive manner. Two [[BCP47](#specification-bib-bcp47)]-complying strings that differ only by case represent the same 
<a id="specification-ref-for-dfn-language-tag-1"></a>
[language tag](#specification-dfn-language-tag).

 

4. If and only if the 
<a id="specification-ref-for-dfn-datatype-iri-3"></a>
[datatype IRI](#specification-dfn-datatype-iri) is `http://www.w3.org/1999/02/22-rdf-syntax-ns#dirLangString`, there is a 
<a id="specification-dfn-base-direction"></a>
base direction that MUST be one of the following:

 

  - `ltr`, indicating that the initial text direction is set to left-to-right

 

  - `rtl`, indicating that the initial text direction is set to right-to-left

 



 

 

A literal is a 
<a id="specification-dfn-language-tagged-string"></a>
language-tagged string if the 
<a id="specification-ref-for-dfn-language-tag-2"></a>
[language tag](#specification-dfn-language-tag) is present and the 
<a id="specification-ref-for-dfn-base-direction-2"></a>
[base direction](#specification-dfn-base-direction) is not present. A literal is a 
<a id="specification-dfn-dir-lang-string"></a>
directional language-tagged string if both the 
<a id="specification-ref-for-dfn-language-tag-3"></a>
[language tag](#specification-dfn-language-tag) and the 
<a id="specification-ref-for-dfn-base-direction-3"></a>
[base direction](#specification-dfn-base-direction) are present. 

 


<a id="specification-dfn-literal-term-equality"></a>
Literal term equality: two literals are term-equal (the same 
<a id="specification-ref-for-dfn-rdf-term-9"></a>
[RDF term](#specification-dfn-rdf-term)) if and only if the following are all true:

 

 

- The two 
<a id="specification-ref-for-dfn-lexical-form-2"></a>
[lexical forms](#specification-dfn-lexical-form) compare equal, where this comparison is performed using 
<a id="specification-ref-for-index-term-case-sensitive-matching-1"></a>
[case-sensitive matching](https://www.w3.org/TR/i18n-glossary/#dfn-case-sensitive) (see description of string comparison in [2.2 Strings in RDF](#specification-rdf-strings)).

 

- The two 
<a id="specification-ref-for-dfn-datatype-iri-4"></a>
[datatype IRIs](#specification-dfn-datatype-iri) compare 
<a id="specification-ref-for-dfn-iri-equality-3"></a>
[equal](#specification-dfn-iri-equality) (per 
<a id="specification-ref-for-dfn-iri-equality-4"></a>
[IRI equality](#specification-dfn-iri-equality)).

 

- The two 
<a id="specification-ref-for-dfn-language-tag-4"></a>
[language tags](#specification-dfn-language-tag) are either both absent, or both present and compare equal, where this comparison is performed using 
<a id="specification-ref-for-index-term-ascii-case-insensitive-matching-1"></a>
[ASCII case-insensitive matching](https://www.w3.org/TR/i18n-glossary/#dfn-ascii-case-insensitive) (in contrast to the case-sensitive comparison of the lexical forms).

 

- The two 
<a id="specification-ref-for-dfn-base-direction-4"></a>
[base directions](#specification-dfn-base-direction) are either both absent, both `ltr`, or both `rtl`.

 

 
<a id="specification-representation-of-literals"></a>

<a id="specification-L2929"></a>
<a id="specification-x3-4-1-representation-of-literals"></a>
#### 3.4.1 Representation of Literals
[](#specification-representation-of-literals)

 

Some concrete syntaxes support 
<a id="specification-dfn-simple-literal"></a>
simple literals consisting of only a 
<a id="specification-ref-for-dfn-lexical-form-3"></a>
[lexical form](#specification-dfn-lexical-form) without any 
<a id="specification-ref-for-dfn-datatype-iri-5"></a>
[datatype IRI](#specification-dfn-datatype-iri), 
<a id="specification-ref-for-dfn-language-tag-5"></a>
[language tag](#specification-dfn-language-tag), or 
<a id="specification-ref-for-dfn-base-direction-5"></a>
[base direction](#specification-dfn-base-direction). Simple literals are syntactic sugar for 
<a id="specification-ref-for-dfn-abstract-syntax-3"></a>
[abstract syntax](#specification-dfn-abstract-syntax) 
<a id="specification-ref-for-dfn-literal-13"></a>
[literals](#specification-dfn-literal) with the 
<a id="specification-ref-for-dfn-datatype-iri-6"></a>
[datatype IRI](#specification-dfn-datatype-iri) `http://www.w3.org/2001/XMLSchema#string` (which is commonly abbreviated as `xsd:string`). 

 

 Similarly, most concrete syntaxes represent 
<a id="specification-ref-for-dfn-language-tagged-string-2"></a>
[language-tagged strings](#specification-dfn-language-tagged-string) and 
<a id="specification-ref-for-dfn-dir-lang-string-4"></a>
[directional language-tagged strings](#specification-dfn-dir-lang-string) without the 
<a id="specification-ref-for-dfn-datatype-iri-7"></a>
[datatype IRI](#specification-dfn-datatype-iri) because it is always either `http://www.w3.org/1999/02/22-rdf-syntax-ns#langString` (`rdf:langString`) or `http://www.w3.org/1999/02/22-rdf-syntax-ns#dirLangString` (`rdf:dirLangString`), respectively. 

 

 Any 
<a id="specification-ref-for-dfn-rdf-string-5"></a>
[string](#specification-dfn-rdf-string) complying with [[BCP47](#specification-bib-bcp47)] MAY be used to represent a 
<a id="specification-ref-for-dfn-language-tag-6"></a>
[language tag](#specification-dfn-language-tag) in concrete syntaxes or implementations. Such strings MAY be case normalized (for example, by canonicalizing as defined by 
<a id="specification-ref-for-index-term-bcp-47-section-4-5-1"></a>
[BCP 47 section 4.5](https://www.rfc-editor.org/rfc/rfc5646#section-4.5)). Alternatively, an implementation MAY preserve the case from the original representation, provided that it processes it in a case-insensitive manner. 

 
<a id="specification-issue-container-generatedID-7"></a>



<a id="specification-h-note-7"></a>


Note

 The treatment of language tags has changed between RDF 1.1 and RDF 1.2. In RDF 1.1, `"chat"@fr` and `"chat"@FR` represent two distinct terms, but implementations may replace either with the other via some form of normalization. In RDF 1.2, they represent the exact same literal, i.e., the case difference in the concrete syntax does not propagate into the abstract syntax. Since many RDF 1.1 implementations do normalize language tags internally, they will not be impacted by this change. 

 

 
<a id="specification-literal-value"></a>

<a id="specification-L2970"></a>
<a id="specification-x3-4-2-literal-value"></a>
#### 3.4.2 Literal Value
[](#specification-literal-value)

 

The 
<a id="specification-dfn-literal-value"></a>
literal value associated with a 
<a id="specification-ref-for-dfn-literal-14"></a>
[literal](#specification-dfn-literal) is defined as follows.

 

 

- If the literal is a 
<a id="specification-ref-for-dfn-language-tagged-string-3"></a>
[language-tagged string](#specification-dfn-language-tagged-string), then the literal value is a pair consisting of its 
<a id="specification-ref-for-dfn-lexical-form-4"></a>
[lexical form](#specification-dfn-lexical-form) and its 
<a id="specification-ref-for-dfn-language-tag-7"></a>
[language tag](#specification-dfn-language-tag), in that order.

 

- If the literal is a 
<a id="specification-ref-for-dfn-dir-lang-string-5"></a>
[directional language-tagged string](#specification-dfn-dir-lang-string), then the literal value is a tuple of its 
<a id="specification-ref-for-dfn-lexical-form-5"></a>
[lexical form](#specification-dfn-lexical-form), its 
<a id="specification-ref-for-dfn-language-tag-8"></a>
[language tag](#specification-dfn-language-tag), and its 
<a id="specification-ref-for-dfn-base-direction-6"></a>
[base direction](#specification-dfn-base-direction), likewise in that order.

 

- If the literal's 
<a id="specification-ref-for-dfn-datatype-2"></a>
[datatype](#specification-dfn-datatype) is handled by an RDF implementation, then one of the following applies: 

 

  - If the literal's 
<a id="specification-ref-for-dfn-lexical-form-6"></a>
[lexical form](#specification-dfn-lexical-form) is in the 
<a id="specification-ref-for-dfn-lexical-space-1"></a>
[lexical space](#specification-dfn-lexical-space) of the 
<a id="specification-ref-for-dfn-datatype-3"></a>
[datatype](#specification-dfn-datatype), then the literal value is the result of applying the 
<a id="specification-ref-for-dfn-lexical-to-value-mapping-1"></a>
[lexical-to-value mapping](#specification-dfn-lexical-to-value-mapping) of the datatype to the 
<a id="specification-ref-for-dfn-lexical-form-7"></a>
[lexical form](#specification-dfn-lexical-form).

 

  - Otherwise, the literal is 
<a id="specification-dfn-ill-typed"></a>
ill-typed and no literal value can be associated with the literal. Such a case produces a semantic 
<a id="specification-ref-for-dfn-inconsistent-2"></a>
[inconsistency](#specification-dfn-inconsistent), but it is not syntactically ill-formed. Implementations SHOULD accept 
<a id="specification-ref-for-dfn-ill-typed-1"></a>
[ill-typed](#specification-dfn-ill-typed) literals and produce RDF graphs from them. Implementations MAY produce warnings when encountering 
<a id="specification-ref-for-dfn-ill-typed-2"></a>
[ill-typed](#specification-dfn-ill-typed) literals.

 

 

 

- If the literal's 
<a id="specification-ref-for-dfn-datatype-iri-8"></a>
[datatype IRI](#specification-dfn-datatype-iri) is not handled by an RDF implementation, then the literal value is not defined by this specification. Implementations SHOULD accept literals with unknown datatype IRIs and produce RDF graphs from them. 

 

 

 It follows from the above that two literals can have the same value without being the same 
<a id="specification-ref-for-dfn-rdf-term-10"></a>
[RDF term](#specification-dfn-rdf-term). For example:

 

```
"1"^^xsd:integer
"01"^^xsd:integer
```

 

denote the same 
<a id="specification-ref-for-dfn-literal-value-4"></a>
[value](#specification-dfn-literal-value), but are not the same literal 
<a id="specification-ref-for-dfn-rdf-term-11"></a>
[RDF term](#specification-dfn-rdf-term) because their 
<a id="specification-ref-for-dfn-lexical-form-8"></a>
[lexical forms](#specification-dfn-lexical-form) differ.

 

 
<a id="specification-section-text-direction"></a>

<a id="specification-L3016"></a>
<a id="specification-x3-4-3-initial-text-direction"></a>
#### 3.4.3 Initial Text Direction
[](#specification-section-text-direction)



This section is non-normative.

 

The 
<a id="specification-ref-for-dfn-base-direction-7"></a>
[base direction](#specification-dfn-base-direction) of a 
<a id="specification-ref-for-dfn-dir-lang-string-6"></a>
[directional language-tagged string](#specification-dfn-dir-lang-string) provides a means of establishing the initial direction of text, including text which is a mixture of right-to-left and left-to-right scripts. The 
<a id="specification-ref-for-index-term-unicode-bidirectional-algorithm-1"></a>
[Unicode Bidirectional Algorithm](https://www.w3.org/TR/i18n-glossary/#dfn-unicode-bidi-algorithm) [[I18N-Glossary](#specification-bib-i18n-glossary)] provides support for automatically rendering a sequence of characters in logical order, so that they are visually ordered as expected, but this is not always sufficient to correctly render bidirectional text. 



 Consider the Arabic translation of the book title "HTML and CSS: Designing Websites". In a left-to-right context (such as an English web page), with proper 
<a id="specification-ref-for-index-term-bidi-isolation-1"></a>
[bidi isolation](https://www.w3.org/TR/i18n-glossary/#dfn-bidi-isolation) but without an explicit base direction, it would be incorrectly displayed as follows: 

 

HTML و CSS: تصميم مواقع الويب

 

while the correct rendering is as follows:

 

HTML و CSS: تصميم مواقع الويب

 

 That example demonstrates the importance of using 
<a id="specification-ref-for-dfn-dir-lang-string-7"></a>
[directional language-tagged strings](#specification-dfn-dir-lang-string) instead of simple 
<a id="specification-ref-for-dfn-language-tagged-string-4"></a>
[language-tagged strings](#specification-dfn-language-tagged-string) in contexts where bidirectional text can be encountered. 

 

 Note that the language and base direction address string external bidirectional issues, related to correctly displaying the string in context (e.g., avoiding [spillover](https://www.w3.org/TR/i18n-glossary/#dfn-spillover-effects) problems). It does not address directional issues internal to the string, which may occur in more complex examples, such as the following: 

 

"HTML و CSS: تصميم مواقع الويب" is the Arabic title of the book.

 

 A 
<a id="specification-ref-for-dfn-dir-lang-string-8"></a>
[directional language-tagged string](#specification-dfn-dir-lang-string) representing that example will have the language tag `en` and the base direction `ltr`, but also requires specific Unicode bidirectional formatting characters to isolate and mark the text between the quotes as `rtl`. 

 
<a id="specification-issue-container-generatedID-8"></a>



<a id="specification-h-note-8"></a>


Note



 Other datatypes provide their own way to encode language and bidirectional text, e.g., [`rdf:HTML`](#specification-section-html) or [`rdf:XMLLiteral`](#specification-section-XMLLiteral). 



 
<a id="specification-issue-container-generatedID-9"></a>



<a id="specification-h-note-9"></a>


Note



 

For more details, see:

 

 

- [Unicode Bidirectional Algorithm basics](https://www.w3.org/International/articles/inline-bidi-markup/uba-basics)

 

- [Unicode controls vs. markup for bidi support](https://www.w3.org/International/questions/qa-bidi-controls)

 

- [How to use Unicode controls for bidi text](https://www.w3.org/International/questions/qa-bidi-unicode-controls)

 

 



 

 

 
<a id="specification-section-blank-nodes"></a>

<a id="specification-L3075"></a>
<a id="specification-x3-5-blank-nodes"></a>
### 3.5 Blank Nodes
[](#specification-section-blank-nodes)

 


<a id="specification-dfn-blank-node"></a>
Blank nodes are disjoint from 
<a id="specification-ref-for-dfn-iri-35"></a>
[IRIs](#specification-dfn-iri) and 
<a id="specification-ref-for-dfn-literal-15"></a>
[literals](#specification-dfn-literal). Otherwise, the set of possible blank nodes is arbitrary. RDF makes no reference to any internal structure of blank nodes.

 


<a id="specification-dfn-blank-node-equality"></a>
Blank node equality: Two blank nodes are equal if and only if they are the same blank node.

 
<a id="specification-note-bnode-id"></a>



<a id="specification-h-note-10"></a>


Note



 


<a id="specification-dfn-blank-node-identifiers"></a>

<a id="specification-dfn-blank-node-identifier"></a>
Blank node identifiers are local identifiers that are used in some 
<a id="specification-ref-for-dfn-concrete-rdf-syntax-8"></a>
[concrete RDF syntaxes](#specification-dfn-concrete-rdf-syntax) or RDF store implementations. They are always locally scoped to the file or RDF store, and are not persistent or portable identifiers for blank nodes. Blank node identifiers are not part of the RDF abstract data model, but are entirely dependent on the concrete syntax or implementation. The syntactic restrictions on blank node identifiers, if any, therefore also depend on the concrete RDF syntax or implementation. Implementations that handle blank node identifiers in concrete syntaxes need to be careful not to create the same blank node from multiple occurrences of the same blank node identifier except in situations where this is supported by the syntax.

 

The term "blank node label" is sometimes used informally as an alternative to the term 
<a id="specification-ref-for-dfn-blank-node-identifier-2"></a>
[blank node identifier](#specification-dfn-blank-node-identifier). This alternative was also used in earlier versions of some RDF-related specifications such as [[SPARQL11-QUERY](#specification-bib-sparql11-query)]. In the interest of consistency, the use of this alternative term is discouraged now.

 



 

 
<a id="specification-section-triple-terms"></a>

<a id="specification-L3111"></a>
<a id="specification-x3-6-triple-terms"></a>
### 3.6 Triple Terms
[](#specification-section-triple-terms)

 

An 
<a id="specification-ref-for-dfn-rdf-triple-30"></a>
[RDF triple](#specification-dfn-rdf-triple) used as the 
<a id="specification-ref-for-dfn-object-11"></a>
[object](#specification-dfn-object) of another 
<a id="specification-ref-for-dfn-rdf-triple-31"></a>
[triple](#specification-dfn-rdf-triple) is called a 
<a id="specification-dfn-triple-term"></a>
triple term. In a given 
<a id="specification-ref-for-dfn-rdf-graph-32"></a>
[RDF graph](#specification-dfn-rdf-graph), a 
<a id="specification-ref-for-dfn-rdf-triple-32"></a>
[triple](#specification-dfn-rdf-triple) can appear as a 
<a id="specification-ref-for-dfn-triple-term-21"></a>
[triple term](#specification-dfn-triple-term), an 
<a id="specification-ref-for-dfn-asserted-triple-12"></a>
[asserted triple](#specification-dfn-asserted-triple), or both. 

 

Triple term equality: Since triple terms are 
<a id="specification-ref-for-dfn-rdf-triple-33"></a>
[triples](#specification-dfn-rdf-triple), equality of triple terms is the same as 
<a id="specification-ref-for-dfn-triple-equality-3"></a>
[triple equality](#specification-dfn-triple-equality).

 

 
<a id="specification-graph-isomorphism"></a>

<a id="specification-L3123"></a>
<a id="specification-x3-7-graph-comparison"></a>
### 3.7 Graph Comparison
[](#specification-graph-isomorphism)

 

This section introduces a notion of graph isomorphism for 
<a id="specification-ref-for-dfn-rdf-graph-33"></a>
[RDF graphs](#specification-dfn-rdf-graph) which is based on a mapping between 
<a id="specification-ref-for-dfn-rdf-term-12"></a>
[RDF terms](#specification-dfn-rdf-term) that maps blank nodes to blank nodes and is the identity function for IRIs and literals.

 

A function M from the set of all 
<a id="specification-ref-for-dfn-rdf-term-13"></a>
[RDF terms](#specification-dfn-rdf-term) into that same set is called an 
<a id="specification-dfn-isomorphic-rdf-term-mapping"></a>
isomorphic RDF-term mapping if it is has all of the following properties:

 

 

- M is bijective.

 

- For every 
<a id="specification-ref-for-dfn-blank-node-13"></a>
[blank node](#specification-dfn-blank-node) b, M(b) is a 
<a id="specification-ref-for-dfn-blank-node-14"></a>
[blank node](#specification-dfn-blank-node) (but not necessarily the same as b).

 

- For every 
<a id="specification-ref-for-dfn-literal-16"></a>
[literal](#specification-dfn-literal) lit, M(lit) is lit.

 

- For every 
<a id="specification-ref-for-dfn-iri-36"></a>
[IRI](#specification-dfn-iri) iri, M(iri) is iri.

 

- For every 
<a id="specification-ref-for-dfn-triple-term-22"></a>
[triple term](#specification-dfn-triple-term) tt of the form (s, p, o), M(tt) is the triple term ( M(s), M(p), M(o) ).

 

 
<a id="specification-section-graph-equality"></a>


Two 
<a id="specification-ref-for-dfn-rdf-graph-34"></a>
[RDF graphs](#specification-dfn-rdf-graph) G and G' are 
<a id="specification-dfn-graph-isomorphism"></a>
isomorphic (that is, they have the same form) if there exists an 
<a id="specification-ref-for-dfn-isomorphic-rdf-term-mapping-1"></a>
[isomorphic RDF-term mapping](#specification-dfn-isomorphic-rdf-term-mapping) M such that the triple (s, p, o) is in G if and only if the triple ( M(s), M(p), M(o) ) is in G'.

 

With this definition, M shows how each blank node in G can be replaced with a new blank node to give G'. Graph isomorphism is needed to support the RDF Test Cases [[RDF11-TESTCASES](#specification-bib-rdf11-testcases)] specification.

 

 

 
<a id="specification-section-dataset"></a>

<a id="specification-L3160"></a>
<a id="specification-x4-rdf-datasets"></a>
## 4. RDF Datasets
[](#specification-section-dataset)

 

An 
<a id="specification-dfn-rdf-dataset"></a>
RDF dataset is a collection of 
<a id="specification-ref-for-dfn-rdf-graph-35"></a>
[RDF graphs](#specification-dfn-rdf-graph), and comprises:

 

 

- Exactly one 
<a id="specification-dfn-default-graph"></a>
default graph, being an 
<a id="specification-ref-for-dfn-rdf-graph-36"></a>
[RDF graph](#specification-dfn-rdf-graph). The default graph does not have a name and MAY be empty.

 

- Zero or more 
<a id="specification-dfn-named-graphs"></a>

<a id="specification-dfn-named-graph"></a>
named graphs. Each named graph is a pair consisting of an 
<a id="specification-ref-for-dfn-iri-37"></a>
[IRI](#specification-dfn-iri) or a blank node (the 
<a id="specification-dfn-graph-name"></a>
graph name), and an 
<a id="specification-ref-for-dfn-rdf-graph-37"></a>
[RDF graph](#specification-dfn-rdf-graph). Graph names are unique within an RDF dataset.

 

 


<a id="specification-ref-for-dfn-blank-node-15"></a>
[Blank nodes](#specification-dfn-blank-node) can be shared between graphs in an 
<a id="specification-ref-for-dfn-rdf-dataset-9"></a>
[RDF dataset](#specification-dfn-rdf-dataset).

 
<a id="specification-note-datasets"></a>



<a id="specification-h-note-11"></a>


Note



 

Despite the use of the word “name” in “
<a id="specification-ref-for-dfn-named-graph-3"></a>
[named graph](#specification-dfn-named-graph)”, the 
<a id="specification-ref-for-dfn-graph-name-3"></a>
[graph name](#specification-dfn-graph-name) is not required to 
<a id="specification-ref-for-dfn-denote-6"></a>
[denote](#specification-dfn-denote) the graph. It is merely syntactically paired with the graph. RDF does not place any formal restrictions on what 
<a id="specification-ref-for-dfn-resource-9"></a>
[resource](#specification-dfn-resource) the graph name may denote, nor on the relationship between that resource and the graph. A discussion of different RDF dataset semantics can be found in [[RDF11-DATASETS](#specification-bib-rdf11-datasets)].

 

Some 
<a id="specification-ref-for-dfn-rdf-dataset-10"></a>
[RDF dataset](#specification-dfn-rdf-dataset) implementations do not track empty 
<a id="specification-ref-for-dfn-named-graph-4"></a>
[named graphs](#specification-dfn-named-graph). Applications can avoid interoperability issues by not ascribing importance to the presence or absence of empty named graphs.

 

SPARQL version 1.2 [[SPARQL12-CONCEPTS](#specification-bib-sparql12-concepts)] uses 
<a id="specification-ref-for-index-term-the-same-concept-of-an-rdf-dataset-1"></a>
[the same concept of an RDF Dataset](https://www.w3.org/TR/sparql12-query/#sparqlDataset) as RDF versions 1.1 and 1.2, in which the graph names of named graphs may be IRIs or blank nodes. In contrast, version 1.1 of the SPARQL Query Language [[SPARQL11-QUERY](#specification-bib-sparql11-query)] only allowed graph names to be IRIs.

 



 
<a id="specification-section-dataset-isomorphism"></a>

<a id="specification-L3201"></a>
<a id="specification-x4-1-rdf-dataset-comparison"></a>
### 4.1 RDF Dataset Comparison
[](#specification-section-dataset-isomorphism)

 
<a id="specification-section-dataset-equality"></a>


Two 
<a id="specification-ref-for-dfn-rdf-dataset-11"></a>
[RDF datasets](#specification-dfn-rdf-dataset) D1 and D2 (respectively, with 
<a id="specification-ref-for-dfn-default-graph-3"></a>
[default graphs](#specification-dfn-default-graph) DG1 and DG2 and sets NG1 and NG2 of 
<a id="specification-ref-for-dfn-named-graph-5"></a>
[named graphs](#specification-dfn-named-graph)) are 
<a id="specification-dfn-dataset-isomorphism"></a>
dataset-isomorphic if and only if there exists an 
<a id="specification-ref-for-dfn-isomorphic-rdf-term-mapping-2"></a>
[isomorphic RDF-term mapping](#specification-dfn-isomorphic-rdf-term-mapping) M for which all of the following properties hold:

 

 

- The triple (s, p, o) is in DG1 if and only if the triple ( M(s), M(p), M(o) ) is in DG2.

 

- The 
<a id="specification-ref-for-dfn-named-graph-6"></a>
[named graph](#specification-dfn-named-graph) (n, G) is in NG1 if and only if there is a 
<a id="specification-ref-for-dfn-named-graph-7"></a>
[named graph](#specification-dfn-named-graph) (n', G') in NG2 such that the following are true: 

 

  - M(n) is 
<a id="specification-ref-for-dfn-rdf-term-equality-4"></a>
[equal](#specification-dfn-rdf-term-equality) to n'.

 

  - For every triple t=(s, p, o), it holds that t is in G if and only if the triple ( M(s), M(p), M(o) ) is in G'.

 

 

 

 

 
<a id="specification-section-dataset-conneg"></a>

<a id="specification-L3227"></a>
<a id="specification-x4-2-content-negotiation-of-rdf-datasets"></a>
### 4.2 Content Negotiation of RDF Datasets
[](#specification-section-dataset-conneg)



This section is non-normative.

 

Web resources may have multiple representations that are made available via 
<a id="specification-ref-for-index-term-content-negotiation-3"></a>
[content negotiation](https://www.w3.org/TR/webarch/#frag-coneg) [[WEBARCH](#specification-bib-webarch)]. A representation may be returned in an RDF serialization format that supports the expression of both 
<a id="specification-ref-for-dfn-rdf-dataset-12"></a>
[RDF datasets](#specification-dfn-rdf-dataset) and 
<a id="specification-ref-for-dfn-rdf-graph-38"></a>
[RDF graphs](#specification-dfn-rdf-graph). If an 
<a id="specification-ref-for-dfn-rdf-dataset-13"></a>
[RDF dataset](#specification-dfn-rdf-dataset) is returned and the consumer is expecting an 
<a id="specification-ref-for-dfn-rdf-graph-39"></a>
[RDF graph](#specification-dfn-rdf-graph), the consumer is expected to use the 
<a id="specification-ref-for-dfn-rdf-dataset-14"></a>
[RDF dataset's](#specification-dfn-rdf-dataset) default graph.

 

 
<a id="specification-section-dataset-quad"></a>

<a id="specification-L3239"></a>
<a id="specification-x4-3-dataset-as-a-set-of-quads"></a>
### 4.3 Dataset as a Set of Quads
[](#specification-section-dataset-quad)



This section is non-normative.

 

A 
<a id="specification-dfn-quad"></a>
quad is a 
<a id="specification-ref-for-dfn-rdf-triple-34"></a>
[triple](#specification-dfn-rdf-triple) associated with an optional 
<a id="specification-ref-for-dfn-graph-name-4"></a>
[graph name](#specification-dfn-graph-name) and is used when referring to triples within an 
<a id="specification-ref-for-dfn-rdf-dataset-15"></a>
[RDF dataset](#specification-dfn-rdf-dataset). 

 

A 
<a id="specification-ref-for-dfn-quad-1"></a>
[quad](#specification-dfn-quad) can be represented as a tuple composed of 
<a id="specification-ref-for-dfn-subject-9"></a>
[subject](#specification-dfn-subject), 
<a id="specification-ref-for-dfn-predicate-8"></a>
[predicate](#specification-dfn-predicate), 
<a id="specification-ref-for-dfn-object-12"></a>
[object](#specification-dfn-object), and an optional 
<a id="specification-ref-for-dfn-graph-name-5"></a>
[graph name](#specification-dfn-graph-name).

 

An 
<a id="specification-ref-for-dfn-rdf-dataset-16"></a>
[RDF dataset](#specification-dfn-rdf-dataset) can be considered to be a set of 
<a id="specification-ref-for-dfn-quad-2"></a>
[quads](#specification-dfn-quad) where quads with no 
<a id="specification-ref-for-dfn-graph-name-6"></a>
[graph name](#specification-dfn-graph-name) supply the 
<a id="specification-ref-for-dfn-rdf-triple-35"></a>
[triples](#specification-dfn-rdf-triple) of the 
<a id="specification-ref-for-dfn-default-graph-4"></a>
[default graph](#specification-dfn-default-graph), and quads with the same graph name supply the triples of the 
<a id="specification-ref-for-dfn-named-graph-8"></a>
[named graph](#specification-dfn-named-graph) with that name.

 
<a id="specification-issue-container-generatedID-10"></a>



<a id="specification-h-note-12"></a>


Note



Although a 
<a id="specification-ref-for-dfn-quad-3"></a>
[quad](#specification-dfn-quad) without a 
<a id="specification-ref-for-dfn-graph-name-7"></a>
[graph name](#specification-dfn-graph-name) consists of the same three components as a 
<a id="specification-ref-for-dfn-rdf-triple-36"></a>
[triple](#specification-dfn-rdf-triple), it is a distinct concept, as it specifically captures the notion of a triple within the 
<a id="specification-ref-for-dfn-default-graph-5"></a>
[default graph](#specification-dfn-default-graph) of an 
<a id="specification-ref-for-dfn-rdf-dataset-17"></a>
[RDF dataset](#specification-dfn-rdf-dataset).



 

 

 
<a id="specification-section-Datatypes"></a>

<a id="specification-L3262"></a>
<a id="specification-x5-datatypes"></a>
## 5. Datatypes
[](#specification-section-Datatypes)

 

Datatypes are used with RDF 
<a id="specification-ref-for-dfn-literal-17"></a>
[literals](#specification-dfn-literal) to represent values such as strings, numbers and dates. The datatype abstraction used in RDF is compatible with XML Schema [[XMLSCHEMA11-2](#specification-bib-xmlschema11-2)]. Any datatype definition that conforms to this abstraction MAY be used in RDF, even if not defined in terms of XML Schema. RDF re-uses many of the XML Schema built-in datatypes, and defines three additional datatypes, `rdf:JSON`, `rdf:HTML`, and `rdf:XMLLiteral`. 

 

A 
<a id="specification-dfn-datatype"></a>
datatype consists of a 
<a id="specification-ref-for-dfn-lexical-space-2"></a>
[lexical space](#specification-dfn-lexical-space), a 
<a id="specification-ref-for-dfn-value-space-1"></a>
[value space](#specification-dfn-value-space) and a 
<a id="specification-ref-for-dfn-lexical-to-value-mapping-2"></a>
[lexical-to-value mapping](#specification-dfn-lexical-to-value-mapping), and is identified by one or more 
<a id="specification-ref-for-dfn-iri-38"></a>
[IRIs](#specification-dfn-iri).

 

The 
<a id="specification-dfn-lexical-space"></a>
lexical space of a datatype is a set of 
<a id="specification-ref-for-dfn-rdf-string-6"></a>
[strings](#specification-dfn-rdf-string).

 

The 
<a id="specification-dfn-lexical-to-value-mapping"></a>
lexical-to-value mapping of a datatype is a set of pairs whose first element belongs to the 
<a id="specification-ref-for-dfn-lexical-space-3"></a>
[lexical space](#specification-dfn-lexical-space), and the second element belongs to the 
<a id="specification-dfn-value-space"></a>
value space of the datatype. Each member of the lexical space is paired with exactly one value, and is a lexical representation of that value. The mapping can be seen as a function from the lexical space to the value space.

 
<a id="specification-note-lang-strings"></a>



<a id="specification-h-note-13"></a>


Note




<a id="specification-ref-for-dfn-language-tagged-string-5"></a>
[Language-tagged strings](#specification-dfn-language-tagged-string) have the 
<a id="specification-ref-for-dfn-datatype-iri-9"></a>
[datatype IRI](#specification-dfn-datatype-iri) `http://www.w3.org/1999/02/22-rdf-syntax-ns#langString` (commonly abbreviated as `rdf:langString`). No datatype is formally defined for this IRI because the definition of 
<a id="specification-ref-for-dfn-datatype-4"></a>
[datatypes](#specification-dfn-datatype) does not accommodate 
<a id="specification-ref-for-dfn-language-tag-9"></a>
[language tags](#specification-dfn-language-tag) in the 
<a id="specification-ref-for-dfn-lexical-space-4"></a>
[lexical space](#specification-dfn-lexical-space). The 
<a id="specification-ref-for-dfn-value-space-2"></a>
[value space](#specification-dfn-value-space) associated with this datatype IRI is the set of all pairs that consist of a string and a language tag. Similarly, 
<a id="specification-ref-for-dfn-dir-lang-string-9"></a>
[directional language-tagged strings](#specification-dfn-dir-lang-string) `http://www.w3.org/1999/02/22-rdf-syntax-ns#dirLangString` (commonly abbreviated as `rdf:dirLangString`) also have a 
<a id="specification-ref-for-dfn-base-direction-8"></a>
[base direction](#specification-dfn-base-direction) in the value space. The 
<a id="specification-ref-for-dfn-value-space-3"></a>
[value space](#specification-dfn-value-space) associated with this datatype IRI is the set of all 3-tuples of a string, a language tag and a base direction. 



 

For example, the XML Schema datatype `xsd:boolean`, where each member of the 
<a id="specification-ref-for-dfn-value-space-4"></a>
[value space](#specification-dfn-value-space) has two lexical representations, is defined as follows:

 

 

Lexical space:

 

{"`true`", "`false`", "`1`", "`0`"}

 

Value space:

 

{true, false}

 

Lexical-to-value mapping

 

{ <"`true`", true>, <"`false`", false>, <"`1`", true>, <"`0`", false>, }

 

 

The 
<a id="specification-ref-for-dfn-literal-18"></a>
[literals](#specification-dfn-literal) that can be defined using this datatype are:

 
<a id="specification-tab-boolean-literals"></a>


- This table lists the literals of type xsd:boolean.
- Literal | Value
- <"`true`", `xsd:boolean`> | true
- <"`false`", `xsd:boolean`> | false
- <"`1`", `xsd:boolean`> | true
- <"`0`", `xsd:boolean`> | false

 
<a id="specification-xsd-datatypes"></a>

<a id="specification-L3350"></a>
<a id="specification-x5-1-the-xml-schema-built-in-datatypes"></a>
### 5.1 The XML Schema Built-in Datatypes
[](#specification-xsd-datatypes)

 


<a id="specification-ref-for-dfn-iri-39"></a>
[IRIs](#specification-dfn-iri) of the form `http://www.w3.org/2001/XMLSchema#xxx`, where `xxx` is the name of a datatype, denote the built-in datatypes defined in [W3C XML Schema Definition Language (XSD) 1.1 Part 2: Datatypes](https://www.w3.org/TR/xmlschema11-2/) [[XMLSCHEMA11-2](#specification-bib-xmlschema11-2)]. The XML Schema built-in types listed in the following table are the 
<a id="specification-dfn-rdf-compatible-xsd-types"></a>
RDF-compatible XSD types. Their use is RECOMMENDED.

 

Readers might note that the only safe datatypes for transferring binary information are `xsd:hexBinary` and `xsd:base64Binary`.

 
<a id="specification-tab-xsd-datatypes"></a>


- A list of the RDF-compatible XSD types, with short descriptions
-  | Datatype | Value space (informative)
- Core types [rowspan=4] | <a id="specification-ref-for-index-term-xsd-string-1"></a>
[`xsd:string`](https://www.w3.org/TR/xmlschema11-2/#string) | Character strings
- <a id="specification-ref-for-index-term-xsd-boolean-1"></a>
[`xsd:boolean`](https://www.w3.org/TR/xmlschema11-2/#boolean) | true, false
- <a id="specification-ref-for-index-term-xsd-decimal-1"></a>
[`xsd:decimal`](https://www.w3.org/TR/xmlschema11-2/#decimal) | Arbitrary-precision decimal numbers
- <a id="specification-ref-for-index-term-xsd-integer-1"></a>
[`xsd:integer`](https://www.w3.org/TR/xmlschema11-2/#integer) | Arbitrary-size integer numbers
- IEEE floating-point
numbers [rowspan=2] | <a id="specification-ref-for-index-term-xsd-double-1"></a>
[`xsd:double`](https://www.w3.org/TR/xmlschema11-2/#double) | 64-bit floating point numbers incl. ±Inf, ±0, NaN
- <a id="specification-ref-for-index-term-xsd-float-1"></a>
[`xsd:float`](https://www.w3.org/TR/xmlschema11-2/#float) | 32-bit floating point numbers incl. ±Inf, ±0, NaN
- Time and date [rowspan=4] | <a id="specification-ref-for-index-term-xsd-date-1"></a>
[`xsd:date`](https://www.w3.org/TR/xmlschema11-2/#date) | Dates (yyyy-mm-dd) with or without timezone
- <a id="specification-ref-for-index-term-xsd-time-1"></a>
[`xsd:time`](https://www.w3.org/TR/xmlschema11-2/#time) | Times (hh:mm:ss.sss…) with or without timezone
- <a id="specification-ref-for-index-term-xsd-datetime-1"></a>
[`xsd:dateTime`](https://www.w3.org/TR/xmlschema11-2/#dateTime) | Date and time with or without timezone
- <a id="specification-ref-for-index-term-xsd-datetimestamp-1"></a>
[`xsd:dateTimeStamp`](https://www.w3.org/TR/xmlschema11-2/#dateTimeStamp) | Date and time with required timezone
- Recurring and
partial dates [rowspan=5] | <a id="specification-ref-for-index-term-xsd-gyear-1"></a>
[`xsd:gYear`](https://www.w3.org/TR/xmlschema11-2/#gYear) | Gregorian calendar year
- <a id="specification-ref-for-index-term-xsd-gmonth-1"></a>
[`xsd:gMonth`](https://www.w3.org/TR/xmlschema11-2/#gMonth) | Gregorian calendar month
- <a id="specification-ref-for-index-term-xsd-gday-1"></a>
[`xsd:gDay`](https://www.w3.org/TR/xmlschema11-2/#gDay) | Gregorian calendar day of the month
- <a id="specification-ref-for-index-term-xsd-gyearmonth-1"></a>
[`xsd:gYearMonth`](https://www.w3.org/TR/xmlschema11-2/#gYearMonth) | Gregorian calendar year and month
- <a id="specification-ref-for-index-term-xsd-gmonthday-1"></a>
[`xsd:gMonthDay`](https://www.w3.org/TR/xmlschema11-2/#gMonthDay) | Gregorian calendar month and day
- Durations [rowspan=3] | <a id="specification-ref-for-index-term-xsd-duration-1"></a>
[`xsd:duration`](https://www.w3.org/TR/xmlschema11-2/#duration) | Duration of time
- <a id="specification-ref-for-index-term-xsd-yearmonthduration-1"></a>
[`xsd:yearMonthDuration`](https://www.w3.org/TR/xmlschema11-2/#yearMonthDuration) | Duration of time (months and years only)
- <a id="specification-ref-for-index-term-xsd-daytimeduration-1"></a>
[`xsd:dayTimeDuration`](https://www.w3.org/TR/xmlschema11-2/#dayTimeDuration) | Duration of time (days, hours, minutes, seconds only)
- Limited-range
integer numbers [rowspan=12] | <a id="specification-ref-for-index-term-xsd-byte-1"></a>
[`xsd:byte`](https://www.w3.org/TR/xmlschema11-2/#byte) | -128…+127 (8 bit)
- <a id="specification-ref-for-index-term-xsd-short-1"></a>
[`xsd:short`](https://www.w3.org/TR/xmlschema11-2/#short) | -32768…+32767 (16 bit)
- <a id="specification-ref-for-index-term-xsd-int-1"></a>
[`xsd:int`](https://www.w3.org/TR/xmlschema11-2/#int) | -2147483648…+2147483647 (32 bit)
- <a id="specification-ref-for-index-term-xsd-long-1"></a>
[`xsd:long`](https://www.w3.org/TR/xmlschema11-2/#long) | -9223372036854775808…+9223372036854775807 (64 bit)
- <a id="specification-ref-for-index-term-xsd-unsignedbyte-1"></a>
[`xsd:unsignedByte`](https://www.w3.org/TR/xmlschema11-2/#unsignedByte) | 0…255 (8 bit)
- <a id="specification-ref-for-index-term-xsd-unsignedshort-1"></a>
[`xsd:unsignedShort`](https://www.w3.org/TR/xmlschema11-2/#unsignedShort) | 0…65535 (16 bit)
- <a id="specification-ref-for-index-term-xsd-unsignedint-1"></a>
[`xsd:unsignedInt`](https://www.w3.org/TR/xmlschema11-2/#unsignedInt) | 0…4294967295 (32 bit)
- <a id="specification-ref-for-index-term-xsd-unsignedlong-1"></a>
[`xsd:unsignedLong`](https://www.w3.org/TR/xmlschema11-2/#unsignedLong) | 0…18446744073709551615 (64 bit)
- <a id="specification-ref-for-index-term-xsd-positiveinteger-1"></a>
[`xsd:positiveInteger`](https://www.w3.org/TR/xmlschema11-2/#positiveInteger) | Integer numbers >0
- <a id="specification-ref-for-index-term-xsd-nonnegativeinteger-1"></a>
[`xsd:nonNegativeInteger`](https://www.w3.org/TR/xmlschema11-2/#nonNegativeInteger) | Integer numbers ≥0
- <a id="specification-ref-for-index-term-xsd-negativeinteger-1"></a>
[`xsd:negativeInteger`](https://www.w3.org/TR/xmlschema11-2/#negativeInteger) | Integer numbers <0
- <a id="specification-ref-for-index-term-xsd-nonpositiveinteger-1"></a>
[`xsd:nonPositiveInteger`](https://www.w3.org/TR/xmlschema11-2/#nonPositiveInteger) | Integer numbers ≤0
- Encoded binary data [rowspan=2] | <a id="specification-ref-for-index-term-xsd-hexbinary-1"></a>
[`xsd:hexBinary`](https://www.w3.org/TR/xmlschema11-2/#hexBinary) | Hex-encoded binary data
- <a id="specification-ref-for-index-term-xsd-base64binary-1"></a>
[`xsd:base64Binary`](https://www.w3.org/TR/xmlschema11-2/#base64Binary) | Base64-encoded binary data
- Miscellaneous
XSD types [rowspan=7] | <a id="specification-ref-for-index-term-xsd-anyuri-1"></a>
[`xsd:anyURI`](https://www.w3.org/TR/xmlschema11-2/#anyURI) | Resolved or relative URI and IRI references
- <a id="specification-ref-for-index-term-xsd-language-1"></a>
[`xsd:language`](https://www.w3.org/TR/xmlschema11-2/#language) | Language tags per [[BCP47](#specification-bib-bcp47)]
- <a id="specification-ref-for-index-term-xsd-normalizedstring-1"></a>
[`xsd:normalizedString`](https://www.w3.org/TR/xmlschema11-2/#normalizedString) | Whitespace-normalized strings
- <a id="specification-ref-for-index-term-xsd-token-1"></a>
[`xsd:token`](https://www.w3.org/TR/xmlschema11-2/#token) | Tokenized strings
- <a id="specification-ref-for-index-term-xsd-nmtoken-1"></a>
[`xsd:NMTOKEN`](https://www.w3.org/TR/xmlschema11-2/#NMTOKEN) | XML NMTOKENs
- <a id="specification-ref-for-index-term-xsd-name-1"></a>
[`xsd:Name`](https://www.w3.org/TR/xmlschema11-2/#Name) | XML Names
- <a id="specification-ref-for-index-term-xsd-ncname-1"></a>
[`xsd:NCName`](https://www.w3.org/TR/xmlschema11-2/#NCName) | XML NCNames

 

The 
<a id="specification-ref-for-dfn-lexical-to-value-mapping-3"></a>
[lexical-to-value mapping](#specification-dfn-lexical-to-value-mapping) for 
<a id="specification-ref-for-index-term-xsd-float-2"></a>
[`xsd:float`](https://www.w3.org/TR/xmlschema11-2/#float) and 
<a id="specification-ref-for-index-term-xsd-double-2"></a>
[`xsd:double`](https://www.w3.org/TR/xmlschema11-2/#double) MUST use a method consistent with 
<a id="specification-ref-for-index-term-doublelexicalmap-1"></a>
[doubleLexicalMap](https://www.w3.org/TR/xmlschema11-2/#f-doubleLexmap), which MUST strictly conform to the rounding method described in 
<a id="specification-ref-for-index-term-floatptround-1"></a>
[floatPtRound](https://www.w3.org/TR/xmlschema11-2/#f-floatPtRound) [[XMLSCHEMA11-2](#specification-bib-xmlschema11-2)].

 

The other built-in XML Schema datatypes are unsuitable for various reasons and SHOULD NOT be used:

 

 

- 
<a id="specification-ref-for-index-term-xsd-qname-1"></a>
[`xsd:QName`](https://www.w3.org/TR/xmlschema11-2/#QName) and 
<a id="specification-ref-for-index-term-xsd-entity-1"></a>
[`xsd:ENTITY`](https://www.w3.org/TR/xmlschema11-2/#ENTITY) require an enclosing XML document context.

 

- 
<a id="specification-ref-for-index-term-xsd-id-1"></a>
[`xsd:ID`](https://www.w3.org/TR/xmlschema11-2/#ID) and 
<a id="specification-ref-for-index-term-xsd-idref-1"></a>
[`xsd:IDREF`](https://www.w3.org/TR/xmlschema11-2/#IDREF) are for cross references within an XML document.

 

- 
<a id="specification-ref-for-index-term-xsd-notation-1"></a>
[`xsd:NOTATION`](https://www.w3.org/TR/xmlschema11-2/#NOTATION) is not intended for direct use.

 

- 
<a id="specification-ref-for-index-term-xsd-idrefs-1"></a>
[`xsd:IDREFS`](https://www.w3.org/TR/xmlschema11-2/#IDREFS), 
<a id="specification-ref-for-index-term-xsd-entities-1"></a>
[`xsd:ENTITIES`](https://www.w3.org/TR/xmlschema11-2/#ENTITIES) and 
<a id="specification-ref-for-index-term-xsd-nmtokens-1"></a>
[`xsd:NMTOKENS`](https://www.w3.org/TR/xmlschema11-2/#NMTOKENS) are sequence-valued datatypes which do not fit the RDF 
<a id="specification-ref-for-dfn-datatype-5"></a>
[datatype](#specification-dfn-datatype) model.

 

 
<a id="specification-issue-container-generatedID-11"></a>



<a id="specification-h-note-14"></a>


Note



The 
<a id="specification-ref-for-dfn-value-space-5"></a>
[value spaces](#specification-dfn-value-space) of 
<a id="specification-ref-for-index-term-xsd-double-3"></a>
[`xsd:double`](https://www.w3.org/TR/xmlschema11-2/#double) and 
<a id="specification-ref-for-index-term-xsd-float-3"></a>
[`xsd:float`](https://www.w3.org/TR/xmlschema11-2/#float) do not include all decimal numbers. For every literal of either of these two datatypes, the value of the literal is a value that can be represented as an [IEEE 754-2008](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933) binary floating point representation of the corresponding precision. For instance, the literal with lexical form `"0.1"` and datatype 
<a id="specification-ref-for-index-term-xsd-float-4"></a>
[`xsd:float`](https://www.w3.org/TR/xmlschema11-2/#float) 
<a id="specification-ref-for-dfn-denote-7"></a>
[denotes](#specification-dfn-denote) the number `0.100000001490116119384765625`. Rather than 
<a id="specification-ref-for-index-term-xsd-double-4"></a>
[`xsd:double`](https://www.w3.org/TR/xmlschema11-2/#double) or 
<a id="specification-ref-for-index-term-xsd-float-5"></a>
[`xsd:float`](https://www.w3.org/TR/xmlschema11-2/#float), the datatype 
<a id="specification-ref-for-index-term-xsd-decimal-2"></a>
[`xsd:decimal`](https://www.w3.org/TR/xmlschema11-2/#decimal) can be used to accurately capture arbitrary decimal numbers.



 

 
<a id="specification-datatype-iris"></a>

<a id="specification-L3469"></a>
<a id="specification-x5-2-datatype-iris"></a>
### 5.2 Datatype IRIs
[](#specification-datatype-iris)

 

Datatypes are identified by 
<a id="specification-ref-for-dfn-iri-40"></a>
[IRIs](#specification-dfn-iri).

 

 If any IRI of the form `http://www.w3.org/2001/XMLSchema#xxx` is handled by an RDF implementation, it MUST refer to the RDF-compatible XSD type named `xsd:xxx` for every XSD type listed in [section 5.1](#specification-xsd-datatypes).

 

The datatypes identified by the three IRIs below are defined in Appendix [A. Additional Datatypes](#specification-section-additional-datatypes):

 

 

- The IRI `http://www.w3.org/1999/02/22-rdf-syntax-ns#XMLLiteral` refers to the datatype `rdf:XMLLiteral`.

 

- The IRI `http://www.w3.org/1999/02/22-rdf-syntax-ns#HTML` refers to the datatype `rdf:HTML`.

 

- The IRI `http://www.w3.org/1999/02/22-rdf-syntax-ns#JSON` refers to the datatype `rdf:JSON`.

 

 

RDF implementations are not required to handle all datatypes. Any literal typed with a datatype not handled by an RDF implementation is treated just like an unknown IRI, i.e., as referring to an unknown thing. Applications MAY give a warning message if they are unable to determine the referent of an IRI used in a typed literal. RDF implementations SHOULD NOT reject a literal with an unknown datatype as either a syntactic or semantic error.



 



Other specifications MAY impose additional constraints on 
<a id="specification-ref-for-dfn-datatype-iri-10"></a>
[datatype IRIs](#specification-dfn-datatype-iri), for example, require support for certain datatypes.

 
<a id="specification-issue-container-generatedID-12"></a>



<a id="specification-h-note-15"></a>


Note



Semantic extensions of RDF might choose to recognize other datatype IRIs and require each of them to refer to a fixed datatype. See [RDF 1.2 Semantics](https://www.w3.org/TR/rdf12-semantics/) [[RDF12-SEMANTICS](#specification-bib-rdf12-semantics)] for more information on semantic extensions.



 
<a id="specification-note-custom-datatypes"></a>



<a id="specification-h-note-16"></a>


Note



The Web Ontology Language [[OWL2-OVERVIEW](#specification-bib-owl2-overview)] offers facilities for formally defining 
<a id="specification-ref-for-index-term-custom-datatypes-1"></a>
[custom datatypes](https://www.w3.org/TR/owl2-syntax/#Datatype_Definitions) that can be used with RDF. Furthermore, a practice for identifying 
<a id="specification-ref-for-index-term-user-defined-simple-xml-schema-datatypes-1"></a>
[user-defined simple XML Schema datatypes](https://www.w3.org/TR/swbp-xsch-datatypes/#sec-userDefined) is suggested in [[SWBP-XSCH-DATATYPES](#specification-bib-swbp-xsch-datatypes)]. RDF implementations are not required to support either of these facilities.



 
<a id="specification-note-recognized-datatype-iris"></a>



<a id="specification-h-note-17"></a>


Note



 In RDF 1.1, 
<a id="specification-dfn-recognized-datatype-iris"></a>
Recognized datatype IRIs were defined in RDF Concepts, overlapping with 
<a id="specification-ref-for-index-term-rdf-semantics-recognizing-1"></a>
[RDF Semantics, "recognizing"](https://www.w3.org/TR/rdf12-semantics/#dfn-recognize) datatype IRIs for 
<a id="specification-ref-for-index-term-semantic-extensions-1"></a>
[semantic extensions](https://www.w3.org/TR/rdf12-semantics/#dfn-semantic-extension). 



 

 

 
<a id="specification-section-fragID"></a>

<a id="specification-L3529"></a>
<a id="specification-x6-fragment-identifiers"></a>
## 6. Fragment Identifiers
[](#specification-section-fragID)



This section is non-normative.

 

RDF uses 
<a id="specification-ref-for-dfn-iri-41"></a>
[IRIs](#specification-dfn-iri), which may include 
<a id="specification-dfn-fragment-identifiers"></a>
 
<a id="specification-dfn-fragment-identifier"></a>
fragment identifiers, as resource identifiers. The semantics of fragment identifiers is 
<a id="specification-ref-for-index-term-fragment-identifier-2"></a>
[defined in RFC 3986](https://www.rfc-editor.org/rfc/rfc3986#section-3.5) [[RFC3986](#specification-bib-rfc3986)]: They identify a secondary resource that is usually a part of, a view of, defined in, or described in the primary resource, and the precise semantics depend on the set of representations that might result from a retrieval action on the primary resource.

 

This section discusses the handling of fragment identifiers in representations that encode 
<a id="specification-ref-for-dfn-rdf-graph-40"></a>
[RDF graphs](#specification-dfn-rdf-graph).

 

In RDF-bearing representations of a primary resource, e.g., `<https://example.com/foo>`, the secondary resource identified by a fragment identifier, e.g., `bar`, is the 
<a id="specification-ref-for-dfn-resource-10"></a>
[resource](#specification-dfn-resource) 
<a id="specification-ref-for-dfn-denote-8"></a>
[denoted](#specification-dfn-denote) by the full 
<a id="specification-ref-for-dfn-iri-42"></a>
[IRI](#specification-dfn-iri) in the 
<a id="specification-ref-for-dfn-rdf-graph-41"></a>
[RDF graph](#specification-dfn-rdf-graph), which would be `<https://example.com/foo#bar>` in this case. Since IRIs in RDF graphs can denote anything, this can be something external to the representation, or even external to the web.

 

In this way, the RDF-bearing representation acts as an intermediary between the web-accessible primary resource and some set of possibly non-web or abstract entities that the 
<a id="specification-ref-for-dfn-rdf-graph-42"></a>
[RDF graph](#specification-dfn-rdf-graph) may describe.

 

In cases where other specifications constrain the semantics of 
<a id="specification-ref-for-dfn-fragment-identifier-2"></a>
[fragment identifiers](#specification-dfn-fragment-identifier) in RDF-bearing representations, the encoded 
<a id="specification-ref-for-dfn-rdf-graph-43"></a>
[RDF graph](#specification-dfn-rdf-graph) should use fragment identifiers in a way that is consistent with these constraints. For example, in an HTML+RDFa document [[HTML-RDFA](#specification-bib-html-rdfa)], a fragment identifier such as `chapter1` may identify a document section via the semantics of HTML's `@name` or `@id` attributes. Such an 
<a id="specification-ref-for-dfn-iri-43"></a>
[IRI](#specification-dfn-iri), e.g., `<#chapter1>`, should then be taken to 
<a id="specification-ref-for-dfn-denote-9"></a>
[denote](#specification-dfn-denote) that same section in any RDFa-encoded 
<a id="specification-ref-for-dfn-rdf-triple-37"></a>
[triples](#specification-dfn-rdf-triple) within the same document. Similarly, fragment identifiers should be used consistently in resources with multiple representations that are made available via 
<a id="specification-ref-for-index-term-content-negotiation-4"></a>
[content negotiation](https://www.w3.org/TR/webarch/#frag-coneg) [[WEBARCH](#specification-bib-webarch)]. For example, if the fragment identifier `chapter1` identifies a document section in an HTML representation of the primary resource, then the 
<a id="specification-ref-for-dfn-iri-44"></a>
[IRI](#specification-dfn-iri) `<#chapter1>` should be taken to 
<a id="specification-ref-for-dfn-denote-10"></a>
[denote](#specification-dfn-denote) that same section in all RDF-bearing representations of the same primary resource.

 

 
<a id="specification-section-generalizations-of-rdf"></a>

<a id="specification-L3579"></a>
<a id="specification-x7-generalizations-of-rdf-triples-graphs-and-datasets"></a>
## 7. Generalizations of RDF Triples, Graphs, and Datasets
[](#specification-section-generalizations-of-rdf)



This section is non-normative.

 

It is sometimes convenient to loosen the requirements on 
<a id="specification-ref-for-dfn-rdf-triple-38"></a>
[RDF triples](#specification-dfn-rdf-triple). For example, the completeness of the RDFS entailment rules is easier to show with a notion of symmetric RDF triples.

 
<a id="specification-section-symmetric-rdf"></a>

<a id="specification-L3587"></a>
<a id="specification-x7-1-symmetric-rdf"></a>
### 7.1 Symmetric RDF
[](#specification-section-symmetric-rdf)

 

 A 
<a id="specification-dfn-symmetric-rdf-triple"></a>
symmetric RDF triple allows the subject to be any 
<a id="specification-ref-for-dfn-rdf-term-14"></a>
[RDF term](#specification-dfn-rdf-term) that is allowed in the object position, one of an 
<a id="specification-ref-for-dfn-iri-45"></a>
[IRI](#specification-dfn-iri), a 
<a id="specification-ref-for-dfn-blank-node-16"></a>
[blank node](#specification-dfn-blank-node), a 
<a id="specification-ref-for-dfn-literal-19"></a>
[literal](#specification-dfn-literal), or a 
<a id="specification-ref-for-dfn-triple-term-23"></a>
[triple term](#specification-dfn-triple-term) (which may itself be a symmetric RDF triple). A 
<a id="specification-dfn-symmetric-rdf-graph"></a>
symmetric RDF graph is a set of symmetric RDF triples. A 
<a id="specification-dfn-symmetric-rdf-dataset"></a>
symmetric RDF dataset comprises a distinguished symmetric RDF graph, and zero or more pairs that each associate an 
<a id="specification-ref-for-dfn-iri-46"></a>
[IRI](#specification-dfn-iri) or a 
<a id="specification-ref-for-dfn-blank-node-17"></a>
[blank node](#specification-dfn-blank-node) with a symmetric RDF graph.

 

Symmetric RDF triples, graphs, and datasets differ from standard, normative RDF 
<a id="specification-ref-for-dfn-rdf-triple-39"></a>
[triples](#specification-dfn-rdf-triple), 
<a id="specification-ref-for-dfn-rdf-graph-44"></a>
[graphs](#specification-dfn-rdf-graph), and 
<a id="specification-ref-for-dfn-rdf-dataset-18"></a>
[datasets](#specification-dfn-rdf-dataset) only by allowing 
<a id="specification-ref-for-dfn-iri-47"></a>
[IRIs](#specification-dfn-iri), 
<a id="specification-ref-for-dfn-blank-node-18"></a>
[blank nodes](#specification-dfn-blank-node), 
<a id="specification-ref-for-dfn-literal-20"></a>
[literals](#specification-dfn-literal), and 
<a id="specification-ref-for-dfn-triple-term-24"></a>
[triple terms](#specification-dfn-triple-term) in the subject and object positions.

 

 
<a id="specification-section-generalized-rdf"></a>

<a id="specification-L3614"></a>
<a id="specification-x7-2-generalized-rdf"></a>
### 7.2 Generalized RDF
[](#specification-section-generalized-rdf)

 

A 
<a id="specification-dfn-generalized-rdf-triple"></a>
generalized RDF triple is a triple having a subject, a predicate, and an object, where each can be an 
<a id="specification-ref-for-dfn-iri-48"></a>
[IRI](#specification-dfn-iri), a 
<a id="specification-ref-for-dfn-blank-node-19"></a>
[blank node](#specification-dfn-blank-node), a 
<a id="specification-ref-for-dfn-literal-21"></a>
[literal](#specification-dfn-literal), or a 
<a id="specification-ref-for-dfn-triple-term-25"></a>
[triple term](#specification-dfn-triple-term) (which may itself be a generalized RDF triple). A 
<a id="specification-dfn-generalized-rdf-graph"></a>
generalized RDF graph is a set of generalized RDF triples. A 
<a id="specification-dfn-generalized-rdf-dataset"></a>
generalized RDF dataset comprises a distinguished generalized RDF graph, and zero or more pairs each associating an 
<a id="specification-ref-for-dfn-iri-49"></a>
[IRI](#specification-dfn-iri), a 
<a id="specification-ref-for-dfn-blank-node-20"></a>
[blank node](#specification-dfn-blank-node), a 
<a id="specification-ref-for-dfn-literal-22"></a>
[literal](#specification-dfn-literal), or a 
<a id="specification-ref-for-dfn-triple-term-26"></a>
[triple term](#specification-dfn-triple-term) (which may itself be a generalized RDF triple), to a generalized RDF graph.

 

Generalized RDF triples, graphs, and datasets differ from standard, normative RDF 
<a id="specification-ref-for-dfn-rdf-triple-40"></a>
[triples](#specification-dfn-rdf-triple), 
<a id="specification-ref-for-dfn-rdf-graph-45"></a>
[graphs](#specification-dfn-rdf-graph), and 
<a id="specification-ref-for-dfn-rdf-dataset-19"></a>
[datasets](#specification-dfn-rdf-dataset) only by allowing 
<a id="specification-ref-for-dfn-iri-50"></a>
[IRIs](#specification-dfn-iri), 
<a id="specification-ref-for-dfn-blank-node-21"></a>
[blank nodes](#specification-dfn-blank-node), 
<a id="specification-ref-for-dfn-literal-23"></a>
[literals](#specification-dfn-literal), and 
<a id="specification-ref-for-dfn-triple-term-27"></a>
[triple terms](#specification-dfn-triple-term) to appear in any position, i.e., as subject, predicate, object, or graph name.

 

 
<a id="specification-note-generalized-rdf"></a>



<a id="specification-h-note-18"></a>


Note



Any user of symmetric or generalized RDF triples, graphs, or datasets needs to be aware that these notions are non-standard extensions of RDF, and their use may cause interoperability problems. There is no requirement for any RDF tool to accept, process, or produce anything beyond standard normative RDF triples, graphs, and datasets. 



 

 
<a id="specification-section-additional-datatypes"></a>

<a id="specification-L3654"></a>
<a id="specification-a-additional-datatypes"></a>
## A. Additional Datatypes
[](#specification-section-additional-datatypes)

 

This section defines additional 
<a id="specification-ref-for-dfn-datatype-6"></a>
[datatypes](#specification-dfn-datatype) that RDF implementations MAY support.

 
<a id="specification-section-html"></a>

<a id="specification-L3658"></a>
<a id="specification-a-1-the-rdf-html-datatype"></a>
### A.1 The `rdf:HTML` Datatype
[](#specification-section-html)

 

RDF provides for HTML content as a possible 
<a id="specification-ref-for-dfn-literal-value-5"></a>
[literal value](#specification-dfn-literal-value). This allows markup in literal values. Such content is indicated in an 
<a id="specification-ref-for-dfn-rdf-graph-46"></a>
[RDF graph](#specification-dfn-rdf-graph) using a 
<a id="specification-ref-for-dfn-literal-24"></a>
[literal](#specification-dfn-literal) whose 
<a id="specification-ref-for-dfn-datatype-7"></a>
[datatype](#specification-dfn-datatype) is set to `rdf:HTML`.

 

The `rdf:HTML` datatype is defined as follows:

 

 
<a id="specification-HTML-uri"></a>


The IRI denoting this datatype

 

is `http://www.w3.org/1999/02/22-rdf-syntax-ns#HTML`.

 
<a id="specification-HTML-value-space"></a>


The 
<a id="specification-ref-for-dfn-value-space-6"></a>
[value space](#specification-dfn-value-space)

 

is the set of DOM 
<a id="specification-ref-for-index-term-documentfragment-1"></a>
[`DocumentFragment`](https://dom.spec.whatwg.org/#interface-documentfragment) nodes [[DOM](#specification-bib-dom)]. Two 
<a id="specification-ref-for-index-term-documentfragment-2"></a>
[`DocumentFragment`](https://dom.spec.whatwg.org/#interface-documentfragment) nodes node and otherNode are considered equal if and only if the DOM method `node.isEqualNode(otherNode)` [[DOM](#specification-bib-dom)] returns `true`.

 
<a id="specification-HTML-mapping"></a>


The lexical-to-value mapping

 

 

Each member of the lexical space is associated with the result of applying the following algorithm:

 

 

- Let `domnodes` be the list of 
<a id="specification-ref-for-index-term-dom-nodes-1"></a>
[DOM nodes](https://dom.spec.whatwg.org/#node) [[DOM](#specification-bib-dom)] that result from applying the 
<a id="specification-ref-for-index-term-html-fragment-parsing-algorithm-1"></a>
[HTML fragment parsing algorithm](https://www.w3.org/TR/html5/#parsing-html-fragments) [[HTML5](#specification-bib-html5)] to the input string, without a context element.

 

- Let `domfrag` be a DOM 
<a id="specification-ref-for-index-term-documentfragment-3"></a>
[`DocumentFragment`](https://dom.spec.whatwg.org/#interface-documentfragment) [[DOM](#specification-bib-dom)] whose `childNodes` attribute is equal to `domnodes`

 

- Return `domfrag.normalize()`.

 

 

 

 
<a id="specification-note-html"></a>



<a id="specification-h-note-19"></a>


Note



 Any language annotation (`lang="…"`), text directionality annotation (`dir="…"`), or XML namespaces (`xmlns`) desired in the HTML content must be included explicitly in the HTML literal. Relative URLs in attributes such as `href` do not have a well-defined base URL and are best avoided. RDF applications may use additional equivalence relations, such as that which relates an `xsd:string` with an `rdf:HTML` literal corresponding to a single text node of the same string.



 

 
<a id="specification-section-XMLLiteral"></a>

<a id="specification-L3712"></a>
<a id="specification-a-2-the-rdf-xmlliteral-datatype"></a>
### A.2 The `rdf:XMLLiteral` Datatype
[](#specification-section-XMLLiteral)

 

RDF provides for XML content as a possible 
<a id="specification-ref-for-dfn-literal-value-6"></a>
[literal value](#specification-dfn-literal-value). Such content is indicated in an 
<a id="specification-ref-for-dfn-rdf-graph-47"></a>
[RDF graph](#specification-dfn-rdf-graph) using a 
<a id="specification-ref-for-dfn-literal-25"></a>
[literal](#specification-dfn-literal) whose 
<a id="specification-ref-for-dfn-datatype-8"></a>
[datatype](#specification-dfn-datatype) is set to `rdf:XMLLiteral`.

 

The `rdf:XMLLiteral` datatype is defined as follows:

 

 
<a id="specification-XMLLiteral-uri"></a>


The IRI denoting this 
<a id="specification-ref-for-dfn-datatype-9"></a>
[datatype](#specification-dfn-datatype)

 

is `http://www.w3.org/1999/02/22-rdf-syntax-ns#XMLLiteral`.

 
<a id="specification-XMLLiteral-lexical-space"></a>


The 
<a id="specification-ref-for-dfn-lexical-space-5"></a>
[lexical space](#specification-dfn-lexical-space)

 

is the set of all 
<a id="specification-ref-for-dfn-rdf-string-7"></a>
[strings](#specification-dfn-rdf-string) which are well-balanced, self-contained 
<a id="specification-ref-for-index-term-xml-content-1"></a>
[XML content](https://www.w3.org/TR/xml11/#NT-content) [[XML11](#specification-bib-xml11)]; and for which embedding between an arbitrary XML start tag and an end tag yields a document conforming to [Namespaces in XML 1.0 (Third Edition)](https://www.w3.org/TR/xml-names/) [[XML-NAMES](#specification-bib-xml-names)].

 
<a id="specification-XMLLiteral-value-space"></a>


The 
<a id="specification-ref-for-dfn-value-space-7"></a>
[value space](#specification-dfn-value-space)

 

is the set of DOM 
<a id="specification-ref-for-index-term-documentfragment-4"></a>
[`DocumentFragment`](https://dom.spec.whatwg.org/#interface-documentfragment) nodes [[DOM](#specification-bib-dom)]. Two 
<a id="specification-ref-for-index-term-documentfragment-5"></a>
[`DocumentFragment`](https://dom.spec.whatwg.org/#interface-documentfragment) nodes node and otherNode are considered equal if and only if the DOM method `node.isEqualNode(otherNode)` returns `true`.

 
<a id="specification-XMLLiteral-mapping"></a>


The 
<a id="specification-ref-for-dfn-lexical-to-value-mapping-4"></a>
[lexical-to-value mapping](#specification-dfn-lexical-to-value-mapping)

 

 

Each member of the lexical space is associated with the result of applying the following algorithm:

 

 

- Let `domfrag` be a DOM 
<a id="specification-ref-for-index-term-documentfragment-6"></a>
[`DocumentFragment`](https://dom.spec.whatwg.org/#interface-documentfragment) node [[DOM](#specification-bib-dom)] corresponding to the input string.

 

- Return `domfrag.normalize()`.

 

 

 

 
<a id="specification-issue-container-generatedID-13"></a>



<a id="specification-h-note-20"></a>


Note



Any XML namespace declarations (`xmlns`), language annotation (`xml:lang`) or base URI declarations (`xml:base`) desired in the XML content must be included explicitly in the XML literal. Note that some concrete RDF syntaxes may define mechanisms for inheriting them from the context (e.g., 
<a id="specification-ref-for-index-term-parsetype-literal-1"></a>
[`@parseType="literal"`](https://www.w3.org/TR/rdf12-xml/#parseTypeLiteralPropertyElt) in RDF/XML [[RDF12-XML](#specification-bib-rdf12-xml)].



 

 
<a id="specification-section-json"></a>

<a id="specification-L3762"></a>
<a id="specification-a-3-the-rdf-json-datatype"></a>
### A.3 The `rdf:JSON` Datatype
[](#specification-section-json)

 

RDF provides for JSON content as a possible 
<a id="specification-ref-for-dfn-literal-value-7"></a>
[literal value](#specification-dfn-literal-value). This includes allowing markup in literal values. Such content is indicated in an 
<a id="specification-ref-for-dfn-rdf-graph-48"></a>
[RDF graph](#specification-dfn-rdf-graph) as a 
<a id="specification-ref-for-dfn-literal-26"></a>
[literal](#specification-dfn-literal) whose 
<a id="specification-ref-for-dfn-datatype-10"></a>
[datatype](#specification-dfn-datatype) is set to `rdf:JSON`.

 

The `rdf:JSON` datatype is defined as follows:

 

 
<a id="specification-JSON-uri"></a>


The IRI denoting this 
<a id="specification-ref-for-dfn-datatype-11"></a>
[datatype](#specification-dfn-datatype)

 

is `http://www.w3.org/1999/02/22-rdf-syntax-ns#JSON`.

 
<a id="specification-JSON-lexical-space"></a>


The 
<a id="specification-ref-for-dfn-lexical-space-6"></a>
[lexical space](#specification-dfn-lexical-space)

 

is the set of all 
<a id="specification-ref-for-dfn-rdf-string-8"></a>
[RDF strings](#specification-dfn-rdf-string) that conform to the 
<a id="specification-ref-for-index-term-json-grammar-1"></a>
[JSON Grammar](https://www.rfc-editor.org/rfc/rfc8259#section-2) as described in 
<a id="specification-ref-for-index-term-json-grammar-2"></a>
[Section 2 JSON Grammar](https://www.rfc-editor.org/rfc/rfc8259#section-2) of [[RFC8259](#specification-bib-rfc8259)], which also conform to the requirements of [The I-JSON Message Format](https://www.rfc-editor.org/rfc/rfc7493) [[RFC7493](#specification-bib-rfc7493)]. 
<a id="specification-issue-container-generatedID-14"></a>



<a id="specification-h-note-21"></a>


Note



 [The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259) [[RFC8259](#specification-bib-rfc8259)] allows strings to include 
<a id="specification-ref-for-index-term-surrogate-code-points-2"></a>
[surrogate code points](https://www.w3.org/TR/i18n-glossary/#dfn-surrogate) not allowed in 
<a id="specification-ref-for-dfn-rdf-string-9"></a>
[RDF strings](#specification-dfn-rdf-string), which are also excluded in [[RFC7493](#specification-bib-rfc7493)], thus the lexical representation of JSON literals excludes those including 
<a id="specification-ref-for-index-term-surrogate-code-points-3"></a>
[surrogate code points](https://www.w3.org/TR/i18n-glossary/#dfn-surrogate). 





 
<a id="specification-JSON-value-space"></a>


The 
<a id="specification-ref-for-dfn-value-space-8"></a>
[value space](#specification-dfn-value-space)

 

is the smallest set containing 
<a id="specification-ref-for-dfn-rdf-string-10"></a>
[strings](#specification-dfn-rdf-string), numbers (
<a id="specification-ref-for-index-term-xsd-double-5"></a>
[xsd:double](https://www.w3.org/TR/xmlschema11-2/#double)), finite unordered maps mapping 
<a id="specification-ref-for-dfn-rdf-string-11"></a>
[strings](#specification-dfn-rdf-string) to values in the [value space](#specification-JSON-value-space), 
<a id="specification-ref-for-index-term-lists-1"></a>
[lists](https://infra.spec.whatwg.org/#list) of values in the [value space](#specification-JSON-value-space), and literal values (
<a id="specification-ref-for-index-term-true-false-1"></a>
[`true`, `false`](https://infra.spec.whatwg.org/#boolean), and 
<a id="specification-ref-for-index-term-null-1"></a>
[`null`](https://infra.spec.whatwg.org/#nulls)) from [Infra Standard](https://infra.spec.whatwg.org/) [[INFRA](#specification-bib-infra)] and [W3C XML Schema Definition Language (XSD) 1.1 Part 2: Datatypes](https://www.w3.org/TR/xmlschema11-2/) [[XMLSCHEMA11-2](#specification-bib-xmlschema11-2)]. 
<a id="specification-issue-container-generatedID-15"></a>



<a id="specification-h-note-22"></a>


Note



The value space of finite unordered maps and 
<a id="specification-ref-for-index-term-lists-2"></a>
[lists](https://infra.spec.whatwg.org/#list) does not include values having themselves as members, which cannot be represented in JSON.



 

Two values are considered equal if and only if they are the same element of the value space.

 

 
<a id="specification-JSON-mapping"></a>


The 
<a id="specification-ref-for-dfn-lexical-to-value-mapping-5"></a>
[lexical-to-value mapping](#specification-dfn-lexical-to-value-mapping)

 

maps every element of the lexical space to the result of parsing it into a 
<a id="specification-ref-for-dfn-rdf-string-12"></a>
[string](#specification-dfn-rdf-string), number (
<a id="specification-ref-for-index-term-xsd-double-6"></a>
[xsd:double](https://www.w3.org/TR/xmlschema11-2/#double)), finite unordered map, 
<a id="specification-ref-for-index-term-lists-3"></a>
[list](https://infra.spec.whatwg.org/#list), or literal value (
<a id="specification-ref-for-index-term-true-false-2"></a>
[`true`, `false`](https://infra.spec.whatwg.org/#boolean), and 
<a id="specification-ref-for-index-term-null-2"></a>
[`null`](https://infra.spec.whatwg.org/#nulls)). 

 

- A 
<a id="specification-ref-for-index-term-json-object-1"></a>
[JSON Object](https://www.rfc-editor.org/rfc/rfc8259#section-4) is mapped to a finite unordered map by transforming each object member into a 
<a id="specification-ref-for-index-term-map-entry-1"></a>
[map entry](https://infra.spec.whatwg.org/#map-entry) with the 
<a id="specification-ref-for-index-term-key-1"></a>
[key](https://infra.spec.whatwg.org/#map-key) taken from the member name and 
<a id="specification-ref-for-index-term-value-1"></a>
[value](https://infra.spec.whatwg.org/#map-value) taken by performing this mapping to the member value. 

 

- A 
<a id="specification-ref-for-index-term-json-array-1"></a>
[JSON Array](https://www.rfc-editor.org/rfc/rfc8259#section-5) is mapped to a 
<a id="specification-ref-for-index-term-lists-4"></a>
[list](https://infra.spec.whatwg.org/#list) such that this 
<a id="specification-ref-for-index-term-lists-5"></a>
[list](https://infra.spec.whatwg.org/#list) contains as many elements as the 
<a id="specification-ref-for-index-term-json-array-2"></a>
[JSON Array](https://www.rfc-editor.org/rfc/rfc8259#section-5) and, for every position i in the 
<a id="specification-ref-for-index-term-json-array-3"></a>
[array](https://www.rfc-editor.org/rfc/rfc8259#section-5), the element at the i-th position in the 
<a id="specification-ref-for-index-term-lists-6"></a>
[list](https://infra.spec.whatwg.org/#list) is the value that results from applying this mapping to the i-th element of the 
<a id="specification-ref-for-index-term-json-array-4"></a>
[array](https://www.rfc-editor.org/rfc/rfc8259#section-5).

 

- A 
<a id="specification-ref-for-index-term-json-number-1"></a>
[JSON Number](https://www.rfc-editor.org/rfc/rfc8259#section-6) is mapped to an 
<a id="specification-ref-for-index-term-xsd-double-7"></a>
[xsd:double](https://www.w3.org/TR/xmlschema11-2/#double) using a method consistent with 
<a id="specification-ref-for-index-term-doublelexicalmap-2"></a>
[doubleLexicalMap](https://www.w3.org/TR/xmlschema11-2/#f-doubleLexmap), which MUST strictly conform to the rounding method described in 
<a id="specification-ref-for-index-term-floatptround-2"></a>
[floatPtRound](https://www.w3.org/TR/xmlschema11-2/#f-floatPtRound) [[XMLSCHEMA11-2](#specification-bib-xmlschema11-2)]. 
<a id="specification-issue-container-generatedID-16"></a>



<a id="specification-h-note-23"></a>


Note



Some numbers cannot be represented as finite 
<a id="specification-ref-for-index-term-xsd-double-8"></a>
[xsd:double](https://www.w3.org/TR/xmlschema11-2/#double) values and may map to `+INF` or `-INF`. Such values cannot be represented as JSON Numbers, limiting the ability to serialize such values back to JSON.



 

 

- A 
<a id="specification-ref-for-index-term-json-string-1"></a>
[JSON String](https://www.rfc-editor.org/rfc/rfc8259#section-7) is mapped to a 
<a id="specification-ref-for-dfn-rdf-string-13"></a>
[string](#specification-dfn-rdf-string) after converting any escape sequences to the associated 
<a id="specification-ref-for-index-term-unicode-code-points-4"></a>
[Unicode code point](https://www.w3.org/TR/i18n-glossary/#dfn-code-point).

 

- A 
<a id="specification-ref-for-index-term-json-literal-name-1"></a>
[JSON literal name](https://www.rfc-editor.org/rfc/rfc8259#section-3) maps JSON `true`, `false`, and `null` values to [[INFRA](#specification-bib-infra)] 
<a id="specification-ref-for-index-term-true-false-3"></a>
[`true`](https://infra.spec.whatwg.org/#boolean), 
<a id="specification-ref-for-index-term-true-false-4"></a>
[`false`](https://infra.spec.whatwg.org/#boolean), and 
<a id="specification-ref-for-index-term-null-3"></a>
[`null`](https://infra.spec.whatwg.org/#nulls) values, respectively.

 

 

 

 
<a id="specification-issue-container-generatedID-17"></a>



<a id="specification-h-note-24"></a>


Note



 The finite unordered maps can be implemented with 
<a id="specification-ref-for-index-term-ordered-maps-1"></a>
[ordered maps](https://infra.spec.whatwg.org/#ordered-map) [[INFRA](#specification-bib-infra)] by systematically sorting key-value pairs by key (using 
<a id="specification-ref-for-index-term-unicode-code-points-5"></a>
[Unicode code point](https://www.w3.org/TR/i18n-glossary/#dfn-code-point) order). This ensures that lexical forms that differ only in the order of object members (e.g., `{"a": "b", "c": "d"}` and `{"c": "d", "a": "b"}`) are mapped to the same value. 



 

 

 
<a id="specification-section-skolemization"></a>

<a id="specification-L3861"></a>
<a id="specification-b-replacing-blank-nodes-with-iris"></a>
## B. Replacing Blank Nodes with IRIs
[](#specification-section-skolemization)

 

Blank nodes do not have identifiers in the RDF abstract data model. The 
<a id="specification-ref-for-dfn-blank-node-identifier-3"></a>
[blank node identifiers](#specification-dfn-blank-node-identifier) introduced by some concrete syntaxes have only local scope and are purely an artifact of the serialization.

 

In situations where stronger identification is needed, systems MAY systematically replace some or all of the blank nodes in an RDF graph with 
<a id="specification-ref-for-dfn-iri-51"></a>
[IRIs](#specification-dfn-iri). Systems wishing to do this SHOULD mint a new, globally unique IRI (a 
<a id="specification-dfn-skolem-iri"></a>
Skolem IRI) for each blank node so replaced.

 

This transformation produces a new graph which entails the original one (see also 
<a id="specification-ref-for-index-term-skolemization-1"></a>
[Skolemization](https://www.w3.org/TR/rdf12-semantics/#skolemization)). In this context it is important to note that Skolem IRIs and blank nodes are different in nature: while IRIs directly denote resources, blank nodes only indicate the existence of a resource. By producing Skolem IRIs, we create concrete witnesses of this existence. As Skolem IRIs are not local, this permits other graphs to subsequently use them, which is not possible with blank nodes.

 

Systems may wish to mint Skolem IRIs in such a way that they can recognize the IRIs as having been introduced solely to replace blank nodes. In some contexts, this allows a system to map Skolem IRIs back to blank nodes if needed. 

 

Systems that want Skolem IRIs to be recognizable outside of the system boundaries SHOULD use a well-known IRI [[RFC8615](#specification-bib-rfc8615)] with the registered name `genid`. This is an IRI that uses the HTTP or HTTPS scheme, or another scheme that has been specified to use well-known IRIs, and whose path component starts with `/.well-known/genid/`. 



For example, the authority responsible for the domain `example.com` could mint the following recognizable Skolem IRI:

 

```
http://example.com/.well-known/genid/d26a2d0e98334696f4ad70a677abc1f6
```

 
<a id="specification-issue-container-generatedID-18"></a>



<a id="specification-h-note-25"></a>


Note



RFC 8615 [[RFC8615](#specification-bib-rfc8615)] only specifies well-known URIs, not IRIs. For the purpose of this document, a well-known IRI is any IRI that results in a well-known 
<a id="specification-ref-for-dfn-uri-1"></a>
[URI](#specification-dfn-uri) after IRI-to-URI mapping [[RFC3987](#specification-bib-rfc3987)].



 

 
<a id="specification-privacy"></a>

<a id="specification-L3906"></a>
<a id="specification-c-privacy-considerations"></a>
## C. Privacy Considerations
[](#specification-privacy)



This section is non-normative.

 

RDF is used to express arbitrary application data, which may include the expression of personally identifiable information (PII) or other information which could be considered sensitive. Authors publishing such information are advised to carefully consider the needs and use of publishing such information, as well as the applicable regulations for the regions where the data is expected to be consumed and potentially revealed (e.g., [GDPR](https://gdpr.eu/), [CCPA](https://oag.ca.gov/privacy/ccpa), [others](https://termly.io/resources/infographics/privacy-laws-around-the-world/)), particularly whether authorization measures are needed for access to the data.

 

 
<a id="specification-security"></a>

<a id="specification-L3921"></a>
<a id="specification-d-security-considerations"></a>
## D. Security Considerations
[](#specification-security)



This section is non-normative.

 

The RDF Abstract Data Model is not used directly for conveying information. Concrete serialization forms are specifically intended to do so.

 

Applications can evaluate given data to infer more assertions or to dereference 
<a id="specification-ref-for-dfn-iri-52"></a>
[IRIs](#specification-dfn-iri), invoking the security considerations of the scheme for that IRI. Note in particular, the privacy issues in [[RFC3023](#specification-bib-rfc3023)] section 10 for HTTP IRIs. Data obtained from an inaccurate or malicious data source may lead to inaccurate or misleading conclusions, as well as the dereferencing of unintended IRIs. Care must be taken to align the trust in consulted resources with the sensitivity of the intended use of the data; inferences of potential medical treatments would likely require different trust than inferences for trip planning.

 

RDF is used to express arbitrary application data; security considerations will vary by domain of use. Security tools and protocols applicable to text (for example, PGP encryption, checksum validation, password-protected compression) can also be used on RDF documents. Security/privacy protocols ought to be imposed which reflect the sensitivity of the embedded information.

 

RDF can express data which is presented to the user, such as RDF Schema labels. Applications rendering 
<a id="specification-ref-for-dfn-rdf-string-14"></a>
[strings](#specification-dfn-rdf-string) retrieved from untrusted RDF documents, or using unescaped characters, ought to use warnings and other appropriate means to limit the possibility that malignant strings might be used to mislead the reader. The security considerations in the media type registration for XML ([[RFC3023](#specification-bib-rfc3023)] section 10) provide additional guidance around the expression of arbitrary data and markup.

 

RDF uses 
<a id="specification-ref-for-dfn-iri-53"></a>
[IRIs](#specification-dfn-iri) as term identifiers. Applications interpreting data expressed in RDF ought to address the security issues of [Internationalized Resource Identifiers (IRIs)](https://www.rfc-editor.org/rfc/rfc3987) [[RFC3987](#specification-bib-rfc3987)] Section 8, as well as [Uniform Resource Identifier (URI): Generic Syntax](https://www.rfc-editor.org/rfc/rfc3986) [[RFC3986](#specification-bib-rfc3986)] Section 7.

 

Multiple 
<a id="specification-ref-for-dfn-iri-54"></a>
[IRIs](#specification-dfn-iri) can have the same appearance. Characters in different scripts can look similar (for instance, a Cyrillic "о" can appear similar to a Latin "o"). A character followed by combining characters can have the same visual representation as another character (for example, LATIN SMALL LETTER "E" followed by COMBINING ACUTE ACCENT has the same visual representation as LATIN SMALL LETTER "E" WITH ACUTE). Any person or application that is writing or interpreting data in RDF must take care to use the IRI that matches the intended semantics, and avoid IRIs that may look similar. Further information about matching visually similar characters can be found in [Unicode Security Considerations](https://www.unicode.org/reports/tr36/tr36-15.html) [[UNICODE-SECURITY](#specification-bib-unicode-security)] and [Internationalized Resource Identifiers (IRIs)](https://www.rfc-editor.org/rfc/rfc3987) [[RFC3987](#specification-bib-rfc3987)] Section 8.

 

 [Comparing](#specification-graph-isomorphism) graphs, or [reasoning](https://www.w3.org/TR/rdf12-semantics/#simple_entailment_properties) with them, often relies on computing (sub)graph isomorphism, which is known to be computationally complex in the worst case. [Querying](https://www.w3.org/TR/sparql12-query/) graphs can also involve computationally complex operations. This means that malicious graphs can be constructed to cause RDF implementations to stall or run out of memory. Implementations processing graphs from untrusted sources are expected to provide mitigations; examples are given in the section on 
<a id="specification-ref-for-index-term-dataset-poisoning-1"></a>
[Dataset Poisoning](https://www.w3.org/TR/rdf-canon/#dataset-poisoning) in [[RDF-CANON](#specification-bib-rdf-canon)]. 

 
<a id="specification-issue-container-generatedID-19"></a>



<a id="specification-h-note-26"></a>


Note



These considerations are a more generic form of Security Considerations for [[RDF12-TURTLE](#specification-bib-rdf12-turtle)], [[RDF12-TRIG](#specification-bib-rdf12-trig)], [[RDF12-N-TRIPLES](#specification-bib-rdf12-n-triples)], and [[RDF12-N-QUADS](#specification-bib-rdf12-n-quads)].



 

 
<a id="specification-internationalization"></a>

<a id="specification-L3986"></a>
<a id="specification-e-internationalization-considerations"></a>
## E. Internationalization Considerations
[](#specification-internationalization)



This section is non-normative.

 

Unicode [[UNICODE](#specification-bib-unicode)] provides a mechanism for signaling direction within a string (see 
<a id="specification-ref-for-index-term-unicode-bidirectional-algorithm-2"></a>
[Unicode Bidirectional Algorithm](https://www.w3.org/TR/i18n-glossary/#dfn-unicode-bidi-algorithm) [[I18N-Glossary](#specification-bib-i18n-glossary)]). RDF provides a mechanism for specifying the 
<a id="specification-ref-for-dfn-base-direction-9"></a>
[base direction](#specification-dfn-base-direction) of a 
<a id="specification-ref-for-dfn-dir-lang-string-10"></a>
[directional language-tagged string](#specification-dfn-dir-lang-string) to signal the initial text direction of a string. For most human language strings, but particularly for those whose base direction cannot be accurately determined from the string content, is it valuable to have an external indicator in order to get the proper display and isolation of the value. One example of such an indicator is the [[HTML](#specification-bib-html)] 
<a id="specification-ref-for-index-term-dir-attribute-1"></a>
[dir attribute](https://html.spec.whatwg.org/multipage/dom.html#the-dir-attribute); see [[STRING-META](#specification-bib-string-meta)].

 

[JSON-LD 1.1](https://www.w3.org/TR/json-ld11/) [[JSON-LD11](#specification-bib-json-ld11)] introduced the 
<a id="specification-ref-for-index-term-i18n-namespace-2"></a>
[i18n namespace](https://www.w3.org/TR/json-ld11/#the-i18n-namespace) to use a datatype to specify both the base direction an 
<a id="specification-ref-for-dfn-language-tag-10"></a>
[language tag](#specification-dfn-language-tag) of an 
<a id="specification-ref-for-dfn-literal-27"></a>
[RDF literal](#specification-dfn-literal).

 

 
<a id="specification-iri-abnf"></a>

<a id="specification-L4007"></a>
<a id="specification-f-iri-grammar"></a>
## F. IRI Grammar
[](#specification-iri-abnf)



This section is non-normative.

 

 The following [[ABNF](#specification-bib-abnf)] grammar applies the changes from [[RFC3987](#specification-bib-rfc3987)] and [[RFC6874](#specification-bib-rfc6874)] to the section 
<a id="specification-ref-for-index-term-collected-abnf-for-uri-1"></a>
[Collected ABNF for URI](https://www.rfc-editor.org/rfc/rfc3986#appendix-A) of [[RFC3986](#specification-bib-rfc3986)] to give a consolidated grammar for IRIs. 

 

 This is provided for convenience only. If it differs from definitions in [[RFC3986](#specification-bib-rfc3986)], [[RFC3987](#specification-bib-rfc3987)], or any subsequent updates, then those definitions should be used. 

 

 

```
IRI            = scheme ":" ihier-part [ "?" iquery ] [ "#" ifragment ]

ihier-part     = "//" iauthority ipath-abempty
               / ipath-absolute
               / ipath-rootless
               / ipath-empty

IRI-reference  = IRI / irelative-ref

absolute-IRI   = scheme ":" ihier-part [ "?" iquery ]

irelative-ref  = irelative-part [ "?" iquery ] [ "#" ifragment ]

irelative-part = "//" iauthority ipath-abempty
               / ipath-absolute
               / ipath-noscheme
               / ipath-empty

scheme         = ALPHA *( ALPHA / DIGIT / "+" / "-" / "." )

iauthority     = [ iuserinfo "@" ] ihost [ ":" port ]
iuserinfo      = *( iunreserved / pct-encoded / sub-delims / ":" )
ihost          = IP-literal / IPv4address / ireg-name
port           = *DIGIT

IP-literal     = "[" ( IPv6address / IPv6addrz / IPvFuture  ) "]"

ZoneID         = 1*( unreserved / pct-encoded )

IPv6addrz      = IPv6address "%25" ZoneID

IPvFuture      = "v" 1*HEXDIG "." 1*( unreserved / sub-delims / ":" )

IPv6address    =                            6( h16 ":" ) ls32
               /                       "::" 5( h16 ":" ) ls32
               / [               h16 ] "::" 4( h16 ":" ) ls32
               / [ *1( h16 ":" ) h16 ] "::" 3( h16 ":" ) ls32
               / [ *2( h16 ":" ) h16 ] "::" 2( h16 ":" ) ls32
               / [ *3( h16 ":" ) h16 ] "::"    h16 ":"   ls32
               / [ *4( h16 ":" ) h16 ] "::"              ls32
               / [ *5( h16 ":" ) h16 ] "::"              h16
               / [ *6( h16 ":" ) h16 ] "::"

h16            = 1*4HEXDIG
ls32           = ( h16 ":" h16 ) / IPv4address
IPv4address    = dec-octet "." dec-octet "." dec-octet "." dec-octet

dec-octet      = DIGIT                 ; 0-9
               / %x31-39 DIGIT         ; 10-99
               / "1" 2DIGIT            ; 100-199
               / "2" %x30-34 DIGIT     ; 200-249
               / "25" %x30-35          ; 250-255

ireg-name      = *( iunreserved / pct-encoded / sub-delims )

ipath          = ipath-abempty   ; begins with "/" or is empty
               / ipath-absolute  ; begins with "/" but not "//"
               / ipath-noscheme  ; begins with a non-colon segment
               / ipath-rootless  ; begins with a segment
               / ipath-empty     ; zero characters

ipath-abempty  = *( "/" isegment )
ipath-absolute = "/" [ isegment-nz *( "/" isegment ) ]
ipath-noscheme = isegment-nz-nc *( "/" isegment )
ipath-rootless = isegment-nz *( "/" isegment )
ipath-empty    = 0

isegment       = *ipchar
isegment-nz    = 1*ipchar
isegment-nz-nc = 1*( iunreserved / pct-encoded / sub-delims / "@" )
               ; non-zero-length segment without any colon ":"

ipchar         = iunreserved / pct-encoded / sub-delims / ":" / "@"

iquery         = *( ipchar / iprivate / "/" / "?" )

ifragment      = *( ipchar / "/" / "?" )

iunreserved    = ALPHA / DIGIT / "-" / "." / "_" / "~" / ucschar

ucschar        = %xA0-D7FF / %xF900-FDCF / %xFDF0-FFEF
               / %x10000-1FFFD / %x20000-2FFFD / %x30000-3FFFD
               / %x40000-4FFFD / %x50000-5FFFD / %x60000-6FFFD
               / %x70000-7FFFD / %x80000-8FFFD / %x90000-9FFFD
               / %xA0000-AFFFD / %xB0000-BFFFD / %xC0000-CFFFD
               / %xD0000-DFFFD / %xE1000-EFFFD

iprivate       = %xE000-F8FF / %xF0000-FFFFD / %x100000-10FFFD

pct-encoded    = "%" HEXDIG HEXDIG

unreserved     = ALPHA / DIGIT / "-" / "." / "_" / "~"
reserved       = gen-delims / sub-delims
gen-delims     = ":" / "/" / "?" / "#" / "[" / "]" / "@"
sub-delims     = "!" / "$" / "&" / "'" / "(" / ")"
               / "*" / "+" / "," / ";" / "="
```

 

 

The ABNF can also be accessed directly from [iri-grammar.abnf](https://www.w3.org/TR/2026/CR-rdf12-concepts-20260407/iri-grammar.abnf).

 

 
<a id="specification-section-Acknowledgments"></a>

<a id="specification-L4125"></a>
<a id="specification-g-acknowledgments"></a>
## G. Acknowledgments
[](#specification-section-Acknowledgments)



This section is non-normative.

 
<a id="specification-acknowledgments-for-rdf-1-0"></a>

<a id="specification-L4128"></a>
<a id="specification-g-1-acknowledgments-for-rdf-1-0"></a>
### G.1 Acknowledgments for RDF 1.0
[](#specification-acknowledgments-for-rdf-1-0)



This section is non-normative.

 

The editors of the original version of the spec were Graham Klyne (Nine by Nine) and Jeremy J. Carroll (Hewlett Packard Labs).

 

This document contains a significant contribution from Pat Hayes, Sergey Melnik and Patrick Stickler, under whose leadership was developed the framework described in the RDF family of specifications for representing datatyped values, such as integers and dates.

 

The editors acknowledge valuable contributions from the following: Frank Manola, Pat Hayes, Dan Brickley, Jos de Roo, Dave Beckett, Patrick Stickler, Peter F. Patel-Schneider, Jerome Euzenat, Massimo Marchiori, Tim Berners-Lee, Dave Reynolds and Dan Connolly.

 

Jeremy Carroll thanks Oreste Signore, his host at the W3C Office in Italy and Istituto di Scienza e Tecnologie dell'Informazione "Alessandro Faedo", part of the Consiglio Nazionale delle Ricerche, where Jeremy is a visiting researcher.

 

This document is a product of extended deliberations by the RDFcore Working Group, whose members have included: Art Barstow (W3C), Dave Beckett (ILRT), Dan Brickley (ILRT), Dan Connolly (W3C), Jeremy Carroll (Hewlett Packard), Ron Daniel (Interwoven Inc), Bill dehOra (InterX), Jos De Roo (AGFA), Jan Grant (ILRT), Graham Klyne (Nine by Nine), Frank Manola (MITRE Corporation), Brian McBride (Hewlett Packard), Eric Miller (W3C), Stephen Petschulat (IBM), Patrick Stickler (Nokia), Aaron Swartz (HWG), Mike Dean (BBN Technologies / Verizon), R. V. Guha (Alpiri Inc), Pat Hayes (IHMC), Sergey Melnik (Stanford University) and Martyn Horner (Profium Ltd).

 

This specification also draws upon an earlier RDF Model and Syntax document edited by Ora Lassilla and Ralph Swick, and RDF Schema edited by Dan Brickley and R. V. Guha. RDF and RDF Schema Working Group members who contributed to this earlier work are: Nick Arnett (Verity), Tim Berners-Lee (W3C), Tim Bray (Textuality), Dan Brickley (ILRT / University of Bristol), Walter Chang (Adobe), Sailesh Chutani (Oracle), Dan Connolly (W3C), Ron Daniel (DATAFUSION), Charles Frankston (Microsoft), Patrick Gannon (CommerceNet), R. V. Guha (Epinions, previously of Netscape Communications), Tom Hill (Apple Computer), Arthur van Hoff (Marimba), Renato Iannella (DSTC), Sandeep Jain (Oracle), Kevin Jones, (InterMind), Emiko Kezuka (Digital Vision Laboratories), Joe Lapp (webMethods Inc.), Ora Lassila (Nokia Research Center), Andrew Layman (Microsoft), Ralph LeVan (OCLC), John McCarthy (Lawrence Berkeley National Laboratory), Chris McConnell (Microsoft), Murray Maloney (Grif), Michael Mealling (Network Solutions), Norbert Mikula (DataChannel), Eric Miller (OCLC), Jim Miller (W3C, emeritus), Frank Olken (Lawrence Berkeley National Laboratory), Jean Paoli (Microsoft), Sri Raghavan (Digital/Compaq), Lisa Rein (webMethods Inc.), Paul Resnick (University of Michigan), Bill Roberts (KnowledgeCite), i Tsuyoshi Sakata (Digital Vision Laboratories), Bob Schloss (IBM), Leon Shklar (Pencom Web Works), David Singer (IBM), Wei (William) Song (SISU), Neel Sundaresan (IBM), Ralph Swick (W3C), Naohiko Uramoto (IBM), Charles Wicksteed (Reuters Ltd.), Misha Wolf (Reuters Ltd.) and Lauren Wood (SoftQuad).

 

 
<a id="specification-acknowledgments-for-rdf-1-1"></a>

<a id="specification-L4189"></a>
<a id="specification-g-2-acknowledgments-for-rdf-1-1"></a>
### G.2 Acknowledgments for RDF 1.1
[](#specification-acknowledgments-for-rdf-1-1)



This section is non-normative.

 

The editors of the RDF 1.1 version of the spec were Richard Cyganiak (DERI), David Wood (3 Round Stones), and Markus Lanthaler (Graz University of Technology).

 

The editors acknowledge valuable contributions from Thomas Baker, Tim Berners-Lee, David Booth, Dan Brickley, Gavin Carothers, Jeremy Carroll, Pierre-Antoine Champin, Dan Connolly, John Cowan, Martin J. Dürst, Alex Hall, Steve Harris, Sandro Hawke, Pat Hayes, Ivan Herman, Peter F. Patel-Schneider, Addison Phillips, Eric Prud'hommeaux, Nathan Rixham, Andy Seaborne, Leif Halvard Silli, Guus Schreiber, Dominik Tomaszuk, and Antoine Zimmermann.

 

The membership of the RDF Working Group included Thomas Baker, Scott Bauer, Dan Brickley, Gavin Carothers, Pierre-Antoine Champin, Olivier Corby, Richard Cyganiak, Souripriya Das, Ian Davis, Lee Feigenbaum, Fabien Gandon, Charles Greer, Alex Hall, Steve Harris, Sandro Hawke, Pat Hayes, Ivan Herman, Nicholas Humfrey, Kingsley Idehen, Gregg Kellogg, Markus Lanthaler, Arnaud Le Hors, Peter F. Patel-Schneider, Eric Prud'hommeaux, Yves Raimond, Nathan Rixham, Guus Schreiber, Andy Seaborne, Manu Sporny, Thomas Steiner, Ted Thibodeau, Mischa Tuffield, William Waites, Jan Wielemaker, David Wood, Zhe Wu, and Antoine Zimmermann.

 

 
<a id="specification-acknowledgments-for-rdf-1-2"></a>

<a id="specification-L4215"></a>
<a id="specification-g-3-acknowledgments-for-rdf-1-2"></a>
### G.3 Acknowledgments for RDF 1.2
[](#specification-acknowledgments-for-rdf-1-2)



This section is non-normative.

 

In addition to the editors, the following people have contributed to this specification: 
<a id="specification-gh-contributors"></a>
Denis Ah-Kang, doerthe, Dominik Tomaszuk, Enrico Franconi, james anderson, Niklas Lindström, Peter F. Patel-Schneider, Ruben Taelman, Sarven Capadisli, Ted Thibodeau Jr, Thomas Tanon, and William Van Woensel 

 

Members of the RDF & SPARQL Working Group Group included Vladimir Alexiev, James Anderson, Amin Anjomshoaa, Julián Arenas-Guerrero, Dörthe Arndt, Bilal Ben Mahria, Erich Bremer, Dan Brickley, Kurt Cagle, Sarven Capadisli, Rémi Ceres, Pierre-Antoine Champin, David Chaves-Fraga, Souripriya Das, Daniil Dobriy, Enrico Franconi, Jeffrey Phillips Freeman, Fabien Gandon, Benjamin Goering, Damien Graux, Adrian Gschwend, Olaf Hartig, Timothée Haudebourg, Ian Horrocks, Gregg Kellogg, Mark Kim, Jose Emilio Labra Gayo, Ora Lassila, Richard Lea, Niklas Lindström, Pasquale Lisena, Thomas Lörtsch, Matthew Nguyen, Peter Patel-Schneider, Thomas Pellissier Tanon, Dave Raggett, Jean-Yves ROSSI, Felix Sasaki, Andy Seaborne, Alan Snyder, Stuart Sutton, Ruben Taelman, Ted Thibodeau Jr, Dominik Tomaszuk, Raphaël Troncy, William Van Woensel, Gregory Williams, Jesse Wright, Achille Zappa, and Antoine Zimmermann. 

 
<a id="specification-issue-container-generatedID-20"></a>



<a id="specification-h-ednote"></a>


Editor's note



Recognize members of the Task Force? Not an easy to find list of contributors.



 

 

 
<a id="specification-changes-12"></a>

<a id="specification-L4279"></a>
<a id="specification-h-changes-between-rdf-1-1-and-rdf-1-2"></a>
## H. Changes between RDF 1.1 and RDF 1.2
[](#specification-changes-12)



This section is non-normative.

 

 

- Added [1.10 RDF Version Announcement](#specification-section-version-announcement) for announcing RDF versions in RDF documents via the HTTP `Content-Type` header and/or syntax.

 

- Added [4.3 Dataset as a Set of Quads](#specification-section-dataset-quad) for informative definition of a 
<a id="specification-ref-for-dfn-quad-4"></a>
[quad](#specification-dfn-quad).

 

- Added [1.5 Triple Terms and Reification](#specification-section-triple-terms-reification) and definitions for 
<a id="specification-ref-for-dfn-triple-term-28"></a>
[triple term](#specification-dfn-triple-term) and 
<a id="specification-ref-for-dfn-asserted-triple-13"></a>
[asserted triple](#specification-dfn-asserted-triple) and extended the definition of 
<a id="specification-ref-for-dfn-rdf-triple-41"></a>
[RDF triple](#specification-dfn-rdf-triple) to permit triple terms as objects. Also defines 
<a id="specification-ref-for-dfn-reifier-7"></a>
[reifier](#specification-dfn-reifier) and 
<a id="specification-ref-for-dfn-reifying-triple-6"></a>
[reifying triple](#specification-dfn-reifying-triple).

 

- Added the 
<a id="specification-ref-for-dfn-base-direction-10"></a>
[base direction](#specification-dfn-base-direction) component as part of a 
<a id="specification-ref-for-dfn-literal-28"></a>
[literal](#specification-dfn-literal), and a description of its use in [3.4.3 Initial Text Direction](#specification-section-text-direction).

 

- Improved the use of IRI terminology, and added [F. IRI Grammar](#specification-iri-abnf). This improves the language using 
<a id="specification-ref-for-dfn-relative-iri-2"></a>
[relative IRI references](#specification-dfn-relative-iri) and clarifies that, in the abstract syntax, IRIs are resolved, avoiding the incorrect use of "absolute IRI".

 

- Changed reference from DOM4, which was not a recommendation at the time, to [[DOM](#specification-bib-dom)], making the definitions of 
<a id="specification-ref-for-dfn-rdf-html-3"></a>
[`rdf:HTML`](../source/specification.html#dfn-rdf-html) and 
<a id="specification-ref-for-dfn-rdf-xmlliteral-3"></a>
[`rdf:XMLLiteral`](../source/specification.html#dfn-rdf-xmlliteral) datatypes normative.

 

- Added [A. Additional Datatypes](#specification-section-additional-datatypes) and moved the sections about the 
<a id="specification-ref-for-dfn-rdf-html-4"></a>
[`rdf:HTML`](../source/specification.html#dfn-rdf-html) and 
<a id="specification-ref-for-dfn-rdf-xmlliteral-4"></a>
[`rdf:XMLLiteral`](../source/specification.html#dfn-rdf-xmlliteral) datatypes to this appendix.

 

- Added the 
<a id="specification-ref-for-dfn-rdf-json-3"></a>
[`rdf:JSON`](../source/specification.html#dfn-rdf-json) datatype, the definition of which is adopted from 
<a id="specification-ref-for-index-term-section-10-2-the-rdf-json-datatype-1"></a>
[Section 10.2 The `rdf:JSON` Datatype](https://www.w3.org/TR/json-ld11/#the-rdf-json-datatype) in [[JSON-LD11](#specification-bib-json-ld11)]. Note that the [value space](#specification-JSON-value-space) defined here updates the 
<a id="specification-ref-for-dfn-value-space-9"></a>
[value space](#specification-dfn-value-space) of the 
<a id="specification-ref-for-index-term-section-10-2-the-rdf-json-datatype-2"></a>
[`rdf:JSON`](https://www.w3.org/TR/json-ld11/#the-rdf-json-datatype) datatype defined in [JSON-LD 1.1](https://www.w3.org/TR/json-ld11/) [[JSON-LD11](#specification-bib-json-ld11)]

 

- Clarify Unicode terminology, using 
<a id="specification-ref-for-index-term-unicode-code-points-6"></a>
[Unicode code points](https://www.w3.org/TR/i18n-glossary/#dfn-code-point), and restriction to the XML 
<a id="specification-ref-for-index-term-char-1"></a>
[Char](https://www.w3.org/TR/xml11/#charsets) production. Also removes obsolete recommendations for the use of Normalization Form C in literals. Adds a definition of 
<a id="specification-ref-for-dfn-rdf-string-15"></a>
[string](#specification-dfn-rdf-string) that can be used in other RDF documents.

 

- Minor edit to improve the example about distinguishing literals, IRIs, and blank nodes in [3.1 Triples](#specification-section-triples).

 

- Implementations were previously allowed to normalize language tags to lower case, which made it ambiguous whether two literals with language tags that differed only by case represented the same literal, or distinct literals. RDF 1.2 requires that language tags be case-insensitively unique but does not specify the common formatting to be used. Two literals with the same lexical form and language tags that differ only by case are the same literal. Implementations can either follow the advice to normalize to lower case, use the recommended BCP47 format, or do something else, as long it is performed consistently.

 

- Added explicit definitions of 
<a id="specification-ref-for-dfn-blank-node-equality-3"></a>
[blank node equality](#specification-dfn-blank-node-equality), 
<a id="specification-ref-for-dfn-rdf-term-equality-5"></a>
[RDF term equality](#specification-dfn-rdf-term-equality), and 
<a id="specification-ref-for-dfn-triple-equality-4"></a>
[triple equality](#specification-dfn-triple-equality).

 

- Removed the section on the canonical mapping for the 
<a id="specification-ref-for-dfn-rdf-xmlliteral-5"></a>
[`rdf:XMLLiteral`](../source/specification.html#dfn-rdf-xmlliteral) datatype.

 

- Refer to the definition and discussion of 
<a id="specification-ref-for-index-term-rdf-semantics-recognizing-2"></a>
[RDF Semantics, "recognizing"](https://www.w3.org/TR/rdf12-semantics/#dfn-recognize) datatype IRIs, instead of Recognized datatype IRIs.

 

- The informal terminology "RDF processor" has been removed.

 

 
<a id="specification-issue-container-generatedID-21"></a>



<a id="specification-h-note-27"></a>


Note



A detailed overview of the differences between RDF versions 1.1 and 1.2 can be found in [What’s New in RDF 1.2](https://w3c.github.io/rdf-new/spec/) [[RDF12-NEW](#specification-bib-rdf12-new)].



 

 
<a id="specification-index"></a>

<a id="specification-L4342"></a>
<a id="specification-i-index"></a>
## I. Index
[](#specification-index)


<a id="specification-index-defined-here"></a>

<a id="specification-L4342"></a>
<a id="specification-i-1-terms-defined-by-this-specification"></a>
### I.1 Terms defined by this specification
[](#specification-index-defined-here)

 

 

-  [abstract syntax](#specification-dfn-abstract-syntax) §1.9



-  [appearing](#specification-dfn-appear) §3.2



-  [asserted](#specification-dfn-asserted-triple) §3.



-  [base direction](#specification-dfn-base-direction) §3.4



-  [base IRI](#specification-dfn-base-iri) §3.3.1



-  [Basic conformance](#specification-dfn-basic) §2.



-  [basic RDF terms](#specification-dfn-basic-rdf-term) §3.2



-  [Blank node equality](#specification-dfn-blank-node-equality) §3.5



-  [Blank node identifiers](#specification-dfn-blank-node-identifier) §3.5



-  [Blank nodes](#specification-dfn-blank-node) §3.5



-  [concrete RDF syntax](#specification-dfn-concrete-rdf-syntax) §1.9



-  [dataset-isomorphic](#specification-dfn-dataset-isomorphism) §4.1



-  [datatype](#specification-dfn-datatype) §5.



-  [datatype IRI](#specification-dfn-datatype-iri) §3.4



-  [default graph](#specification-dfn-default-graph) §4.



-  [denotes](#specification-dfn-denote) §1.2



-  [directional language-tagged string](#specification-dfn-dir-lang-string) §3.4



-  [Entailment](#specification-dfn-entailment) §1.8



-  [Equivalence](#specification-dfn-equivalence) §1.8



-  [fragment identifiers](#specification-dfn-fragment-identifier) §6.



-  [Full conformance](#specification-dfn-full) §2.



-  [generalized RDF dataset](#specification-dfn-generalized-rdf-dataset) §7.2



-  [generalized RDF graph](#specification-dfn-generalized-rdf-graph) §7.2



-  [generalized RDF triple](#specification-dfn-generalized-rdf-triple) §7.2



-  [graph name](#specification-dfn-graph-name) §4.



-  [ground](#specification-dfn-ground) §3.2



-  [ill-typed](#specification-dfn-ill-typed) §3.4.2



-  [Inconsistency](#specification-dfn-inconsistent) §1.8



-  [IRI](#specification-dfn-iri) §3.3



-  [IRI equality](#specification-dfn-iri-equality) §3.3



-  [IRI references](#specification-dfn-iri-reference) §3.3



-  [isomorphic](#specification-dfn-graph-isomorphism) §3.7



-  [isomorphic RDF-term mapping](#specification-dfn-isomorphic-rdf-term-mapping) §3.7



-  [language tag](#specification-dfn-language-tag) §3.4



-  [language-tagged string](#specification-dfn-language-tagged-string) §3.4



-  [lexical form](#specification-dfn-lexical-form) §3.4



-  [lexical space](#specification-dfn-lexical-space) §5.



-  [lexical-to-value mapping](#specification-dfn-lexical-to-value-mapping) §5.



-  [literal](#specification-dfn-literal) §3.4



-  [Literal term equality](#specification-dfn-literal-term-equality) §3.4



-  [literal value](#specification-dfn-literal-value) §3.4.2



-  [named graphs](#specification-dfn-named-graph) §4.



-  [namespace](#specification-dfn-namespace) §1.4



-  [namespace IRI](#specification-dfn-namespace-iri) §1.4



-  [namespace prefix](#specification-dfn-namespace-prefix) §1.4



-  [nodes](#specification-dfn-node) §3.1



-  [object](#specification-dfn-object) §3.1



-  [predicate](#specification-dfn-predicate) §3.1



-  [property](#specification-dfn-property) §1.2



-  [proposition](#specification-dfn-proposition) §1.8



-  [quad](#specification-dfn-quad) §4.3



-  [RDF dataset](#specification-dfn-rdf-dataset) §4.



-  [RDF document](#specification-dfn-rdf-document) §1.9



-  [RDF graph](#specification-dfn-rdf-graph) §3.



-  [RDF Reference IRI](#specification-dfn-rdf-reference) §3.3.1



-  [RDF source](#specification-dfn-rdf-source) §1.6



-  [RDF statement](#specification-dfn-rdf-statement) §1.2



-  [RDF string](#specification-dfn-rdf-string) §2.2



-  [RDF term equality](#specification-dfn-rdf-term-equality) §3.2



-  [RDF terms](#specification-dfn-rdf-term) §3.2



-  [RDF triple](#specification-dfn-rdf-triple) §3.1



-  [RDF vocabulary](#specification-dfn-rdf-vocabulary) §1.4



-  [RDF-compatible XSD types](#specification-dfn-rdf-compatible-xsd-types) §5.1



-  [`rdf:HTML`](../source/specification.html#dfn-rdf-html) §A.1



-  [`rdf:JSON`](../source/specification.html#dfn-rdf-json) §A.3



-  [`rdf:XMLLiteral`](../source/specification.html#dfn-rdf-xmlliteral) §A.2



-  [referent](#specification-dfn-referent) §1.3



-  [reifier](#specification-dfn-reifier) §1.5



-  [reifying triple](#specification-dfn-reifying-triple) §1.5



-  [relative IRI references](#specification-dfn-relative-iri) §3.3.1



-  [resources](#specification-dfn-resource) §1.2



-  [simple literals](#specification-dfn-simple-literal) §3.4.1



-  [Skolem IRI](#specification-dfn-skolem-iri) §B.



-  [subject](#specification-dfn-subject) §3.1



-  [symmetric RDF dataset](#specification-dfn-symmetric-rdf-dataset) §7.1



-  [symmetric RDF graph](#specification-dfn-symmetric-rdf-graph) §7.1



-  [symmetric RDF triple](#specification-dfn-symmetric-rdf-triple) §7.1



-  [transparent](#specification-dfn-transparent) §1.5



-  [triple annotation](#specification-dfn-triple-annotation) §1.5



-  [Triple equality](#specification-dfn-triple-equality) §3.1



-  [triple term](#specification-dfn-triple-term) §3.6



-  [URIs](#specification-dfn-uri) §3.3



-  [value space](#specification-dfn-value-space) §5.



-  [version label](#specification-dfn-version-label) §2.1

 

 


<a id="specification-index-defined-elsewhere"></a>

<a id="specification-L4515"></a>
<a id="specification-i-2-terms-defined-by-reference"></a>
### I.2 Terms defined by reference
[](#specification-index-defined-elsewhere)

 

 

-  [[BCP47](#specification-bib-bcp47)] defines the following: 

 

  -  
<a id="specification-index-term-bcp-47-section-4-5"></a>
BCP 47 section 4.5 



  -  
<a id="specification-index-term-section-2-2-9"></a>
section 2.2.9 

 

 



-  [[DID-CORE](#specification-bib-did-core)] defines the following: 

 

  -  
<a id="specification-index-term-did-syntax"></a>
DID syntax 

 

 



-  [[DOM](#specification-bib-dom)] defines the following: 

 

  -  
<a id="specification-index-term-documentfragment"></a>
DocumentFragment 



  -  
<a id="specification-index-term-dom-nodes"></a>
DOM nodes 



  -  
<a id="specification-index-term-isequalnode-othernode-for-node"></a>
`isEqualNode(otherNode)` (for `Node`) 



  -  
<a id="specification-index-term-normalize-for-node"></a>
`normalize()` (for `Node`) 

 

 



-  [[HTML](#specification-bib-html)] defines the following: 

 

  -  
<a id="specification-index-term-dir-attribute"></a>
dir attribute 

 

 



-  [[HTML5](#specification-bib-html5)] defines the following: 

 

  -  
<a id="specification-index-term-html-fragment-parsing-algorithm"></a>
HTML fragment parsing algorithm 

 

 



-  [[I18N-GLOSSARY](#specification-bib-i18n-glossary)] defines the following: 

 

  -  
<a id="specification-index-term-ascii-case-insensitive-matching"></a>
ASCII case-insensitive matching 



  -  
<a id="specification-index-term-bidi-isolation"></a>
bidi isolation 



  -  
<a id="specification-index-term-case-sensitive-matching"></a>
case-sensitive matching 



  -  
<a id="specification-index-term-code-units"></a>
code units 



  -  
<a id="specification-index-term-normalization-form-c"></a>
Normalization Form C 



  -  
<a id="specification-index-term-surrogate-code-points"></a>
surrogate code points 



  -  
<a id="specification-index-term-unicode-bidirectional-algorithm"></a>
Unicode Bidirectional Algorithm 



  -  
<a id="specification-index-term-unicode-character-encoding"></a>
Unicode character encoding 



  -  
<a id="specification-index-term-unicode-code-points"></a>
Unicode code points 



  -  
<a id="specification-index-term-unicode-scalar-values"></a>
Unicode scalar values 

 

 



-  [[INFRA](#specification-bib-infra)] defines the following: 

 

  -  
<a id="specification-index-term-key"></a>
key 



  -  
<a id="specification-index-term-lists"></a>
lists 



  -  
<a id="specification-index-term-map-entry"></a>
map entry 



  -  
<a id="specification-index-term-null"></a>
null 



  -  
<a id="specification-index-term-ordered-maps"></a>
ordered maps 



  -  
<a id="specification-index-term-true-false"></a>
true, false 



  -  
<a id="specification-index-term-value"></a>
value 

 

 



-  [[JSON-LD11](#specification-bib-json-ld11)] defines the following: 

 

  -  
<a id="specification-index-term-i18n-namespace"></a>
i18n namespace 



  -  
<a id="specification-index-term-section-10-2-the-rdf-json-datatype"></a>
Section 10.2 The rdf:JSON Datatype 

 

 



-  [[OWL2-OVERVIEW](#specification-bib-owl2-overview)] defines the following: 

 

  -  
<a id="specification-index-term-owl-2"></a>
OWL 2 

 

 



-  [[OWL2-SYNTAX](#specification-bib-owl2-syntax)] defines the following: 

 

  -  
<a id="specification-index-term-custom-datatypes"></a>
custom datatypes 

 

 



-  [[RDF-CANON](#specification-bib-rdf-canon)] defines the following: 

 

  -  
<a id="specification-index-term-dataset-poisoning"></a>
Dataset Poisoning 

 

 



-  [[RDF12-SEMANTICS](#specification-bib-rdf12-semantics)] defines the following: 

 

  -  
<a id="specification-index-term-entailment-regime"></a>
entailment regime 



  -  
<a id="specification-index-term-interpretation"></a>
interpretation 



  -  
<a id="specification-index-term-rdf-semantics-recognizing"></a>
RDF Semantics, "recognizing" 



  -  
<a id="specification-index-term-semantic-extensions"></a>
semantic extensions 



  -  
<a id="specification-index-term-skolemization"></a>
Skolemization 

 

 



-  [[RDF12-XML](#specification-bib-rdf12-xml)] defines the following: 

 

  -  
<a id="specification-index-term-parsetype-literal"></a>
@parseType="literal" 

 

 



-  [[RFC3986](#specification-bib-rfc3986)] defines the following: 

 

  -  
<a id="specification-index-term-base-iri-can-be-established"></a>
base IRI can be established 



  -  
<a id="specification-index-term-collected-abnf-for-uri"></a>
Collected ABNF for URI 



  -  
<a id="specification-index-term-fragment-identifier"></a>
fragment identifier 



  -  
<a id="specification-index-term-iri-scheme"></a>
IRI scheme 



  -  
<a id="specification-index-term-path-component"></a>
path component 



  -  
<a id="specification-index-term-relative-reference"></a>
relative reference 



  -  
<a id="specification-index-term-resolved"></a>
resolved 



  -  
<a id="specification-index-term-resolved-against"></a>
resolved against 

 

 



-  [[RFC3987](#specification-bib-rfc3987)] defines the following: 

 

  -  
<a id="specification-index-term-section-1-3"></a>
section 1.3 



  -  
<a id="specification-index-term-section-3-1"></a>
section 3.1 



  -  
<a id="specification-index-term-section-5"></a>
Section 5 



  -  
<a id="specification-index-term-section-5-3-1"></a>
section 5.3.1 

 

 



-  [[RFC7230](#specification-bib-rfc7230)] defines the following: 

 

  -  
<a id="specification-index-term-http-uri-scheme"></a>
HTTP URI scheme 



  -  
<a id="specification-index-term-http-uri"></a>
http-URI 



  -  
<a id="specification-index-term-scheme-rules-for-http-https"></a>
scheme rules for HTTP/HTTPS 

 

 



-  [[RFC8259](#specification-bib-rfc8259)] defines the following: 

 

  -  
<a id="specification-index-term-json-array"></a>
JSON Array 



  -  
<a id="specification-index-term-json-grammar"></a>
JSON Grammar 



  -  
<a id="specification-index-term-json-literal-name"></a>
JSON literal name 



  -  
<a id="specification-index-term-json-number"></a>
JSON Number 



  -  
<a id="specification-index-term-json-object"></a>
JSON Object 



  -  
<a id="specification-index-term-json-string"></a>
JSON String 

 

 



-  [[SPARQL12-QUERY](#specification-bib-sparql12-query)] defines the following: 

 

  -  
<a id="specification-index-term-the-same-concept-of-an-rdf-dataset"></a>
the same concept of an RDF Dataset 

 

 



-  [[SWBP-N-ARYRELATIONS](#specification-bib-swbp-n-aryrelations)] defines the following: 

 

  -  
<a id="specification-index-term-indirectly-expressed-in-rdf"></a>
indirectly expressed in RDF 

 

 



-  [[SWBP-XSCH-DATATYPES](#specification-bib-swbp-xsch-datatypes)] defines the following: 

 

  -  
<a id="specification-index-term-user-defined-simple-xml-schema-datatypes"></a>
user-defined simple XML Schema datatypes 

 

 



-  [[WEBARCH](#specification-bib-webarch)] defines the following: 

 

  -  
<a id="specification-index-term-content-negotiation"></a>
content negotiation 



  -  
<a id="specification-index-term-dereferences"></a>
dereferences 



  -  
<a id="specification-index-term-iri-collision"></a>
IRI collision 



  -  
<a id="specification-index-term-iri-owner"></a>
IRI owner 



  -  
<a id="specification-index-term-uri-persistence"></a>
URI persistence 

 

 



-  [[XML11](#specification-bib-xml11)] defines the following: 

 

  -  
<a id="specification-index-term-char"></a>
Char 



  -  
<a id="specification-index-term-xml-content"></a>
XML content 

 

 



-  [[XMLSCHEMA11-2](#specification-bib-xmlschema11-2)] defines the following: 

 

  -  
<a id="specification-index-term-doublelexicalmap"></a>
doubleLexicalMap 



  -  
<a id="specification-index-term-floatptround"></a>
floatPtRound 



  -  
<a id="specification-index-term-xsd-anyuri"></a>
xsd:anyURI 



  -  
<a id="specification-index-term-xsd-base64binary"></a>
xsd:base64Binary 



  -  
<a id="specification-index-term-xsd-boolean"></a>
xsd:boolean 



  -  
<a id="specification-index-term-xsd-byte"></a>
xsd:byte 



  -  
<a id="specification-index-term-xsd-date"></a>
xsd:date 



  -  
<a id="specification-index-term-xsd-datetime"></a>
xsd:dateTime 



  -  
<a id="specification-index-term-xsd-datetimestamp"></a>
xsd:dateTimeStamp 



  -  
<a id="specification-index-term-xsd-daytimeduration"></a>
xsd:dayTimeDuration 



  -  
<a id="specification-index-term-xsd-decimal"></a>
xsd:decimal 



  -  
<a id="specification-index-term-xsd-double"></a>
xsd:double 



  -  
<a id="specification-index-term-xsd-duration"></a>
xsd:duration 



  -  
<a id="specification-index-term-xsd-entities"></a>
xsd:ENTITIES 



  -  
<a id="specification-index-term-xsd-entity"></a>
xsd:ENTITY 



  -  
<a id="specification-index-term-xsd-float"></a>
xsd:float 



  -  
<a id="specification-index-term-xsd-gday"></a>
xsd:gDay 



  -  
<a id="specification-index-term-xsd-gmonth"></a>
xsd:gMonth 



  -  
<a id="specification-index-term-xsd-gmonthday"></a>
xsd:gMonthDay 



  -  
<a id="specification-index-term-xsd-gyear"></a>
xsd:gYear 



  -  
<a id="specification-index-term-xsd-gyearmonth"></a>
xsd:gYearMonth 



  -  
<a id="specification-index-term-xsd-hexbinary"></a>
xsd:hexBinary 



  -  
<a id="specification-index-term-xsd-id"></a>
xsd:ID 



  -  
<a id="specification-index-term-xsd-idref"></a>
xsd:IDREF 



  -  
<a id="specification-index-term-xsd-idrefs"></a>
xsd:IDREFS 



  -  
<a id="specification-index-term-xsd-int"></a>
xsd:int 



  -  
<a id="specification-index-term-xsd-integer"></a>
xsd:integer 



  -  
<a id="specification-index-term-xsd-language"></a>
xsd:language 



  -  
<a id="specification-index-term-xsd-long"></a>
xsd:long 



  -  
<a id="specification-index-term-xsd-name"></a>
xsd:Name 



  -  
<a id="specification-index-term-xsd-ncname"></a>
xsd:NCName 



  -  
<a id="specification-index-term-xsd-negativeinteger"></a>
xsd:negativeInteger 



  -  
<a id="specification-index-term-xsd-nmtoken"></a>
xsd:NMTOKEN 



  -  
<a id="specification-index-term-xsd-nmtokens"></a>
xsd:NMTOKENS 



  -  
<a id="specification-index-term-xsd-nonnegativeinteger"></a>
xsd:nonNegativeInteger 



  -  
<a id="specification-index-term-xsd-nonpositiveinteger"></a>
xsd:nonPositiveInteger 



  -  
<a id="specification-index-term-xsd-normalizedstring"></a>
xsd:normalizedString 



  -  
<a id="specification-index-term-xsd-notation"></a>
xsd:NOTATION 



  -  
<a id="specification-index-term-xsd-positiveinteger"></a>
xsd:positiveInteger 



  -  
<a id="specification-index-term-xsd-qname"></a>
xsd:QName 



  -  
<a id="specification-index-term-xsd-short"></a>
xsd:short 



  -  
<a id="specification-index-term-xsd-string"></a>
xsd:string 



  -  
<a id="specification-index-term-xsd-time"></a>
xsd:time 



  -  
<a id="specification-index-term-xsd-token"></a>
xsd:token 



  -  
<a id="specification-index-term-xsd-unsignedbyte"></a>
xsd:unsignedByte 



  -  
<a id="specification-index-term-xsd-unsignedint"></a>
xsd:unsignedInt 



  -  
<a id="specification-index-term-xsd-unsignedlong"></a>
xsd:unsignedLong 



  -  
<a id="specification-index-term-xsd-unsignedshort"></a>
xsd:unsignedShort 



  -  
<a id="specification-index-term-xsd-yearmonthduration"></a>
xsd:yearMonthDuration 

 

 

 

 



 
<a id="specification-references"></a>

<a id="specification-L4873"></a>
<a id="specification-j-references"></a>
## J. References
[](#specification-references)


<a id="specification-normative-references"></a>

<a id="specification-L4873"></a>
<a id="specification-j-1-normative-references"></a>
### J.1 Normative references
[](#specification-normative-references)

 


<a id="specification-bib-bcp47"></a>


[BCP47]



 [Tags for Identifying Languages](https://www.rfc-editor.org/rfc/rfc5646). A. Phillips, Ed.; M. Davis, Ed. IETF. September 2009. Best Current Practice. URL: [https://www.rfc-editor.org/rfc/rfc5646](https://www.rfc-editor.org/rfc/rfc5646) 


<a id="specification-bib-dom"></a>


[DOM]



 [DOM Standard](https://dom.spec.whatwg.org/). Anne van Kesteren. WHATWG. Living Standard. URL: [https://dom.spec.whatwg.org/](https://dom.spec.whatwg.org/) 


<a id="specification-bib-html5"></a>


[HTML5]



 [HTML5](https://www.w3.org/TR/html5/). Ian Hickson; Robin Berjon; Steve Faulkner; Travis Leithead; Erika Doyle Navara; Theresa O'Connor; Silvia Pfeiffer. W3C. 27 March 2018. W3C Recommendation. URL: [https://www.w3.org/TR/html5/](https://www.w3.org/TR/html5/) 


<a id="specification-bib-i18n-glossary"></a>


[I18N-GLOSSARY]



 [Internationalization Glossary](https://www.w3.org/TR/i18n-glossary/). Richard Ishida; Addison Phillips. W3C. 17 October 2024. W3C Working Group Note. URL: [https://www.w3.org/TR/i18n-glossary/](https://www.w3.org/TR/i18n-glossary/) 


<a id="specification-bib-infra"></a>


[INFRA]



 [Infra Standard](https://infra.spec.whatwg.org/). Anne van Kesteren; Domenic Denicola. WHATWG. Living Standard. URL: [https://infra.spec.whatwg.org/](https://infra.spec.whatwg.org/) 


<a id="specification-bib-rdf11-testcases"></a>


[RDF11-TESTCASES]



 [RDF 1.1 Test Cases](https://www.w3.org/TR/rdf11-testcases/). Gregg Kellogg; Markus Lanthaler. W3C. 25 February 2014. W3C Working Group Note. URL: [https://www.w3.org/TR/rdf11-testcases/](https://www.w3.org/TR/rdf11-testcases/) 


<a id="specification-bib-rfc2119"></a>


[RFC2119]



 [Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/rfc/rfc2119). S. Bradner. IETF. March 1997. Best Current Practice. URL: [https://www.rfc-editor.org/rfc/rfc2119](https://www.rfc-editor.org/rfc/rfc2119) 


<a id="specification-bib-rfc3629"></a>


[RFC3629]



 [UTF-8, a transformation format of ISO 10646](https://www.rfc-editor.org/rfc/rfc3629). F. Yergeau. IETF. November 2003. Internet Standard. URL: [https://www.rfc-editor.org/rfc/rfc3629](https://www.rfc-editor.org/rfc/rfc3629) 


<a id="specification-bib-rfc3986"></a>


[RFC3986]



 [Uniform Resource Identifier (URI): Generic Syntax](https://www.rfc-editor.org/rfc/rfc3986). T. Berners-Lee; R. Fielding; L. Masinter. IETF. January 2005. Internet Standard. URL: [https://www.rfc-editor.org/rfc/rfc3986](https://www.rfc-editor.org/rfc/rfc3986) 


<a id="specification-bib-rfc3987"></a>


[RFC3987]



 [Internationalized Resource Identifiers (IRIs)](https://www.rfc-editor.org/rfc/rfc3987). M. Duerst; M. Suignard. IETF. January 2005. Proposed Standard. URL: [https://www.rfc-editor.org/rfc/rfc3987](https://www.rfc-editor.org/rfc/rfc3987) 


<a id="specification-bib-rfc7493"></a>


[RFC7493]



 [The I-JSON Message Format](https://www.rfc-editor.org/rfc/rfc7493). T. Bray, Ed. IETF. March 2015. Proposed Standard. URL: [https://www.rfc-editor.org/rfc/rfc7493](https://www.rfc-editor.org/rfc/rfc7493) 


<a id="specification-bib-rfc8174"></a>


[RFC8174]



 [Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/rfc/rfc8174). B. Leiba. IETF. May 2017. Best Current Practice. URL: [https://www.rfc-editor.org/rfc/rfc8174](https://www.rfc-editor.org/rfc/rfc8174) 


<a id="specification-bib-rfc8259"></a>


[RFC8259]



 [The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259). T. Bray, Ed. IETF. December 2017. Internet Standard. URL: [https://www.rfc-editor.org/rfc/rfc8259](https://www.rfc-editor.org/rfc/rfc8259) 


<a id="specification-bib-rfc8615"></a>


[RFC8615]



 [Well-Known Uniform Resource Identifiers (URIs)](https://www.rfc-editor.org/rfc/rfc8615). M. Nottingham. IETF. May 2019. Proposed Standard. URL: [https://www.rfc-editor.org/rfc/rfc8615](https://www.rfc-editor.org/rfc/rfc8615) 


<a id="specification-bib-unicode"></a>


[Unicode]



 [The Unicode Standard](https://www.unicode.org/versions/latest/). Unicode Consortium. URL: [https://www.unicode.org/versions/latest/](https://www.unicode.org/versions/latest/) 


<a id="specification-bib-xml-names"></a>


[XML-NAMES]



 [Namespaces in XML 1.0 (Third Edition)](https://www.w3.org/TR/xml-names/). Tim Bray; Dave Hollander; Andrew Layman; Richard Tobin; Henry Thompson et al. W3C. 8 December 2009. W3C Recommendation. URL: [https://www.w3.org/TR/xml-names/](https://www.w3.org/TR/xml-names/) 


<a id="specification-bib-xml11"></a>


[XML11]



 [Extensible Markup Language (XML) 1.1 (Second Edition)](https://www.w3.org/TR/xml11/). Tim Bray; Jean Paoli; Michael Sperberg-McQueen; Eve Maler; François Yergeau; John Cowan et al. W3C. 16 August 2006. W3C Recommendation. URL: [https://www.w3.org/TR/xml11/](https://www.w3.org/TR/xml11/) 


<a id="specification-bib-xmlschema11-2"></a>


[XMLSCHEMA11-2]



 [W3C XML Schema Definition Language (XSD) 1.1 Part 2: Datatypes](https://www.w3.org/TR/xmlschema11-2/). David Peterson; Sandy Gao; Ashok Malhotra; Michael Sperberg-McQueen; Henry Thompson; Paul V. Biron et al. W3C. 5 April 2012. W3C Recommendation. URL: [https://www.w3.org/TR/xmlschema11-2/](https://www.w3.org/TR/xmlschema11-2/) 



 


<a id="specification-informative-references"></a>

<a id="specification-L4912"></a>
<a id="specification-j-2-informative-references"></a>
### J.2 Informative references
[](#specification-informative-references)

 


<a id="specification-bib-abnf"></a>


[ABNF]



 [Augmented BNF for Syntax Specifications: ABNF](https://www.rfc-editor.org/rfc/rfc5234). D. Crocker, Ed.; P. Overell. IETF. January 2008. Internet Standard. URL: [https://www.rfc-editor.org/rfc/rfc5234](https://www.rfc-editor.org/rfc/rfc5234) 


<a id="specification-bib-cooluris"></a>


[COOLURIS]



 [Cool URIs for the Semantic Web](https://www.w3.org/TR/cooluris/). Leo Sauermann; Richard Cyganiak. W3C. 3 December 2008. W3C Working Group Note. URL: [https://www.w3.org/TR/cooluris/](https://www.w3.org/TR/cooluris/) 


<a id="specification-bib-did-core"></a>


[did-core]



 [Decentralized Identifiers (DIDs) v1.0](https://www.w3.org/TR/did-core/). Manu Sporny; Amy Guy; Markus Sabadello; Drummond Reed. W3C. 19 July 2022. W3C Recommendation. URL: [https://www.w3.org/TR/did-core/](https://www.w3.org/TR/did-core/) 


<a id="specification-bib-html"></a>


[HTML]



 [HTML Standard](https://html.spec.whatwg.org/multipage/). Anne van Kesteren; Domenic Denicola; Dominic Farolino; Ian Hickson; Philip Jägenstedt; Simon Pieters. WHATWG. Living Standard. URL: [https://html.spec.whatwg.org/multipage/](https://html.spec.whatwg.org/multipage/) 


<a id="specification-bib-html-rdfa"></a>


[HTML-RDFA]



 [HTML+RDFa 1.1 - Second Edition](https://www.w3.org/TR/html-rdfa/). Manu Sporny. W3C. 17 March 2015. W3C Recommendation. URL: [https://www.w3.org/TR/html-rdfa/](https://www.w3.org/TR/html-rdfa/) 


<a id="specification-bib-json-ld11"></a>


[JSON-LD11]



 [JSON-LD 1.1](https://www.w3.org/TR/json-ld11/). Gregg Kellogg; Pierre-Antoine Champin; Dave Longley. W3C. 16 July 2020. W3C Recommendation. URL: [https://www.w3.org/TR/json-ld11/](https://www.w3.org/TR/json-ld11/) 


<a id="specification-bib-linked-data"></a>


[LINKED-DATA]



 [Linked Data Design Issues](https://www.w3.org/DesignIssues/LinkedData.html). Tim Berners-Lee. W3C. 27 July 2006. W3C-Internal Document. URL: [https://www.w3.org/DesignIssues/LinkedData.html](https://www.w3.org/DesignIssues/LinkedData.html) 


<a id="specification-bib-owl2-overview"></a>


[OWL2-OVERVIEW]



 [OWL 2 Web Ontology Language Document Overview (Second Edition)](https://www.w3.org/TR/owl2-overview/). W3C OWL Working Group. W3C. 11 December 2012. W3C Recommendation. URL: [https://www.w3.org/TR/owl2-overview/](https://www.w3.org/TR/owl2-overview/) 


<a id="specification-bib-owl2-syntax"></a>


[OWL2-SYNTAX]



 [OWL 2 Web Ontology Language Structural Specification and Functional-Style Syntax (Second Edition)](https://www.w3.org/TR/owl2-syntax/). Boris Motik; Peter Patel-Schneider; Bijan Parsia. W3C. 11 December 2012. W3C Recommendation. URL: [https://www.w3.org/TR/owl2-syntax/](https://www.w3.org/TR/owl2-syntax/) 


<a id="specification-bib-rdf-canon"></a>


[RDF-CANON]



 [RDF Dataset Canonicalization](https://www.w3.org/TR/rdf-canon/). Gregg Kellogg; Dave Longley; Dan Yamamoto. W3C. 21 May 2024. W3C Recommendation. URL: [https://www.w3.org/TR/rdf-canon/](https://www.w3.org/TR/rdf-canon/) 


<a id="specification-bib-rdf-concepts-20040210"></a>


[RDF-CONCEPTS-20040210]



 [Resource Description Framework (RDF): Concepts and Abstract Syntax](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/). Graham Klyne; Jeremy Carroll. W3C. 10 February 2004. W3C Recommendation. URL: [https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/) 


<a id="specification-bib-rdf11-concepts"></a>


[RDF11-CONCEPTS]



 [RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/). Richard Cyganiak; David Wood; Markus Lanthaler. W3C. 25 February 2014. W3C Recommendation. URL: [https://www.w3.org/TR/rdf11-concepts/](https://www.w3.org/TR/rdf11-concepts/) 


<a id="specification-bib-rdf11-datasets"></a>


[RDF11-DATASETS]



 [RDF 1.1: On Semantics of RDF Datasets](https://www.w3.org/TR/rdf11-datasets/). Antoine Zimmermann. W3C. 25 February 2014. W3C Working Group Note. URL: [https://www.w3.org/TR/rdf11-datasets/](https://www.w3.org/TR/rdf11-datasets/) 


<a id="specification-bib-rdf11-mt"></a>


[RDF11-MT]



 [RDF 1.1 Semantics](https://www.w3.org/TR/rdf11-mt/). Patrick Hayes; Peter Patel-Schneider. W3C. 25 February 2014. W3C Recommendation. URL: [https://www.w3.org/TR/rdf11-mt/](https://www.w3.org/TR/rdf11-mt/) 


<a id="specification-bib-rdf12-interop"></a>


[RDF12-INTEROP]



 [RDF 1.2 Interoperability](https://w3c.github.io/rdf-interop/spec/). Pierre-Antoine Champin. W3C. W3C Editor's Draft. URL: [https://w3c.github.io/rdf-interop/spec/](https://w3c.github.io/rdf-interop/spec/) 


<a id="specification-bib-rdf12-n-quads"></a>


[RDF12-N-QUADS]



 [RDF 1.2 N-Quads](https://www.w3.org/TR/rdf12-n-quads/). Gregg Kellogg; Dominik Tomaszuk. W3C. 20 March 2026. W3C Working Draft. URL: [https://www.w3.org/TR/rdf12-n-quads/](https://www.w3.org/TR/rdf12-n-quads/) 


<a id="specification-bib-rdf12-n-triples"></a>


[RDF12-N-TRIPLES]



 [RDF 1.2 N-Triples](https://www.w3.org/TR/rdf12-n-triples/). Gregg Kellogg; Dominik Tomaszuk. W3C. 26 March 2026. W3C Working Draft. URL: [https://www.w3.org/TR/rdf12-n-triples/](https://www.w3.org/TR/rdf12-n-triples/) 


<a id="specification-bib-rdf12-new"></a>


[RDF12-NEW]



 [What’s New in RDF 1.2](https://w3c.github.io/rdf-new/spec/). The W3C RDF & SPARQL Working Group. W3C. W3C Editor's Draft. URL: [https://w3c.github.io/rdf-new/spec/](https://w3c.github.io/rdf-new/spec/) 


<a id="specification-bib-rdf12-primer"></a>


[RDF12-PRIMER]



 [RDF 1.2 Primer](https://www.w3.org/TR/rdf12-primer/). Niklas Lindström; Pierre-Antoine Champin. W3C. 3 April 2025. DNOTE. URL: [https://www.w3.org/TR/rdf12-primer/](https://www.w3.org/TR/rdf12-primer/) 


<a id="specification-bib-rdf12-schema"></a>


[RDF12-SCHEMA]



 [RDF 1.2 Schema](https://www.w3.org/TR/rdf12-schema/). Dominik Tomaszuk. W3C. 20 March 2026. W3C Working Draft. URL: [https://www.w3.org/TR/rdf12-schema/](https://www.w3.org/TR/rdf12-schema/) 


<a id="specification-bib-rdf12-semantics"></a>


[RDF12-SEMANTICS]



 [RDF 1.2 Semantics](https://www.w3.org/TR/rdf12-semantics/). Peter Patel-Schneider; Dörthe Arndt; Enrico Franconi. W3C. 26 March 2026. W3C Working Draft. URL: [https://www.w3.org/TR/rdf12-semantics/](https://www.w3.org/TR/rdf12-semantics/) 


<a id="specification-bib-rdf12-trig"></a>


[RDF12-TRIG]



 [RDF 1.2 TriG](https://www.w3.org/TR/rdf12-trig/). Gregg Kellogg; Dominik Tomaszuk. W3C. 20 March 2026. W3C Working Draft. URL: [https://www.w3.org/TR/rdf12-trig/](https://www.w3.org/TR/rdf12-trig/) 


<a id="specification-bib-rdf12-turtle"></a>


[RDF12-TURTLE]



 [RDF 1.2 Turtle](https://www.w3.org/TR/rdf12-turtle/). Gregg Kellogg; Dominik Tomaszuk. W3C. 20 March 2026. W3C Working Draft. URL: [https://www.w3.org/TR/rdf12-turtle/](https://www.w3.org/TR/rdf12-turtle/) 


<a id="specification-bib-rdf12-xml"></a>


[RDF12-XML]



 [RDF 1.2 XML Syntax](https://www.w3.org/TR/rdf12-xml/). Gregg Kellogg; Jerven Bolleman. W3C. 26 March 2026. W3C Working Draft. URL: [https://www.w3.org/TR/rdf12-xml/](https://www.w3.org/TR/rdf12-xml/) 


<a id="specification-bib-rdfa-core"></a>


[RDFA-CORE]



 [RDFa Core 1.1 - Third Edition](https://www.w3.org/TR/rdfa-core/). Ben Adida; Mark Birbeck; Shane McCarron; Ivan Herman et al. W3C. 17 March 2015. W3C Recommendation. URL: [https://www.w3.org/TR/rdfa-core/](https://www.w3.org/TR/rdfa-core/) 


<a id="specification-bib-rfc3023"></a>


[RFC3023]



 [XML Media Types](https://www.rfc-editor.org/rfc/rfc3023). M. Murata; S. St. Laurent; D. Kohn. IETF. January 2001. Proposed Standard. URL: [https://www.rfc-editor.org/rfc/rfc3023](https://www.rfc-editor.org/rfc/rfc3023) 


<a id="specification-bib-rfc5890"></a>


[RFC5890]



 [Internationalized Domain Names for Applications (IDNA): Definitions and Document Framework](https://www.rfc-editor.org/rfc/rfc5890). J. Klensin. IETF. August 2010. Proposed Standard. URL: [https://www.rfc-editor.org/rfc/rfc5890](https://www.rfc-editor.org/rfc/rfc5890) 


<a id="specification-bib-rfc5892"></a>


[RFC5892]



 [The Unicode Code Points and Internationalized Domain Names for Applications (IDNA)](https://www.rfc-editor.org/rfc/rfc5892). P. Faltstrom, Ed. IETF. August 2010. Proposed Standard. URL: [https://www.rfc-editor.org/rfc/rfc5892](https://www.rfc-editor.org/rfc/rfc5892) 


<a id="specification-bib-rfc6874"></a>


[RFC6874]



 [Representing IPv6 Zone Identifiers in Address Literals and Uniform Resource Identifiers](https://www.rfc-editor.org/rfc/rfc6874). B. Carpenter; S. Cheshire; R. Hinden. IETF. February 2013. Proposed Standard. URL: [https://www.rfc-editor.org/rfc/rfc6874](https://www.rfc-editor.org/rfc/rfc6874) 


<a id="specification-bib-rfc7230"></a>


[rfc7230]



 [Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing](https://httpwg.org/specs/rfc7230.html). R. Fielding, Ed.; J. Reschke, Ed. IETF. June 2014. Proposed Standard. URL: [https://httpwg.org/specs/rfc7230.html](https://httpwg.org/specs/rfc7230.html) 


<a id="specification-bib-sparql11-query"></a>


[SPARQL11-QUERY]



 [SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/). Steven Harris; Andy Seaborne. W3C. 21 March 2013. W3C Recommendation. URL: [https://www.w3.org/TR/sparql11-query/](https://www.w3.org/TR/sparql11-query/) 


<a id="specification-bib-sparql12-concepts"></a>


[SPARQL12-CONCEPTS]



 [SPARQL 1.2 Concepts](https://w3c.github.io/sparql-concepts/spec/). The W3C RDF & SPARQL Working Group. W3C. W3C Editor's Draft. URL: [https://w3c.github.io/sparql-concepts/spec/](https://w3c.github.io/sparql-concepts/spec/) 


<a id="specification-bib-sparql12-entailment"></a>


[SPARQL12-ENTAILMENT]



 [SPARQL 1.2 Entailment Regimes](https://www.w3.org/TR/sparql12-entailment/). Peter Patel-Schneider. W3C. 14 August 2025. W3C Working Draft. URL: [https://www.w3.org/TR/sparql12-entailment/](https://www.w3.org/TR/sparql12-entailment/) 


<a id="specification-bib-sparql12-federated-query"></a>


[SPARQL12-FEDERATED-QUERY]



 [SPARQL 1.2 Federated Query](https://www.w3.org/TR/sparql12-federated-query/). Ruben Taelman; Gregory Williams. W3C. 26 January 2026. W3C Working Draft. URL: [https://www.w3.org/TR/sparql12-federated-query/](https://www.w3.org/TR/sparql12-federated-query/) 


<a id="specification-bib-sparql12-graph-store-protocol"></a>


[SPARQL12-GRAPH-STORE-PROTOCOL]



 [SPARQL 1.2 Graph Store Protocol](https://www.w3.org/TR/sparql12-graph-store-protocol/). Andy Seaborne; Thomas Pellissier Tanon. W3C. 19 December 2024. W3C Working Draft. URL: [https://www.w3.org/TR/sparql12-graph-store-protocol/](https://www.w3.org/TR/sparql12-graph-store-protocol/) 


<a id="specification-bib-sparql12-new"></a>


[SPARQL12-NEW]



 [What’s New in SPARQL 1.2](https://w3c.github.io/sparql-new/spec/). The W3C RDF & SPARQL Working Group. W3C. W3C Editor's Draft. URL: [https://w3c.github.io/sparql-new/spec/](https://w3c.github.io/sparql-new/spec/) 


<a id="specification-bib-sparql12-protocol"></a>


[SPARQL12-PROTOCOL]



 [SPARQL 1.2 Protocol](https://www.w3.org/TR/sparql12-protocol/). Andy Seaborne; Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 14 August 2025. W3C Working Draft. URL: [https://www.w3.org/TR/sparql12-protocol/](https://www.w3.org/TR/sparql12-protocol/) 


<a id="specification-bib-sparql12-query"></a>


[SPARQL12-QUERY]



 [SPARQL 1.2 Query Language](https://www.w3.org/TR/sparql12-query/). Olaf Hartig; Andy Seaborne; Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 23 March 2026. W3C Working Draft. URL: [https://www.w3.org/TR/sparql12-query/](https://www.w3.org/TR/sparql12-query/) 


<a id="specification-bib-sparql12-results-csv-tsv"></a>


[SPARQL12-RESULTS-CSV-TSV]



 [SPARQL 1.2 Query Results CSV and TSV Formats](https://www.w3.org/TR/sparql12-results-csv-tsv/). Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 14 August 2025. W3C Working Draft. URL: [https://www.w3.org/TR/sparql12-results-csv-tsv/](https://www.w3.org/TR/sparql12-results-csv-tsv/) 


<a id="specification-bib-sparql12-results-json"></a>


[SPARQL12-RESULTS-JSON]



 [SPARQL 1.2 Query Results JSON Format](https://www.w3.org/TR/sparql12-results-json/). Andy Seaborne; Ruben Taelman; Gregory Williams; Thomas Pellissier Tanon. W3C. 14 August 2025. W3C Working Draft. URL: [https://www.w3.org/TR/sparql12-results-json/](https://www.w3.org/TR/sparql12-results-json/) 


<a id="specification-bib-sparql12-results-xml"></a>


[SPARQL12-RESULTS-XML]



 [SPARQL 1.2 Query Results XML Format](https://www.w3.org/TR/sparql12-results-xml/). Ruben Taelman; Dominik Tomaszuk; Thomas Pellissier Tanon. W3C. 27 December 2024. W3C Working Draft. URL: [https://www.w3.org/TR/sparql12-results-xml/](https://www.w3.org/TR/sparql12-results-xml/) 


<a id="specification-bib-sparql12-service-description"></a>


[SPARQL12-SERVICE-DESCRIPTION]



 [SPARQL 1.2 Service Description](https://www.w3.org/TR/sparql12-service-description/). Ruben Taelman; Gregory Williams. W3C. 19 March 2026. W3C Working Draft. URL: [https://www.w3.org/TR/sparql12-service-description/](https://www.w3.org/TR/sparql12-service-description/) 


<a id="specification-bib-sparql12-update"></a>


[SPARQL12-UPDATE]



 [SPARQL 1.2 Update](https://www.w3.org/TR/sparql12-update/). Ruben Taelman; Andy Seaborne; Thomas Pellissier Tanon. W3C. 14 August 2025. W3C Working Draft. URL: [https://www.w3.org/TR/sparql12-update/](https://www.w3.org/TR/sparql12-update/) 


<a id="specification-bib-string-meta"></a>


[STRING-META]



 [Strings on the Web: Language and Direction Metadata](https://www.w3.org/TR/string-meta/). Richard Ishida; Addison Phillips. W3C. 17 October 2024. W3C Working Group Note. URL: [https://www.w3.org/TR/string-meta/](https://www.w3.org/TR/string-meta/) 


<a id="specification-bib-swbp-n-aryrelations"></a>


[SWBP-N-ARYRELATIONS]



 [Defining N-ary Relations on the Semantic Web](https://www.w3.org/TR/swbp-n-aryRelations/). Natasha Noy; Alan Rector. W3C. 12 April 2006. W3C Working Group Note. URL: [https://www.w3.org/TR/swbp-n-aryRelations/](https://www.w3.org/TR/swbp-n-aryRelations/) 


<a id="specification-bib-swbp-xsch-datatypes"></a>


[SWBP-XSCH-DATATYPES]



 [XML Schema Datatypes in RDF and OWL](https://www.w3.org/TR/swbp-xsch-datatypes/). Jeremy Carroll; Jeff Pan. W3C. 14 March 2006. W3C Working Group Note. URL: [https://www.w3.org/TR/swbp-xsch-datatypes/](https://www.w3.org/TR/swbp-xsch-datatypes/) 


<a id="specification-bib-unicode-security"></a>


[UNICODE-SECURITY]



 [Unicode Security Considerations](https://www.unicode.org/reports/tr36/tr36-15.html). Mark Davis; Michel Suignard. Unicode Consortium. 19 September 2014. Unicode Technical Report #36. URL: [https://www.unicode.org/reports/tr36/tr36-15.html](https://www.unicode.org/reports/tr36/tr36-15.html) 


<a id="specification-bib-url"></a>


[URL]



 [URL Standard](https://url.spec.whatwg.org/). Anne van Kesteren. WHATWG. Living Standard. URL: [https://url.spec.whatwg.org/](https://url.spec.whatwg.org/) 


<a id="specification-bib-vocab-org"></a>


[VOCAB-ORG]



 [The Organization Ontology](https://www.w3.org/TR/vocab-org/). Dave Reynolds. W3C. 16 January 2014. W3C Recommendation. URL: [https://www.w3.org/TR/vocab-org/](https://www.w3.org/TR/vocab-org/) 


<a id="specification-bib-webarch"></a>


[WEBARCH]



 [Architecture of the World Wide Web, Volume One](https://www.w3.org/TR/webarch/). Ian Jacobs; Norman Walsh. W3C. 15 December 2004. W3C Recommendation. URL: [https://www.w3.org/TR/webarch/](https://www.w3.org/TR/webarch/)


<!-- materialization-redistribution-notice -->
## Redistribution notice

This document includes material copied from or derived from "RDF 1.2 Concepts and Abstract Data Model", W3C Candidate Recommendation Snapshot 07 April 2026, https://www.w3.org/TR/2026/CR-rdf12-concepts-20260407/. Copyright © 2004-2026 World Wide Web Consortium. https://www.w3.org/copyright/software-license-2023/. This converted repository copy is not the official W3C rendering and is not a W3C Recommendation or an endorsement by W3C.

Appendix F's consolidated IRI ABNF includes code copied from or derived from IETF RFC 3986, "Uniform Resource Identifier (URI): Generic Syntax" (January 2005), by Tim Berners-Lee, Roy T. Fielding and Larry Masinter, https://www.rfc-editor.org/rfc/rfc3986.txt; and IETF RFC 3987, "Internationalized Resource Identifiers (IRIs)" (January 2005), by Martin Dürst and Michel Suignard, https://www.rfc-editor.org/rfc/rfc3987.txt. The code permission is RFC 3667 (BCP 78), Section 3.3(a)(E), subject to Section 5, https://www.rfc-editor.org/rfc/rfc3667.txt; the pre-March-2005 code guidance is https://trustee.ietf.org/about/faq/. The following original Full Copyright Statement applies separately to each of RFC 3986 and RFC 3987 and is retained for the Appendix F code, not asserted as a license for the W3C document as a whole:

Copyright (C) The Internet Society (2005).

This document is subject to the rights, licenses and restrictions contained in BCP 78, and except as set forth therein, the authors retain all their rights.

This document and the information contained herein are provided on an "AS IS" basis and THE CONTRIBUTOR, THE ORGANIZATION HE/SHE REPRESENTS OR IS SPONSORED BY (IF ANY), THE INTERNET SOCIETY AND THE INTERNET ENGINEERING TASK FORCE DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

Appendix F's IP-literal, ZoneID and IPv6addrz code includes material copied from or derived from IETF RFC 6874, "Representing IPv6 Zone Identifiers in Address Literals and Uniform Resource Identifiers" (February 2013), by Brian Carpenter, Stuart Cheshire and Robert M. Hinden, https://www.rfc-editor.org/rfc/rfc6874.txt. Its original Copyright Notice is retained below; "Simplified BSD" is the original historical label. The applicable dated TLP4 is https://trustee.ietf.org/wp-content/uploads/IETF-TLP-4.pdf (effective 28 December 2009), Section 4.c/4.e. The IETF Trust confirms that this was always the three-clause Revised BSD text and the license text did not change: https://trustee.ietf.org/documents/trust-legal-provisions/tlp-5/. This permission applies to these RFC 6874 code components, not the W3C document as a whole.

Copyright (c) 2013 IETF Trust and the persons identified as the document authors. All rights reserved.

This document is subject to BCP 78 and the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info) in effect on the date of publication of this document. Please review these documents carefully, as they describe your rights and restrictions with respect to this document. Code Components extracted from this document must include Simplified BSD License text as described in Section 4.e of the Trust Legal Provisions and are provided without warranty as described in the Simplified BSD License.

BSD License (TLP4 Section 4.c; year inserted for RFC 6874):

Copyright (c) 2013 IETF Trust and the persons identified as authors of the code. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

- Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
- Neither the name of Internet Society, IETF or IETF Trust, nor the names of specific contributors, may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


Changes: Original dated HTML and the explicitly listed scientific assets are retained byte-for-byte. Collector additions: structural Markdown, source-line anchors, local href routes and selector sidecar; ordered table cells with declared span annotations, separate dt/dd blocks and pre/code characters (including br line breaks and NBSP) are retained without executing source scripts. Only the per-source declared navigation/definition panels and head logo/icon nodes are excluded from the derived DOM; original identity, copyright, status, authors, acknowledgements, references and source-native discrepancies are preserved. Legacy root document.md and selectors.jsonl are unchanged.

Scope: 仅覆盖本轮列定固定 HTML 原响应、4件在该作品正文中实际引用且经实物信用审阅准入的科学图及同层 figure.css，以及由其生成的结构文字/新 selector sidecar；旧根文字/旧 selectors 的历史 text-only grant 另保留，不倒写旧获取。不授权未保留的 logo/ORCID、独立替代格式、外链作品/ontology/RDF/数据/代码、商标、专利或权利人无权许可的第三方内容。附录 F 对应 RFC 代码继续同时遵守原完整组合条款，不转授 RFC 全文或将这些条件扩张至非 RFC 图/样式/整份规范。

Full license and original rights links: [NOTICE.md](../NOTICE.md).

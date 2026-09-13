# Data Catalog Vocabulary (DCAT) - Version 3

W3C Recommendation 22 August 2024

See also translations .

This document is also available in these non-normative formats: Turtle , RDF/XML , and JSON-LD

Copyright ©
    2024 World Wide Web Consortium . W3C ® liability , trademark and permissive document license rules apply.

DCAT 3 supersedes DCAT 2 [ VOCAB-DCAT-2 ], but it does not make it obsolete. DCAT 3 maintains the DCAT namespace as its terms preserve backward compatibility with  DCAT 2. DCAT 3 relaxes constraints and adds new classes and properties, but these changes do not break the definition of previous terms.

Any new implementation is expected to adopt DCAT 3, while the existing implementations do not need to upgrade to it, unless they want to use the new features. In particular, current DCAT 2 deployments that do not overlap with the DCAT 3 new features (e.g., versioning, dataset series and inverse properties) don't need to change anything to remain in conformance with DCAT 3.


## Abstract

DCAT is an RDF vocabulary designed to facilitate interoperability between data catalogs published on the Web.
      This document defines the schema and provides examples for its use.

DCAT enables a publisher to describe datasets and data services in a catalog using a standard model and vocabulary that facilitates the consumption and aggregation of metadata from multiple catalogs.
        This can increase the discoverability of datasets and data services.
        It also makes it possible to have a decentralized approach to publishing data catalogs and makes federated search for datasets across catalogs in multiple sites possible using the same query mechanism and structure.
        Aggregated DCAT metadata can serve as a manifest file as part of the digital preservation process.

The namespace for DCAT terms is http://www.w3.org/ns/dcat#

The suggested prefix for the DCAT namespace is dcat


## Status of This Document

This section describes the status of this
      document at the time of its publication. A list of current W3C publications and the latest revision of this technical report can be found
      in the W3C technical reports index at
      https://www.w3.org/TR/.

This document defines a major revision of the DCAT 2 vocabulary ([ VOCAB-DCAT-2 ]) in response to use cases, requirements and community experience which could not be considered during the previous vocabulary development. This revision extends the DCAT standard in line with community practice while supporting diverse approaches to data description and dataset exchange. The main changes to the DCAT vocabulary have been:

addition of spdx:checksum property and spdx:Checksum class to provide digest for DCAT distributions

addition of properties for supporting versioning, e.g., dcat:version , dcat:previousVersion , dcat:hasCurrentVersion , see 11. Versioning

addition of a dcat:DatasetSeries class and properties for representing Dataset Series, see 12. Dataset series

This new version of the vocabulary updates and expands the original but preserves backward compatibility. A full list of the significant changes (with links to the relevant GitHub issues) is described in D. Change history .

Issues, requirements, and features that have been considered and discussed by the Data eXchange Working Group but have not been addressed due to lack of maturity or consensus are collected in GitHub. Those believed to be a priority for a future release are in the milestone DCAT Future Priority Work .


### DCAT history

The original DCAT vocabulary was developed and hosted at the Digital Enterprise Research Institute (DERI) , then refined by the eGov Interest Group , and finally standardized in 2014 [ VOCAB-DCAT-1 ] by the Government Linked Data (GLD) Working Group.

A second recommended revision of DCAT, DCAT 2 [ VOCAB-DCAT-2 ], was developed by the Dataset Exchange Working Group in response to a new set of Use Cases and Requirements [ DCAT-UCR ] gathered from peoples' experience with the DCAT vocabulary from the time of the original version, and new applications that were not considered in the first version.

This version of DCAT, DCAT 3, was developed by the Dataset Exchange Working Group , considering some of the more pressing use cases and requests among those left unaddressed in the previous standardization round.  A summary of the changes from [ VOCAB-DCAT-2 ] is provided in D. Change history .


### External terms

DCAT incorporates terms from pre-existing vocabularies where stable terms with appropriate meanings could be found, such as foaf:homepage and dcterms:title .
      Informal summary definitions of the externally-defined terms are included in the DCAT vocabulary for convenience, while authoritative definitions are available in the normative references.
      Changes to definitions in the references, if any, supersede the summaries given in this specification.
      Note that conformance to DCAT ( 4. Conformance ) concerns usage of only the terms in the DCAT vocabulary specification, so possible changes to other external definitions will not affect the conformance of DCAT implementations.


### Please send comments

This document was published by the Dataset Exchange Working Group as
    a Recommendation using the Recommendation track .

W3C recommends the wide deployment of this specification as a standard for
      the Web.

A W3C Recommendation is a specification that, after extensive
      consensus-building, is endorsed by W3C and its Members, and
      has commitments from Working Group members to royalty-free licensing for implementations.

This document was produced by a group
        operating under the W3C Patent
          Policy . W3C maintains a public list of any patent disclosures made in connection with the deliverables of
          the group; that page also includes
          instructions for disclosing a patent. An individual who has actual
          knowledge of a patent which the individual believes contains Essential Claim(s) must disclose the information in accordance with section 6 of the W3C Patent Policy .

This document is governed by the 03 November 2023 W3C Process Document .


## 1. Introduction

This section is non-normative.

Sharing data resources among different organizations, researchers, governments and citizens requires the provision of metadata.
        This is irrespective of the data being open or not.
        DCAT is a vocabulary for publishing data catalogs on the Web, which was originally developed in the context of government data catalogs
        such as data.gov and data.gov.uk , but it is also applicable and has been used in other contexts.

DCAT 3 has extended the previous version to support further use cases and requirements [ DCAT-UCR ].
        These include the possibility of cataloging other resources in addition to
        datasets, such as dataset series. The revision also supports describing versioning of resources.  Guidance on how to use inverse properties is provided.

DCAT provides RDF classes and properties to allow datasets and data services to be described and included in a catalog.
    The use of a standard model and vocabulary facilitates the consumption and aggregation of metadata from multiple catalogs, which can:

increase the discoverability of datasets and data services

allow federated search for datasets across catalogs in multiple sites

Data described in a catalog can come in many formats, ranging from spreadsheets, through XML and RDF to various specialized formats.
        DCAT does not make any assumptions about these serialization formats of the datasets but it does
        distinguish between the abstract dataset and its different manifestations or distributions.

Data is often provided through a service which supports selection of an extract, sub-set, or combination of existing data, or of new data generated by some data processing function.
        DCAT allows the description of a data access service to be included in a catalog.

Complementary vocabularies can be used together with DCAT to provide more detailed format-specific information.
      For example, properties from the VoID vocabulary [ VOID ] can be used within DCAT to express various statistics about a dataset if that dataset is in RDF format.

This document does not prescribe any particular method of deploying data catalogs expressed in DCAT.
      DCAT information can be presented in many forms including RDF accessible via SPARQL endpoints, embedded in HTML pages as [ HTML-RDFa ], or serialized as RDF/XML [ RDF-SYNTAX-GRAMMAR ], [ N3 ], [ Turtle ], [ JSON-LD ] or other formats.
      Within this document the examples use [ Turtle ] because of its readability.


## 2. Motivation for change

This section is non-normative.

The original Recommendation [ VOCAB-DCAT-1 ] published in January 2014 provided the basic framework for describing datasets. It made an important distinction between a dataset as an abstract idea and a distribution as a manifestation of the dataset. Although DCAT has been widely adopted, it has become clear that the original specification lacked a number of essential features that were added either through the mechanism of a profile, such as the European Commission's DCAT-AP [ DCAT-AP ], or the development of larger vocabularies that to a greater or lesser extent built upon the base standard, such as the Healthcare and Life Sciences Community Profile [ HCLS-Dataset ], the Data Tag Suite [ DATS ] and more. DCAT 2 [ VOCAB-DCAT-2 ] was developed to address the specific shortcomings that have come to light through the experiences of different communities, the aim being to improve interoperability between the outputs of these larger vocabularies.
    For example, DCAT 2 provided classes, properties and guidance to address identifiers , dataset quality information , and data citation issues.

This revision, DCAT 3,  updates the specification throughout. Significant changes from the 2014 Recommendation and DCAT 2 are marked within the text using "Note" sections, as well as being described in D. Change history .


## 3. Namespaces

The namespace for DCAT is http://www.w3.org/ns/dcat# .
        DCAT also makes extensive use of terms from other vocabularies, in particular Dublin Core [ DCTERMS ].
        DCAT defines a minimal set of classes and properties of its own.


### 3.1 Normative namespaces

Namespaces and prefixes used in normative parts of this recommendation are shown in the following table.


### 3.2 Non-normative namespaces

This section is non-normative.

Namespaces and prefixes used in examples and guidelines in the document and not from normative parts of the recommendation are shown in the following table.


## 4. Conformance

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words MAY , MUST , MUST NOT , and SHOULD in this document
        are to be interpreted as described in BCP 14 [ RFC2119 ] [ RFC8174 ]
        when, and only when, they appear in all capitals, as shown here.

A data catalog conforms to DCAT if:

Access to data is organized into datasets, distributions, data services and dataset series.

An RDF description of the catalog itself, the corresponding cataloged resources, and distributions is available (but the choice of
            RDF syntax, access protocol, and access policy are not mandated by this specification).

The contents of all metadata fields that are held in the catalog and that contain data about the catalog itself, the corresponding cataloged resources,  and distributions are included in this RDF description and are expressed using the appropriate classes and properties from DCAT, except where no such class or property exists.

All classes and properties defined in DCAT are used in a way consistent with the semantics declared in this specification.

A DCAT profile is a specification for a data catalog that adds additional constraints to DCAT. A data catalog that conforms to the profile also conforms to DCAT. Additional constraints in a profile MAY include:

Cardinality constraints, including a minimum set of required metadata fields

Sub-classes and sub-properties of the standard DCAT classes and properties

Classes and properties for additional metadata fields not covered in DCAT vocabulary specification

Controlled vocabularies or IRI sets as acceptable values for properties

Requirements for specific access mechanisms (RDF syntaxes, protocols) to the catalog's RDF description

The notion of profile used in this document denotes metadata specifications that the Dublin Core community would call application profiles [ DCAP ].


## 5. Vocabulary overview

This section is non-normative.


### 5.1 DCAT scope

DCAT is an RDF vocabulary for representing data catalogs.
      DCAT is based around seven main classes ( Figure 1 ):

dcat:Catalog represents a catalog, which is a dataset in which each individual item is a metadata record describing some resource; the scope of dcat:Catalog is collections of metadata about datasets , data services , or other resource types.

dcat:Resource represents a dataset, a data service or any other resource that may be described by a metadata record in a catalog.
          This class is not intended to be used directly, but is the parent class of dcat:Dataset , dcat:DataService and dcat:Catalog .
          Resources in a catalog should be instances of one of these classes, or of a sub-class of these, or of a sub-class of dcat:Resource defined in a DCAT profile or other DCAT application. dcat:Resource is actually an extension point for defining a catalog of any kind of resources. dcat:Dataset and dcat:DataService can be used for datasets and services which are not documented in any catalog.

dcat:Dataset represents a collection of data, published or curated by a single agent or identifiable community. The notion of dataset in DCAT is broad and inclusive, with the intention of accommodating resource types arising from all communities. Data comes in many forms including numbers, text, pixels, imagery, sound and other multi-media, and potentially other types, any of which might be collected into a dataset.

dcat:Distribution represents an accessible form of a dataset such as a downloadable file.

dcat:DataService represents a collection of operations accessible through an interface ( API ) that provide access to one or more datasets or data processing functions.

dcat:DatasetSeries is a dataset that represents a collection of datasets that are published separately, but share some characteristics that group them.

dcat:CatalogRecord represents a metadata record in the catalog, primarily concerning the registration information, such as who added the record and when.

Along with the rest of 5. Vocabulary overview , this diagram is non-normative .
        Furthermore, while the diagram uses UML-style class notation it should be interpreted following the usual RDF open-world assumptions around the presence/absence of properties, relationships, and their cardinality.
        The properties shown in each class reflect those specified in the descriptions of classes in 6. Vocabulary specification .
        Open arrow-heads indicate RDFS sub-class-of relationships (not object-oriented generalization). 
        To assist in understanding the full scope of each class, available properties are copied down from each '::super-class'.

A dataset in DCAT is defined as a "collection of data, published or curated by a single agent, and available for access or download in one or more serializations or formats".
        A dataset is a conceptual entity, and can be represented by one or more distributions that serialize the dataset for transfer.
        Distributions of a dataset can be provided via data services .

A data service typically provides selection, extraction, combination, processing or transformation operations over datasets that might be hosted locally or remote to the service.
      The result of any request to a data service is a representation of a part or all of a dataset or catalog.
      A data service might be tied to specific datasets, or its source data might be configured at request- or run-time.
      A data distribution service allows selection and download of a distribution of a dataset or subset.
      A data discovery service allows a client to find a suitable dataset.
      Other kinds of data service include data transformation services, such as coordinate transformation services, re-sampling and interpolation services, and various data processing services, including simulation and modeling services.
      Note that a data service in DCAT is a collection of operations or API which provides access to data.
      An interactive user-interface is often available to provide convenient access to API operations, but its description is outside the scope of DCAT.
      The details of a particular data service endpoint will often be specified through a description conforming to a standard service type, which complement the scope of the DCAT vocabulary itself.

Descriptions of datasets and data services can be included in a catalog .
      A catalog is a kind of dataset whose member items are descriptions of datasets and data services.
      Other types of resources might also be cataloged, but the scope of DCAT is currently limited to datasets and data services.
      To extend the scope of a catalog beyond datasets and data services it is recommended to define additional sub-classes of dcat:Resource in a DCAT profile or other DCAT application.
      To extend the scope of service descriptions beyond data distribution services it is recommended to define additional sub-classes of dcat:DataService in a DCAT profile or other DCAT application.

The scope of DCAT 1 [ VOCAB-DCAT-1 ] was limited to catalogs of datasets.
        A number of use cases for the revision [ DCAT-UCR ] involve data services as members of a catalog - see § 5.16 DCAT Distribution to describe Web services and § 5.18 Modeling service-based data access .
        Since DCAT 2 [ VOCAB-DCAT-2 ], DCAT includes both datasets and data services to enable these to be part of a DCAT conformant catalog.
        Provision for catalogs to be composed of other catalogs is also made.
        See Issue #172 .

Catalogs of other kinds of things might be designed following the DCAT pattern, e.g., dealing with facilities, instruments, samples and specimens, other physical artifacts, events or activities.
        These are currently out of scope for DCAT, but might be defined through further sub-classes of dcat:Resource , which could be specified in a DCAT profile or other DCAT application.

A catalog record describes an entry in the catalog. Notice that while dcat:Resource represents the dataset or service itself, dcat:CatalogRecord is the record that describes the registration of a resource in the catalog. The use of dcat:CatalogRecord is considered optional. It is used to capture provenance information about entries in a catalog explicitly. If this is not necessary then dcat:CatalogRecord can be safely ignored.


### 5.2 RDF considerations

The DCAT vocabulary is an OWL2 ontology [ OWL2-OVERVIEW ] formalized using [ RDF-SCHEMA ].
        Each class and property in DCAT is denoted by an IRI [ RFC3987 ].
        Locally defined elements are in the namespace http://www.w3.org/ns/dcat# .
        Elements are also adopted from several external vocabularies, in particular [ FOAF ], [ DCTERMS ] and [ PROV-O ]

RDF allows resources to have global identifiers ( IRIs ) or to be blank nodes.
        Blank nodes can be used to denote resources without explicitly naming them with an IRI .
        They can appear in the subject and object position of a triple [ RDF11-PRIMER ].
        For example, in many actual DCAT catalogs, distributions are represented as blank nodes nested inside the related dataset description.
        While blank nodes can offer flexibility for some use cases, in a Linked Data context, blank nodes limit our ability to collaboratively annotate data.
        A  blank node resource cannot be the target of a link and it can't be annotated with new information from new sources.
        As one of the biggest benefits of the Linked Data approach is that "anyone can say anything anywhere", use of blank nodes undermines some of the advantages we can gain from wide adoption of the RDF model.
        Even within the closed world of a single application dataset, use of blank nodes can quickly become limiting when integrating new data [ LinkedDataPatterns ].
        For these reasons, it is recommended that instances of the DCAT main classes have a global identifier, and use of blank nodes is generally discouraged when encoding DCAT in RDF.

All RDF examples in this document are written in Turtle syntax [ Turtle ] and many are available from the DXWG code repository .

Each RDF example in this document is intended to demonstrate specific capabilities of DCAT, and therefore only shows a subset of all the potential properties and links which might appear in a complete DCAT resource.


### 5.3 Basic example

This example provides a quick overview of how DCAT might be used to represent a government catalog and its datasets. Titles, labels and keywords are provided both in English and Spanish to demonstrate the use of language tags.

First, the catalog description:

ex:catalog
  a dcat:Catalog ;
  dcterms:title "Imaginary Catalog"@en ;
  dcterms:title "Catálogo imaginario"@es ;
  rdfs:label "Imaginary Catalog"@en ;
  rdfs:label "Catálogo imaginario"@es ;
  foaf:homepage <http://dcat.example.org/catalog> ;
  dcterms:publisher ex:transparency-office ;
  dcterms:language <http://id.loc.gov/vocabulary/iso639-1/en>  ;
  dcat:dataset ex:dataset-001 , ex:dataset-002 , ex:dataset-003 ;
  .

The publisher of the catalog has the relative IRI ex:transparency-office . Further description of the publisher can be provided as in Example 2 :

ex:transparency-office
  a foaf:Organization ;
  rdfs:label "Transparency Office"@en ;
  rdfs:label "Oficina de Transparencia"@es ;
  .

The catalog lists each of its datasets via the dcat:dataset property. In Example 1 , an example dataset was mentioned with the relative IRI ex:dataset-001 . A possible description of it using DCAT is shown below:

ex:dataset-001
  a dcat:Dataset ;
  dcterms:title "Imaginary dataset"@en ;
  dcterms:title "Conjunto de datos imaginario"@es ;
  dcat:keyword "accountability"@en, "transparency"@en, "payments"@en ;
  dcat:keyword "responsabilidad"@es, "transparencia"@es, "pagos"@es ;
  dcterms:creator ex:finance-employee-001 ;
  dcterms:issued "2011-12-05"^^xsd:date ;
  dcterms:modified "2011-12-15"^^xsd:date ;
  dcat:contactPoint <http://dcat.example.org/transparency-office/contact> ;
  dcterms:temporal [ a dcterms:PeriodOfTime ;
    dcat:startDate "2011-07-01"^^xsd:date ; 
    dcat:endDate   "2011-09-30"^^xsd:date ;
  ];
  dcat:temporalResolution "P1D"^^xsd:duration ;
  dcterms:spatial <http://sws.geonames.org/6695072/> ;
  dcat:spatialResolutionInMeters "30.0"^^xsd:decimal ;
  dcterms:publisher ex:finance-ministry ;
  dcterms:language <http://id.loc.gov/vocabulary/iso639-1/en> ;
  dcterms:accrualPeriodicity <http://purl.org/linked-data/sdmx/2009/code#freq-W>  ;
  dcat:distribution ex:dataset-001-csv ;
  .

Five distinct temporal descriptors are shown for this dataset.
          The dataset publication and revision dates are shown in dcterms:issued and dcterms:modified .
          For the frequency of update of the dataset in dcterms:accrualPeriodicity , we use an instance from the content-oriented guidelines developed as part of the W3C Data Cube Vocabulary [ VOCAB-DATA-CUBE ] efforts.
            The temporal coverage or extent is given in dcterms:temporal defining a dcterms:PeriodOfTime as a closed interval indicated by dcat:startDate and dcat:endDate .
          The temporal resolution, which describes the minimum spacing of items within the dataset, is given in dcat:temporalResolution using the standard datatype xsd:duration .

Additionally, the spatial coverage or extent is given dcterms:spatial using an IRI from Geonames .
          The spatial resolution, which describes the minimum spatial separation of items within the dataset, is given in dcat:spatialResolutionInMeters using the standard datatype xsd:decimal .

A contact point is provided where comments and feedback about the dataset can be sent.
          Further details about the contact point, such as email address or telephone number, can be provided using vCard [ VCARD-RDF ].

One representation of the dataset ex:dataset-001-csv can be downloaded as a 5kB CSV file. This is
            represented as an RDF resource of type dcat:Distribution .

ex:dataset-001-csv
  a dcat:Distribution ;
  dcat:downloadURL <http://dcat.example.org/files/001.csv> ;
  dcterms:title "CSV distribution of imaginary dataset 001"@en ;
  dcterms:title "distribución en CSV del conjunto de datos imaginario 001"@es ;
  dcat:mediaType <http://www.iana.org/assignments/media-types/text/csv> ;
  dcat:byteSize "5120"^^xsd:nonNegativeInteger ;
  .


### 5.4 Classifying datasets thematically

The catalog classifies its datasets according to a set of domains represented by the relative IRI ex:themes . SKOS [ SKOS-REFERENCE ] can be used to describe the domains used:

ex:catalog dcat:themeTaxonomy ex:themes .

ex:themes
  a skos:ConceptScheme ;
  skos:prefLabel "A set of domains to classify documents"@en ;
  .

ex:dataset-001 dcat:theme ex:accountability .

Notice that this dataset is classified under the domain represented by the relative IRI ex:accountability .
            It is recommended to define the concept as part of the concept scheme identified by the IRI ex:themes that was used to describe the catalog domains. An example SKOS description:

ex:accountability
  a skos:Concept ;
  skos:inScheme ex:themes ;
  skos:prefLabel "Accountability"@en ;
  .


### 5.5 Classifying dataset types

The type or genre of a dataset can be indicated using the dcterms:type property.
            It is recommended that the value of the property is taken from a well governed and broadly recognised set of resource types,
            such as the DCMI Type Vocabulary [ DCTERMS ],
            the MARC Genre/Terms Scheme ,
            the [ ISO-19115-1 ] MD_Scope codes ,
            the DataCite resource types [ DataCite ],
            or the PARSE.Insight content-types from Re3data [ RE3DATA-SCHEMA ].

In the following examples, a (notional) dataset is classified separately using values from different vocabularies.

ex:dataset-001
  rdf:type  dcat:Dataset ;
  dcterms:type  <http://purl.org/dc/dcmitype/Dataset> ;
  .

ex:dataset-001
  rdf:type  dcat:Dataset ;
  dcterms:type  <http://id.loc.gov/vocabulary/marcgt/dtb> ;
  .

It is also possible for multiple classifications to be present in a single description.

ex:dataset-001
  rdf:type  dcat:Dataset ;
  dcterms:type  <http://purl.org/dc/dcmitype/Dataset> ;
  dcterms:type  <http://id.loc.gov/vocabulary/marcgt/dtb> ;
  dcterms:type  <urn:example:datacite/resourceType/Dataset> ;
  dcterms:type  <urn:example:re3data/contentType/database> ;
.

<urn:example:datacite/resourceType/Dataset>
  rdfs:label "Dataset"@en ;
  dcterms:source [ rdfs:label "DataCite resource types"@en ] ;
  .

<urn:example:re3data/contentType/database>
  rdfs:label "Database"@en ;
  dcterms:source [ rdfs:label "Re3data content types"@en ] ;
  .


### 5.6 Describing catalog records metadata

If the catalog publisher decides to keep metadata
            describing its records (i.e., the records containing metadata
            describing the datasets), dcat:CatalogRecord can be used. For example,
            while ex:dataset-001 was issued on 2011-12-05, its description on Imaginary Catalog was added on 2011-12-11. This can be represented by DCAT as in Example 9 :

ex:catalog dcat:record ex:record-001  .

ex:record-001
  a dcat:CatalogRecord ;
  foaf:primaryTopic ex:dataset-001 ;
  dcterms:issued "2011-12-11"^^xsd:date ;
  .


### 5.7 Dataset available only behind some Web page

ex:dataset-002 is available as a CSV file. However ex:dataset-002 can only be obtained through some Web page
            where the user needs to follow some links, provide some information and check some boxes
            before accessing the data.

ex:dataset-002
  a dcat:Dataset ;
  dcat:landingPage <http://dcat.example.org/dataset-002.html> ;
  dcat:distribution ex:dataset-002-csv ;
  .
ex:dataset-002-csv
  a dcat:Distribution ;
  dcat:accessURL <http://dcat.example.org/dataset-002.html> ;
  dcat:mediaType <http://www.iana.org/assignments/media-types/text/csv> ;
  .

Notice the use of a dcat:landingPage and the definition of the dcat:Distribution instance.


### 5.8 A dataset available as a download and behind some Web page

On the other hand, ex:dataset-003 can be obtained through some landing page but also can be downloaded from a known URL.

ex:dataset-003
  a dcat:Dataset ;
  dcat:landingPage <http://dcat.example.org/dataset-003.html> ;
  dcat:distribution ex:dataset-003-csv ;
  .
ex:dataset-003-csv
  a dcat:Distribution ;
  dcat:downloadURL <http://dcat.example.org/dataset-003.csv> ;
  dcat:mediaType <http://www.iana.org/assignments/media-types/text/csv> ;
  .

Notice that we used dcat:downloadURL with the downloadable distribution and that the other distribution accessible through the landing page
        does not have to be defined as a separate dcat:Distribution instance.


### 5.9 A dataset available through a service

ex:dataset-004 is distributed in different representations from different services.
          The dcat:accessURL for each dcat:Distribution corresponds with the dcat:endpointURL of the service.
          Each service is characterized by its general type using dcterms:type (here using values from the INSPIRE spatial data service type vocabulary),
          its specific API definition using dcterms:conformsTo ,
          with the detailed description of the individual endpoint parameters and options linked using dcat:endpointDescription .

ex:dataset-004
  rdf:type dcat:Dataset ;
  dcat:distribution ex:dataset-004-csv ;
  dcat:distribution ex:dataset-004-png ;
  .

ex:dataset-004-csv
  rdf:type dcat:Distribution ;
  dcat:accessService ex:table-service-005 ;
  dcat:accessURL <http://dcat.example.org/api/table-005> ;
  dcat:mediaType <http://www.iana.org/assignments/media-types/text/csv> ;
  .

ex:dataset-004-png
  rdf:type dcat:Distribution ;
  dcat:accessService ex:figure-service-006 ;
  dcat:accessURL <http://dcat.example.org/api/figure-006> ;
  dcat:mediaType <http://www.iana.org/assignments/media-types/image/png> ;
  .

ex:figure-service-006
  rdf:type dcat:DataService ;
  dcterms:conformsTo <http://dcat.example.org/apidef/figure/v1.0> ;
  dcterms:type <https://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceType/view> ;
  dcat:endpointDescription <http://dcat.example.org/api/figure-006/params> ;
  dcat:endpointURL <http://dcat.example.org/api/figure-006> ;
  dcat:servesDataset ex:dataset-004 ;
  .

ex:table-service-005
  rdf:type dcat:DataService ;
  dcterms:conformsTo <http://dcat.example.org/apidef/table/v2.2> ;
  dcterms:type <https://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceType/download> ;
  dcat:endpointDescription <http://dcat.example.org/api/table-005/capability> ;
  dcat:endpointURL <http://dcat.example.org/api/table-005> ;
  dcat:servesDataset ex:dataset-003, ex:dataset-004 ;
  .


## 6. Vocabulary specification


### 6.1 RDF representation

New RDF serializations will be made available for DCAT 3 in the official URIs as soon as DCAT 3 becomes REC. In the meanwhile, the DCAT 3 RDFs are available in the DXWG GitHub repository : dcat3.ttl , dcat3.rdf , and dcat3.jsonld

The (revised) DCAT vocabulary is available in RDF .
            The primary artifact dcat.ttl is a serialization of the core DCAT vocabulary.
            Alongside it are a set of other RDF files that provide additional information, including:

The files dcat-external.ttl , dcat-external.rdf , and dcat-external.jsonld includes externally defined terms where DCAT has provided additional documentation or usage notes.

The files dcat-external.ttl , dcat-external.rdf , and dcat-external.jsonld includes externally defined terms where DCAT has provided additional documentation or usage notes.

The files dcat2.ttl , dcat2.rdf , and dcat2.jsonld that correspond to version 2 of DCAT [ VOCAB-DCAT-2 ].

The files dcat2.ttl , dcat2.rdf , and dcat2.jsonld that correspond to version 2 of DCAT [ VOCAB-DCAT-2 ].

The files dcat2014.ttl and dcat2014.rdf that correspond to the 2014 version of DCAT [ VOCAB-DCAT-1 ].

Where possible, properties defined by DCAT do not have specified domains in order to leave the property open for use with any kind of resources. 
	The intention is that such properties can be reused in any suitable circumstance where they make sense.


### 6.2 Elements from other vocabularies

DCAT requires use of elements from a number of other vocabularies.
        Furthermore, DCAT may be augmented by additional elements from external vocabularies, following the usual RDFS [ RDF-SCHEMA ] and OWL2 [ OWL2-OVERVIEW ] rules and patterns.


#### 6.2.1 Complementary vocabularies

Elements from a number of complementary vocabularies MAY be used together with DCAT to provide more detailed information.
        For example: properties from the VoID vocabulary [ VOID ] allow the description of various statistics about a DCAT-described dataset if that dataset is in RDF format; properties from the Provenance ontology [ PROV-O ] can be used to provide more information about the workflow that generated a dataset or service and related activities and agents; classes and properties from the Organization Ontology [ VOCAB-ORG ] can be used to explain additional details of responsible agents.


#### 6.2.2 Element definitions

The definitions (including domain and range) of terms outside the DCAT namespace are provided here only for convenience and MUST NOT be considered normative. The authoritative definitions of these terms are in the corresponding specifications, i.e., [ DC11 ], [ DCTERMS ], [ FOAF ], [ PROV-O ], [ RDF-SCHEMA ], [ SKOS-REFERENCE ], [ XMLSCHEMA11-2 ] and [ VCARD-RDF ].


### 6.3 Class: Catalog

The scope of dcat:Catalog in DCAT 1 was catalogs of datasets [ VOCAB-DCAT-1 ]. Since DCAT 2 [ VOCAB-DCAT-2 ], this was generalized, and properties common to all cataloged resources were associated with a super-class dcat:Resource .

Moreover, an explicit class for data services was added in DCAT, to enable these to be part of a catalog.

Finally, dcat:Catalog was made a sub-class of dcat:Dataset , and provision for catalogs to be composed of other catalogs is also enabled.

See Issue #116 and Issue #172 .

The following properties are specific to this class:

catalog record

resource

dataset

service

catalog

homepage

themes

The following properties of the super-class dcat:Dataset are also available for use:

distribution

frequency

spatial/geographic coverage

spatial resolution

temporal coverage

temporal resolution

was generated by

The following properties of the super-class dcat:Resource are also available for use:

access rights

conforms to

contact point

creator

description

has policy

identifier

is referenced by

keyword/tag

landing page

license

language

relation

rights

qualified relation

publisher

release date

theme/category

title

type/genre

update/modification date

qualified attribution

has current version

has version

previous version

replaces

status

version

version notes

first

last

previous


#### 6.3.1 Property: homepage


#### 6.3.2 Property: themes


#### 6.3.3 Property: resource

Property added in this context in DCAT 3.


#### 6.3.4 Property: dataset


#### 6.3.5 Property: service

Property added in DCAT 2.


#### 6.3.6 Property: catalog

Property added in DCAT 2.


#### 6.3.7 Property: catalog record


### 6.4 Class: Cataloged Resource

Class added in DCAT 2.

The following properties are specific to this class:

access rights

conforms to

contact point

creator

description

has part

has policy

identifier

is referenced by

keyword/tag

landing page

license

language

relation

rights

qualified relation

publisher

release date

theme/category

title

type/genre

update/modification date

qualified attribution

has current version

has version

previous version

replaces

status

version

version notes

first

last

previous

The class of all cataloged resources, the super-class of dcat:Dataset , dcat:DataService , dcat:Catalog and any other member of a dcat:Catalog .

This class carries properties common to all cataloged resources, including datasets and data services.

The instances of this class SHOULD be included in a catalog.

When describing a resource which is not a dcat:Dataset or dcat:DataService , it is recommended to create a suitable sub-class of dcat:Resource , or use dcat:Resource with the dcterms:type property to indicate the specific type.


#### 6.4.1 Property: access rights

Property added in DCAT 2.


#### 6.4.2 Property: conforms to

Property added in DCAT 2.

For guidance on the use of this property, see 14.2.1 Conformance to a standard .

dcterms:Standard is defined in [ DCTERMS ] as "A basis for comparison; a reference point against which other things can be evaluated." The target resource is not restricted to formal standards issued by bodies like ISO and W3C . In this context, it is any resource that specifies one or more aspects of the cataloged resource content, for example schema, semantics, syntax, usage guidelines, file format, or specific serialization. The meaning of conformance is determined by provisions in the target standard.


#### 6.4.3 Property: contact point

In DCAT 1 [ VOCAB-DCAT-1 ] the domain of dcat:contactPoint was dcat:Dataset , which limited use of this property in other contexts. The domain was relaxed in DCAT 2. See Issue #95 .


#### 6.4.4 Property: creator

Property added in DCAT 2, specifically to address data citation requirements.

This property is added to the dcat:Resource class, as the dcat:Dataset super-class. For more details, see 13. Data citation .

The use of the [ PROV-O ] qualified-attribution pattern is described in 15.1 Relationships between datasets and agents . dcterms:creator corresponds with a general attribution with the role 'creator'.


#### 6.4.5 Property: description


#### 6.4.6 Property: title


#### 6.4.7 Property: release date


#### 6.4.8 Property: update/modification date


#### 6.4.9 Property: language

dcterms:LinguisticSystem

Resources defined by the Library of Congress ( ISO 639-1 , ISO 639-2 ) SHOULD be used.

If a ISO 639-1 (two-letter) code is defined for language, then its corresponding IRI SHOULD be used; if no ISO 639-1 code is defined, then IRI corresponding to the ISO 639-2 (three-letter) code SHOULD be used.


#### 6.4.10 Property: publisher

The use of the [ PROV-O ] qualified-attribution pattern is described in 15.1 Relationships between datasets and agents . dcterms:publisher corresponds with a general attribution with the role 'publisher'.


#### 6.4.11 Property: identifier


#### 6.4.12 Property: theme/category

In DCAT 1 [ VOCAB-DCAT-1 ] the domain of dcat:theme was dcat:Dataset , which limited use of this property in other contexts. The domain was relaxed in DCAT 2. 
                See Issue #123 .

DCAT 3 maintains the same expectation as DCAT 2 for the use of the property dcat:theme . DCAT 3 defines dcat:theme as an OWL object property and  drops its range to  make the formalization of the property more consistent with the expected use. In particular, the change intends to prevent that each entity used as object of dcat:theme is automatically inferred as skos:Concept . See issue #1364 .


#### 6.4.13 Property: type/genre

Property added in DCAT 2. 
                See Issue #64 .

DCMI Type vocabulary [ DCTERMS ]

[ ISO-19115-1 ] scope codes

Datacite resource types [ DataCite ]

PARSE.Insight content-types used by re3data.org [ RE3DATA-SCHEMA ] (see item 15 contentType)

MARC intellectual resource types


#### 6.4.14 Property: relation

Property added in DCAT 2.

Many existing and legacy catalogs do not distinguish between dataset components, representations, documentation, schemata and other resources that are lumped together as part of a dataset. dcterms:relation is a super-property of a number of more specific properties which express more precise relationships, so use of dcterms:relation is not inconsistent with a subsequent reclassification with more specific semantics, though the more specialized sub-properties SHOULD be used to link a dataset to component and supplementary resources if possible.


#### 6.4.15 Property: qualified relation

Property added in DCAT 2.

This DCAT property follows the common qualified relation pattern described in 15. Qualified relations .

Since this property is a sub-property of prov:qualifiedInfluence , use of this property on an individual entails that the context resource is a member of the class prov:Entity [ PROV-O ] .


#### 6.4.16 Property: keyword/tag

In DCAT 1 [ VOCAB-DCAT-1 ] the domain of dcat:keyword was dcat:Dataset , which limited use of this property in other contexts. The domain was relaxed in DCAT 2 - see Issue #121 .


#### 6.4.17 Property: landing page

In DCAT 1 [ VOCAB-DCAT-1 ] the domain of dcat:landingPage was dcat:Dataset , which limited use of this property in other contexts. The domain was relaxed in DCAT 2 - see Issue #122 .


#### 6.4.18 Property: qualified attribution

Property added in this context in DCAT 2.

This DCAT property follows the common qualified relation pattern described in 15. Qualified relations .

Use of this property on an individual entails that the context resource is a member of the class prov:Entity [ PROV-O ].


#### 6.4.19 Property: license


#### 6.4.20 Property: rights


#### 6.4.21 Property: has part

Property added in this context in DCAT 3.


#### 6.4.22 Property: has policy

Property added in DCAT 2.


#### 6.4.23 Property: is referenced by

Property added in DCAT 2.

For examples on the use of this property, see C.3 Link datasets and publications .


#### 6.4.24 Property: previous version

Property added in DCAT 3.

This property is meant to be used to specify a version chain, consisting of snapshots of a resource.

The notion of version used by this property is limited to versions resulting from revisions occurring to a resource as part of its life-cycle. One of the typical cases here is representing the history of the versions of a dataset that have been released over time.

For guidance on the use of this property, see 11.1.1 Version chains and hierarchies .


#### 6.4.25 Property: has version

Property added in DCAT 3.

This property is intended for relating a non-versioned or abstract resource to several versioned resources, e.g., snapshots [ PAV ].

The notion of version used by this property is limited to versions resulting from revisions occurring to a resource as part of its life-cycle. Therefore, its semantics is more specific than its super-property dcterms:hasVersion , which makes use of a broader notion of version, including editions and adaptations.

For guidance on the use of this property, see 11.1.1 Version chains and hierarchies .


#### 6.4.26 Property: current version

Property added in DCAT 3.

This property is intended for relating a non-versioned or abstract resource to a single snapshot that can be used as a permalink to indicate the current version of the content [ PAV ].

The notion of version used by this property is limited to versions resulting from revisions occurring to a resource as part of its life-cycle.

For guidance on the use of this property, see 11.1.1 Version chains and hierarchies .


#### 6.4.27 Property: replaces

Property added in DCAT 3.

For guidance on the use of this property, see 11.1.2 Versions replaced by other ones .


#### 6.4.28 Property: version

Property added in DCAT 3.

DCAT does not prescribe how a version name / identifier should be specified, and refers for guidance to [ DWBP ]'s Best Practice 7: Provide a version indicator .

For guidance on the use of this property, see 11.2 Version information .


#### 6.4.29 Property: version notes

Property added in DCAT 3.

In case of backward compatibility issues with the previous version of the resource, a textual description of them SHOULD be specified by using this property.

For guidance on the use of this property, see 11.2 Version information .


#### 6.4.30 Property: status

Property added in DCAT 3.

DCAT does not prescribe the use of any specific set of life-cycle statuses, but refers to existing standards and community practices fit for the relevant application scenario.

For guidance on the use of this property, see 11.3 Resource life-cycle .


#### 6.4.31 Property: first

Property added in DCAT 3.

In DCAT this property is used for resources belonging to a dcat:DatasetSeries .

For guidance on the use of this property, see 12. Dataset series .


#### 6.4.32 Property: last

Property added in DCAT 3.

In DCAT this property is used for resources belonging to a dcat:DatasetSeries .

For guidance on the use of this property, see 12. Dataset series .


#### 6.4.33 Property: previous

Property added in DCAT 3.

In DCAT this property is used for resources belonging to a dcat:DatasetSeries .

It is important to note that this property is different from dcat:previousVersion , as it does not denote a previous version of the same resource, but a distinct resource immediately preceding the current one in an ordered collection of resources.

For guidance on the use of this property, see 12. Dataset series .


### 6.5 Class: Catalog Record

The following properties are specific to this class ( dcat:CatalogRecord ):

conforms to

description

listing date

primary topic

title

update/modification date

If a catalog is represented as an RDF Dataset with named graphs (as defined in [ SPARQL11-QUERY ]),
            then it is appropriate to place the description of each dataset
            (consisting of all RDF triples that mention the dcat:Dataset , dcat:CatalogRecord , and any of its dcat:Distribution s)
            into a separate named graph. The name of that graph SHOULD be the IRI of the catalog record.


#### 6.5.1 Property: title


#### 6.5.2 Property: description


#### 6.5.3 Property: listing date


#### 6.5.4 Property: update/modification date


#### 6.5.5 Property: primary topic


#### 6.5.6 Property: conforms to

Property added in this context in DCAT 2.

For guidance on the use of this property, see 14.2.1 Conformance to a standard .

dcterms:Standard is defined in [ DCTERMS ] as "A basis for comparison; a reference point against which other things can be evaluated." The target resource is not restricted to formal standards issued by bodies like ISO and W3C . In this context, it is any resource that specifies one or more aspects of the catalog record content, for example schema, semantics, syntax, usage guidelines, file format, or specific serialization. The meaning of conformance is determined by provisions in the target standard.


### 6.6 Class: Dataset

In DCAT 1 [ VOCAB-DCAT-1 ] dcat:Dataset was a sub-class of dctype:Dataset , which is a member of the DCMI Types vocabulary [ DCTERMS ].
              The scope of dcat:Dataset also includes other members of the DCMI Types vocabulary , such as various multimedia (imagery, sound, video) and text, so the sub-class relationship defined in DCAT 1 [ VOCAB-DCAT-1 ] was removed in the DCAT 2 vocabulary - see Issue #98 .

Note that members of the DCMI Types vocabulary may appear as the value of the dcterms:type property, as shown in 5.5 Classifying dataset types .

The following properties are specific to this class:

distribution

frequency

in series

spatial/geographic coverage

spatial resolution

temporal coverage

temporal resolution

was generated by

The following properties of the super-class dcat:Resource are also available for use:

access rights

conforms to

contact point

creator

description

has policy

identifier

is referenced by

keyword/tag

landing page

license

language

relation

rights

qualified relation

publisher

release date

theme/category

title

type/genre

update/modification date

qualified attribution

has current version

has version

previous version

replaces

status

version

version notes

first

last

previous

Information about licenses and rights SHOULD be provided on the level of Distribution. Information about licenses and rights MAY be provided for a Dataset in addition to but not instead of the information provided for the Distributions of that Dataset. Providing license or rights information for a Dataset that is different from information provided for a Distribution of that Dataset SHOULD be avoided as this can create legal conflicts.


#### 6.6.1 Property: distribution


#### 6.6.2 Property: frequency

Examples showing how dcterms:accrualPeriodicity and dcat:temporalResolution may be combined are given in 10.1 Temporal properties .


#### 6.6.3 Property: in series

Property added in DCAT 3.

For guidance on the use of this property, see 12. Dataset series .


#### 6.6.4 Property: spatial/geographical coverage

Options for expressing the details of a dcterms:Location are provided in 6.16 Class: Location .


#### 6.6.5 Property: spatial resolution

Property added in DCAT 2.

The range of this property is a number representing a length in meters.
            This is intended to provide a summary indication of the spatial resolution of the data as a single number.
          More complex descriptions of various aspects of spatial precision, accuracy, resolution and other statistics can be provided using the Data Quality Vocabulary [ VOCAB-DQV ].

As for the use of datatype, note that [ JSON-LD ] converts numbers to xsd:double or xsd:integer , and properly generating xsd:decimal requires the use of strings with an explicit or coerced datatype. In [ Turtle ], seemingly minor modifications can change the datatype of a value: 100.0 is an xsd:decimal , while 1e2 is an xsd:double .

Note also that number constants without a decimal part (e.g. 42 ) will, in [ Turtle ] or [ JSON-LD ], produce a literal with datatype xsd:integer . Since [ XMLSCHEMA11-2 ] defines xsd:integer as a derived type of xsd:decimal , such literals are semantically valid as values of dcat:spatialResolutionInMeters . However, syntactic validation tools such as [ SHACL ] or [ ShEx ] consider them as distinct datatypes. Authors of validation schemas in these languages should therefore consider adding xsd:integer to the accepted datatypes for dcat:spatialResolutionInMeters .


#### 6.6.6 Property: temporal coverage

Options for expressing the details of a dcterms:PeriodOfTime are provided in 6.15 Class: Period of Time .


#### 6.6.7 Property: temporal resolution

Property added in DCAT 2.

This is intended to provide a summary indication of the temporal resolution of the data distribution as a single value.
        More complex descriptions of various aspects of temporal precision, accuracy, resolution and other statistics can be provided using the Data Quality Vocabulary [ VOCAB-DQV ].

The distinction between dcat:temporalResolution and dcterms:accrualPeriodicity is illustrated by examples in 10.1 Temporal properties .


#### 6.6.8 Property: was generated by

Property added in this context in DCAT 2.

Use of this property on an individual entails that the context resource is a member of the class prov:Entity [ PROV-O ] .

Details about how to describe the activity that generated a dataset, such as a project, initiative, on-going activity, mission or survey, are out of scope for this document. prov:Activity provides for some basic properties such as begin and end time, associated agents etc.
                Further details may be provided through classes defined in applications.
                A number of ontologies for describing projects are available, for example
                VIVO for academic research projects [ VIVO-ISF ],
                DOAP (Description of a Project) for software projects [ DOAP ], and
                DBPedia for general projects [ DBPEDIA-ONT ] which are expected to be suitable for different applications.


### 6.7 Class: Dataset Series

Class added in DCAT 3, see Issue #1272 .

The following properties of the super-classes dcat:Resource and dcat:Dataset are also available for use:

access rights

conforms to

contact point

creator

distribution

description

has part

has policy

identifier

in series

is referenced by

keyword/tag

landing page

license

language

relation

rights

qualified relation

publisher

release date

theme/category

title

type/genre

update/modification date

qualified attribution

frequency

spatial/geographic coverage

spatial resolution

temporal coverage

temporal resolution

was generated by

has current version

has version

previous version

replaces

status

version

version notes

first

last

previous

Some of the inherited properties may have a particular semantics when used with dcat:DatasetSeries . For more details, see 12. Dataset series .

For guidance on the use of this property, see 12. Dataset series .


### 6.8 Class: Distribution

The following properties are specific to this class:

access rights

access URL

access service

byte size

compression format

conforms to

description

download URL

format

has policy

license

media type

packaging format

release date

rights

spatial resolution

temporal resolution

title

update/modification date

Examples of distributions include a CSV file, a [ netCDF ] file, a JSON document, or a data-cube, files made accessible according to different profiles, such as XML or JSON schemas or [ ShEx ] or [ SHACL ] expressions.

In some cases all distributions of a dataset will be fully informationally equivalent, in the sense that lossless transformations between the representations are possible.
            An example would be different serializations of an RDF graph using RDF/XML [ RDF-SYNTAX-GRAMMAR ], [ Turtle ], [ N3 ], [ JSON-LD ].
            However, in other cases the distributions might have different levels of fidelity to the underlying data.
            For example, a graphical representation about the data on a CSV file may not contain the same total information recorded in the CSV file, but they could be considered as two distributions for the same dataset as they are about the same data.

As a counter-example, budget data for different years would usually be modeled as different datasets, each with their own distributions, since all distributions of one dataset should broadly contain the same data.

Nevertheless, the question of whether different representations can be understood to be distributions of the same dataset, or distributions of different datasets, is application specific. Judgment about how to describe them is the responsibility of the provider, taking into account their understanding of the expectations of users, and practices in the relevant community.

Links between a dcat:Distribution and services or Web addresses where it can be accessed are expressed using dcat:accessURL , dcat:accessService , dcat:downloadURL , as shown in Figure 1 and described in the definitions below.


#### 6.8.1 Property: title


#### 6.8.2 Property: description


#### 6.8.3 Property: release date


#### 6.8.4 Property: update/modification date


#### 6.8.5 Property: license


#### 6.8.6 Property: access rights


#### 6.8.7 Property: rights

dcterms:license , which is a sub-property of dcterms:rights , can be used to link a distribution to a license document. However, dcterms:rights allows linking to a rights statement that can include licensing information as well as other information that supplements the license such as attribution.

Information about licenses and rights SHOULD be provided on the level of Distribution. Information about licenses and rights MAY be provided for a Dataset in addition to but not instead of the information provided for the Distributions of that Dataset. Providing license or rights information for a Dataset that is different from information provided for a Distribution of that Dataset SHOULD be avoided as this can create legal conflicts. See also guidance at 9. License and rights statements .


#### 6.8.8 Property: has policy

Property added in this context in DCAT 2.


#### 6.8.9 Property: access URL

dcat:accessURL SHOULD be used for the URL of a service or location that can provide access to this distribution, typically through a Web form, query or API call.

dcat:downloadURL is preferred for direct links to downloadable resources.

If the distribution(s) are accessible only through a landing page (i.e., direct download URLs are not known), then the landing page URL associated with the dcat:Dataset SHOULD be duplicated as access URL on a distribution (see 5.7 Dataset available only behind some Web page ).

dcat:accessURL matches the property-chain dcat:accessService / dcat:endpointURL . In the RDF representation of DCAT this is axiomatized as an OWL property-chain axiom.


#### 6.8.10 Property: access service

Property added in DCAT 2.


#### 6.8.11 Property: download URL


#### 6.8.12 Property: byte size


#### 6.8.13 Property: spatial resolution

Property added in DCAT 2.

The range of this property is a number representing a length in meters.
            This is intended to provide a summary indication of the spatial resolution of the data distribution as a single number.
          More complex descriptions of various aspects of spatial precision, accuracy, resolution and other statistics can be provided using the Data Quality Vocabulary [ VOCAB-DQV ].


#### 6.8.14 Property: temporal resolution

Property added in DCAT 2.

This is intended to provide a summary indication of the temporal resolution of the data distribution as a single value.
            More complex descriptions of various aspects of temporal precision, accuracy, resolution and other statistics can be provided using the Data Quality Vocabulary [ VOCAB-DQV ].


#### 6.8.15 Property: conforms to

Property added in this context in DCAT 2.

For guidance on the use of this property, see 14.2.1 Conformance to a standard .

dcterms:Standard is defined in [ DCTERMS ] as "A basis for comparison; a reference point against which other things can be evaluated." It is not restricted to formal standards issued by bodies like ISO and W3C . In this context it will usually be used for a schema, ontology, data model or profile which specifies the structure of a dataset distribution. This is not necessarily tied to a single encoding or serialization.


#### 6.8.16 Property: media type

The range of dcat:mediaType was tightened from dcterms:MediaTypeOrExtent to dcterms:MediaType as part of the DCAT 2 vocabulary.


#### 6.8.17 Property: format


#### 6.8.18 Property: compression format

Property added in DCAT 2.

For examples on the use of this property, see C.5 Compressed and packaged distributions .


#### 6.8.19 Property: packaging format

Property added in  DCAT 2.

For examples on the use of this property, see C.5 Compressed and packaged distributions .


#### 6.8.20 Property: checksum

Property added in DCAT 3.

The checksum is related to the download URL.


### 6.9 Class: Data Service

Class added in DCAT 2.

The following properties are specific to this class: endpoint description , endpoint URL , serves dataset .

The following properties of the super-class dcat:Resource are also available for use:

access rights

conforms to

contact point

creator

description

has policy

identifier

is referenced by

keyword/tag

landing page

license

language

relation

rights

qualified relation

publisher

release date

theme/category

title

type/genre

update/modification date

qualified attribution

has current version

has version

previous version

replaces

status

version

version notes

first

last

previous

For examples on the use of this class and related properties, see C.4 Data services .


#### 6.9.1 Property: endpoint URL


#### 6.9.2 Property: endpoint description


#### 6.9.3 Property: serves dataset


### 6.10 Class: Concept Scheme


### 6.11 Class: Concept


### 6.12 Class: Organization/Person

foaf:Person (for people)

foaf:Organization (for government agencies or other entities)


### 6.13 Class: Relationship

Class added in DCAT 2.

The following properties are specific to this class: relation , had role .

Examples illustrating use of this class and its properties are given in 15. Qualified relations .


#### 6.13.1 Property: relation


#### 6.13.2 Property: had role

Property added in DCAT 2.

This DCAT property complements prov:hadRole which provides the function of an entity or agent with respect to an activity.


### 6.14 Class: Role

Class added in DCAT 2.

Examples illustrating use of this class are given in 15. Qualified relations .

Used in a qualified-relation to specify the role of an Entity with respect to another Entity.
            It is recommended that the values be managed as a controlled vocabulary of entity roles such as

[ ISO-19115-1 ] DS_AssociationTypeCode

IANA Registry of Link Relations [ IANA-RELATIONS ]

DataCite metadata schema [ DataCite ]

MARC relators

This DCAT class complements prov:Role which provides the function of an entity or agent with respect to an activity.


### 6.15 Class: Period of Time

Class added in this context in DCAT 2.

The following properties are specific to this class: start date , end date . beginning , end .

Examples illustrating use of these options for the temporal coverage of a dataset are given in 10.1 Temporal properties .


#### 6.15.1 Property: start date

Property added in DCAT 2.


#### 6.15.2 Property: end date

Property added in DCAT 2.


#### 6.15.3 Property: beginning

Property added in this context in DCAT 2.

The value of time:hasEnd is a time:Instant for whose position several options are available. In particular times that do not use the conventional Gregorian calendar can be expressed, such as geological and archeological periods, and times given as numeric positions on a time-line.


#### 6.15.4 Property: end

Property added in this context in DCAT 2.

The value of time:hasEnd is a time:Instant for whose position several options are available. In particular times that do not use the conventional Gregorian calendar can be expressed, such as geological and archeological periods, and times given as numeric positions on a time-line.


### 6.16 Class: Location

Class added in this context in DCAT 2.

The following properties are specific to this class: geometry , bounding box , centroid .

Examples illustrating use of these options for the spatial coverage of a dataset are given in 10.2 Spatial properties .

For an extensive geometry (i.e., a set of coordinates denoting the vertices of the relevant geographic area), the property locn:geometry [ LOCN ] SHOULD be used.

For a geographic bounding box delimiting a spatial area the property dcat:bbox SHOULD be used.

For the geographic center of a spatial area, or another characteristic point, the property dcat:centroid SHOULD be used.


#### 6.16.1 Property: geometry

Property added in this context in DCAT 2.


#### 6.16.2 Property: bounding box

Property added in DCAT 2.

The WKT encoding supports geospatial positions expressed in coordinate reference systems other than WGS84 .


#### 6.16.3 Property: centroid

Property added in DCAT 2.

The WKT encoding supports geospatial positions expressed in coordinate reference systems other than WGS84 .


### 6.17 Class: Checksum

Class added in DCAT 3.

The following properties are specific to this class: algorithm , checksum value .


#### 6.17.1 Property: algorithm

Property added in DCAT 3.

The set of individuals of class spdx:ChecksumAlgorithm .


#### 6.17.2 Property: checksum value

Property added in DCAT 3.


## 7. Use of inverse properties

The properties described in 6. Vocabulary specification do not include inverses intentionally, with the purpose of ensuring interoperability also in systems not making use of OWL reasoning.

However, recognizing that inverses are needed for some use cases, DCAT supports them, but with the requirement that they MAY be used only in addition to those described in 6. Vocabulary specification , and that they MUST NOT be used to replace them.

The following table lists the inverse properties supported in DCAT.


## 8. Dereferenceable identifiers

This section is non-normative.

The scientific and data provider communities use a number of different identifiers for publications, authors and data. DCAT primarily relies on persistent HTTP IRIs as an effective way of making identifiers actionable. Notably, quite a few identifier schemes can be encoded as dereferenceable HTTP IRIs , and some of them are also returning machine-readable metadata (e.g., DOIs [ ISO-26324 ] and ORCIDs ). Regardless, data providers still might need to refer to legacy identifiers, non-HTTP dereferenceable identifiers, locally minted or third-party-provided identifiers. In these cases, [ DCTERMS ] and [ VOCAB-ADMS ] can be of use.

The property dcterms:identifier explicitly indicates HTTP IRIs as well as legacy identifiers. In the following examples, dcterms:identifier identifies a dataset, but it can similarly be used with any kind of resources.

<https://dcat.example.org/id> a dcat:Dataset;
  dcterms:identifier "https://dcat.example.org/id"^^xsd:anyURI ;
  .

Proxy dereferenceable IRIs can be used when resources do not have HTTP dereferenceable IDs. For example, in Example 14 , dcat.example.org/proxyid is a proxy for id .

<https://dcat.example.org/proxyid> a dcat:Dataset;
  dcterms:identifier "id"^^xsd:string ;
  .

The property adms:identifier [ VOCAB-ADMS ] can express other locally minted identifiers or external identifiers, like DOI, ELI , arΧiv for creative works and ORCID , VIAF , ISNI for actors such as authors and publishers, as long as the identifiers are globally unique and stable.

Example 15 uses adms:schemaAgency and dcterms:creator to represent the authority that defines the identifier scheme (e.g., the DOI foundation in the example), adms:schemaAgency is used when the authority has no IRI associated. The CrossRef and DataCite display guidelines recommend displaying DOIs as full URL link in the form https://doi.org/10.xxxx/xxxxx/ .

<https://dcat.example.org/id> a dcat:Dataset;
  adms:identifier  <https://dcat.example.org/iddoi> ;
  dcterms:publisher <https://dcat.example.org/PoelenJorritH> ;
  .

<https://dcat.example.org/iddoi> a adms:Identifier ;
  # reading https://www.w3.org/TR/skos-reference/#notations more than one skos:notation can be set
  skos:notation "https://doi.org/10.5281/zenodo.1486279"^^xsd:anyURI;
  # the authority/agency defining the identifier scheme, used if the agency has no IRI
  adms:schemaAgency "International DOI Foundation" ;
  # the authority/agency defining the identifier scheme, used if the agency has IRI
  dcterms:creator  ex:InternationalDOIFundation ;
  .

ex:InternationalDOIFundation a foaf:Organization ;
  rdfs:label "International DOI Foundation" ;
  foaf:homepage <https://www.doi.org/> ;
  .

<https://dcat.example.org/PoelenJorritH> a foaf:Person;
  foaf:name "Jorrit H. Poelen" ;
  adms:identifier <https://dcat.example.org/PoelenJorritHID> ;
  .

<https://dcat.example.org/PoelenJorritHID> a adms:Identifier;
  skos:notation "https://orcid.org/0000-0003-3138-4118"^^xsd:anyURI ;
  # the authority/agency defining the identifier scheme, used if the agency has no IRI
  adms:schemaAgency "ORCID" ;
  .

Example 15 does not represent the authority responsible for assigning and maintaining identifiers using that scheme (e.g., Zenodo ) as naming the registrant goes against the philosophy of DOI, where the sub-spaces are abstracted from the organization that registers them, with the advantage that DOIs do not change when the organization changes or the responsibility for that sub-space is handed over to someone else. Example 15 shows a locally minted identifier for the creator of the dataset (e.g., https://dcat.example.org/PoelenJorritHID ) and its correspondent ORCID identifier (e.g., https://orcid.org/0000-0003-3138-4118 ).

When the HTTP dereferenceable ID returns an RDF/OWL description for the dataset, the use of owl:sameAs might be considered. For example,

<https://dcat.example.org/id3> a dcat:Dataset;
  ...
  owl:sameAs <https://doi.org/10.5281/zenodo.1486279> ;
  .

when dereferenced with media type text/turtle , https://doi.org/10.5281/zenodo.1486279 returns a [ SCHEMA-ORG ] description for the dataset, which might dynamically enrich the description provided by https://dcat.example.org/id .

Identifiers for datasets should follow the best practices in § 8.7 Data Identifiers of [ DWBP ].

The need to distinguish between primary and alternative (or legacy) identifiers for a dataset within DCAT has been posed as a requirement. However, it is very much application-specific and would be better addressed in DCAT profiles rather than mandating a general approach.

Depending on the application context, specific guidelines such as "DCAT-AP: How to manage duplicates?" can be adopted for distinguishing authoritative datasets from dataset harvested by third parties catalogs.


### 8.1 Indicating common identifier types

If identifiers are not HTTP dereferenceable, common identifier types can be served as RDF datatypes [ RDF11-CONCEPTS ] or custom OWL datatypes [ OWL2-SYNTAX ] for the sake of interoperability, see ex:type in Example 17 .

<https://dcat.example.org/id4> a dcat:Dataset;
  ...
  adms:identifier <https://dcat.example.org/sid> .

<https://dcat.example.org/sid5> rdf:type adms:Identifier ;
  # the actual id
  skos:notation "PA 1-060-815"^^ex:type ;
  # Human readable schema agency
  adms:schemaAgency "US Copyright Office" ;
  dcterms:issued "2001-09-12"^^xsd:date ;
  .

If a registered IRI type is used (following [ RFC3986 ], § 3.1 Scheme ), the identifier scheme is part of the IRI ; thus indicating a separate identifier scheme in 'type' is redundant. For example, DOI is registered as a namespace in the info IRI scheme [ IANA-URI-SCHEMES ] (see DOI FAQ #11 ), so according to [ RFC3986 ], it should be encoded as in Example 18 .

<https://dcat.example.org/sid6> rdf:type adms:Identifier ;
  # the actual id
  skos:notation "info:doi/10.1109/5.771073"^^xsd:anyURI .

Otherwise, examples of common types for identifier scheme ( arXiv , etc.) are defined in DataCite schema [ DataCite ] and FAIRsharing Registry .


## 9. License and rights statements

This section is non-normative.

Selecting the right way to express conditions for access to and re-use of resources can be complex.
    Implementers should always seek legal advice before deciding which conditions apply to the resource being described.

This specification distinguishes three main situations:
    one where a statement is associated with a resource that is explicitly declared as a 'license';
    a second, where the statement is associated with a resource denoting only access rights;
    a third, covering all the other cases - i.e., statements not concerning licensing conditions and/or access rights (e.g., copyright statements).

The provision of licensing conditions and access rights complies with the Best Practices 4 (" Provide data license information ") and 22 (" Provide an explanation for data that is not available "), respectively, from [ DWBP ].

To address these scenarios, it is recommended to use the property dcterms:rights , and its sub-properties dcterms:license and dcterms:accessRights . More precisely:

use dcterms:license to refer to licenses; Note For interoperability, it is recommended to use canonical IRIs of well-known licenses such as those defined by Creative Commons .

use dcterms:license to refer to licenses;

For interoperability, it is recommended to use canonical IRIs of well-known licenses such as those defined by Creative Commons .

use dcterms:accessRights to express statements concerning only access rights (e.g., whether data can be accessed by anyone or just by authorized parties); Note Access rights can also be expressed as code lists / taxonomies. Examples include the access rights code list  [ EUV-AR ] used in [ DCAT-AP ] and the Eprints Access Rights Vocabulary Encoding Scheme .

use dcterms:accessRights to express statements concerning only access rights (e.g., whether data can be accessed by anyone or just by authorized parties);

Access rights can also be expressed as code lists / taxonomies. Examples include the access rights code list  [ EUV-AR ] used in [ DCAT-AP ] and the Eprints Access Rights Vocabulary Encoding Scheme .

use dcterms:rights for all the other types of rights statements - those which are not covered by dcterms:license and dcterms:accessRights , such as copyright statements. Note A more sophisticated approach to express rights, based on and extending [ DCTERMS ], is provided by the Open Data Rights Statement Vocabulary (ODRS) [ ODRS ], which defines properties for specifying, among others, copyright statements and copyright notices.

use dcterms:rights for all the other types of rights statements - those which are not covered by dcterms:license and dcterms:accessRights , such as copyright statements.

A more sophisticated approach to express rights, based on and extending [ DCTERMS ], is provided by the Open Data Rights Statement Vocabulary (ODRS) [ ODRS ], which defines properties for specifying, among others, copyright statements and copyright notices.

The following example is about a dataset publicly available (with no access restriction) and whose distribution is released by using a standard license - namely, the Creative Commons Attribution (CC-BY) 4.0 license. Access rights are specified by using the [ EUV-AR ] code list. Property dcterms:rights is used for the copyright statement, which is specified with a textual description, by using property rdfs:label (following the Dublin Core™ User Guide ).

ex:ds7890 a dcat:Dataset ;
# other dataset properties...
  dcterms:accessRights 
    <http://publications.europa.eu/resource/authority/access-right/PUBLIC> ;
  dcterms:rights [ a dcterms:RightsStatement ;
    rdfs:label "© 2021 ACME Inc."@en
  ] ;
  dcat:distribution [ a dcat:Distribution ;
# other distribution properties...
    dcterms:license <https://creativecommons.org/licenses/by/4.0/>
  ] ;
.

Finally, in the particular case when rights are expressed via ODRL policies , it is recommended to use the odrl:hasPolicy property as the link from the description of the cataloged resource or distribution to the ODRL policy.

The Open Digital Rights Language ( ODRL ) is a policy expression language that provides a flexible and interoperable information model [ ODRL-MODEL ], vocabulary [ ODRL-VOCAB ], and encoding mechanisms for representing statements about usage (i.e., permissions, prohibitions, and obligations) of content and services.

This example shows how to use [ ODRL-VOCAB ] for a dataset with very specific usage rules. In this case, the data can be read and derivatives can be created, but no commercial use of the dataset is allowed. In addition, it is a requirement to register before the permissions are granted.

ex:ds4242 a dcat:Dataset ;
# other dataset properties...
  dcat:distribution [ a dcat:Distribution ;
# other distribution properties...
    odrl:hasPolicy [ a odrl:Policy ;
      odrl:permission [ a odrl:Permission ;
        odrl:action ( 
          <http://www.w3.org/ns/odrl/2/read>
          <http://www.w3.org/ns/odrl/2/derive> 
        ) 
      ];
      odrl:prohibition [ a odrl:Prohibition ;
        odrl:action <http://creativecommons.org/ns#CommercialUse>
      ] ;
      odrl:obligation [ a odrl:Duty ;
        odrl:action <https://schema.org/RegisterAction> 
      ];
    ] ;
  ] ;
.

The above example does not explicitly define the ODRL Asset, so assumes the enclosing identified entity is the subject of the policy as per § 2.2.3 Target Policy Property in [ ODRL-MODEL ]. In addition, the example above follows the ODRL compact policy rules as per § 2.7.1 Compact Policy in [ ODRL-MODEL ].


## 10. Time and space

This section is non-normative.


### 10.1 Temporal properties

Five temporal properties of resources may be described using DCAT.

The release time of a resource is given using dcterms:issued .
          The value is usually encoded as a xsd:date .

The revision or update time of a resource is given using dcterms:modified .
          The value is usually encoded as a xsd:date .

The update schedule for a resource is indicated using dcterms:accrualPeriodicity .
          The value should be taken from a controlled vocabulary such as Dublin Core Collection Description Frequency Vocabulary .

The minimum temporal separation of items in a dataset is given using dcat:temporalResolution .
          The value is encoded as a xsd:duration .
          The update schedule and the temporal resolution can be combined to support the description of different kinds of time-series data as shown below.

The temporal extent of a dataset is given using dcterms:temporal .
          The value is a dcterms:PeriodOfTime .
          A number of options for expressing the details of a dcterms:PeriodOfTime are recommended in 6.15 Class: Period of Time .
          Examples of these follow.

ex:ds913
  a dcat:Dataset ;
  dcterms:accrualPeriodicity <http://purl.org/cld/freq/daily> ;
  dcat:temporalResolution "PT15M"^^xsd:duration ;
.

ex:ds782
  a dcat:Dataset ;
  dcterms:accrualPeriodicity <http://purl.org/cld/freq/continuous> ;
  dcat:temporalResolution "PT1H"^^xsd:duration ;
.

ex:ds257 a dcat:Dataset ;
  dcterms:temporal [ a dcterms:PeriodOfTime ;
    dcat:startDate "2016-03-04"^^xsd:date ;
    dcat:endDate   "2018-08-05"^^xsd:date ;
  ] .

The following dataset specification is equivalent to the one in Example 23 , but it uses [ OWL-TIME ]:

ex:ds348 a dcat:Dataset ;
  dcterms:temporal [ a dcterms:PeriodOfTime , time:ProperInterval ;
    time:hasBeginning [ a time:Instant ;
      time:inXSDDate "2016-03-04"^^xsd:date ;
    ] ;
    time:hasEnd [ a time:Instant ;
      time:inXSDDate "2018-08-05"^^xsd:date ;
    ] ;
  ] .

ex:ds429 a dcat:Dataset ;
  dcterms:temporal [ a dcterms:PeriodOfTime , time:ProperInterval ;
    time:hasBeginning [ a time:Instant ;
      time:inXSDgYear "1914"^^xsd:gYear ;
    ] ;
    time:hasEnd [ a time:Instant ;
      time:inXSDgYear "1939"^^xsd:gYear ;
    ] ;
  ] .

ex:ds850 a dcat:Dataset ;
  dcterms:temporal [ a dcterms:PeriodOfTime , time:ProperInterval ;
    time:hasBeginning [ a time:Instant ;
      time:inTimePosition [ a time:TimePosition ;
        time:hasTRS <http://resource.geosciml.org/classifier/cgi/geologicage/ma> ;
        time:numericPosition "541.0"^^xsd:decimal ;
      ] ;
    ] ;
    time:hasEnd [ a time:Instant ;
      time:inTimePosition [ a time:TimePosition ;
        time:hasTRS <http://resource.geosciml.org/classifier/cgi/geologicage/ma> ;
        time:numericPosition "251.902"^^xsd:decimal ;
      ] ;
    ] ;
  ] .

ex:ds127 a dcat:Dataset ;
  dcterms:temporal [ a dcterms:PeriodOfTime ;
    dcat:startDate "2016-03-04"^^xsd:date ;
  ] .

ex:ds586 a dcat:Dataset ;
  dcterms:temporal [ a dcterms:PeriodOfTime , time:ProperInterval ;
    time:hasEnd [ time:inXSDDate "2018-08-05"^^xsd:date ] ;
  ] .


### 10.2 Spatial properties

Two spatial properties of datasets may be described using DCAT.

The minimum spatial separation of items in a dataset is given using dcat:spatialResolutionInMeters .
          The value is a decimal number. An example of the use of dcat:spatialResolutionInMeters is given in Example 3 .

The minimum spatial separation of items in a dataset is given using dcat:spatialResolutionInMeters .
          The value is a decimal number.

An example of the use of dcat:spatialResolutionInMeters is given in Example 3 .

The spatial extent of a dataset is given using dcterms:spatial .
          The value is a dcterms:Location .
          A number of options for expressing the details of a dcterms:Location are recommended in 6.16 Class: Location . Examples of these follow.

The spatial extent of a dataset is given using dcterms:spatial .
          The value is a dcterms:Location .
          A number of options for expressing the details of a dcterms:Location are recommended in 6.16 Class: Location .

Examples of these follow.

The following examples are built on the relevant ones included in [ SDW-BP ] (in particular, § 12.2.2 Geometries and coordinate reference systems ).

In the examples, for properties locn:geometry , dcat:bbox , and dcat:centroid , the geometry is always specified with WKT . As per [ GeoSPARQL ], when the CRS specification is omitted this implies that the default CRS is used - namely CRS84 (corresponding to WGS84, but with axis order longitude/latitude).

For more details on coordinate reference systems and geometry encoding, we refer the reader to [ SDW-BP ], and, in particular, to the following sections:

§ 9 Coordinate Reference Systems ( CRS )

§ 12.2.2 Geometries and coordinate reference systems

A dataset whose spatial coverage corresponds to Anne Frank's house in Amsterdam, specified as a polygon (the coordinate reference system is CRS84).

<AnneFrank_0> a dcat:Dataset ;
  dcterms:spatial [
    a dcterms:Location ;
    locn:geometry """POLYGON ((
      4.8842353 52.375108 , 4.884276 52.375153 ,
      4.8842567 52.375159 , 4.883981 52.375254 ,
      4.8838502 52.375109 , 4.883819 52.375075 ,
      4.8841037 52.374979 , 4.884143 52.374965 ,
      4.8842069 52.375035 , 4.884263 52.375016 ,
      4.8843200 52.374996 , 4.884255 52.374926 ,
      4.8843289 52.374901 , 4.884451 52.375034 ,
      4.8842353 52.375108
    ))"""^^geosparql:wktLiteral ;
  ] .

The same dataset in Example 29 , but where the coordinates of the polygon are specified by using the national Dutch CRS - EPSG:28992 ("Amersfoort / RD New").

<AnneFrank_1> a dcat:Dataset ;
  dcterms:spatial [
    a dcterms:Location ;
    locn:geometry """<http://www.opengis.net/def/crs/EPSG/0/28992> POLYGON ((
      120749.725 487589.422 , 120752.55 487594.375  ,
      120751.227 487595.129 , 120732.539 487605.788 ,
      120723.505 487589.745 , 120721.387 487585.939 ,
      120740.668 487575.07  , 120743.316 487573.589 ,
      120747.735 487581.337 , 120751.564 487579.154 ,
      120755.411 487576.96  , 120750.935 487569.172 ,
      120755.941 487566.288 , 120764.369 487581.066 ,
      120749.725 487589.422
    ))"""^^geosparql:wktLiteral ;
  ] .

The same dataset of Example 29 , but where spatial coverage is specified by using the centroid / representative point of Anne Frank's house.

<AnneFrank_2> a dcat:Dataset ;
  dcterms:spatial [
    a dcterms:Location ;
    dcat:centroid "POINT(4.88412 52.37509)"^^geosparql:wktLiteral ;
  ] .

The Dutch dataset of postal addresses, with its spatial coverage (Netherlands) specified as a bounding box.

ex:Dutch-postal a dcat:Dataset ;
  dcterms:title "Adressen"@nl ;
  dcterms:title "Addresses"@en ;
  dcterms:description """INSPIRE Adressen afkomstig uit de basisregistratie Adressen,
                   beschikbaar voor heel Nederland"""@nl ;
  dcterms:description """INSPIRE addresses derived from the Addresses base registry,
                   available for the Netherlands"""@en ;
  dcat:theme <http://inspire.ec.europa.eu/theme/ad> ;
  dcterms:spatial [
    a dcterms:Location ;
    dcat:bbox """POLYGON((
      3.053 47.975 , 7.24  47.975 ,
      7.24  53.504 , 3.053 53.504 ,
      3.053 47.975
    ))"""^^geosparql:wktLiteral ;
  ] .


## 11. Versioning

This section is non-normative.

The notion of version is often used as a generic term to denote some kind of relationship between a resource and a derived one. Examples, among others, include revisions, editions, adaptations, and translations.

This section focuses specifically on how to use DCAT to describe versions resulting from a revision - i.e., from changes occurring to a resource as part of its life-cycle.

For this purpose, DCAT builds upon existing vocabularies, in particular the versioning component of the [ PAV ] ontology, and the relevant terms from [ DCTERMS ], [ OWL2-OVERVIEW ], and [ VOCAB-ADMS ].

It is important to note that versioning can be applied to any of the first class citizens DCAT resources, including Catalogs, Catalog Records, Datasets, Distributions.

Note also that the DCAT approach described in the following sections is meant to be complementary with those already used in specific types of resources (e.g., [ OWL2-OVERVIEW ] provides a set of versioning properties for ontologies), as well as in given domains and communities. For a comparison between the DCAT versioning approach and those of other vocabularies, see 11.4 Complementary approaches to versioning .

The notion of version is very much related to the community practices, the data management policy and the workflows in place. It is up to data providers to decide when and why a new version should be released. For this reason, DCAT refrains from providing definitions or rules about when changes in a resource should turn into a new release of it, and refers for guidance to [ DWBP ] ( § 8.6 Data Versioning and § 8.7 Data Identifiers ).


### 11.1 Relationships between versions

DCAT supports the following kinds of relationships between versions:

Those indicating the version chain and hierarchy (the version history).

Those indicating whether a version is replaced/superseded by another one.


#### 11.1.1 Version chains and hierarchies

DCAT defines specific properties for describing version history, aligned with the corresponding [ PAV ] ones:

dcat:previousVersion (equivalent to pav:previousVersion )

dcat:hasVersion (equivalent to pav:hasVersion );

dcat:hasVersion (equivalent to pav:hasVersion );

dcat:hasCurrentVersion (equivalent to pav:hasCurrentVersion , and subproperty of dcat:hasVersion ).

Property dcat:previousVersion is used to build a version chain that can be navigated backward from a given version to the first one. This reflects the most typical use case - i.e., linking different versions published as distinct resources in a catalog.

In addition to this, property dcat:hasVersion can be used to specify a version hierarchy, by linking an abstract resource to its versions.

If needed, the version hierarchy can be further described by specific properties. More precisely, property dcat:hasCurrentVersion link an abstract resource to snapshot corresponding to the current version of the content, whereas property dcat:isVersionOf (inverse of dcat:hasVersion ) gives the possibility of specifying a back link from a version to the abstract resource (for the use of this property, see 7. Use of inverse properties ).

On how to use DCAT to specify a resource's status, see 11.3 Resource life-cycle .

Note that the only properties necessary to specify a version chain and hierarchy are, respectively, dcat:previousVersion and dcat:hasVersion . Whether to use or not the other ones depends on the requirements of the relevant use case.

The following example reuses those in § 8.6 Data Versioning of [ DWBP ] and revises them to show how to specify a version chain and hierarchy on a bus stops dataset, by using the properties described in this section.

The MyCity bus stops dataset is updated whenever the list of bus stops changes. The different versions are preserved in order to keep an historical record of the bus stops available at given points in time. An abstract dataset is used to point to the version with the most up to date list of bus stops.

In Figure 5 , the resource with IRI mycity-bus:stops is the abstract resource, corresponding always to the latest version of the MyCity bus stops dataset, whereas the other ones correspond to specific versions of it. The current version is the one with IRI mycity-bus:stops-2015-12-07 .

The corresponding [ Turtle ] representation:

mycity-bus:stops a dcat:Dataset ;
  ...
  dcat :has Version mycity-bus:stops- 2015 - 01 - 01 ,
    mycity-bus:stops- 2015 - 05 - 05 ,
    mycity-bus:stops- 2015 - 12 - 07 ;
  dcat :has CurrentVersion mycity-bus:stops- 2015 - 12 - 07 ;
.

mycity-bus:stops- 2015 - 01 - 01 a dcat:Dataset ;
  ...
  dcat :is VersionOf mycity-bus:stops ;
.

mycity-bus:stops- 2015 - 05 - 05 a dcat:Dataset ;
  ...
  dcat:previousVersion mycity-bus:stops- 2015 - 01 - 01 ;
  dcat :is VersionOf mycity-bus:stops ;
.

mycity-bus:stops- 2015 - 12 - 07 a dcat:Dataset ;
  ...
  dcat:previousVersion mycity-bus:stops- 2015 - 05 - 05 ;
  dcat :is VersionOf mycity-bus:stops ;
.


#### 11.1.2 Versions replaced by other ones

Another type of relationship concerns whether a given version replaces/supersedes another one. For this purpose, DCAT reuses the relevant [ DCTERMS ] property, namely, dcterms:replaces , plus its inverse dcterms:isReplacedBy , in case a back link needs to be provided.

It is worth noting that these properties are not denoting by themselves a version chain - i.e., a version is not necessarily replacing its immediate predecessor.

The following example reuses the description of the MyCity bus stop dataset in Example 33 to show how replaced versions can be specified in DCAT.

mycity-bus:stops- 2015 - 01 - 01 a dcat:Dataset ;
  ...
  dcat :is VersionOf mycity-bus:stops ;
.

mycity-bus:stops- 2015 - 05 - 05 a dcat:Dataset ;
  ...
  dcat:previousVersion mycity-bus:stops- 2015 - 01 - 01 ;
  dcat :is VersionOf mycity-bus:stops ;
  dcterms:replaces mycity-bus:stops- 2015 - 01 - 01 ;
.

mycity-bus:stops- 2015 - 12 - 07 a dcat:Dataset ;
  ...
  dcat:previousVersion mycity-bus:stops- 2015 - 05 - 05 ;
  dcat :is VersionOf mycity-bus:stops ;
  dcterms:replaces mycity-bus:stops- 2015 - 05 - 05 ;
.


### 11.2 Version information

Besides the relationships illustrated in the previous section, versioned resources may be associated with additional information, describing, e.g., their differences with the original resource (the version "delta"),  the version identifier, and release date.

For these purposes, DCAT makes use of the following properties:

dcat:version (equivalent to pav:version [ PAV ]), for the version name / identifier;

dcterms:issued [ DCTERMS ], for the version release date;

adms:versionNotes [ VOCAB-ADMS ], for a textual description of the changes, including backward compatibility issues with the previous version of the resource.

adms:versionNotes [ VOCAB-ADMS ], for a textual description of the changes, including backward compatibility issues with the previous version of the resource.

DCAT does not prescribe how a version name / identifier should be specified, and refers for guidance to [ DWBP ]'s Best Practice 7: Provide a version indicator .

The following example reuses the one in [ DWBP ]'s Best Practice 7: Provide a version indicator to show how version information can be specified in DCAT.

mycity-bus:stops- 2015 - 01 - 01 a dcat:Dataset ;
  dcterms:title "Bus stops of MyCity" ;
  ...
  dcterms :is sued " 2015 - 01 - 01 "^^xsd:date ;
  ...
  dcat:version "1.0" ;
  adms:versionNotes "First version of the bus stop dataset." @en ;
.


### 11.3 Resource life-cycle

The life-cycle of a resource is an aspect orthogonal to versioning, and sometimes strictly related. The evolution of a resource along its life-cycle (from its conception, to its creation and publication) may result in new versions, although this is not always the case (e.g., in case an approval workflow is in place, the resource may not undergo any change if no revision is needed). Similarly, the creation of a new version may not necessarily lead to a change in status (e.g., when changes are not substantial, and/or are implemented on resources still in development). Moreover, when a resource is replaced because of a revision (correcting errors, adding new content, etc.), it may be moved to a different life-cycle status (e.g., deprecation or withdrawal).

It is worth noting that the status of a resource with respect to its life-cycle is often an important piece of information by itself, from both the data provider's and data consumers' perspectives. For a data consumer, it is important to know if a resource is still in development or not, as well as if it is deprecated or withdrawn (and, in such cases, if there is a new version to be used). On the other hand, for a data provider, flagging a resource with its status in the life-cycle is fundamental for the correct administration of the data management workflow. E.g., a resource before being published may need to be stable, and possibly flagged as approved and/or registered. Finally, besides the actual status of a resource, another useful piece of information is when the resource moved to a different status (e.g., when it was created, reviewed, accepted, published).

As for versioning, the resource life-cycle depends on community practices, data management policies, and the workflows in place. Moreover, different resource types (e.g., datasets vs catalog records) may have different life-cycle statuses.

For the specification of life-cycle statuses, DCAT makes use of property adms:status [ VOCAB-ADMS ], along with the appropriate [ DCTERMS ] time-related properties ( dcterms:created , dcterms:dateSubmitted , dcterms:dateAccepted , dcterms:dateCopyrighted , dcterms:issued , dcterms:modified , dcterms:valid ). However, DCAT does not prescribe the use of any specific set of life-cycle statuses, but refers to existing standards and community practices fit for the relevant application scenario.

Examples of life-cycle statuses include:

Those defined in the ISO standard for item registration [ ISO-19135 ] (accepted / not accepted, deprecated, experimental, reserved, retired, stable, submitted, superseded, valid / invalid).

The progress codes defined in [ ISO-19115 ] (accepted, completed, deprecated, final, historical archive, not accepted, obsolete, ongoing, pending, planned, proposed, required, retired, superseded, tentative, under development, valid, withdrawn).

The ADMS Status vocabulary [ ADMS-SKOS ], used in [ DCAT-AP ], which includes four statuses: completed, deprecated, under development, and withdrawn.

The dataset statuses [ EUV-DS ] and concept statuses [ EUV-CS ] vocabularies from the EU Vocabularies registry.

The UK Government Linked Data Registry project [ UKGOVLD-REG ] provides an example of how the life-cycle statuses defined in [ ISO-19135 ] can be used in a registry, along with the criteria for status transition.


### 11.4 Complementary approaches to versioning

The DCAT versioning approach can coexist with existing versioning practices - as those used in specific communities, domains, and resource types.

As an example, the following table shows the correspondences between the DCAT versioning properties and the vocabularies most frequently used to specify similar concepts, namely, OWL, for ontologies, [ DCTERMS ], and [ PROV-O ].

Note that correspondence does not imply equivalence. These properties have different scopes and semantics, and therefore they can complement but not replace each other. In particular, OWL properties are meant to be used on resources that can be typed as owl:Ontology 's, whereas the [ DCTERMS ] ones use a very broad notion of version (including editions and adaptations). On the other hand, DCAT versioning properties are meant to be used on any resource in a catalog, and they use a very specific notion of version , as explained in the introduction to 11. Versioning . Finally, the [ PROV-O ] property prov:wasRevisionOf , although semantically similar to dcat:previousVersion , is not explicitly meant to be used to build a version chain, whereas prov:generalizationOf and prov:specializationOf are semantically broader than their sub-properties dcat:hasVersion and dcat:isVersionOf , respectively.

The following example shows how DCAT and OWL can be used complementarily to versioning [ VOCAB-DCAT-2 ].

<http://www.w3.org/ns/dcat> a owl:Ontology , dcat:Dataset ;
  owl:versionInfo "3" ;
  dcat:version "3" ;
  owl:versionIRI <http://www.w3.org/ns/dcat3> ;
  dcat :has CurrentVersion <http://www.w3.org/ns/dcat3> ;
  owl:priorVersion <http://www.w3.org/ns/dcat2> ;
  dcat:previousVersion <http://www.w3.org/ns/dcat2> ;
  dcat :has Version <http://www.w3.org/ns/dcat2014> ,
    <http://www.w3.org/ns/dcat2> ,
    <http://www.w3.org/ns/dcat3> ;
.


## 12. Dataset series

This section is non-normative.

With "dataset series" we refer to data, somehow interrelated, that are published separately. An example is budget data split by year and/or country, instead of being made available in a single dataset.

Dataset series are defined in [ ISO-19115 ] as a collection of datasets […] sharing common characteristics . However, their use is not limited to geospatial data, although in other domains they can be named differently (e.g., time series, data slices) and defined more or less strictly (see, e.g., the notion of "dataset slice" in [ VOCAB-DATA-CUBE ]).

The reasons and criteria for grouping datasets into series are manyfold, and they may be related to, e.g., data characteristics, publishing process, and how they are typically used. For instance, data huge in size (as geospatial ones) are more easily handled (by data providers as well as data consumers) by splitting them into smaller ones. Another example is data released on a yearly basis, which are typically published as separate datasets, instead of appending the new data to the first in the series.

As there are no common rules and criteria across domains to decide when dataset series should be created and how they should be organized, DCAT does not prescribe any specific approach, and refer for guidance and domain- and community practices. The purpose of this section is limited to providing guidance on how dataset series can be specified in DCAT.


### 12.1 How to specify dataset series

DCAT makes dataset series first class citizens of data catalogs by minting a new class dcat:DatasetSeries , defined as a subclass of dcat:Dataset . 
The datasets are linked to the dataset series by using the property dcat:inSeries . 

    Note that a dataset series can also be hierarchical, and a dataset series can be a member of another dataset series.

In the following example, yearly budget data are grouped into a series. The series is typed as dcat:DatasetSeries , the child datasets are typed as dcat:Dataset . The datasets are linked to the series by using dcat:inSeries .

ex:EUCatalogue a dcat:Catalog ;
  dcterms:title "European Data Catalogue" @en ;
  dcat:dataset ex:budget , ex:employment , ex:finance ;
  .

ex:budget a dcat:DatasetSeries ;
  dcterms:title "Budget data" @en ;
  .
  
ex:budget- 2018 a dcat:Dataset ;
  dcterms:title "Budget data for year 2018" @en ;
  dcat:inSeries ex:budget ;
  .
  
ex:budget- 2019 a dcat:Dataset ;
  dcterms:title "Budget data for year 2019" @en ;
  dcat:inSeries ex:budget ;
  .
  
ex:budget- 2020 a dcat:Dataset ;
  dcterms:title "Budget data for year 2020" @en ;
  dcat:inSeries ex:budget ;
  .

Dataset series may evolve over time, by acquiring new datasets. E.g., a dataset series about yearly budget data will acquire a new child dataset every year. In such cases, it might be important to link the yearly releases with relationships specifying the first, previous, next, and latest ones. In such a scenario, DCAT makes use of properties dcat:first , dcat:prev , and dcat:last , respectively. See 7. Use of inverse properties for dcat:next .

The following example extends Example 37 by specifying the publication date ( dcterms:issued ) of each child dataset, and the previous ( dcat:prev ) and next ( dcat:next ) dataset in the series. Moreover, the dataset series is linked to its first ( dcat:first ) and last ( dcat:last ) child datasets.

ex:budget a dcat:DatasetSeries ;
  dcterms:title "Budget data" @en ;
  dcat :first ex:budget- 2018 ;
  dcat:last ex:budget- 2020 ;
  .
  
ex:budget- 2018 a dcat:Dataset ;
  dcterms:title "Budget data for year 2018" @en ;
  dcat:inSeries ex:budget ;
  dcterms :is sued " 2019 - 01 - 01 "^^xsd:date ;
  dcat:next ex:budget- 2019 ;
  .
  
ex:budget- 2019 a dcat:Dataset ;
  dcterms:title "Budget data for year 2019" @en ;
  dcat:inSeries ex:budget ;
  dcterms :is sued " 2020 - 01 - 01 "^^xsd:date ;
  dcat:prev ex:budget- 2018 ;
  dcat:next ex:budget- 2020 ;
  .
  
ex:budget- 2020 a dcat:Dataset ;
  dcterms:title "Budget data for year 2020" @en ;
  dcat:inSeries ex:budget ;
  dcterms :is sued " 2021 - 01 - 01 "^^xsd:date ;
  dcat:prev ex:budget- 2019 ;
  .

Datasets in a series can, of course, be versioned. In such a case, the dataset can be linked to its versions by using the approach illustrated in 11.1.1 Version chains and hierarchies , as shown in Example 39 .

This use case was contributed in Issue #1409 .

The following example extends Example 38 by supposing that dataset ex:budget-2019 has two different versions, namely, ex:budget-2019-rev0 and ex:budget-2019-rev1 . Dataset ex:budget-2019 is linked to its versions by using property dcat:hasVersion , and to its current version ( ex:budget-2019-rev1 ) by using property dcat:hasCurrentVersion .

ex:budget a dcat:DatasetSeries ;
  dcterms:title "Budget data" @en ;
  dcat :first ex:budget- 2018 ;
  dcat:last ex:budget- 2020 ;
  .
  
ex:budget- 2018 a dcat:Dataset ;
  dcterms:title "Budget data for year 2018" @en ;
  dcat:inSeries ex:budget ;
  dcterms :is sued " 2019 - 01 - 01 "^^xsd:date ;
  dcat:next ex:budget- 2019 ;
  .
  
ex:budget- 2019 a dcat:Dataset ;
  dcterms:title "Budget data for year 2019" @en ;
  dcat:inSeries ex:budget ;
  dcat :has Version ex:budget- 2019 -rev0 , ex:budget- 2019 -rev1 ;
  dcat :has CurrentVersion ex:budget- 2019 -rev1 ;
  dcterms :is sued " 2020 - 01 - 01 "^^xsd:date ;
  dcat:prev ex:budget- 2018 ;
  dcat:next ex:budget- 2020 ;
  .

ex:budget- 2019 -rev0 a dcat:Dataset ;
  dcterms:title "Budget data for year 2019" @en ;
  dcat:version "rev0" ;
  dcat :is VersionOf ex:budget- 2019 ;
  dcterms :is sued " 2020 - 01 - 01 "^^xsd:date ;
  .

ex:budget- 2019 -rev1 a dcat:Dataset ;
  dcterms:title "Budget data for year 2019" @en ;
  dcat:version "rev1" ;
  dcat :is VersionOf ex:budget- 2019 ;
  dcat:previousVersion ex:budget- 2019 -rev0 ;
  dcterms :is sued " 2020 - 05 - 10 "^^xsd:date ;
  .
  
ex:budget- 2020 a dcat:Dataset ;
  dcterms:title "Budget data for year 2020" @en ;
  dcat:inSeries ex:budget ;
  dcterms :is sued " 2021 - 01 - 01 "^^xsd:date ;
  dcat:prev ex:budget- 2019 ;
  .


### 12.2 Dataset series metadata

Properties about dataset series can be classified into two groups.

The first group is about properties describing the dataset series itself. For instance, this is the case of property dcterms:accrualPeriodicity , whose value should correspond to the frequency upon which a new child dataset is added.

The second group is about properties reflecting the dimensions described in child dataset metadata, via upstream inheritance - i.e., property values of child datasets are inherited by their parent (the dataset series).

Typically, this means that, for each of the relevant properties, the dataset series takes as value the union of those specified in child datasets. For instance:

If the temporal coverage of child datasets is a different year, e.g., 2018, 2019, 2020, the temporal coverage of the series will be the time period between years 2018 and 2020.

If child datasets have a different geographic bounding box as spatial coverage, the spatial coverage of the series will be the union of these bounding boxes (i.e., a bounding box including the ones of the child datasets).

If each child dataset uses a different spatial reference system, the dataset series will have multiple spatial reference systems.

Finally, some annotation properties of child datasets may need to be taken into account as well at the level of dataset series. In particular, properties concerning the creation / publication / update dates of child datasets may affect the corresponding ones in the series. For these properties, DCAT recommends the following approach:

The creation date ( dcterms:created ) of the dataset series should correspond to the earliest creation date of the child datasets.

The publication date ( dcterms:issued ) of the dataset series should correspond to the earliest publication date of the child datasets.

The update date ( dcterms:modified ) of the dataset series should correspond to the latest publication or update date of the child datasets.

To ensure dataset series metadata be correct and updated, mechanisms can be put in place to implement upstream inheritance automatically. However, DCAT does not recommend any specific strategy to be adopted.

The following example is a variant of Example 38 , with child datasets corresponding to yearly budget data for specific countries. The temporal resolution ( dcat:temporalResolution ), temporal coverage ( dcat:temporal ), and spatial coverage ( dcat:spatial ) of the dataset series correspond to the union of those of the child datasets. Moreover, the dataset series specifies as publication date the one of the first published child dataset, whereas the date of publication of the last child dataset is specified as update date ( dcterms:modified ). Finally, the update frequency ( dcterms:accrualPeriodicity ) of the dataset series is annual, as the child datasets are published on a yearly basis.

ex:budget a dcat:DatasetSeries ;
  dcterms:title "Budget data" @en ;
  dcterms :is sued " 2019 - 01 - 01 "^^xsd:date ,
  dcterms:modified "2021-01-01" ^^xsd:date ;
  dcterms:accrualPeriodicity <http://purl.org/cld/freq/annual> ;
  dcat:temporalResolution "P1Y" ^^xsd:duration ;
  dcterms:temporal [ a dcterms:PeriodOfTime ;
    dcat:startDate "2018-01-01" ^^xsd:date ;
    dcat:endDate "2020-12-31" ^^xsd:date ;
  ] ;  
  dcterms:spatial <http://publications.europa.eu/resource/dataset/country/BEL> ,
    <http://publications.europa.eu/resource/dataset/country/FRA> ,
    <http://publications.europa.eu/resource/dataset/country/ITA> ,
    ...  ;
  .
  
ex:budget- 2018 -be a dcat:Dataset ;
  dcterms:title "Belgium budget data for year 2018" @en ;
  dcat:inSeries ex:budget ;
  dcterms :is sued " 2019 - 01 - 01 "^^xsd:date ;
  dcat:next ex:budget- 2019 -be ;
  dcterms:accrualPeriodicity <http://purl.org/cld/freq/annual> ;
  dcat:temporalResolution "P1Y" ^^xsd:duration ;
  dcterms:temporal [ a dcterms:PeriodOfTime ;
    dcat:startDate "2018-01-01" ^^xsd:date ;
    dcat:endDate "2018-12-31" ^^xsd:date ;
  ] ;  
  dcterms:spatial <http://publications.europa.eu/resource/dataset/country/BEL> ;
  .
  
...
  
ex:budget- 2018 -fr a dcat:Dataset ;
  dcterms:title "France budget data for year 2018" @en ;
  dcat:inSeries ex:budget ;
  dcterms :is sued " 2019 - 01 - 01 "^^xsd:date ;
  dcat:next ex:budget- 2019 -fr ;
  dcterms:accrualPeriodicity <http://purl.org/cld/freq/annual> ;
  dcat:temporalResolution "P1Y" ^^xsd:duration ;
  dcterms:temporal [ a dcterms:PeriodOfTime ;
    dcat:startDate "2018-01-01" ^^xsd:date ;
    dcat:endDate "2018-12-31" ^^xsd:date ;
  ] ;  
  dcterms:spatial <http://publications.europa.eu/resource/dataset/country/FRA> ;
  .

...
  
ex:budget- 2018 -it a dcat:Dataset ;
  dcterms:title "Italy budget data for year 2018" @en ;
  dcat:inSeries ex:budget ;
  dcterms :is sued " 2019 - 01 - 01 "^^xsd:date ;
  dcat:next ex:budget- 2019 -it ;
  dcterms:accrualPeriodicity <http://purl.org/cld/freq/annual> ;
  dcat:temporalResolution "P1Y" ^^xsd:duration ;
  dcterms:temporal [ a dcterms:PeriodOfTime ;
    dcat:startDate "2018-01-01" ^^xsd:date ;
    dcat:endDate "2018-12-31" ^^xsd:date ;
  ] ;  
  dcterms:spatial <http://publications.europa.eu/resource/dataset/country/ITA> ;
  .
  
...


### 12.3 Dataset series in existing DCAT implementations

Existing DCAT implementations adopt two main alternative approaches to specifying dataset series:

The dataset series is typed as a dcat:Dataset , whereas its child datasets are typed as dcat:Distribution 's.

Both the dataset series and its child datasets are typed as a dcat:Dataset 's, and the two are usually linked by using the [ DCTERMS ] properties dcterms:hasPart / dcterms:isPartOf .

In both cases, the dataset series is sometimes soft-typed by using the [ DCTERMS ] property dcterms:type (e.g., this is the approach used in [ GeoDCAT-AP ], and adopted in [ DCAT-AP-IT ] and [ GeoDCAT-AP-IT ]).

These options are not formally incompatible with DCAT, so they can coexist with dcat:DatasetSeries during the upgrade to DCAT 3.


## 13. Data citation

This section is non-normative.

Dataset citation is one of the requirements identified.
        Data citation is the practice of referencing data in a similar way as when providing bibliographic references, acknowledging data
        as a first class output in any investigative process. Data citation offers multiple benefits, such as supporting proper attribution
        and credit to those producing the data, facilitating data discovery, supporting tracking the impact and reuse of data, allowing for
        collaboration and re-use of data, and enabling the reproducibility of results based on the data.

To support data citation, the dataset description should include at a minimum: the dataset identifier, the dataset creator(s), the dataset title,
        the dataset publisher and the dataset publication or release date. These elements are those required by the DataCite metadata schema [ DataCite ],
        which is the metadata associated by the persistent identifiers (Digital Object Identifiers or DOIs ) assigned by [ DataCite ] to research data.

In order to support data citation, DCAT 2 added the consideration of dereferenceable identifiers and support for indicating the creators of the cataloged resources . The remaining properties necessary for data citation were already available in DCAT 1 [ VOCAB-DCAT-1 ].

The constraints on the availability of properties required for data citation in the dataset description can be represented as a DCAT data citation profile.


## 14. Quality information

This section is non-normative.

This section is non-normative as it provides guidance on how to document the quality of DCAT
      first class entities (e.g., datasets, distributions) and it does not define new DCAT terms. The guidance relies on the
      Data Quality Vocabulary (DQV) [ VOCAB-DQV ], which is a W3C Group Note.

The Data Quality Vocabulary (DQV) [ VOCAB-DQV ] offers common modeling patterns for different aspects of Data
    Quality.
    It can relate  DCAT datasets and distributions with different types of quality information including:

dqv:QualityAnnotation , which represents feedback and quality certificates given about the dataset or its distribution.

dqv:QualityPolicy , which represents a policy or agreement that is chiefly governed by data quality concerns.

dqv:QualityMeasurement , which represents a metric value providing quantitative or qualitative information about the dataset or distribution.

Each type of quality information can pertain to one or more quality dimensions, namely, quality characteristics relevant
    to the consumer. The practice to see the quality as a multi-dimensional space is consolidated in the field of quality
    management to split the quality management into addressable chunks. DQV does not define a normative list of quality
    dimensions. It offers the quality dimensions proposed in ISO /IEC 25012 [ ISO-IEC-25012 ] and [ ZaveriEtAl ]
    as two possible starting points. It also provides an RDF representation for the quality dimensions and categories defined in the latter. Ultimately, implementers will need to choose themselves
    the collection of quality dimensions that best fits their needs.
    The following section shows how DCAT and DQV can be coupled to describe the quality of datasets and distributions.
    For a comprehensive introduction  and further examples of use, please refer to [ VOCAB-DQV ].

The following examples make no comments on where the quality information would reside and how it is managed. That
  is out of scope for the DCAT vocabulary.  The assumption made is that the quality individuals are available using
  the IRIs indicated.
        Besides, the examples and more in general the [ VOCAB-DQV ]  is neutral to the data portal design choices on how to collect
  quality information. For example, data portals can collect [ VOCAB-DQV ] instances by implementing specific UI to annotate
  data or by taking inputs from 3rd-party services.


### 14.1 Providing quality information

A data consumer ( ex:consumer1 )  describes the quality of the dataset ex:genoaBusStopsDataset that includes a georeferenced list of bus stops in Genoa. He/she annotates the dataset with a DQV quality note
  ( ex:genoaBusStopsDatasetCompletenessNote ) about data completeness ( ldqd:completeness ) to
  warn that the dataset includes only 20500 out of the 30000 stops.

ex:genoaBusStopsDataset a dcat:Dataset ;
  dqv:hasQualityAnnotation ex:genoaBusStopsDatasetCompletenessNote .

ex:genoaBusStopsDatasetCompletenessNote a dqv:UserQualityFeedback ;
  oa:hasTarget ex:genoaBusStopsDataset ;
  oa:hasBody ex:textBody ;
  oa:motivatedBy dqv:qualityAssessment ;
  prov:wasAttributedTo ex:consumer1 ;
  prov:generatedAtTime "2018-05-27T02:52:02Z"^^xsd:dateTime ;
  dqv:inDimension ldqd:completeness
  .

ex:textBody a oa:TextualBody ;
  rdf:value "Incomplete dataset: it contains only 20500 out of 30000 existing bus stops" ;
  dc:language "en" ;
  dc:format "text/plain"
  .

The activity ex:myQualityChecking employs the service ex:myQualityChecker to check the
  quality of the ex:genoaBusStopsDataset dataset. The metric ex:completenessWRTExpectedNumberOfEntities is applied to measure the dataset completeness ( ldqd:completeness ) and it results in the quality measurement ex:genoaBusStopsDatasetCompletenessMeasurement .

ex:genoaBusStopsDataset
  dqv:hasQualityMeasurement ex:genoaBusStopsDatasetCompletenessMeasurement .

ex:genoaBusStopsDatasetCompletenessMeasurement a dqv:QualityMeasurement ;
  dqv:computedOn ex:genoaBusStopsDataset ;
  dqv:isMeasurementOf ex:completenessWRTExpectedNumberOfEntities ;
  dqv:value "0.6833333"^^xsd:decimal  ;
  prov:wasAttributedTo ex:myQualityChecker ;
  prov:generatedAtTime "2018-05-27T02:52:02Z"^^xsd:dateTime ;
  prov:wasGeneratedBy ex:myQualityChecking
  .

ex:completenessWRTExpectedNumberOfEntities a dqv:Metric ;
  skos:definition "The degree of completeness as ratio between the actual number of entities included in the dataset and the declared expected number of entities."@en ;
  dqv:expectedDataType xsd:decimal ;
  dqv:inDimension ldqd:completeness .

# ex:myQualityChecker is a service computing some quality metrics
ex:myQualityChecker a prov:SoftwareAgent ;
  rdfs:label "A quality assessment service"@en .
  # Further details about quality service/software can be provided, for example,
  # deploying  vocabularies such as Dataset Usage Vocabulary (DUV), Dublin Core or ADMS.SW

# ex:myQualityChecking is the activity that has generated 
# ex:genoaBusStopsDatasetCompletenessMeasurement from ex:genoaBusStopsDataset
ex:myQualityChecking a prov:Activity ;
  rdfs:label "The checking of genoaBusStopsDataset's quality"@en ;
  prov:wasAssociatedWith ex:myQualityChecker ;
  prov:used ex:genoaBusStopsDataset ;
  prov:generated ex:genoaBusStopsDatasetCompletenessMeasurement ;
  prov:endedAtTime "2018-05-27T02:52:02Z"^^xsd:dateTime ;
  prov:startedAtTime "2018-05-27T00:52:02Z"^^xsd:dateTime .

Other examples of quality documentation are available in [ VOCAB-DQV ], including examples about how to express dataset accuracy and precision .


### 14.2 Documenting conformance to standards

This section shows different modeling patterns combining [ VOCAB-DQV ] with [ PROV-O ] and EARL [ EARL10-Schema ] to represent the conformance degree to a stated quality standard and the details about the conformance tests.


#### 14.2.1 Conformance to a standard

The use of dcterms:conformsTo and dcterms:Standard is a well-known pattern
      to represent the conformance to a standard. Example 43 , directly borrowed from [ SDW-BP ] ( Example 51 ), declares a fictitious dcat:Dataset conformant to the EU INSPIRE Regulation on interoperability of spatial data sets and services ( "Commission Regulation (EU) No 1089/2010
      of 23 November 2010 implementing Directive 2007/2/EC of the European Parliament and of the Council as regards
      interoperability of spatial data sets and services" ).

ex:Dataset-1 a dcat:Dataset;
  dcterms:conformsTo <http://data.europa.eu/eli/reg/2014/1312/oj> .

# Reference standard / specification
<http://data.europa.eu/eli/reg/2014/1312/oj> a dcterms:Standard ;
  dcterms:title "Commission Regulation (EU) No 1089/2010 of 23 November 2010 implementing Directive 2007/2/EC of the European Parliament and of the Council as regards interoperability of spatial data sets and services"@en ;
  dcterms:issued "2010-11-23"^^xsd:date .

Another example concerns the specification of the coordinate reference system ( CRS ) used in a dataset - an information which is typically included in geospatial metadata. Example 44 shows how the CRS of a dataset can be specified in DCAT:

ex:Dataset-2 a dcat:Dataset;
  dcterms:conformsTo <http://www.opengis.net/def/crs/EPSG/0/28992> .

In Example 44 , http://www.opengis.net/def/crs/EPSG/0/28992 is an IRI from the OGC CRS Registry, corresponding to EPSG:28992 ("Amersfoort / RD New") (see also Example 30 ).

The provision of a resource CRS complies with Best Practice 8 ( State how coordinate values are encoded ) from [ SDW-BP ].

In order to ensure interoperability, it is important to consistently use the IRIs identifying the reference standards / specifications. In particular, DCAT recommends the following general rules:

Use IRIs from reference registries, when available. Examples include the W3C TR registry , the OGC Definitions Server , the ISO OBP .

Use the IRI of the standard / specification, and not the namespace IRI . E.g., to express conformance of a dcat:CatalogRecord with DCAT, the IRI to be used is https://www.w3.org/TR/vocab-dcat/ , and not http://www.w3.org/ns/dcat# .

Use the canonical, persistent IRI . This is usually specified in the document itself. If you are in doubt, use the one included in the bibliographic citations for that standard / specification.

Use the non-versioned IRI . If you need to express conformance with a specific version of the standard / specification, use both the un-versioned and the versioned IRI . E.g., in case you need to explicitly state conformance of a dcat:CatalogRecord with DCAT 2, use both https://www.w3.org/TR/vocab-dcat/ and https://www.w3.org/TR/vocab-dcat-2/ .

Example 45 extends Example 9 to show how to specify that a given catalog record is conformant with DCAT, by following the above rules.

ex:catalog dcat:record ex:record-001 .

ex:record-001
  a dcat:CatalogRecord ;
  foaf:primaryTopic ex:dataset-001 ;
  dcterms:issued "2011-12-11"^^xsd:date ;
  dcterms:conformsTo <https://www.w3.org/TR/vocab-dcat/> ;
  .

The following table shows the IRIs of some of the standards used in the examples included in this document.


#### 14.2.2 Degree of conformance

Some legal context requires to specify the degree of conformance. For example, INSPIRE metadata adopts a
      specific controlled vocabulary [ INSPIRE-DoC ]
      to express non-conformance and non-evaluation beside the full compliance. Similar controlled vocabularies can
      be defined in other contexts.

Example 47 specifies some newly minted concepts representing the degree of conformance (i.e., conformant, not conformant) and  declares the dcterms:type for indicating
      the result of conformance test. Following a pattern used in [ GeoDCAT-AP ], the example uses a prov:Entity to model the  conformance test (e.g., ex:testResult ), a prov:Activity to model the testing activity (e.g., ex:testingActivity ), a prov:Plan derived from the Data on the Web Best Practices [ DWBP ] (e.g., ex:conformanceTest ) to check for the whole set of best practices. A qualified PROV association binds the testing activity to the conformance test.

Depending on the kind of dataset, other best practices and standards, such as the FAIR Principles [ FAIR ] or the Spatial Data on the Web Best Practices [ SDW-BP ], can be considered as a replacement or used in combination with [ DWBP ].

ex:Dataset-3 a dcat:Dataset ;
  prov:wasUsedBy ex:testingActivity .

ex:testingActivity a prov:Activity ;
  prov:generated ex:testResult ;
  prov:qualifiedAssociation [
    a prov:Association ;
    # http://validator.example.org/ is the agent who ran the test.
    prov:agent  <http://validator.example.org/>
    # following the plan ex:conformanceTest
    prov:hadPlan ex:conformanceTest
  ] .

# Conformance test result
ex:testResult a prov:Entity ;
  prov:wasGeneratedBy ex:testingActivity;
  # ex:notConformant belongs to a SKOS concept scheme about conformance
  dcterms:type ex:notConformant .

ex:conformanceTest a prov:Plan ;
  # Here one can specify additional information on the test, which in the example is derived by the W3C Data on the Web Best Practices
  prov:wasDerivedFrom <https://www.w3.org/TR/dwbp/> .

Also, [ VOCAB-DQV ] can be deployed to  measure the compliance to a specific standard. In Example 48 , the ex:levelOfComplianceToDWBP is a quality metrics which measures the compliance of a dataset to [ DWBP ] in terms of the percentage of passed compliance tests. Example 48 assumes iso as a namespace prefix representing the quality dimensions and categories defined in the ISO /IEC 25012 [ ISO-IEC-25012 ].

ex:levelOfComplianceToDWBP a dqv:Metric ;
  skos:definition "The degree of compliance to DWBP defined as the percentage of passed compliance tests."@en ;
  dqv:expectedDataType xsd:double ;
  dqv:inDimension  iso:compliance .

iso:compliance a dqv:Dimension ;
  skos:prefLabel "Compliance"@en ;
  skos:definition "The degree to which data has attributes that adhere to standards, conventions or regulations in force and similar rules relating to data quality in a specific context of use."@en ;
  dqv:inCategory iso:inherentAndSystemDependentDataQuality .
  
iso:inherentAndSystemDependentDataQuality a dqv:Category ;
  skos:prefLabel "Inherent and System-Dependent Data Quality"@en .

The quality measurement ex:measurement_complianceToDWBP represents the level of compliance for dataset ex:Dataset , namely, measurement of the metric ex:levelOfComplianceToDWBP . If only a part of the compliance tests succeeds (e.g., half of the compliance tests), the measurement would look like in Example 49 .

ex:measurement_complianceToDWBP a dqv:QualityMeasurement ;
  dqv:computedOn ex:Dataset ;
  dqv:value "50"^^xsd:double ;
  sdmx-attribute:unitMeasure <http://www.wurvoc.org/vocabularies/om-1.8/Percentage> ;
  dcterms:date "2018-01-10"^^xsd:date ;
  dqv:isMeasurementOf ex:levelOfComplianceToDWBP .


#### 14.2.3 Conformance test results

Further information about the tests can be provided using EARL [ EARL10-Schema ]. EARL provides specific
      classes to describe the testing activity, which can be adopted in conjunction with [ PROV-O ]. Example 50 describes the Testing activity ex:testingActivity as an earl:Assertion instead of a qualified association on the prov:Activity . The earl:Assertion states
      that dataset ex:Dataset has been tested with the conformance test ex:conformanceTest , and it
        has passed the test as described in ex:testResult .

ex:assertion a earl:Assertion ;
  earl:subject ex:Dataset ;
  earl:test ex:conformanceTest ;
  earl:result ex:testResult ;
  # let's indicate if the test was manual, automatic, or what ..
  earl:mode earl:automatic ;
  earl:assertedBy <http://validator.example.org/> ;
  prov:wasAttributedTo  <http://validator.example.org/> .

ex:conformanceTest a earl:TestRequirement, prov:Plan ;
  dcterms:title "Set of conformance test derived from the W3C Data on the Web Best Practices"@en ;
  # it includes different subtests
  dcterms:hasPart ex:testBP1, ex:testBP2, ...,  ex:testBP35 ;
  #It is derived  by the reference standard
  prov:wasDerivedFrom  <https://www.w3.org/TR/dwbp/> .

ex:testResult a earl:TestResult ;
  #  results in conformancy .
  dcterms:type  ex:conformant ;
  prov:wasGeneratedBy ex:testingActivity;
  #the overall set of tests have been passed
  earl:outcome earl:passed .

# the description of the validator
<http://validator.example.org/> a earl:Assertor, prov:Agent ;
  dcterms:description "A test execution service that runs conformance test suites."@en ;
  dcterms:title "Validator"@en .

#the testing activity
ex:testingActivity a prov:Activity ;
  prov:generated ex:assertion, ex:testResult ;
  prov:use ex:Dataset ;
  prov:wasAssociatedWith <http://validator.example.org/> .

Example 51 shows how the description would have looked like if the subtest ex:testq1 had failed. In particular, dcterms:description and earl:info provide additional warnings or error messages in a human-readable form.

ex:assertion1 a earl:Assertion ;
  earl:subject ex:Dataset ;
  earl:test ex:testq1 ;
  earl:result [
    a earl:TestResult ;
    #  results in no conformancy
    dcterms:type ex:nonConformant ;
    #the overall set of tests have not been passed (!?)
    dcterms:date "2015-09-29T11:50:00+00:00"^^xsd:dateTime ;
    # Some XML encoding of the error
      dcterms:description """
        <ul xmlns="http://www.w3.org/1999/xhtml">
          <li> test 1 has failed. Some description of the errors found</li>
        </ul>"""^^rdf:HTML ;
      earl:info """
        <test-method duration-ms="47" finished-at="2015-09-29T11:50:00Z"
        name="validate" signature="validate()" started-at="2015-09-29T11:50:00Z"
        status="FAIL">
          <exception class="java.lang.AssertionError">
            <message>
              Total validation errors found: 2
            </message>
          </exception>
        </test-method>"""^^rdf:XMLLiteral ;
     earl:outcome earl:fail .
  ];
  # we do not know if the test was manual, automatic, or what ..
  earl:mode earl:automatic.

Depending on the details required about tests, [ VOCAB-DQV ] can express the testing activity and errors as well. In Example 52 , ex:error is a quality annotation that represents the previous error, and ex:testResult is defined as a dqv:QualityMetadata to  collect the above annotations and the compliance measurements providing  provenance information.

ex:errors
  a dqv:QualityAnnotation ;
  #this annotation is derived by the measurement
  prov:wasGeneratedBy  ex:testingActivity;
  oa:hasTarget ex:Dataset ;
  oa:hasBody [
    #errors/failed test description
    a oa:TextualBody ;
    rdf:value  """
      <test-method duration-ms="47" finished-at="2015-09-29T11:50:00Z"
        name="validate" signature="validate()" started-at="2015-09-29T11:50:00Z"
        status="FAIL">
        <exception class="java.lang.AssertionError">
          <message>
            Total validation errors found: 2
          </message>
        </exception>
      </test-method>"""^^rdf:XMLLiteral ;
    #it can be in any format supported by dc
    dc:format  "application/xml" ;
  ] ;
  oa:motivatedBy dqv:qualityAssessment , oa:assessing ;
  dqv:inDimension iso:compliance ;
  .

ex:testResult
  a dqv:QualityMetadata ;
  #  change the the dcterms:type according to the resulted compliance
  dcterms:type <http://inspire.ec.europa.eu/metadata-codelist/DegreeOfConformity/conformant> ;
  prov:wasAttributedTo <http://validator.example.org/> ;
  prov:generatedAtTime "2018-05-27T02:52:02Z"^^xsd:dateTime ;
  prov:wasGeneratedBy ex:testingActivity .

# The graph contains the rest of the statements presented in the previous examples.
# The graph is expressed according to TRIG syntax not TTL (see https://www.w3.org/TR/trig/)
ex:testResult {
  a dcat:Dataset ;
  dqv:hasQualityMeasurement ex:measurement_complianceToDWBP ;
  dqv:hasQualityAnnotation ex:errors .
}

#the testing activity
ex:testingActivity a prov:Activity ;
  prov:generated  ex:testResult ;
  prov:use ex:Dataset ;
  prov:wasAssociatedWith <http://validator.example.org/> ;
  .

Of course, the above modeling patterns can represent any quality tests, not only conformance to standards.


## 15. Qualified relations

This section is non-normative.

DCAT includes elements to support description of many aspects of datasets and data services. Nevertheless, additional information is required in order to fully express the semantics of some relationships. An example is that, while [ DCTERMS ] provides the standard roles creator , contributor and publisher for attribution of a resource to a responsible party or agent, there are many other potential roles, see for example the CI_RoleCode values from [ ISO-19115-1 ]. Similarly, while [ DCTERMS ] and [ PROV-O ] provide some properties to capture relationships between resources, including was derived from , was quoted from , is version of , references and several others, many additional concerns are seen in the list of [ ISO-19115-1 ] DS_AssociationTypeCodes , the IANA Registry of Link Relations [ IANA-RELATIONS ], the DataCite metadata schema [ DataCite ]
    and the MARC relators . While these relations could be captured with additional sub-properties of dcterms:relation , dcterms:contributor , etc., this would lead to an explosion in the number of properties, and anyway the full set of potential roles and relationships is unknown.

A common approach for meeting these kinds of requirements is to introduce an additional resource to carry parameters that qualify the relationship. Precedents are the qualified terms in [ PROV-O ] and the sample relations in the Semantic Sensor Network ontology [ VOCAB-SSN ]. The general Qualified Relation pattern is described in [ LinkedDataPatterns ].

Many of the qualified terms from [ PROV-O ] are relevant to the description of resources in catalogs but these are incomplete due to the activity-centric viewpoint taken by PROV-O. Addressing some of the gaps, additional forms are included in the DCAT vocabulary to satisfy requirements that do not involve explicit activities. These are summarized in Figure 6 :

Note that, while the focus of these qualified forms is to allow for additional roles on a relationship, other aspect of the relationships, such as the applicable time interval, are easily attached when a specific node is used to describe the relationship like this (e.g., see the chart of Influence relations in [ PROV-O ] for some examples).

Because of the global domain constraints on prov:qualifiedAttribution and the super-property of dcat:qualifiedRelation , use of the qualified forms entail that the context resource is a member of the class prov:Entity [ RDF-SCHEMA ].


### 15.1 Relationships between datasets and agents

The standard [ DCTERMS ] properties dcterms:contributor , dcterms:creator and dcterms:publisher , and the generic prov:wasAttributedTo from [ PROV-O ], support basic associations of responsible agents with a cataloged resource.
    However, there are many other roles of importance in relation to datasets and services - e.g., funder, distributor, custodian, editor.
    Some of these roles are enumerated in the CI_RoleCode values from [ ISO-19115-1 ], in the [ DataCite ] metadata schema, and included within the MARC relators .

A general method for assigning an agent to a resource with a specified role is provided by using the qualified form prov:qualifiedAttribution from [ PROV-O ]. Example 53 provides an illustration:

ex:DS987
  a dcat:Dataset ;
  prov:qualifiedAttribution [
    a prov:Attribution ;
    prov:agent <https://www.ala.org.au/> ;
    dcat:hadRole <urn:example:isotc211/CI_RoleCode/distributor>
  ] ;
  prov:qualifiedAttribution [
    a prov:Attribution ;
    prov:agent <https://www.education.gov.au/> ;
    dcat:hadRole <urn:example:isotc211/CI_RoleCode/funder>
  ] ;
.

In Example 53 the roles are denoted by IRIs from a non-normative, non-dereferenceable representation of the CI_RoleCode codelist from [ ISO-19115-1 ] (e.g., URN like urn:example:isotc211/CI_RoleCode ). Linked data dereferenceable and normative representations should be preferred when available.

The domain of prov:hadRole property is prov:Association , i.e., [ PROV-O ] roles relate to activities, not entities [ PROV-O ].
  Therefore, a new property dcat:hadRole is used to attach a specific role to the association-class prov:Attribution .


### 15.2 Relationships between datasets and other resources

The standard [ DCTERMS ] properties dcterms:relation and sub-properties such as dcterms:hasPart / dcterms:isPartOf , dcterms:hasVersion / dcterms:isVersionOf , dcterms:replaces / dcterms:isReplacedBy , dcterms:requires / dcterms:isRequiredBy , prov:wasDerivedFrom , prov:wasQuotedFrom ,
    support the description of relationships between datasets and other cataloged resources.
    However, there are many other relationships of importance - e.g., alternate, canonical, original, preview, stereo-mate, working-copy-of.
    Some of these roles are enumerated in the DS_AssociationTypeCodes values from [ ISO-19115-1 ], the IANA Registry of Link Relations [ IANA-RELATIONS ], in the [ DataCite ] metadata schema, and included within the MARC relators .

A general method for relating a resource to another resource with a specified role is provided by using the qualified form dcat:qualifiedRelation . Example 54 provides illustrations:

ex:Test987
  a dcat:Dataset ;
  dcat:qualifiedRelation [
    a dcat:Relationship ;
    dcterms:relation <http://dcat.example.org/Original987> ;
    dcat:hadRole <http://www.iana.org/assignments/relation/original>
  ] ;
.

ex:Test543L
  a dcat:Dataset ;
  dcat:qualifiedRelation [
    a dcat:Relationship ;
    dcterms:relation <http://dcat.example.org/Test543R> ;
    dcat:hadRole <urn:example:isotc211/DS_AssociationTypeCode/stereoMate>
  ] ;
.

In Example 54 the roles are denoted by IRIs from [ IANA-RELATIONS ] and from a (non-normative) linked data representation of the DS_AssociationTypeCode codelist from [ ISO-19115-1 ].

The property dcat:qualifiedRelation and association-class dcat:Relationship follow the pattern established in W3C [ PROV-O ] and described in § 3.3 Qualified Terms .
  However, [ PROV-O ] is activity-centric, and does not support Entity-Entity relations except for the single case of 'was derived from', thus necessitating the new elements shown here to support the general case.


## 16. DCAT Profiles

This section is non-normative.

The DCAT-2014 vocabulary [ VOCAB-DCAT-1 ] and DCAT 2 [ VOCAB-DCAT-2 ] have been extended for application in data catalogs in different domains.
        Each of these new specifications constitutes a DCAT profile, i.e., a named set of constraints based on DCAT (see 4. Conformance ). In some cases,
        a profile extends one of the DCAT profiles themselves, by adding classes and properties for metadata fields not covered in the reference DCAT profile.

Some of the DCAT profiles are:

DCAT-AP [ DCAT-AP ]: The DCAT application profile for data portals in Europe

GeoDCAT-AP [ GeoDCAT-AP ]: Geospatial profile of [ DCAT-AP ]

StatDCAT-AP [ StatDCAT-AP ]: Statistical profile of [ DCAT-AP ]

DCAT-AP_IT [ DCAT-AP-IT ]: Italian profile of [ DCAT-AP ]

GeoDCAT-AP_IT [ GeoDCAT-AP-IT ]: Italian profile of [ GeoDCAT-AP ]

DCAT-AP-NO [ DCAT-AP-NO ]: Norwegian profile of [ DCAT-AP ]

DCAT-AP.de [ DCAT-AP.de ]: German profile of [ DCAT-AP ]

DCAT-BE [ DCAT-BE ]: Belgian profile of [ DCAT-AP ]

DCAT-AP-SE [ DCAT-AP-SE ]: Swedish profile of [ DCAT-AP ]


## 17. Security and Privacy Considerations

The DCAT vocabulary supports datasets that may contain personal or private information. In addition, the metadata expressed with DCAT may itself contain personal or private information, such as resource creators , publishers , and other parties or agents described via qualified relations .
    Implementers who produce, maintain, publish or consume such vocabulary terms must take steps to ensure security and privacy considerations are addressed. Sensitive data and metadata must be stored securely and made available only to authorized parties, in accordance with the legal and functional requirements of the type of data involved. Detailing how to secure web content and authenticate users is beyond the scope of DCAT.

Some datasets require assurances of integrity and authenticity (for example, data about software vulnerabilities). For these, checksums can serve as a type of verification. 
    DCAT borrows the spdx:Checksum class from [ SPDX ] to ensure the integrity and authenticity of DCAT distributions. Publishers may provide a checksum value (a hash) and the algorithm used to generate the hash for each resource in the distribution. A checksum must, however, be provided via a route that is separate from the data it sums. It may be included in metadata that is provided with the data (e.g., a tarfile that includes a file for the distribution and a file for the metadata that includes a checksum for the distribution file), but if so the checksum, or a checksum for the metadata, must also be provided separately to foil an attacker who would manipulate the checksum along with the data. A checksum provided in DCAT metadata will not provide the expected assurances if the integrity and authenticity of the metadata are not also guaranteed.

Integrity and authenticity of DCAT data ultimately depend on the trustworthiness of the source. DCAT providers should address integrity and authenticity at the application level and transport level. For example, they should ensure the integrity and authenticity of their API and download endpoints, make DCAT data and metadata files downloadable from authoritative HTTPS origins, and provide any checksums via a separate channel from the data they represent.


## 18. Accessibility Considerations

The DCAT vocabulary provides a model for describing data catalogs. The nature of data in the catalogs depends on the specific domains of application and might include non-text data.  When possible, it is important to enforce alternative text for non-text data resources through the DCAT profile mechanisms or systems supporting the creation and editing of such data to improve the accessibility to data. The practice to provide text alternatives for any non-text content, which can be changed into other forms people need, such as large print, braille, speech, symbols, or simpler language complies with accessibility guidelines included in [ UNDERSTANDING-WCAG20 ].


## A. Acknowledgments

The editors gratefully acknowledge the contributions made to this document by all members of the working group , especially
  
  Annette Greiner, 
  Antoine Isaac, 
   
  Dan Brickley, 
  
  
  Karen Coyle, 
  Lars G. Svensson, 
  
  Makx Dekkers, 
  Nicholas Car, 
  Rob Atkinson, 
  Tom Baker.

The editors would also like to thank the following for comments received: 
  
  Addison Phillips, 
  Alex Nelson,
  Andreas Geißner,
  Andreas Kuckartz, 
  Anna Odgaard Ingram, 
   
  Aymen Charef,
  Bart Hanssens,
  Becky Gibson,
  Bert van Nuffelen, 
  Bob Coret, 
  Brian Donohue,
  Chavdar Ivanov,
  
  
  
  Claus Stadler,
  
  Cristiano Longo, 
  Christophe Dzikowski,
  
  
  Dimitris Zeginis,
  Dominik Schneider,
  Emidio Stani,
  
  
  Ivo Velitchkov,
  Jakob Voß, 
  Jakub Klímek, 
  Jan Voskuil,
  
  Jim J. Yang,
  Joep Meindertsma,
  Joep van Genuchten, 
  Katherine Anderson Aur,
  
  
  Ludger A. Rinsche,
  
  Marielle Adam, 
  Martial Honsberger,
  Mathias Bonduel,
  Mathias Richter,
  
  Matthias Palmér, 
  
  
  Nancy Jean,
  Nuno Freire,
  Øystein Åsnes, 
  
  Paul van Genuchten,
  
  Pieter J. C. van Everdingen,
  Renato Iannella, 
  Rajaram Kaliyaperumal,
  Robin Gower,
  
  Sabine Maennel,
  Sebastian Hellman,
  
  Simson L. Garfinkel,
  Siri Jodha S. Khalsa, 
  
  Stefan Ollinger,
  Stephen Richard, 
  Stian Soiland-Reyes,
  Stig B. Dørmænen,
  
  Susheel Varma,
  Sidney Cox,
  Thomas Francart,
  
  Vittorio Meloni,
  
  Wouter Beek, 
  Yves Coene.

The editors also gratefully acknowledge the chairs of this Working Group: Caroline Burle and Peter Winstanley — and staff contacts Philippe Le Hégaret and Pierre-Antoine Champin.


## B. Alignment with Schema.org

This section is non-normative.

See the issues on Alignments and Crosswalks for more discussion.

Schema.org [ SCHEMA-ORG ] includes a number of types and properties based on the original DCAT work (see sdo:Dataset as a starting point),
            and the index for Google's Dataset Search service relies on structured description in Web pages about datasets using both schema.org and DCAT .
            A comparison of the DCAT backbone, shown in Figure 1 above with the related classes from [ SCHEMA-ORG ] in Figure 7 shows the similarity, in particular: .

the distinction between (abstract) Dataset and (concrete) DataDownload matches  dcat:Dataset / dcat:Distribution

the relationship of Datasets to DataCatalogs

General purpose Web search services that use metadata at all rely primarily on [ SCHEMA-ORG ], so the relationship of DCAT to [ SCHEMA-ORG ] is of interest for data providers and catalog publishers who wish their datasets and services to be exposed through those indexes.

A mapping between DCAT 1 and schema.org was discussed on the original proposal to extend [ SCHEMA-ORG ] for describing datasets and data catalogs.
            Partial mappings between DCAT 1 [ VOCAB-DCAT-1 ] and [ SCHEMA-ORG ] were provided earlier by the Spatial Data on the Web Working Group , building upon previous work.

A recommended mapping from the revised DCAT (this document) to [ SCHEMA-ORG ] version 3.4 is available in an RDF file .
            This mapping is axiomatized using the predicates rdfs:subClassOf , rdfs:subPropertyOf , owl:equivalentClass , owl:equivalentProperty , skos:closeMatch ,
            and also using the annotation properties sdo:domainIncludes and sdo:rangeIncludes to match [ SCHEMA-ORG ] semantics. The alignment is summarized in the table below, considering the prefix sdo as http://schema.org/ .


## C. Examples

This section is non-normative.


### C.1 Loosely structured catalog

The background to this example is discussed in Issue #253 ("Best practice for a loosely-structured catalog").

In many legacy catalogs and repositories (e.g., CKAN), ‘datasets’ are ‘just a bag of files’. There is no distinction made between distribution (representation), and other kinds of relationship (e.g., documentation, schema, supporting documents) from the dataset to each of the files.

If the nature of the relationships between a dataset and component resources in a catalog, repository, or elsewhere are not known, dcterms:relation or its sub-property dcterms:hasPart can be used:

ex:d33937
  dcterms:description "A set of RDF graphs representing the International [Chrono]stratigraphic Chart, ..."@en ;
  dcterms:identifier "https://doi.org/10.25919/5b4d2b83cbf2d"^^xsd:anyURI ;
  dcterms:creator <https://orcid.org/0000-0002-3884-3420> ;
  dcterms:relation ex:ChronostratChart2017-02.pdf  ;
  dcterms:relation ex:ChronostratChart2017-02.jpg ;
  dcterms:hasPart ex:timescale.zip ;
  dcterms:hasPart ex:d33937-jsonld ;
  dcterms:hasPart ex:d33937-nt ;
  dcterms:hasPart ex:d33937-rdf ;
  dcterms:hasPart ex:d33937-ttl ;
.

If the nature of the relationship is known, then other sub-properties of dcterms:relation should be used to convey this. In particular, if it is clear that any of these related resources is a proper representation of the dataset, then dcat:distribution should be used.

ex:d33937
  rdf:type dcat:Dataset ;
  dcterms:description "A set of RDF graphs representing the International [Chrono]stratigraphic Chart, ..."@en ;
  dcterms:identifier "https://doi.org/10.25919/5b4d2b83cbf2d"^^xsd:anyURI ;
  dcterms:hasFormat ex:ChronostratChart2017-02.pdf  ;
  dcterms:hasFormat ex:ChronostratChart2017-02.jpg ;
  dcat:distribution ex:timescale.zip ;
  dcat:distribution ex:d33937-jsonld ;
  dcat:distribution ex:d33937-nt ;
  dcat:distribution ex:d33937-rdf ;
  dcat:distribution ex:d33937-ttl ;
.
ex:d33937-jsonld  rdf:type dcat:Distribution ;
  dcat:downloadURL ex:isc2017.jsonld ;
  dcat:byteSize "698039"^^xsd:nonNegativeInteger ;
  dcat:mediaType <http://www.iana.org/assignments/media-types/application/ld+json> ;
.
ex:d33937-nt  rdf:type dcat:Distribution ;
  dcat:downloadURL ex:isc2017.nt ;
  dcat:byteSize "2047874"^^xsd:nonNegativeInteger ;
  dcat:mediaType <http://www.iana.org/assignments/media-types/application/n-triples> ;
.
ex:d33937-rdf  rdf:type dcat:Distribution ;
  dcat:downloadURL ex:isc2017.rdf ;
  dcat:byteSize "1600569"^^xsd:nonNegativeInteger ;
  dcat:mediaType <http://www.iana.org/assignments/media-types/application/rdf+xml> ;
.
ex:d33937-ttl  rdf:type dcat:Distribution ;
  dcat:downloadURL ex:isc2017.ttl ;
  dcat:byteSize "531703"^^xsd:nonNegativeInteger ;
  dcat:mediaType <http://www.iana.org/assignments/media-types/text/turtle> ;
.

This example is available from the DXWG DCAT 3 code repository at csiro-dap-examples.ttl and csiro-stratchart_dcat3.ttl .

Additional detail about the nature of the related resources can be given using suitable elements from other RDF vocabularies, along with dataset descriptors from DCAT. For example, the example above might be more fully expressed as follows (embedded comments explain the different resources in the graph):

dap:d33937
  rdf:type dcat:Dataset ;
  dcterms:title "The data"@en ;
  dcterms:conformsTo <http://resource.geosciml.org/ontology/timescale/gts> ;
  dcterms:description "A set of RDF graphs representing the International [Chrono]stratigraphic Chart [...]"@en ;
  dcterms:identifier "https://doi.org/10.25919/5b4d2b83cbf2d" ;
  dcterms:issued "2018-07-07"^^xsd:date ;
  dcterms:license <https://creativecommons.org/licenses/by/4.0/> ;
  dcterms:publisher <http://www.csiro.au> ;
  dcterms:hasPart <http://stratigraphy.org/ICSchart/ChronostratChart2017-02.jpg> ;
  dcterms:hasPart <http://stratigraphy.org/ICSchart/ChronostratChart2017-02.pdf> ;
  dcterms:hasPart [
    rdf:type dcat:Dataset ;
    dcterms:conformsTo <https://www.w3.org/TR/owl2-overview/> ;
    dcterms:title "The ontology used for the data"@en ;
    dcterms:description "This is an RDF/OWL representation of the GeoSciML Geologic Timescale model ..."@en ;
    dcterms:issued "2011-01-01"^^xsd:date ;
    dcterms:modified "2017-04-28"^^xsd:date ;
    dcterms:title "Geologic Timescale model" ;
    dcterms:type <http://purl.org/adms/assettype/DomainModel> ;
    dcat:distribution [
      rdf:type dcat:Distribution ;
      dcterms:title "RDF/XML representation of the ontology used for the data"@en ;
      dcat:downloadURL <http://resource.geosciml.org/ontology/timescale/gts.rdf> ;
      dcat:mediaType <http://www.iana.org/assignments/media-types/application/rdf+xml> ;
    ] ;
    dcat:distribution [
      rdf:type dcat:Distribution ;
      dcterms:title "TTL representation of the ontology used for the data"@en ;
      dcat:downloadURL <http://resource.geosciml.org/ontology/timescale/gts.ttl> ;
      dcat:mediaType <http://www.iana.org/assignments/media-types/text/turtle> ;
    ] ;
    dcat:distribution [
      rdf:type dcat:Distribution ;
      dcterms:title "Webpage describing the ontology used for the data"@en ;
      dcat:downloadURL <http://resource.geosciml.org/ontology/timescale/gts.html> ;
      dcat:mediaType <http://www.iana.org/assignments/media-types/text/html> ;
    ] ;
    dcat:landingPage <http://resource.geosciml.org/ontology/timescale/gts> ;
  ] ;
  dcat:distribution [
    rdf:type dcat:Distribution ;
    dcterms:conformsTo <https://www.w3.org/TR/rdf-schema/> ;
    dcterms:title "RDF representation of the data"@en ;
    dcat:accessService [
      rdf:type dcat:DataService ;
      dcterms:conformsTo <https://www.w3.org/TR/sparql11-protocol/> ;
      dcterms:title "International Chronostratigraphic Chart hosted at Research Vocabularies Australia"@en ;
      dcterms:description "Service that supports queries to obtain RDF representations of subsets of the data"@en ;
      dcat:endpointURL <http://vocabs.ands.org.au/repository/api/sparql/csiro_international-chronostratigraphic-chart_2017> ;
      dcat:landingPage <https://vocabs.ands.org.au/viewById/196> ;
    ] ;
  ] ;
  dcat:distribution [
    rdf:type dcat:Distribution ;
    dcterms:identifier "isc2017.jsonld" ;
    dcterms:title "JSON-LD serialization of the RDF representation of the entire dataset"@en ;
    dcat:mediaType <http://www.iana.org/assignments/media-types/application/ld+json> ;
  ] ;
  dcat:distribution [
    rdf:type dcat:Distribution ;
    dcterms:identifier "isc2017.nt" ;
    dcterms:title "N-Triples serialization of the RDF representation of the entire dataset"@en ;
    dcat:mediaType <http://www.iana.org/assignments/media-types/application/n-triples> ;
  ] ;
  dcat:distribution [
    rdf:type dcat:Distribution ;
    dcterms:identifier "isc2017.rdf" ;
    dcterms:title "RDF/XML serialization of the RDF representation of the entire dataset"@en ;
    dcat:mediaType <http://www.iana.org/assignments/media-types/application/rdf+xml> ;
  ] ;
  dcat:distribution [
    rdf:type dcat:Distribution ;
    dcterms:identifier "isc2017.ttl" ;
    dcterms:title "TTL serialization of the RDF representation of the entire dataset"@en ;
    dcat:mediaType <http://www.iana.org/assignments/media-types/text/turtle> ;
  ] ;
  dcat:landingPage <https://data.csiro.au/dap/landingpage?pid=csiro:33937> ;
.

<http://stratigraphy.org/ICSchart/ChronostratChart2017-02.jpg>
  rdf:type foaf:Document ;
  dcterms:type <http://purl.org/dc/dcmitype/Image> ;
  dcterms:format  <http://www.iana.org/assignments/media-types/img/jpeg> ;
  dcterms:description "Coloured image representation of the International Chronostratigraphic Chart"@en ;
  dcterms:issued "2017-02-01"^^xsd:date ;
  dcterms:title "International Chronostratigraphic Chart"@en ;
.
<http://stratigraphy.org/ICSchart/ChronostratChart2017-02.pdf>
  rdf:type foaf:Document ;
  dcterms:type <http://purl.org/dc/dcmitype/Image> ;
  dcterms:format <http://www.iana.org/assignments/media-types/application/pdf> ;
  dcterms:description "Coloured image representation of the International Chronostratigraphic Chart"@en ;
  dcterms:issued "2017-02-01"^^xsd:date ;
  dcterms:title "International Chronostratigraphic Chart"@en ;
.

This example is available from the DXWG DCAT 3 code repository at csiro-stratchart.ttl .


### C.2 Dataset provenance

The provenance or business context of a dataset can be described using elements from the W3C Provenance Ontology [ PROV-O ].

For example, a simple link from a dataset description to the project that generated the dataset can be formalized as follows (other details elided for clarity):

dap:atnf-P366-2003SEPT
  rdf:type dcat:Dataset ;
  dcterms:bibliographicCitation "Burgay, M; McLaughlin, M; Kramer, M; Lyne, A; Joshi, B; Pearce, G; D'Amico, N; Possenti, A; Manchester, R; Camilo, F (2017): Parkes observations for project P366 semester 2003SEPT. v1. CSIRO. Data Collection. https://doi.org/10.4225/08/598dc08d07bb7" ;
  dcterms:title "Parkes observations for project P366 semester 2003SEPT"@en ;
  dcat:landingPage <https://data.csiro.au/dap/landingpage?pid=csiro:P366-2003SEPT> ;
  prov:wasGeneratedBy dap:P366 ;
  .

dap:P366
  rdf:type prov:Activity ;
  dcterms:type <http://dbpedia.org/resource/Observation> ;
  prov:startedAtTime "2000-11-01"^^xsd:date ;
  prov:used dap:Parkes-radio-telescope ;
  prov:wasInformedBy dap:ATNF ;
  rdfs:label "P366 - Parkes multibeam high-latitude pulsar survey"@en ;
  rdfs:seeAlso <https://doi.org/10.1111/j.1365-2966.2006.10100.x> ;
  .

This example is available from the DXWG DCAT 3 code repository at csiro-dap-examples.ttl .

Several properties capture provenance information, including within the citation and title, but the primary link to a formal description of the project is through prov:wasGeneratedBy .
          A terse description of the project is shown as a prov:Activity , though this would not necessarily be part of the same catalog.
          Note that as the project is ongoing, the activity has no end date.

Further provenance information might be provided using the other starting point properties from PROV, in particular prov:wasAttributedTo (to link to an agent associated with the dataset production) and prov:wasDerivedFrom (to link to a predecessor dataset). Both of these complement Dublin Core properties already used in DCAT, as follows:

prov:wasAttributedTo provides a general link to all kinds of associated agents, such as project sponsors, managers, dataset owners, etc., which are not correctly characterized using dcterms:creator , dcterms:contributor or dcterms:publisher .

prov:wasDerivedFrom supports a more specific relationship to an input or predecessor dataset compared with dcterms:source , which is not necessarily a previous dataset.

Further patterns for the use of qualified properties for resource attribution and interrelationships are described in 15. Qualified relations .


### C.3 Link datasets and publications

Datasets are often associated with publications (scholarly articles, reports, etc.) and DCAT relies on the property dcterms:isReferencedBy to provide a way to link publications about a dataset to the dataset

The following example shows how a dataset published in the Dryad repository is linked to a publication available in the Nature Scientific Data journal :

ex:globtherm
  dcterms:title "Data from: GlobTherm, a global database on thermal tolerances for aquatic and terrestrial organisms"@en ;
  dcterms:description "How climate affects species distributions is a longstanding question receiving renewed interest owing to the need to predict the impacts of global warming on biodiversity. Is climate change forcing species to live near their critical thermal limits? Are these limits likely to change through natural selection? These and other important questions can be addressed with models relating geographical distributions of species with climate data, but inferences made with these models are highly contingent on non-climatic factors such as biotic interactions. Improved understanding of climate change effects on species will require extensive analysis of thermal physiological traits, but such data are scarce and scattered. To overcome current limitations, we created the GlobTherm database. The database contains experimentally derived species’ thermal tolerance data currently comprising over 2,000 species of terrestrial, freshwater, intertidal and marine multicellular algae, plants, fungi, and animals. The GlobTherm database will be maintained and curated by iDiv with the aim of expanding it, and enable further investigations on the effects of climate on the distribution of life on Earth."@en ;
  dcterms:identifier "https://doi.org/10.5061/dryad.1cv08"^^xsd:anyURI ;
  dcterms:creator <https://orcid.org/0000-0002-7883-3577> ;
  dcterms:relation <https://doi.org/10.5061/dryad.1cv08/6> ;
  dcterms:relation <https://doi.org/10.5061/dryad.1cv08/7> ;
  dcterms:isReferencedBy <https://doi.org/10.1038/sdata.2018.22>.

This example is available from the DXWG DCAT 3 code repository at dryad-globtherm-sdata.ttl


### C.4 Data services

Data services may be described using DCAT.
          The values of the classifiers dcterms:type , dcterms:conformsTo , and dcat:endpointDescription provide progressively more detail about a service, whose actual endpoint is given by the dcat:endpointURL .

The first example describes a data catalog hosted by the European Environment Agency (EEA).
          This is classified as a dcat:DataService and has the dcterms:type set to " discovery " from the INSPIRE classification of spatial data service types [ INSPIRE-SDST ].

This example is available from the DXWG DCAT 3 code repository at eea-csw.ttl

ex:EEA-CSW-Endpoint
  rdf:type dcat:DataService ;
  dcterms:type <http://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceCategory/infoCatalogueService> ;
  dcterms:accessRights <http://publications.europa.eu/resource/authority/access-right/PUBLIC> ;
  dcterms:conformsTo <http://www.opengis.net/def/serviceType/ogc/csw> ;
  dcterms:description "The EEA public catalogue of spatial datasets references
    the spatial datasets used by the European Environment Agency as well as
    the spatial datasets produced by or for the EEA. In the latter case,
    when datasets are publicly available, a link to the location from where
    they can be downloaded is included in the dataset's metadata. The
    catalogue has been initially populated with the most important spatial
    datasets already available on the data&maps section of the EEA website
    and is currently updated with any newly published spatial dataset."@en ;
  dcterms:identifier "eea-sdi-public-catalogue" ;
  dcterms:issued "2012-01-01"^^xsd:date ;
  dcterms:license <https://creativecommons.org/licenses/by/2.5/dk/> ;
  dcterms:spatial [
    rdf:type dcterms:Location ;
    dcat:bbox "POLYGON((-180 90,180 90,180 -90,-180 -90,-180 90))"^^gsp:wktLiteral ;
  ] ;
  dcterms:title "European Environment Agency's public catalogue of spatial datasets."@en ;
  dcterms:type <http://inspire.ec.europa.eu/metadata-codelist/ResourceType/service> ;
  dcterms:type <http://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceType/discovery> ;
  dcat:contactPoint ex:EEA ;
  dcat:endpointDescription <https://sdi.eea.europa.eu/catalogue/srv/eng/csw?service=CSW&request=GetCapabilities> ;
  dcat:endpointURL <http://sdi.eea.europa.eu/catalogue/srv/eng/csw> ;
.

Example 61 shows a dataset hosted by Geoscience Australia, which is available from three distinct services, as indicated by the value of the dcat:servesDataset property of each of the service descriptions.
          These are classified as a dcat:DataService and also have the dcterms:type set to " download " and " view " from the INSPIRE classification of spatial data service types [ INSPIRE-SDST ].

Example 61 is available from the DXWG DCAT 3 code repository at ga-courts.ttl

ga-courts:jc
  rdf:type dcat:Dataset ;
  dcterms:description "The dataset contains spatial locations, in point format, of the Australian High Court, Australian Federal Courts and the Australian Magistrates Courts."@en ;
  dcterms:spatial [
    rdf:type dcterms:Location ;
      dcat:bbox """<http://www.opengis.net/def/crs/EPSG/0/4283> POLYGON((
      -42.885989 115.864566 , -12.460578 115.864566 ,
      -12.460578 153.276835 , -42.885989 153.276835 ,
      -42.885989 115.864566 
    ))"""^^geosparql:wktLiteral ;
  ] ;
  dcterms:title "Judicial Courts"@en ;
  dcterms:type <http://purl.org/dc/dcmitype/Dataset> ;
  dcat:landingPage <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/cc365600-294a-597d-e044-00144fdd4fa6> ;
.

ga-courts:jc-esri
  rdf:type dcat:DataService ;
  dcterms:conformsTo <https://developers.arcgis.com/rest/> ;
  dcterms:description "This web service provides access to the National Judicial Courts dataset and presents the spatial locations of all the known Australian High Courts, Australian Federal Courts and the Australian Federal Circuit Courts located within Australia, all complemented with feature attribution."@en ;
  dcterms:identifier "2b8540c8-4a43-144d-e053-12a3070a3ff7" ;
  dcterms:title "National Judicial Courts MapServer"@en ;
  dcterms:type <http://purl.org/dc/dcmitype/Service> ;
  dcterms:type <https://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceType/download> ;
  dcterms:type <https://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceType/view> ;
  dcat:endpointURL <http://services.ga.gov.au/gis/rest/services/Judicial_Courts/MapServer> ;
  dcat:landingPage <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/2b8540c8-4a43-144d-e053-12a3070a3ff7> ;
  dcat:servesDataset ga-courts:jc ;
.

ga-courts:jc-wfs
  rdf:type dcat:DataService ;
  dcterms:conformsTo <http://www.opengis.net/def/serviceType/ogc/wfs/2.0.0> ;
  dcterms:conformsTo <http://www.opengis.net/def/serviceType/ogc/wfs/1.1.0> ;
  dcterms:conformsTo <http://www.opengis.net/def/serviceType/ogc/wfs/1.0.0> ;
  dcterms:description "This web service provides access to the National Judicial Courts dataset and presents the spatial locations of all the known Australian High Courts, Australian Federal Courts and the Australian Federal Circuit Courts located within Australia, all complemented with feature attribution."@en ;
  dcterms:identifier "2b8540c8-4a42-144d-e053-12a3070a3ff7" ;
  dcterms:title "National Judicial Courts WFS"@en ;
  dcterms:type <http://purl.org/dc/dcmitype/Service> ;
  dcterms:type <https://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceType/download> ;
  dcat:endpointDescription <http://services.ga.gov.au/gis/services/Judicial_Courts/MapServer/WFSServer?request=GetCapabilities&service=WFS> ;
  dcat:endpointURL <http://services.ga.gov.au/gis/services/Judicial_Courts/MapServer/WFSServer> ;
  dcat:landingPage <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/2b8540c8-4a42-144d-e053-12a3070a3ff7> ;
  dcat:servesDataset ga-courts:jc ;
.

ga-courts:jc-wms
  rdf:type dcat:DataService ;
  dcterms:conformsTo <http://www.opengis.net/def/serviceType/ogc/wms/1.3> ;
  dcterms:description "This web service provides access to the National Judicial Courts dataset and presents the spatial locations of all the known Australian High Courts, Australian Federal Courts and the Australian Federal Circuit Courts located within Australia, all complemented with feature attribution."@en ;
  dcterms:identifier "2b8540c8-4a41-144d-e053-12a3070a3ff7" ;
  dcterms:title "National Judicial Courts WMS"@en ;
  dcterms:type <http://purl.org/dc/dcmitype/Service> ;
  dcterms:type <https://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceType/view> ;
  dcat:endpointDescription <http://services.ga.gov.au/gis/services/Judicial_Courts/MapServer/WMSServer?request=GetCapabilities&service=WMS> ;
  dcat:endpointURL <http://services.ga.gov.au/gis/services/Judicial_Courts/MapServer/WMSServer> ;
  dcat:landingPage <https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/2b8540c8-4a41-144d-e053-12a3070a3ff7> ;
  dcat:servesDataset ga-courts:jc ;
.


### C.5 Compressed and packaged distributions

The first example is for a distribution with a downloadable file that is compressed into a GZIP file.

@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .

<https://data.gov.cz/zdroj/datová-sada/247025684/22> a dcat:Distribution ;
  dcat:downloadURL <https://mvcr1.opendata.cz/czechpoint/2007.csv.gz> ;
  dcterms:license <https://data.gov.cz/podmínky-užití/volný-přístup/> ;
  dcterms:conformsTo <https://mvcr1.opendata.cz/czechpoint/2007.json> ;
  dcterms:format <http://publications.europa.eu/resource/authority/file-type/CSV> ;
  dcat:mediaType <http://www.iana.org/assignments/media-types/text/csv> ;
  dcat:compressFormat <http://www.iana.org/assignments/media-types/application/gzip>
.

The second example is for a distribution with several files packed into a TAR file.

@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .

<https://data.gov.cz/zdroj/datová-sada/247025684/22> a dcat:Distribution ;
  dcat:downloadURL <https://mvcr1.opendata.cz/czechpoint/data.tar> ;
  dcterms:license <https://data.gov.cz/podmínky-užití/volný-přístup/> ;
  dcterms:conformsTo <https://mvcr1.opendata.cz/czechpoint/2007.json> ;
  dcterms:format <http://publications.europa.eu/resource/authority/file-type/CSV> ;
  dcat:mediaType <http://www.iana.org/assignments/media-types/text/csv> ;
  dcat:packageFormat <http://publications.europa.eu/resource/authority/file-type/TAR>
.

The third example is for a distribution with several files packed into a TAR file which has been compressed into a GZIP file.

@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .

<https://data.gov.cz/zdroj/datová-sada/247025684/22> a dcat:Distribution ;
  dcat:downloadURL <https://mvcr1.opendata.cz/czechpoint/data.tar.gz> ;
  dcterms:conformsTo <https://mvcr1.opendata.cz/czechpoint/2007.json> ;
  dcterms:license <https://data.gov.cz/podmínky-užití/volný-přístup/> ;
  dcterms:format <http://publications.europa.eu/resource/authority/file-type/CSV> ;
  dcat:mediaType <http://www.iana.org/assignments/media-types/text/csv> ;
  dcat:packageFormat <http://publications.europa.eu/resource/authority/file-type/TAR> ;
  dcat:compressFormat <http://www.iana.org/assignments/media-types/application/gzip>
  .

These examples are available from the DXWG DCAT 3 code repository at compress-and-package.ttl


## D. Change history

A full change-log is available on GitHub


## E. Changes since the Candidate Recommendation Snapshot 18 January 2024

The document has undergone the following changes since the Candidate Recommendation Snapshot 18 January 2024 [ VOCAB-DCAT-3-20240118 ]:

Editorial fixes as suggested in Issues #1581 , #1583 , #1591 .

Editorial fixes as suggested in Issues #1581 , #1583 , #1591 .

Fixed the wrong link to SPDX 2.2 - see Issue #1592 .

Fixed the wrong link to SPDX 2.2 - see Issue #1592 .

Removed the references at risk features in status section, as implementations for those features have been collected in the implementation report.

Removed the references at risk features in status section, as implementations for those features have been collected in the implementation report.


## F. Changes since the fourth public working draft of 10 May 2022

The document has undergone the following changes since the DCAT 3 fourth public working draft of 10 May 2022 [ VOCAB-DCAT-3-20220510 ]:

The recommended range of properties 6.6.5 Property: spatial resolution and 6.8.13 Property: spatial resolution has been extended to include xsd:double in addition to xsd:decimal - see Issue #1536 .

The recommended range of properties 6.6.5 Property: spatial resolution and 6.8.13 Property: spatial resolution has been extended to include xsd:double in addition to xsd:decimal - see Issue #1536 .

Updated section 17. Security and Privacy Considerations to include suggestions about integrity and authenticity  - see Issue #1526 .

Updated section 17. Security and Privacy Considerations to include suggestions about integrity and authenticity  - see Issue #1526 .

Updated usage note in 6.4.9 Property: language to provide guidance on the use of dcterms:language in multilingual distributions - see Issue #1532 .

Updated usage note in 6.4.9 Property: language to provide guidance on the use of dcterms:language in multilingual distributions - see Issue #1532 .

Added health warning related to BCP 47 - see Issue #959 .

Added health warning related to BCP 47 - see Issue #959 .

Updated Example 36 ( 11.4 Complementary approaches to versioning ) to illustrate how to use OWL and DCAT to version DCAT 3.

Updated Example 36 ( 11.4 Complementary approaches to versioning ) to illustrate how to use OWL and DCAT to version DCAT 3.

Editorial and bug fixes throughout the document.

Editorial and bug fixes throughout the document.


## G. Changes since the third public working draft of 11 January 2022

The document has undergone the following changes since the DCAT 3 third public working draft of 11 January 2022 [ VOCAB-DCAT-3-20220111 ]:

Editorial fix to the inconsistent use of "item" and "resource" throughout the document, by replacing "item" with "resource" when referring to an instance of dcat:Resource - see Issue #1490 . This revision has affected the definitions and/or the usage notes of the following terms in section 6.4 Class: Cataloged Resource : 6.4.5 Property: description , 6.4.6 Property: title , 6.4.7 Property: release date , 6.4.8 Property: update/modification date , 6.4.9 Property: language , 6.4.10 Property: publisher , 6.4.11 Property: identifier , 6.4.14 Property: relation .

Editorial fix to the inconsistent use of "item" and "resource" throughout the document, by replacing "item" with "resource" when referring to an instance of dcat:Resource - see Issue #1490 . This revision has affected the definitions and/or the usage notes of the following terms in section 6.4 Class: Cataloged Resource : 6.4.5 Property: description , 6.4.6 Property: title , 6.4.7 Property: release date , 6.4.8 Property: update/modification date , 6.4.9 Property: language , 6.4.10 Property: publisher , 6.4.11 Property: identifier , 6.4.14 Property: relation .

Added Example 45 ( 14.2.1 Conformance to a standard ) and introductory paragraph to show how to use property dcterms:conformsTo with a dcat:CatalogRecord - see Issue #1489 .

Added Example 45 ( 14.2.1 Conformance to a standard ) and introductory paragraph to show how to use property dcterms:conformsTo with a dcat:CatalogRecord - see Issue #1489 .

Added property dcat:inCatalog as the inverse of dcat:resource in section 7. Use of inverse properties - see Issue #1484 .

Added property dcat:inCatalog as the inverse of dcat:resource in section 7. Use of inverse properties - see Issue #1484 .

Updated class diagram in Figure 1 to align it with the current version of the specification. In particular: Added newly defined properties - see Issue #1469 . Removed inverse properties listed in section 7. Use of inverse properties - see Issues #1410 and #1413 . Removed cardinality restrictions not present in the RDF definition - see resolution #3 of 8 March 2022 .

Updated class diagram in Figure 1 to align it with the current version of the specification. In particular:

Added newly defined properties - see Issue #1469 .

Removed inverse properties listed in section 7. Use of inverse properties - see Issues #1410 and #1413 .

Removed cardinality restrictions not present in the RDF definition - see resolution #3 of 8 March 2022 .

Added property dcat:seriesMember as the inverse of dcat:inSeries in section 7. Use of inverse properties - see Issue #1335 .

Added property dcat:seriesMember as the inverse of dcat:inSeries in section 7. Use of inverse properties - see Issue #1335 .

Added Example 39 ( 12.1 How to specify dataset series ) and introductory paragraph to show how to combine dataset series and dataset versions - see Issue #1409 .

Added Example 39 ( 12.1 How to specify dataset series ) and introductory paragraph to show how to combine dataset series and dataset versions - see Issue #1409 .

Defined a new property dcat:resource to link a dcat:Catalog to a dcat:Resource , thus replacing property dcterms:hasPart that in DCAT 2 was introduced for this purpose. As a consequence, properties dcat:dataset , dcat:service , and dcat:catalog have been revised to be sub-properties of dcat:resource - see Issue #1469 .

Defined a new property dcat:resource to link a dcat:Catalog to a dcat:Resource , thus replacing property dcterms:hasPart that in DCAT 2 was introduced for this purpose. As a consequence, properties dcat:dataset , dcat:service , and dcat:catalog have been revised to be sub-properties of dcat:resource - see Issue #1469 .

Added property dcterms:hasPart under dcat:Resource - see Issue #1469 .

Added property dcterms:hasPart under dcat:Resource - see Issue #1469 .

Fixed inconsistent URIs in Example 15 ( 8. Dereferenceable identifiers ) - see Issue #1459 .

Fixed inconsistent URIs in Example 15 ( 8. Dereferenceable identifiers ) - see Issue #1459 .

Aligned the definitions of the properties dcat:dataset , dcat:service , dcat:catalog - see Issue #1465 .

Aligned the definitions of the properties dcat:dataset , dcat:service , dcat:catalog - see Issue #1465 .

The definition of property dcat:version has been revised to make it explicit that version indicators can be numeric or textual - see Issue #1442 .

The definition of property dcat:version has been revised to make it explicit that version indicators can be numeric or textual - see Issue #1442 .

Revised Example 62 , Example 63 , and Example 64 ( C.5 Compressed and packaged distributions ) to remove all occurrences of property dcat:accessURL when taking as value the same URL of dcat:downloadURL - see Issue #1437 .

Revised Example 62 , Example 63 , and Example 64 ( C.5 Compressed and packaged distributions ) to remove all occurrences of property dcat:accessURL when taking as value the same URL of dcat:downloadURL - see Issue #1437 .

Revised usage note of property dcat:packageFormat to include the ZIP format as one of the examples of packaging formats - see Issue #1438 .

Revised usage note of property dcat:packageFormat to include the ZIP format as one of the examples of packaging formats - see Issue #1438 .

Editorial fixes to 5.1 DCAT scope - see Issue #1440 .

Editorial fixes to 5.1 DCAT scope - see Issue #1440 .


## H. Changes since the second public working draft of 4 May 2021

The document has undergone the following changes since the DCAT 3 second public working draft of 4 May 2021 [ VOCAB-DCAT-3-20210504 ]:

New section 7. Use of inverse properties has been added, and properties dcat:isVersionOf , dcat:next , and dcterms:isReplacedBy have been removed from 6. Vocabulary specification - see Issue #1336 .

New section 7. Use of inverse properties has been added, and properties dcat:isVersionOf , dcat:next , and dcterms:isReplacedBy have been removed from 6. Vocabulary specification - see Issue #1336 .

New section 18. Accessibility Considerations has been added - see Issue #1358 .

New section 18. Accessibility Considerations has been added - see Issue #1358 .

Revision of UML diagrams - see Issues #1383 , #1294 , #1252 .

Revision of UML diagrams - see Issues #1383 , #1294 , #1252 .

Revision of the usage note of dcat:Resource - see Issue #1388 .

Revision of the usage note of dcat:Resource - see Issue #1388 .

Clarified the scope of dcterms:identifier - see Issue #771 .

Clarified the scope of dcterms:identifier - see Issue #771 .

5.3 Basic example has been updated to tell a more coherent story (see Issue #1155 ) and express temporal coverage by using dcterms:PeriodOfTime , dcat:startDate , and dcat:endDate .

5.3 Basic example has been updated to tell a more coherent story (see Issue #1155 ) and express temporal coverage by using dcterms:PeriodOfTime , dcat:startDate , and dcat:endDate .

The usage notes of properties dcat:bbox and dcat:centroid have been revised to make it clearer that they are supposed to be used only with geometry literals - see Issue #1359 .

The property dcat:theme have been explicitly defined as an OWL object property and its range is dropped; consistency of the usage note of dcat:themeTaxonomy has been improved -   see Issues #1364 and #1153 .


## I. Changes since the first public working draft of 17 December 2020

The document has undergone the following changes since the DCAT 3 first public working draft of 17 December 2020 [ VOCAB-DCAT-3-20201217 ]:

5.3 Basic example has been extended to include titles, labels, and keywords in two different languages (English and Spanish) to illustrate the use of language tags.

5.3 Basic example has been extended to include titles, labels, and keywords in two different languages (English and Spanish) to illustrate the use of language tags.

The recommended range of property 6.8.12 Property: byte size has been changed from xsd:decimal to xsd:nonNegativeInteger

The recommended range of property 6.8.12 Property: byte size has been changed from xsd:decimal to xsd:nonNegativeInteger

11. Versioning has been revised to focus specifically on versions derived from the revision of a resource, and by following the [ PAV ] approach for the specification of version chains and hierarchies - previous, next, current, last version. In particular: The introductory text has been revised according to the new scope. The section on version types (link to previous version) has been removed, and a new section has been added to describe how to specify relationships between versions. Dropped support to the specification of backward (in)compatibility between versions by using properties owl:backwardCompatibleWith and owl:incompatibleWith , originally included in 11.2 Version information . A new section has been added at the end to compare the DCAT versioning approach with those used in OWL, [ DCTERMS ], and [ PROV-O ]. The other sections include only editorial changes.

11. Versioning has been revised to focus specifically on versions derived from the revision of a resource, and by following the [ PAV ] approach for the specification of version chains and hierarchies - previous, next, current, last version. In particular:

The introductory text has been revised according to the new scope.

The section on version types (link to previous version) has been removed, and a new section has been added to describe how to specify relationships between versions.

Dropped support to the specification of backward (in)compatibility between versions by using properties owl:backwardCompatibleWith and owl:incompatibleWith , originally included in 11.2 Version information .

A new section has been added at the end to compare the DCAT versioning approach with those used in OWL, [ DCTERMS ], and [ PROV-O ].

The other sections include only editorial changes.

6.4 Class: Cataloged Resource has been updated to include the definition of the properties illustrated in 11. Versioning .

12. Dataset series has been revised making dataset series first class citizens of data catalogs and introducing new properties for linking dataset series and datasets. In particular: A new class dcat:DatasetSeries has been defined (see 6.7 Class: Dataset Series ) - see Issue #1272 . Property dcat:inSeries has been added to 6.6 Class: Dataset - see Issue #1307 . Properties dcat:first , dcat:prev , dcat:next , and dcat:last have been added to 6.4 Class: Cataloged Resource - see Issue #1308 .

12. Dataset series has been revised making dataset series first class citizens of data catalogs and introducing new properties for linking dataset series and datasets. In particular:

A new class dcat:DatasetSeries has been defined (see 6.7 Class: Dataset Series ) - see Issue #1272 .

Property dcat:inSeries has been added to 6.6 Class: Dataset - see Issue #1307 .

Properties dcat:first , dcat:prev , dcat:next , and dcat:last have been added to 6.4 Class: Cataloged Resource - see Issue #1308 .

Added property spdx:checksum to 6.8 Class: Distribution ; added class spdx:Checksum (see 6.17 Class: Checksum ), and its properties spdx:algorithm and spdx:checksumValue - see Issue #1287 .

Revised range of property locn:geometry , to align it with its definition in [ LOCN ]. The usage note of this property has been also revised to make it clear that it can be used with either geometry literals or classes - see Issue #1293 .

Added examples to 9. License and rights statements - see Issues #676 and #1333 .

Replaced [ DCTERMS ] namespace prefix dct: with dcterms: throughout the document - see Issue #1314 .

Fixed inconsistent use of "URI" and " IRI " throughout the document - see Issue #1341 .

Removed NOTE in Example 31 showing an example of the use of [ W3C-BASIC-GEO ] for the specification of point geometries - see Issue #1347 .

Revised textual descriptions of classes and properties to clarify that the resources in a catalog are not limited to datasets and data services - see Issue #1349 .

Fixed inconsistent use of property labels - see Issue #1350 .

Updated definition for dcat:catalog - see Issue #1156 .


## J. Changes since the W3C Recommendation of 4 February 2020

The document has undergone the following changes since the DCAT 2 W3C Recommendation of 4 February 2020 [ VOCAB-DCAT-2-20200204 ]:

Examples about loosely structured catalog were updated replacing dcterms:relation with more specific subrelations and emphasizing the use of dcterms:hasPart .

Section 11. Versioning was extended with draft guidelines to deal with version delta (Issue #89 ), version release date (Issue #91 ),  version identifier (Issue #92 ),  version compatibility (Issue #1258 ) and resource status (Issue #1238 ).

A new section 12. Dataset series was added to draft guidelines on dataset series (Issue #868 ) and to show related examples (Issue #806 ).


## K. References


### K.1 Normative references


### K.2 Informative references

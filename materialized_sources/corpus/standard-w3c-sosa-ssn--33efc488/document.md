# Semantic Sensor Network Ontology


## W3C Recommendation 19 October 2017 (Link errors corrected 08 December 2017)

Please check the errata for any errors or issues reported since publication.

See also translations .

Copyright © 2017 OGC & W3C ® ( MIT , ERCIM , Keio , Beihang ), W3C liability , trademark and document use rules apply.


## Abstract

The Semantic Sensor Network (SSN) ontology is an ontology for describing sensors and their observations, the involved procedures, the studied features of interest, the samples used to do so, and the observed properties, as well as actuators. SSN
            follows a horizontal and vertical modularization architecture by including a lightweight but self-contained core ontology called SOSA (Sensor, Observation, Sample, and Actuator) for its elementary classes and properties. With their different
            scope and different degrees of axiomatization, SSN and SOSA are able to support a wide range of applications and use cases, including satellite imagery, large-scale scientific monitoring, industrial and household infrastructures, social sensing,
            citizen science, observation-driven ontology engineering, and the Web of Things. Both ontologies are described below, and examples of their usage are given.

The namespace for SSN terms is http://www.w3.org/ns/ssn/ . The namespace for SOSA terms is http://www.w3.org/ns/sosa/ .

The suggested prefix for the SSN namespace is ssn . The suggested prefix for the SOSA namespace is sosa .

The SSN ontology is available at http://www.w3.org/ns/ssn/ . The SOSA ontology is available at http://www.w3.org/ns/sosa/ .


## Status of This Document

Status update (December 2017): The following links were targeting wrong resources and have been fixed in-place: the link to the ontology graph in section 5.1 , the link to the DUL namespace in section 6.1.1 , the link to the SOSA to PROV alignment in section 6.5.1 , and the link to the graph corresponding to the example in appendix B.11 . Additional editorial errors noted in the errata document.

This section describes the status of this document at the time of its publication. Other documents may supersede this document. A list of current W3C publications and the latest revision of this technical report can be found in the W3C technical reports index at https://www.w3.org/TR/.

For OGC - this document was prepared by the Spatial Data on the Web Working Group ( SDWWG ) — a joint W3C -OGC
            project (see charter ). The document is prepared following W3C conventions. At the time of publication, this document was in the approval process for the OGC Full standards track and thus its status in the OGC will be indicated in Discussion Papers or OGC Standards on the OGC website. Recipients of this document are invited to submit, with their comments, notification of any relevant patent rights of which they are aware and to provide supporting documentation.

This document was published by the Spatial Data on the Web Working Group as a Recommendation. Comments regarding this document are welcome. Please send them to the GitHub repository . An archive of the mailing list is also available.

Please see the Working Group's implementation
            report .

This document has been reviewed by W3C Members, by software developers, and by other W3C groups and interested parties, and is endorsed by the Director
            as a W3C Recommendation. It is a stable document and may be used as reference material or cited from another document. W3C 's role in making the Recommendation
            is to draw attention to the specification and to promote its widespread deployment. This enhances the functionality and interoperability of the Web.

This document was produced by a group operating under the W3C Patent
            Policy . W3C maintains a public list of any patent
              disclosures made in connection with the deliverables of the group; that page also includes instructions for disclosing a patent. An individual who has actual knowledge of a patent which the individual believes contains Essential
            Claim(s) must disclose the information in accordance with section
            6 of the W3C Patent Policy .

This document is governed by the 1 March 2017 W3C Process Document .


## 1. Introduction

This section is non-normative.

Sensors are a major source of data available on the Web today. While sensor data may be published as mere values, searching, reusing, integrating, and interpreting these data requires more than just the observation results. Of equal importance
            for the proper interpretation of these values is information about the studied feature of interest, such as a river, the observed property, such as flow velocity, the utilized sampling strategy, such as the specific locations and times at
            which the velocity was measured, and a variety of other information. OGC's Sensor Web Enablement standards [ OandM ], [ SensorML ] provide a means to annotate sensors and their observations. However, these standards are not integrated and aligned
            with W3C Semantic Web technologies and Linked Data in particular, which are key drivers for creating and maintaining a global and densely interconnected graph of data. With the rise of the Web
            of Things and smart cities and homes more generally, actuators and the data they produce also become first-class citizens of the Web. Given their close relation to sensors, observations, procedures, and features of interest, it is desirable
            to provide a common ontology that also includes actuators and actuation. Finally, with the increasing diversity of data and data providers, definitions such as those for sensors need to be broadened, e.g., to include social sensing. The following
            specifications introduce the new Semantic Sensor Network (SSN) and Sensor, Observation, Sample, and Actuator (SOSA) ontologies that are set out to provide flexible but coherent perspectives for representing the entities, relations, and activities
            involved in sensing, sampling, and actuation. SOSA provides a lightweight core for SSN and aims at broadening the target audience and application areas that can make use of Semantic Web ontologies. At the same time, SOSA acts as minimal interoperability
            fall-back level, i.e., it defines those common classes and properties for which data can be safely exchanged across all uses of SSN, its modules, and SOSA.


## 2. Modularization

This section is non-normative.

Practitioners using the original Semantic Sensor Network Ontology as defined in the W3C Semantic Sensor Network Incubator Group [ SSNO ]
            have identified a major issue in its complexity, partly due to the layering underneath the Dolce-UltraLite (DUL) upper level ontology. In response to this, the new Semantic Sensor Network (SSN) ontology offers several ontology subsets that
            are distinguished mainly through their ontological commitments. This section explains the rationale and method for modularizing SSN, i.e., offering several distinct ontologies that are similar in their domain of discourse, but with different
            ontological commitments, suitable to several use cases and target audiences. For example, SOSA is intended to provide Schema.org-style semantic enrichment capabilities for data repositories managed by an audience broader than typical ontology
            engineers, while still ensuring interoperability with SSN-based repositories.

Ontology modularization is a common method used in ontology engineering to segment an ontology into smaller parts. In general, ontology modularization aims at providing users of ontologies with the knowledge they require, reducing the scope as
            much as possible to what is strictly necessary in a given use case. Two main categories of ontology modularization can be distinguished.

The first category comprises those approaches that focus on the composition of existing ontologies by means of integrating and mapping ontologies, most commonly through owl:import statements. OWL import has a direction from a dependent
            ontology to a dependency ontology. Although import is transitive, knowledge is propagated in only one direction. The importing ontology assumes all the meaning of the imported terms used, by including all axioms relevant to the meaning of
            these terms. However, the imported ontology does not capture any of the semantics of the importing ontology.

The second category comprises of mapping approaches that aim to partition and extract parts of ontologies as modules. These mapping approaches are not necessarily directional, but most approaches of ontology extraction rely on the directionality
            of the imported modules. The main feature of an ontology module under the second category is that it is self-contained, i.e., the module captures the meaning of the imported terms used by including all axioms relevant to the meaning of these
            terms. This means, that the result of certain reasoning tasks such as subsumption or query answering within a single module should be possible and result in the same answers without the need to access other modules of the ontology.

Our modularization uses the first approach by composing the ontology into several modules that use owl:import statements, whereby we distinguish two methods depending on the directionality of the segmentation: a vertical segmentation
            and a horizontal segmentation.


## Vertical Segmentation

Vertical modules build upon each other, i.e., they directionally owl:import lower level modules. Lower level modules are independent of their higher level modules and logically consistent on their own.

For example, the Dolce-UltraLite Alignment Module imports the SSN
          Ontology which itself imports the SOSA Ontology . However, in reverse, neither SOSA nor SSN import the Dolce-UltraLite
          Alignment Module . In fact, SOSA as the core, does not import any other ontologies, which makes it truly independent of vertical modules that add more expressivity and further ontological commitments to the lightweight semantics of SOSA .

Note that higher level here is not to be confused with upper level ontologies. Upper level ontologies are general knowledge ontologies that can be directionally imported in many domains, whereas our definition of higher level ontologies here refers
            to an ontology that extends one or several ontology modules to capture a larger part of a knowledge domain and/or combine knowledge domains.


## Horizontal Segmentation

Modules that are horizontally layered may depend on each other, i.e., they may rely on the directional import of another horizontal module. Only one horizontal module that is dependent on the SSN ontology is presented in this specification, the Sample Relations Module . Other ontologies that add domain-specific terms to SSN, but require the import of SSN, can be considered horizontal modules.


## 3. Origins of SSN and SOSA

This section is non-normative.

Here we briefly review the origins of SSN and SOSA, namely the initial SSN version published by the W3C Semantic Sensor Network Incubator
          Group [ SSNO ] and work on Sensor Web Enablement by the OGC. We also highlight the most substantial changes made since the initial release of the SSN ontology.

Starting in 2002, the OGC's Sensor Web Enablement initiative has developed a generic framework for delivering sensor data, dealing with remote-sensing, moving platforms, and in-situ monitoring and sensing. The Sensor Observation Service defines
            a standard query interface for sensor and observation data, following the pattern established by OGC for their Web Services. The returned XML data conforms with the Sensor Model Language [ SensorML ]
            and OMXML [ OMXML ], whereby the latter implements Observations and Measurements [ OandM ].

SensorML and O&M are complementary viewpoints. SensorML is 'provider-centric' and encodes details of the sensor along with raw observation data. SensorML is self-contained and highly flexible. This makes life easy for data producers but is
            demanding on consumers. SensorML provides extensive support for serialization of numeric data arrays and is particularly optimized for data that includes multiple parallel streams that must be processed together. For example, the data collected
            by cameras on airborne vehicles must be geo-referenced based on the instantaneous position of the platform and orientation of the camera. In contrast, O&M was designed to be more 'user-centric' with the target of the observation and the
            observed property as first-class objects. O&M works at a higher semantic level than SensorML, but only provides abstract classes for sensors, features of interest and observable properties, expecting the details to be provided by specific
            applications and domains. O&M also provided a model for sampling, since almost all scientific observations are made on a subset of, or proxy for, the ultimate feature of interest.

The initial W3C Semantic Sensor Network Incubator Group ontology (SSN) was built around an ontology design pattern called the Stimulus
            Sensor Observation (SSO) pattern [ SSO-Pattern ]. The SSO was developed as a minimal and common ground for heavy-weight ontologies for the use on the Semantic Sensor Web as well
            as to explicitly address the need for light-weight semantics requested by the Linked Data community. The SSO was also aligned to the Dolce-Ultralite upper ontology (DUL).

The new SSN described in this document is based on a revised and expanded version of this pattern, namely the Sensor, Observation,
            Sample, and Actuator (SOSA) ontology. Similar to the original SSO, SOSA acts as a central building block for the SSN but puts more emphasis on light-weight use and the ability to be used standalone. The axiomatization also changed to
            provide an experience more related to Schema.org. Notable differences include the usage of the Schema.org domainIncludes and rangeIncludes annotation properties that provide an informal semantics compared to the inferential semantics of their OWL 2 counterparts. In line with the changes implemented for the new SSN, SOSA
            also drops the direct DUL alignment although an optional alignment can be achieved via the SSN-DUL alignment provided in Section 6.1 . SOSA is also more explicit than SSO in its support for virtual and human sensor.
            Finally, and most notably, SOSA extends SSO's original scope beyond sensors and their observations by including classes and properties for actuators and sampling. SOSA also distinguishes between phenomenonTime and resultTime .

Drawing on considerable implementation and application experience with SSN and sensor and observation ontologies more broadly, the new SSN and SOSA ontologies presented here are set out to address changes in scope and audience, shortcomings of
            the initial work, as well as new technical developments. The list below highlights the most important (but by far not exclusive) updates.

Addressing changes in scope and audience The initial SSN was developed with ontology engineers in mind as the primary audience. Due to the widespread adoption of SSN, the increasing role of citizen science, the strong focus on lightweight vocabularies by the Linked Data community,
                        and vocabularies such as Schema.org, the ontology was streamlined. SOSA is added as a core, and is also useful as a standalone ontology targeting Web developers, citizen science, lightweight Linked Data publishing, resource-constraint
                        IoT devices, data intensive applications (with the possibility of using lightweight reasoning), and so on. The new SSN introduces additional classes and relations on top of SOSA to model the capabilities of sensors and actuators,
                        the compositionality of systems, and so forth to suit more complex needs or cases in which more provenance data is required, e.g., to improve reproducibility. Almost all scientific observations make heavy use of sampling strategies, and, therefore, the Sampling, Sampler, and Sample classes, as well as their corresponding properties, have been added to SOSA and SSN. Due to the increasing importance of the Web of Things and smart instrumentation and environments more generally, the classes Actuator and Actuation have been added to SOSA and SSN.

The initial SSN was developed with ontology engineers in mind as the primary audience. Due to the widespread adoption of SSN, the increasing role of citizen science, the strong focus on lightweight vocabularies by the Linked Data community,
                        and vocabularies such as Schema.org, the ontology was streamlined. SOSA is added as a core, and is also useful as a standalone ontology targeting Web developers, citizen science, lightweight Linked Data publishing, resource-constraint
                        IoT devices, data intensive applications (with the possibility of using lightweight reasoning), and so on. The new SSN introduces additional classes and relations on top of SOSA to model the capabilities of sensors and actuators,
                        the compositionality of systems, and so forth to suit more complex needs or cases in which more provenance data is required, e.g., to improve reproducibility.

Almost all scientific observations make heavy use of sampling strategies, and, therefore, the Sampling, Sampler, and Sample classes, as well as their corresponding properties, have been added to SOSA and SSN.

Due to the increasing importance of the Web of Things and smart instrumentation and environments more generally, the classes Actuator and Actuation have been added to SOSA and SSN.

Addressing shortcomings of the initial SSN The new SSN streamlines the relations (and need for) the old Device, Platform, and Systems classes. The old SSN was perceived as too heavyweight (on its axiomatization) and too dependent on OWL reasoning by some users. To strike a balance, DL expressivity of the new lightweight SOSA ontology is ALI(D) which is efficiently supported
                        by modern triple stores, while the new SSN is ALRIN(D). In contrast, the old SSN is SRIQ. The SSN previously imported DUL and many SSN terms inherited from DUL terms. Due to frequent user requests, this has been redesigned so that SSN (and SOSA) can be used entirely independently of DUL if desired. Some of the alignments
                        with DUL have been reconsidered. Those parts of SSN that use DUL terms have been separated into the SSN Alignment with DUL ontology. This alignment and therefore the role of DUL in SSN
                        have been declared non-normative. The definitions for many classes and properties have changed slightly to improve explanation or to correct minor errors. Examples have been separated from the main definitions. The initial SSN has been criticized for its partially inconsistent handling of virtual sensors (including software and simulations) and related classes and properties. The new SSN and SOSA address this issue by allowing all major classes
                        to be virtual, and to better support humans and other animals as agents. The notion of Procedure (formerly Plan) has been clarified to describe a workflow, protocol, plan, algorithm, or computational method specifying how to make an Observation, create a Sample, or make a change to the state of the world
                        via an Actuator. The Observation class in the initial SSN was conceptualized as a subclass of the DUL Situation class. To improve alignment with O&M and user expectations, as well as to follow a consistent modeling strategy for observations, sampling,
                        and actuation, the Observation class defined in SOSA and the new SSN are now conceptualized as activities.

The new SSN streamlines the relations (and need for) the old Device, Platform, and Systems classes.

The old SSN was perceived as too heavyweight (on its axiomatization) and too dependent on OWL reasoning by some users. To strike a balance, DL expressivity of the new lightweight SOSA ontology is ALI(D) which is efficiently supported
                        by modern triple stores, while the new SSN is ALRIN(D). In contrast, the old SSN is SRIQ.

The SSN previously imported DUL and many SSN terms inherited from DUL terms. Due to frequent user requests, this has been redesigned so that SSN (and SOSA) can be used entirely independently of DUL if desired. Some of the alignments
                        with DUL have been reconsidered. Those parts of SSN that use DUL terms have been separated into the SSN Alignment with DUL ontology. This alignment and therefore the role of DUL in SSN
                        have been declared non-normative.

The definitions for many classes and properties have changed slightly to improve explanation or to correct minor errors. Examples have been separated from the main definitions.

The initial SSN has been criticized for its partially inconsistent handling of virtual sensors (including software and simulations) and related classes and properties. The new SSN and SOSA address this issue by allowing all major classes
                        to be virtual, and to better support humans and other animals as agents.

The notion of Procedure (formerly Plan) has been clarified to describe a workflow, protocol, plan, algorithm, or computational method specifying how to make an Observation, create a Sample, or make a change to the state of the world
                        via an Actuator.

The Observation class in the initial SSN was conceptualized as a subclass of the DUL Situation class. To improve alignment with O&M and user expectations, as well as to follow a consistent modeling strategy for observations, sampling,
                        and actuation, the Observation class defined in SOSA and the new SSN are now conceptualized as activities.

Addressing technical developments The initial SSN used local/guarded domain and range restrictions. The lightweight SOSA ontology uses an even more restrained axiomatization to foster wide reuse and adaptation among an audience that is not necessarily familiar with
                        OWL. SOSA makes use of the domainIncludes and rangeIncludes annotation properties defined in Schema.org. These had not been available before. Given the increased interest in using Semantic Web technologies directly on the level of individual sensors, actuators, or platforms, SOSA's axiomatization does not use many of the more complex language elements introduced by SSN.

The initial SSN used local/guarded domain and range restrictions. The lightweight SOSA ontology uses an even more restrained axiomatization to foster wide reuse and adaptation among an audience that is not necessarily familiar with
                        OWL. SOSA makes use of the domainIncludes and rangeIncludes annotation properties defined in Schema.org. These had not been available before.

Given the increased interest in using Semantic Web technologies directly on the level of individual sensors, actuators, or platforms, SOSA's axiomatization does not use many of the more complex language elements introduced by SSN.


## 4. Axiomatization

This section introduces the specifications for SOSA and SSN.


### 4.1 Namespaces

The namespace for SSN terms is http://www.w3.org/ns/ssn/ . The namespace for SOSA terms is http://www.w3.org/ns/sosa/ .

The suggested prefix for the SSN namespace is ssn . The suggested prefix for the SOSA namespace is sosa .

The SSN ontology is available at http://www.w3.org/ns/ssn/ . The SOSA ontology is available at http://www.w3.org/ns/sosa/ .


### 4.2 Overview of Classes and Properties

This section is non-normative.

Classes: sosa:ActuatableProperty , sosa:Actuation , sosa:Actuator , ssn:Deployment , sosa:FeatureOfInterest , ssn:Input , sosa:ObservableProperty , sosa:Observation , ssn:Output , sosa:Platform , ssn:Property , sosa:Procedure , sosa:Result , sosa:Sample , sosa:Sampler , sosa:Sampling , sosa:Sensor , ssn:Stimulus , ssn:System

Object Properties: sosa:actsOnProperty , sosa:madeByActuator , ssn:deployedOnPlatform , ssn:deployedSystem , ssn:detects , ssn:forProperty , ssn:hasDeployment , sosa:hasFeatureOfInterest , ssn:hasInput , ssn:hasOutput , ssn:hasProperty , sosa:hasResult , sosa:hasSample , ssn:hasSubSystem , sosa:hosts , ssn:implementedBy , ssn:implements , ssn:inDeployment , sosa:isActedOnBy , sosa:isFeatureOfInterestOf , sosa:isHostedBy , sosa:isObservedBy , ssn:isPropertyOf , ssn:isProxyFor , sosa:isResultOf , sosa:isSampleOf , sosa:madeActuation , sosa:madeBySampler , sosa:madeBySensor , sosa:madeObservation , sosa:madeSampling , sosa:observedProperty , sosa:observes , sosa:phenomenonTime , sosa:usedProcedure , ssn:wasOriginatedBy

Datatype Properties: sosa:hasSimpleResult , sosa:resultTime

Several conceptual modules have been defined to cover key sensor, actuation and sampling concepts. The different conceptual modules of SOSA/SSN can be seen in the following figure.

An overview of the main classes and properties inside the ontology modules can be seen in the following figures, from the perspectives of Observation, Actuation and Sampling. In the figures, and in the rest of the document, SOSA-related components
                and restrictions are shown in green, while SSN-only components are shown in blue.


### 4.3 Observations


#### 4.3.1 Overview and examples

This section is non-normative.

The following figure provides an overview of the core classes and properties that are specifically related to modeling Observations. SOSA axioms are shown in green, while SSN-only axioms are shown in blue.

The following examples illustrate how the terms related to Observation can be used:

iPhone Barometer

Coal Oil Point Reserve

Apartment 134

Tree height measurement

Number of sunspots

Seismographs

Wind sensor spinning cups

IP68 Smart Sensor


#### 4.3.2 Specification

This section introduces the following classes and properties:

sosa:ObservableProperty , sosa:Observation , sosa:observedProperty , sosa:phenomenonTime , sosa:Sensor , sosa:observes , sosa:isObservedBy , sosa:madeObservation , sosa:madeBySensor , ssn:Stimulus , ssn:isProxyFor , ssn:wasOriginatedBy , ssn:detects

IRI: http://www.w3.org/ns/sosa/ObservableProperty

a OWL Class

IRI: http://www.w3.org/ns/sosa/Observation

a OWL Class

IRI: http://www.w3.org/ns/sosa/observedProperty

a OWL Object Property

IRI: http://www.w3.org/ns/sosa/phenomenonTime

a OWL Object Property

IRI: http://www.w3.org/ns/sosa/Sensor

a OWL Class

IRI: http://www.w3.org/ns/sosa/observes

a OWL Object Property

IRI: http://www.w3.org/ns/sosa/isObservedBy

a OWL Object Property

IRI: http://www.w3.org/ns/sosa/madeObservation

a OWL Object Property

IRI: http://www.w3.org/ns/sosa/madeBySensor

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/Stimulus

a OWL Class

IRI: http://www.w3.org/ns/ssn/isProxyFor

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/wasOriginatedBy

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/detects

a OWL Object Property


### 4.4 Actuations


#### 4.4.1 Overview and examples

This section is non-normative.

The following figure provides an overview of the core classes and properties that are secifically related to modeling Actuations. SOSA axioms are shown in green, while SSN-only axioms are shown in blue.

The following example illustrate how the terms related to Actuations can be used:

apartment 134


#### 4.4.2 Specification

This section introduces the following classes and properties:

sosa:ActuatableProperty , sosa:Actuation , sosa:actsOnProperty , sosa:isActedOnBy , sosa:Actuator , sosa:madeActuation , sosa:madeByActuator

IRI: http://www.w3.org/ns/sosa/ActuatableProperty

a OWL Class

IRI: http://www.w3.org/ns/sosa/Actuation

a OWL Class

IRI: http://www.w3.org/ns/sosa/actsOnProperty

a OWL Object Property

IRI: http://www.w3.org/ns/sosa/isActedOnBy

a OWL Object Property

IRI: http://www.w3.org/ns/sosa/Actuator

a OWL Class

IRI: http://www.w3.org/ns/sosa/madeActuation

a OWL Object Property

IRI: http://www.w3.org/ns/sosa/madeByActuator

a OWL Object Property


### 4.5 Samplings


#### 4.5.1 Overview and examples

This section is non-normative.

The following figure provides an overview of the core classes and properties that are secifically related to modeling Samplings. SOSA axioms are shown in green, while SSN-only axioms are shown in blue.

The following examples illustrate how the terms related to Samplings can be used:

iPhone Barometer

Coal Oil Point Reserve

Seismographs

Ice Core

DHT22 Deployment

IP68 Smart Sensor


#### 4.5.2 Specification

This section introduces the following classes and properties:

sosa:Sample , sosa:hasSample , sosa:isSampleOf , sosa:Sampling , sosa:Sampler , sosa:madeSampling , sosa:madeBySampler

IRI: http://www.w3.org/ns/sosa/Sample

a OWL Class

IRI: http://www.w3.org/ns/sosa/hasSample

a OWL Object Property

IRI: http://www.w3.org/ns/sosa/isSampleOf

a OWL Object Property

IRI: http://www.w3.org/ns/sosa/Sampling

a OWL Class

IRI: http://www.w3.org/ns/sosa/Sampler

a OWL Class

IRI: http://www.w3.org/ns/sosa/madeSampling

a OWL Object Property

IRI: http://www.w3.org/ns/sosa/madeBySampler

a OWL Object Property


### 4.6 Features of Interest and Properties


#### 4.6.1 Overview and examples

This section is non-normative.

The following figure provides an overview of the core classes and properties that are secifically related to modeling Features of Interest and Properties. SOSA axioms are shown in green, while SSN-only axioms are shown in blue.

The following examples illustrate how the terms related to Features of Interest and Properties can be used:

iPhone Barometer

Coal Oil Point Reserve

apartment 134

Tree height measurement

Seismographs

Number of sunspots

Wind sensor spinning cups

Ice Core

DHT22 Deployment

IP68 Smart Sensor


#### 4.6.2 Specification

This section introduces the following classes and properties:

sosa:FeatureOfInterest , sosa:hasFeatureOfInterest , sosa:isFeatureOfInterestOf , ssn:Property , ssn:hasProperty , ssn:isPropertyOf , ssn:forProperty

IRI: http://www.w3.org/ns/sosa/FeatureOfInterest

a OWL Class

IRI: http://www.w3.org/ns/sosa/hasFeatureOfInterest

a OWL Object Property

IRI: http://www.w3.org/ns/sosa/isFeatureOfInterestOf

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/Property

a OWL Class

IRI: http://www.w3.org/ns/ssn/hasProperty

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/isPropertyOf

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/forProperty

a OWL Object Property


### 4.7 Results


#### 4.7.1 Overview and examples

This section is non-normative.

The following figure provides an overview of the core classes and properties that are secifically related to modeling Results. SOSA axioms are shown in green, while SSN-only axioms are shown in blue.

The following examples illustrate how the terms related to Results can be used:

iPhone Barometer

Coal Oil Point Reserve

apartment 134

Tree height measurement

Seismographs

Number of sunspots

Wind sensor spinning cups

Ice Core

IP68 Smart Sensor


#### 4.7.2 Specification

This section introduces the following classes and properties:

sosa:Result , sosa:hasResult , sosa:isResultOf , sosa:hasSimpleResult , sosa:resultTime

IRI: http://www.w3.org/ns/sosa/Result

a OWL Class

IRI: http://www.w3.org/ns/sosa/hasResult

a OWL Object Property

IRI: http://www.w3.org/ns/sosa/isResultOf

a OWL Object Property

IRI: http://www.w3.org/ns/sosa/hasSimpleResult

a OWL Datatype Property

IRI: http://www.w3.org/ns/sosa/resultTime

a OWL Datatype Property


### 4.8 Procedures


#### 4.8.1 Overview and examples

This section is non-normative.

The following figure provides an overview of the core classes and properties that are secifically related to modeling Procedures. SOSA axioms are shown in green, while SSN-only axioms are shown in blue.

The following examples illustrate how the terms related to Procedures can be used:

DHT22 Description

IP68 Smart Sensor


#### 4.8.2 Specification

This section introduces the following classes and properties:

sosa:Procedure , sosa:usedProcedure , ssn:implements , ssn:implementedBy , ssn:hasInput , ssn:hasOutput , ssn:Input , ssn:Output ,

IRI: http://www.w3.org/ns/sosa/Procedure

a OWL Class

IRI: http://www.w3.org/ns/sosa/usedProcedure

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/implements

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/implementedBy

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/hasInput

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/Input

a OWL Class

IRI: http://www.w3.org/ns/ssn/hasOutput

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/Output

a OWL Class


### 4.9 Systems and their Deployment


#### 4.9.1 Overview and examples

This section is non-normative.

The following figure provides an overview of the core classes and properties that are secifically related to modeling systems and their deployment. SOSA axioms are shown in green, while SSN-only axioms are shown in blue.

The following examples illustrate how the terms related to Systems and their Deployment can be used:

DHT22 Description

DHT22 Deployment


#### 4.9.2 Specification

This section introduces the following classes and properties:

sosa:Platform , sosa:hosts , sosa:isHostedBy , ssn:System , ssn:hasSubSystem , ssn:Deployment , ssn:deployedSystem , ssn:hasDeployment , ssn:deployedOnPlatform , ssn:inDeployment

IRI: http://www.w3.org/ns/sosa/Platform

a OWL Class

IRI: http://www.w3.org/ns/sosa/hosts

a OWL Object Property

IRI: http://www.w3.org/ns/sosa/isHostedBy

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/System

a OWL Class

IRI: http://www.w3.org/ns/ssn/hasSubSystem

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/Deployment

a OWL Class

IRI: http://www.w3.org/ns/ssn/deployedSystem

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/hasDeployment

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/deployedOnPlatform

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/inDeployment

a OWL Object Property


## 5. Horizontal Segmentation

This section is non-normative.


### 5.1 System Capabilities Module

The namespace for system capabilities, operating ranges, and survival ranges terms is http://www.w3.org/ns/ssn/systems/

The suggested prefix for the system capabilities, operating ranges, and survival ranges terms is ssn-system

An ontology graph for this is
           available .


#### 5.1.1 Overview and examples

This section is non-normative.

The following figure provides an overview on the core classes and properties that are specifically related to modeling System capabilities, operating ranges, and survival ranges, under given conditions.

The following examples illustrate how the terms related to System capabilities, operating ranges, and survival ranges can be used:

DHT22 Description

IP68 Smart Sensor


#### 5.1.2 Specification

This section introduces the following classes and properties:

ssn-system:inCondition , ssn-system:Condition , ssn-system:hasSystemCapability , ssn-system:SystemCapability , ssn-system:hasSystemProperty , ssn-system:SystemProperty , ssn-system:MeasurementRange , ssn-system:ActuationRange , ssn-system:Accuracy , ssn-system:DetectionLimit , ssn-system:Drift , ssn-system:Frequency , ssn-system:Latency , ssn-system:Precision , ssn-system:Resolution , ssn-system:ResponseTime , ssn-system:Selectivity , ssn-system:Sensitivity , ssn-system:hasOperatingRange , ssn-system:OperatingRange , ssn-system:hasOperatingProperty , ssn-system:OperatingProperty , ssn-system:MaintenanceSchedule , ssn-system:OperatingPowerRange ssn-system:hasSurvivalRange , ssn-system:SurvivalRange , ssn-system:hasSurvivalProperty , ssn-system:SurvivalProperty ssn-system:SystemLifetime , ssn-system:BatteryLifetime ssn-system:qualityOfObservation

IRI: http://www.w3.org/ns/ssn/System

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/inCondition

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/systems/Condition

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/hasSystemCapability

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/systems/SystemCapability

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/hasSystemProperty

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/systems/SystemProperty

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/MeasurementRange

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/ActuationRange

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/Accuracy

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/DetectionLimit

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/Drift

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/Frequency

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/Latency

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/Precision

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/Resolution

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/ResponseTime

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/Selectivity

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/Sensitivity

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/hasOperatingRange

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/systems/OperatingRange

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/hasOperatingProperty

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/systems/OperatingProperty

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/MaintenanceSchedule

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/OperatingPowerRange

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/hasSurvivalRange

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/systems/SurvivalRange

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty

a OWL Object Property

IRI: http://www.w3.org/ns/ssn/systems/SurvivalProperty

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/SystemLifetime

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/BatteryLifetime

a OWL Class

IRI: http://www.w3.org/ns/ssn/systems/qualityOfObservation

a OWL Object Property


### 5.2 Sample Relations Module

This section is non-normative.

Samples are often related to other samples, by sub-sampling, topological relationships (stations along a traverse, pixels within an image, probe spots on a polished section, specimens retrieved within a borehole) or as parts of sample processing
                chains (crushing, splitting, dissecting, disolving). There are an essentially unlimited set of relationships between samples, so the nature of the relationship has its own class. This section describes a flexible model to describe such
                relationships between samples. The model is based on the QualifiedRelation
            pattern .

The namespace for Sample relationships terms is http://www.w3.org/ns/sosa/sampling/

The suggested prefix for the sample relationships namespace is sampling

An ontology
            graph for this is available .

The following figure provides an overview on the classes and properties that are specifically related to modeling Sample relationships.


#### 5.2.1 Sample Relationships Specification

This section introduces the following classes and properties:

sampling:RelationshipNature , sampling:hasSampleRelationship , sampling:natureOfRelationship , sampling:relatedSample

IRI: http://www.w3.org/ns/sosa/sampling/RelationshipNature

a OWL Class

IRI: http://www.w3.org/ns/sosa/sampling/SampleRelationship

a OWL Class

IRI: http://www.w3.org/ns/sosa/sampling/hasSampleRelationship

a OWL Object Property

IRI: http://www.w3.org/ns/sosa/sampling/natureOfRelationship

a OWL Object Property

IRI: http://www.w3.org/ns/sosa/sampling/relatedSample

a OWL Object Property


## 6. Vertical Segmentation

This section introduces the specifications for the vertical segmentation modules that align SOSA and SSN to a variety of related ontologies and specifications.


### 6.1 Dolce-Ultralite Alignment Module

This section is non-normative.

This section introduces the alignment of SSN to the DOLCE UltraLite upper ontology (DUL) which is the core dependency of the previous version of SSN. This serves to axiomatically clarify the intended meaning of SSN terms and will assist SSN
                users wishing to interoperate with other DUL-aligned ontologies. It is also imported in the SSNX alignment module that aligns SSN to the previous version of SSN. Note, however, that the DUL alignment can be used independently to align
                SSN with more generic concepts/properties of DUL.


#### 6.1.1 Namespaces

This section is non-normative.

The following namespace prefixes are used in the alignment to SOSA and SSN


#### 6.1.2 Class Alignments

This section is non-normative.

The following classes in SOSA and SSN can be aligned via a subclass relation as follows.

For more complex alignments, the axiomatic alignments are defined as follows.


#### 6.1.3 Property Alignments

This section is non-normative.

Additional alignments from SOSA/SSN to DUL properties are defined as follows.


### 6.2 SSNX Alignment Module

This section is non-normative.

This section formally relates the SSN ontology to the previous version of SSN that was published by the SSN-XG ("old SSN"). This may be useful for backward-compatibility and transition purposes. While the namespaces for SSN and DUL have changed
                since the SSN-XG first published the old SSN, the SSN alignment, known as "SSN-SSNX" is available at http://www.w3.org/2017/01/ssn-ssnx/ . Note that SSN-SSNX imports SSN-DUL.


#### 6.2.1 Namespaces

This section is non-normative.

The following namespace prefixes are used in the alignment to SOSA and SSN


#### 6.2.2 Class Alignments

This section is non-normative.

The primary classes from SSN-XG have direct equivalent classes in SOSA and SSN as shown below.

The following classes in SOSA and SSN are interpreted as superclasses of the corresponding ones in SSN-XG.

The more complex aligments of SSN-XG classes are expressed as combinations of axiomatic statements as follows.


#### 6.2.3 Property Alignments

This section is non-normative.

The following properties from SSN-XG have direct equivalent properties in SOSA and SSN.

Additional alignments from SSG-XG properties to SOSA and SSN are defined as follows.

The more complicated alignments are presented in combination with the property-chain axioms as follows.


### 6.3 O&M Alignment Module

This section introduces the alignment of SOSA/SSN to OGC Observations and Measurements [ OandM ] (also known as ISO 19156:2011).

The XML implementation of O&M [ OMXML ] is used for the payload for Sensor Observation Services, of which there are many operational deployments. Integration of these with observation
                data formalized using SOSA and SSN is highly desirable, and would be expected to significantly enrich the set of resources represented using SOSA/SSN. The alignment presented here provides a basis for transforming OM-XML data into RDF
                resources or OWL individuals according to the SOSA/SSN ontologies.


#### 6.3.1 Identifying the UML elements

O&M is specified as a UML model, following the patterns specified in ISO 19109 Geographic Information - Rules for Application Schema [ ISO-19109 ]. This means that the classes
                    represent concepts from the application domain, so can be approximately equated with classes in an ontology.

An OWL implementation of O&M may be generated by explicit translation of the UML following rules specified in [ ISO-19150-2 ] - see [ OM-Heavy ].
                    This translation generates an RDF entity denoted by a URI for every class, class attribute, and association-role from the original O&M UML model. The form of the URIs is also specified in [ ISO-19150-2 ],
                    and appear explicitly in the official
              OWL implementation of ISO 19156 (O&M) maintained by the ISO/TC
              211 Group on Ontology Management . These URIs are therefore convenient identifiers for elements of the O&M in a formal alignment.

The explicit translation from the UML model comes at the cost of a large set of dependencies on similar OWL translations of other UML models from the ISO 19100 series standards. Furthermore, the ontology structure reflects artefacts of
                    the UML-style of modeling. This implementation may introduce entailments that are inconsistent with SOSA/SSN (though no inconsistencies have been identified yet) so it is important to understand that use of these URIs here are principally intended to denote the original
                    UML classes and properties, rather than this OWL implementation.

NOTE: In response to the complexity of the explicit translation, a handcrafted version in more idiomatic OWL, without the dependencies, is also available [ OM-Lite ].

NOTE: At time of writing, the ISO-specified URIs do not de-reference. However, ISO/TC 211 are currently developing a publication system to enable this and thus the use of these URIs as Linked Data.


#### 6.3.2 Namespaces

The following namespace prefixes are used in the alignment to SOSA.


#### 6.3.3 Utility Classes

Three utility classes are defined locally to support the formalization of the alignment.


#### 6.3.4 Class Alignments

The primary classes from [ OandM ] have direct equivalents in SOSA classes supplemented by the utility classes described above, as follows.

Additional alignments from SOSA/SSN classes to O&M classes are as follows.

iso19156_sp:PreparationStep is a subclass since the act of Sampling applies to all sample types, not only physical specimens.

where iso19156_gfi:GFI_DomainFeature has the definition:

sosa:FeatureOfInterest is a subclass of iso19156_gfi:GFI_DomainFeature since not all domain features are subjects of observation.

where iso19156_gfi:GFI_Feature has the definition


#### 6.3.5 Property Alignments

The following properties from [ OandM ] have direct equivalents in SOSA properties.

Additional alignments from O&M properties to SOSA are as follows.

These are modeled as sub-properties because sosa:usedProcedure, sosa:hasResult, sosa:isResultOf and sosa:resultTime applies to actuation, observation or sampling activities.

This is modeled as a sub-property because the domain of iso19156-sfs:SF_SpatialSamplingFeature.hostedProcedure is a spatial sampling feature, such as a station, rather than a more general platform.

An RDF file containing a graph
              corresponding to this alignment is available .


### 6.4 OBOE Alignment Module

This section is non-normative.

This section introduces the alignment of SOSA to OBOE .

OBOE, the Extensible Observation Ontology, is used within the biodiversity community for semantic representation of observation data. The ontology is composed of multiple modules. The core observation elements are in the module OBOE-core.


#### 6.4.1 Namespaces

The following namespace prefixes are used in the alignment to SOSA.


#### 6.4.2 Class Alignments

This section is non-normative.

An oboe:Observation is composed of a collection of oboe:Measurements with the same feature of interest. Each oboe:Measurement concerns a distinct observed-property ("characteristic") and uses a distinct procedure ("protocol"). We therefore
                    choose to align sosa:Observation with oboe:Measurement.

The primary classes from [ OBOE ] are aligned with SOSA classes as follows.

The class oboe:Entity appears in OBOE as the range of the oboe:ofEntity and oboe:hasValue properties, so we interpret it as a general superclass.


#### 6.4.3 Property Alignments

This section is non-normative.

The following properties from [ OBOE ] may be directly aligned with SOSA properties.

oboe:hasValue, oboe:usesProtocol and oboe:usesMethod are sub-properties of the corresponding SOSA properties which apply to actuation and sampling as well as observation.

The feature of interest is linked to the oboe:Observation that contains a oboe:Measurement, rather than to the oboe:Measurement directly, so a property-chain axiom is required to express the alignment.

The properties oboe:hasMeasurement and its inverse oboe:measurementFor link an oboe:Observation to its member oboe:Measurements. These could be modeled as sub-properties related to rdfs:member and its inverse as follows.

An RDF file containing a graph
              corresponding to this alignment is available .


### 6.5 PROV Alignment Module

This section is non-normative.

This section introduces the alignment of SOSA to W3C PROV ([ prov-overview ], [ prov-dm ],
                [ prov-o ]).

The underlying structure of PROV is based around a process-flow model, with three base classes: Entity , which is the class of physical, digital, conceptual, or other kinds of things with some
                fixed aspects; Activity , which is the class of things that occur over a period of time and act upon or with entities, and it may include consuming, processing, transforming, modifying,
                relocating, using, or generating entities; and Agent , the class of things that bear some form of responsibility for an activity taking place, for the existence of an entity, or for another
                agent's activity.

The SOSA/SSN ontologies conceive observations, actuations, and acts of sampling as activities or events, that results in information being produced, or a change in the world, or the production or transformation of a sample. Thus, an alignment
                of SOSA to PROV is natural. Compton et al. [ SSN-PROV ] and Cox [ OM-Lite ] have previously described alignments of the SSNX and
                O&M models with [ prov-o ]. The alignment here is based on that work, also extended to consider actuation.


#### 6.5.1 Namespaces

This section is non-normative.

The following namespace prefixes are used in the alignment of SOSA to PROV.


#### 6.5.2 Class Alignments

This section is non-normative.

The primary classes from SOSA are aligned with the PROV classes as follows.

1. Acts of Observation, Actuation and Sampling are each kinds of Activity, thus:

2. Sensors, Actuators and Samplers are entities that are responsible for the corresponding activities, thus:

3. Procedures for observation, actuation or sampling are a kind of prov:Plan, thus:

4. The other classes from the core SOSA ontology represent either real or information resources, so are interpreted as kinds of prov:Entity, thus:


#### 6.5.3 Property Alignments

This section is non-normative.

The following properties from SOSA have simple alignments with PROV properties:

The final property alignment first requires some sub-properties of PROV properties to be defined:

Then sosa:usedProcedure is given by a property chain axiom:

An RDF file containing a graph corresponding to this alignment is available .


## 7. Common Modeling Questions

This section is non-normative.


### 7.1 Location

Many of the key classes provided by SOSA and SSN represent entities that can be located in space such as sensors, features of interest, actuators, samples, and so forth, or activities that can be located via their participating entities, e.g.,
                platforms. These entities will usually be described using models and ontologies defined for application domains, including technical disciplines, social and business contexts. In these contexts there are a number of implementations that
                support the expression of spatial properties, including location. These are discussed further in the Spatial Data on the Web Best Practices note [ SDW-BP ].

In particular, GeoSPARQL [ GeoSPARQL ] provides a flexible and relatively complete platform for geospatial objects, that fosters interoperability between geo-datasets. To do so, these
                entities can be declared as instances of geo:Feature and geometries can be assigned to them via the geo:hasGeometry property. In case of classes, e.g., specific features of interests such as rivers, these can be defined as subclasses of
                geo:Feature.


### 7.2 Forecasts

This section is non-normative.

One may also represent forecasts as observations if the value of sosa:phenomenonTime is later in time than the sosa:resultTime . Given the definition of these terms, it means that: The time when the
          Observation act was completed is before the time that the Result of
          the observation applies to the FeatureOfInterest.

Other means to represent forecasts are reported, but not in the scope of this specification. For example [ Lefrancois-et-al-2017 ] derives the SSN Sensing/Sensor/Observation pattern and define Forecasting/Forecaster/Forecast classes.

Describing a plan for some actuation or observation in the future is not covered by this specification.


### 7.3 Quantity Values and Unit of Measures

This section is non-normative.

The result of an sosa:Observation or an sosa:Actuation can be a quantity value with a numeric value and a unit of measure.

It is not in the scope of this specification to recommend any particular way of modeling results as quantity values. There exists external vocabularies that are specifically designed for modeling quantity values as OWL individuals. Examples
                    include the Quantities, Units, Dimensions and Data Types Ontologies (QUDT, [ QUDT ]) and the Ontology of Units of Measure (OM, [ Rijgersberg-et-al-2013 ]). With QUDT 1.1, a sosa:Result would be a qudt:QuantityValue . With OM 2, a sosa:Result would be a om:Measure or om:Point .

@prefix sosa: < http: // www.w3.org / ns / sosa /> .
@prefix xsd: < http: // www.w3.org / 2001 / XMLSchema #> .
@prefix qudt-1-1: < http: // qudt.org / 1.1 / schema / qudt #> .
@prefix qudt-unit-1-1: < http: // qudt.org / 1.1 / vocab / unit #> . < Observation / 234534 > a sosa:Observation ;
   rdfs:comment "Observation of the difference between 
                    the outside temperature and the inside temperature."@en ;
   sosa:hasFeatureOfInterest < apartment / 134 > ;
   sosa:hasResult [
      a qudt-1-1:QuantityValue ;
      qudt-1-1:unit qudt-unit-1-1:DegreeCelsius ;
      qudt-1-1:numericValue "-29.9"^^xsd:double ] . < Observation / 83985 > a sosa:Observation ;
   rdfs:comment "Observation of the temperature inside apartment #134."@en ;
   sosa:hasFeatureOfInterest < apartment / 134 > ;
   sosa:hasResult [
      a qudt-1-1:QuantityValue ;
      qudt-1-1:unit qudt-unit-1-1:DegreeCelsius ;
      qudt-1-1:numericValue "22.4"^^xsd:double ] .

@prefix sosa: < http: // www.w3.org / ns / sosa /> .
@prefix xsd: < http: // www.w3.org / 2001 / XMLSchema #> .
@prefix om: < http: // www.ontology-of-units-of-measure.org / resource / om-2 /> . < Observation / 234534 > a sosa:Observation ;
   rdfs:comment "Observation of the difference between
                    the outside temperature and the inside temperature."@en ;
   sosa:hasFeatureOfInterest < apartment / 134 > ;
   sosa:hasResult [
      a om:Measure ;
      om:hasUnit om:degreeCelsius ;
      om:hasNumericalValue "-29.9"^^xsd:double ] . < Observation / 83985 > a sosa:Observation ;
   rdfs:comment "Observation of the temperature inside apartment #134."@en ;
   sosa:hasFeatureOfInterest < apartment / 134 > ;
   sosa:hasResult [
      a om:Point ;
      om:hasScale om:CelsiusScale ;
      om:hasNumericalValue "22.4"^^xsd:double ] .

Other means to represent quantity values as literals are reported, but not in the scope of this specification. This solution would require the use of some custom datatype whose value space is some set of quantity values. Such a datatype
                    should be supported by RDF and SPARQL engines to support the comparison of quantity values. On the other hand, this approach is not compatible with the OWL specifications, that restrict the set of datatypes that can be used. See sec.
                    5.2 in [ owl2-syntax ] for more details.

@ prefix cdt: <http://w3id.org/lindt/custom_datatypes#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .

<observation/ 123 > a sosa:Observation ; sosa :hasSimpleResult "12 .4 m "^^ cdt :length .


### 7.4 Generic or Specific Instances of ssn:Property

This section is non-normative.

This specification does not specify whether an instance of ssn:Property should be generic to all features of interest (e.g., ex:Temperature , ex:OnOffStatus ), or specific to a single feature of interest (e.g., <myBodyTemperature> , <LightStatus> ). Implementers are free to choose one way of modeling things or the other.

On the other hand, one SHOULD NOT use OWL punning to make ex:Temperature denote both a subclass of ssn:Property and an instance of ssn:Property . In fact, merging the two examples below in a single RDF Graph would make an OWL reasoner infer that ex:Temperature , <office/1/temperature> , and <office/2/temperature> , denote the same individual.

This also holds for subclasses of ssn:Property : sosa:ObservableProperty , and sosa:ActuatableProperty .

This first example is modeling instances of ssn:Property as generic to all features of interest:

ex:Temperature a ssn:Property . < office / 1 > a sosa:FeatureOfInterest;
  ssn:hasProperty ex:Temperature . < Observation / 1 > a sosa:Observation ;
  sosa:observedProperty ex:Temperature ;
  sosa:hasFeatureOfInterest < office / 1 > . < office / 2 > a sosa:FeatureOfInterest;
  ssn:hasProperty ex:Temperature . < Observation / 2 > a sosa:Observation ;
  sosa:observedProperty ex:Temperature ;
  sosa:hasFeatureOfInterest < office / 2 > .

This second example is modeling instances of ssn:Property as specific to a features of interest:

ex:Temperature a owl:Class ;
  rdfs:subClassOf ssn:Property . < office / 1 > a sosa:FeatureOfInterest;
  ssn:hasProperty < office / 1 / temperature > . < office / 1 / temperature > a ex:Temperature , ssn:Property . < Observation / 1 > a sosa:Observation ;
  sosa:observedProperty < office / 1 / temperature > ;
  sosa:hasFeatureOfInterest < office / 1 > . < office / 2 > a sosa:FeatureOfInterest;
  ssn:hasProperty < office / 2 / temperature > . < office / 2 / temperature > a ex:Temperature , ssn:Property . < Observation / 2 > a sosa:Observation ;
  sosa:observedProperty < office / 2 / temperature > ;
  sosa:hasFeatureOfInterest < office / 2 > .


### 7.5 Generic or Specific Instances of ssn:System

This section is non-normative.

This specification does not specify whether an instance of ssn:System should be generic (e.g., ex:TemperatureSensor , ex:LightActuator ), or specific to a single feature of interest (e.g., <temperatureSensor/84> , <light/112> ). Implementers are free to choose one way of modeling things or the other.

On the other hand, one SHOULD NOT use OWL punning to make ex:Temperature denote both a subclass of ssn:Property and an instance of ssn:Property. In fact, merging the two examples below in a single RDF Graph would make an OWL reasoner infer that ex:TemperatureSensor , <TemperatureSensor/1> ,
                and <TemperatureSensor/2> , denote the same individual.

This also holds for subclasses of ssn:System : sosa:Sensor , sosa:Actuator , and sosa:Sampler .

This first example is modeling instances of ssn:System as generic:

ex:TemperatureSensor a ssn:System . < Observation / 1 > a sosa:Observation ;
  sosa:madeBySensor ex:TemperatureSensor . < Observation / 2 > a sosa:Observation ;
  sosa:madeBySensor ex:TemperatureSensor . # describing the system capabilities and operating/survival range can be done generically # with this modeling choice: ex:TemperatureSensor ssn-system:hasOperatingRange ex:TemperatureSensorOperatingRange .

ex:TemperatureSensorOperatingRange a ssn-system:OperatingRange ;
  ssn-system:inCondition ex:NormalTemperatureCondition , ex:NormalHumidityCondition .

This second example is modeling instances of ssn:System as specific:

ex:TemperatureSensor a owl:Class ;
  rdfs:subClassOf ssn:System . < TemperatureSensor / 1 > a ex:TemperatureSensor , ssn:System . < Observation / 1 > a sosa:Observation ;
  sosa:madeBySensor < TemperatureSensor / 1 > . < TemperatureSensor / 2 > a ex:TemperatureSensor , ssn:System . < Observation / 2 > a sosa:Observation ;
  sosa:madeBySensor < TemperatureSensor / 2 > .

# describing the system capabilities and operating/survival range can be done at the level of 
# the class or at the level of each instance with this modeling choice:

ex:TemperatureSensor  rdfs:subClassOf [
    owl:onProperty ssn-system:hasOperatingRange ;
    owl:hasValue ex:TemperatureSensorOperatingRange ] . < TemperatureSensor / 1 > ssn-system:hasOperatingRange ex:TemperatureSensorOperatingRange ; # this axiom can be inferred
  ssn-system:hasOperatingRange < moreSpecificTemperatureSensorOperatingRange > . < moreSpecificTemperatureSensorOperatingRange > a ssn-system:OperatingRange ;
  ssn-system:inCondition < modeSpecificTemperatureCondition > , < modeSpecificHumidityCondition > .


## A. Wide review

Results of the wide review of SOSA and SSN is summarized here .


## B. Complete Examples


### B.1 iPhone Barometer

An RDF file containing a graph corresponding to this example is available .

@prefix rdf: < http: // www.w3.org / 1999 / 02 / 22-rdf-syntax-ns #> .
@prefix rdfs: < http: // www.w3.org / 2000 / 01 / rdf-schema #> .
@prefix xsd: < http: // www.w3.org / 2001 / XMLSchema #> .
@prefix sosa: < http: // www.w3.org / ns / sosa /> .
@prefix time: < http: // www.w3.org / 2006 / time #> .
@prefix qudt-1-1: < http: // qudt.org / 1.1 / schema / qudt #> .
@prefix qudt-unit-1-1: < http: // qudt.org / 1.1 / vocab / unit #> .
@prefix cdt: < http: // w3id.org / lindt / custom_datatypes #> .
@base < http: // example.org / data /> .

# The barometric readings from a Bosch Sensortec BMP282 sensor in an Apple IPhone 7
# observed on June 6 2017 using only the SOSA core for modelling. < earthAtmosphere > rdf:type sosa:FeatureOfInterest ;
  rdfs:label "Atmosphere of Earth"@en .


# An iPhone 7 as the Platform that hosts several sensors,
# among others the Bosch Sensortec BMP282 atmospheric pressure sensor. < iphone7 / 35-207306-844818-0 > a sosa:Platform ;
  rdfs:label "IPhone 7 - IMEI 35-207306-844818-0"@en ;
  rdfs:comment "IPhone 7 - IMEI 35-207306-844818-0 - John Doe"@en ;
  sosa:hosts < sensor / 35-207306-844818-0 / BMP282 > . < sensor / 35-207306-844818-0 / BMP282 > rdf:type sosa:Sensor ;
  rdfs:label "Bosch Sensortec BMP282"@en ;
  sosa:observes < sensor / 35-207306-844818-0 / BMP282 / atmosphericPressure > .


# An observation made by the BMP282 atmospheric pressure sensor. < Observation / 346344 > rdf:type sosa:Observation ;
  sosa:observedProperty < sensor / 35-207306-844818-0 / BMP282 / atmosphericPressure > ;
  sosa:hasFeatureOfInterest < earthAtmosphere > ;
  sosa:madeBySensor < sensor / 35-207306-844818-0 / BMP282 > ;
  sosa:hasSimpleResult "1021.45 hPa"^^cdt:ucum ;
  sosa:resultTime "2017-06-06T12:36:12Z"^^xsd:dateTime .


# Another observation made a second later by the BMP282 atmospheric pressure sensor
# using the QUDT Ontology for the Units of Measurement
# and the Time Ontology for the instant. < Observation / 346345 > rdf:type sosa:Observation ;
  sosa:observedProperty < sensor / 35-207306-844818-0 / BMP282 / atmosphericPressure > ;
  sosa:hasFeatureOfInterest < earthAtmosphere > ;
  sosa:madeBySensor < sensor / 35-207306-844818-0 / BMP282 > ;
  sosa:hasResult [
    rdf:type qudt-1-1:QuantityValue ;
    qudt-1-1:numericValue "101936"^^xsd:double ;
    qudt-1-1:unit qudt-unit-1-1:Pascal ] ;
  sosa:resultTime [
    rdf:type time:Instant ;
    time:inXSDDateTimeStamp "2017-06-06T12:36:13+00:00"^^xsd:dateTimeStamp ] .


### B.2 Coal Oil Point Reserve

An RDF file containing a graph corresponding to this example is available .

@prefix rdf: < http: // www.w3.org / 1999 / 02 / 22-rdf-syntax-ns #> .
 @prefix owl: < http: // www.w3.org / 2002 / 07 / owl #> .
 @prefix rdfs: < http: // www.w3.org / 2000 / 01 / rdf-schema #> .
 @prefix sosa: < http: // www.w3.org / ns / sosa #> .
 @prefix xsd: < http: // www.w3.org / 2001 / XMLSchema #> .
 @prefix cdt: < http: // w3id.org / lindt / custom_datatypes #> .

@base < http: // example.org / data /> . < IDEA > a owl:Ontology ;
   owl:imports < http: // www.w3.org / ns / sosa > . < COPR > a sosa:FeatureOfInterest ;
   sosa:hasSample < COPR_SL > ;
   rdfs:comment "Coal Oil Point Reserve: UC Santa Barbara Natural Reserve System"@en ;
   rdfs:label "Coal Oil Point Reserve"@en . < COPR_Station_Location > a sosa:Sample ;
   rdfs:comment "."@en ;
   rdfs:label "Air around COPR Station"@en ;
   sosa:isSampleOf < COPR > . < COPR_Station > a sosa:Platform ;
   rdfs:comment "Station at Coal Oil Point Reserve, CA (see http://www.geog.ucsb.edu/ideas/COPR.html for details)"@en ;
   rdfs:label "Coal Oil Point Reserve Wx Station"@en ;
   rdfs:seeAlso < http: // www.geog.ucsb.edu / ideas / COPR.html > ;
   sosa:hosts < COPR-HMP45C-L > . < COPR-HMP45C-L > a sosa:Platform ;
   rdfs:label "HMP45C-L Temperature and Relative Humidity Probe at Coal Oil Point, UCSB, CA"@en ;
   sosa:hosts < HUMICAP-H > ;
   sosa:isHostedBy < COPR_Station > . < HUMICAP-H > a sosa:Sensor ;
   rdfs:label "Vaisala HUMICAP H-chip"@en ;
   sosa:isHostedBy < COPR-HMP45C-L > . < RelativeHumidity > a sosa:ObservableProperty ;
   rdfs:comment "Humidity is a measure of the moisture content of air."@en ;
   rdfs:label "Relative Humidity"@en . < MeasuringRelativeHumidity > a sosa:Procedure ;
   rdfs:comment "Instructions for measuring relative humidity"@en . < RH_avg_1_COPR_15min_201706020300PM > a sosa:Observation ;
   rdfs:comment "Relative humidity as averaged over 15min at COPR."@en ;
   rdfs:label "Relative humidity, AVG, 15min, COPR, 06.02.2017, 3:00 PM"@en ;
   sosa:madeBySensor < HUMICAP-H > ;
   sosa:hasFeatureOfInterest < COPR_Station_Location > ;
   sosa:hasSimpleResult "92.5 %"^^cdt:ucum ;
   sosa:resultTime "2017-06-02-T03:00:00-7:00"^^xsd:dateTime ;
   sosa:observedProperty < RelativeHumidity > ;
   sosa:usedProcedure < MeasuringRelativeHumidity > .


### B.3 apartment 134

An RDF file containing a graph corresponding to this example is available .

@prefix rdf: < http: // www.w3.org / 1999 / 02 / 22-rdf-syntax-ns #> .
@prefix time: < http: // www.w3.org / 2006 / time #> .
@prefix sosa: < http: // www.w3.org / ns / sosa /> .
@prefix ssn: < http: // www.w3.org / ns / ssn /> .
@prefix xsd: < http: // www.w3.org / 2001 / XMLSchema #> .
@prefix qudt-1-1: < http: // qudt.org / 1.1 / schema / qudt #> .
@prefix qudt-unit-1-1: < http: // qudt.org / 1.1 / vocab / unit #> .
@base < http: // example.org / data /> .

# The electric consumption of apartment #134 on April 15 2017 was 22.4 kWh as 
# observed by sensor #926. The result was available 12 seconds later. < Observation / 235714 > rdf:type sosa:Observation ;
  sosa:observedProperty < apartment / 134 / electricConsumption > ;
  sosa:madeBySensor < sensor / 926 > ; 
  sosa:hasResult [
     rdf:type qudt-1-1:QuantityValue ;
     qudt-1-1:numericValue "22.4"^^xsd:double ;
     qudt-1-1:unit qudt-unit-1-1:Kilowatthour ] ;
  sosa:phenomenonTime [
    rdf:type time:Interval ;
    time:hasBeginning [ 
      rdf:type time:Instant ;
      time:inXSDDateTimeStamp "2017-04-15T00:00:00+00:00"^^xsd:dateTimeStamp ] ;
    time:hasEnd [ 
      rdf:type time:Instant ;
      time:inXSDDateTimeStamp "2017-04-16T00:00:00+00:00"^^xsd:dateTimeStamp ] ] ;
  sosa:resultTime "2017-04-16T00:00:12+00:00"^^xsd:dateTimeStamp .


# Sensor #926 observes the electric consumption of apartment #134, and we know that 
# it made some observations. < sensor / 926 > rdf:type sosa:Sensor ;
  sosa:observes < apartment / 134 / electricConsumption > ;
  sosa:madeObservation < Observation / 235714 > , < Observation / 235715 > , < Observation / 235716 > .

# mobile sensor tempSensor #23 observes the temperature in its surroundings, and we know 
# that it made some observations. < tempSensor / 23 > rdf:type sosa:Sensor ;
  sosa:observes < tempSensor / 23 # temperature > ;
  sosa:madeObservation < tempSensor / 23 / 4572 > , < tempSensor / 23 / 4573 > , < tempSensor / 23 / 4574 > .


# Sensor #926 observes the electric consumption of apartment #134 < sensor / 926 > rdf:type sosa:Sensor ;
  sosa:observes < apartment / 134 / electricConsumption > .

# This is equivalent to saying that the electric consumption of apartment #134 is 
# observed by Sensor #926 < apartment / 134 / electricConsumption > rdf:type sosa:ObservableProperty ;
  sosa:isObservedBy < sensor / 926 > .


# Sensor #926 made observations identified by < Observation / 235714 > and < Observation / 235715 > . < sensor / 926 > rdf:type sosa:Sensor ;
  sosa:madeObservation < Observation / 235714 > , < Observation / 235715 > .

# This is equivalent to saying that these observations have been made by sensor #926. < Observation / 235714 > rdf:type sosa:Observation ;
  sosa:madeBySensor < sensor / 926 > . < Observation / 235754 > rdf:type sosa:Observation ;
  sosa:madeBySensor < sensor / 926 > .


# the window opening state is an ActuatableProperty.
# SSN allows to explicitly say that < window / 104 # state > is a property of < window > < window > rdf:type sosa:FeatureOfInterest ;
  ssn:hasProperty < window / 104 # state > . < window / 104 # state > rdf:type sosa:ActuatableProperty ;
  sosa:isActedOnBy < actuation / 188 > .


# WindowCloser #987 made actuation #188
# SSN allows to explicitly say that < windowCloser / 987 > is designed to automatically open and close window #104. < windowCloser / 987 > rdf:type sosa:Actuator ;
  sosa:madeActuation < actuation / 188 > ;
  ssn:forProperty < window / 104 # state > .


# Actuation #188 acted on the state of window #104 and returned 'true'. < actuation / 188 > rdf:type sosa:Actuation ;
  sosa:actsOnProperty < window / 104 # state > ;
  sosa:actuationMadeBy < windowCloser / 987 > ; 
  sosa:hasSimplResult true ;
  sosa:resultTime "2017-04-18T17:24:00+02:00"^^xsd:dateTimeStamp .

An RDF file containing a graph corresponding to this example is available .

@prefix rdf: < http: // www.w3.org / 1999 / 02 / 22-rdf-syntax-ns #> .
@prefix time: < http: // www.w3.org / 2006 / time #> .
@prefix sosa: < http: // www.w3.org / ns / sosa /> .
@prefix xsd: < http: // www.w3.org / 2001 / XMLSchema #> .
@prefix qudt-1-1: < http: // qudt.org / 1.1 / schema / qudt #> .
@prefix qudt-unit-1-1: < http: // qudt.org / 1.1 / vocab / unit #> .
@base < http: // example.org / data /> .

# The electric consumption of apartment #134 on April 15 2017 was 22.4 kWh as 
# observed by sensor #926. The result was available 12 seconds later. < Observation / 235714 > rdf:type sosa:Observation ;
  sosa:observedProperty < apartment / 134 / electricConsumption > ;
  sosa:madeBySensor < sensor / 926 > ; 
  sosa:hasResult [
     rdf:type qudt-1-1:QuantityValue ;
     qudt-1-1:numericValue "22.4"^^xsd:double ;
     qudt-1-1:unit qudt-unit-1-1:Kilowatthour ] ;
  sosa:phenomenonTime [
    rdf:type time:Interval ;
    time:hasBeginning [ 
      rdf:type time:Instant ;
      time:inXSDDateTimeStamp "2017-04-15T00:00:00+00:00"^^xsd:dateTimeStamp ] ;
    time:hasEnd [ 
      rdf:type time:Instant ;
      time:inXSDDateTimeStamp "2017-04-16T00:00:00+00:00"^^xsd:dateTimeStamp ] ] ;
  sosa:resultTime "2017-04-16T00:00:12+00:00"^^xsd:dateTimeStamp .


# Sensor #926 observes the electric consumption of apartment #134, and we know that 
# it made some observations. < sensor / 926 > rdf:type sosa:Sensor ;
  sosa:observes < apartment / 134 / electricConsumption > ;
  sosa:madeObservation < Observation / 235714 > , < Observation / 235715 > , < Observation / 235716 > .

# mobile sensor tempSensor #23 observes the temperature in its surroundings, and we know 
# that it made some observations. < tempSensor / 23 > rdf:type sosa:Sensor ;
  sosa:observes < tempSensor / 23 # temperature > ;
  sosa:madeObservation < tempSensor / 23 / 4572 > , < tempSensor / 23 / 4573 > , < tempSensor / 23 / 4574 > .


# Sensor #926 observes the electric consumption of apartment #134 < sensor / 926 > rdf:type sosa:Sensor ;
  sosa:observes < apartment / 134 / electricConsumption > .

# This is equivalent to saying that the electric consumption of apartment #134 is 
# observed by Sensor #926 < apartment / 134 / electricConsumption > rdf:type sosa:ObservableProperty ;
  sosa:isObservedBy < sensor / 926 > .


# Sensor #926 made observations identified by < Observation / 235714 > and < Observation / 235715 > . < sensor / 926 > rdf:type sosa:Sensor ;
  sosa:madeObservation < Observation / 235714 > , < Observation / 235715 > .

# This is equivalent to saying that these observations have been made by sensor #926. < Observation / 235714 > rdf:type sosa:Observation ;
  sosa:madeBySensor < sensor / 926 > . < Observation / 235754 > rdf:type sosa:Observation ;
  sosa:madeBySensor < sensor / 926 > .


# the window opening state is an ActuatableProperty. < window > rdf:type sosa:FeatureOfInterest . < window / 104 # state > rdf:type sosa:ActuatableProperty ;
  sosa:isActedOnBy < actuation / 188 > .


# WindowCloser #987 made actuation #188 < windowCloser / 987 > rdf:type sosa:Actuator ;
  sosa:madeActuation < actuation / 188 > .


# Actuation #188 acted on the state of window #104 and returned 'true'. < actuation / 188 > rdf:type sosa:Actuation ;
  sosa:actsOnProperty < window / 104 # state > ;
  sosa:actuationMadeBy < windowCloser / 987 > ; 
  sosa:hasSimplResult true ;
  sosa:resultTime "2017-04-18T17:24:00+02:00"^^xsd:dateTimeStamp .


### B.4 Tree height measurement

An RDF file containing a graph corresponding to this example is available .

@prefix rdf: < http: // www.w3.org / 1999 / 02 / 22-rdf-syntax-ns #> .
@prefix rdfs: < http: // www.w3.org / 2000 / 01 / rdf-schema #> .
@prefix sosa: < http: // www.w3.org / ns / sosa /> .
@prefix ssn: < http: // www.w3.org / ns / ssn /> .
@prefix xsd: < http: // www.w3.org / 2001 / XMLSchema #> .
@prefix qudt-1-1: < http: // qudt.org / 1.1 / schema / qudt #> .
@prefix qudt-unit-1-1: < http: // qudt.org / 1.1 / vocab / unit #> .
@base < http: // example.org / data /> .

# rangefinder #30 is a laser range finder sensor that was used 
# to observe the height of tree #124 and #125. < rangefinder / 30 > rdf:type           sosa:Sensor ;
  rdfs:label "rangefinder #30"@en ;
  rdfs:comment "rangefinder #30 is a laser range finder sensor."@en .

# rangefinder #30 made observation #1087 of the height of tree #124. < observation / 1087 > rdf:type               sosa:Observation ;
  rdfs:label "observation #1087"@en ;
  sosa:hasFeatureOfInterest < tree / 124 > ;
  sosa:observedProperty < tree / 124 / height > ;
  sosa:madeBySensor < rangefinder / 30 > ;
  sosa:hasResult [ 
    qudt-1-1:unit qudt-unit-1-1:Meter ; 
    qudt-1-1:numericalValue "15.3"^^xsd:double ] .

# using SSN, one can explicitly link a property and its feature of interest. < tree / 124 > rdf:type    sosa:FeatureOfInterest ;
  rdfs:label "tree #124"@en ;
  ssn:hasProperty < tree / 124 # height > . < tree / 124 # height > rdf:type    sosa:ObservableProperty , ssn:Property ;
  rdfs:label "the height of tree #124"@en ;
  ssn:isPropertyOf < tree / 124 > .

# rangefinder #30 made observation #1088 of the height of tree #125. < observation / 1088 > rdf:type               sosa:Observation ;
  rdfs:label "observation #1088"@en ;
  sosa:hasFeatureOfInterest < tree / 125 > ;
  sosa:observedProperty < tree / 125 / height > ;
  sosa:madeBySensor < rangefinder / 30 > ;
  sosa:hasResult [ 
    qudt-1-1:numericValue "23.0"^^xsd:double ;
    qudt-1-1:unit qudt-unit-1-1:Meter ] .

# using SSN, one can explicitly link a property and its feature of interest. < tree / 125 > rdf:type    sosa:FeatureOfInterest ;
  rdfs:label "tree #125"@en ;
  ssn:hasProperty < tree / 125 # height > . < tree / 125 # height > rdf:type    sosa:ObservableProperty , ssn:Property ;
  rdfs:label "the height of tree #125"@en ;
  ssn:isPropertyOf < tree / 124 > .

An RDF file containing a graph corresponding to this example is available .

@prefix rdf: < http: // www.w3.org / 1999 / 02 / 22-rdf-syntax-ns #> .
@prefix rdfs: < http: // www.w3.org / 2000 / 01 / rdf-schema #> .
@prefix sosa: < http: // www.w3.org / ns / sosa /> .
@prefix xsd: < http: // www.w3.org / 2001 / XMLSchema #> .
@prefix qudt-1-1: < http: // qudt.org / 1.1 / schema / qudt #> .
@prefix qudt-unit-1-1: < http: // qudt.org / 1.1 / vocab / unit #> .
@base < http: // example.org / data /> .

# rangefinder #30 is a laser range finder sensor that was used 
# to observe the height of tree #124 and #125. < rangefinder / 30 > rdf:type           sosa:Sensor ;
  rdfs:label "rangefinder #30"@en ;
  rdfs:comment "rangefinder #30 is a laser range finder sensor."@en .

# rangefinder #30 made observation #1087 of the height of tree #124. < observation / 1087 > rdf:type               sosa:Observation ;
  rdfs:label "observation #1087"@en ;
  sosa:hasFeatureOfInterest < tree / 124 > ;
  sosa:observedProperty < tree / 124 / height > ;
  sosa:madeBySensor < rangefinder / 30 > ;
  sosa:hasResult [ 
    qudt-1-1:unit qudt-unit-1-1:Meter ; 
    qudt-1-1:numericalValue "15.3"^^xsd:double ] . < tree / 124 > rdf:type    sosa:FeatureOfInterest ;
  rdfs:label "tree #124"@en . < tree / 124 # height > rdf:type    sosa:ObservableProperty , ssn:Property ;
  rdfs:label "the height of tree #124"@en .

# rangefinder #30 made observation #1088 of the height of tree #125. < observation / 1088 > rdf:type               sosa:Observation ;
  rdfs:label "observation #1088"@en ;
  sosa:hasFeatureOfInterest < tree / 125 > ;
  sosa:observedProperty < tree / 125 / height > ;
  sosa:madeBySensor < rangefinder / 30 > ;
  sosa:hasResult [ 
    qudt-1-1:numericValue "23.0"^^xsd:double ;
    qudt-1-1:unit qudt-unit-1-1:Meter ] . < tree / 125 > rdf:type    sosa:FeatureOfInterest ;
  rdfs:label "tree #125"@en . < tree / 125 # height > rdf:type    sosa:ObservableProperty , ssn:Property ;
  rdfs:label "the height of tree #125"@en .


### B.5 Seismographs

An RDF file containing a graph corresponding to this example is available .

@prefix rdf: < http: // www.w3.org / 1999 / 02 / 22-rdf-syntax-ns #> .
@prefix rdfs: < http: // www.w3.org / 2000 / 01 / rdf-schema #> .
@prefix sosa: < http: // www.w3.org / ns / sosa /> .
@prefix ssn: < http: // www.w3.org / ns / ssn /> .
@prefix geo: < http: // www.w3.org / 2003 / 01 / geo / wgs84_pos #> .
@prefix xsd: < http: // www.w3.org / 2001 / XMLSchema #> .
@prefix qudt-1-1: < http: // qudt.org / 1.1 / schema / qudt #> .
@prefix qudt-unit-1-1: < http: // qudt.org / 1.1 / vocab / unit #> .
@base < http: // example.org / data /> .

# Observation #358 of seismograph VCAB DP1 BP 40 (Vineyard Canyon, Parkfield, Ca) measured
# a earth displacement speed of 0.000500 cm/sec at 8:23 am on April 18, 2017, Pacific
# Daylight Time. < earth > rdf:type    sosa:FeatureOfInterest ;
  rdfs:label "earth"@en . < VCAB-DP1-BP-40 > rdf:type sosa:Sensor ;
  rdfs:label "seismograph VCAB DP1 BP 40 (Vineyard Canyon, Parkfield, Ca)"@en ;
  rdfs:seeAlso < https: // earthquake.usgs.gov / monitoring / seismograms / 153 > ;
  sosa:observes < VCAB-DP1-BP-40#groundDisplacementSpeed > . < VCAB-DP1-BP-40#location > rdf:type sosa:FeatureOfInterest ;
  rdfs:label "location of VCAB-DP1-BP-40"@en ;
  geo:lat 35.8648067 ;
  geo:long -120.6195831 ;
  geo:alt 12.75 ;
  sosa:isSampleOf < earth > . < VCAB-DP1-BP-40#groundDisplacementSpeed > rdf:type    sosa:ObservableProperty , ssn:Property ;
  rdfs:label "the ground displacement speed at location of VCAB-DP1-BP-40"@en ;
  sosa:isObservedBy < VCAB-DP1-BP-40 > . < VCAB-DP1-BP-40?t=2017-04-18T08%3A23%3A00-07%3A00 > rdf:type sosa:Observation ;
  sosa:madeBySensor < VCAB-DP1-BP-40 > ; 
  sosa:hasFeatureOfInterest < VCAB-DP1-BP-40#location > ;
  sosa:observedProperty < VCAB-DP1-BP-40#groundDisplacementSpeed > ;
  sosa:hasResult [
     rdf:type qudt-1-1:QuantityValue ;
     qudt-1-1:numericValue "5e-4"^^xsd:double ;
     qudt-1-1:unit qudt-unit-1-1:CentimeterPerSecond ] ;
  sosa:resultTime "2017-04-18T08:23:00-07:00"^^xsd:dateTimeStamp .

# using SSN one can explicitly state that < VCAB-DP1-BP-40#groundDisplacementSpeed > is the property of < VCAB-DP1-BP-40#location > . < VCAB-DP1-BP-40#location > ssn:hasProperty < VCAB-DP1-BP-40#groundDisplacementSpeed > ;

An RDF file containing a graph corresponding to this example is available .

@prefix rdf: < http: // www.w3.org / 1999 / 02 / 22-rdf-syntax-ns #> .
@prefix rdfs: < http: // www.w3.org / 2000 / 01 / rdf-schema #> .
@prefix sosa: < http: // www.w3.org / ns / sosa /> .
@prefix geo: < http: // www.w3.org / 2003 / 01 / geo / wgs84_pos #> .
@prefix xsd: < http: // www.w3.org / 2001 / XMLSchema #> .
@prefix qudt-1-1: < http: // qudt.org / 1.1 / schema / qudt #> .
@prefix qudt-unit-1-1: < http: // qudt.org / 1.1 / vocab / unit #> .
@base < http: // example.org / data /> .

# Observation #358 of seismograph VCAB DP1 BP 40 (Vineyard Canyon, Parkfield, Ca) measured
# a earth displacement speed of 0.000500 cm/sec at 8:23 am on April 18, 2017, Pacific
# Daylight Time. < earth > rdf:type    sosa:FeatureOfInterest ;
  rdfs:label "earth"@en . < VCAB-DP1-BP-40 > rdf:type sosa:Sensor ;
  rdfs:label "seismograph VCAB DP1 BP 40 (Vineyard Canyon, Parkfield, Ca)"@en ;
  rdfs:seeAlso < https: // earthquake.usgs.gov / monitoring / seismograms / 153 > ;
  sosa:observes < VCAB-DP1-BP-40#groundDisplacementSpeed > . < VCAB-DP1-BP-40#location > rdf:type sosa:FeatureOfInterest ;
  rdfs:label "location of VCAB-DP1-BP-40"@en ;
  geo:lat 35.8648067 ;
  geo:long -120.6195831 ;
  geo:alt 12.75 ;
  sosa:isSampleOf < earth > . < VCAB-DP1-BP-40#groundDisplacementSpeed > rdf:type    sosa:ObservableProperty , ssn:Property ;
  rdfs:label "the ground displacement speed at location of VCAB-DP1-BP-40"@en ;
  sosa:isObservedBy < VCAB-DP1-BP-40 > . < VCAB-DP1-BP-40?t=2017-04-18T08%3A23%3A00-07%3A00 > rdf:type sosa:Observation ;
  sosa:madeBySensor < VCAB-DP1-BP-40 > ; 
  sosa:hasFeatureOfInterest < VCAB-DP1-BP-40#location > ;
  sosa:observedProperty < VCAB-DP1-BP-40#groundDisplacementSpeed > ;
  sosa:hasResult [
     rdf:type qudt-1-1:QuantityValue ;
     qudt-1-1:numericValue "5e-4"^^xsd:double ;
     qudt-1-1:unit qudt-unit-1-1:CentimeterPerSecond ] ;
  sosa:resultTime "2017-04-18T08:23:00-07:00"^^xsd:dateTimeStamp .


### B.6 Number of sunspots

An RDF file containing a graph corresponding to this example is available .

@prefix rdf: < http: // www.w3.org / 1999 / 02 / 22-rdf-syntax-ns #> .
@prefix time: < http: // www.w3.org / 2006 / time #> .
@prefix sosa: < http: // www.w3.org / ns / sosa /> .
@prefix xsd: < http: // www.w3.org / 2001 / XMLSchema #> .
@base < http: // example.org / data /> .

# The result of an observation of the sunspot number is available a few minutes 
# after the phenomenon time, due to the light travel duration. < Observation / 7536 > rdf:type sosa:Observation ;
  sosa:observedProperty < Sun#sunspotNumber > ;
  sosa:hasSimpleResult 66 ;
  sosa:phenomenonTime [
    rdf:type time:Instant ;
    time:inXSDDateTimeStamp "2017-03-31T11:51:42+00:00"^^xsd:dateTimeStamp ] ;
  sosa:resultTime "2017-03-31T12:00:00+00:00"^^xsd:dateTimeStamp .


### B.7 Wind sensor spinning cups

An RDF file containing a graph corresponding to this example is available .

@prefix rdf: < http: // www.w3.org / 1999 / 02 / 22-rdf-syntax-ns #> .
@prefix sosa: < http: // www.w3.org / ns / sosa /> .
@prefix ssn: < http: // www.w3.org / ns / ssn /> .
@prefix xsd: < http: // www.w3.org / 2001 / XMLSchema #> .
@base < http: // example.org / data /> .

# movements of spinning cups on wind sensor #14 serves as proxies for the wind speed
# at the location of the wind sensor. < windSensor / 14 > rdf:type sosa:Sensor ;
  sosa:observes < location / 4687 # windSpeed > .

# wind sensor #14 detected some movement of spinning cups, from which originated the
# observations #147 and #148. < windSensor / 14 > rdf:type sosa:Sensor ;
  sosa:madeObservation < observation / 147 > , < observation / 148 > ; 
  ssn:detects < observation / 147 # spinningCupsMovement > , < observation / 148 # spinningCupsMovement > .

# observation #147 was originated by the movement of the spinning cups of sensor #14.
# the result of observations #147 and #148 is using some custom datatype that encodes the unit of measure. < observation / 147 > rdf:type sosa:Observation ;
  sosa:observedProperty < location / 4687 # windSpeed > ;
  sosa:madeBySensor < windSensor / 14 > ;
  ssn:wasOriginatedBy < observation / 147 # spinningCupsMovement > ;
  sosa:resultTime "2017-04-12T12:00:00Z"^^xsd:dateTime ;
  sosa:hasSimpleResult "47 km/h"^^ < speed > . < observation / 147 # spinningCupsMovement > rdf:type ssn:Stimulus ;
  ssn:isProxyFor < location / 4687 # windSpeed > . < observation / 148 > rdf:type sosa:Observation ;
  sosa:observedProperty < location / 4687 # windSpeed > ;
  sosa:madeBySensor < windSensor / 14 > ;
  ssn:wasOriginatedBy < observation / 148 # spinningCupsMovement > ;
  sosa:resultTime "2017-04-12T12:01:00Z"^^xsd:dateTime ;
  sosa:hasSimpleResult "43 km/h"^^ < speed > . < observation / 148 # spinningCupsMovement > rdf:type ssn:Stimulus ;
  ssn:isProxyFor < location / 4687 # windSpeed > .

An RDF file containing a graph corresponding to this example is available .

@prefix rdf: < http: // www.w3.org / 1999 / 02 / 22-rdf-syntax-ns #> .
@prefix sosa: < http: // www.w3.org / ns / sosa /> .
@prefix xsd: < http: // www.w3.org / 2001 / XMLSchema #> .
@base < http: // example.org / data /> .

# movements of spinning cups on wind sensor #14 serves as proxies for the wind speed
# at the location of the wind sensor. < windSensor / 14 > rdf:type sosa:Sensor ;
  sosa:observes < location / 4687 # windSpeed > .

# wind sensor #14 made observations #147 and #148. < windSensor / 14 > rdf:type sosa:Sensor ;
  sosa:madeObservation < observation / 147 > , < observation / 148 > .

# the result of observations #147 and #148 is using some custom datatype that encodes the unit of measure. < observation / 147 > rdf:type sosa:Observation ;
  sosa:observedProperty < location / 4687 # windSpeed > ;
  sosa:madeBySensor < windSensor / 14 > ;
  sosa:resultTime "2017-04-12T12:00:00Z"^^xsd:dateTime ;
  sosa:hasSimpleResult "47 km/h"^^ < speed > . < observation / 148 > rdf:type sosa:Observation ;
  sosa:observedProperty < location / 4687 # windSpeed > ;
  sosa:madeBySensor < windSensor / 14 > ;
  sosa:resultTime "2017-04-12T12:01:00Z"^^xsd:dateTime ;
  sosa:hasSimpleResult "43 km/h"^^ < speed > .


### B.8 Ice Core

In order to characterize a thing with a large extent, or which is not directly accessible, the usual observational strategy is to obtain one or more samples. Observations may then be made more conveniently on the samples, with the intention
                    of characterizing the larger thing. This intentionality is captured using the property sosa:isSampleOf .

In the following example, the ice core is a sample of the Antarctic ice sheet, and observations are made on the ice core.

A convenient side effect of this feature is that all observations related to the larger thing (the ice sheet) can be found, and then potentially joined together in a meta-analysis in order to characterize that.

An RDF file containing a graph corresponding to this example is available .

@prefix rdf: < http: // www.w3.org / 1999 / 02 / 22-rdf-syntax-ns #> .
@prefix time: < http: // www.w3.org / 2006 / time #> .
@prefix sosa: < http: // www.w3.org / ns / sosa /> .
@prefix ssn: < http: // www.w3.org / ns / ssn /> .
@prefix xsd: < http: // www.w3.org / 2001 / XMLSchema #> .
@prefix geo: < http: // www.w3.org / 2003 / 01 / geo / wgs84_pos #> .
@base < http: // example.org / data /> .


# The CO2 level observed in an ice core is 240 parts per million.
# the ice core is a sample of the polar ice sheet of Antarctica. < http: // dbpedia.org / resource / Antarctic_ice_sheet > a sosa:FeatureOfInterest ;
  sosa:hasSample < iceCore / 12 > , < iceCore / 13 > , < iceCore / 14 > . < iceCore / 12 > rdf:type sosa:Sample ;
  sosa:isSampleOf < http: // dbpedia.org / resource / Antarctic_ice_sheet > ;
  sosa:isResultOf < WellDrilling / 4578 > ;
  sosa:madeBySampler < thermalDrill / 2 > . < WellDrilling / 4578 > a sosa:Sampling ;
    geo:lat -73.35 ; 
    geo:long 9.32 ;
    sosa:hasResult < iceCore / 12 > ;
    sosa:madeBySampler < thermalDrill / 2 > ;
    sosa:resultTime "2017-04-03T11:12:00Z"^^xsd:dateTime ;
    sosa:hasFeatureOfInterest < http: // dbpedia.org / resource / Antarctic_ice_sheet > . < iceCore / 12 # observation > a sosa:Observation ;
  sosa:observedProperty < iceCore / 12 # CO2 > ;
  sosa:hasSimpleResult 240 .

# using SSN one can explicitly state that < iceCore / 12 # CO2 > is the property of < iceCore / 12 > . < iceCore / 12 # CO2 > ssn:isPropertyOf < iceCore / 12 > .

An RDF file containing a graph corresponding to this example is available .

@prefix rdf: < http: // www.w3.org / 1999 / 02 / 22-rdf-syntax-ns #> .
@prefix time: < http: // www.w3.org / 2006 / time #> .
@prefix sosa: < http: // www.w3.org / ns / sosa /> .
@prefix xsd: < http: // www.w3.org / 2001 / XMLSchema #> .
@prefix geo: < http: // www.w3.org / 2003 / 01 / geo / wgs84_pos #> .
@base < http: // example.org / data /> .


# The CO2 level observed in an ice core is 240 parts per million.
# the ice core is a sample of the polar ice sheet of Antarctica. < http: // dbpedia.org / resource / Antarctic_ice_sheet > a sosa:FeatureOfInterest ;
  sosa:hasSample < iceCore / 12 > , < iceCore / 13 > , < iceCore / 14 > . < iceCore / 12 > rdf:type sosa:Sample ;
  sosa:isSampleOf < http: // dbpedia.org / resource / Antarctic_ice_sheet > ;
  sosa:isResultOf < WellDrilling / 4578 > ;
  sosa:madeBySampler < thermalDrill / 2 > . < WellDrilling / 4578 > a sosa:Sampling ;
    geo:lat -73.35 ; 
    geo:long 9.32 ;
    sosa:hasResult < iceCore / 12 > ;
    sosa:madeBySampler < thermalDrill / 2 > ;
    sosa:resultTime "2017-04-03T11:12:00Z"^^xsd:dateTime ;
    sosa:hasFeatureOfInterest < http: // dbpedia.org / resource / Antarctic_ice_sheet > . < iceCore / 12 # observation > a sosa:Observation ;
  sosa:observedProperty < iceCore / 12 # CO2 > ;
  sosa:hasSimpleResult 240 .


### B.9 DHT22 Description

An RDF file containing a graph corresponding to this example is available .

@prefix rdf: < http: // www.w3.org / 1999 / 02 / 22-rdf-syntax-ns #> .
@prefix rdfs: < http: // www.w3.org / 2000 / 01 / rdf-schema #> .
@prefix xsd: < http: // www.w3.org / 2001 / XMLSchema #> .
@prefix qudt-1-1: < http: // qudt.org / 1.1 / schema / qudt #> .
@prefix qudt-unit-1-1: < http: // qudt.org / 1.1 / vocab / unit #> .
@prefix schema: < http: // schema.org /> .

@prefix sosa: < http: // www.w3.org / ns / sosa /> .
@prefix ssn: < http: // www.w3.org / ns / ssn /> .
@prefix ssn-system: < http: // www.w3.org / ns / ssn / systems /> .

@prefix rdfp: < https: // w3id.org / rdfp /> .

@base < http: // example.org / data /> . < DHT22#Procedure > a sosa:Procedure ;
  ssn:hasOutput < DHT22#output > . < DHT22#output > a ssn:Output , rdfp:GraphDescription ;
  rdfs:comment "The output is a RDF Graph that describes both the temperature and the humidity. It can be validated by a SHACL shapes graph."@en ;
  rdfp:presentedBy [
    a rdfp:GraphDescription ;
    rdfp:validationRule < shacl_shapes_graph > ;
  ] . < DHT22 / 4578 > a ssn:System ;
  rdfs:comment "DHT22 sensor #4578 contains a humidity and a temperature sensor."@en ;
  rdfs:seeAlso < https: // www.sparkfun.com / datasheets / Sensors / Temperature / DHT22.pdf > ;
  ssn:hasSubSystem < DHT22 / 4578 # TemperatureSensor > , < DHT22 / 4578 # HumiditySensor > . < DHT22 / 4578 # TemperatureSensor > a sosa:Sensor , ssn:System ;
  rdfs:comment "The embedded temperature sensor, a specific instance of temperature sensor."@en ;
  ssn-system:hasOperatingRange < DHT22 / 4578 # TemperatureSensorOperatingRange > ; 
  ssn-system:hasSystemCapability < DHT22 / 4578 # TemperatureSensorCapability > ;
  ssn:implements < DHT22#Procedure > . < DHT22 / 4578 # HumiditySensor > a sosa:Sensor , ssn:System ;
  rdfs:comment "The embedded humidity sensor, a specific instance of humidity sensor."@en ;
  ssn-system:hasOperatingRange < DHT22 / 4578 # HumiditySensorOperatingRange > ;
  ssn:implements < DHT22#Procedure > . < DHT22 / 4578 # TemperatureSensorOperatingRange > a ssn-system:OperatingRange ;
  rdfs:comment "The conditions in which the DHT22 temperature sensor is expected to operate."@en ;
  ssn-system:inCondition < NormalTemperatureCondition > , < NormalHumidityCondition > . < DHT22 / 4578 # HumiditySensorOperatingRange > a ssn-system:OperatingRange ;
  rdfs:comment "The conditions in which the DHT22 humidity sensor is expected to operate."@en ;
  ssn-system:inCondition < NormalTemperatureCondition > , < NormalHumidityCondition > . < NormalOperatingCondition > a ssn-system:Condition , schema:PropertyValue ;
  rdfs:comment "A temperature range of -40 to 80 Celsius."@en ;
  schema:minValue -40.0 ;
  schema:maxValue 80.0 ;
  schema:unitCode qudt-unit-1-1:DegreeCelsius . < NormalHumidityCondition > a ssn-system:Condition , schema:PropertyValue ;
  rdfs:comment "A relative humidity range of 5 to 85 %."@en ;
  schema:minValue 5.0 ;
  schema:maxValue 85.0 ;
  schema:unitCode qudt-unit-1-1:Percent . < DHT22 / 4578 # TemperatureSensorCapability > a ssn:Property , ssn-system:SystemCapability , schema:PropertyValue ;
  rdfs:comment "The capabilities of the temperature sensor in normal temperature and humidity conditions." ;
  ssn-system:inCondition < NormalTemperatureCondition > , < NormalHumidityCondition > ;
  ssn-system:hasSystemProperty < DHT22 / 4578 # TemperatureSensorAccuracy > , < DHT22 / 4578 # TemperatureSensorSensitivity > , < DHT22 / 4578 # TemperatureSensorRepeatability > , < DHT22 / 4578 # TemperatureSensorFrequency > . < DHT22 / 4578 # TemperatureSensorAccuracy > a ssn:Property , ssn-system:Accuracy , schema:PropertyValue ;
  rdfs:comment "The accuracy of the temperature sensor is +-0.5 °C in normal temperature and humidity conditions."@en ;
  schema:minValue -0.5 ;
  schema:maxValue 0.5 ;
  schema:unitCode qudt-unit-1-1:DegreeCelsius . < DHT22 / 4578 # TemperatureSensorSensitivity > a ssn:Property , ssn-system:Sensitivity , ssn-system:Resolution , schema:PropertyValue ;
  rdfs:comment "The sensitivity and resolution of the temperature sensor is 0.1 °C in normal temperature and humidity conditions."@en ;
  schema:value 0.1 ;
  schema:unitCode qudt-unit-1-1:DegreeCelsius . < DHT22 / 4578 # TemperatureSensorPrecision > a ssn:Property , ssn-system:Precision , schema:PropertyValue ;
  rdfs:comment "The precision (= repeatability) of the temperature sensor is +-0.2 °C in normal temperature and humidity conditions."@en ;
  schema:minValue 0.2 ;
  schema:maxValue 0.2 ;
  schema:unitCode qudt-unit-1-1:DegreeCelsius . < DHT22 / 4578 # TemperatureSensorFrequency > a ssn:Property , ssn-system:Frequency , schema:PropertyValue ;
  rdfs:comment "The smallest possible time between one observation and the next is 2 s on average."@en ;
  schema:value 2 ;
  schema:unitCode qudt-unit-1-1:Second . < observation / 1087 > rdf:type sosa:Observation ;
  sosa:madeBySensor < DHT22 / 4578 # TemperatureSensor > ;
  sosa:usedProcedure < DHT22#Procedure > ;
  ssn-system:qualityOfObservation < observation / 1087 # quality > ;


# one may classify the quality of observation using some class: < observation / 1087 # quality > rdf:type ex:FairQuality .


# one may use some other ontology to further qualify this quality. < observation / 1087 # quality > ex:evaluatedBy < Tom > ;
  ex:confidenceValue "6"^^xsd:integer;
  rdfs:comment """Tom gave a confidence value of 6 out of 10 on this observation."""@en .

# one may use some quantity ontology.

@prefix qudt-1-1: < http: // qudt.org / 1.1 / schema / qudt #> .
@prefix qudt-unit-1-1: < http: // qudt.org / 1.1 / vocab / unit #> . < observation / 1087 # quality > rdf:type qudt-1-1:Quantity ;
  qudt-1-1:quantityValue [
    rdf:type qudt-1-1:QuantityValue ;
    qudt-1-1:numericValue "98.4"^^xsd:double ;
    qudt-1-1:unit qudt-unit-1-1:Percent ] .

An RDF file containing a graph corresponding to this example is available .

@prefix rdf: < http: // www.w3.org / 1999 / 02 / 22-rdf-syntax-ns #> .
@prefix rdfs: < http: // www.w3.org / 2000 / 01 / rdf-schema #> .
@prefix xsd: < http: // www.w3.org / 2001 / XMLSchema #> .
@prefix qudt-1-1: < http: // qudt.org / 1.1 / schema / qudt #> .
@prefix qudt-unit-1-1: < http: // qudt.org / 1.1 / vocab / unit #> .
@prefix schema: < http: // schema.org /> .

@prefix sosa: < http: // www.w3.org / ns / sosa /> .
@prefix ssn: < http: // www.w3.org / ns / ssn /> .
@prefix ssn-system: < http: // www.w3.org / ns / ssn / systems /> .

@prefix rdfp: < https: // w3id.org / rdfp /> .

@base < http: // example.org / data /> . < DHT22#Procedure > a sosa:Procedure . < DHT22 / 4578 > a sosa:Platform ;
  rdfs:comment "DHT22 sensor #4578 contains a humidity and a temperature sensor."@en ;
  rdfs:seeAlso < https: // www.sparkfun.com / datasheets / Sensors / Temperature / DHT22.pdf > . < DHT22 / 4578 # TemperatureSensor > a sosa:Sensor ;
  sosa:isHostedBy < DHT22 / 4578 > .
  rdfs:comment "The embedded temperature sensor, a specific instance of temperature sensor."@en . < observation / 1087 > a sosa:Observation ;
  sosa:madeBySensor < DHT22 / 4578 # TemperatureSensor > ;
  sosa:usedProcedure < DHT22#Procedure > .


### B.10 DHT22 Deployment

This example shows how the conditions (temperature and humidity) in a room may be measured using one or more sensors. Each sensor observes the conditions in its immediate vicinity, and the values are then used to characterize the room.

In Room 145 one of the walls is external in the building, so there is expected to be a temperature gradient across the room, and there are two sensors on different walls. In room 245 there is one sensor on the south wall. Each of these
                    locations corresponds to a sosa:Sample of the entire room. The wall also serves as a sosa:Platform on which the sensors are mounted.

An RDF file containing a graph corresponding to this example is available .

@prefix rdf: < http: // www.w3.org / 1999 / 02 / 22-rdf-syntax-ns #> .
@prefix rdfs: < http: // www.w3.org / 2000 / 01 / rdf-schema #> .
@prefix xsd: < http: // www.w3.org / 2001 / XMLSchema #> .
@prefix qudt-1-1: < http: // qudt.org / 1.1 / schema / qudt #> .
@prefix qudt-unit-1-1: < http: // qudt.org / 1.1 / vocab / unit #> .
@prefix schema: < http: // schema.org /> .

@prefix sosa: < http: // www.w3.org / ns / sosa /> .
@prefix ssn: < http: // www.w3.org / ns / ssn /> .
@prefix ssn-system: < http: // www.w3.org / ns / ssn / systems /> .

@base < http: // example.org / data /> . < Room145 > a sosa:FeatureOfInterest ;
  rdfs:label "Room #145"@en ;
  sosa:hasSample < Room145 / east > ;
  sosa:hasSample < Room145 / south > . < Room145 / east > a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
    rdfs:label "East wall of room #145."@en ;
    rdfs:comment "This wall hosts PCB Board 1 with DHT22 temperature and humidity sensor #4578."@en ;
    sosa:hosts < PCBBoard1 > . < Room145 / south > a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
    rdfs:label "South wall of room #145."@en ;
    rdfs:comment "This wall hosts PCB Board 2 with DHT22 temperature and humidity sensor #4579."@en ;
    sosa:hosts < PCBBoard2 > . < Room245 > a sosa:FeatureOfInterest ;
  rdfs:label "Room #245"@en ;
  sosa:hasProperty < Room245#temperature > , < Room245#humidity > ;
  sosa:hasSample < Room245 / south > . < Room245 / south > a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
    rdfs:label "South wall of room #245."@en ;
    sosa:hosts < PCBBoard3 > . < PCBBoard1 > a ssn:System , sosa:Platform ;
  rdfs:label "PCB Board 1"@en ;
  rdfs:comment "PCB Board 1 hosts DHT22 temperature and humidity sensor #4578 permanently, one can say it has it as one of its subsystems."@en ;
  sosa:hosts < DHT22 / 4578 > ;
  ssn:hasSubSystem < DHT22 / 4578 > . < DHT22 / 4578 > a ssn:System ;
    rdfs:label "DHT22 sensor #4578"@en ;
    sosa:isHostedBy < PCBBoard1 > . < PCBBoard2 > a ssn:System , sosa:Platform ;
  rdfs:label "PCB Board 2"@en ;
  rdfs:comment "PCB Board 2 hosts DHT22 temperature and humidity sensor #4579 permanently, one can say it has it as one of its subsystems."@en ;
  sosa:hosts < DHT22 / 4578 > ;
  ssn:hasSubSystem < DHT22 / 4578 > . < DHT22 / 4579 > a ssn:System ;
    rdfs:label "DHT22 sensor #4579."@en ;
    sosa:isHostedBy < PCBBoard2 > . < PCBBoard3 > a ssn:System , sosa:Platform ;
  rdfs:label "PCB Board 3"@en ;
  rdfs:comment "PCB Board 3 hosts DHT22 temperature and humidity sensor #4580 permanently, one can say it has it as one of its subsystems."@en ;
  sosa:hosts < DHT22 / 4578 > ;
  ssn:hasSubSystem < DHT22 / 4578 > . < DHT22 / 4580 > a ssn:System ;
    rdfs:label "DHT22 sensor #4580."@en ;
    sosa:isHostedBy < PCBBoard3 > . < Room245Deployment > a ssn:Deployment ;
  rdfs:comment "Deployment of PCB Board 3 on the south wall of room #245 for the purpose of observing the temperature and humidity of room #245."@en ;
  ssn:deployedOnPlatform < Room245 / south > ;
  ssn:deployedSystem < PCBBoard3 > ;
  ssn:forProperty < Room245#temperature > , < Room245#humidity > . < Room145Deployment > a ssn:Deployment ;
  rdfs:comment "Deployment of PCB Board 1 and 2 on the east and south wall of room #145, respectively, for the purpose of observing the temperature and humidity of room #145."@en ;
  ssn:deployedOnPlatform < Room245 / east > , < Room245 / south > ;
  ssn:deployedSystem < PCBBoard1 > , < PCBBoard2 > ;
  ssn:forProperty < Room145#temperature > , < Room145#humidity > .

An RDF file containing a graph corresponding to this example is available .

@prefix rdf: < http: // www.w3.org / 1999 / 02 / 22-rdf-syntax-ns #> .
@prefix rdfs: < http: // www.w3.org / 2000 / 01 / rdf-schema #> .
@prefix xsd: < http: // www.w3.org / 2001 / XMLSchema #> .
@prefix qudt-1-1: < http: // qudt.org / 1.1 / schema / qudt #> .
@prefix qudt-unit-1-1: < http: // qudt.org / 1.1 / vocab / unit #> .
@prefix schema: < http: // schema.org /> .

@prefix sosa: < http: // www.w3.org / ns / sosa /> .

@base < http: // example.org / data /> . < Room145 > a sosa:FeatureOfInterest ;
  rdfs:label "Room #145"@en ;
  sosa:hasSample < Room145 / east > ;
  sosa:hasSample < Room145 / south > . < Room145 / east > a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
    rdfs:label "East wall of room #145."@en ;
    rdfs:comment "This wall hosts PCB Board 1 with DHT22 temperature and humidity sensor #4578."@en ;
    sosa:hosts < PCBBoard1 > . < Room145 / south > a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
    rdfs:label "South wall of room #145."@en ;
    rdfs:comment "This wall hosts PCB Board 2 with DHT22 temperature and humidity sensor #4579."@en ;
    sosa:hosts < PCBBoard2 > . < Room245 > a sosa:FeatureOfInterest ;
  rdfs:label "Room #245"@en ;
  sosa:hasProperty < Room245#temperature > , < Room245#humidity > ;
  sosa:hasSample < Room245 / south > . < Room245 / south > a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
    rdfs:label "South wall of room #245."@en ;
    sosa:hosts < PCBBoard3 > . < PCBBoard1 > a sosa:Platform ;
  rdfs:label "PCB Board 1"@en ;
  rdfs:comment "PCB Board 1 hosts DHT22 temperature and humidity sensor #4578 permanently."@en ;
  sosa:hosts < DHT22 / 4578 > . < DHT22 / 4578 > a sosa:Platform ;
    rdfs:label "DHT22 sensor #4578"@en ;
    sosa:isHostedBy < PCBBoard1 > . < PCBBoard2 > a sosa:Platform ;
  rdfs:label "PCB Board 2"@en ;
  rdfs:comment "PCB Board 2 hosts DHT22 temperature and humidity sensor #4579 permanentlys."@en ;
  sosa:hosts < DHT22 / 4578 > . < DHT22 / 4579 > a sosa:Platform ;
    rdfs:label "DHT22 sensor #4579."@en ;
    sosa:isHostedBy < PCBBoard2 > . < PCBBoard3 > a sosa:Platform ;
  rdfs:label "PCB Board 3"@en ;
  rdfs:comment "PCB Board 3 hosts DHT22 temperature and humidity sensor #4580 permanently."@en ;
  sosa:hosts < DHT22 / 4578 > . < DHT22 / 4580 > a sosa:Platform ;
    rdfs:label "DHT22 sensor #4580."@en ;
    sosa:isHostedBy < PCBBoard3 > .


### B.11 IP68 Smart Sensor

This example describes the IP68 Smart Sensor that and some of its capabilities and operating ranges. A specific IP68 Smart Sensor observes the air temperature, and its own battery state.

An RDF file containing a graph corresponding to this example is available .

@prefix rdf: < http: // www.w3.org / 1999 / 02 / 22-rdf-syntax-ns #> .
@prefix geo: < http: // www.w3.org / 2003 / 01 / geo / wgs84_pos #> .
@prefix gr: < http: // purl.org / goodrelations / v1 #> .
@prefix org: < http: // www.w3.org / ns / org #> .
@prefix schema: < http: // schema.org /> .
@prefix sosa: < http: // www.w3.org / ns / sosa /> .
@prefix ssn: < http: // www.w3.org / ns / ssn /> .
@prefix ssn-system: < http: // www.w3.org / ns / ssn / systems /> .
@prefix qudt-unit-1-1: < http: // qudt.org / vocab / unit #> .
@prefix prov: < http: // www.w3.org / ns / prov #> .
@prefix owl: < http: // www.w3.org / 2002 / 07 / owl #> .
@prefix seas: < https: // w3id.org / seas /> .
@prefix cdt: < http: // w3id.org / lindt / custom_datatypes #> .

@base < https: // data.grandlyon.com /> . < Organization / 1 > a org:Organization ;
    owl:sameAs < http: // dbpedia.org / page / Metropolis_of_Lyon > . < Air > a sosa:FeatureOfInterest ;
  rdfs:label "The air."@en . < IP68_Outdoor_Temperature_Sensor > a owl:Class , gr:ProductOrServiceModel ;
  gr:name "IP68 Outdoor Temperature Sensor"@en ;
  rdfs:label "IP68 Outdoor Temperature Sensor"@en ;
  rdfs:subClassOf [
    owl:onProperty ssn-system:hasOperatingRange ;
    owl:hasValue < IP68_Outdoor_Temperature_Sensor#operatingRange > ] ;
  rdfs:subClassOf [
    owl:onProperty ssn-system:hasSystemCapability ;
    owl:hasValue < IP68_Outdoor_Temperature_Sensor#systemCapability > ] . < IP68_Outdoor_Temperature_Sensor#operatingRange > a ssn-system:OperatingRange , ssn:Property ;
  ssn-system:inCondition < IP68_Outdoor_Temperature_Sensor#normalOperatingCondition > . < IP68_Outdoor_Temperature_Sensor#normalOperatingCondition > a ssn-system:Condition , schema:PropertyValue ;
  rdfs:comment "A temperature range of -20 to 70 Celsius."@en ;
  schema:minValue -20.0 ;
  schema:maxValue 70.0 ;
  schema:unitCode qudt-unit-1-1:DegreeCelsius . < IP68_Outdoor_Temperature_Sensor#systemCapability > a ssn:Property , ssn-system:SystemCapability ;
  rdfs:comment "The sensor capability in normal operating conditions."@en ;
  ssn-system:hasSystemProperty < IP68_Outdoor_Temperature_Sensor#RFSensitivity > , < IP68_Outdoor_Temperature_Sensor#TemperatureAccuracy > , < IP68_Outdoor_Temperature_Sensor#TemperatureResolution > , < IP68_Outdoor_Temperature_Sensor#BatteryAccuracy > , < IP68_Outdoor_Temperature_Sensor#BatteryResolution > ;
  ssn-system:inCondition < IP68_Outdoor_Temperature_Sensor#normalOperatingCondition > . < IP68_Outdoor_Temperature_Sensor#RFSensitivity > a ssn:Property , ssn-system:Sensitivity , schema:PropertyValue ;
  schema:value -137 ;
  schema:unitCode qudt-unit-1-1:DecibelReferredToOneMilliwatt . < IP68_Outdoor_Temperature_Sensor#TemperatureAccuracy > a ssn:Property , ssn-system:Accuracy , schema:PropertyValue ;
  ssn:forProperty < Air?lat=45.75&long=4.85#temperature > ;
  schema:minValue -0.2 ;
  schema:maxValue 0.2 ;
  schema:unitCode qudt-unit-1-1:DegreeCelsius . < IP68_Outdoor_Temperature_Sensor#TemperatureResolution > a ssn:Property , ssn-system:Resolution , schema:PropertyValue ;
  ssn:forProperty < Air?lat=45.75&long=4.85#temperature > ;
  schema:value 0.0625 ;
  schema:unitCode qudt-unit-1-1:DegreeCelsius . < IP68_Outdoor_Temperature_Sensor#BatteryResolution > a ssn:Property , ssn-system:Resolution , schema:PropertyValue ;
  ssn:forProperty < Sensor / SL-T-P1 # battery > ;
  schema:value 3.937e-3 ;
  schema:unitCode qudt-unit-1-1:Percent . < Air?lat=45.75&long=4.85 > a sosa:Sample ;
  rdfs:label "The air at lat 45.75 and long 4.85."@en ;
  sosa:isSampleOf < Air > ;
  ssn:hasProperty < Air?lat=45.75&long=4.85#temperature > . < Air?lat=45.75&long=4.85#temperature > a ssn:Property , sosa:ObservableProperty ;
  ssn:isPropertyOf < Air?lat=45.75&long=4.85 > . < Sensor / SL-T-P1 > a gr:ProductOrService, sosa:Sensor , seas:LoRaCommunicationDevice , < IP68_Outdoor_Temperature_Sensor > ;
    gr:hasBrand [ a gr:Brand ; gr:name "Sensing Labs"@en ] ;
    geo:alt 100.0 ;
    geo:lat 45.75 ;
    geo:lon 4.85 ;
    ssn:implements < IP68_Outdoor_Temperature_Sensor#temperatureSensingProcedure > ;
    ssn:implements < IP68_Outdoor_Temperature_Sensor#batterySensingProcedure > ;
    ssn:observes < Sensor / SL-T-P1 # battery > ;
    ssn:observes < Air?lat=45.75&long=4.85#temperature > . < Deployment / SL-T-P1 / 2017-06-06 > a ssn:Deployment ;
  ssn:deployedSystem < Sensor / SL-T-P1 > ;
  prov:startedAtTime "2017-06-06"^^xsd:date ;
  prov:wasAssociatedWith < Organization / 1 > ;
  ssn:deployedOnPlatform < Tree / 1 > . < Observation / 5872357 # temperature > a sosa:Observation ;
    sosa:hasSimpleResult "64.5244681928429 Cel"^^cdt:ucum ;
    sosa:madeBySensor < Sensor / SL-T-P1 > ;
    sosa:hasFeatureOfInterest < Air?lat=45.75&long=4.85 > ;
    sosa:observedProperty < Air?lat=45.75&long=4.85#temperature > ;
    sosa:resultTime "2017-06-20T21:49:18+00:00"^^xsd:dateTime . < Observation / 5872357 # battery > a sosa:Observation ;
    sosa:hasSimpleResult "73.2 %"^^cdt:ucum ;
    sosa:madeBySensor < Sensor / SL-T-P1 > ;
    sosa:hasFeatureOfInterest < Sensor / SL-T-P1 > ;
    sosa:observedProperty < Sensor / SL-T-P1 # battery > ;
    sosa:resultTime "2017-06-20T21:49:18+00:00"^^xsd:dateTime .


### B.12 Examples from O&M

An XML implementation of the Observations and Measurements specification is available from OGC [ OandM ], known as [ OMXML ]. Annex C in
                that document contains a large set of examples. To assist users of O&M to understand SOSA/SSN, and potentially to migrate services based on OMXML to SOSA/SSN, an RDF file containing a graph corresponding to the OMXML examples is provided .

Note that in some cases the information contained in the OMXML examples goes beyond what is supported directly by SOSA/SSN, so the examples use terms from some other well known RDF vocabularies, such as [ GeoSPARQL ],
                [ QUDT ], [ owl-time ], and [ prov-o ], as well as the sample relations module. In some cases these only approximate the semantics of the OMXML examples. This is indicated in editorial notes embedded in the RDF file. In a few places where there was no well-known RDF implementation matching the requirements,
                the details have been omitted.


## C. Acknowledgments


## D. Change History

A full change-log is available on GitHub .


## Changes since Original (https://www.w3.org/2005/Incubator/ssn/XGR-ssn-20110628/)

The DUL ontology, that was imported in SSN, is no longer imported and all axioms using terms from DUL have been removed from SSN and collected in the DUL-SSN alignment module.

The namespace was changed to match the planned namespace for this publication.

The modularization as presented here, including the core, is entirely new.


## Changes since 1st Public Working Draft (http://www.w3.org/TR/2016/WD-vocab-ssn-20160531/)

Correction to include some SSN terms that were unintentionally dropped from the FPWD. Correction to remove an asserted subclass of owl:Thing that was introduced into FPWD (these were both by-products of the DUL removal).

Correction to some https namespace usage that crept into the FPWD.

Transition to the new namespace used by the DUL module.

Inclusion of the DUL alignment and the old SSN (of the SSN-XG) alignment.

ssn:Sensor has been changed to be a subclass of dul:Object instead of dul:Physical Object.

Various typography and spelling errors and consistency of expression in annotation properties have been improved. These do not induce any changes in the intended meaning of the terms.

Specgen 6 has been used to generate the ontology documentation. The popular sketch of SSN structure has been removed.

Object properties ssn:isValueOf, ssn:produces and ssn:featureInObservation, along with a propertychain subproperty of produces and another propertychain subproperty of hasProperty, were introduced unintentionally in the FPWD.


### Changes since 2nd Public Working Draft (https://www.w3.org/TR/2017/WD-vocab-ssn-20170105/)

Changed meta prefix declaration to schema

Added voaf:Vocabulary class to ontology instances

Added dcterms:license statements

Added vann:preferredNamespacePrefix and vann:preferredNamespaceUri statements

Added SOSA and SSN alignment

Added SSN/SOSA alignments with O&M

Consistently added Capitalization of all ontology terms in all rdfs:comments

Addressed naming inconsistency with changes in name to isObservedBy/observes, madeBySensor/madeObservation

Use skos:examples to describe examples of classes/properties

Removed history skos:historyNote

SOSA-specific changes: Various typography and spelling errors and consistency of expression in annotation properties have been improved Added "sosa:hasResult meta:domainIncludes sosa:Actuation" and "sosa:isResultOf meta:rangeIncludes sosa:Actuation" Changed the defintion of FeatureofInterest to account for actuators Introduced sosa:actsOnProperty and its inverse property sosa:isActedOnBy Added madeBySensor property Renamed invokes and invokedBy to madeActuation and madeByActuator Changed hostedBy to isHostedBy Added Sampler (device) and Sampling (act) to SOSA Added madeSampling and madeBySampler properties Added Sample to range of hasResult, and to domain or isResultOf Added hasSimpleResult and hasResult instead of hasValue Added ObservableProperty and ActuatableProperty Changed rdfs:comment and skos:definition of sosa:Platform Refined sosa:Result Changed sosa:madeByActuator to sosa:actuationMadeBy Added schema:domainIncludes sosa:Sampling to sosa:observedProperty Added schema:rangeIncludes time:TemporalEntity and schema:domainIncludes sosa:Sampling to sosa:phenomenonTime Changed sosa:actuationMadeBy to sosa:madeByActuator

Various typography and spelling errors and consistency of expression in annotation properties have been improved

Added "sosa:hasResult meta:domainIncludes sosa:Actuation" and "sosa:isResultOf meta:rangeIncludes sosa:Actuation"

Changed the defintion of FeatureofInterest to account for actuators

Introduced sosa:actsOnProperty and its inverse property sosa:isActedOnBy

Added madeBySensor property

Renamed invokes and invokedBy to madeActuation and madeByActuator

Changed hostedBy to isHostedBy

Added Sampler (device) and Sampling (act) to SOSA

Added madeSampling and madeBySampler properties

Added Sample to range of hasResult, and to domain or isResultOf

Added hasSimpleResult and hasResult instead of hasValue

Added ObservableProperty and ActuatableProperty

Changed rdfs:comment and skos:definition of sosa:Platform

Refined sosa:Result

Changed sosa:madeByActuator to sosa:actuationMadeBy

Added schema:domainIncludes sosa:Sampling to sosa:observedProperty

Added schema:rangeIncludes time:TemporalEntity and schema:domainIncludes sosa:Sampling to sosa:phenomenonTime

Changed sosa:actuationMadeBy to sosa:madeByActuator

SSN-specific changes: Changed syntax and layout in the alignment to SSN of the SSN-XG Refine ssn:Property: ObservableProperty in sosa, Property in ssn, old SSN Property equivalent with ssn:Property Import sosa: "ssn: a owl:Ontology ; owl:imports sosa:." Update prefix for featureOfInterest in ssn:Observation and ssn:Property definition Added skos:examples to several rdfs:comments Changed sub class relation of Accuracy from ssn:MeasurementProperty to ssn:SystemProperty Changed sub class of ssn:Deployment from DeploymentRelatedProcess to DeploymentRelatedProcedure Changed DeploymentRelatedProcess Class to DeploymentRelatedProcedure Changed sub class of ssn:DetectionLimit from ssn:MeasurementProperty to ssn:SystemProperty Deprecated the ssn:Device class Changed sub class of ssn:Drift from ssn:MeasurementProperty to ssn:SystemProperty Changed the rdfs:comment of ssn:Drift to include Actuators Changed sub class of ssn:Frequency from ssn:MeasurementProperty to ssn:SystemProperty Changed sub class of ssn:Latency from ssn:MeasurementProperty to ssn:SystemProperty Changed the rdfs:comment of ssn:Latency to include Actuators Changed the rdfs:comment of ssn:MaintenanceSchedule to reference the System class only Changed MeasurementCapability to SystemCapability and changed its axiom from hasMeasurementProperty to hasSystemProperty Changed MeasurementProperty to SystemProperty Changed sub class of ssn:MeasurementRange from ssn:MeasurementProperty to ssn:SystemProperty and changed its rdfs:comment Changed the Observation’s classes qualified property restriction from ssn:featureOfInterest to sosa:hasFeatureOfInterest and ssn:FeatureOfInterest to sosa:FeatureOfInterest Changed the Observation’s class universal property restrictions from ssn:observationResult to sosa:hasResult and ssn:SensorOutput to sosa:Result Changed the Observation’s class universal property restriction from ssn:observedProperty to sosa:observedProperty and ssn:ObservedProperty to sosa:ObservableProperty Changed the Observation’s class qualified property restriction from ssn:observedProperty to sosa:observedProperty and ssn:ObservedProperty to sosa:ObservableProperty Changed the Observation’s class qualified property restrictions from ssn:observedBy to sosa:madeBySensor and ssn:Sensor to sosa:Sensor Changed the Observation’s class universal property restrictions from ssn:sensingMethodUsed to sosa:usedProcedure and sosa:usedProcedure Changed the Observation’s class qualified property restrictions from ssn:sensingMethodUsed to sosa:usedProcedure and sosa:usedProcedure Changed the minimum cardinality restriction on the Observation class from ssn:observationSamplingTime to sosa:resultTime Removed ssn:ObservationValue Class Changed rdfs:comment of ssn:OperatingPowerRange Changed rdfs:comment of ssn:OperatingProperty Changed rdfs:comment of ssn:OperatingRange Changed rdfs:comment of ssn:Output Changed the Platform’s class universal property restrictions from ssn:attachedSystem Changed sub class of ssn:Precision from ssn:MeasurementProperty to ssn:SystemProperty Changed ssn:Process to sosa:Procedure Changed rdfs:comment for ssn:Property Changed the Property’s class existential property restrictions class range from ssn:FeatureOfInterest to sosa:FeatureOfInterest Changed rdfs:comment for ssn:Resolution Changed sub class of ssn:Resolution from ssn:MeasurementProperty to ssn:SystemProperty Changed rdfs:comment for ssn:ResponseTime Changed sub class of ssn:ResponseTime from ssn:MeasurementProperty to ssn:SystemProperty Changed rdfs:comment for ssn:Selectivity Changed sub class of ssn:Selectivitye from ssn:MeasurementProperty to ssn:SystemProperty Removed ssn:Sensing Class Removed ssn:SensingDevice Class Changed the Sensor classes existential property restrictions from ssn:hasMeasurementCapability to ssn:SystemCapability and ssn:MeasurementCapability to ssn:SystemCapability Changed the Sensor classes universal property restriction on ssn:observes to sosa:observes Changed the Sensor classes existential property restrictions range class from ssn:Sensing to sosa:Procedure Removed ssn:SensorDataSheet Class Removed ssn:SensorInput Class Removed ssn:SensorOutput Class Changed rdfs:comment for ssn:Stimulus Changed rdfs:comment for ssn:SurvivalProperty Changed rdfs:comment for ssn:SurvivalRange Changed rdfs:comment for ssn:System Changed the System’s class universal property restriction from ssn:onPlatform to sosa:isHostedBy and ssn:Platform to sosa:Platform Added a universal property restriction to the System’s class on the hasSystemCapability property with a class range of SystemCapability Changed rdfs:comment for ssn:SystemLifetime Added Property Restrictions to SOSA:ActuatableProperty for sosa:isActedOnBy Added Property Restrictions to SOSA:Actuation for sosa:hasFeatureOfInterest, sosa:hasResult, sosa:resultTime, sosa:usedProcedure, sosa:hasFeatureOfInterest and sosa:actuationMadeBy Added ssn:ActuationRange Class Added Property Restrictions to sosa:Actuator for ssn:implements, ssn:forProperty and sosa:MadeActuation and sosa:hasResult Removed ssn:DeploymentRelatedProcess Added Property Restrictions to ssn:Input for ssn:hasInput Added Property Restriction to ssn:MeasurementRange Added Property Restrictions to sosa:ObservableProperty for isObservedBy, inverseOf sosa:observedProperty and inverseOf ssn:isProxyFor Added Property Restrictions to ssn:OperatingProperty Added Property Restrictions to ssn:Precision Added Property Restrictions to sosa:Result Added Property Restrictions to sosa:Sample Added Property Restrictions to sosa:Sampler Added Property Restrictions to sosa:Sampling Added Property Restrictions to ssn:SystemProperty Added sub class of System relation to sosa:Sensor Added Property Restrictions to ssn:Stimulus Added Property Restrictions to ssn:SurvivalProperty Added Property Restrictions to ssn:SurvivalRange Added Property Restrictions to ssn:System Removed attachedSystem property Changed rdfs:comment for ssn:deployedOnPlatform Removed ssn:deploymentProcessPart Changed rdfs:comment for ssn:detects Removed ssn:featureOfInterest property Changed rdfs:comment for ssn:forProperty and added a skos:example property Changed rdfs:comment for ssn:hasDeployment Renamed ssn:hasMeasurementCapability to ssn:hasSystemCapability and changed its rdf:comment Renamed ssn:hasMeasurementProperty to ssn:hasSystemProperty and changed its rdf:comment Changed rdfs:comment for ssn:hasOperatingProperty Changed rdfs:comment for ssn:hasSurvivalProperty Changed rdfs:comment for ssn:hasSurvivalRange Changed rdfs:comment for ssn:implementedBy Changed rdfs:comment for ssn:implements Changed rdfs:comment for ssn:inCondition and added skos:example property Changed rdfs:comment for ssn:inDeployment and added skos:example property Removed ssn:isProducedBy property Changed rdfs:comment for ssn:isPropertyOf Changed rdfs:comment for ssn:isProxyFor and added skos:example property Removed ssn:madeObservation property Removed ssn:observationResult property Removed ssn:observationResultTime property Removed ssn:observationSamplingTime property Removed ssn:observedProperty property Changed ssn:observes to sosa:observes, removed sub-property chain for sosa:observes and defined it as sub-property of ssn:forProperty Removed ssn:ofFeature property Removed ssn:onPlatform property Changed rdfs:comment for ssn:qualityOfObservation Removed ssn:sensingMethodUsed property Added rdfs:comment for ssn:hasInput Changed sosa:Platform subclass of dul:PhysicalObject Removed axiom FunctionalProperty(ssn:isPropertyOf) to account for generic modeling of ssn:Property such as ex:Temperature

Changed syntax and layout in the alignment to SSN of the SSN-XG

Refine ssn:Property: ObservableProperty in sosa, Property in ssn, old SSN Property equivalent with ssn:Property

Import sosa: "ssn: a owl:Ontology ; owl:imports sosa:."

Update prefix for featureOfInterest in ssn:Observation and ssn:Property definition

Added skos:examples to several rdfs:comments

Changed sub class relation of Accuracy from ssn:MeasurementProperty to ssn:SystemProperty

Changed sub class of ssn:Deployment from DeploymentRelatedProcess to DeploymentRelatedProcedure

Changed DeploymentRelatedProcess Class to DeploymentRelatedProcedure

Changed sub class of ssn:DetectionLimit from ssn:MeasurementProperty to ssn:SystemProperty

Deprecated the ssn:Device class

Changed sub class of ssn:Drift from ssn:MeasurementProperty to ssn:SystemProperty

Changed the rdfs:comment of ssn:Drift to include Actuators

Changed sub class of ssn:Frequency from ssn:MeasurementProperty to ssn:SystemProperty

Changed sub class of ssn:Latency from ssn:MeasurementProperty to ssn:SystemProperty

Changed the rdfs:comment of ssn:Latency to include Actuators

Changed the rdfs:comment of ssn:MaintenanceSchedule to reference the System class only

Changed MeasurementCapability to SystemCapability and changed its axiom from hasMeasurementProperty to hasSystemProperty

Changed MeasurementProperty to SystemProperty

Changed sub class of ssn:MeasurementRange from ssn:MeasurementProperty to ssn:SystemProperty and changed its rdfs:comment

Changed the Observation’s classes qualified property restriction from ssn:featureOfInterest to sosa:hasFeatureOfInterest and ssn:FeatureOfInterest to sosa:FeatureOfInterest

Changed the Observation’s class universal property restrictions from ssn:observationResult to sosa:hasResult and ssn:SensorOutput to sosa:Result

Changed the Observation’s class universal property restriction from ssn:observedProperty to sosa:observedProperty and ssn:ObservedProperty to sosa:ObservableProperty

Changed the Observation’s class qualified property restriction from ssn:observedProperty to sosa:observedProperty and ssn:ObservedProperty to sosa:ObservableProperty

Changed the Observation’s class qualified property restrictions from ssn:observedBy to sosa:madeBySensor and ssn:Sensor to sosa:Sensor

Changed the Observation’s class universal property restrictions from ssn:sensingMethodUsed to sosa:usedProcedure and sosa:usedProcedure

Changed the Observation’s class qualified property restrictions from ssn:sensingMethodUsed to sosa:usedProcedure and sosa:usedProcedure

Changed the minimum cardinality restriction on the Observation class from ssn:observationSamplingTime to sosa:resultTime

Removed ssn:ObservationValue Class

Changed rdfs:comment of ssn:OperatingPowerRange

Changed rdfs:comment of ssn:OperatingProperty

Changed rdfs:comment of ssn:OperatingRange

Changed rdfs:comment of ssn:Output

Changed the Platform’s class universal property restrictions from ssn:attachedSystem

Changed sub class of ssn:Precision from ssn:MeasurementProperty to ssn:SystemProperty

Changed ssn:Process to sosa:Procedure

Changed rdfs:comment for ssn:Property

Changed the Property’s class existential property restrictions class range from ssn:FeatureOfInterest to sosa:FeatureOfInterest

Changed rdfs:comment for ssn:Resolution

Changed sub class of ssn:Resolution from ssn:MeasurementProperty to ssn:SystemProperty

Changed rdfs:comment for ssn:ResponseTime

Changed sub class of ssn:ResponseTime from ssn:MeasurementProperty to ssn:SystemProperty

Changed rdfs:comment for ssn:Selectivity

Changed sub class of ssn:Selectivitye from ssn:MeasurementProperty to ssn:SystemProperty

Removed ssn:Sensing Class

Removed ssn:SensingDevice Class

Changed the Sensor classes existential property restrictions from ssn:hasMeasurementCapability to ssn:SystemCapability and ssn:MeasurementCapability to ssn:SystemCapability

Changed the Sensor classes universal property restriction on ssn:observes to sosa:observes

Changed the Sensor classes existential property restrictions range class from ssn:Sensing to sosa:Procedure

Removed ssn:SensorDataSheet Class

Removed ssn:SensorInput Class

Removed ssn:SensorOutput Class

Changed rdfs:comment for ssn:Stimulus

Changed rdfs:comment for ssn:SurvivalProperty

Changed rdfs:comment for ssn:SurvivalRange

Changed rdfs:comment for ssn:System

Changed the System’s class universal property restriction from ssn:onPlatform to sosa:isHostedBy and ssn:Platform to sosa:Platform

Added a universal property restriction to the System’s class on the hasSystemCapability property with a class range of SystemCapability

Changed rdfs:comment for ssn:SystemLifetime

Added Property Restrictions to SOSA:ActuatableProperty for sosa:isActedOnBy

Added Property Restrictions to SOSA:Actuation for sosa:hasFeatureOfInterest, sosa:hasResult, sosa:resultTime, sosa:usedProcedure, sosa:hasFeatureOfInterest and sosa:actuationMadeBy

Added ssn:ActuationRange Class

Added Property Restrictions to sosa:Actuator for ssn:implements, ssn:forProperty and sosa:MadeActuation and sosa:hasResult

Removed ssn:DeploymentRelatedProcess

Added Property Restrictions to ssn:Input for ssn:hasInput

Added Property Restriction to ssn:MeasurementRange

Added Property Restrictions to sosa:ObservableProperty for isObservedBy, inverseOf sosa:observedProperty and inverseOf ssn:isProxyFor

Added Property Restrictions to ssn:OperatingProperty

Added Property Restrictions to ssn:Precision

Added Property Restrictions to sosa:Result

Added Property Restrictions to sosa:Sample

Added Property Restrictions to sosa:Sampler

Added Property Restrictions to sosa:Sampling

Added Property Restrictions to ssn:SystemProperty

Added sub class of System relation to sosa:Sensor

Added Property Restrictions to ssn:Stimulus

Added Property Restrictions to ssn:SurvivalProperty

Added Property Restrictions to ssn:SurvivalRange

Added Property Restrictions to ssn:System

Removed attachedSystem property

Changed rdfs:comment for ssn:deployedOnPlatform

Removed ssn:deploymentProcessPart

Changed rdfs:comment for ssn:detects

Removed ssn:featureOfInterest property

Changed rdfs:comment for ssn:forProperty and added a skos:example property

Changed rdfs:comment for ssn:hasDeployment

Renamed ssn:hasMeasurementCapability to ssn:hasSystemCapability and changed its rdf:comment

Renamed ssn:hasMeasurementProperty to ssn:hasSystemProperty and changed its rdf:comment

Changed rdfs:comment for ssn:hasOperatingProperty

Changed rdfs:comment for ssn:hasSurvivalProperty

Changed rdfs:comment for ssn:hasSurvivalRange

Changed rdfs:comment for ssn:implementedBy

Changed rdfs:comment for ssn:implements

Changed rdfs:comment for ssn:inCondition and added skos:example property

Changed rdfs:comment for ssn:inDeployment and added skos:example property

Removed ssn:isProducedBy property

Changed rdfs:comment for ssn:isPropertyOf

Changed rdfs:comment for ssn:isProxyFor and added skos:example property

Removed ssn:madeObservation property

Removed ssn:observationResult property

Removed ssn:observationResultTime property

Removed ssn:observationSamplingTime property

Removed ssn:observedProperty property

Changed ssn:observes to sosa:observes, removed sub-property chain for sosa:observes and defined it as sub-property of ssn:forProperty

Removed ssn:ofFeature property

Removed ssn:onPlatform property

Changed rdfs:comment for ssn:qualityOfObservation

Removed ssn:sensingMethodUsed property

Added rdfs:comment for ssn:hasInput

Changed sosa:Platform subclass of dul:PhysicalObject

Removed axiom FunctionalProperty(ssn:isPropertyOf) to account for generic modeling of ssn:Property such as ex:Temperature


### Changes since 3rd Public Working Draft (https://www.w3.org/TR/2017/WD-vocab-ssn-20170504/)

Fixed colouring of O&M module in Figure 1 to be normative

Updated figures in the Axiomatization section

Added examples to Appendix

Added a "at risk" section in Status of This Document section

Reorganized specification sections to have: One non-normative overview section, with links to the examples that showcase the terms in that section The normative specification section Moved ssn:qualityOfObservation, properties related to system capabilities, operating range, and survival range, to horizontal ontology module http://www.w3.org/ns/ssn/systems/ marked at risk

One non-normative overview section, with links to the examples that showcase the terms in that section

The normative specification section

Moved ssn:qualityOfObservation, properties related to system capabilities, operating range, and survival range, to horizontal ontology module http://www.w3.org/ns/ssn/systems/ marked at risk

Added new horizontal module for System Capabilities to Figure 1

Fixed errors in class alignments in Dolce-Ultralite Alignment Module, ssn:Sensor to sosa:Sensor, ssn:FeatureOfInterest to sosa:FeatureOfInterest and sosa:Deployment to ssn:Deployment

Fixed errors in property alignments in Dolce-Ultralite Alignment Module, ssn:usedProcedure to sosa:usedProcedure

Applied consistent use of Manchester OWL Syntax in all axioms in SSN/SOSA

Fixed error in sosa:actsOnProperty axiom of sosa:Actuation, i.e. changed Qualified Cardinality to Minimum Cardinality

Fixed error in the use of Hash URIs and SlashURIs in the System Capabilities module

Combined Location and Forecasting in one section and added an example how to model Quantity Values and Unit of Measures

Added Wide Review Section and Exit Criteria Section

Switched Horizontal Segmentation and Vertical Segmentation sections around

Requested bug fixes to correct the SSN/SOSA alignment to DUL


### Changes since W3C Candidate Recommendation 11 July 2017 (https://www.w3.org/TR/2017/CR-vocab-ssn-20170711/)

Made System Capabilities Module informative as of exit criteria

Fixed wrong link in Origins of SSN and SOSA Section to point to Section 6.1

Added Coal Oil Point Reserve and IP68 Smart Sensor examples

Fixed inconsistency in Fig. 6 & 7, i.e. defined the range of property sosa:isActedOnBy as sosa:Actuation

Removed Features at Risk section

Removed Candidate Recommendation Exit Criteria section


## E. References


### E.1 Normative references


### E.2 Informative references

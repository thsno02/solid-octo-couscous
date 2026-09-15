# LinkML Documentation ¶

Everything you need to know about LinkML , the
Linked Data Modeling Language.

LinkML is a flexible modeling language that allows you to author
schemas in YAML that describe the structure of your data. Additionally, it is a framework for working with and validating data in a variety
of formats (JSON, RDF, TSV), with generators for compiling LinkML
schemas to other frameworks.

LinkML is open source (licensed under the Apache-2.0 license) and community-driven. You can find the code on GitHub .


## Documentation ¶

Contents:

LinkML at a glance Feature: Easy to author schemas Feature: Rich modeling language A bridge between frameworks Feature: Generation of documentation and websites A rapidly growing toolchain We eat our own dogfood! More examples

Feature: Easy to author schemas

Feature: Rich modeling language

A bridge between frameworks

Feature: Generation of documentation and websites

A rapidly growing toolchain

We eat our own dogfood!

More examples

Quick Install Guide Local installation: Use the Python package Alternative: Use the official Docker/OCI image Installation for contributors

Local installation: Use the Python package

Alternative: Use the official Docker/OCI image

Installation for contributors

Tutorial Part 1: Creating your first LinkML schema Part 2: Adding a container object Part 3: Adding constraints and performing validation Part 4: Working with RDF Part 5: Using Python dataclasses Part 6: Enumerations Part 7: Slots and inheritance Part 8: Generating Projects Part 9: Working with SQL databases

Part 1: Creating your first LinkML schema

Part 2: Adding a container object

Part 3: Adding constraints and performing validation

Part 4: Working with RDF

Part 5: Using Python dataclasses

Part 6: Enumerations

Part 7: Slots and inheritance

Part 8: Generating Projects

Part 9: Working with SQL databases

LinkML Schemas Models Schema Element Metadata Inheritance Slots Arrays URIs and Mappings Semantic Enumerations Inlining objects Adding constraints and rules Type designators Subsets Imports Advanced features Mapping schemas to other frameworks Schema Linter Derived models Annotations The metamodel Expression Language

Models

Schema Element Metadata

Inheritance

Slots

Arrays

URIs and Mappings

Semantic Enumerations

Inlining objects

Adding constraints and rules

Type designators

Subsets

Imports

Advanced features

Mapping schemas to other frameworks

Schema Linter

Derived models

Annotations

The metamodel

Expression Language

Working with Data Converting between different representations Data Validation Working with RDF and LinkML CSVs and Tabular Data Python Working with data in SQL Databases

Converting between different representations

Data Validation

Working with RDF and LinkML

CSVs and Tabular Data

Python

Working with data in SQL Databases

Generators Schema Frameworks Linked Data Standards Documentation Generation Language Specific Database Others Feature Dashboard Common

Schema Frameworks

Linked Data Standards

Documentation Generation

Language Specific

Database

Others

Feature Dashboard

Common

How-to Guides LinkML Project Copier Template How to run a collaborative data modeling project How to recognize and work with different structural forms Using yq for querying and manipulating schemas Using JSON-LD How to model quantities and measurements Porting LinkML tools to other programming languages Multidimensional Arrays How to make a property graph schema How to Generate AI prompts Deprecating elements while maintaining PURLs and other URIs Using ontology terms as values in data Implements vs Instantiates vs Inheritance: A Best Practices Guide How to implement skip logic in LinkML

LinkML Project Copier Template

How to run a collaborative data modeling project

How to recognize and work with different structural forms

Using yq for querying and manipulating schemas

Using JSON-LD

How to model quantities and measurements

Porting LinkML tools to other programming languages

Multidimensional Arrays

How to make a property graph schema

How to Generate AI prompts

Deprecating elements while maintaining PURLs and other URIs

Using ontology terms as values in data

Implements vs Instantiates vs Inheritance: A Best Practices Guide

How to implement skip logic in LinkML

Examples of use Introductory Example Example Models INCLUDE Data Coordination Center LinkML Registry Presentations about LinkML

Introductory Example

Example Models

INCLUDE Data Coordination Center

LinkML Registry

Presentations about LinkML

The LinkML Ecosystem Tools that build off or enhance LinkML

Tools that build off or enhance LinkML

LinkML specification

Get Involved Community Meetings Workshops and Presentations Monthly LinkML Office Hours

Community Meetings

Workshops and Presentations

Monthly LinkML Office Hours

FAQ FAQ: General FAQ: Why LinkML FAQ: Modeling FAQ: Tools FAQ: Python FAQ: Getting Help FAQ: Contributing FAQ: Tricky Choices

FAQ: General

FAQ: Why LinkML

FAQ: Modeling

FAQ: Tools

FAQ: Python

FAQ: Getting Help

FAQ: Contributing

FAQ: Tricky Choices


## Metamodel Reference ¶

The LinkML metamodel is itself described in LinkML. This model is
hosted in the linkml-model repository. Each element of the model has a URI of the form https://w3id.org/linkml/<ELEMENT> , shortened to the CURIE linkml:<ELEMENT>

The key schema elements are:

linkml:SchemaDefinition linkml:ClassDefinition linkml:SlotDefinition linkml:TypeDefinition linkml:EnumDefinition

linkml:SchemaDefinition

linkml:ClassDefinition

linkml:ClassDefinition

linkml:SlotDefinition

linkml:SlotDefinition

linkml:TypeDefinition

linkml:TypeDefinition

linkml:EnumDefinition

linkml:EnumDefinition


## Schema Developers ¶

If you are a Python developer looking to use LinkML programmatically to build schemas,
work with data, or integrate LinkML into your applications, this section is for you:

Schema Developers Guide:

CLI linkml linkml config linkml generate linkml lint linkml validate Entrypoints

linkml

linkml config

linkml generate

linkml lint

linkml validate

Entrypoints

Schema Developers Guide Jupyter Notebooks Manipulating Schemas How to Manage Releases of your LinkML Schema SchemaView SchemaBuilder Data Conversion: Loaders and Dumpers Inferring Missing Values Using SQL Databases SQLStore Tool Implementer Guide

Jupyter Notebooks

Manipulating Schemas

How to Manage Releases of your LinkML Schema

SchemaView

SchemaBuilder

Data Conversion: Loaders and Dumpers

Inferring Missing Values

Using SQL Databases

SQLStore

Tool Implementer Guide

Code MetaModel Utils Validator Deprecation Log

MetaModel

Utils

Validator

Deprecation Log

Configuration Sources Keys CLI Examples API

Sources

Keys

CLI

Examples

API


## Maintainers ¶

If you want to contribute to the LinkML framework itself, including bug fixes,
new features, or documentation improvements:

Maintainers Guide:

Maintainers Guide Contribution Guidelines GitHub Organization Contributor Hierarchy CODEOWNERS Deprecations Code of Conduct Generator and Validator Governance

Contribution Guidelines

GitHub Organization

Contributor Hierarchy

CODEOWNERS

Deprecations

Code of Conduct

Generator and Validator Governance


## Indices and tables ¶

Index

Index

Module Index

Module Index

Search Page

Search Page

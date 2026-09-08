
# Mission and Scope

## Mission

The repository is building the evidence base for a pipeline that periodically discovers new papers, blogs, public researcher viewpoints, standards, datasets, benchmarks, incidents, and open implementations; verifies and stores their provenance; then turns them into an evolving knowledge system.

The core research question is not merely “how do we update a knowledge graph?” It is:

> How can knowledge be generated, represented, evaluated, selected, retained, recombined, superseded, retracted, and governed by agents without losing evidence, identity, time, disagreement, or rollback?

## Why the scope is deliberately broad

“Evolution” is a shared mechanism across several fields. Understanding knowledge evolution requires the surrounding lineages:

- recursive self-improvement and self-modification;
- open-ended evolution, quality diversity, novelty, and stepping stones;
- continual learning and stability–plasticity;
- model editing and persistent agent memory;
- automated research and self-driving laboratories;
- ontology, schema, semantic layers, mapping, and source binding;
- evidence, provenance, contradiction, uncertainty, and belief revision;
- evaluator, permission, policy, and rollback governance;
- LLM Wiki as persistent, compiled knowledge organization.

The scope is broad by design, but inclusion is not unlimited. Generic agent frameworks, generic RAG applications, and general graph databases are included only when they expose a mechanism relevant to knowledge evolution or its governance.

## Unit of collection

A collected item is a **source record**, not automatically accepted knowledge. Examples:

- an arXiv paper;
- a journal article;
- a standard or ontology;
- an official methodology page;
- a lab or researcher article;
- a GitHub implementation;
- eventually, a dataset, benchmark version, incident, retraction, or experiment trace.

Each item must preserve canonical identity, source type, verification state, version/snapshot state, rights, classification, linkages, evidence level, governance risks, and collection rationale.

## Unit of future knowledge

The intended durable unit is not a PDF, Markdown page, or bare triple. It is a typed assertion with:

- stable identity;
- assertion kind;
- evidence and source selector;
- temporal and contextual scope;
- uncertainty;
- contradiction links;
- derivation or experiment lineage;
- review and promotion state;
- version, supersession, retraction, and rollback lineage.

LLM Wiki pages will be compiled views over these objects.

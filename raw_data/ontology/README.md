# Ontology and knowledge architecture

Ontology is a first-class substrate of this collection because knowledge cannot evolve safely without an explicit model of identity, meaning, constraints, evidence, time, action and governance.

## Do not collapse these concepts

- **taxonomy / thesaurus**: navigation and terminology; typically lightweight and semi-formal.
- **vocabulary**: reusable identifiers and terms.
- **ontology**: explicit conceptual commitments and, when formalized, axioms and entailments.
- **schema**: structural contract for records, messages, tables or APIs.
- **shape / constraint model**: executable conformance rules for instances.
- **semantic layer**: business-facing meanings mapped to physical data and metrics.
- **data contract**: producer-consumer agreement covering schema, quality, ownership and service levels.
- **operational ontology**: domain model plus source bindings, actions, functions, permissions and decision lineage.

## Recommended architecture

Use a layered **Executable Knowledge Model**, not one monolithic ontology:

1. identity and persistent identifiers;
2. terminology, taxonomy and multilingual labels;
3. conceptual/formal ontology;
4. structural schemas and executable constraints;
5. mappings and source bindings;
6. entities, claims, observations, evidence and uncertainty;
7. temporal, contextual and causal models;
8. actions, processes and decisions;
9. policy, permissions and privacy;
10. versioning, migration, semantic diff, review and rollback;
11. catalog, federation, research-object packaging and observability.

## Palantir interpretation

Palantir Foundry's Ontology is best interpreted as an **operational ontology** or **executable semantic operating model**. It combines semantic elements (objects, properties and links) with kinetic elements (actions and functions), physical-data bindings, dynamic security, applications and a branch/review/merge lifecycle. This is much broader than OWL alone.

An open implementation should therefore compose standards and tools rather than search for one exact replacement:

`OWL/SKOS + SHACL/LinkML + SSSOM/R2RML + NGSI-LD + ODRL/OPA/Cedar + PROV-O/RO-Crate + versioned graph + catalog/lineage`

## Non-negotiable governance rules

- Every object has a stable identity independent of labels and source IDs.
- Observation, assertion, inference, prediction, decision and action are distinct kinds.
- Asserted and inferred statements remain distinguishable.
- Open-world semantics, closed-world validation and application defaults are declared separately.
- Mappings are versioned evidence-bearing objects, never timeless `sameAs` shortcuts.
- Ontology/schema changes are ChangeSets with semantic diff, compatibility class, migration, impact analysis, reviewers and rollback.
- Deprecation, supersession and retraction preserve resolvable lineage.
- SHACL/schema validity is not factual truth; cryptographic authenticity is not epistemic correctness.
- Agent-generated schema or mappings remain proposals until independent checks and owner review pass.

See `../collections/ontology_knowledge_architecture.yaml` for the machine-readable model and `../audits/ontology_knowledge_gap_2026-09-09.yaml` for the coverage review.

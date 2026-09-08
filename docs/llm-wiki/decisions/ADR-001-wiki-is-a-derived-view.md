
# ADR-001: Wiki Is a Derived View

- Status: Accepted
- Date: 2026-09-09

## Context

A persistent Markdown wiki is highly useful for human orientation and agent context. However, a page can combine many claims, sources, editorial choices, and levels of certainty. Treating the page as the authoritative truth object makes precise retraction, contradiction, and source-update handling difficult.

## Decision

The wiki is a compiled view over source, identity, ontology, claim, evidence, temporal, and governance objects.

`raw_data/` and future claim/evidence records retain authority. Wiki pages retain navigation, synthesis, pedagogy, and editorial state.

## Consequences

- pages can be regenerated;
- page revisions and claim versions remain separate;
- citations point through claim/source IDs;
- source retraction can target dependent sections;
- another renderer can replace Markdown without losing knowledge identity;
- build manifests and dependency graphs become mandatory.

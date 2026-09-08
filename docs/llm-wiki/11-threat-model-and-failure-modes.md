
# Threat Model and Failure Modes

## Threat surfaces

### Source attacks

- prompt injection inside papers or web pages;
- malicious metadata;
- poisoned citations;
- derivative mirrors that create circular support;
- silently changed URLs;
- adversarial PDFs or archives;
- license traps.

Mitigation: treat source text as data, isolate parsing, use canonical sources, hash revisions, restrict tools, and never execute embedded instructions.

### Compilation attacks

- model invents claims;
- model widens or narrows scope;
- model removes uncertainty;
- model merges identities;
- model hides disagreement;
- model overwrites protected human text;
- model optimizes for evaluator wording.

Mitigation: claim-first compilation, evidence selectors, protected regions, semantic diff, independent checks, and review.

### Governance attacks

- generator also grades and approves itself;
- policy file is modified as part of a normal ingest;
- reviewer identity is spoofed;
- high-risk change is split into many low-risk changes;
- rollback artifacts are incomplete.

Mitigation: separation of powers, signed or authenticated decisions, policy-path protection, aggregate impact analysis, and rollback drills.

### Consumption attacks

- agent reads stale page;
- context pack omits counterevidence;
- malicious page link expands privileges;
- answer is filed back and cited as independent evidence;
- summaries recursively amplify earlier compression errors.

Mitigation: as-of and freshness state, contested-claim inclusion, least-privilege tools, circularity checks, and source expansion.

## Common non-adversarial failures

### Page sprawl

Too many near-duplicate pages make routing worse.

### Monolithic overview

One page becomes too large and hides claim ownership and update cadence.

### Link inflation

The agent adds generic links that create a dense but meaningless graph.

### Source-list fallacy

A long bibliography creates the appearance of support without sentence-level entailment.

### Consensus collapse

The system selects one answer and erases the fact that sources disagree.

### Temporal collapse

Old and current facts are mixed without valid time.

### Identity collapse

Similar names are merged, propagating false relations.

### Manual-edit loss

Recompilation overwrites human correction.

### Stale cache

A cache hit ignores ontology, prompt, or entity-registry changes.

### Evaluation theater

Scores improve while real research or decision tasks do not.

## Incident response

1. stop publication;
2. preserve logs and candidate artifacts;
3. identify affected builds and consumers;
4. classify source, claim, page, schema, or policy failure;
5. rollback or quarantine;
6. repair dependency graph;
7. add regression fixture;
8. update threat model and admission policy;
9. publish a postmortem.

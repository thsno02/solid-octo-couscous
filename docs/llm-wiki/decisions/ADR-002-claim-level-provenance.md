
# ADR-002: Claim-Level Provenance

- Status: Accepted
- Date: 2026-09-09

## Context

A page-level `sources: []` field says which documents contributed to a page, but it does not prove which source supports which sentence, qualifier, number, or time range.

## Decision

Every promoted factual claim has a stable claim ID, source revision, source selector, evidence hash, assertion kind, scope, and review state. Published pages reference claims. High-risk statements expose atomic claim references; normal factual paragraphs retain direct source citations.

## Consequences

- citations can be checked for entailment and scope;
- contradictions can be represented rather than overwritten;
- retractions and updates can propagate through dependencies;
- factuality evaluation becomes atomic;
- extraction and storage cost increase;
- page generation must consume claim bundles rather than arbitrary raw text.

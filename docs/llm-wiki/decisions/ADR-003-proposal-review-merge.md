
# ADR-003: Proposal, Review, Merge

- Status: Accepted
- Date: 2026-09-09

## Context

Direct LLM writes are fast but make semantic drift, evidence loss, identity corruption, and policy bypass difficult to detect. Git line diffs alone do not describe changes in meaning.

## Decision

Every generated modification is a `WikiChange` proposal. It records the base revision, source delta, affected claims and pages, operations, semantic diff, validation results, review decision, rollout, and rollback.

Normal compilation agents cannot directly merge published changes.

## Consequences

- generated work is auditable;
- low-risk repairs can still be automated under policy;
- high-risk changes receive independent review;
- rejected changes remain useful training and audit evidence;
- publication latency increases;
- reviewer routing and ownership must be implemented.

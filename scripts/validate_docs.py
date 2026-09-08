#!/usr/bin/env python3
"""Validate the durable documentation and LLM Wiki examples.

The validator intentionally checks only deterministic contracts:
- required documentation entry points exist,
- relative Markdown links resolve,
- example YAML parses,
- example page/change/claim records conform to their schemas,
- core implementation documents retain required anchors.

Scientific completeness and prose quality remain review responsibilities.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import unquote

import yaml
from jsonschema import Draft202012Validator, FormatChecker


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = REPO_ROOT / "docs"
RAW_ROOT = REPO_ROOT / "raw_data"

REQUIRED_FILES = [
    "docs/README.md",
    "docs/260909-collection/README.md",
    "docs/260909-collection/01-mission-and-scope.md",
    "docs/260909-collection/02-coverage-map.md",
    "docs/260909-collection/03-source-model-and-directory-layout.md",
    "docs/260909-collection/04-metadata-schemas-and-identifiers.md",
    "docs/260909-collection/05-trust-verification-and-promotion.md",
    "docs/260909-collection/06-collection-workflow-and-ci.md",
    "docs/260909-collection/07-known-gaps-and-roadmap.md",
    "docs/260909-collection/08-agent-handoff-and-operating-rules.md",
    "docs/260909-collection/09-batch-ledger.md",
    "docs/llm-wiki/README.md",
    "docs/llm-wiki/01-principles-and-boundaries.md",
    "docs/llm-wiki/02-reference-architecture.md",
    "docs/llm-wiki/03-knowledge-page-and-claim-model.md",
    "docs/llm-wiki/04-build-pipeline.md",
    "docs/llm-wiki/05-aggregation-linking-and-navigation.md",
    "docs/llm-wiki/06-evaluation-and-quality-gates.md",
    "docs/llm-wiki/07-admission-governance-and-evolution.md",
    "docs/llm-wiki/08-consumption-and-agent-interfaces.md",
    "docs/llm-wiki/09-repo-implementation-plan.md",
    "docs/llm-wiki/10-runbooks-prompts-and-jobs.md",
    "docs/llm-wiki/11-threat-model-and-failure-modes.md",
    "docs/llm-wiki/12-open-questions-and-research-agenda.md",
    "docs/llm-wiki/13-research-basis.md",
    "docs/llm-wiki/decisions/ADR-001-wiki-is-a-derived-view.md",
    "docs/llm-wiki/decisions/ADR-002-claim-level-provenance.md",
    "docs/llm-wiki/decisions/ADR-003-proposal-review-merge.md",
    "docs/llm-wiki/templates/wiki-page.example.yaml",
    "docs/llm-wiki/templates/wiki-change.example.yaml",
    "docs/llm-wiki/templates/claim.example.yaml",
]

CORE_ANCHORS = {
    "docs/260909-collection/01-mission-and-scope.md": [
        "## Mission",
        "## Why the scope is deliberately broad",
        "## Unit of future knowledge",
    ],
    "docs/260909-collection/02-coverage-map.md": [
        "## Strong or usable seed coverage",
        "## Materially under-covered",
        "## Coverage rule",
    ],
    "docs/llm-wiki/04-build-pipeline.md": [
        "## Stage 0 — trigger and scope",
        "## Stage 4 — atomic claim and evidence extraction",
        "## Stage 9 — candidate page compilation",
        "## Stage 13 — admission and merge",
        "## Stage 16 — monitoring, lint, and repair",
        "## Minimum viable build",
    ],
    "docs/llm-wiki/06-evaluation-and-quality-gates.md": [
        "## Evaluation layers",
        "## Gate classes",
        "## Evaluator policy",
    ],
    "docs/llm-wiki/09-repo-implementation-plan.md": [
        "## Phase 1 — source registry and materialization",
        "## Phase 2 — claim and evidence layer",
        "## Phase 3 — first wiki compiler",
        "## Phase 6 — maintenance",
    ],
}

MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def validate_relative_links(errors: list[str]) -> int:
    checked = 0
    for md_path in sorted(DOCS_ROOT.rglob("*.md")):
        text = md_path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().split(" ", 1)[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = unquote(target.split("#", 1)[0])
            resolved = (md_path.parent / target).resolve()
            checked += 1
            try:
                resolved.relative_to(REPO_ROOT.resolve())
            except ValueError:
                errors.append(f"DOC_LINK_OUTSIDE_REPO {rel(md_path)} -> {target}")
                continue
            if not resolved.exists():
                errors.append(f"BROKEN_DOC_LINK {rel(md_path)} -> {target}")
    return checked


def validate_example(
    example_path: Path,
    schema_path: Path,
    errors: list[str],
) -> None:
    try:
        example = load_yaml(example_path)
        schema = load_yaml(schema_path)
    except Exception as exc:
        errors.append(f"YAML_PARSE {rel(example_path)}: {exc}")
        return
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for issue in sorted(validator.iter_errors(example), key=lambda err: list(err.path)):
        pointer = "/".join(str(part) for part in issue.path) or "<root>"
        errors.append(f"DOC_SCHEMA {rel(example_path)} at {pointer}: {issue.message}")


def main() -> int:
    errors: list[str] = []

    for required in REQUIRED_FILES:
        if not (REPO_ROOT / required).exists():
            errors.append(f"MISSING_DOC {required}")

    for path_str, anchors in CORE_ANCHORS.items():
        path = REPO_ROOT / path_str
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for anchor in anchors:
            if anchor not in text:
                errors.append(f"MISSING_DOC_ANCHOR {path_str}: {anchor}")

    checked_links = validate_relative_links(errors)

    validate_example(
        DOCS_ROOT / "llm-wiki/templates/wiki-page.example.yaml",
        RAW_ROOT / "schemas/wiki_page.schema.yaml",
        errors,
    )
    validate_example(
        DOCS_ROOT / "llm-wiki/templates/wiki-change.example.yaml",
        RAW_ROOT / "schemas/wiki_change.schema.yaml",
        errors,
    )
    validate_example(
        DOCS_ROOT / "llm-wiki/templates/claim.example.yaml",
        RAW_ROOT / "schemas/knowledge_model.schema.yaml",
        errors,
    )

    md_files = len(list(DOCS_ROOT.rglob("*.md")))
    yaml_examples = len(list(DOCS_ROOT.rglob("*.yaml")))
    print(
        "docs_validation_summary "
        f"markdown_files={md_files} "
        f"yaml_examples={yaml_examples} "
        f"relative_links_checked={checked_links} "
        f"errors={len(errors)}"
    )

    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("\nDocumentation validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

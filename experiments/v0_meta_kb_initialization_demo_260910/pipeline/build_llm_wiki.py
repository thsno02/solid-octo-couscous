#!/usr/bin/env python3
"""Compile the v0 LLM Wiki from the materialized claim/evidence layer."""
from __future__ import annotations

from pathlib import Path

from llm_wiki_common import *
from llm_wiki_pages import compile_pages
from llm_wiki_outputs import *
from llm_wiki_release import record_validation


def main() -> int:
    paths = [
        EXP / "00_inputs/selected_sources.yaml",
        EXP / "04_claims/claims.jsonl",
        EXP / "03_evidence/evidence.jsonl",
        EXP / "02_entities/sources.jsonl",
        EXP / "00_inputs/materialization_snapshot.yaml",
        EXP / "config.yaml",
    ]
    code_paths = [
        Path(__file__),
        Path(__file__).with_name("llm_wiki_common.py"),
        Path(__file__).with_name("llm_wiki_atomic.py"),
        Path(__file__).with_name("llm_wiki_core.py"),
        Path(__file__).with_name("llm_wiki_pages.py"),
        Path(__file__).with_name("llm_wiki_outputs.py"),
        Path(__file__).with_name("llm_wiki_machine.py"),
        Path(__file__).with_name("llm_wiki_release.py"),
        Path(__file__).with_name("llm_wiki_validation.py"),
        Path(__file__).with_name("validate_demo.py"),
        Path(__file__).with_name("evidence_validation.py"),
        Path(__file__).with_name("rights_propagation.py"),
        ROOT / "raw_data/schemas/knowledge_model.schema.yaml",
        ROOT / "raw_data/schemas/wiki_page.schema.yaml",
        ROOT / "raw_data/schemas/wiki_change.schema.yaml",
    ]
    if any(not path.exists() for path in paths + code_paths):
        raise SystemExit("missing compiler inputs or modules")
    selected = yload(paths[0], {}).get("sources", [])
    claims = jread(paths[1])
    evidence = jread(paths[2])
    snapshot = yload(paths[4], {})
    config = yload(paths[5], {})
    key = sha_text("|".join(sha_file(path) for path in paths + code_paths) + "|" + VERSION)
    build = f"build:llm-wiki-v0:{key[:16]}"
    at = str(snapshot.get("generated_at") or "2026-09-13T17:43:07Z")
    # A failed compile must not leave an old successful release marker behind.
    for name in ("wiki_build_manifest.yaml", "change_feed.jsonl"):
        (EXP / "08_release" / name).unlink(missing_ok=True)
    shutil.rmtree(WIKI, ignore_errors=True)
    WIKI.mkdir(parents=True, exist_ok=True)
    pages = compile_pages(selected, claims, evidence, snapshot)
    write_pages(pages, build, at, selected)
    products = machine(pages, claims, evidence, selected, build, at)
    pipeline(pages, claims, selected, snapshot, config, build, at, products)
    try:
        result = validate(claims, evidence, selected)
        from validate_demo import main as validate_demo
        if validate_demo(write_reports=True):
            raise RuntimeError("demo evidence validation failed")
    except Exception:
        record_validation({"errors": ["compiler validation failed"]})
        raise
    record_validation(result)
    ywrite(EXP / "06_evaluation/compiler_validation.yaml", result)
    manifest(build, at, paths + code_paths)
    print(
        "llm_wiki_built "
        f"build_id={build} pages={len(pages)} claims={len(claims)} sources={len(selected)} "
        f"typed_links={sum(len(page['outgoing']) for page in pages)} "
        f"context_packs={len(products['packs'])} warnings={len(result['warnings'])} errors={len(result['errors'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

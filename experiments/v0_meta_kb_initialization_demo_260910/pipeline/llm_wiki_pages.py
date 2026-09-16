#!/usr/bin/env python3
"""Page planning and candidate page compilation for the v0 LLM Wiki."""
from __future__ import annotations

from typing import Any

from llm_wiki_atomic import build_atomic_pages
from llm_wiki_common import EXP, ROOT
from llm_wiki_core import build_core_pages
from rights_propagation import page_rights_payload, rights_markdown


def compile_pages(
    sources: list[dict[str, Any]],
    claims: list[dict[str, Any]],
    evidence: list[dict[str, Any]],
    snapshot: dict[str, Any],
) -> list[dict[str, Any]]:
    pages = build_core_pages(build_atomic_pages(sources, claims, evidence, snapshot), snapshot)
    claims_by_uid = {str(claim["uid"]): claim for claim in claims}
    sources_by_uid = {str(source["uid"]): source for source in sources}
    wiki_repo_path = (EXP.relative_to(ROOT) / "05_wiki").as_posix()
    for page in pages:
        refs, unavailable = page_rights_payload(page["rendered_claims"], claims_by_uid)
        page["rights_refs"] = refs
        page["rights_unavailable_source_refs"] = unavailable
        section = rights_markdown(
            current_repo_path=f"{wiki_repo_path}/{page['path']}",
            rights_refs=refs,
            unavailable_source_refs=unavailable,
            sources_by_uid=sources_by_uid,
        )
        if section:
            page["body"] = page["body"].rstrip() + "\n\n" + section
    return pages

#!/usr/bin/env python3
"""Page planning and candidate page compilation for the v0 LLM Wiki."""
from __future__ import annotations

from typing import Any

from llm_wiki_atomic import build_atomic_pages
from llm_wiki_core import build_core_pages


def compile_pages(
    sources: list[dict[str, Any]],
    claims: list[dict[str, Any]],
    evidence: list[dict[str, Any]],
    snapshot: dict[str, Any],
) -> list[dict[str, Any]]:
    return build_core_pages(build_atomic_pages(sources, claims, evidence, snapshot), snapshot)

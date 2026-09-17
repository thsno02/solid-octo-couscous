#!/usr/bin/env python3
"""Validate that every collected source has an honest, locally consumable capsule."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw_data"
CORPUS = ROOT / "materialized_sources" / "corpus"
INDEX = ROOT / "materialized_sources" / "index.yaml"
REGISTRY = ROOT / "source_registry" / "registry.yaml"
AUDIT = ROOT / "raw_data" / "audits" / "materialization_completeness_2026-09-10.yaml"

CONTENT_TIERS = {"full_text", "semantic_capsule", "excerpt_capsule", "metadata_capsule"}
STATUSES = {"materialized", "partial", "metadata_only", "failed"}


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_yaml_checked(path: Path, label: str, errors: list[str]) -> Any:
    try:
        return load_yaml(path)
    except (OSError, yaml.YAMLError) as exc:
        errors.append(f"{label}_YAML {path.relative_to(ROOT)}: {exc}")
        return None


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def scoped_path(raw_path: Any, scope: Path, *, repository_root: Path | None = None) -> Path | None:
    """Resolve a repository-relative path only when it stays inside ``scope``."""

    if not isinstance(raw_path, str) or not raw_path:
        return None
    path = Path(raw_path)
    if path.is_absolute() or ".." in path.parts:
        return None
    candidate = (repository_root or ROOT) / path
    try:
        candidate.resolve().relative_to(scope.resolve())
    except (OSError, ValueError):
        return None
    return candidate


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def validate_tex_reading_view(
    manifest: dict[str, Any], capsule_root: Path, actual_hashes: dict[str, str],
    errors: list[str], *, repository_root: Path | None = None,
) -> None:
    """An opt-in reading view remains derived and bound to retained local inputs."""
    materialization = manifest.get("materialization") or {}
    view = materialization.get("tex_reading_view")
    if not isinstance(view, dict) or view.get("enabled") is not True:
        return
    uid, repo_root = manifest.get("uid"), repository_root or ROOT
    try:
        if manifest.get("adapter") != "arxiv_latex_v2" or view.get("profile") != "conservative-v1" or view.get("document") != "normalized/reading.md":
            raise ValueError("invalid adapter/profile/document")
        if materialization.get("document") != view["document"] or materialization.get("normalized_document") != view["document"]:
            raise ValueError("chosen consumer is not the declared reading view")
        if view.get("legacy_documents") != ["normalized/document.tex", "normalized/document.txt"]:
            raise ValueError("both legacy documents must remain declared")
        root_name, support, paths = view["source_root"], view["citation_support"], view["source_paths"]
        if not isinstance(support, list) or not isinstance(paths, list) or not paths or len(set(paths)) != len(paths):
            raise ValueError("invalid finite source paths")
        for name in [root_name, *support]:
            if not isinstance(name, str) or not name or Path(name).is_absolute() or ".." in Path(name).parts or Path(name).parts[0] != "source":
                raise ValueError("reading inputs must be retained source paths")
        root_relative = (capsule_root / root_name).relative_to(repo_root).as_posix()
        if paths[0] != root_relative or not {(capsule_root / name).relative_to(repo_root).as_posix() for name in support}.issubset(paths):
            raise ValueError("source paths do not cover root and citation support")
        source_rows = [json.loads(line) for line in (capsule_root / "files.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
        retained = {row["path"]: row for row in source_rows}
        for path_name in paths:
            path = scoped_path(path_name, capsule_root / "source", repository_root=repo_root)
            if path is None or not path.is_file() or path_name not in actual_hashes or path_name not in retained or retained[path_name].get("sha256") != actual_hashes[path_name] or retained[path_name].get("bytes") != path.stat().st_size:
                raise ValueError("reading input is not inventoried retained source")
        for name in [view["document"], *view["legacy_documents"], "files.jsonl"]:
            if (capsule_root / name).relative_to(repo_root).as_posix() not in actual_hashes:
                raise ValueError("reading or legacy input is not inventoried")
        document = capsule_root / view["document"]
        local_path = document.relative_to(repo_root).as_posix()
        text = document.read_text(encoding="utf-8")
        lines = text.splitlines()
        selectors = [json.loads(line) for line in (capsule_root / "selectors.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
        count = view["legacy_selector_count"]
        if not isinstance(count, int) or isinstance(count, bool) or not 0 <= count < len(selectors) or any(row.get("local_path") == local_path for row in selectors[:count]):
            raise ValueError("invalid legacy prefix or no reading selectors")
        for row in selectors[count:]:
            first, last = row.get("start_line"), row.get("end_line")
            if any(not isinstance(value, int) or isinstance(value, bool) for value in (first, last)) or not 1 <= first <= last <= len(lines):
                raise ValueError("invalid reading range")
            if row.get("selector") != f"derived://{local_path}#L{first}-L{last}" or row.get("local_path") != local_path or row.get("kind") not in {"file", "section"} or row.get("reading_profile") != view["profile"]:
                raise ValueError("invalid derived reading selector")
            if row.get("derived_from") != root_relative or row.get("source_paths") != paths or not isinstance(row.get("transformation"), str) or not row["transformation"].strip():
                raise ValueError("missing reading transformation/source provenance")
            preview = row.get("text_preview")
            if not isinstance(preview, str) or not preview or preview not in "\n".join(lines[first - 1:last]):
                raise ValueError("reading preview does not resolve in its own span")
            if "source_heading_line" in row:
                source_path = row.get("source_heading_path")
                heading_line = row["source_heading_line"]
                if source_path not in paths or not isinstance(heading_line, int) or isinstance(heading_line, bool) or not 1 <= heading_line <= len((repo_root / source_path).read_text(encoding="utf-8").splitlines()):
                    raise ValueError("invalid original heading location")
        if not any(row.get("kind") == "file" and row.get("start_line") == 1 for row in selectors[count:]):
            raise ValueError("reading view needs a real file range")
    except (KeyError, TypeError, AttributeError, ValueError, OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"TEX_READING_VIEW {uid}: {exc}")


def validate_retained_markdown_binding(
    manifest: dict[str, Any], capsule_root: Path, actual_hashes: dict[str, str],
    errors: list[str], *, repository_root: Path | None = None, check_derived: bool = True,
) -> None:
    """Bind an opt-in retained Markdown original to its inventory and retrieval."""
    materialization = manifest.get("materialization")
    sidecar_declared = isinstance(manifest.get("selectors"), list) and "normalized/selectors.jsonl" in manifest["selectors"]
    if sidecar_declared or (capsule_root / "source/specification.html").exists() or isinstance(materialization, dict) and any(field in materialization for field in ("retained_text_binding", "retained_text_selectors")):
        if not isinstance(materialization, dict) or "retained_text_sources" not in materialization:
            label = "RETAINED_DATED_HTML" if (capsule_root / "source/specification.html").exists() or isinstance(materialization, dict) and materialization.get("retained_text_binding") == "dated_html_response" else "RETAINED_TEXT_DECLARATION"
            errors.append(f"{label} {manifest.get('uid')}: retained original has no text declaration")
            return
    if isinstance(materialization, dict) and "retained_text_sources" in materialization:
        validate_retained_text_binding(manifest, capsule_root, actual_hashes, errors, repository_root=repository_root, check_derived=check_derived)
        return
    if not isinstance(materialization, dict) or "retained_markdown_source" not in materialization:
        return
    uid = manifest.get("uid")
    source_name = materialization["retained_markdown_source"]
    repo_root = repository_root or ROOT
    if not isinstance(source_name, str) or not source_name or Path(source_name).is_absolute() or ".." in Path(source_name).parts:
        errors.append(f"RETAINED_MARKDOWN_SOURCE_PATH {uid}")
        return
    source_relative = (capsule_root / source_name).relative_to(repo_root).as_posix()
    source = scoped_path(source_relative, capsule_root, repository_root=repo_root)
    source_hash = actual_hashes.get(source_relative)
    if source is None or not source.is_file() or not source_hash:
        errors.append(f"RETAINED_MARKDOWN_SOURCE_UNHASHED {uid}")
        return
    inventory = manifest.get("local_files")
    rows = [item for item in inventory if isinstance(item, dict) and item.get("path") == source_relative] if isinstance(inventory, list) else []
    if len(rows) != 1 or rows[0].get("sha256") != source_hash:
        errors.append(f"RETAINED_MARKDOWN_INVENTORY_HASH {uid}")
    if manifest.get("revision") != f"sha256:{source_hash}":
        errors.append(f"RETAINED_MARKDOWN_REVISION {uid}")
    retrievals = manifest.get("retrievals")
    rows = [item for item in retrievals if isinstance(item, dict) and item.get("local_path") == source_name] if isinstance(retrievals, list) else []
    if len(rows) != 1 or rows[0].get("sha256") != source_hash or rows[0].get("bytes") != source.stat().st_size:
        errors.append(f"RETAINED_MARKDOWN_RETRIEVAL {uid}")


def validate_retained_text_binding(
    manifest: dict[str, Any], capsule_root: Path, actual_hashes: dict[str, str],
    errors: list[str], *, repository_root: Path | None = None, check_derived: bool = True,
) -> None:
    """Bind the finite native-text assembly to existing per-file snapshot evidence."""
    materialization = manifest["materialization"]
    uid = manifest.get("uid")
    binding = materialization.get("retained_text_binding")
    if binding == "dated_html_response" or binding == "wiki_page_revision_set":
        validate_retained_text_sidecar_binding(manifest, capsule_root, actual_hashes, errors, repository_root=repository_root, check_derived=check_derived)
        return
    git_sidecar = binding == "git_snapshot"
    if not git_sidecar and (binding is not None or "retained_text_selectors" in materialization):
        errors.append(f"RETAINED_TEXT_BINDING {uid}")
        return
    sources = materialization["retained_text_sources"]
    if "retained_markdown_source" in materialization or not isinstance(sources, list) or not sources:
        errors.append(f"RETAINED_TEXT_DECLARATION {uid}")
        return
    revision = re.fullmatch(r"git:([0-9a-f]{40})", str(manifest.get("revision", "")))
    commit = revision.group(1) if revision else None
    source_metadata = load_yaml_checked(capsule_root / "source-metadata.yaml", "RETAINED_TEXT_METADATA", errors)
    versioning = (source_metadata.get("versioning") or {}) if isinstance(source_metadata, dict) else {}
    if not commit or not isinstance(versioning, dict) or versioning.get("snapshot_commit") != commit or versioning.get("source_version") != manifest.get("source_version"):
        errors.append(f"RETAINED_TEXT_REVISION {uid}")
    repo_root = repository_root or ROOT
    names: set[str] = set()
    for item in sources:
        source_name = item.get("source") if isinstance(item, dict) else None
        format_name = item.get("format") if isinstance(item, dict) else None
        if (
            not isinstance(source_name, str) or not source_name or Path(source_name).is_absolute()
            or ".." in Path(source_name).parts or Path(source_name).parts[0] != "source"
            or source_name in names or not isinstance(format_name, str) or format_name not in {"md", "yaml", "html"}
            or Path(source_name).suffix.lower() not in {"md": {".md"}, "yaml": {".yaml", ".yml"}, "html": {".html", ".htm"}}[format_name]
        ):
            errors.append(f"RETAINED_TEXT_SOURCE_PATH_FORMAT {uid}: {source_name}")
            continue
        names.add(source_name)
        if git_sidecar and "role" in item and (format_name != "yaml" or item["role"] != "example"):
            errors.append(f"RETAINED_TEXT_ROLE {uid}: {source_name}")
        if "docfx_includes" in item and (not git_sidecar or format_name != "md"):
            errors.append(f"RETAINED_DOCFX_BINDING {uid}: {source_name}")
        source_relative = (capsule_root / source_name).relative_to(repo_root).as_posix()
        source = scoped_path(source_relative, capsule_root, repository_root=repo_root)
        source_hash = actual_hashes.get(source_relative)
        if source is None or not source.is_file() or not source_hash:
            errors.append(f"RETAINED_TEXT_SOURCE_UNHASHED {uid}: {source_name}")
            continue
        if git_sidecar and sha256_file(source) != source_hash:
            errors.append(f"RETAINED_TEXT_SOURCE_DRIFT {uid}: {source_name}")
        if "config_range" in item:
            bounds = item["config_range"]
            start = bounds.get("start_line") if isinstance(bounds, dict) else None
            end = bounds.get("end_line") if isinstance(bounds, dict) else None
            if format_name != "html" or any(not isinstance(value, int) or isinstance(value, bool) for value in (start, end)) or not 1 <= start <= end <= len(source.read_bytes().decode("utf-8").splitlines()):
                errors.append(f"RETAINED_HTML_CONFIG_RANGE {uid}: {source_name}")
        inventory = manifest.get("local_files")
        rows = [row for row in inventory if isinstance(row, dict) and row.get("path") == source_relative] if isinstance(inventory, list) else []
        if len(rows) != 1 or rows[0].get("sha256") != source_hash or rows[0].get("bytes") != source.stat().st_size:
            errors.append(f"RETAINED_TEXT_INVENTORY {uid}: {source_name}")
        retrievals = manifest.get("retrievals")
        rows = [row for row in retrievals if isinstance(row, dict) and row.get("local_path") == source_name] if isinstance(retrievals, list) else []
        if len(rows) != 1 or rows[0].get("sha256") != source_hash or rows[0].get("bytes") != source.stat().st_size or rows[0].get("commit") != commit:
            errors.append(f"RETAINED_TEXT_RETRIEVAL {uid}: {source_name}")
    if git_sidecar:
        validate_retained_text_sidecar_binding(manifest, capsule_root, actual_hashes, errors, repository_root=repository_root, check_derived=check_derived)


def validate_retained_text_sidecar_binding(
    manifest: dict[str, Any], capsule_root: Path, actual_hashes: dict[str, str], errors: list[str],
    *, repository_root: Path | None = None, check_derived: bool = True,
) -> None:
    """Check the explicit consumer pair while preserving legacy acquisition bytes."""
    from urllib.parse import unquote, urlsplit
    from materialize_all_sources import preflight_dated_html_assets, preflight_docfx_includes, preflight_wiki_html_sources, redistribution_footer, retained_markdown_frontmatter_end, retained_text_selector_file
    repo_root = (repository_root or ROOT).resolve()
    capsule_root = capsule_root.resolve()
    uid = manifest.get("uid")
    dated_html = manifest["materialization"].get("retained_text_binding") == "dated_html_response"
    wiki_html = manifest["materialization"].get("retained_text_binding") == "wiki_page_revision_set"
    label = "RETAINED_DATED_HTML" if dated_html else "RETAINED_WIKI_HTML" if wiki_html else "RETAINED_GIT_TEXT"
    try:
        if manifest.get("adapter") != "generic_web_or_document_v2":
            raise ValueError("retained sidecar needs its actual generic adapter")
        selectors = retained_text_selector_file(manifest, capsule_root, require_exists=check_derived)
        materialization = manifest["materialization"]
        single_git = materialization.get("retained_text_binding") == "git_snapshot" and manifest["selectors"] == ["normalized/selectors.jsonl"]
        if dated_html:
            source = capsule_root / "source/specification.html"
            source_path = source.relative_to(repo_root).as_posix()
            source_hash = sha256_file(source)
            if actual_hashes.get(source_path) != source_hash or manifest.get("revision") != f"sha256:{source_hash}":
                raise ValueError("dated HTML revision differs from its actual original")
            inventory = [row for row in manifest["local_files"] if row.get("path") == source_path]
            if len(inventory) != 1 or inventory[0].get("sha256") != source_hash or inventory[0].get("bytes") != source.stat().st_size:
                raise ValueError("dated HTML original differs from inventory")
        metadata_path = (repo_root / manifest["metadata_path"]).resolve()
        metadata_path.relative_to(repo_root)
        canonical, capsule = load_yaml(metadata_path), load_yaml(capsule_root / "source-metadata.yaml")
        version = manifest["source_version"]
        if not isinstance(version, str) or not version.strip():
            raise ValueError("retained sidecar needs its explicit selected version")
        package = manifest["rights"]["redistribution_package"]
        if not isinstance(package, dict) or any(not isinstance(package.get(field), str) or not package[field].strip() for field in (
            "source_revision", "source_version_url", "notice_path", "attribution", "modifications", "scope",
        )) or package["source_revision"] != manifest["revision"]:
            raise ValueError("retained sidecar package is incomplete or covers a different revision")
        approved_url = package["source_version_url"]
        if dated_html:
            parsed = urlsplit(approved_url)
            if parsed.scheme != "https" or not parsed.netloc or parsed.query or parsed.fragment or parsed.username:
                raise ValueError("dated HTML needs its literal approved HTTPS URL")
        for metadata in (canonical, capsule):
            if (
                not isinstance(metadata, dict) or not isinstance(metadata.get("versioning"), dict)
                or metadata["versioning"].get("source_version") != version
                or (dated_html or wiki_html) and metadata.get("full_text_url") != approved_url
                or not dated_html and not wiki_html and manifest["revision"] != f"git:{metadata['versioning'].get('snapshot_commit')}"
                or metadata.get("rights", {}).get("redistribution_package") != package
                or any(metadata.get(field) != canonical.get(field) for field in ("uid", "title", "url", "canonical_url", "canonical_id"))
                or metadata.get("uid") != uid
            ):
                raise ValueError("retained sidecar canonical/capsule identity, version, commit or package differs")
        if not dated_html and not wiki_html:
            rewrites = materialization.get("link_rewrites", {})
            if not isinstance(rewrites, dict):
                raise ValueError("retained Git sidecar needs a finite local href mapping")
            for target in rewrites.values():
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc:
                    raise ValueError("retained Git rewrite must target a local original")
                if not parsed.path:
                    continue
                path = (capsule_root / "normalized" / unquote(parsed.path)).resolve()
                path.relative_to(capsule_root / "source")
                local_path = path.relative_to(capsule_root).as_posix()
                original_path = path.relative_to(repo_root).as_posix()
                original_hash = sha256_file(path)
                inventory = [row for row in manifest["local_files"] if row.get("path") == original_path]
                retrievals = [row for row in manifest["retrievals"] if row.get("local_path") == local_path]
                if len(inventory) != 1 or inventory[0].get("sha256") != original_hash or inventory[0].get("bytes") != path.stat().st_size or len(retrievals) != 1 or retrievals[0].get("sha256") != original_hash or retrievals[0].get("bytes") != path.stat().st_size or manifest["revision"] != f"git:{retrievals[0].get('commit')}":
                    raise ValueError("retained Git rewrite original differs from inventory, retrieval or fixed commit")
        if dated_html:
            records = [row for row in manifest["retrievals"] if row.get("local_path") == "source/specification.html"]
            if len(records) != 1 or any(records[0].get(field) != expected for field, expected in (
                ("requested_url", approved_url), ("resolved_url", approved_url), ("sha256", source_hash),
                ("bytes", source.stat().st_size), ("http_status", 200),
            )) or not isinstance(records[0].get("content_type"), str) or records[0]["content_type"].split(";", 1)[0].strip() != "text/html" or not isinstance(records[0].get("retrieved_at"), str) or not records[0]["retrieved_at"].strip():
                raise ValueError("dated HTML retrieval does not describe the approved response")
        review = [row for row in load_yaml(repo_root / "raw_data/audits/materialization_rights_review.yaml")["items"] if row.get("uid") == uid]
        if len(review) != 1 or review[0].get("redistribution_package") != package or review[0].get("source_revision") != manifest["revision"] or review[0].get("manifest_path") != (capsule_root / "manifest.yaml").relative_to(repo_root).as_posix() or review[0].get("publication_gate", {}).get("decision") != "allow":
            raise ValueError("retained sidecar audit allowance or four-party package differs")
        notice_path = (repo_root / package["notice_path"]).resolve()
        notice_path.relative_to(repo_root)
        notice = notice_path.read_bytes()
        if not notice.strip() or (capsule_root / "NOTICE.md").read_bytes() != notice:
            raise ValueError("retained sidecar full NOTICE differs from its reviewed asset")
        history = manifest["historical_acquisition"]
        if not isinstance(history, dict) or not all(field in history for field in ("revision", "retrievals", "rights", "local_files")) or not isinstance(history["local_files"], list) or not history["local_files"]:
            raise ValueError("retained sidecar must preserve its prior acquisition facts")
        if single_git and (history.get("status") != "metadata_only" or history.get("content_tier") != "metadata_capsule" or history.get("selectors") != [] or history["revision"] is not None or history["retrievals"] != [] or history.get("materialization") is not None):
            raise ValueError("single Git sidecar requires its actual metadata-only acquisition history")
        if not single_git and "materialization" not in history:
            raise ValueError("retained sidecar must preserve its prior materialization facts")
        for name in ("document.md", "selectors.jsonl"):
            path = capsule_root / name
            old = [row for row in history["local_files"] if row.get("path") == path.relative_to(repo_root).as_posix()]
            if single_git:
                if old or path.exists():
                    raise ValueError("single Git sidecar cannot hide a legacy document or selectors")
            elif len(old) != 1 or old[0].get("sha256") != sha256_file(path) or old[0].get("bytes") != path.stat().st_size:
                raise ValueError("retained sidecar legacy document or selectors changed")
        docfx_root, docfx_calls = None, {}
        docfx_options = {}
        if any("docfx_includes" in item for item in materialization["retained_text_sources"]):
            if materialization.get("retained_text_binding") != "git_snapshot":
                raise ValueError("DocFX includes need their native Git binding")
            paths = [(capsule_root / item["source"], item["format"]) for item in materialization["retained_text_sources"]]
            for item, (source, _) in zip(materialization["retained_text_sources"], paths):
                retrieval = next((row for row in manifest["retrievals"] if row.get("local_path") == item["source"]), {})
                docfx_options[source.resolve()] = {"git_snapshot": True, "snapshot_commit": canonical["versioning"]["snapshot_commit"], "source_url": retrieval.get("resolved_url") or retrieval.get("requested_url") or "", **({"docfx_includes": item["docfx_includes"]} if "docfx_includes" in item else {})}
            docfx_root, docfx_calls = preflight_docfx_includes(paths, capsule_root, docfx_options)
        if dated_html:
            preflight_dated_html_assets(manifest, capsule_root, repository_root=repo_root)
        if wiki_html:
            preflight_wiki_html_sources(manifest, capsule_root, canonical, capsule, repository_root=repo_root, actual_hashes=actual_hashes)
        if check_derived or (capsule_root / materialization["document"]).exists() or selectors.exists():
            document = capsule_root / materialization["document"]
            text = document.read_bytes().decode("utf-8")
            if text.count("<!-- materialization-redistribution-notice -->") != 1 or not text.endswith(redistribution_footer(package, "../NOTICE.md")):
                raise ValueError("retained sidecar current footer is missing or changed")
            lines = text.splitlines()
            source_ranges = {
                (capsule_root / item["source"]).relative_to(repo_root).as_posix(): (item, len((capsule_root / item["source"]).read_bytes().decode("utf-8").splitlines()))
                for item in materialization["retained_text_sources"]
            }
            rows = [json.loads(line) for line in selectors.read_bytes().decode("utf-8").splitlines() if line.strip()]
            if not rows:
                raise ValueError("retained sidecar has no derived selectors")
            seen_sources = set()
            seen_calls = set()
            for row in rows:
                item, source_lines = source_ranges.get(row.get("derived_from"), ({}, 0))
                start, end = row.get("start_line"), row.get("end_line")
                original_start, original_end = row.get("source_start_line"), row.get("source_end_line")
                if (
                    any(not isinstance(value, int) or isinstance(value, bool) for value in (start, end, original_start, original_end))
                    or not 1 <= start <= end <= len(lines) or not 1 <= original_start <= original_end <= source_lines
                    or row.get("selector") != f"derived://{document.relative_to(repo_root).as_posix()}#L{start}-L{end}"
                    or row.get("local_path") != document.relative_to(repo_root).as_posix() or row.get("source_format") != item.get("format")
                    or row.get("source_role") != item.get("role")
                    or not isinstance(row.get("transformation"), str) or not row["transformation"].strip()
                    or not isinstance(row.get("text_preview"), str) or not row["text_preview"] or row["text_preview"] not in "\n".join(lines[start - 1:end])
                ):
                    raise ValueError("retained sidecar selector provenance or real range differs")
                invocation = row.get("included_at")
                if docfx_root:
                    source = repo_root / row["derived_from"]
                    if source == docfx_root:
                        if invocation is not None or any(original_start <= line <= original_end for line in docfx_calls):
                            raise ValueError("DocFX root selector cannot cross an include call")
                    else:
                        if not isinstance(invocation, dict) or set(invocation) != {"source", "line"} or invocation.get("source") != docfx_root.relative_to(repo_root).as_posix() or not isinstance(invocation.get("line"), int) or isinstance(invocation["line"], bool) or docfx_calls.get(invocation["line"]) != source or original_start <= retained_markdown_frontmatter_end(source.read_bytes().decode("utf-8")):
                            raise ValueError("DocFX include selector differs from its real body or invocation")
                        seen_calls.add(invocation["line"])
                elif invocation is not None:
                    raise ValueError("undeclared DocFX selector invocation")
                seen_sources.add(row["derived_from"])
            if seen_sources != set(source_ranges):
                raise ValueError("retained sidecar omits a declared original")
            if docfx_root and seen_calls != set(docfx_calls):
                raise ValueError("DocFX sidecar omits a declared include occurrence")
    except (KeyError, TypeError, AttributeError, ValueError, OSError, yaml.YAMLError) as exc:
        errors.append(f"{label} {uid}: {exc}")


def pdf_page_sections(text: str) -> tuple[dict[int, str], set[int]]:
    """Split extracted PDF text at exact page headings."""

    matches = list(re.finditer(r"(?m)^## Page ([1-9]\d*)[ \t]*$", text))
    sections: dict[int, str] = {}
    duplicates: set[int] = set()
    for index, match in enumerate(matches):
        page = int(match.group(1))
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        if page in sections:
            duplicates.add(page)
        else:
            sections[page] = text[match.end():end]
    return sections, duplicates


def pdf_primary_excerpt_range(supplement: dict[str, Any], text: str) -> tuple[int, int]:
    """Bound a parent-paper excerpt to Page 1, never an embedded work's abstract."""
    lines = text.splitlines()
    headings = [(index, int(match.group(1))) for index, line in enumerate(lines)
                if (match := re.fullmatch(r"## Page ([1-9]\d*)[ \t]*", line))]
    if not headings or headings[0][1] != 1:
        raise ValueError("primary PDF excerpt requires a native Page 1 boundary")
    first = headings[0][0] + 2
    last = headings[1][0] if len(headings) > 1 else next(
        (index for index, line in enumerate(lines) if line == "<!-- materialization-redistribution-notice -->"), len(lines),
    )
    declaration = supplement.get("primary_excerpt")
    if declaration is None:
        return first, last
    if not isinstance(declaration, dict) or set(declaration) != {"start_line", "end_line"}:
        raise ValueError("primary_excerpt must declare only start_line and end_line")
    start, end = declaration["start_line"], declaration["end_line"]
    if any(not isinstance(value, int) or isinstance(value, bool) for value in (start, end)) or not first <= start <= end <= last:
        raise ValueError("primary_excerpt must be a continuous line range inside native Page 1")
    return start, end


def validate_pdf_page_binding(
    selector: dict[str, Any], native_document: str | None, page_sections: dict[int, str],
    selector_prefix: str, page_count: int | None, seen_pages: set[int],
    location: str, errors: list[str], *, label: str = "ARXIV_PDF",
) -> bool:
    """Shared strict PDF URI/page/preview binding for primary and supplemental PDFs."""
    before = len(errors)
    selector_id = selector.get("selector")
    page = selector.get("page")
    if selector.get("local_path") != native_document:
        errors.append(f"{label}_NATIVE_SELECTOR_TARGET {location}: {selector.get('local_path')}")
    match = re.fullmatch(re.escape(selector_prefix) + r"([1-9]\d*)", selector_id) if isinstance(selector_id, str) else None
    if match is None or not isinstance(page, int) or isinstance(page, bool) or int(match.group(1)) != page:
        errors.append(f"{label}_SELECTOR_HASH_OR_PAGE {location}: {selector_id}")
    if isinstance(page, int) and not isinstance(page, bool):
        if page in seen_pages:
            errors.append(f"{label}_SELECTOR_PAGE_DUPLICATE {location}: {page}")
        seen_pages.add(page)
        if page_count is not None and page > page_count:
            errors.append(f"{label}_SELECTOR_PAGE_RANGE {location}: {page}")
        preview = selector.get("text_preview")
        if isinstance(preview, str) and page in page_sections and preview not in page_sections[page]:
            errors.append(f"{label}_SELECTOR_PREVIEW_CROSS_PAGE {location}: {page}")
    return len(errors) == before


def validate_pdf_page_coverage(
    materialization: dict[str, Any], page_count: int | None, selector_pages: set[int],
    page_selector_count: int, total_selector_count: int, uid: str, errors: list[str],
    *, derived_selector_count: int = 0, label: str = "ARXIV_PDF",
) -> tuple[set[int], set[int]]:
    """Account for every PDF page without permitting undeclared non-page evidence."""
    def page_set(field: str) -> set[int]:
        value = materialization.get(field)
        if not isinstance(value, list) or any(not isinstance(page, int) or isinstance(page, bool) or page < 1 for page in value):
            errors.append(f"{label}_PAGE_SET {uid} {field}={value!r}")
            return set()
        pages = set(value)
        if len(pages) != len(value):
            errors.append(f"{label}_PAGE_SET_DUPLICATE {uid} {field}")
        if page_count is not None and any(page > page_count for page in pages):
            errors.append(f"{label}_PAGE_SET_RANGE {uid} {field}={value!r}")
        return pages
    empty = page_set("pdf_pages_without_extractable_text")
    failed = page_set("pdf_page_extraction_failures")
    if selector_pages & empty or selector_pages & failed or empty & failed:
        errors.append(f"{label}_PAGE_SET_OVERLAP {uid}")
    if page_count is not None:
        expected = set(range(1, page_count + 1))
        covered = selector_pages | empty | failed
        if covered != expected:
            errors.append(f"{label}_PAGE_COVERAGE {uid} expected={sorted(expected)} actual={sorted(covered)}")
    if materialization.get("pdf_text_page_count") != page_selector_count:
        errors.append(f"{label}_TEXT_PAGE_COUNT {uid} declared={materialization.get('pdf_text_page_count')} actual={page_selector_count}")
    if page_selector_count + derived_selector_count != total_selector_count:
        errors.append(f"{label}_NON_PAGE_SELECTOR {uid} pages={page_selector_count} declared_derived={derived_selector_count} selectors={total_selector_count}")
    return empty, failed


def validate_pdf_supplement(
    manifest: dict[str, Any], capsule_root: Path, declared_files: set[str],
    actual_hashes: dict[str, str], errors: list[str], *, repository_root: Path | None = None,
) -> int:
    """Validate the fixed main PDF and one explicitly required publisher SI."""
    supplement = manifest.get("pdf_supplement")
    if supplement is None:
        if (capsule_root / "pdf-supplement/document.pdf").is_file():
            errors.append(f"PDF_SUPPLEMENT_UNDECLARED {manifest.get('uid')}")
        if manifest.get("source_type") == "journal" or (
            manifest.get("source_type") == "arxiv" and manifest.get("adapter") == "arxiv_latex_v2"
        ):
            try:
                for path in ((repository_root or ROOT) / manifest["metadata_path"], capsule_root / "source-metadata.yaml"):
                    metadata = load_yaml(path)
                    versioning = metadata.get("versioning")
                    if versioning is not None and not isinstance(versioning, dict):
                        raise ValueError("publisher versioning must be a mapping or null")
                    if isinstance(versioning, dict) and "publisher_pdf" in versioning:
                        errors.append(f"PDF_SUPPLEMENT_DECLARATION_MISSING {manifest.get('uid')}")
                        break
            except (KeyError, TypeError, AttributeError, ValueError, OSError, yaml.YAMLError) as exc:
                errors.append(f"PDF_SUPPLEMENT_VERSION {manifest.get('uid')}: {exc}")
        return 0
    uid = str(manifest.get("uid") or "")
    label = "PDF_SUPPLEMENT"
    repo_root = repository_root or ROOT
    if not isinstance(supplement, dict):
        errors.append(f"{label}_DECLARATION {uid}")
        return 0
    from materialize_all_sources import pdf_supplement_version_urls
    try:
        metadata = load_yaml(repo_root / manifest["metadata_path"])
        capsule = load_yaml(capsule_root / "source-metadata.yaml")
        version_url, si_url = pdf_supplement_version_urls(manifest, metadata, capsule, supplement.get("source_version"))
        publisher = supplement["source_version"].startswith("publisher-vor:")
        si = supplement.get("supplementary_information")
        if (si_url is not None) != (si is not None):
            raise ValueError("required publisher SI is missing or an undeclared SI is present")
        if (capsule_root / "pdf-supplement/supplementary-information").exists() and si_url is None:
            raise ValueError("retained SI files have no publisher declaration")
        if si is not None and (not isinstance(si, dict) or "supplementary_information" in si or si.get("source_version") != supplement.get("source_version")):
            raise ValueError("SI must be one PDF belonging to the same declared publisher version")
    except (KeyError, TypeError, AttributeError, ValueError, OSError, yaml.YAMLError) as exc:
        errors.append(f"{label}_VERSION {uid}: {exc}")
        return 0
    parts = [(supplement, "pdf-supplement", version_url, label)]
    if si_url is not None:
        parts.append((si, "pdf-supplement/supplementary-information", si_url, f"{label}_SI"))
    selector_count = sum(
        _validate_pdf_supplement_part(
            manifest, part, directory, approved_url, capsule_root, declared_files, actual_hashes, errors,
            repo_root=repo_root, label=part_label, publisher=publisher,
        )
        for part, directory, approved_url, part_label in parts
    )
    # A new allowance is independent of any historical root-document publication block.
    from validate_publication_rights import validate_pdf_supplement_rights
    try:
        audit = load_yaml(repo_root / "raw_data/audits/materialization_rights_review.yaml")
        review = next((row for row in audit["items"] if isinstance(row, dict) and row.get("uid") == uid), None)
        rights_errors, rights_blocks = validate_pdf_supplement_rights(manifest, capsule_root / "manifest.yaml", repo_root, review)
        errors.extend(rights_errors)
        errors.extend(f"{label}_UNADMITTED {message}" for message in rights_blocks)
    except (KeyError, TypeError, ValueError, OSError, yaml.YAMLError) as exc:
        errors.append(f"{label}_RIGHTS_AUDIT {uid}: {exc}")
    return selector_count


def _validate_pdf_supplement_part(
    manifest: dict[str, Any], supplement: dict[str, Any], directory: str, version_url: str,
    capsule_root: Path, declared_files: set[str], actual_hashes: dict[str, str], errors: list[str],
    *, repo_root: Path, label: str, publisher: bool,
) -> int:
    """Apply the same native page checks independently to each retained PDF."""
    uid = str(manifest.get("uid") or "")
    def local_relative(path: Path) -> str:
        return path.relative_to(repo_root).as_posix()
    from materialize_all_sources import extract_pdf_text, pdf_supplement_retrieval_url_matches
    materialization = supplement.get("materialization")
    if not isinstance(materialization, dict):
        errors.append(f"{label}_MATERIALIZATION {uid}")
        return 0
    if materialization.get("pdf_text_extraction_mode") != "plain":
        errors.append(f"{label}_EXTRACTION_MODE {uid}")
    expected_paths = {"source_pdf": f"{directory}/document.pdf", "document": f"{directory}/document.txt", "normalized_document": f"{directory}/document.txt"}
    if any(materialization.get(field) != value for field, value in expected_paths.items()) or supplement.get("selectors") != [f"{directory}/selectors.jsonl"]:
        errors.append(f"{label}_PATHS {uid}")
    if supplement.get("media_type") != "application/pdf" or not isinstance(supplement.get("body_quality_verified"), bool):
        errors.append(f"{label}_MEDIA_OR_QUALITY {uid}")
    if not isinstance(supplement.get("limitations"), list) or any(not isinstance(value, str) or not value.strip() for value in supplement["limitations"]):
        errors.append(f"{label}_LIMITATIONS {uid}")
    paths = {name: capsule_root / directory / name for name in ("document.pdf", "document.txt", "selectors.jsonl", "NOTICE.md")}
    if any(
        local_relative(path) not in declared_files or not path.is_file()
        or scoped_path(local_relative(path), capsule_root, repository_root=repo_root) is None
        for path in paths.values()
    ):
        errors.append(f"{label}_FILE_UNHASHED_OR_MISSING {uid}")
        return 0
    # Consumers can pass manifest hashes: read every actual SI file rather than trusting that map.
    observed_hashes = {}
    for name, path in paths.items():
        relative = local_relative(path)
        observed_hashes[name] = sha256_file(path)
        inventory = [row for row in manifest.get("local_files", []) if row.get("path") == relative]
        if (
            actual_hashes.get(relative) != observed_hashes[name] or len(inventory) != 1
            or inventory[0].get("bytes") != path.stat().st_size or inventory[0].get("sha256") != observed_hashes[name]
        ):
            errors.append(f"{label}_FILE_INVENTORY_DRIFT {uid} {relative}")
    source = paths["document.pdf"]
    source_hash = observed_hashes["document.pdf"]
    if not source_hash or materialization.get("source_pdf_sha256") != source_hash or supplement.get("revision") != f"sha256:{source_hash}":
        errors.append(f"{label}_REVISION {uid}")
    retrievals = supplement.get("retrievals")
    retrieval = retrievals[0] if isinstance(retrievals, list) and len(retrievals) == 1 and isinstance(retrievals[0], dict) else {}
    if (
        not pdf_supplement_retrieval_url_matches(retrieval, version_url, publisher=publisher)
        or retrieval.get("sha256") != source_hash or retrieval.get("bytes") != source.stat().st_size
        or not isinstance(retrieval.get("retrieved_at"), str) or not retrieval["retrieved_at"].strip()
        or not isinstance(retrieval.get("content_type"), str) or retrieval["content_type"].split(";", 1)[0].strip() != "application/pdf"
    ):
        errors.append(f"{label}_RETRIEVAL {uid}")
    try:
        payload = source.read_bytes()
        if not payload.startswith(b"%PDF-"):
            raise ValueError("source is not a PDF")
        native_text, _, page_count = extract_pdf_text(payload, extraction_mode="plain")
        # Native PDF glyphs can include CR: universal-newline reads would alter them.
        stored_text = paths["document.txt"].read_bytes().decode("utf-8")
        source_text = stored_text.split("<!-- materialization-redistribution-notice -->", 1)[0].rstrip() + "\n"
        if source_text != native_text:
            errors.append(f"{label}_NATIVE_TEXT_DRIFT {uid}")
        rows = [json.loads(line) for line in paths["selectors.jsonl"].read_text(encoding="utf-8").splitlines() if line.strip()]
    except Exception as exc:
        errors.append(f"{label}_PARSE {uid}: {exc}")
        return 0
    if supplement.get("primary_excerpt") is not None:
        try:
            pdf_primary_excerpt_range(supplement, native_text)
        except ValueError as exc:
            errors.append(f"{label}_PRIMARY_EXCERPT {uid}: {exc}")
    if materialization.get("pdf_page_count") != page_count or materialization.get("stored_characters") != len(stored_text):
        errors.append(f"{label}_PAGE_OR_CHARACTER_COUNT {uid}")
    sections, duplicates = pdf_page_sections(native_text)
    if duplicates or set(sections) != set(range(1, page_count + 1)):
        errors.append(f"{label}_PAGE_MARKERS {uid}")
    seen_pages: set[int] = set()
    seen_ids: set[str] = set()
    page_selectors = 0
    target = local_relative(paths["document.txt"])
    for index, selector in enumerate(rows, 1):
        if not isinstance(selector, dict):
            errors.append(f"{label}_SELECTOR_NOT_OBJECT {uid}:{index}")
            continue
        selector_id = selector.get("selector")
        if not isinstance(selector_id, str) or not selector_id or selector_id in seen_ids:
            errors.append(f"{label}_SELECTOR_ID {uid}:{index}")
        else:
            seen_ids.add(selector_id)
        preview = selector.get("text_preview")
        if not isinstance(preview, str) or not preview or preview not in native_text:
            errors.append(f"{label}_SELECTOR_PREVIEW_UNRESOLVED {uid}:{index}")
        path = scoped_path(selector.get("local_path"), capsule_root, repository_root=repo_root)
        if path is None or not path.is_file() or selector.get("local_path") not in declared_files:
            errors.append(f"{label}_SELECTOR_TARGET {uid}:{index}")
        if selector.get("kind") != "page" or any(field in selector for field in ("start_line", "end_line", "ordinal", "source_page")):
            errors.append(f"{label}_SELECTOR_KIND {uid}:{index}")
        if selector.get("page") is not None:
            page_selectors += 1
            validate_pdf_page_binding(selector, target, sections, f"pdf://sha256-{(source_hash or '')[:16]}#page=", page_count, seen_pages, f"{uid}:{index}", errors, label=label)
        else:
            errors.append(f"{label}_SELECTOR_PAGE {uid}:{index}")
    empty, failed = validate_pdf_page_coverage(materialization, page_count, seen_pages, page_selectors, len(rows), uid, errors, label=label)
    actual_empty = {page for page, text in sections.items() if not text.strip()}
    actual_failed = {page for page, text in sections.items() if text.strip().startswith("[page extraction failed:")}
    if empty != actual_empty or failed != actual_failed:
        errors.append(f"{label}_EXTRACTION_DIAGNOSTICS {uid}")
    if materialization.get("selector_count") != len(rows):
        errors.append(f"{label}_SELECTOR_COUNT {uid}")
    from materialize_all_sources import has_substantive_document_text
    if materialization.get("substantive_text") != has_substantive_document_text(native_text) or (
        supplement.get("body_quality_verified") is True and (materialization.get("substantive_text") is not True or failed)
    ):
        errors.append(f"{label}_FALSE_BODY_QUALITY {uid}")
    return len(rows)


def pdf_image_transcription_declaration(
    materialization: dict[str, Any], capsule_root: Path, declared_files: set[str],
    page_count: int | None, uid: str, errors: list[str],
) -> tuple[str | None, set[int], str | None]:
    """Permit derived page text only with an explicit, source-bound declaration."""
    declaration = materialization.get("image_page_transcription")
    if declaration is None:
        return None, set(), None
    if not isinstance(declaration, dict):
        errors.append(f"ARXIV_PDF_TRANSCRIPTION_DECLARATION {uid}")
        return None, set(), None
    valid = True

    def reject(detail: str) -> None:
        nonlocal valid
        errors.append(f"ARXIV_PDF_TRANSCRIPTION_PROVENANCE {uid} {detail}")
        valid = False

    document = declaration.get("document")
    document_path: Path | None = None
    if isinstance(document, str) and document and not Path(document).is_absolute() and ".." not in Path(document).parts:
        candidate = capsule_root / document
        try:
            candidate.resolve().relative_to((capsule_root / "derived").resolve())
            if candidate.is_file():
                document_path = candidate
        except (OSError, ValueError):
            pass
    document_rel = relative(document_path) if document_path is not None else None
    if document_rel is None or document_rel not in declared_files or document == materialization.get("document"):
        reject(f"document={document!r} must be a separately inventoried derived text file")
    for field in ("renderer", "model_revision", "scope"):
        value = declaration.get(field)
        if not isinstance(value, str) or not value.strip():
            reject(f"{field} is required (use an explicit not_exposed value when appropriate)")
    method = declaration.get("method")
    if not isinstance(method, str) or method not in {"agent_visual_transcription", "manual_transcription"}:
        reject(f"method={method!r}")
    if declaration.get("native_text_extraction_changed") is not False:
        reject("native_text_extraction_changed must be false")
    if declaration.get("conventional_ocr_performed") is not False:
        reject("visual/manual transcription must not claim conventional OCR")
    if not isinstance(declaration.get("complete_image_representation"), bool):
        reject("complete_image_representation must explicitly state the retained boundary")

    source_pages = declaration.get("source_pages")
    pages: set[int] = set()
    if not isinstance(source_pages, list) or not source_pages or any(
        not isinstance(page, int) or isinstance(page, bool) or page < 1
        or page_count is None or page > page_count for page in source_pages
    ):
        reject(f"source_pages={source_pages!r}")
    else:
        pages = set(source_pages)
        if len(pages) != len(source_pages):
            reject("source_pages must be unique")
        gaps = materialization.get("pdf_pages_without_extractable_text")
        failures = materialization.get("pdf_page_extraction_failures")
        if not isinstance(gaps, list) or not isinstance(failures, list) or not all(page in gaps or page in failures for page in pages):
            reject("source_pages must remain acknowledged native extraction gaps")
    render_dpi = declaration.get("render_dpi")
    if not isinstance(render_dpi, dict) or any(not isinstance(page, int) or isinstance(page, bool) for page in render_dpi) or set(render_dpi) != pages or any(
        not isinstance(dpi, int) or isinstance(dpi, bool) or dpi < 1 for dpi in render_dpi.values()
    ):
        reject("render_dpi must declare a positive resolution for every source page")
    return (document_rel, pages, method) if valid else (None, set(), None)


def evidence_role_for(status: Any, content_tier: Any) -> str:
    if status in {"metadata_only", "failed"} or content_tier == "metadata_capsule":
        return "catalog-only"
    if status == "partial" or content_tier == "excerpt_capsule":
        return "bounded-excerpt"
    if content_tier == "semantic_capsule":
        return "static-repository-evidence"
    return "source-text"


def compare_item_to_manifest(
    *,
    label: str,
    item: dict[str, Any],
    manifest: dict[str, Any],
    fields: tuple[tuple[str, str], ...],
    errors: list[str],
) -> None:
    uid = str(item.get("uid") or "")
    for item_field, manifest_field in fields:
        if item.get(item_field) != manifest.get(manifest_field):
            errors.append(
                f"{label}_FIELD_MISMATCH {uid} {item_field}="
                f"{item.get(item_field)!r} manifest={manifest.get(manifest_field)!r}"
            )


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    metadata_paths = sorted(RAW.rglob("metadata.yaml"))
    metadata_rel_paths = {relative(path) for path in metadata_paths}
    manifests = sorted(CORPUS.glob("*/manifest.yaml")) if CORPUS.exists() else []
    if len(manifests) != len(metadata_paths):
        errors.append(f"CAPSULE_COUNT metadata={len(metadata_paths)} manifests={len(manifests)}")

    seen_uids: set[str] = set()
    manifest_by_uid: dict[str, tuple[Path, dict[str, Any]]] = {}
    metadata_references: Counter[str] = Counter()
    tiers: Counter[str] = Counter()
    statuses: Counter[str] = Counter()
    hashed_files = 0
    selector_count = 0

    for manifest_path in manifests:
        manifest = load_yaml_checked(manifest_path, "MANIFEST", errors)
        if not isinstance(manifest, dict):
            if manifest is not None:
                errors.append(f"MANIFEST_NOT_OBJECT {relative(manifest_path)}")
            continue

        uid = str(manifest.get("uid") or "")
        if not uid:
            errors.append(f"MANIFEST_UID_MISSING {relative(manifest_path)}")
        elif uid in seen_uids:
            errors.append(f"DUPLICATE_UID {uid}")
        else:
            manifest_by_uid[uid] = (manifest_path, manifest)
        seen_uids.add(uid)

        tier = str(manifest.get("content_tier") or "")
        status = str(manifest.get("status") or "")
        if tier not in CONTENT_TIERS:
            errors.append(f"BAD_CONTENT_TIER {uid} {tier}")
        if status not in STATUSES:
            errors.append(f"BAD_STATUS {uid} {status}")
        tiers[tier] += 1
        statuses[status] += 1

        if status == "materialized" and tier not in {"full_text", "semantic_capsule"}:
            errors.append(f"STATUS_TIER_MISMATCH {uid} {status} {tier}")
        if status in {"metadata_only", "failed"} and tier != "metadata_capsule":
            errors.append(f"STATUS_TIER_MISMATCH {uid} {status} {tier}")
        if status in {"partial", "metadata_only", "failed"} and not any(
            manifest.get(field) for field in ("errors", "warnings", "limitations")
        ):
            errors.append(f"INCOMPLETE_WITHOUT_DIAGNOSTIC {uid} {status} {tier}")

        metadata_path = manifest.get("metadata_path")
        if isinstance(metadata_path, str):
            metadata_references[metadata_path] += 1
        if not isinstance(metadata_path, str) or metadata_path not in metadata_rel_paths:
            errors.append(f"BROKEN_METADATA_PATH {uid} {metadata_path}")
            metadata_file = None
        else:
            metadata_file = ROOT / metadata_path

        capsule_root = manifest_path.parent
        local_files = manifest.get("local_files")
        declared_files: set[str] = set()
        actual_hashes: dict[str, str] = {}
        declared_bytes = 0
        if not isinstance(local_files, list):
            errors.append(f"LOCAL_FILES_MISSING {uid}")
            local_files = []
        for item in local_files:
            if not isinstance(item, dict):
                errors.append(f"LOCAL_FILE_BAD_ENTRY {uid}")
                continue
            raw_path = item.get("path")
            expected_hash = item.get("sha256")
            if not isinstance(raw_path, str) or not isinstance(expected_hash, str):
                errors.append(f"LOCAL_FILE_FIELDS {uid} {item}")
                continue
            if raw_path in declared_files:
                errors.append(f"LOCAL_FILE_DUPLICATE {uid} {raw_path}")
                continue
            declared_files.add(raw_path)
            path = scoped_path(raw_path, capsule_root)
            if path is None:
                errors.append(f"LOCAL_FILE_OUTSIDE_CAPSULE {uid} {raw_path}")
                continue
            if not path.is_file():
                errors.append(f"LOCAL_FILE_MISSING {uid} {raw_path}")
                continue
            try:
                actual_hash = sha256_file(path)
                actual_bytes = path.stat().st_size
            except OSError as exc:
                errors.append(f"LOCAL_FILE_READ {uid} {raw_path}: {exc}")
                continue
            hashed_files += 1
            declared_bytes += actual_bytes
            actual_hashes[raw_path] = actual_hash
            if actual_hash != expected_hash:
                errors.append(f"HASH_MISMATCH {uid} {raw_path}")
            expected_bytes = item.get("bytes")
            if not isinstance(expected_bytes, int) or isinstance(expected_bytes, bool) or expected_bytes != actual_bytes:
                errors.append(f"BYTE_COUNT_MISMATCH {uid} {raw_path} expected={expected_bytes} actual={actual_bytes}")

        actual_files = {
            relative(path)
            for path in capsule_root.rglob("*")
            if path.is_file() and path != manifest_path
        }
        for path in sorted(actual_files - declared_files):
            errors.append(f"UNHASHED_LOCAL_FILE {uid} {path}")
        for path in sorted(declared_files - actual_files):
            errors.append(f"DECLARED_LOCAL_FILE_ABSENT {uid} {path}")
        if manifest.get("local_bytes") != declared_bytes:
            errors.append(
                f"LOCAL_BYTES_MISMATCH {uid} expected={manifest.get('local_bytes')} actual={declared_bytes}"
            )

        validate_retained_markdown_binding(manifest, capsule_root, actual_hashes, errors)
        validate_tex_reading_view(manifest, capsule_root, actual_hashes, errors)

        source_metadata_path = capsule_root / "source-metadata.yaml"
        if metadata_file is not None and source_metadata_path.is_file():
            source_metadata = load_yaml_checked(source_metadata_path, "SOURCE_METADATA", errors)
            canonical_metadata = load_yaml_checked(metadata_file, "CANONICAL_METADATA", errors)
            if source_metadata is not None and canonical_metadata is not None and source_metadata != canonical_metadata:
                errors.append(f"SOURCE_METADATA_MISMATCH {uid} {metadata_path}")
        else:
            errors.append(f"SOURCE_METADATA_MISSING {uid}")

        expected_pdf_selector_prefix: str | None = None
        arxiv_pdf_page_count: int | None = None
        arxiv_pdf_materialization: dict[str, Any] | None = None
        arxiv_pdf_selector_pages: set[int] = set()
        arxiv_pdf_selector_count = 0
        arxiv_pdf_derived_selector_count = 0
        arxiv_pdf_derived_selector_pages: set[int] = set()
        image_transcription_path: str | None = None
        image_transcription_pages: set[int] = set()
        image_transcription_method: str | None = None
        if manifest.get("source_type") == "arxiv":
            adapter = manifest.get("adapter")
            if adapter == "arxiv_latex_v2":
                for raw_path in sorted(declared_files):
                    if Path(raw_path).suffix.lower() not in {".tex", ".ltx"}:
                        continue
                    path = scoped_path(raw_path, capsule_root)
                    if path is not None and path.is_file():
                        try:
                            with path.open("rb") as handle:
                                magic = handle.read(5)
                            if magic == b"%PDF-":
                                errors.append(f"ARXIV_PDF_AS_TEX {uid} {raw_path}")
                        except OSError as exc:
                            errors.append(f"ARXIV_TEX_SNIFF {uid} {raw_path}: {exc}")
            if adapter == "arxiv_pdf_v1" and manifest.get("archive_container") not in {"pdf", "gzip-pdf"}:
                errors.append(f"ARXIV_PDF_CONTAINER {uid} {manifest.get('archive_container')}")
            if adapter == "arxiv_pdf_v1" and manifest.get("archive_container") in {"pdf", "gzip-pdf"}:
                materialization = manifest.get("materialization")
                if not isinstance(materialization, dict):
                    errors.append(f"ARXIV_PDF_MATERIALIZATION {uid}")
                    materialization = {}
                arxiv_pdf_materialization = materialization
                if manifest.get("media_type") != "application/pdf":
                    errors.append(f"ARXIV_PDF_MEDIA_TYPE {uid} {manifest.get('media_type')}")
                source_pdf = materialization.get("source_pdf")
                source_pdf_path: Path | None = None
                if isinstance(source_pdf, str) and source_pdf:
                    candidate = capsule_root / source_pdf
                    try:
                        candidate.resolve().relative_to(capsule_root.resolve())
                        source_pdf_path = candidate
                    except (OSError, ValueError):
                        pass
                if source_pdf_path is None or not source_pdf_path.is_file():
                    errors.append(f"ARXIV_PDF_SOURCE_MISSING {uid} {source_pdf}")
                else:
                    source_pdf_rel = relative(source_pdf_path)
                    source_pdf_hash = actual_hashes.get(source_pdf_rel)
                    if source_pdf_rel not in declared_files:
                        errors.append(f"ARXIV_PDF_SOURCE_UNHASHED {uid} {source_pdf_rel}")
                    try:
                        with source_pdf_path.open("rb") as handle:
                            magic = handle.read(5)
                        if magic != b"%PDF-":
                            errors.append(f"ARXIV_PDF_MAGIC {uid} {source_pdf_rel}")
                    except OSError as exc:
                        errors.append(f"ARXIV_PDF_READ {uid} {source_pdf_rel}: {exc}")
                    try:
                        from pypdf import PdfReader

                        arxiv_pdf_page_count = len(PdfReader(source_pdf_path).pages)
                    except Exception as exc:
                        errors.append(f"ARXIV_PDF_PARSE {uid} {source_pdf_rel}: {exc}")
                    if materialization.get("pdf_page_count") != arxiv_pdf_page_count:
                        errors.append(
                            f"ARXIV_PDF_PAGE_COUNT {uid} declared={materialization.get('pdf_page_count')} "
                            f"actual={arxiv_pdf_page_count}"
                        )
                    if not source_pdf_hash or materialization.get("source_pdf_sha256") != source_pdf_hash:
                        errors.append(
                            f"ARXIV_PDF_HASH {uid} declared={materialization.get('source_pdf_sha256')} "
                            f"actual={source_pdf_hash}"
                        )
                    if source_pdf_hash:
                        expected_pdf_selector_prefix = f"pdf://sha256-{source_pdf_hash[:16]}#page="

                    retrievals = manifest.get("retrievals")
                    transport_hash = None
                    if isinstance(retrievals, list) and retrievals and isinstance(retrievals[-1], dict):
                        transport_hash = retrievals[-1].get("sha256")
                    if not isinstance(transport_hash, str) or manifest.get("revision") != f"sha256:{transport_hash}":
                        errors.append(f"ARXIV_PDF_TRANSPORT_REVISION {uid}")
                    if manifest.get("archive_container") == "pdf" and transport_hash != source_pdf_hash:
                        errors.append(f"ARXIV_PDF_RAW_HASH {uid}")

                failures = materialization.get("pdf_page_extraction_failures")
                pages_without_text = materialization.get("pdf_pages_without_extractable_text")
                if tier == "full_text" and (materialization.get("substantive_text") is not True or failures):
                    errors.append(f"ARXIV_PDF_FALSE_FULL_TEXT {uid}")
                if status == "materialized" and pages_without_text:
                    errors.append(f"ARXIV_PDF_UNACKNOWLEDGED_TEXT_GAPS {uid}")
                image_transcription_path, image_transcription_pages, image_transcription_method = pdf_image_transcription_declaration(
                    materialization, capsule_root, declared_files, arxiv_pdf_page_count, uid, errors,
                )

        selectors_path = capsule_root / "selectors.jsonl"
        selector_paths = [selectors_path]
        try:
            from materialize_all_sources import retained_text_selector_file
            sidecar = retained_text_selector_file(manifest, capsule_root, require_exists=True)
            if manifest.get("selectors") == ["normalized/selectors.jsonl"]:
                selectors_path = sidecar
                selector_paths = [sidecar]
            elif sidecar != selectors_path:
                selector_paths.append(sidecar)
        except (KeyError, TypeError, AttributeError, ValueError, OSError) as exc:
            errors.append(f"RETAINED_TEXT_SELECTORS {uid}: {exc}")
        selector_declaration = manifest.get("selectors")
        if not isinstance(selector_declaration, list):
            errors.append(f"SELECTOR_DECLARATION_BAD {uid}")
            selector_declaration = []
        if tier != "metadata_capsule" and selectors_path.relative_to(capsule_root).as_posix() not in selector_declaration:
            errors.append(f"SELECTOR_DECLARATION_MISSING {uid}")
        if tier != "metadata_capsule" and not selectors_path.exists():
            errors.append(f"SELECTORS_MISSING {uid}")

        manifest_selector_count = 0
        valid_selector_count = 0
        seen_selectors: set[str] = set()
        target_text: dict[str, str] = {}
        target_pdf_sections: dict[str, tuple[dict[int, str], set[int]]] = {}
        if selectors_path.exists():
            try:
                selector_lines = [line for path in selector_paths for line in path.read_text(encoding="utf-8").splitlines()]
            except (OSError, UnicodeError) as exc:
                errors.append(f"SELECTORS_READ {uid}: {exc}")
                selector_lines = []
            for line_number, line in enumerate(selector_lines, 1):
                if not line.strip():
                    continue
                try:
                    selector = json.loads(line)
                except json.JSONDecodeError as exc:
                    errors.append(f"SELECTOR_JSON {uid}:{line_number}: {exc}")
                    continue
                manifest_selector_count += 1
                selector_count += 1
                if not isinstance(selector, dict):
                    errors.append(f"SELECTOR_NOT_OBJECT {uid}:{line_number}")
                    continue

                selector_id = selector.get("selector")
                if not isinstance(selector_id, str) or not selector_id:
                    errors.append(f"SELECTOR_ID {uid}:{line_number}: {selector_id}")
                elif selector_id in seen_selectors:
                    errors.append(f"SELECTOR_DUPLICATE {uid}:{line_number}: {selector_id}")
                else:
                    seen_selectors.add(selector_id)

                local_path = selector.get("local_path")
                path = scoped_path(local_path, capsule_root)
                if path is None or not path.is_file():
                    errors.append(f"SELECTOR_TARGET {uid}:{line_number}: {local_path}")
                    continue
                if local_path not in declared_files:
                    errors.append(f"SELECTOR_TARGET_UNHASHED {uid}:{line_number}: {local_path}")
                    continue
                if local_path not in target_text:
                    try:
                        target_text[local_path] = path.read_text(encoding="utf-8")
                    except (OSError, UnicodeError) as exc:
                        errors.append(f"SELECTOR_TARGET_READ {uid}:{line_number}: {local_path}: {exc}")
                        continue
                text = target_text[local_path]

                selector_valid = True
                derived_transcription_selector = False
                preview = selector.get("text_preview")
                if preview is not None:
                    if not isinstance(preview, str) or not preview or preview not in text:
                        errors.append(f"SELECTOR_PREVIEW_UNRESOLVED {uid}:{line_number}: {selector_id}")
                        selector_valid = False

                start_line = selector.get("start_line")
                end_line = selector.get("end_line")
                line_range_valid = False
                if start_line is not None or end_line is not None:
                    line_count = max(1, len(text.splitlines()))
                    if (
                        not isinstance(start_line, int)
                        or isinstance(start_line, bool)
                        or not isinstance(end_line, int)
                        or isinstance(end_line, bool)
                        or start_line < 1
                        or end_line < start_line
                        or end_line > line_count
                    ):
                        errors.append(
                            f"SELECTOR_LINE_RANGE {uid}:{line_number}: "
                            f"{start_line}-{end_line} target_lines={line_count}"
                        )
                        selector_valid = False
                    else:
                        line_range_valid = True

                page = selector.get("page")
                if page is not None:
                    if local_path not in target_pdf_sections:
                        target_pdf_sections[local_path] = pdf_page_sections(text)
                    page_sections, duplicate_markers = target_pdf_sections[local_path]
                    if (
                        not isinstance(page, int)
                        or isinstance(page, bool)
                        or page < 1
                        or page not in page_sections
                    ):
                        errors.append(f"SELECTOR_PAGE_UNRESOLVED {uid}:{line_number}: {page}")
                        selector_valid = False
                    for duplicate_page in sorted(duplicate_markers):
                        errors.append(
                            f"PDF_PAGE_MARKER_DUPLICATE {uid}:{line_number}: {duplicate_page}"
                        )
                        selector_valid = False
                    if expected_pdf_selector_prefix is not None:
                        arxiv_pdf_selector_count += 1
                        native_document = arxiv_pdf_materialization.get("document") if arxiv_pdf_materialization else None
                        native_document_rel = relative(capsule_root / native_document) if (
                            isinstance(native_document, str) and not Path(native_document).is_absolute()
                            and ".." not in Path(native_document).parts
                        ) else None
                        if not validate_pdf_page_binding(
                            selector, native_document_rel, page_sections, expected_pdf_selector_prefix,
                            arxiv_pdf_page_count, arxiv_pdf_selector_pages, f"{uid}:{line_number}", errors,
                        ):
                            selector_valid = False

                if expected_pdf_selector_prefix is not None and page is None and image_transcription_path is not None:
                    source_page = selector.get("source_page")
                    uri_match = re.fullmatch(r"derived://[^#\s]+#L([1-9]\d*)-L([1-9]\d*)", selector_id) if isinstance(selector_id, str) else None
                    if (
                        local_path != image_transcription_path or selector.get("kind") != "line_range"
                        or "page" in selector or not isinstance(source_page, int) or isinstance(source_page, bool)
                        or source_page not in image_transcription_pages
                        or selector.get("extraction_method") != image_transcription_method
                        or not line_range_valid or uri_match is None
                        or int(uri_match.group(1)) != start_line or int(uri_match.group(2)) != end_line
                    ):
                        errors.append(f"ARXIV_PDF_TRANSCRIPTION_SELECTOR {uid}:{line_number}: {selector_id}")
                        selector_valid = False
                    if not isinstance(preview, str) or not preview or not line_range_valid or preview not in "\n".join(text.splitlines()[start_line - 1:end_line]):
                        errors.append(f"ARXIV_PDF_TRANSCRIPTION_PREVIEW_RANGE {uid}:{line_number}: {selector_id}")
                        selector_valid = False
                    derived_transcription_selector = True

                ordinal = selector.get("ordinal")
                if ordinal is not None and (
                    not isinstance(ordinal, int) or isinstance(ordinal, bool) or ordinal < 1
                ):
                    errors.append(f"SELECTOR_ORDINAL {uid}:{line_number}: {ordinal}")
                    selector_valid = False
                if selector_valid:
                    valid_selector_count += 1
                    if derived_transcription_selector:
                        arxiv_pdf_derived_selector_count += 1
                        arxiv_pdf_derived_selector_pages.add(selector["source_page"])

        expected_selector_count = (
            manifest.get("materialization", {}).get("selector_count")
            if isinstance(manifest.get("materialization"), dict)
            else None
        )
        if expected_selector_count is not None and expected_selector_count != manifest_selector_count:
            errors.append(
                f"SELECTOR_COUNT_MISMATCH {uid} expected={expected_selector_count} actual={manifest_selector_count}"
            )
        if tier == "metadata_capsule" and manifest_selector_count:
            errors.append(f"METADATA_CAPSULE_HAS_SELECTORS {uid} count={manifest_selector_count}")
        if tier != "metadata_capsule" and valid_selector_count == 0:
            errors.append(f"NO_VALID_SELECTORS {uid}")
        if expected_pdf_selector_prefix is not None and arxiv_pdf_materialization is not None:
            validate_pdf_page_coverage(
                arxiv_pdf_materialization, arxiv_pdf_page_count, arxiv_pdf_selector_pages,
                arxiv_pdf_selector_count, manifest_selector_count, uid, errors,
                derived_selector_count=arxiv_pdf_derived_selector_count,
            )
            if image_transcription_path is not None and arxiv_pdf_derived_selector_pages != image_transcription_pages:
                errors.append(
                    f"ARXIV_PDF_TRANSCRIPTION_PAGE_COVERAGE {uid} declared={sorted(image_transcription_pages)} "
                    f"actual={sorted(arxiv_pdf_derived_selector_pages)}"
                )

        selector_count += validate_pdf_supplement(manifest, capsule_root, declared_files, actual_hashes, errors)

    for metadata_path, count in sorted(metadata_references.items()):
        if count > 1:
            errors.append(f"DUPLICATE_METADATA_REFERENCE {metadata_path} count={count}")
    for metadata_path in sorted(metadata_rel_paths - set(metadata_references)):
        errors.append(f"METADATA_WITHOUT_MANIFEST {metadata_path}")

    manifest_rel_paths = {relative(path) for path in manifests}
    for path, label in ((INDEX, "INDEX"), (REGISTRY, "REGISTRY"), (AUDIT, "AUDIT")):
        if not path.exists():
            errors.append(f"{label}_MISSING {relative(path)}")

    if INDEX.exists():
        index = load_yaml_checked(INDEX, "INDEX", errors)
        items = index.get("items") if isinstance(index, dict) else None
        if not isinstance(items, list):
            errors.append("INDEX_ITEMS_INVALID")
            items = []
        if len(items) != len(metadata_paths):
            errors.append(f"INDEX_COUNT expected={len(metadata_paths)} actual={len(items)}")
        index_uids: set[str] = set()
        index_manifests: set[str] = set()
        for item in items:
            if not isinstance(item, dict):
                errors.append("INDEX_ITEM_NOT_OBJECT")
                continue
            uid = str(item.get("uid") or "")
            manifest_ref = item.get("manifest")
            if not uid or uid in index_uids:
                errors.append(f"INDEX_UID_DUPLICATE_OR_MISSING {uid}")
            index_uids.add(uid)
            if not isinstance(manifest_ref, str) or manifest_ref in index_manifests:
                errors.append(f"INDEX_MANIFEST_DUPLICATE_OR_MISSING {manifest_ref}")
            if isinstance(manifest_ref, str):
                index_manifests.add(manifest_ref)
            linked = manifest_by_uid.get(uid)
            if linked is None:
                errors.append(f"INDEX_UID_UNKNOWN {uid}")
                continue
            linked_path, linked_manifest = linked
            if manifest_ref != relative(linked_path):
                errors.append(f"INDEX_MANIFEST_MISMATCH {uid} {manifest_ref}")
            compare_item_to_manifest(
                label="INDEX",
                item=item,
                manifest=linked_manifest,
                fields=(("status", "status"), ("content_tier", "content_tier"), ("revision", "revision"), ("local_bytes", "local_bytes")),
                errors=errors,
            )
        if index_uids != set(manifest_by_uid):
            errors.append("INDEX_UID_SET_MISMATCH")
        if index_manifests != manifest_rel_paths:
            errors.append("INDEX_MANIFEST_SET_MISMATCH")

    if REGISTRY.exists():
        registry = load_yaml_checked(REGISTRY, "REGISTRY", errors)
        entries = registry.get("entries") if isinstance(registry, dict) else None
        if not isinstance(entries, list):
            errors.append("REGISTRY_ENTRIES_INVALID")
            entries = []
        count = registry.get("entry_count") if isinstance(registry, dict) else None
        if count != len(entries) or len(entries) != len(metadata_paths):
            errors.append(
                f"REGISTRY_COUNT expected={len(metadata_paths)} declared={count} actual={len(entries)}"
            )
        registry_uids: set[str] = set()
        for entry in entries:
            if not isinstance(entry, dict):
                errors.append("REGISTRY_ENTRY_NOT_OBJECT")
                continue
            uid = str(entry.get("uid") or "")
            if not uid or uid in registry_uids:
                errors.append(f"REGISTRY_UID_DUPLICATE_OR_MISSING {uid}")
            registry_uids.add(uid)
            linked = manifest_by_uid.get(uid)
            if linked is None:
                errors.append(f"REGISTRY_UID_UNKNOWN {uid}")
                continue
            linked_path, linked_manifest = linked
            if entry.get("metadata_path") != linked_manifest.get("metadata_path"):
                errors.append(f"REGISTRY_METADATA_MISMATCH {uid}")
            materialization = entry.get("materialization")
            if not isinstance(materialization, dict):
                errors.append(f"REGISTRY_MATERIALIZATION_INVALID {uid}")
                continue
            if materialization.get("manifest") != relative(linked_path):
                errors.append(f"REGISTRY_MANIFEST_MISMATCH {uid}")
            expected_role = evidence_role_for(
                linked_manifest.get("status"), linked_manifest.get("content_tier")
            )
            if materialization.get("evidence_role") != expected_role:
                errors.append(
                    f"REGISTRY_EVIDENCE_ROLE_MISMATCH {uid} "
                    f"expected={expected_role} actual={materialization.get('evidence_role')}"
                )
            compare_item_to_manifest(
                label="REGISTRY",
                item={"uid": uid, **materialization},
                manifest=linked_manifest,
                fields=(("state", "status"), ("content_tier", "content_tier"), ("revision", "revision"), ("local_bytes", "local_bytes")),
                errors=errors,
            )
        if registry_uids != set(manifest_by_uid):
            errors.append("REGISTRY_UID_SET_MISMATCH")

    if AUDIT.exists():
        audit = load_yaml_checked(AUDIT, "AUDIT", errors)
        if not isinstance(audit, dict):
            errors.append("AUDIT_NOT_OBJECT")
        else:
            expected_audit_fields = {
                "collection_records": len(metadata_paths),
                "local_capsules": len(manifests),
                "all_records_local": len(manifests) == len(metadata_paths),
                "status_counts": dict(statuses),
                "content_tier_counts": dict(tiers),
                "metadata_only_count": tiers["metadata_capsule"],
                "partial_count": statuses["partial"],
                "hashed_files": hashed_files,
            }
            for field, expected in expected_audit_fields.items():
                if audit.get(field) != expected:
                    errors.append(
                        f"AUDIT_FIELD_MISMATCH {field} expected={expected!r} actual={audit.get(field)!r}"
                    )
            acceptance = audit.get("acceptance")
            if not isinstance(acceptance, dict) or not all(
                acceptance.get(field)
                for field in (
                    "all_metadata_records_have_local_manifest",
                    "no_unclassified_missing_capsule",
                    "full_content_gaps_are_explicit",
                )
            ):
                errors.append("AUDIT_ACCEPTANCE_FALSE_OR_MISSING")

    print(
        "materialization_completeness_validation "
        f"metadata={len(metadata_paths)} manifests={len(manifests)} "
        f"tiers={dict(tiers)} statuses={dict(statuses)} "
        f"hashes={hashed_files} selectors={selector_count} "
        f"warnings={len(warnings)} errors={len(errors)}"
    )
    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"- {warning}")
    if errors:
        print("\nErrors:")
        error_limit = 50
        for error in errors[:error_limit]:
            print(f"- {error}")
        if len(errors) > error_limit:
            print(f"- ... {len(errors) - error_limit} additional errors omitted")
        return 1
    print("\nAll collected source records have validated local capsules.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

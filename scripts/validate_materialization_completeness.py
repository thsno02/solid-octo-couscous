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


def validate_retained_markdown_binding(
    manifest: dict[str, Any], capsule_root: Path, actual_hashes: dict[str, str],
    errors: list[str], *, repository_root: Path | None = None,
) -> None:
    """Bind an opt-in retained Markdown original to its inventory and retrieval."""
    materialization = manifest.get("materialization")
    if isinstance(materialization, dict) and "retained_text_sources" in materialization:
        validate_retained_text_binding(manifest, capsule_root, actual_hashes, errors, repository_root=repository_root)
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
    errors: list[str], *, repository_root: Path | None = None,
) -> None:
    """Bind the finite native-text assembly to existing per-file snapshot evidence."""
    materialization = manifest["materialization"]
    uid = manifest.get("uid")
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
            or source_name in names or not isinstance(format_name, str) or format_name not in {"md", "yaml"}
            or Path(source_name).suffix.lower() not in ({".md"} if format_name == "md" else {".yaml", ".yml"})
        ):
            errors.append(f"RETAINED_TEXT_SOURCE_PATH_FORMAT {uid}: {source_name}")
            continue
        names.add(source_name)
        source_relative = (capsule_root / source_name).relative_to(repo_root).as_posix()
        source = scoped_path(source_relative, capsule_root, repository_root=repo_root)
        source_hash = actual_hashes.get(source_relative)
        if source is None or not source.is_file() or not source_hash:
            errors.append(f"RETAINED_TEXT_SOURCE_UNHASHED {uid}: {source_name}")
            continue
        inventory = manifest.get("local_files")
        rows = [row for row in inventory if isinstance(row, dict) and row.get("path") == source_relative] if isinstance(inventory, list) else []
        if len(rows) != 1 or rows[0].get("sha256") != source_hash or rows[0].get("bytes") != source.stat().st_size:
            errors.append(f"RETAINED_TEXT_INVENTORY {uid}: {source_name}")
        retrievals = manifest.get("retrievals")
        rows = [row for row in retrievals if isinstance(row, dict) and row.get("local_path") == source_name] if isinstance(retrievals, list) else []
        if len(rows) != 1 or rows[0].get("sha256") != source_hash or rows[0].get("bytes") != source.stat().st_size or rows[0].get("commit") != commit:
            errors.append(f"RETAINED_TEXT_RETRIEVAL {uid}: {source_name}")


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
    """Validate only the optional, fixed-version PDF alongside the unchanged TeX representation."""
    supplement = manifest.get("pdf_supplement")
    if supplement is None:
        if (capsule_root / "pdf-supplement/document.pdf").is_file():
            errors.append(f"PDF_SUPPLEMENT_UNDECLARED {manifest.get('uid')}")
        return 0
    uid = str(manifest.get("uid") or "")
    label = "PDF_SUPPLEMENT"
    repo_root = repository_root or ROOT
    def local_relative(path: Path) -> str:
        return path.relative_to(repo_root).as_posix()
    if not isinstance(supplement, dict) or manifest.get("adapter") != "arxiv_latex_v2" or manifest.get("source_type") != "arxiv":
        errors.append(f"{label}_DECLARATION {uid}")
        return 0
    from materialize_all_sources import arxiv_pdf_version_url, extract_pdf_text
    try:
        version_url = arxiv_pdf_version_url(manifest.get("canonical_id"), supplement.get("source_version"))
        metadata = load_yaml(repo_root / manifest["metadata_path"])
        if (metadata.get("versioning") or {}).get("source_version") != supplement.get("source_version"):
            raise ValueError("version differs from canonical source version")
    except (KeyError, TypeError, ValueError, OSError, yaml.YAMLError) as exc:
        errors.append(f"{label}_VERSION {uid}: {exc}")
        version_url = None
    materialization = supplement.get("materialization")
    if not isinstance(materialization, dict):
        errors.append(f"{label}_MATERIALIZATION {uid}")
        return 0
    if materialization.get("pdf_text_extraction_mode") != "plain":
        errors.append(f"{label}_EXTRACTION_MODE {uid}")
    expected_paths = {"source_pdf": "pdf-supplement/document.pdf", "document": "pdf-supplement/document.txt", "normalized_document": "pdf-supplement/document.txt"}
    if any(materialization.get(field) != value for field, value in expected_paths.items()) or supplement.get("selectors") != ["pdf-supplement/selectors.jsonl"]:
        errors.append(f"{label}_PATHS {uid}")
    if supplement.get("media_type") != "application/pdf" or not isinstance(supplement.get("body_quality_verified"), bool):
        errors.append(f"{label}_MEDIA_OR_QUALITY {uid}")
    if not isinstance(supplement.get("limitations"), list) or any(not isinstance(value, str) or not value.strip() for value in supplement["limitations"]):
        errors.append(f"{label}_LIMITATIONS {uid}")
    paths = {name: capsule_root / name for name in ("pdf-supplement/document.pdf", "pdf-supplement/document.txt", "pdf-supplement/selectors.jsonl", "pdf-supplement/NOTICE.md")}
    if any(
        local_relative(path) not in declared_files or not path.is_file()
        or scoped_path(local_relative(path), capsule_root, repository_root=repo_root) is None
        for path in paths.values()
    ):
        errors.append(f"{label}_FILE_UNHASHED_OR_MISSING {uid}")
        return 0
    source = paths["pdf-supplement/document.pdf"]
    source_hash = actual_hashes.get(local_relative(source))
    if not source_hash or materialization.get("source_pdf_sha256") != source_hash or supplement.get("revision") != f"sha256:{source_hash}":
        errors.append(f"{label}_REVISION {uid}")
    retrievals = supplement.get("retrievals")
    retrieval = retrievals[0] if isinstance(retrievals, list) and len(retrievals) == 1 and isinstance(retrievals[0], dict) else {}
    if (
        version_url is None or retrieval.get("requested_urls") != [version_url] or retrieval.get("resolved_url") != version_url
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
        stored_text = paths["pdf-supplement/document.txt"].read_text(encoding="utf-8")
        source_text = stored_text.split("<!-- materialization-redistribution-notice -->", 1)[0].rstrip() + "\n"
        if source_text != native_text:
            errors.append(f"{label}_NATIVE_TEXT_DRIFT {uid}")
        rows = [json.loads(line) for line in paths["pdf-supplement/selectors.jsonl"].read_text(encoding="utf-8").splitlines() if line.strip()]
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
    target = local_relative(paths["pdf-supplement/document.txt"])
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
    # Only the new PDF allowance is a fail-closed materialization condition;
    # unrelated, pre-existing full-text publication blocks remain independent.
    from validate_publication_rights import validate_pdf_supplement_rights
    try:
        audit = load_yaml(repo_root / "raw_data/audits/materialization_rights_review.yaml")
        review = next((row for row in audit["items"] if isinstance(row, dict) and row.get("uid") == uid), None)
        rights_errors, rights_blocks = validate_pdf_supplement_rights(manifest, capsule_root / "manifest.yaml", repo_root, review)
        errors.extend(rights_errors)
        errors.extend(f"{label}_UNADMITTED {message}" for message in rights_blocks)
    except (KeyError, TypeError, ValueError, OSError, yaml.YAMLError) as exc:
        errors.append(f"{label}_RIGHTS_AUDIT {uid}: {exc}")
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
        selector_declaration = manifest.get("selectors")
        if not isinstance(selector_declaration, list):
            errors.append(f"SELECTOR_DECLARATION_BAD {uid}")
            selector_declaration = []
        if tier != "metadata_capsule" and "selectors.jsonl" not in selector_declaration:
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
                selector_lines = selectors_path.read_text(encoding="utf-8").splitlines()
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

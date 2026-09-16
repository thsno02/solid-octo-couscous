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


def scoped_path(raw_path: Any, scope: Path) -> Path | None:
    """Resolve a repository-relative path only when it stays inside ``scope``."""

    if not isinstance(raw_path, str) or not raw_path:
        return None
    path = Path(raw_path)
    if path.is_absolute() or ".." in path.parts:
        return None
    candidate = ROOT / path
    try:
        candidate.resolve().relative_to(scope.resolve())
    except (OSError, ValueError):
        return None
    return candidate


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


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
                preview = selector.get("text_preview")
                if preview is not None:
                    if not isinstance(preview, str) or not preview or preview not in text:
                        errors.append(f"SELECTOR_PREVIEW_UNRESOLVED {uid}:{line_number}: {selector_id}")
                        selector_valid = False

                start_line = selector.get("start_line")
                end_line = selector.get("end_line")
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
                        uri_match = (
                            re.fullmatch(
                                re.escape(expected_pdf_selector_prefix) + r"([1-9]\d*)",
                                selector_id,
                            )
                            if isinstance(selector_id, str)
                            else None
                        )
                        if uri_match is None or not isinstance(page, int) or int(uri_match.group(1)) != page:
                            errors.append(f"ARXIV_PDF_SELECTOR_HASH_OR_PAGE {uid}:{line_number}: {selector_id}")
                            selector_valid = False
                        if isinstance(page, int) and not isinstance(page, bool):
                            if page in arxiv_pdf_selector_pages:
                                errors.append(f"ARXIV_PDF_SELECTOR_PAGE_DUPLICATE {uid}:{line_number}: {page}")
                                selector_valid = False
                            arxiv_pdf_selector_pages.add(page)
                            if arxiv_pdf_page_count is not None and page > arxiv_pdf_page_count:
                                errors.append(f"ARXIV_PDF_SELECTOR_PAGE_RANGE {uid}:{line_number}: {page}")
                                selector_valid = False
                            if (
                                isinstance(preview, str)
                                and page in page_sections
                                and preview not in page_sections[page]
                            ):
                                errors.append(
                                    f"ARXIV_PDF_SELECTOR_PREVIEW_CROSS_PAGE {uid}:{line_number}: {page}"
                                )
                                selector_valid = False

                ordinal = selector.get("ordinal")
                if ordinal is not None and (
                    not isinstance(ordinal, int) or isinstance(ordinal, bool) or ordinal < 1
                ):
                    errors.append(f"SELECTOR_ORDINAL {uid}:{line_number}: {ordinal}")
                    selector_valid = False
                if selector_valid:
                    valid_selector_count += 1

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
            def declared_page_set(field: str) -> set[int]:
                value = arxiv_pdf_materialization.get(field)
                if not isinstance(value, list) or any(
                    not isinstance(page, int) or isinstance(page, bool) or page < 1 for page in value
                ):
                    errors.append(f"ARXIV_PDF_PAGE_SET {uid} {field}={value!r}")
                    return set()
                pages = set(value)
                if len(pages) != len(value):
                    errors.append(f"ARXIV_PDF_PAGE_SET_DUPLICATE {uid} {field}")
                if arxiv_pdf_page_count is not None and any(page > arxiv_pdf_page_count for page in pages):
                    errors.append(f"ARXIV_PDF_PAGE_SET_RANGE {uid} {field}={value!r}")
                return pages

            pages_without_text = declared_page_set("pdf_pages_without_extractable_text")
            failed_pages = declared_page_set("pdf_page_extraction_failures")
            if (
                arxiv_pdf_selector_pages & pages_without_text
                or arxiv_pdf_selector_pages & failed_pages
                or pages_without_text & failed_pages
            ):
                errors.append(f"ARXIV_PDF_PAGE_SET_OVERLAP {uid}")
            if arxiv_pdf_page_count is not None:
                expected_pages = set(range(1, arxiv_pdf_page_count + 1))
                covered_pages = arxiv_pdf_selector_pages | pages_without_text | failed_pages
                if covered_pages != expected_pages:
                    errors.append(
                        f"ARXIV_PDF_PAGE_COVERAGE {uid} expected={sorted(expected_pages)} "
                        f"actual={sorted(covered_pages)}"
                    )
            if arxiv_pdf_materialization.get("pdf_text_page_count") != arxiv_pdf_selector_count:
                errors.append(
                    f"ARXIV_PDF_TEXT_PAGE_COUNT {uid} "
                    f"declared={arxiv_pdf_materialization.get('pdf_text_page_count')} "
                    f"actual={arxiv_pdf_selector_count}"
                )
            if arxiv_pdf_selector_count != manifest_selector_count:
                errors.append(
                    f"ARXIV_PDF_NON_PAGE_SELECTOR {uid} pages={arxiv_pdf_selector_count} "
                    f"selectors={manifest_selector_count}"
                )

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

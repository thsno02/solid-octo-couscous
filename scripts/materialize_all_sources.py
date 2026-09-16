#!/usr/bin/env python3
"""Materialize every collected source into a local, source-specific capsule.

The goal is not to pretend that every URL can legally or technically be mirrored in
full.  The invariant is stronger and more honest:

* every metadata record receives a local capsule and manifest;
* open scholarly sources are materialized as full text when available;
* GitHub repositories are frozen at a commit and converted into semantic capsules,
  not vendored wholesale;
* web and proprietary sources are stored as full text only when the metadata says
  redistribution is open, otherwise as bounded evidence excerpts;
* every generated file is hashed and every selector resolves to a local file.

The script is deterministic for a frozen upstream revision except for retrieval
metadata such as timestamps.  Git history is the immutable version store; this
script does not duplicate all payloads into a second snapshot tree.
"""
from __future__ import annotations

import argparse
import base64
import concurrent.futures
import dataclasses
import gzip
import hashlib
import io
import json
import os
import posixpath
import re
import shutil
import subprocess
import tarfile
import threading
import time
import urllib.parse
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

import requests
import yaml

ROOT = Path(__file__).resolve().parents[1]
RAW_ROOT = ROOT / "raw_data"
MATERIALIZED_ROOT = ROOT / "materialized_sources"
CORPUS_ROOT = MATERIALIZED_ROOT / "corpus"
REGISTRY_ROOT = ROOT / "source_registry"
AUDIT_ROOT = RAW_ROOT / "audits"

USER_AGENT = (
    "solid-octo-couscous-materializer/2.0 "
    "(+https://github.com/thsno02/solid-octo-couscous)"
)

DIRECTORY_SOURCE_TYPES = {
    "arxiv": "arxiv",
    "biorxiv": "biorxiv",
    "journal": "journal",
    "paper": "paper",
    "standard": "standard",
    "methodology": "methodology",
    "industry": "industry",
    "blog": "blog",
    "githubs": "github",
    "dataset": "dataset",
    "benchmark": "benchmark",
    "incident": "incident",
    "x": "x",
}

TYPE_ALIASES = {
    "book_chapter": "paper",
    "book-chapter": "paper",
    "conference": "paper",
    "preprint": "paper",
    "industry_doc": "industry",
    "industry-doc": "industry",
    "ontology": "standard",
    "github_repo": "github",
    "github-repository": "github",
}

ARXIV_TEXT_EXTENSIONS = {
    ".tex",
    ".ltx",
    ".bib",
    ".bbl",
    ".sty",
    ".cls",
    ".bst",
    ".def",
    ".txt",
    ".md",
    ".rst",
    ".json",
    ".yaml",
    ".yml",
    ".csv",
}

GITHUB_TEXT_EXTENSIONS = {
    ".md",
    ".mdx",
    ".rst",
    ".txt",
    ".adoc",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".ini",
    ".cfg",
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".go",
    ".rs",
    ".java",
    ".kt",
    ".scala",
    ".rb",
    ".sh",
    ".sql",
    ".proto",
    ".graphql",
    ".gql",
    ".xml",
}

PROMINENT_GITHUB_FILENAMES = {
    "readme.md",
    "readme.rst",
    "readme.txt",
    "agents.md",
    "claude.md",
    "architecture.md",
    "design.md",
    "overview.md",
    "concepts.md",
    "security.md",
    "contributing.md",
    "citation.cff",
    "license",
    "license.md",
    "license.txt",
    "pyproject.toml",
    "package.json",
    "go.mod",
    "cargo.toml",
    "requirements.txt",
    "makefile",
    "dockerfile",
}

GITHUB_DOC_KEYWORDS = {
    "architecture",
    "design",
    "overview",
    "concept",
    "ontology",
    "schema",
    "memory",
    "knowledge",
    "evaluation",
    "benchmark",
    "workflow",
    "agent",
    "api",
    "interface",
    "security",
    "governance",
    "provenance",
    "retrieval",
    "compile",
    "ingest",
    "index",
}

_thread_local = threading.local()
_arxiv_semaphore = threading.Semaphore(3)
_github_semaphore = threading.Semaphore(6)
_generic_semaphore = threading.Semaphore(6)


@dataclasses.dataclass(frozen=True)
class SourceRecord:
    uid: str
    source_type: str
    canonical_id: str | None
    title: str
    canonical_url: str | None
    metadata_path: Path
    metadata: dict[str, Any]
    priority: str
    rights_access: str

    @property
    def relative_metadata_path(self) -> str:
        return self.metadata_path.relative_to(ROOT).as_posix()

    @property
    def capsule_key(self) -> str:
        base = safe_key(self.uid)
        suffix = hashlib.sha1(self.relative_metadata_path.encode("utf-8")).hexdigest()[:8]
        return f"{base}--{suffix}"

    @property
    def capsule_root(self) -> Path:
        return CORPUS_ROOT / self.capsule_key


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def safe_key(value: str) -> str:
    value = value.strip().replace("/", "--").replace(":", "-")
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-._")
    return value or "source"


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def dump_yaml(value: Any) -> str:
    return yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=110)


def write_yaml(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dump_yaml(value), encoding="utf-8")


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_source_type(path: Path, metadata: dict[str, Any]) -> str:
    relative = path.relative_to(RAW_ROOT)
    directory = relative.parts[0] if relative.parts else "unknown"
    if directory in DIRECTORY_SOURCE_TYPES:
        return DIRECTORY_SOURCE_TYPES[directory]
    raw = str(metadata.get("source_type") or metadata.get("source") or directory).strip().lower()
    raw = raw.replace(" ", "_")
    return TYPE_ALIASES.get(raw, raw)


def canonical_id_for(source_type: str, metadata: dict[str, Any]) -> str | None:
    candidates = [
        metadata.get("canonical_id"),
        metadata.get("arxiv_id") if source_type == "arxiv" else None,
        metadata.get("repo") if source_type == "github" else None,
        metadata.get("doi"),
        metadata.get("id"),
    ]
    for candidate in candidates:
        if candidate is None:
            continue
        value = str(candidate).strip()
        if not value:
            continue
        if source_type == "arxiv":
            value = re.sub(r"v\d+$", "", value)
        return value
    return None


def canonical_url_for(source_type: str, canonical_id: str | None, metadata: dict[str, Any]) -> str | None:
    for field in (
        "canonical_url",
        "url",
        "official_url",
        "source_url",
        "paper_url",
        "landing_page",
    ):
        value = metadata.get(field)
        if isinstance(value, str) and value.strip():
            return value.strip()
    if canonical_id and source_type == "arxiv":
        return f"https://arxiv.org/abs/{canonical_id}"
    if canonical_id and source_type == "github":
        return f"https://github.com/{canonical_id}"
    if canonical_id and metadata.get("doi"):
        return f"https://doi.org/{canonical_id}"
    return None


def discover_records() -> list[SourceRecord]:
    records: list[SourceRecord] = []
    seen_uids: Counter[str] = Counter()
    for path in sorted(RAW_ROOT.rglob("metadata.yaml")):
        metadata = load_yaml(path)
        if not isinstance(metadata, dict):
            continue
        source_type = normalize_source_type(path, metadata)
        canonical_id = canonical_id_for(source_type, metadata)
        title = str(metadata.get("title") or metadata.get("repo") or path.parent.name).strip()
        base_uid = str(metadata.get("uid") or f"{source_type}:{canonical_id or safe_key(title)}").strip()
        seen_uids[base_uid] += 1
        uid = base_uid if seen_uids[base_uid] == 1 else f"{base_uid}#{seen_uids[base_uid]}"
        canonical_url = canonical_url_for(source_type, canonical_id, metadata)
        collection = metadata.get("collection") if isinstance(metadata.get("collection"), dict) else {}
        priority = str(collection.get("priority") or metadata.get("priority") or "P1")
        rights = metadata.get("rights") if isinstance(metadata.get("rights"), dict) else {}
        rights_access = str(rights.get("access") or "unknown")
        records.append(
            SourceRecord(
                uid=uid,
                source_type=source_type,
                canonical_id=canonical_id,
                title=title,
                canonical_url=canonical_url,
                metadata_path=path,
                metadata=metadata,
                priority=priority,
                rights_access=rights_access,
            )
        )
    return records


def session() -> requests.Session:
    current = getattr(_thread_local, "session", None)
    if current is None:
        current = requests.Session()
        current.headers.update({"User-Agent": USER_AGENT, "Accept": "*/*"})
        _thread_local.session = current
    return current


def fetch_bytes(url: str, *, timeout: int, max_bytes: int, attempts: int = 3) -> tuple[bytes, str, dict[str, str]]:
    last_error: Exception | None = None
    for attempt in range(attempts):
        response: requests.Response | None = None
        try:
            request_headers: dict[str, str] = {}
            host = urllib.parse.urlparse(url).netloc.lower()
            token = os.getenv("GITHUB_TOKEN")
            if token and host == "api.github.com":
                request_headers.update({
                    "Authorization": f"Bearer {token}",
                    "X-GitHub-Api-Version": "2022-11-28",
                })
            response = session().get(
                url,
                timeout=timeout,
                stream=True,
                allow_redirects=True,
                headers=request_headers,
            )
            response.raise_for_status()
            chunks: list[bytes] = []
            total = 0
            for chunk in response.iter_content(chunk_size=128 * 1024):
                if not chunk:
                    continue
                total += len(chunk)
                if total > max_bytes:
                    raise RuntimeError(f"response exceeded {max_bytes} bytes")
                chunks.append(chunk)
            headers = {str(key).lower(): str(value) for key, value in response.headers.items()}
            resolved_url = str(response.url)
            response.close()
            return b"".join(chunks), resolved_url, headers
        except Exception as exc:  # requests raises several useful subclasses.
            if response is not None:
                response.close()
            last_error = exc
            if attempt + 1 < attempts:
                time.sleep(min(8, 2**attempt))
    raise RuntimeError(f"fetch failed for {url}: {last_error}")


def local_file_inventory(root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.name == "manifest.yaml":
            continue
        rows.append(
            {
                "path": path.relative_to(ROOT).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    return rows


def candidate_urls(record: SourceRecord) -> list[str]:
    fields = (
        "source_archive_url",
        "open_copy_url",
        "pdf_url",
        "full_text_url",
        "download_url",
        "source_url",
        "canonical_url",
        "url",
    )
    urls: list[str] = []
    for field in fields:
        value = record.metadata.get(field)
        if isinstance(value, str) and value.startswith(("http://", "https://")):
            urls.append(value)
    if record.canonical_url:
        urls.append(record.canonical_url)
    deduped: list[str] = []
    seen: set[str] = set()
    for url in urls:
        if url not in seen:
            seen.add(url)
            deduped.append(url)
    return deduped


def text_is_open(record: SourceRecord, config: dict[str, Any], resolved_url: str | None = None) -> bool:
    if record.rights_access in {"open", "source_available"}:
        return True
    if record.metadata.get("rights") and isinstance(record.metadata["rights"], dict):
        if record.metadata["rights"].get("license_spdx"):
            return True
    allowed_types = set(config.get("full_text_source_types", []))
    if record.source_type in allowed_types:
        return True
    if resolved_url:
        host = urllib.parse.urlparse(resolved_url).netloc.lower()
        if any(host == domain or host.endswith("." + domain) for domain in config.get("open_full_text_domains", [])):
            return True
    return False


def write_capsule_readme(record: SourceRecord, root: Path, manifest: dict[str, Any]) -> None:
    lines = [
        f"# {record.title}",
        "",
        f"- UID: `{record.uid}`",
        f"- Source type: `{record.source_type}`",
        f"- Canonical ID: `{record.canonical_id}`",
        f"- Canonical URL: {record.canonical_url or 'unresolved'}",
        f"- Materialization status: `{manifest.get('status')}`",
        f"- Content tier: `{manifest.get('content_tier')}`",
        "",
        "This directory is a local evidence capsule. It is not, by itself, a trusted knowledge assertion.",
    ]
    if manifest.get("rights", {}).get("redistribution_package"):
        lines.extend(["", "Redistribution notice and attribution: [NOTICE.md](NOTICE.md)."])
    materialization = manifest.get("materialization") or {}
    if materialization.get("retained_markdown_source"):
        lines.extend(["", "Local retained representations:"])
        for label, field in (("Consumer Markdown", "document"), ("Original Markdown", "retained_markdown_source"), ("Original HTML", "retained_html_source")):
            if materialization.get(field):
                lines.append(f"- [{label}]({materialization[field]})")
    (root / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


class RedistributionPackageError(ValueError):
    """A declared publication condition failed; never downgrade it to metadata-only."""


class ArxivPreflightError(RuntimeError):
    """An arXiv rebuild cannot safely replace the retained capsule."""


class RetainedMarkdownPreflightError(RuntimeError):
    """A fixed Markdown snapshot cannot safely be replayed; keep its originals."""


def redistribution_notice_href(root: Path, document: Path) -> str:
    """Return the safe relative link from a materialized document to its notice."""
    resolved_root = root.resolve()
    resolved_document = document.resolve()
    resolved_document.relative_to(resolved_root)
    return Path(
        os.path.relpath(resolved_root / "NOTICE.md", start=resolved_document.parent)
    ).as_posix()


def redistribution_footer(package: dict[str, Any], notice_href: str = "NOTICE.md") -> str:
    """Append attribution without shifting existing source selectors."""
    return (
        "\n\n<!-- materialization-redistribution-notice -->\n"
        "## Redistribution notice\n\n"
        f"{package['attribution']}\n\n"
        f"Changes: {package['modifications']}\n\n"
        f"Scope: {package['scope']}\n\n"
        f"Full license and original rights links: [NOTICE.md]({notice_href}).\n"
    )


def apply_redistribution_package(record: SourceRecord, root: Path, manifest: dict[str, Any]) -> None:
    """Restore reviewed license packaging on every materialization, not just once."""
    rights = record.metadata.get("rights") or {}
    package = rights.get("redistribution_package")
    if not package:
        return
    if package.get("source_revision") != manifest.get("revision"):
        if manifest.get("content_tier") == "full_text":
            raise ValueError("declared redistribution package does not cover the retrieved revision")
        return
    for field in ("source_revision", "source_version_url", "notice_path", "attribution", "modifications", "scope"):
        if not isinstance(package.get(field), str) or not package[field].strip():
            raise ValueError(f"redistribution package is missing {field}")
    notice_path = (ROOT / package["notice_path"]).resolve()
    notice_path.relative_to(ROOT.resolve())
    notice = notice_path.read_text(encoding="utf-8")
    if not notice.strip():
        raise ValueError("redistribution notice is empty")
    document_name = manifest.get("materialization", {}).get("document")
    if not document_name:
        raise ValueError("redistribution package needs an explicit materialized document")
    document = (root / document_name).resolve()
    document.relative_to(root.resolve())
    notice_href = redistribution_notice_href(root, document)
    text = document.read_text(encoding="utf-8")
    previous = manifest.get("rights", {}).get("redistribution_package")
    marker_count = text.count("<!-- materialization-redistribution-notice -->")
    if marker_count:
        if marker_count != 1 or not previous:
            raise ValueError("unexpected or duplicate redistribution footer")
        previous_footer = redistribution_footer(previous, notice_href)
        if not text.endswith(previous_footer):
            raise ValueError("previous redistribution footer is not intact at end of document")
        text = text[:-len(previous_footer)]
    text += redistribution_footer(package, notice_href)
    document.write_text(text, encoding="utf-8")
    (root / "NOTICE.md").write_text(notice, encoding="utf-8")
    manifest["materialization"]["stored_characters"] = len(text)
    manifest["rights"].update({
        "declared_access": rights.get("access"),
        "full_text_redistribution_assumed": False,
        "license_spdx": rights.get("license_spdx"),
        "license_url": rights.get("license_url"),
        "license_verified_at": rights.get("license_verified_at"),
        "redistribution_package": dict(package),
    })


def base_manifest(record: SourceRecord, adapter: str, generated_at: str) -> dict[str, Any]:
    return {
        "manifest_version": 2,
        "uid": record.uid,
        "source_type": record.source_type,
        "canonical_id": record.canonical_id,
        "title": record.title,
        "canonical_url": record.canonical_url,
        "metadata_path": record.relative_metadata_path,
        "generated_at": generated_at,
        "adapter": adapter,
        "status": "metadata_only",
        "content_tier": "metadata_capsule",
        "revision": None,
        "rights": {
            "declared_access": record.rights_access,
            "full_text_redistribution_assumed": False,
        },
        "retrievals": [],
        "selectors": [],
        "local_files": [],
        "warnings": [],
        "errors": [],
    }


def prepare_capsule(record: SourceRecord) -> Path:
    root = record.capsule_root
    shutil.rmtree(root, ignore_errors=True)
    root.mkdir(parents=True, exist_ok=True)
    write_yaml(root / "source-metadata.yaml", record.metadata)
    return root


def finalize_capsule(record: SourceRecord, root: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    try:
        apply_redistribution_package(record, root, manifest)
    except (KeyError, TypeError, AttributeError, ValueError, OSError) as exc:
        raise RedistributionPackageError(f"{record.uid}: {exc}") from exc
    write_capsule_readme(record, root, manifest)
    manifest["local_files"] = local_file_inventory(root)
    manifest["local_bytes"] = sum(item["bytes"] for item in manifest["local_files"])
    write_yaml(root / "manifest.yaml", manifest)
    return manifest


def unpack_arxiv(payload: bytes) -> tuple[list[tuple[str, bytes]], str]:
    try:
        with tarfile.open(fileobj=io.BytesIO(payload), mode="r:*") as archive:
            members = []
            for member in archive.getmembers():
                if not member.isfile() or member.size > 8_000_000:
                    continue
                handle = archive.extractfile(member)
                if handle is not None:
                    members.append((member.name, handle.read()))
            return members, "tar"
    except tarfile.TarError:
        pass
    try:
        uncompressed = gzip.decompress(payload)
    except OSError:
        return [("main.tex", payload)], "single"
    try:
        with tarfile.open(fileobj=io.BytesIO(uncompressed), mode="r:*") as archive:
            members = []
            for member in archive.getmembers():
                if not member.isfile() or member.size > 8_000_000:
                    continue
                handle = archive.extractfile(member)
                if handle is not None:
                    members.append((member.name, handle.read()))
            return members, "gzip-tar"
    except tarfile.TarError:
        return [("main.tex", uncompressed)], "gzip-single"


def arxiv_pdf_payload(payload: bytes) -> tuple[bytes | None, str | None]:
    """Return the actual PDF bytes and transport container when magic confirms it."""

    if payload.startswith(b"%PDF-"):
        return payload, "pdf"
    if not payload.startswith(b"\x1f\x8b"):
        return None, None
    try:
        uncompressed = gzip.decompress(payload)
    except OSError:
        return None, None
    if uncompressed.startswith(b"%PDF-"):
        return uncompressed, "gzip-pdf"
    return None, None


def looks_like_single_tex(payload: bytes) -> bool:
    """Recognize a single TeX source without treating arbitrary 200 bodies as TeX."""

    if b"\x00" in payload[:8192]:
        return False
    sample = payload[:1_000_000].decode("utf-8", errors="ignore")
    return bool(
        re.search(
            r"\\(?:documentclass\b|documentstyle\b|begin\s*\{document\}|input\b|include\b|"
            r"title\b|author\b|section\b|def\b|newcommand\b|usepackage\b|bye\b)",
            sample,
        )
    )


def is_obvious_error_document(payload: bytes) -> bool:
    prefix = payload.lstrip()
    if prefix.startswith(b"\xef\xbb\xbf"):
        prefix = prefix[3:].lstrip()
    prefix = prefix[:512].lower()
    return prefix.startswith((b"<!doctype html", b"<html", b"<!--", b"<?xml", b"{", b"["))


def classify_arxiv_payload(payload: bytes) -> str | None:
    """Classify only supported arXiv e-print representations by their bytes."""

    _, pdf_container = arxiv_pdf_payload(payload)
    if pdf_container is not None:
        return pdf_container
    if is_obvious_error_document(payload):
        return None
    try:
        with tarfile.open(fileobj=io.BytesIO(payload), mode="r:*") as archive:
            if any(member.isfile() for member in archive.getmembers()):
                return "tar"
    except tarfile.TarError:
        pass
    if payload.startswith(b"\x1f\x8b"):
        try:
            uncompressed = gzip.decompress(payload)
        except OSError:
            return None
        if is_obvious_error_document(uncompressed):
            return None
        return "gzip-single" if looks_like_single_tex(uncompressed) else None
    return "single" if looks_like_single_tex(payload) else None


def arxiv_eprint_id(record: SourceRecord) -> str:
    """Bind an arXiv retrieval to ``versioning.source_version`` when declared."""

    if not record.canonical_id:
        raise ValueError("missing arXiv identifier")
    versioning = record.metadata.get("versioning")
    source_version = versioning.get("source_version") if isinstance(versioning, dict) else None
    if source_version in (None, ""):
        return record.canonical_id
    if not isinstance(source_version, str) or not re.fullmatch(r"v[1-9]\d*", source_version.strip()):
        raise ValueError("arXiv versioning.source_version must be vN")
    return f"{record.canonical_id}{source_version.strip()}"


def tex_comment_start(line: str) -> int | None:
    """A percent sign is escaped only after an odd run of backslashes."""
    for index, character in enumerate(line):
        if character != "%":
            continue
        previous = index - 1
        while previous >= 0 and line[previous] == "\\":
            previous -= 1
        if (index - previous - 1) % 2 == 0:
            return index
    return None


def tex_without_comments(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines(keepends=True):
        start = tex_comment_start(line)
        if start is not None:
            ending = "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else "\r" if line.endswith("\r") else ""
            line = line[:start] + ending
        lines.append(line)
    return "".join(lines)


def tex_root_candidates(
    files: dict[str, str], *, exclusions: list[dict[str, str]] | None = None,
) -> list[str]:
    """Find document roots by structure, including TeX saved with a .txt suffix."""
    candidates: list[str] = []
    for path, text in sorted(files.items()):
        suffix = PurePosixPath(path).suffix.lower()
        if suffix not in {".tex", ".ltx", ".txt"}:
            continue
        body = tex_without_comments(text)
        begin = re.search(r"\\begin\s*\{document\}", body)
        if begin is None or re.search(r"\\end\s*\{document\}", body[begin.end():]) is None:
            continue
        # An ordinary .txt containing a TeX fragment is not a source document.
        if suffix == ".txt" and re.search(
            r"\\(?:documentclass|documentstyle)\b", body[:begin.start()]
        ) is None:
            continue
        document_class = re.search(
            r"\\documentclass\s*(?:\[[^\]]*\]\s*)?\{\s*([^{}]+?)\s*\}", body[:begin.start()]
        )
        reason: str | None = None
        evidence = ""
        if document_class is not None and document_class.group(1).strip().lower() == "standalone":
            reason, evidence = "standalone_document", document_class.group(0)
        title_match = re.search(r"\\title\s*(?:\[[^\]]*\]\s*)?\{([^{}]*)\}", body)
        if reason is None and title_match is not None:
            title = re.sub(r"\\[A-Za-z@]+|\\\\", " ", title_match.group(1))
            title = " ".join(title.replace("\\", " ").split())
            if re.search(
                r"^(?:formatting instructions\b.*\b(?:submissions|proceedings)|"
                r"author guidelines\b.*\bproceedings|a new style for\b.*\bpapers)\s*$",
                title, re.IGNORECASE,
            ):
                reason, evidence = "formatting_template_document", title
        parts = PurePosixPath(path).parts
        historical_directory = any(re.fullmatch(r"revision[-_]history", part, re.IGNORECASE) for part in parts[:-1])
        historical_copy = (
            any(part.lower() == "history" for part in parts[:-1])
            and re.search(r"\bpre-final-revision\b", PurePosixPath(path).stem.replace("_", "-"), re.IGNORECASE)
        )
        if reason is None and (historical_directory or historical_copy):
            reason, evidence = "explicit_historical_document", path
        if reason is not None:
            if exclusions is not None:
                exclusions.append({"kind": reason, "path": path, "evidence": evidence})
            continue
        candidates.append(path)
    return candidates


def choose_main_tex(files: dict[str, str]) -> str | None:
    candidates = tex_root_candidates(files)
    # Multiple real documents require a boundary decision, not a size tie-break.
    return candidates[0] if len(candidates) == 1 else None


def resolve_tex_include(
    current_path: str, target: str, files: dict[str, str], *, directory: str | None = None,
) -> str | None:
    """Resolve retained literal paths, without root fallback for an explicit import directory."""
    target = target.strip().strip("{}\"")
    if not target:
        return None
    current_dir = PurePosixPath(directory) if directory is not None else PurePosixPath(current_path).parent
    candidates = [current_dir / target]
    if directory is None:
        candidates.append(PurePosixPath(target))
    expanded: list[PurePosixPath] = []
    for candidate in candidates:
        expanded.append(candidate)
        if not candidate.suffix:
            expanded.append(candidate.with_suffix(".tex"))
    for candidate in expanded:
        normalized = posixpath.normpath(candidate.as_posix())
        if normalized.startswith(("/", "../")) or normalized in {".", ".."}:
            continue
        if normalized in files:
            return normalized
    return None


def flatten_tex(
    main_path: str,
    files: dict[str, str],
    *,
    max_depth: int = 20,
    diagnostics: list[dict[str, str]] | None = None,
    include_graph: list[dict[str, str]] | None = None,
) -> str:
    """Expand literal braced calls, not macros, conditionals, or a full TeX engine.

    ``import`` directories are relative to the selected root's compile directory;
    ``subimport`` appends to the enclosing import directory. A nested ``import``
    resets that directory. Within an import, ``input``/``include`` search only the
    active import directory: unsupported ancestor/system-path searches stay missing
    rather than silently selecting a same-named root file. Only retained paths resolve.
    """
    include_pattern = re.compile(
        r"\\(?:(input|include)\s*\{([^{}]+)\}|(import|subimport)\s*\{([^{}]*)\}\s*\{([^{}]+)\})"
    )
    root_directory = PurePosixPath(main_path).parent.as_posix()

    def visit(path: str, stack: tuple[str, ...], import_directory: str | None) -> str:
        if path in stack:
            if diagnostics is not None:
                diagnostics.append({"kind": "cycle", "path": path})
            return f"\n% [cycle omitted: {path}]\n"
        if len(stack) >= max_depth:
            if diagnostics is not None:
                diagnostics.append({"kind": "depth_limit", "path": path})
            return f"\n% [include depth exceeded: {path}]\n"
        text = files.get(path, "")
        supported_starts = {match.start() for match in include_pattern.finditer(text)}
        for match in re.finditer(r"\\(?:input|include|import|subimport)\b", text):
            line_prefix = text[text.rfind("\n", 0, match.start()) + 1:match.start()]
            if match.start() not in supported_starts and tex_comment_start(line_prefix) is None:
                if diagnostics is not None:
                    line_end = text.find("\n", match.start())
                    diagnostics.append({
                        "kind": "unsupported_include_syntax", "path": path,
                        "target": text[match.start():line_end if line_end >= 0 else len(text)],
                    })

        def replace(match: re.Match[str]) -> str:
            line_prefix = text[text.rfind("\n", 0, match.start()) + 1:match.start()]
            if tex_comment_start(line_prefix) is not None:
                return match.group(0)
            command = match.group(1) or match.group(3)
            target = match.group(2) if match.group(1) else match.group(5)
            next_import_directory = import_directory
            directory = import_directory
            if match.group(3):
                base_directory = root_directory if command == "import" else import_directory or root_directory
                directory = posixpath.normpath(posixpath.join(base_directory, match.group(4).strip()))
                next_import_directory = directory
            if "\\" in target or (match.group(3) and "\\" in match.group(4)):
                if diagnostics is not None:
                    diagnostics.append({"kind": "unsupported_include_syntax", "path": path, "target": match.group(0)})
                return match.group(0)
            resolved = resolve_tex_include(path, target, files, directory=directory)
            if resolved is None:
                if diagnostics is not None:
                    diagnostics.append({
                        "kind": "missing_include", "path": path, "target": target,
                        **({"directory": directory} if directory is not None else {}),
                    })
                return match.group(0)
            if include_graph is not None:
                include_graph.append({"from": path, "to": resolved})
            return (
                f"\n% --- begin included file: {resolved} ---\n"
                + visit(resolved, stack + (path,), next_import_directory)
                + f"\n% --- end included file: {resolved} ---\n"
            )

        return include_pattern.sub(replace, text)

    return visit(main_path, tuple(), None)


def tex_to_plain(
    text: str, *, diagnostics: list[dict[str, str]] | None = None, path: str = "document.tex",
) -> str:
    # Preserve section labels and arguments while removing the most disruptive TeX syntax.
    text = tex_without_comments(text)
    begin = re.search(r"\\begin\s*\{document\}", text)
    if begin is not None:
        if diagnostics is not None and re.search(r"\\abstract\b|\\begin\s*\{abstract\}", text[:begin.start()]):
            diagnostics.append({"kind": "preamble_semantic_abstract_omitted", "path": path})
        text = text[begin.end():]
        end = re.search(r"\\end\s*\{document\}", text)
        if end is not None:
            text = text[:end.start()]
    text = re.sub(r"\\(?:sub)*section\*?\{([^{}]+)\}", r"\n\n## \1\n", text)
    text = re.sub(r"\\paragraph\*?\{([^{}]+)\}", r"\n\n### \1\n", text)
    text = re.sub(r"\\begin\{abstract\}", "\n\n## Abstract\n", text)
    text = re.sub(r"\\end\{abstract\}", "\n", text)
    text = re.sub(r"\\label\{[^{}]*\}", "", text)
    text = re.sub(r"\\(?:cite|citep|citet|ref|eqref|label|url|href)\*?(?:\[[^\]]*\])?\{([^{}]*)\}", r" \1 ", text)
    text = re.sub(r"\\(?:textbf|textit|emph|mathrm|mathbf|mathit|operatorname)\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\(?:begin|end)\s*\{[^{}]+\}(?:\[[^\]]*\])?", "\n", text)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?", " ", text)
    text = text.replace("{", " ").replace("}", " ")
    text = re.sub(r"\$+", " ", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def write_arxiv_tex_derivatives(
    record: SourceRecord,
    root: Path,
    stored: dict[str, str],
    *,
    revision: str,
) -> dict[str, Any]:
    """Reuse retained source text; write only normalized files and selectors."""
    source_root = root / "source"
    root_exclusions: list[dict[str, str]] = []
    candidates = tex_root_candidates(stored, exclusions=root_exclusions)
    main_tex = candidates[0] if len(candidates) == 1 else None
    diagnostics: list[dict[str, str]] = []
    normalization_diagnostics: list[dict[str, str]] = []
    include_graph: list[dict[str, str]] = []
    normalized: dict[str, str] = {}
    if main_tex:
        flattened = flatten_tex(main_tex, stored, diagnostics=diagnostics, include_graph=include_graph)
        normalized = {
            "normalized/document.tex": flattened,
            "normalized/document.txt": tex_to_plain(flattened, diagnostics=normalization_diagnostics, path=main_tex),
        }
        for path, text in normalized.items():
            destination = root / path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(text, encoding="utf-8")

    selectors: list[dict[str, Any]] = []
    revision_selector = revision.split(":", 1)[-1][:16]
    for path, text in sorted(stored.items()):
        lines = text.splitlines()
        selector_base = f"arxiv://{record.canonical_id}@sha256-{revision_selector}/{path}"
        selectors.append({
            "selector": f"{selector_base}#L1-L{max(1, len(lines))}",
            "local_path": (source_root / path).relative_to(ROOT).as_posix(),
            "kind": "file", "start_line": 1, "end_line": max(1, len(lines)),
        })
        for line_number, line in enumerate(lines, 1):
            match = re.search(r"\\(section|subsection|subsubsection|paragraph)\*?\{([^{}]+)\}", line)
            if match:
                selectors.append({
                    "selector": f"{selector_base}#L{line_number}",
                    "local_path": (source_root / path).relative_to(ROOT).as_posix(),
                    "kind": match.group(1), "heading": match.group(2).strip(),
                    "start_line": line_number, "end_line": line_number,
                })
    for path, text in sorted(normalized.items()):
        lines = text.splitlines()
        selector_base = f"arxiv://{record.canonical_id}@sha256-{revision_selector}/{path}"
        provenance = {"derived_from": f"source/{main_tex}", "transformation": "TeX include expansion"}
        if path.endswith(".txt"):
            provenance["transformation"] += " and lossy plain-text normalization; preamble excluded"
        selectors.append({
            "selector": f"{selector_base}#L1-L{max(1, len(lines))}",
            "local_path": (root / path).relative_to(ROOT).as_posix(),
            "kind": "file", "start_line": 1, "end_line": max(1, len(lines)),
            **({"text_preview": next(line for line in lines if line.strip())} if text.strip() else {}),
            **provenance,
        })
        if path.endswith(".txt"):
            headings = [(number, re.match(r"^(#{2,3})\s+(.+)$", line)) for number, line in enumerate(lines, 1)]
            headings = [(number, match) for number, match in headings if match is not None]
            for index, (start, match) in enumerate(headings):
                end = headings[index + 1][0] - 1 if index + 1 < len(headings) else len(lines)
                selectors.append({
                    "selector": f"{selector_base}#L{start}-L{end}",
                    "local_path": (root / path).relative_to(ROOT).as_posix(),
                    "kind": "section", "heading": match.group(2),
                    "start_line": start, "end_line": end,
                    "text_preview": next((line for line in lines[start:end] if line.strip()), lines[start - 1])[:700],
                    **provenance,
                })
    write_jsonl(root / "selectors.jsonl", selectors)
    return {
        "main_tex": main_tex, "tex_root_candidates": candidates, "tex_root_exclusions": root_exclusions,
        "document": "normalized/document.txt" if main_tex else None,
        "normalized_document": "normalized/document.txt" if main_tex else None,
        "normalized_tex": "normalized/document.tex" if main_tex else None,
        "tex_include_graph": include_graph, "tex_include_errors": diagnostics,
        "tex_normalization_diagnostics": normalization_diagnostics,
        "selector_count": len(selectors),
    }


def materialize_arxiv(record: SourceRecord, config: dict[str, Any], generated_at: str) -> dict[str, Any]:
    root = record.capsule_root
    manifest = base_manifest(record, "arxiv_latex_v2", generated_at)
    arxiv_id = record.canonical_id
    if not arxiv_id:
        if root.exists():
            raise ArxivPreflightError(f"{record.uid}: missing arXiv identifier; retained capsule unchanged")
        root = prepare_capsule(record)
        manifest["errors"].append("missing arXiv identifier")
        return finalize_capsule(record, root, manifest)

    try:
        requested_arxiv_id = arxiv_eprint_id(record)
    except ValueError as exc:
        if root.exists():
            raise ArxivPreflightError(f"{record.uid}: {exc}; retained capsule unchanged") from exc
        root = prepare_capsule(record)
        manifest["errors"].append(str(exc))
        return finalize_capsule(record, root, manifest)
    quoted_id = urllib.parse.quote(requested_arxiv_id, safe="/")
    urls = [
        f"https://export.arxiv.org/e-print/{quoted_id}",
        f"https://arxiv.org/e-print/{quoted_id}",
    ]
    payload: bytes | None = None
    payload_kind: str | None = None
    resolved_url: str | None = None
    headers: dict[str, str] = {}
    for url in urls:
        try:
            candidate_payload, candidate_url, candidate_headers = fetch_bytes(
                url,
                timeout=int(config.get("http_timeout_seconds", 45)),
                max_bytes=int(config.get("arxiv_max_archive_bytes", 60_000_000)),
            )
            candidate_kind = classify_arxiv_payload(candidate_payload)
            content_type = (candidate_headers.get("content-type") or "").lower()
            if candidate_kind is None or (
                "application/pdf" in content_type and candidate_kind not in {"pdf", "gzip-pdf"}
            ):
                manifest["warnings"].append(
                    f"rejected unsupported arXiv e-print payload from {candidate_url or url} "
                    f"(content-type {content_type or 'unreported'})"
                )
                continue
            payload = candidate_payload
            payload_kind = candidate_kind
            resolved_url = candidate_url
            headers = candidate_headers
            break
        except Exception as exc:
            manifest["warnings"].append(str(exc))
    if payload is None:
        if root.exists():
            raise ArxivPreflightError(f"{record.uid}: arXiv source archive could not be acquired; retained capsule unchanged")
        root = prepare_capsule(record)
        manifest["errors"].append("arXiv source archive could not be acquired")
        # Preserve a bounded local copy of the abstract page when the source archive fails.
        manifest["adapter"] = "generic_web_or_document_v2"
        return materialize_generic(
            record,
            config,
            generated_at,
            existing_root=root,
            existing_manifest=manifest,
            force_excerpt_reason=(
                "arXiv source archive was unavailable; the landing or abstract page is fallback evidence, not full text."
            ),
        )

    archive_hash = sha256_bytes(payload)
    manifest["revision"] = f"sha256:{archive_hash}"
    manifest["retrievals"].append(
        {
            "requested_urls": urls,
            "resolved_url": resolved_url,
            "content_type": headers.get("content-type"),
            "bytes": len(payload),
            "sha256": archive_hash,
        }
    )
    pdf_payload, pdf_container = arxiv_pdf_payload(payload)
    if pdf_payload is not None and pdf_container is not None:
        root = prepare_capsule(record)
        manifest["adapter"] = "arxiv_pdf_v1"
        manifest["archive_container"] = pdf_container
        manifest["media_type"] = "application/pdf"
        manifest["retrievals"][-1]["detected_media_type"] = "application/pdf"

        source_root = root / "source"
        source_root.mkdir(parents=True, exist_ok=True)
        source_pdf = source_root / "document.pdf"
        source_pdf.write_bytes(pdf_payload)
        source_pdf_hash = sha256_bytes(pdf_payload)
        document_text = ""
        selectors: list[dict[str, Any]] = []
        page_count: int | None = None
        extraction_failed_pages: list[int] = []
        pages_without_text: list[int] = []
        try:
            document_text, extracted_selectors, page_count = extract_pdf_text(pdf_payload)
            for selector in extracted_selectors:
                page = selector.get("page")
                preview = selector.get("text_preview")
                if isinstance(preview, str) and preview.startswith("[page extraction failed:"):
                    if isinstance(page, int):
                        extraction_failed_pages.append(page)
                    continue
                if not isinstance(preview, str) or not preview.strip():
                    if isinstance(page, int):
                        pages_without_text.append(page)
                    continue
                selector["selector"] = selector["selector"].replace(
                    "sha256-PENDING", f"sha256-{source_pdf_hash[:16]}"
                )
                selectors.append(selector)
        except Exception as exc:
            manifest["errors"].append(f"PDF parsing failed: {exc}")

        substantive_text = has_substantive_document_text(document_text) if document_text else False
        document_name: str | None = None
        if document_text:
            document_name = "document.txt"
            document_path = root / document_name
            document_path.write_text(document_text, encoding="utf-8")
            if selectors:
                local_path = document_path.relative_to(ROOT).as_posix()
                for selector in selectors:
                    selector["local_path"] = local_path
                write_jsonl(root / "selectors.jsonl", selectors)
                manifest["selectors"] = ["selectors.jsonl"]

        limitations: list[str] = []
        if pages_without_text:
            limitations.append(
                "PDF pages without extractable text: "
                + ", ".join(str(page) for page in pages_without_text)
                + "; the original PDF is preserved and no OCR was performed."
            )
        if extraction_failed_pages:
            limitations.append(
                "PDF text extraction failed on pages: "
                + ", ".join(str(page) for page in extraction_failed_pages)
                + "; the original PDF is preserved."
            )

        if substantive_text and selectors and not extraction_failed_pages:
            manifest["content_tier"] = "full_text"
            manifest["status"] = "partial" if pages_without_text else "materialized"
        elif selectors:
            manifest["content_tier"] = "excerpt_capsule"
            manifest["status"] = "partial"
        else:
            manifest["content_tier"] = "metadata_capsule"
            manifest["status"] = "partial"
            if page_count == 0:
                manifest["warnings"].append("PDF contained no pages; retained only as acquisition evidence.")
            elif not manifest["errors"]:
                manifest["warnings"].append(
                    "PDF contained no substantive extractable text; the original PDF was retained without OCR."
                )
        manifest["warnings"].extend(limitations)
        if limitations:
            manifest["limitations"] = limitations
        manifest["rights"] = {
            "declared_access": record.rights_access,
            "full_text_redistribution_assumed": True,
            "basis": "arXiv e-print PDF",
        }
        manifest["materialization"] = {
            "document": document_name,
            "normalized_document": document_name,
            "source_pdf": "source/document.pdf",
            "source_pdf_sha256": source_pdf_hash,
            "stored_characters": len(document_text),
            "selector_count": len(selectors),
            "pdf_page_count": page_count,
            "pdf_text_page_count": len(selectors),
            "pdf_pages_without_extractable_text": pages_without_text,
            "pdf_page_extraction_failures": extraction_failed_pages,
            "substantive_text": substantive_text,
        }
        return finalize_capsule(record, root, manifest)

    bundle, container_kind = unpack_arxiv(payload)
    if payload_kind not in {"tar", "single", "gzip-single"}:
        raise RuntimeError(f"unsupported classified arXiv payload: {payload_kind}")
    manifest["archive_container"] = container_kind

    stored: dict[str, str] = {}
    omitted: list[dict[str, str]] = []
    total_bytes = 0
    max_total = int(config.get("arxiv_max_stored_text_bytes", 30_000_000))
    max_files = int(config.get("arxiv_max_files", 2500))
    max_file = int(config.get("arxiv_max_single_file_bytes", 6_000_000))
    for original_name, raw in bundle:
        if len(stored) >= max_files:
            omitted.append({"path": original_name, "reason": "file-count-budget"})
            continue
        pure = PurePosixPath(original_name.replace("\\", "/"))
        if pure.is_absolute() or ".." in pure.parts:
            omitted.append({"path": original_name, "reason": "unsafe-path"})
            continue
        parts = [part for part in pure.parts if part not in {"", "."}]
        if not parts:
            continue
        pure = PurePosixPath(*parts)
        if pure.suffix.lower() not in ARXIV_TEXT_EXTENSIONS:
            omitted.append({"path": original_name, "reason": "non-text-document-member"})
            continue
        if len(raw) > max_file or total_bytes + len(raw) > max_total:
            omitted.append({"path": original_name, "reason": "size-budget"})
            continue
        text = raw.decode("utf-8", errors="replace")
        stored[pure.as_posix()] = text
        total_bytes += len(text.encode("utf-8"))

    candidates = tex_root_candidates(stored)
    if (root / "normalized").is_dir() and len(candidates) != 1:
        raise ArxivPreflightError(
            f"{record.uid}: new payload has no unique TeX root ({candidates!r}); retained capsule unchanged"
        )
    root = prepare_capsule(record)
    source_root = root / "source"
    source_root.mkdir(parents=True, exist_ok=True)
    for path, text in stored.items():
        destination = source_root / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text, encoding="utf-8")

    derivatives = write_arxiv_tex_derivatives(record, root, stored, revision=manifest["revision"])
    main_tex = derivatives["main_tex"]
    write_jsonl(
        root / "files.jsonl",
        (
            {
                "path": (source_root / path).relative_to(ROOT).as_posix(),
                "bytes": (source_root / path).stat().st_size,
                "sha256": sha256_file(source_root / path),
                "lines": len(text.splitlines()),
            }
            for path, text in sorted(stored.items())
        ),
    )

    manifest.update(
        {
            "status": "materialized" if stored else "partial",
            "content_tier": "full_text" if stored else "metadata_capsule",
            "rights": {
                "declared_access": record.rights_access,
                "full_text_redistribution_assumed": True,
                "basis": "arXiv source archive",
            },
            "materialization": {
                "stored_text_files": len(stored),
                "stored_text_bytes": total_bytes,
                **derivatives,
                "omitted_member_count": len(omitted),
            },
            "selectors": ["selectors.jsonl"],
            "omitted": omitted[:250],
        }
    )
    if not main_tex and stored:
        manifest["status"] = "partial"
        manifest["warnings"].append("TeX files were stored but a root document was not identified")
        if len(derivatives["tex_root_candidates"]) > 1:
            manifest["warnings"].append("Multiple TeX document roots require an explicit target boundary decision.")
    if derivatives["tex_include_errors"]:
        manifest["status"] = "partial"
        manifest["warnings"].append("TeX include expansion is incomplete; see materialization.tex_include_errors.")
    if derivatives["tex_normalization_diagnostics"]:
        manifest["status"] = "partial"
        limitation = (
            "Plain-text normalization excludes semantic abstracts declared in the preamble; "
            "retained source and normalized TeX remain authoritative. This is not a full TeX parser."
        )
        manifest["warnings"].append(limitation)
        manifest.setdefault("limitations", []).append(limitation)
    return finalize_capsule(record, root, manifest)


def github_api_json(url: str, timeout: int = 35, max_bytes: int = 50_000_000) -> dict[str, Any]:
    payload, _, _ = fetch_bytes(url, timeout=timeout, max_bytes=max_bytes)
    data = json.loads(payload.decode("utf-8"))
    if not isinstance(data, dict):
        raise RuntimeError(f"expected object from GitHub API: {url}")
    return data


def github_file_rank(path: str) -> tuple[int, int, str]:
    pure = PurePosixPath(path)
    lower = path.lower()
    name = pure.name.lower()
    depth = len(pure.parts)
    if name.startswith("readme") and depth == 1:
        rank = 0
    elif name in PROMINENT_GITHUB_FILENAMES and depth <= 3:
        rank = 1
    elif lower.startswith("docs/") and any(keyword in lower for keyword in GITHUB_DOC_KEYWORDS):
        rank = 2
    elif lower.startswith("docs/"):
        rank = 3
    elif name in PROMINENT_GITHUB_FILENAMES:
        rank = 4
    elif any(keyword in lower for keyword in GITHUB_DOC_KEYWORDS) and pure.suffix.lower() in GITHUB_TEXT_EXTENSIONS:
        rank = 5
    else:
        rank = 10
    return rank, depth, path


def sanitize_relative_path(path: str) -> PurePosixPath | None:
    pure = PurePosixPath(path.replace("\\", "/"))
    if pure.is_absolute() or ".." in pure.parts:
        return None
    parts = [part for part in pure.parts if part not in {"", "."}]
    return PurePosixPath(*parts) if parts else None


def decode_github_blob(blob: dict[str, Any]) -> bytes:
    content = blob.get("content")
    encoding = blob.get("encoding")
    if not isinstance(content, str):
        raise RuntimeError("GitHub blob has no content")
    if encoding == "base64":
        return base64.b64decode(content.replace("\n", ""))
    return content.encode("utf-8")


def extract_markdown_headings(
    text: str, path: str, *, structured: bool = False,
) -> list[dict[str, Any]]:
    """Keep legacy ATX output; opt in to Setext, fences and Pandoc simple tables."""
    headings: list[dict[str, Any]] = []
    fence = ""
    simple_table = False
    previous: tuple[int, str] | None = None
    lines = text.splitlines()
    for line_number, line in enumerate(lines, 1):
        if structured:
            if fence:
                if re.fullmatch(rf" {{0,3}}{re.escape(fence[0])}{{{len(fence)},}}[ \t]*", line):
                    fence = ""
                previous = None
                continue
            opening = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
            if opening and not (opening.group(1)[0] == "`" and "`" in opening.group(2)):
                fence = opening.group(1)
                previous = None
                continue
            if simple_table:
                if re.fullmatch(r" {0,3}-{3,}[ \t]*", line):
                    simple_table = False
                previous = None
                continue
            if (
                re.fullmatch(r" {0,3}-{3,}[ \t]*", line) and line_number + 1 < len(lines)
                and re.fullmatch(r" {0,3}-+(?:[ \t]+-+)+[ \t]*", lines[line_number + 1])
            ):
                simple_table = True
                previous = None
                continue
        match = re.match(
            r"^ {0,3}(#{1,6})[ \t]+(.+?)[ \t]*$" if structured else r"^(#{1,6})\s+(.+?)\s*$",
            line,
        )
        if match:
            heading = match.group(2).strip()
            if structured:
                heading = re.sub(r"[ \t]+#+[ \t]*$", "", heading)
            headings.append(
                {
                    "path": path,
                    "line": line_number,
                    "level": len(match.group(1)),
                    "heading": heading,
                }
            )
            previous = None
        elif structured:
            underline = re.fullmatch(r" {0,3}(=+|-+)[ \t]*", line)
            if underline and previous:
                headings.append({
                    "path": path, "line": previous[0],
                    "level": 1 if underline.group(1)[0] == "=" else 2,
                    "heading": previous[1],
                })
                previous = None
            else:
                previous = (line_number, line.strip()) if re.match(r"^ {0,3}\S", line) else None
    return headings


def derive_retained_markdown(
    source: Path, document: Path, asset_rewrites: dict[str, str],
) -> list[dict[str, Any]]:
    """Copy retained UTF-8 Markdown, rewriting only explicitly mapped img src paths.

    Line endings and all other text are preserved. Paths belong to this repository;
    returned section ranges partition the document, including its leading preamble.
    """
    if source.resolve() == document.resolve():
        raise ValueError("derived Markdown cannot overwrite its retained original")
    if not isinstance(asset_rewrites, dict) or any(
        not isinstance(old, str) or not old or not isinstance(new, str) or not new
        or "\n" in old or "\r" in old or "\n" in new or "\r" in new
        for old, new in asset_rewrites.items()
    ):
        raise ValueError("asset_rewrites must map nonempty single-line paths")
    local_path = document.resolve().relative_to(ROOT.resolve()).as_posix()
    source_path = source.resolve().relative_to(ROOT.resolve()).as_posix()
    text = source.read_bytes().decode("utf-8")
    text = re.sub(
        r"(<img\b[^>]*?\s+src\s*=\s*)([\"'])(.*?)\2",
        lambda match: match.group(1) + match.group(2)
        + asset_rewrites.get(match.group(3), match.group(3)) + match.group(2),
        text, flags=re.IGNORECASE,
    )
    lines = text.splitlines()
    headings = extract_markdown_headings(text, local_path, structured=True)
    starts = [(1, headings[0] if headings else None)] + [
        (heading["line"], heading) for heading in headings[1:]
    ]
    selectors: list[dict[str, Any]] = []
    if text.strip():
        for index, (start, heading) in enumerate(starts):
            end = starts[index + 1][0] - 1 if index + 1 < len(starts) else len(lines)
            selectors.append({
                "selector": f"derived://{local_path}#L{start}-L{end}",
                "local_path": local_path, "kind": "section" if heading else "file",
                "start_line": start, "end_line": end,
                "text_preview": next(line for line in lines[start - 1:end] if line.strip())[:700],
                "derived_from": source_path,
                **({"heading": heading["heading"], "level": heading["level"]} if heading else {}),
            })
    document.parent.mkdir(parents=True, exist_ok=True)
    document.write_bytes(text.encode("utf-8"))
    return selectors


def github_git_inventory(
    repository: str,
    config: dict[str, Any],
) -> tuple[dict[str, Any], str, str, str, None, dict[str, Any], None]:
    """Freeze a public repository and expose bounded raw-file candidates.

    ``git ls-remote`` provides the immutable default-branch commit without using the
    rate-limited REST API. Evidence is then fetched from commit-pinned raw URLs for a
    small set of conventional high-value paths. This intentionally does not claim to
    be a complete repository tree inventory.
    """
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
        raise RuntimeError(f"unsafe owner/repository identifier: {repository}")

    env = os.environ.copy()
    env.update({"GIT_TERMINAL_PROMPT": "0", "GIT_LFS_SKIP_SMUDGE": "1"})
    result = subprocess.run(
        ["git", "ls-remote", "--symref", f"https://github.com/{repository}.git", "HEAD"],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )
    if result.returncode != 0:
        diagnostic = (result.stderr or result.stdout).strip().splitlines()
        raise RuntimeError(diagnostic[-1] if diagnostic else f"git ls-remote exited {result.returncode}")
    default_branch = "HEAD"
    commit_sha = ""
    for line in result.stdout.splitlines():
        if line.startswith("ref: ") and line.endswith("\tHEAD"):
            default_branch = line.split("\t", 1)[0].removeprefix("ref: refs/heads/")
        elif line.endswith("\tHEAD"):
            commit_sha = line.split("\t", 1)[0]
    if not re.fullmatch(r"[0-9a-f]{40}", commit_sha):
        raise RuntimeError("git ls-remote did not return an immutable HEAD commit")

    candidate_paths = [
        "README.md", "README.rst", "README.txt", "README",
        "CONTRIBUTING.md", "SECURITY.md", "AGENTS.md", "CLAUDE.md",
        "pyproject.toml", "package.json", "Cargo.toml", "go.mod", "pom.xml",
        "Makefile", "Dockerfile", "docs/README.md", "docs/index.md",
        "docs/architecture.md", "docs/design.md", "docs/api.md",
        "documentation/README.md",
    ]
    entries = [
        {
            "path": path,
            "type": "blob",
            "sha": None,
            "size": 1,
            "url": None,
            "_raw_url": f"https://raw.githubusercontent.com/{repository}/{commit_sha}/{urllib.parse.quote(path)}",
        }
        for path in candidate_paths
    ]
    repo_info = {
        "full_name": repository,
        "default_branch": default_branch,
        "html_url": f"https://github.com/{repository}",
        "description": None,
        "language": None,
        "topics": [],
        "license": None,
    }
    return repo_info, repository, default_branch, commit_sha, None, {"tree": entries, "truncated": True, "fallback": "commit_pinned_raw_paths"}, None


def materialize_github(record: SourceRecord, config: dict[str, Any], generated_at: str) -> dict[str, Any]:
    root = prepare_capsule(record)
    manifest = base_manifest(record, "github_repo_semantic_capsule_v2", generated_at)
    repository = record.canonical_id
    if not repository or "/" not in repository:
        manifest["errors"].append("missing canonical owner/repository")
        return finalize_capsule(record, root, manifest)

    api_root = f"https://api.github.com/repos/{repository}"
    git_clone_root: Path | None = None
    try:
        repo_info = github_api_json(api_root)
        canonical_repo = str(repo_info.get("full_name") or repository)
        default_branch = str(repo_info.get("default_branch") or "HEAD")
        commit_info = github_api_json(f"https://api.github.com/repos/{canonical_repo}/commits/{urllib.parse.quote(default_branch, safe='')}")
        commit_sha = str(commit_info.get("sha"))
        commit_tree = commit_info.get("commit", {}).get("tree", {})
        tree_sha = str(commit_tree.get("sha") or "")
        if not tree_sha:
            raise RuntimeError("default branch commit has no tree SHA")
        try:
            tree_info = github_api_json(
                f"https://api.github.com/repos/{canonical_repo}/git/trees/{tree_sha}?recursive=1",
                max_bytes=int(config.get("github_max_tree_response_bytes", 50_000_000)),
            )
        except Exception as tree_error:
            # Large repositories can exceed the recursive-tree response budget. Fall back to
            # bounded root/docs listings instead of degrading immediately to metadata-only.
            manifest["warnings"].append(f"recursive tree fallback: {tree_error}")
            fallback_entries: list[dict[str, Any]] = []
            listing_urls = [
                f"https://api.github.com/repos/{canonical_repo}/contents?ref={commit_sha}",
                f"https://api.github.com/repos/{canonical_repo}/contents/docs?ref={commit_sha}",
                f"https://api.github.com/repos/{canonical_repo}/contents/doc?ref={commit_sha}",
            ]
            for listing_url in listing_urls:
                try:
                    payload, _, _ = fetch_bytes(listing_url, timeout=35, max_bytes=8_000_000)
                    listing = json.loads(payload.decode("utf-8"))
                    if isinstance(listing, list):
                        for listed in listing:
                            if not isinstance(listed, dict) or listed.get("type") != "file":
                                continue
                            fallback_entries.append(
                                {
                                    "path": listed.get("path"),
                                    "type": "blob",
                                    "sha": listed.get("sha"),
                                    "size": listed.get("size"),
                                    "url": listed.get("git_url"),
                                }
                            )
                except Exception as listing_error:
                    manifest["warnings"].append(f"listing fallback failed: {listing_error}")
            tree_info = {"tree": fallback_entries, "truncated": True, "fallback": True}
    except Exception as api_error:
        try:
            repo_info, canonical_repo, default_branch, commit_sha, tree_sha, tree_info, git_clone_root = github_git_inventory(repository, config)
            manifest["warnings"].append(f"GitHub API unavailable; used Git transport fallback: {api_error}")
        except Exception as git_error:
            manifest["errors"].append(f"GitHub API: {api_error}")
            manifest["errors"].append(f"Git fallback: {git_error}")
            manifest["status"] = "metadata_only"
            return finalize_capsule(record, root, manifest)

    entries = tree_info.get("tree") if isinstance(tree_info.get("tree"), list) else []
    blobs = [entry for entry in entries if isinstance(entry, dict) and entry.get("type") == "blob"]
    extension_counts: Counter[str] = Counter()
    top_level_counts: Counter[str] = Counter()
    for entry in blobs:
        path = str(entry.get("path") or "")
        pure = PurePosixPath(path)
        extension_counts[pure.suffix.lower() or "<none>"] += 1
        top_level_counts[pure.parts[0] if pure.parts else "<root>"] += 1

    max_files = int(config.get("github_max_evidence_files", 35))
    max_file_bytes = int(config.get("github_max_single_file_bytes", 250_000))
    max_total_bytes = int(config.get("github_max_total_evidence_bytes", 3_000_000))
    ranked = sorted(blobs, key=lambda entry: github_file_rank(str(entry.get("path") or "")))
    selected: list[dict[str, Any]] = []
    total_selected_size = 0
    seen_paths: set[str] = set()
    for entry in ranked:
        path = str(entry.get("path") or "")
        if path in seen_paths:
            continue
        seen_paths.add(path)
        rank = github_file_rank(path)[0]
        size = int(entry.get("size") or 0)
        suffix = PurePosixPath(path).suffix.lower()
        if rank >= 10 or (suffix and suffix not in GITHUB_TEXT_EXTENSIONS) or size <= 0 or size > max_file_bytes:
            continue
        if len(selected) >= max_files or total_selected_size + size > max_total_bytes:
            continue
        selected.append(entry)
        total_selected_size += size

    evidence_root = root / "evidence" / "files"
    evidence_rows: list[dict[str, Any]] = []
    selector_rows: list[dict[str, Any]] = []
    headings: list[dict[str, Any]] = []
    document_parts: list[str] = []
    for entry in selected:
        path = str(entry.get("path") or "")
        safe_path = sanitize_relative_path(path)
        if safe_path is None:
            continue
        try:
            if entry.get("_raw_url"):
                raw, _, _ = fetch_bytes(
                    str(entry["_raw_url"]),
                    timeout=20,
                    max_bytes=max_file_bytes,
                    attempts=1,
                )
            elif git_clone_root is not None:
                raw = (git_clone_root / safe_path.as_posix()).read_bytes()
            else:
                blob = github_api_json(str(entry.get("url")))
                raw = decode_github_blob(blob)
            if b"\x00" in raw[:4096]:
                continue
            text = raw.decode("utf-8", errors="replace")
        except Exception as exc:
            manifest["warnings"].append(f"{path}: {exc}")
            continue
        destination = evidence_root / safe_path.as_posix()
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text, encoding="utf-8")
        lines = text.splitlines()
        local_path = destination.relative_to(ROOT).as_posix()
        selector_base = f"github://{canonical_repo}@{commit_sha}/{path}"
        selector_rows.append(
            {
                "selector": f"{selector_base}#L1-L{max(1, len(lines))}",
                "local_path": local_path,
                "kind": "file",
                "start_line": 1,
                "end_line": max(1, len(lines)),
            }
        )
        for heading in extract_markdown_headings(text, path):
            headings.append(heading)
            selector_rows.append(
                {
                    "selector": f"{selector_base}#L{heading['line']}",
                    "local_path": local_path,
                    "kind": "heading",
                    "heading": heading["heading"],
                    "start_line": heading["line"],
                    "end_line": heading["line"],
                }
            )
        evidence_rows.append(
            {
                "repository_path": path,
                "local_path": local_path,
                "blob_sha": entry.get("sha"),
                "bytes": destination.stat().st_size,
                "sha256": sha256_file(destination),
                "lines": len(lines),
            }
        )
        excerpt_lines = lines[: min(len(lines), int(config.get("github_document_excerpt_lines", 220)))]
        document_parts.append(f"\n\n## `{path}`\n\n" + "\n".join(excerpt_lines))

    write_jsonl(root / "evidence" / "files.jsonl", evidence_rows)
    write_jsonl(root / "selectors.jsonl", selector_rows)
    repository_map = {
        "repository": canonical_repo,
        "requested_repository": repository,
        "default_branch": default_branch,
        "commit": commit_sha,
        "tree_sha": tree_sha,
        "tree_truncated": bool(tree_info.get("truncated")),
        "repository_description": repo_info.get("description"),
        "primary_language": repo_info.get("language"),
        "topics": repo_info.get("topics") or [],
        "license": (repo_info.get("license") or {}).get("spdx_id") if isinstance(repo_info.get("license"), dict) else None,
        "repository_file_count_seen": len(blobs),
        "selected_evidence_files": len(evidence_rows),
        "top_level_counts": dict(top_level_counts.most_common(30)),
        "extension_counts": dict(extension_counts.most_common(30)),
        "prominent_headings": headings[:250],
    }
    write_yaml(root / "repository-map.yaml", repository_map)

    description = str(repo_info.get("description") or record.title or "No repository description supplied.")
    document_header = (
        f"# Repository semantic capsule: {canonical_repo}\n\n"
        f"- Commit: `{commit_sha}`\n"
        f"- Default branch: `{default_branch}`\n"
        f"- Description: {description}\n"
        f"- Selected evidence files: {len(evidence_rows)} of {len(blobs)} files observed\n"
        "- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.\n"
    )
    (root / "document.md").write_text(document_header + "".join(document_parts) + "\n", encoding="utf-8")

    wiki_root = root / "wiki"
    wiki_root.mkdir(parents=True, exist_ok=True)
    (wiki_root / "index.md").write_text(
        f"# {canonical_repo}\n\n"
        "- [Overview](overview.md)\n"
        "- [Architecture evidence](architecture.md)\n"
        "- [Interfaces and operations](interfaces-and-operations.md)\n",
        encoding="utf-8",
    )
    heading_lines = [f"- `{item['path']}:{item['line']}` — {item['heading']}" for item in headings[:120]]
    (wiki_root / "overview.md").write_text(
        f"# Overview: {canonical_repo}\n\n{description}\n\n"
        f"Frozen at `{commit_sha}`. This is a candidate semantic view, not a verified runtime assessment.\n",
        encoding="utf-8",
    )
    (wiki_root / "architecture.md").write_text(
        f"# Architecture evidence: {canonical_repo}\n\n"
        + ("\n".join(heading_lines) if heading_lines else "No architecture headings were extracted.")
        + "\n",
        encoding="utf-8",
    )
    interface_files = [row["repository_path"] for row in evidence_rows if any(token in row["repository_path"].lower() for token in ("api", "cli", "config", "schema", "workflow", "interface"))]
    (wiki_root / "interfaces-and-operations.md").write_text(
        f"# Interfaces and operations: {canonical_repo}\n\n"
        + "\n".join(f"- `{path}`" for path in interface_files[:100])
        + "\n",
        encoding="utf-8",
    )

    manifest.update(
        {
            "status": "materialized" if evidence_rows else "partial",
            "content_tier": "semantic_capsule" if evidence_rows else "metadata_capsule",
            "canonical_id": canonical_repo,
            "canonical_url": str(repo_info.get("html_url") or record.canonical_url),
            "revision": commit_sha,
            "rights": {
                "declared_access": record.rights_access,
                "full_text_redistribution_assumed": False,
                "repository_license": repository_map["license"],
                "basis": "bounded commit-pinned evidence selection; repository not vendored",
            },
            "retrievals": [
                {
                    "resolved_url": str(repo_info.get("html_url") or record.canonical_url),
                    "commit": commit_sha,
                    "tree_sha": tree_sha,
                    "tree_truncated": bool(tree_info.get("truncated")),
                }
            ],
            "materialization": {
                "repository_file_count_seen": len(blobs),
                "selected_evidence_files": len(evidence_rows),
                "selected_evidence_bytes": sum(row["bytes"] for row in evidence_rows),
                "selector_count": len(selector_rows),
                "repo_wiki_pages": 4,
            },
            "selectors": ["selectors.jsonl"],
            "limitations": [
                "The full repository is not copied.",
                "Static evidence does not prove tests, benchmarks, security, or production behavior.",
                "Generated repo wiki pages remain candidate views.",
            ],
        }
    )
    result = finalize_capsule(record, root, manifest)
    if git_clone_root is not None:
        shutil.rmtree(git_clone_root.parent, ignore_errors=True)
    return result


def html_to_sections(payload: bytes, resolved_url: str) -> tuple[str, list[dict[str, Any]], str | None]:
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(payload, "html.parser")
    for tag in soup(["script", "style", "noscript", "svg", "canvas", "form", "nav", "footer"]):
        tag.decompose()
    title = soup.title.get_text(" ", strip=True) if soup.title else None
    main = soup.find("main") or soup.find("article") or soup.body or soup
    blocks: list[dict[str, Any]] = []
    text_parts: list[str] = []
    index = 0
    for node in main.find_all(["h1", "h2", "h3", "h4", "p", "li", "pre"]):
        text = node.get_text(" ", strip=True)
        if not text or len(text) < 2:
            continue
        index += 1
        kind = "heading" if node.name and node.name.startswith("h") else ("code" if node.name == "pre" else "paragraph")
        blocks.append(
            {
                "selector": f"web://{sha256_bytes(resolved_url.encode())[:16]}#B{index}",
                "kind": kind,
                "ordinal": index,
                "text_preview": text[:240],
            }
        )
        if kind == "heading":
            level = int(node.name[1]) if node.name and len(node.name) > 1 and node.name[1].isdigit() else 2
            text_parts.append("\n" + "#" * min(6, max(1, level)) + " " + text + "\n")
        else:
            text_parts.append(text + "\n")
    return "\n".join(text_parts).strip() + "\n", blocks, title


def extract_pdf_text(
    payload: bytes, max_pages: int | None = None, *, extraction_mode: str = "layout",
) -> tuple[str, list[dict[str, Any]], int]:
    from pypdf import PdfReader

    if extraction_mode not in {"layout", "plain"}:
        raise ValueError("unsupported PDF text extraction mode")
    reader = PdfReader(io.BytesIO(payload))
    page_count = len(reader.pages)
    limit = page_count if max_pages is None else min(page_count, max_pages)
    text_parts: list[str] = []
    selectors: list[dict[str, Any]] = []
    for page_index in range(limit):
        try:
            text = reader.pages[page_index].extract_text(
                extraction_mode=extraction_mode,
                **({"layout_mode_strip_rotated": False} if extraction_mode == "layout" else {}),
            ) or ""
        except Exception as exc:
            text = f"[page extraction failed: {exc}]"
        text_parts.append(f"\n\n## Page {page_index + 1}\n\n{text.strip()}\n")
        selectors.append(
            {
                "selector": f"pdf://sha256-PENDING#page={page_index + 1}",
                "kind": "page",
                "page": page_index + 1,
                "text_preview": text.strip()[:240],
            }
        )
    return "".join(text_parts).strip() + "\n", selectors, page_count


def arxiv_pdf_version_url(canonical_id: Any, source_version: Any) -> str:
    """Require an existing arXiv identity and an explicit, positive version."""
    if not isinstance(canonical_id, str) or not re.fullmatch(r"\d{4}\.\d{4,5}", canonical_id):
        raise ValueError("PDF supplement requires an unversioned arXiv canonical ID")
    if not isinstance(source_version, str) or not re.fullmatch(r"v[1-9]\d*", source_version):
        raise ValueError("PDF supplement requires a fixed vN source version")
    return f"https://arxiv.org/pdf/{canonical_id}{source_version}"


def build_pdf_supplement(
    root: Path, source_version: str, retrieval: dict[str, Any], rights: dict[str, Any],
    *, body_quality_verified: bool = False, limitations: list[str] | None = None,
    primary_excerpt: dict[str, int] | None = None,
) -> dict[str, Any]:
    """Derive page text from an already acquired PDF without rebuilding the TeX capsule.

    The caller owns acquisition, the independently reviewed PDF notice, canonical
    metadata/audit updates and the final local-file inventory. No source bytes,
    default document/selectors, manifest or metadata are changed here.
    """
    manifest = load_yaml(root / "manifest.yaml")
    if manifest.get("source_type") != "arxiv" or manifest.get("adapter") != "arxiv_latex_v2":
        raise ValueError("PDF supplement is only supported on an existing arXiv TeX capsule")
    version_url = arxiv_pdf_version_url(manifest.get("canonical_id"), source_version)
    metadata = load_yaml(root / "source-metadata.yaml")
    if (metadata.get("versioning") or {}).get("source_version") != source_version:
        raise ValueError("PDF supplement version differs from the retained source version")
    payload = (root / "pdf-supplement/document.pdf").read_bytes()
    if not payload.startswith(b"%PDF-"):
        raise ValueError("PDF supplement source is not a PDF")
    source_hash = sha256_bytes(payload)
    revision = f"sha256:{source_hash}"
    if (
        retrieval.get("requested_urls") != [version_url] or retrieval.get("resolved_url") != version_url
        or retrieval.get("bytes") != len(payload) or retrieval.get("sha256") != source_hash
        or retrieval.get("content_type", "").split(";", 1)[0].strip() != "application/pdf"
        or not retrieval.get("retrieved_at")
    ):
        raise ValueError("PDF supplement retrieval does not describe the fixed-version PDF")
    package = rights.get("redistribution_package") or {}
    gate = rights.get("publication_gate") or {}
    if not all(isinstance(package.get(field), str) and package[field].strip() for field in (
        "source_revision", "source_version_url", "notice_path", "attribution", "modifications", "scope",
    )) or package.get("source_revision") != revision or package.get("source_version_url") != version_url:
        raise ValueError("PDF supplement needs its own complete, revision-bound redistribution package")
    if gate.get("decision") != "allow" or gate.get("approved_scope") != package.get("scope"):
        raise ValueError("PDF supplement scope has no explicit publication allowance")

    # This batch contains body text in Form XObjects that layout mode omits.
    # The optional layer explicitly uses plain mode; primary PDFs keep layout.
    document_text, extracted, page_count = extract_pdf_text(payload, extraction_mode="plain")
    selectors = []
    empty_pages = []
    failed_pages = []
    for original in extracted:
        preview = original.get("text_preview") or ""
        if preview.startswith("[page extraction failed:"):
            failed_pages.append(original["page"])
        elif not preview.strip():
            empty_pages.append(original["page"])
        else:
            selectors.append({
                **original,
                "selector": f"pdf://sha256-{source_hash[:16]}#page={original['page']}",
                "local_path": (root / "pdf-supplement/document.txt").relative_to(ROOT).as_posix(),
            })
    document_text += redistribution_footer(package)
    (root / "pdf-supplement/document.txt").write_text(document_text, encoding="utf-8")
    write_jsonl(root / "pdf-supplement/selectors.jsonl", selectors)
    return {
        "source_version": source_version,
        "revision": revision,
        "media_type": "application/pdf",
        "retrievals": [dict(retrieval)],
        "selectors": ["pdf-supplement/selectors.jsonl"],
        "body_quality_verified": body_quality_verified,
        "limitations": list(limitations or []),
        **({"primary_excerpt": dict(primary_excerpt)} if primary_excerpt is not None else {}),
        "rights": rights,
        "materialization": {
            "source_pdf": "pdf-supplement/document.pdf", "source_pdf_sha256": source_hash,
            "document": "pdf-supplement/document.txt", "normalized_document": "pdf-supplement/document.txt",
            "stored_characters": len(document_text), "selector_count": len(selectors),
            "pdf_page_count": page_count, "pdf_text_page_count": len(selectors),
            "pdf_text_extraction_mode": "plain",
            "pdf_pages_without_extractable_text": empty_pages, "pdf_page_extraction_failures": failed_pages,
            "substantive_text": has_substantive_document_text(document_text.split("<!-- materialization-redistribution-notice -->", 1)[0]),
        },
    }


def filter_selectors_for_document(
    selectors: Iterable[dict[str, Any]],
    document_text: str,
) -> tuple[list[dict[str, Any]], int]:
    """Keep only selectors whose cited evidence remains in ``document_text``.

    Generic adapters create selectors from the downloaded representation before the
    local character budget is applied.  A selector for a removed HTML block or PDF
    page is not locally resolvable merely because its ``local_path`` still exists.
    Preview evidence must occur in the stored text, and line selectors are clamped to
    the actual stored file.
    """

    stored_lines = document_text.splitlines()
    line_count = max(1, len(stored_lines))
    stored_pages = {
        int(match.group(1))
        for match in re.finditer(r"(?m)^## Page (\d+)\s*$", document_text)
    }
    retained: list[dict[str, Any]] = []
    omitted = 0

    for original in selectors:
        selector = dict(original)
        start_line = selector.get("start_line")
        end_line = selector.get("end_line")
        if start_line is not None or end_line is not None:
            if (
                not isinstance(start_line, int)
                or isinstance(start_line, bool)
                or not isinstance(end_line, int)
                or isinstance(end_line, bool)
                or start_line < 1
                or end_line < start_line
                or start_line > line_count
            ):
                omitted += 1
                continue
            clamped_end = min(end_line, line_count)
            selector["end_line"] = clamped_end
            selector_id = selector.get("selector")
            if isinstance(selector_id, str) and clamped_end != end_line:
                selector["selector"] = re.sub(r"(#L\d+-L)\d+$", rf"\g<1>{clamped_end}", selector_id)

        page = selector.get("page")
        if page is not None and (
            not isinstance(page, int)
            or isinstance(page, bool)
            or page < 1
            or page not in stored_pages
        ):
            omitted += 1
            continue

        preview = selector.get("text_preview")
        if preview is not None:
            if not isinstance(preview, str) or not preview or preview not in document_text:
                omitted += 1
                continue

        retained.append(selector)

    return retained, omitted


def has_substantive_document_text(document_text: str) -> bool:
    """Reject navigation/title shells that contain no non-heading evidence."""

    non_heading = re.sub(r"(?m)^\s{0,3}#{1,6}\s+.*$", "", document_text)
    tokens = re.findall(r"[\w\u0080-\uffff]+", non_heading)
    return len(non_heading.strip()) >= 20 and len(tokens) >= 3


def replay_retained_markdown(
    record: SourceRecord, manifest: dict[str, Any], generated_at: str,
) -> dict[str, Any]:
    """Replay an explicitly fixed snapshot without fetching or clearing originals."""
    root = record.capsule_root
    try:
        identity = {
            "uid": record.uid, "source_type": record.source_type,
            "canonical_id": record.canonical_id, "canonical_url": record.canonical_url,
            "title": record.title, "metadata_path": record.relative_metadata_path,
        }
        if any(manifest.get(field) != value for field, value in identity.items()):
            raise ValueError("retained snapshot canonical identity differs from metadata")
        source_metadata = load_yaml(root / "source-metadata.yaml")
        version = (record.metadata.get("versioning") or {}).get("source_version")
        if (
            not isinstance(source_metadata, dict) or not isinstance(version, str) or not version.strip()
            or manifest.get("source_version") != version
            or (source_metadata.get("versioning") or {}).get("source_version") != version
            or any(source_metadata.get(field) != record.metadata.get(field) for field in (
                "uid", "title", "url", "canonical_url", "canonical_id",
            ))
        ):
            raise ValueError("retained snapshot source metadata or selected version differs")
        materialization = manifest["materialization"]
        paths: dict[str, Path] = {}
        for field, prefix in (("retained_markdown_source", "source"), ("document", "normalized")):
            relative_path = sanitize_relative_path(materialization[field])
            if relative_path is None or relative_path.parts[0] != prefix:
                raise ValueError(f"retained {field} must be a capsule-local {prefix} path")
            paths[field] = (root / relative_path).resolve()
            paths[field].relative_to(root.resolve())
        source, document = paths["retained_markdown_source"], paths["document"]
        from validate_materialization_completeness import validate_retained_markdown_binding
        binding_errors: list[str] = []
        validate_retained_markdown_binding(
            manifest, root, {source.relative_to(ROOT.resolve()).as_posix(): sha256_file(source)},
            binding_errors, repository_root=ROOT,
        )
        if binding_errors:
            raise ValueError("; ".join(binding_errors))
        rewrites = materialization.get("asset_rewrites", {})
        if not isinstance(rewrites, dict):
            raise ValueError("retained asset_rewrites must be an explicit path mapping")
        for old, new in rewrites.items():
            if not isinstance(old, str) or not isinstance(new, str):
                raise ValueError("retained asset_rewrites must map local paths")
            asset = (source.parent / old).resolve()
            asset.relative_to(root.resolve())
            if not asset.is_file() or asset != (document.parent / new).resolve():
                raise ValueError("retained asset rewrite must resolve to the same local original")
        package = (record.metadata.get("rights") or {}).get("redistribution_package")
        if package and package.get("source_revision") != manifest.get("revision"):
            raise ValueError("redistribution package does not cover the retained snapshot revision")
        selectors = derive_retained_markdown(source, document, rewrites)
        write_jsonl(root / "selectors.jsonl", selectors)
        manifest["generated_at"] = generated_at
        manifest["selectors"] = ["selectors.jsonl"]
        materialization.update({
            "normalized_document": materialization["document"],
            "stored_characters": len(document.read_bytes().decode("utf-8")),
            "selector_count": len(selectors),
        })
        return finalize_capsule(record, root, manifest)
    except (KeyError, TypeError, AttributeError, ValueError, OSError, yaml.YAMLError) as exc:
        raise RetainedMarkdownPreflightError(f"{record.uid}: {exc}; retained originals preserved") from exc


def materialize_generic(
    record: SourceRecord,
    config: dict[str, Any],
    generated_at: str,
    *,
    existing_root: Path | None = None,
    existing_manifest: dict[str, Any] | None = None,
    force_excerpt_reason: str | None = None,
) -> dict[str, Any]:
    if existing_root is None and (record.capsule_root / "manifest.yaml").is_file():
        retained = load_yaml(record.capsule_root / "manifest.yaml")
        retained_materialization = retained.get("materialization") if isinstance(retained, dict) else None
        if isinstance(retained_materialization, dict) and "retained_markdown_source" in retained_materialization:
            return replay_retained_markdown(record, retained, generated_at)
    root = existing_root or prepare_capsule(record)
    manifest = existing_manifest or base_manifest(record, "generic_web_or_document_v2", generated_at)
    if existing_root is None:
        # prepare_capsule already wrote this; retained for clarity.
        pass
    urls = candidate_urls(record)
    if not urls:
        manifest["errors"].append("no retrievable URL in metadata")
        return finalize_capsule(record, root, manifest)

    payload: bytes | None = None
    resolved_url: str | None = None
    headers: dict[str, str] = {}
    requested_url: str | None = None
    for url in urls[: int(config.get("generic_max_candidate_urls", 4))]:
        try:
            payload, resolved_url, headers = fetch_bytes(
                url,
                timeout=int(config.get("http_timeout_seconds", 45)),
                max_bytes=int(config.get("generic_max_download_bytes", 30_000_000)),
            )
            requested_url = url
            break
        except Exception as exc:
            manifest["warnings"].append(str(exc))
    if payload is None or resolved_url is None:
        manifest["errors"].append("all candidate URLs failed")
        return finalize_capsule(record, root, manifest)

    content_hash = sha256_bytes(payload)
    content_type = headers.get("content-type", "").lower()
    full_text_allowed = text_is_open(record, config, resolved_url)
    manifest["revision"] = f"sha256:{content_hash}"
    manifest["retrievals"].append(
        {
            "requested_url": requested_url,
            "resolved_url": resolved_url,
            "content_type": content_type,
            "bytes": len(payload),
            "sha256": content_hash,
        }
    )
    manifest["rights"]["full_text_redistribution_assumed"] = full_text_allowed

    selectors: list[dict[str, Any]] = []
    document_text = ""
    document_name = "document.md"
    page_count: int | None = None
    is_pdf = payload.startswith(b"%PDF") or "application/pdf" in content_type or resolved_url.lower().split("?", 1)[0].endswith(".pdf")
    try:
        if is_pdf:
            max_pages = None if full_text_allowed else int(config.get("restricted_pdf_excerpt_pages", 3))
            document_text, selectors, page_count = extract_pdf_text(payload, max_pages=max_pages)
            pdf_hash_prefix = content_hash[:16]
            for selector in selectors:
                selector["selector"] = selector["selector"].replace("sha256-PENDING", f"sha256-{pdf_hash_prefix}")
            document_name = "document.txt"
        elif "html" in content_type or payload.lstrip().startswith((b"<!DOCTYPE html", b"<html", b"<HTML")):
            document_text, selectors, detected_title = html_to_sections(payload, resolved_url)
            if detected_title:
                manifest["detected_title"] = detected_title
        else:
            document_text = payload.decode("utf-8", errors="replace")
            lines = document_text.splitlines()
            selectors = [
                {
                    "selector": f"text://sha256-{content_hash[:16]}#L1-L{max(1, len(lines))}",
                    "kind": "file",
                    "start_line": 1,
                    "end_line": max(1, len(lines)),
                    "text_preview": document_text[:240],
                }
            ]
            document_name = "document.txt"
    except Exception as exc:
        manifest["errors"].append(f"content parsing failed: {exc}")
        return finalize_capsule(record, root, manifest)

    content_was_truncated = False
    if not full_text_allowed or force_excerpt_reason:
        max_chars = int(config.get("restricted_excerpt_chars", 8_000))
        if len(document_text) > max_chars:
            content_was_truncated = True
            document_text = document_text[:max_chars].rstrip() + "\n"
        if force_excerpt_reason:
            manifest["warnings"].append(force_excerpt_reason)
        else:
            manifest["warnings"].append(
                "Full-text redistribution was not established; stored content is a bounded evidence excerpt."
            )
    else:
        max_chars = int(config.get("open_full_text_max_chars", 1_500_000))
        if len(document_text) > max_chars:
            content_was_truncated = True
            document_text = document_text[:max_chars].rstrip() + "\n"
            manifest["warnings"].append("Open text exceeded the configured local character budget and was truncated.")

    selectors, omitted_selector_count = filter_selectors_for_document(selectors, document_text)
    if omitted_selector_count:
        manifest["warnings"].append(
            f"Omitted {omitted_selector_count} selectors whose evidence was outside the stored document boundary."
        )

    if document_text.strip():
        (root / document_name).write_text(document_text, encoding="utf-8")
        substantive_text = has_substantive_document_text(document_text)
        if substantive_text and selectors:
            local_path = (root / document_name).relative_to(ROOT).as_posix()
            for selector in selectors:
                selector["local_path"] = local_path
            write_jsonl(root / "selectors.jsonl", selectors)
            complete_full_text = (
                full_text_allowed and not content_was_truncated and not force_excerpt_reason
            )
            manifest["status"] = "materialized" if complete_full_text else "partial"
            manifest["content_tier"] = "full_text" if complete_full_text else "excerpt_capsule"
            manifest["selectors"] = ["selectors.jsonl"]
        else:
            selectors = []
            if not substantive_text:
                manifest["warnings"].append(
                    "Retrieved document contained no substantive non-heading text; retained only as acquisition evidence."
                )
            else:
                manifest["warnings"].append(
                    "Retrieved document had no selector that resolved inside the stored boundary; retained only as acquisition evidence."
                )
        manifest["materialization"] = {
            "document": document_name,
            "stored_characters": len(document_text),
            "selector_count": len(selectors),
            "pdf_page_count": page_count,
            "full_text_allowed": full_text_allowed,
            "content_was_truncated": content_was_truncated,
            "substantive_text": substantive_text,
            "omitted_selector_count": omitted_selector_count,
            "forced_excerpt_reason": force_excerpt_reason,
        }
    return finalize_capsule(record, root, manifest)


def adapter_name(source_type: str) -> str:
    if source_type == "arxiv":
        return "arxiv_latex_v2"
    if source_type == "github":
        return "github_repo_semantic_capsule_v2"
    return "generic_web_or_document_v2"


def evidence_role_for(status: Any, content_tier: Any) -> str:
    if status in {"metadata_only", "failed"} or content_tier == "metadata_capsule":
        return "catalog-only"
    if status == "partial" or content_tier == "excerpt_capsule":
        return "bounded-excerpt"
    if content_tier == "semantic_capsule":
        return "static-repository-evidence"
    return "source-text"


def materialize_one(record: SourceRecord, config: dict[str, Any], generated_at: str) -> dict[str, Any]:
    try:
        if record.source_type == "arxiv":
            with _arxiv_semaphore:
                time.sleep(0.25)
                return materialize_arxiv(record, config, generated_at)
        if record.source_type == "github":
            with _github_semaphore:
                return materialize_github(record, config, generated_at)
        with _generic_semaphore:
            return materialize_generic(record, config, generated_at)
    except (RedistributionPackageError, ArxivPreflightError, RetainedMarkdownPreflightError):
        raise
    except Exception as exc:
        root = record.capsule_root
        if record.source_type == "arxiv" and root.exists():
            raise
        if not root.exists():
            root = prepare_capsule(record)
        manifest = base_manifest(record, adapter_name(record.source_type), generated_at)
        manifest["status"] = "metadata_only"
        manifest["errors"].append(f"unhandled adapter failure: {type(exc).__name__}: {exc}")
        return finalize_capsule(record, root, manifest)


def rebuild_registry(records: list[SourceRecord], manifests: dict[str, dict[str, Any]], generated_at: str) -> None:
    entries: list[dict[str, Any]] = []
    for record in records:
        manifest = manifests[record.uid]
        manifest_path = record.capsule_root / "manifest.yaml"
        entries.append(
            {
                "uid": record.uid,
                "source_type": record.source_type,
                "canonical_id": record.canonical_id,
                "title": record.title,
                "canonical_url": record.canonical_url,
                "metadata_path": record.relative_metadata_path,
                "verification_state": (
                    record.metadata.get("verification", {}).get("state")
                    if isinstance(record.metadata.get("verification"), dict)
                    else "pending"
                ),
                "priority": record.priority,
                "adapter": {
                    "name": manifest.get("adapter"),
                    "semanticization_required": record.source_type == "github",
                },
                "materialization": {
                    "state": manifest.get("status"),
                    "content_tier": manifest.get("content_tier"),
                    "evidence_role": evidence_role_for(
                        manifest.get("status"), manifest.get("content_tier")
                    ),
                    "revision": manifest.get("revision"),
                    "root": record.capsule_root.relative_to(ROOT).as_posix(),
                    "manifest": manifest_path.relative_to(ROOT).as_posix(),
                    "local_bytes": manifest.get("local_bytes", 0),
                },
            }
        )
    entries.sort(key=lambda item: (str(item["source_type"]), str(item["uid"])))
    REGISTRY_ROOT.mkdir(parents=True, exist_ok=True)
    write_yaml(
        REGISTRY_ROOT / "registry.yaml",
        {
            "registry_version": 2,
            "generated_at": generated_at,
            "repository": "thsno02/solid-octo-couscous",
            "entry_count": len(entries),
            "entries": entries,
        },
    )
    write_jsonl(REGISTRY_ROOT / "registry.jsonl", entries)
    (REGISTRY_ROOT / "README.md").write_text(
        "# 来源注册表（Source Registry）\n\n"
        "每条已收集的 metadata record 都在 `materialized_sources/corpus/` 下对应一个本地胶囊。"
        "注册表明确区分全文（full text）、repository 语义胶囊（semantic capsule）、"
        "有边界的摘录（bounded excerpt）和仅 metadata 的胶囊。\n",
        encoding="utf-8",
    )


def write_indexes_and_audit(records: list[SourceRecord], manifests: dict[str, dict[str, Any]], generated_at: str) -> None:
    items: list[dict[str, Any]] = []
    by_type: dict[str, Counter[str]] = defaultdict(Counter)
    statuses: Counter[str] = Counter()
    tiers: Counter[str] = Counter()
    metadata_only: list[dict[str, Any]] = []
    partial: list[dict[str, Any]] = []
    total_bytes = 0
    total_hashes = 0
    for record in records:
        manifest = manifests[record.uid]
        status = str(manifest.get("status") or "unknown")
        tier = str(manifest.get("content_tier") or "unknown")
        statuses[status] += 1
        tiers[tier] += 1
        by_type[record.source_type][tier] += 1
        total_bytes += int(manifest.get("local_bytes") or 0)
        total_hashes += len(manifest.get("local_files") or [])
        item = {
            "uid": record.uid,
            "source_type": record.source_type,
            "canonical_id": record.canonical_id,
            "title": record.title,
            "status": status,
            "content_tier": tier,
            "manifest": (record.capsule_root / "manifest.yaml").relative_to(ROOT).as_posix(),
            "revision": manifest.get("revision"),
            "local_bytes": manifest.get("local_bytes", 0),
        }
        items.append(item)
        if tier == "metadata_capsule":
            metadata_only.append(item)
        elif status == "partial":
            partial.append(item)
    items.sort(key=lambda item: (str(item["source_type"]), str(item["uid"])))
    full_or_semantic = tiers["full_text"] + tiers["semantic_capsule"]
    locally_usable = full_or_semantic + tiers["excerpt_capsule"]
    total = len(records)
    index = {
        "materialization_index_version": 2,
        "generated_at": generated_at,
        "corpus_root": "materialized_sources/corpus",
        "summary": {
            "records": total,
            "statuses": dict(statuses),
            "content_tiers": dict(tiers),
            "all_records_have_local_capsules": len(items) == total,
            "full_or_semantic_count": full_or_semantic,
            "locally_usable_count": locally_usable,
            "local_bytes": total_bytes,
            "hashed_files": total_hashes,
        },
        "items": items,
    }
    write_yaml(MATERIALIZED_ROOT / "index.yaml", index)
    (MATERIALIZED_ROOT / "README.md").write_text(
        "# 物化来源语料（Materialized Source Corpus）\n\n"
        "`corpus/` 为每条 metadata record 保存一个本地胶囊（local capsule）。"
        "内容层级（content tier）包括：\n\n"
        "- `full_text`：技术上已取得本地全文；该层级本身不证明具备公开再分发许可；\n"
        "- `semantic_capsule`：GitHub repository 已固定到具体 commit，并根据选定证据生成语义胶囊；\n"
        "- `excerpt_capsule`：未确认再分发权利时，只保存有边界的本地摘录；\n"
        "- `metadata_capsule`：仅允许元数据消费；也可能保留抓取失败的标题等诊断性文件，不能作为正文证据。\n\n"
        "本地胶囊不自动等于可信知识（trusted knowledge）。\n\n"
        "公开存储另受[版权与许可审计](../docs/materialization-rights-audit.md)约束。"
        "`full_text_redistribution_assumed` 是历史获取器的假设，不是许可凭据；"
        "Git LFS 或公开 release artifact 也不消除再分发义务。摘录有长度边界也不自动代表具备公开再分发权。\n\n"
        "离线修复和定位器抽检结果见 `raw_data/audits/`。注册表的 `evidence_role` 将仅目录导航（catalog-only）、"
        "有限摘录（bounded-excerpt）、仓库静态证据（static-repository-evidence）与原文（source-text）分开。\n",
        encoding="utf-8",
    )
    audit = {
        "audit_id": "materialization-completeness-2026-09-10",
        "generated_at": generated_at,
        "repository": "thsno02/solid-octo-couscous",
        "collection_records": total,
        "local_capsules": len(items),
        "all_records_local": len(items) == total,
        "status_counts": dict(statuses),
        "content_tier_counts": dict(tiers),
        "by_source_type": {key: dict(value) for key, value in sorted(by_type.items())},
        "full_or_semantic_coverage": round(full_or_semantic / total, 4) if total else 0,
        "locally_usable_coverage": round(locally_usable / total, 4) if total else 0,
        "metadata_only_count": len(metadata_only),
        "partial_count": len(partial),
        "metadata_only_items": metadata_only,
        "partial_items": partial,
        "local_bytes": total_bytes,
        "hashed_files": total_hashes,
        "interpretation": (
            "Every record having a local capsule does not mean every copyrighted or inaccessible source is mirrored in full. "
            "The content tier records the actual consumability boundary."
        ),
        "acceptance": {
            "all_metadata_records_have_local_manifest": len(items) == total,
            "no_unclassified_missing_capsule": len(items) == total,
            "full_content_gaps_are_explicit": True,
        },
    }
    AUDIT_ROOT.mkdir(parents=True, exist_ok=True)
    write_yaml(AUDIT_ROOT / "materialization_completeness_2026-09-10.yaml", audit)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="pipeline/materialization_all_260910.yaml")
    parser.add_argument("--workers", type=int, default=None)
    parser.add_argument(
        "--only-source-type",
        choices=sorted(set(DIRECTORY_SOURCE_TYPES.values())),
        help="Rebuild one source family and reuse existing capsules for all other records.",
    )
    args = parser.parse_args()

    config = load_yaml(ROOT / args.config)
    if not isinstance(config, dict):
        raise SystemExit("materialization config must be a YAML object")
    generated_at = str(config.get("generated_at") or utc_now())
    records = discover_records()
    if not records:
        raise SystemExit("no metadata records found")

    selected_records = (
        [record for record in records if record.source_type == args.only_source_type]
        if args.only_source_type
        else records
    )
    if not selected_records:
        raise SystemExit(f"no metadata records found for source type {args.only_source_type}")

    CORPUS_ROOT.mkdir(parents=True, exist_ok=True)
    workers = int(args.workers or config.get("workers", 12))
    manifests: dict[str, dict[str, Any]] = {}
    if args.only_source_type:
        for record in records:
            if record in selected_records:
                continue
            manifest_path = record.capsule_root / "manifest.yaml"
            if not manifest_path.exists():
                raise SystemExit(
                    f"cannot run an incremental rebuild; existing capsule is missing for {record.uid}"
                )
            manifest = load_yaml(manifest_path)
            if not isinstance(manifest, dict):
                raise SystemExit(f"existing manifest is invalid for {record.uid}")
            manifests[record.uid] = manifest
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        future_map = {
            pool.submit(materialize_one, record, config, generated_at): record
            for record in selected_records
        }
        for future in concurrent.futures.as_completed(future_map):
            record = future_map[future]
            try:
                manifest = future.result()
            except (RedistributionPackageError, ArxivPreflightError, RetainedMarkdownPreflightError):
                raise
            except Exception as exc:
                if record.source_type == "arxiv" and record.capsule_root.exists():
                    raise
                root = prepare_capsule(record)
                manifest = base_manifest(record, adapter_name(record.source_type), generated_at)
                manifest["errors"].append(f"executor failure: {type(exc).__name__}: {exc}")
                manifest = finalize_capsule(record, root, manifest)
            manifests[record.uid] = manifest
            print(
                f"materialized uid={record.uid} type={record.source_type} "
                f"status={manifest.get('status')} tier={manifest.get('content_tier')}",
                flush=True,
            )

    rebuild_registry(records, manifests, generated_at)
    write_indexes_and_audit(records, manifests, generated_at)
    total = len(records)
    local = sum((record.capsule_root / "manifest.yaml").exists() for record in records)
    print(f"materialization_complete records={total} local_capsules={local}")
    return 0 if local == total else 1


if __name__ == "__main__":
    raise SystemExit(main())

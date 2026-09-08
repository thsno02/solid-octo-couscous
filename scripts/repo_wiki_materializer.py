#!/usr/bin/env python3
"""Efficient commit-pinned GitHub repository semantic capsule materializer.

The full tree is indexed without requesting blob sizes. Only a bounded set of
high-value evidence files is fetched, together, through ``git archive``.
"""
from __future__ import annotations
import json
import os
import re
import shutil
import subprocess
import tarfile
import tempfile
from collections import Counter
from io import BytesIO
from pathlib import Path, PurePosixPath
from typing import Any


def run(command: list[str], cwd: Path | None = None, timeout: int = 180, binary: bool = False):
    env = os.environ.copy()
    env.update({
        "GIT_TERMINAL_PROMPT": "0",
        "GIT_ASKPASS": "echo",
    })
    result = subprocess.run(
        command,
        cwd=cwd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.decode(errors="replace")[-4000:])
    return result.stdout if binary else result.stdout.decode(errors="replace")


def parse_tree(output: str) -> list[dict[str, Any]]:
    records = []
    for line in output.splitlines():
        match = re.match(r"^(\d+)\s+(\w+)\s+([0-9a-f]{40})\t(.+)$", line)
        if not match:
            continue
        records.append({
            "mode": match.group(1),
            "type": match.group(2),
            "blob_sha": match.group(3),
            "size": None,
            "path": match.group(4),
        })
    return records


def priority(record: dict[str, Any]) -> tuple[int, int, str]:
    path = record["path"]
    name = PurePosixPath(path).name.lower()
    extension = PurePosixPath(path).suffix.lower()
    depth = len(PurePosixPath(path).parts)
    if name.startswith("readme") and depth == 1:
        rank = 0
    elif name in {
        "agents.md", "claude.md", "architecture.md", "design.md",
        "contributing.md", "security.md", "roadmap.md",
    }:
        rank = 1
    elif path.lower().startswith(("docs/", "documentation/")) and extension in {".md", ".rst", ".txt"}:
        rank = 2
    elif name in {
        "pyproject.toml", "package.json", "go.mod", "cargo.toml",
        "requirements.txt", "dockerfile", "makefile", "mkdocs.yml",
    }:
        rank = 3
    else:
        rank = 9
    return rank, depth, path.lower()


def fetch_selected(repository: Path, commit: str, paths: list[str]) -> dict[str, bytes]:
    if not paths:
        return {}
    payload = run(
        ["git", "archive", "--format=tar", commit, "--", *paths],
        cwd=repository,
        timeout=300,
        binary=True,
    )
    files: dict[str, bytes] = {}
    with tarfile.open(fileobj=BytesIO(payload), mode="r:") as archive:
        for member in archive.getmembers():
            if not member.isfile():
                continue
            handle = archive.extractfile(member)
            if handle is not None:
                files[member.name] = handle.read()
    return files


def materialize(item: dict[str, Any], metadata_paths: dict, timestamp: str, core):
    name = str(item["repo"])
    root = core.OUT / "github" / core.key(name)
    shutil.rmtree(root, ignore_errors=True)
    (root / "evidence" / "excerpts").mkdir(parents=True)
    (root / "wiki").mkdir(parents=True)

    with tempfile.TemporaryDirectory() as temporary:
        repository = Path(temporary) / "repository"
        try:
            run([
                "git", "clone", "--filter=blob:none", "--no-checkout", "--depth", "1",
                f"https://github.com/{name}.git", str(repository),
            ], timeout=240)
            commit = run(["git", "rev-parse", "HEAD"], repository, timeout=30).strip()
            tree_output = run(["git", "ls-tree", "-r", commit], repository, timeout=90)
            records = parse_tree(tree_output)
        except Exception as exc:
            failure = {
                "manifest_version": 1,
                "source_type": "github",
                "canonical_id": name,
                "status": "failed",
                "generated_at": timestamp,
                "metadata_path": metadata_paths.get(("github", name.lower())),
                "errors": [str(exc)],
            }
            core.write(root / "manifest.yaml", failure)
            return failure

        with (root / "evidence" / "files.jsonl").open("w", encoding="utf-8") as handle:
            for record in records:
                handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")

        candidates = [record for record in records if record["type"] == "blob" and priority(record)[0] < 9]
        candidates.sort(key=priority)
        candidates = candidates[: int(item.get("max_evidence_files", 24))]
        selected_paths = [record["path"] for record in candidates]
        try:
            fetched = fetch_selected(repository, commit, selected_paths)
        except Exception as exc:
            failure = {
                "manifest_version": 1,
                "source_type": "github",
                "canonical_id": name,
                "status": "failed",
                "generated_at": timestamp,
                "metadata_path": metadata_paths.get(("github", name.lower())),
                "source_revision": {"repository": name, "commit": commit},
                "errors": [f"selected-evidence-fetch: {exc}"],
            }
            core.write(root / "manifest.yaml", failure)
            return failure

        texts: dict[str, str] = {}
        excerpts = []
        max_lines = int(item.get("max_excerpt_lines", 500))
        for record in candidates:
            path = record["path"]
            raw = fetched.get(path)
            if raw is None:
                continue
            text = raw.decode("utf-8", errors="replace")
            texts[path] = text
            source_lines = text.splitlines()
            lines = source_lines[:max_lines]
            local = root / "evidence" / "excerpts" / f"{core.key(path)}-{record['blob_sha'][:8]}.txt"
            local.write_text("\n".join(lines) + "\n", encoding="utf-8")
            excerpts.append({
                "path": path,
                "blob_sha": record["blob_sha"],
                "blob_bytes": len(raw),
                "selector": f"repo://{name}@{commit}/{path}#L1-L{len(lines)}",
                "local_path": local.relative_to(core.ROOT).as_posix(),
                "truncated": len(lines) < len(source_lines),
                "content_sha256": core.sha(local.read_bytes()),
            })

        with (root / "evidence" / "excerpts.jsonl").open("w", encoding="utf-8") as handle:
            for excerpt in excerpts:
                handle.write(json.dumps(excerpt, ensure_ascii=False, sort_keys=True) + "\n")

        readme = next(
            (path for path in texts if PurePosixPath(path).name.lower().startswith("readme")),
            "",
        )
        readme_text = texts.get(readme, "")
        readme_lines = readme_text.splitlines()
        description = next(
            (
                re.sub(r"\s+", " ", line.strip())
                for line in readme_lines
                if line.strip() and not line.lstrip().startswith(("#", "<", "!", "[", "|", "---"))
            ),
            "Repository semantic capsule.",
        )
        top_paths = Counter(PurePosixPath(record["path"]).parts[0] for record in records)
        extensions = Counter(
            PurePosixPath(record["path"]).suffix.lower()
            for record in records
            if PurePosixPath(record["path"]).suffix
        )

        overview = core.front(
            name, commit, f"{name} — repository overview", "overview", "system", description, timestamp
        )
        overview += (
            f"# {name}\n\n{description}\n\n"
            f"- Frozen commit: `{commit}`\n"
            f"- Indexed paths: {len(records)}\n"
            f"- Evidence excerpts: {len(excerpts)}\n\n"
            "## README outline\n"
        )
        for line_number, line in enumerate(readme_lines, 1):
            if re.match(r"^#{1,6}\s+", line):
                overview += (
                    f"- {line.lstrip('# ')} — "
                    f"`repo://{name}@{commit}/{readme}#L{line_number}`\n"
                )
        (root / "wiki" / "overview.md").write_text(overview, encoding="utf-8")

        architecture = core.front(
            name, commit, f"{name} — architecture", "architecture", "system",
            f"Structural view of {name}.", timestamp,
        )
        architecture += "# Architecture\n\n## Top-level paths\n\n"
        architecture += "\n".join(f"- `{path}`: {count} paths" for path, count in top_paths.most_common(40))
        architecture += "\n\n## Extension profile\n\n"
        architecture += "\n".join(
            f"- `{extension or 'none'}`: {count}" for extension, count in extensions.most_common(30)
        )
        architecture += "\n\nDirectory structure is not proof of runtime behavior.\n"
        (root / "wiki" / "architecture.md").write_text(architecture, encoding="utf-8")

        operations = core.front(
            name, commit, f"{name} — interfaces and operations", "interfaces-and-operations", "method",
            f"Candidate operating surface of {name}.", timestamp,
        )
        operations += "# Interfaces and operations\n\n"
        inside_code = False
        for line_number, line in enumerate(readme_lines, 1):
            if line.strip().startswith("```"):
                inside_code = not inside_code
                continue
            if inside_code and line.strip() and len(line.strip()) < 220:
                operations += (
                    f"- `{line.strip()}` — "
                    f"`repo://{name}@{commit}/{readme}#L{line_number}`\n"
                )
        operations += "\nCommands are syntactically extracted and unverified.\n"
        (root / "wiki" / "interfaces-and-operations.md").write_text(operations, encoding="utf-8")

        index = core.front(
            name, commit, f"{name} — semantic capsule index", "index", "map",
            f"Navigation for {name}.", timestamp,
        )
        index += (
            "# Semantic capsule\n\n"
            "- [Overview](overview.md)\n"
            "- [Architecture](architecture.md)\n"
            "- [Interfaces and operations](interfaces-and-operations.md)\n\n"
            "## Evidence\n\n"
            "- `../evidence/files.jsonl`\n"
            "- `../evidence/excerpts.jsonl`\n"
        )
        (root / "wiki" / "index.md").write_text(index, encoding="utf-8")

        manifest = {
            "manifest_version": 1,
            "source_type": "github",
            "canonical_id": name,
            "status": "materialized",
            "generated_at": timestamp,
            "metadata_path": metadata_paths.get(("github", name.lower())),
            "source_revision": {
                "repository": name,
                "commit": commit,
                "clone_url": f"https://github.com/{name}.git",
            },
            "materialization": {
                "root": root.relative_to(core.ROOT).as_posix(),
                "indexed_paths": len(records),
                "selected_evidence_files": len(excerpts),
                "repo_contents_vendored": False,
                "tree_listing_requested_blob_sizes": False,
                "selected_blobs_fetched_as_single_archive": True,
            },
            "semanticization": {
                "backend": "deterministic-repo-capsule-v2",
                "state": "candidate",
                "llm_used": False,
                "wiki_pages": [
                    "wiki/index.md", "wiki/overview.md", "wiki/architecture.md",
                    "wiki/interfaces-and-operations.md",
                ],
                "limitations": [
                    "Selected evidence only",
                    "No runtime execution",
                    "No symbol or call graph in this seed pass",
                    "Requires semantic review",
                ],
            },
        }
        core.write(root / "manifest.yaml", manifest)
        return manifest

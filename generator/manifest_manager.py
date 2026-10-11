"""
Manifest Manager Module.

Handles tracking generated Python programs, calculating content hashes,
preventing duplicates, and cycling through topics systematically.
"""

from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Set

DEFAULT_CATEGORIES: List[str] = [
    "basics",
    "strings",
    "lists",
    "functions",
    "oop",
    "dsa",
    "utilities",
]


def normalize_code(code: str) -> str:
    """Normalize line endings and outer whitespace for consistent hashing."""
    return code.replace("\r\n", "\n").strip()


def calculate_content_hash(code: str) -> str:
    """
    Calculate a SHA-256 checksum of the normalized Python source code.
    Used to detect and prevent duplicate program submissions.
    """
    normalized = normalize_code(code)
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def load_manifest(manifest_path: str) -> Dict[str, Any]:
    """
    Load the manifest file from disk. If missing or corrupt, returns an empty schema.
    """
    empty_schema: Dict[str, Any] = {
        "last_updated": None,
        "total_programs": 0,
        "programs": [],
    }

    if not os.path.exists(manifest_path):
        return empty_schema

    try:
        with open(manifest_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if not isinstance(data, dict):
                return empty_schema
            data.setdefault("programs", [])
            data.setdefault("total_programs", len(data["programs"]))
            data.setdefault("last_updated", None)
            return data
    except (json.JSONDecodeError, OSError):
        return empty_schema


def save_manifest(manifest_path: str, manifest: Dict[str, Any]) -> None:
    """
    Persist the updated manifest dictionary to disk formatted with 2-space indentation.
    """
    os.makedirs(os.path.dirname(os.path.abspath(manifest_path)), exist_ok=True)
    with open(manifest_path, "w", encoding="utf-8") as file:
        json.dump(manifest, file, indent=2, ensure_ascii=False)
        file.write("\n")


def is_duplicate(
    manifest: Dict[str, Any],
    filename: str,
    content_hash: str,
    title: Optional[str] = None,
) -> bool:
    """
    Verify whether a program with the same hash, filename, or title already exists.
    """
    norm_filename = os.path.normpath(filename).replace("\\", "/")
    norm_title = title.strip().lower() if title else None

    for entry in manifest.get("programs", []):
        # 1. Exact content hash match
        if entry.get("content_hash") == content_hash:
            return True

        # 2. Filename collision
        existing_filename = os.path.normpath(entry.get("filename", "")).replace("\\", "/")
        if existing_filename == norm_filename:
            return True

        # 3. Exact title collision
        if norm_title and entry.get("title", "").strip().lower() == norm_title:
            return True

    return False


def get_completed_ids(manifest: Dict[str, Any]) -> Set[str]:
    """Return all unique template IDs or slugs already recorded."""
    ids: Set[str] = set()
    for entry in manifest.get("programs", []):
        if "id" in entry and entry["id"]:
            ids.add(entry["id"])
    return ids


def get_next_category(
    manifest: Dict[str, Any],
    categories: Optional[List[str]] = None,
) -> str:
    """
    Select the next category using a round-robin approach.
    Cycles through: basics -> strings -> lists -> functions -> oop -> dsa -> utilities.
    """
    active_categories = categories or DEFAULT_CATEGORIES
    programs = manifest.get("programs", [])

    if not programs:
        return active_categories[0]

    last_category = programs[-1].get("category")
    if last_category in active_categories:
        current_index = active_categories.index(last_category)
        next_index = (current_index + 1) % len(active_categories)
        return active_categories[next_index]

    return active_categories[0]


def has_run_today(manifest: Dict[str, Any], target_date: Optional[str] = None) -> bool:
    """
    Check if a program has already been generated today (UTC date YYYY-MM-DD).
    """
    if target_date is None:
        target_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    for entry in manifest.get("programs", []):
        gen_date = entry.get("generated_date", "")
        # Checks either 'YYYY-MM-DD' or ISO timestamp starting with date
        if gen_date.startswith(target_date):
            return True
    return False


def record_program(
    manifest: Dict[str, Any],
    program_id: str,
    category: str,
    filename: str,
    title: str,
    summary: str,
    content_hash: str,
    source: str = "template",
) -> Dict[str, Any]:
    """
    Record a newly generated program in the manifest and update metrics.
    """
    now = datetime.now(timezone.utc)
    entry = {
        "id": program_id,
        "category": category,
        "filename": os.path.normpath(filename).replace("\\", "/"),
        "title": title,
        "summary": summary,
        "content_hash": content_hash,
        "source": source,
        "generated_date": now.strftime("%Y-%m-%d"),
        "timestamp": now.isoformat(),
    }

    manifest.setdefault("programs", []).append(entry)
    manifest["total_programs"] = len(manifest["programs"])
    manifest["last_updated"] = now.isoformat()

    return entry

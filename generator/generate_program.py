"""
Daily Python Program Generator - Main Entrypoint.

Orchestrates automated daily program generation, duplicate prevention,
syntax verification, file writes, and manifest tracking.

Usage:
    python generator/generate_program.py
    python generator/generate_program.py --category dsa
    python generator/generate_program.py --force
    python generator/generate_program.py --dry-run
"""

from __future__ import annotations

import argparse
import ast
import os
import sys
from typing import Any, Dict, List, Optional

# Ensure repository root is on sys.path
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from generator.ai_generator import generate_ai_program
from generator.fallback_templates import (
    TEMPLATES,
    get_templates_by_category,
)
from generator.manifest_manager import (
    DEFAULT_CATEGORIES,
    calculate_content_hash,
    get_completed_ids,
    get_next_category,
    has_run_today,
    is_duplicate,
    load_manifest,
    record_program,
    save_manifest,
)

MANIFEST_PATH = os.path.join(REPO_ROOT, "manifest.json")
PROGRAMS_DIR = os.path.join(REPO_ROOT, "programs")


def is_safe_path(base_dir: str, target_path: str) -> bool:
    """
    Prevent directory traversal attacks by ensuring target_path resolves strictly inside base_dir.
    """
    resolved_base = os.path.abspath(base_dir)
    resolved_target = os.path.abspath(target_path)
    return (
        os.path.commonpath([resolved_base, resolved_target]) == resolved_base
        and resolved_base != resolved_target
    )


def select_template_program(
    category: str,
    completed_ids: set[str],
) -> Optional[Dict[str, Any]]:
    """
    Find the next uncompleted template for the chosen category.
    If all in category are completed, cycle back or pick from any available uncompleted template.
    """
    category_templates = get_templates_by_category(category)

    # 1. Uncompleted in target category
    for tmpl in category_templates:
        if tmpl["id"] not in completed_ids:
            return tmpl

    # 2. Any uncompleted template across all categories
    for tmpl in TEMPLATES:
        if tmpl["id"] not in completed_ids:
            return tmpl

    # 3. If everything has been used (after 70+ days), return the first template with modified ID
    if category_templates:
        base = category_templates[0].copy()
        base["id"] = f"{base['id']}_cycle_{len(completed_ids)}"
        base["filename"] = f"cycle_{base['filename']}"
        return base

    return None


def run_generator(
    category_arg: str = "auto",
    source_preference: str = "auto",
    force: bool = False,
    dry_run: bool = False,
) -> int:
    """
    Execute generation cycle. Returns exit code (0 for success, 1 for failure).
    """
    print("=" * 60)
    print(" [*] DAILY PYTHON CODE GENERATOR")
    print("=" * 60)

    # 1. Load Manifest
    manifest = load_manifest(MANIFEST_PATH)
    total_existing = manifest.get("total_programs", 0)
    print(f"[Manifest] Loaded {total_existing} previously recorded programs.")

    # 2. Check if already executed today
    if not force and has_run_today(manifest):
        print("[Info] A program has already been generated today (UTC).")
        print("       Use '--force' if you wish to generate another program today.")
        print("       Exiting cleanly without changes.")
        return 0

    # 3. Determine Category
    if category_arg == "auto" or category_arg not in DEFAULT_CATEGORIES:
        category = get_next_category(manifest, DEFAULT_CATEGORIES)
        print(f"[Category Selection] Auto-selected round-robin category: '{category}'")
    else:
        category = category_arg
        print(f"[Category Selection] User-specified category: '{category}'")

    completed_ids = get_completed_ids(manifest)
    recent_titles = [p.get("title", "") for p in manifest.get("programs", [])]

    candidate_program: Optional[Dict[str, Any]] = None

    # 4. Attempt AI Generation if enabled/requested
    if source_preference in ("auto", "ai"):
        print(f"[AI Generator] Checking for API keys and attempting generation for '{category}'...")
        ai_result = generate_ai_program(category, recent_titles)
        if ai_result:
            code_hash = calculate_content_hash(ai_result["code"])
            rel_file = os.path.join("programs", category, ai_result["filename"]).replace("\\", "/")
            if not is_duplicate(manifest, rel_file, code_hash, ai_result["title"]):
                candidate_program = ai_result
                print(f"[AI Generator] Successfully generated: '{ai_result['title']}' via {ai_result.get('source', 'AI')}")
            else:
                print("[AI Generator] AI program was a duplicate of previous content. Falling back.")
        else:
            print("[AI Generator] AI generation skipped or unavailable. Using curated fallback.")

    # 5. Use Fallback Template if AI was not used
    if not candidate_program:
        print(f"[Fallback Template] Selecting next available template for category '{category}'...")
        tmpl = select_template_program(category, completed_ids)
        if not tmpl:
            print("[Error] No templates available for generation.")
            return 1
        candidate_program = tmpl.copy()
        candidate_program["source"] = "curated-template"
        print(f"[Fallback Template] Selected: '{tmpl['title']}' (ID: {tmpl['id']})")

    # 6. Syntax Validation
    code = candidate_program["code"]
    try:
        ast.parse(code)
    except SyntaxError as err:
        print(f"[Fatal Error] Generated code failed syntax validation: {err}")
        return 1

    # 7. File Path Resolution and Traversal Protection
    filename = candidate_program["filename"]
    cat_dir = os.path.join(PROGRAMS_DIR, candidate_program["category"])
    target_filepath = os.path.join(cat_dir, filename)

    if not is_safe_path(PROGRAMS_DIR, target_filepath):
        print(f"[Security Error] Refusing to write to unsafe path: {target_filepath}")
        return 1

    # If filename already exists on disk, add suffix to avoid overwriting existing lessons
    if os.path.exists(target_filepath):
        name_part, ext = os.path.splitext(filename)
        counter = 2
        while os.path.exists(os.path.join(cat_dir, f"{name_part}_v{counter}{ext}")):
            counter += 1
        filename = f"{name_part}_v{counter}{ext}"
        target_filepath = os.path.join(cat_dir, filename)
        candidate_program["filename"] = filename

    # 8. Content Hash and Duplicate Verification
    content_hash = calculate_content_hash(code)
    rel_path = os.path.relpath(target_filepath, REPO_ROOT).replace("\\", "/")

    if is_duplicate(manifest, rel_path, content_hash, candidate_program.get("title")):
        print(f"[Warning] Duplicate detected for '{rel_path}'. Program already recorded.")
        if not force:
            return 0

    # 9. Output Plan or Write to Disk
    line_count = len(code.splitlines())

    if dry_run:
        print("\n[Dry Run] Validated successfully without writing to disk:")
        print(f" - Path   : {rel_path}")
        print(f" - Title  : {candidate_program['title']}")
        print(f" - SHA-256: {content_hash}")
        print(f" - Lines  : {line_count}")
        return 0

    # Write source file
    os.makedirs(os.path.dirname(target_filepath), exist_ok=True)
    with open(target_filepath, "w", encoding="utf-8") as f:
        f.write(code)

    # Record in manifest
    record_program(
        manifest=manifest,
        program_id=candidate_program["id"],
        category=candidate_program["category"],
        filename=rel_path,
        title=candidate_program["title"],
        summary=candidate_program.get("summary", ""),
        content_hash=content_hash,
        source=candidate_program.get("source", "template"),
    )
    save_manifest(MANIFEST_PATH, manifest)

    print("\n" + "=" * 60)
    print(" [SUCCESS] PROGRAM GENERATED SUCCESSFULLY")
    print("=" * 60)
    print(f" Target File  : {rel_path}")
    print(f" Title        : {candidate_program['title']}")
    print(f" Category     : {candidate_program['category']}")
    print(f" Source       : {candidate_program.get('source')}")
    print(f" Line Count   : {line_count} lines")
    print(f" SHA-256      : {content_hash[:16]}...")
    print(f" Total Tracked: {manifest['total_programs']} programs")
    print("=" * 60)

    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Automated Daily Python Practice Program Generator"
    )
    parser.add_argument(
        "--category",
        choices=["auto", "basics", "strings", "lists", "functions", "oop", "dsa", "utilities"],
        default="auto",
        help="Target category for the program (default: auto round-robin)",
    )
    parser.add_argument(
        "--source",
        choices=["auto", "ai", "template"],
        default="auto",
        help="Generation source strategy (default: auto)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force generation even if a program was already added today",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Test generation and validation without saving files or updating manifest",
    )

    args = parser.parse_args()
    exit_code = run_generator(
        category_arg=args.category,
        source_preference=args.source,
        force=args.force,
        dry_run=args.dry_run,
    )
    sys.exit(exit_code)


if __name__ == "__main__":
    main()

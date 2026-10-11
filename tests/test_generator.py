"""
Unit and Integration Tests for Daily Python Code Generator.

Compatible with both standard library 'unittest' (zero extra installations)
and 'pytest' for GitHub Actions automation.

Covers:
- Template syntax and structure verification
- Manifest loading, hashing, and duplicate checking
- Path traversal and security protections
- Dry-run execution
"""

import ast
import os
import tempfile
import unittest

from generator.ai_generator import check_ast_safety, sanitize_filename
from generator.fallback_templates import TEMPLATES
from generator.generate_program import is_safe_path, run_generator
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


class TestFallbackTemplates(unittest.TestCase):
    """Validate all built-in offline program templates."""

    def test_templates_count_and_diversity(self):
        """Ensure we provide a comprehensive catalog of at least 70 templates."""
        self.assertGreaterEqual(
            len(TEMPLATES), 70, f"Expected at least 70 templates, found {len(TEMPLATES)}"
        )

    def test_templates_unique_ids(self):
        """Ensure all template IDs are distinct."""
        ids = [t["id"] for t in TEMPLATES]
        self.assertEqual(len(ids), len(set(ids)), "Found duplicate template IDs!")

    def test_templates_have_valid_categories(self):
        """Ensure all templates map to known categories."""
        expected_cats = set(DEFAULT_CATEGORIES)
        for t in TEMPLATES:
            self.assertIn(
                t["category"],
                expected_cats,
                f"Invalid category {t['category']} in template {t['id']}",
            )

    def test_all_templates_syntax_valid(self):
        """Ensure all template source code passes AST parsing without SyntaxErrors."""
        for t in TEMPLATES:
            code = t["code"]
            try:
                tree = ast.parse(code)
                self.assertIsNotNone(tree)
            except SyntaxError as e:
                self.fail(f"Template '{t['id']}' has syntax error: {e}")

    def test_templates_metadata_complete(self):
        """Ensure every template has title, filename, summary, and code."""
        for t in TEMPLATES:
            self.assertTrue(t["title"].strip(), f"Template {t['id']} missing title")
            self.assertTrue(t["filename"].endswith(".py"), f"Template {t['id']} invalid filename")
            self.assertTrue(t["summary"].strip(), f"Template {t['id']} missing summary")
            has_definition = "def " in t["code"] or "class " in t["code"]
            self.assertTrue(has_definition, f"Template {t['id']} missing function or class")


class TestManifestManager(unittest.TestCase):
    """Test manifest persistence, hash tracking, and duplicate prevention."""

    def test_load_nonexistent_manifest(self):
        """Loading a non-existent file returns default schema."""
        data = load_manifest("non_existent_manifest_file.json")
        self.assertEqual(data["total_programs"], 0)
        self.assertEqual(data["programs"], [])

    def test_save_and_load_manifest(self):
        """Verify save and reload cycle preserves data."""
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
            tmp_path = tmp.name

        try:
            initial = {"last_updated": None, "total_programs": 0, "programs": []}
            record_program(
                manifest=initial,
                program_id="test_01",
                category="basics",
                filename="programs/basics/test.py",
                title="Test Program",
                summary="A test program",
                content_hash="abc123hash",
                source="test",
            )
            save_manifest(tmp_path, initial)
            reloaded = load_manifest(tmp_path)

            self.assertEqual(reloaded["total_programs"], 1)
            self.assertEqual(reloaded["programs"][0]["id"], "test_01")
            self.assertEqual(reloaded["programs"][0]["content_hash"], "abc123hash")
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_content_hash_consistency(self):
        """Verify content hash is deterministic and ignores CRLF differences."""
        code_crlf = "print('hello')\r\n"
        code_lf = "print('hello')\n"
        self.assertEqual(calculate_content_hash(code_crlf), calculate_content_hash(code_lf))

    def test_duplicate_detection(self):
        """Ensure is_duplicate flags matching hashes, filenames, and titles."""
        manifest = {
            "programs": [
                {
                    "id": "p1",
                    "filename": "programs/basics/hello.py",
                    "content_hash": "hash_xyz",
                    "title": "Hello World",
                }
            ]
        }
        # Hash match
        self.assertTrue(
            is_duplicate(manifest, "programs/basics/other.py", "hash_xyz", "Different Title")
        )
        # Filename match
        self.assertTrue(
            is_duplicate(manifest, "programs/basics/hello.py", "different_hash", "Different Title")
        )
        # Title match (case-insensitive)
        self.assertTrue(
            is_duplicate(manifest, "programs/basics/different.py", "different_hash", "hello world")
        )
        # Clean new item
        self.assertFalse(
            is_duplicate(manifest, "programs/basics/clean.py", "unique_hash", "Brand New Title")
        )

    def test_round_robin_category_progression(self):
        """Verify category cycles across DEFAULT_CATEGORIES."""
        cats = ["basics", "strings", "lists", "functions", "oop", "dsa", "utilities"]
        manifest = {"programs": []}

        # First when empty
        self.assertEqual(get_next_category(manifest, cats), "basics")

        # After basics -> strings
        manifest["programs"].append({"category": "basics"})
        self.assertEqual(get_next_category(manifest, cats), "strings")

        # After utilities -> cycles back to basics
        manifest["programs"].append({"category": "utilities"})
        self.assertEqual(get_next_category(manifest, cats), "basics")


class TestSecurityAndSafety(unittest.TestCase):
    """Test AST security inspection and file path traversal guards."""

    def test_path_safety_within_base(self):
        """Ensure paths strictly inside base_dir are deemed safe."""
        base = os.path.abspath("programs")
        safe_target = os.path.join(base, "basics", "prime.py")
        self.assertTrue(is_safe_path(base, safe_target))

    def test_path_safety_traversal_rejection(self):
        """Ensure directory traversal attempts are rejected."""
        base = os.path.abspath("programs")
        malicious_target = os.path.abspath(os.path.join(base, "..", "secret.py"))
        self.assertFalse(is_safe_path(base, malicious_target))

    def test_ast_safety_allows_clean_code(self):
        """Safe code with math, typing, and standard loops must pass."""
        safe_code = """
import math
def compute(x: int) -> float:
    return math.sqrt(x)
"""
        self.assertTrue(check_ast_safety(safe_code))

    def test_ast_safety_rejects_eval_and_system(self):
        """Dangerous calls like eval() and os.system() must be rejected."""
        self.assertFalse(check_ast_safety("eval('2 + 2')"))
        self.assertFalse(check_ast_safety("import os\nos.system('dir')"))
        self.assertFalse(check_ast_safety("exec('print(1)')"))

    def test_sanitize_filename(self):
        """Ensure arbitrary strings become safe filenames."""
        clean = sanitize_filename("Prime Number Checker & Sieve (2026)!")
        self.assertEqual(clean, "prime_number_checker_sieve_2026.py")


class TestGeneratorDryRun(unittest.TestCase):
    """Verify end-to-end generator execution in dry-run mode."""

    def test_dry_run_auto(self):
        exit_code = run_generator(category_arg="auto", force=True, dry_run=True)
        self.assertEqual(exit_code, 0)

    def test_dry_run_specific_categories(self):
        for cat in ["basics", "strings", "lists", "functions", "oop", "dsa", "utilities"]:
            exit_code = run_generator(category_arg=cat, force=True, dry_run=True)
            self.assertEqual(exit_code, 0)


if __name__ == "__main__":
    unittest.main()

"""
AI Program Generator Module.

Optionally leverages Google Gemini API (or OpenAI API) to generate fresh, unique
daily Python practice programs. If no API key is present or if the network request fails,
it returns None so the caller seamlessly falls back to the curated template library.

Safety & Security:
- Validates the returned source code with ast.parse() before saving.
- Disallows execution and inspects AST for dangerous operations (e.g., eval, subprocess).
"""

from __future__ import annotations

import ast
import json
import os
import re
from typing import Any, Dict, List, Optional
import urllib.request
import urllib.error


FORBIDDEN_CALLS = {
    "eval",
    "exec",
    "os.system",
    "subprocess.Popen",
    "subprocess.run",
    "subprocess.call",
    "shutil.rmtree",
}


def sanitize_filename(name: str) -> str:
    """Convert arbitrary title into safe snake_case filename with .py extension."""
    name = re.sub(r"[^\w\s-]", "", name).strip().lower()
    slug = re.sub(r"[-\s]+", "_", name)
    if not slug.endswith(".py"):
        slug += ".py"
    return slug


def check_ast_safety(source_code: str) -> bool:
    """
    Parse source code AST and reject any programs containing dangerous system calls.
    Does NOT execute the code.
    """
    try:
        tree = ast.parse(source_code)
    except SyntaxError:
        return False

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            # Check direct function calls like eval(...) or exec(...)
            if isinstance(node.func, ast.Name) and node.func.id in FORBIDDEN_CALLS:
                return False
            # Check module calls like os.system(...)
            if isinstance(node.func, ast.Attribute):
                attr_name = node.func.attr
                if isinstance(node.func.value, ast.Name):
                    full_name = f"{node.func.value.id}.{attr_name}"
                    if full_name in FORBIDDEN_CALLS:
                        return False
    return True


def extract_python_code(raw_text: str) -> str:
    """Extract clean Python code from markdown code fences or raw string."""
    # Match ```python ... ``` or ``` ... ```
    pattern = r"```(?:python)?\s*([\s\S]*?)\s*```"
    matches = re.findall(pattern, raw_text, re.IGNORECASE)
    if matches:
        return matches[0].strip()
    return raw_text.strip()


def extract_metadata_from_code(code: str, fallback_category: str) -> tuple[str, str, str]:
    """
    Extract a descriptive title, summary, and filename from docstring or comments.
    """
    lines = code.splitlines()
    title = ""
    summary = ""

    # Look for title in docstring
    try:
        parsed = ast.parse(code)
        doc = ast.get_docstring(parsed)
        if doc:
            doc_lines = [l.strip() for l in doc.splitlines() if l.strip()]
            if doc_lines:
                title = doc_lines[0].rstrip(".")
            if len(doc_lines) > 1:
                summary = doc_lines[1]
    except Exception:
        pass

    if not title:
        # Fallback to first comment or header
        for line in lines:
            if line.startswith("#"):
                clean = line.lstrip("#").strip()
                if clean:
                    title = clean
                    break

    if not title:
        title = f"Daily {fallback_category.title()} Program"

    if not summary:
        summary = f"Practical Python program covering {fallback_category} concepts."

    filename = sanitize_filename(title)
    return title, summary, filename


def generate_with_gemini(
    api_key: str,
    category: str,
    recent_titles: List[str],
) -> Optional[str]:
    """
    Call Google Gemini REST API to generate a Python practice program.
    Uses urllib.request (zero extra dependencies).
    """
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

    recent_notice = ""
    if recent_titles:
        titles_preview = ", ".join(f'"{t}"' for t in recent_titles[-10:])
        recent_notice = f"Do NOT generate any program similar to these recently generated programs: {titles_preview}."

    prompt = f"""
You are an expert Python educator. Generate a complete, beginner-friendly, high-quality Python program for practice.

Topic Category: {category}
{recent_notice}

Requirements:
1. Write 100% syntactically valid Python 3 code.
2. Include a descriptive module docstring at the very top explaining:
   - What the program does
   - Key concepts learned
   - Sample input and expected output
3. Include clean, educational inline comments explaining each step.
4. Include an `if __name__ == "__main__":` block demonstrating the code with realistic sample data.
5. Do NOT use external packages outside the Python standard library (e.g. math, random, collections, json, csv, datetime, re, etc.).
6. NEVER use dangerous functions like eval(), exec(), os.system(), or subprocess.
7. Return ONLY the code inside ```python and ``` code fence. No explanations before or after.
"""

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 2048,
        },
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=25) as response:
            if response.status == 200:
                data = json.loads(response.read().decode("utf-8"))
                candidates = data.get("candidates", [])
                if candidates:
                    parts = candidates[0].get("content", {}).get("parts", [])
                    if parts:
                        return parts[0].get("text", "")
    except (urllib.error.URLError, urllib.error.HTTPError, OSError) as err:
        print(f"[AI Generator Warning] Gemini API call failed: {err}")
        return None

    return None


def generate_with_openai(
    api_key: str,
    category: str,
    recent_titles: List[str],
) -> Optional[str]:
    """
    Call OpenAI Chat Completion API to generate a Python practice program.
    """
    url = "https://api.openai.com/v1/chat/completions"

    recent_notice = ""
    if recent_titles:
        titles_preview = ", ".join(f'"{t}"' for t in recent_titles[-10:])
        recent_notice = f"Do NOT duplicate these recently created programs: {titles_preview}."

    prompt = f"""
Generate a beginner-friendly, educational Python practice program for category: {category}.
{recent_notice}
Include a module docstring, sample input/output, comments, and an `if __name__ == '__main__':` block.
Use only the Python standard library. Return ONLY code inside ```python ```.
"""

    payload = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=25) as response:
            if response.status == 200:
                data = json.loads(response.read().decode("utf-8"))
                choices = data.get("choices", [])
                if choices:
                    return choices[0].get("message", {}).get("content", "")
    except (urllib.error.URLError, urllib.error.HTTPError, OSError) as err:
        print(f"[AI Generator Warning] OpenAI API call failed: {err}")
        return None

    return None


def generate_ai_program(
    category: str,
    recent_titles: Optional[List[str]] = None,
) -> Optional[Dict[str, Any]]:
    """
    Attempt to generate a fresh Python program using configured AI providers.
    Returns a dictionary with program details, or None if unavailable/invalid.
    """
    gemini_key = os.getenv("GEMINI_API_KEY", "").strip()
    openai_key = os.getenv("OPENAI_API_KEY", "").strip()

    raw_response: Optional[str] = None
    provider_used = ""

    if gemini_key:
        provider_used = "gemini"
        raw_response = generate_with_gemini(gemini_key, category, recent_titles or [])
    elif openai_key:
        provider_used = "openai"
        raw_response = generate_with_openai(openai_key, category, recent_titles or [])
    else:
        # No API key present in environment
        return None

    if not raw_response:
        return None

    code = extract_python_code(raw_response)
    if not code:
        return None

    # Strict syntax validation
    try:
        ast.parse(code)
    except SyntaxError as err:
        print(f"[AI Generator Warning] Generated code had syntax error: {err}")
        return None

    # Safety validation
    if not check_ast_safety(code):
        print("[AI Generator Warning] Generated code rejected by safety filter.")
        return None

    title, summary, filename = extract_metadata_from_code(code, category)
    slug = f"ai_{category}_{filename.replace('.py', '')}"

    return {
        "id": slug,
        "category": category,
        "filename": filename,
        "title": title,
        "summary": summary,
        "code": code,
        "source": f"ai-{provider_used}",
    }

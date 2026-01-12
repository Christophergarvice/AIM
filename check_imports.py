"""
check_imports.py
----------------
This script scans your project for Python files and tests if they can be imported correctly.
Useful after renaming folders, files, or changing imports.
"""

import importlib
import os
import sys
from pathlib import Path

# Add the repo root to Python’s import path
sys.path.insert(0, str(Path(__file__).resolve().parent))

def scan_and_import(base_dir):
    base_path = Path(base_dir)
    errors = []

    print(f"🔍 Scanning Python files in: {base_path.resolve()}\n")

    for py_file in base_path.rglob("*.py"):
        # Skip __init__.py files
        if py_file.name == "__init__.py":
            continue

        # Convert path to importable module name (e.g., app.flask_app)
        relative = py_file.relative_to(base_path)
        module_name = ".".join(relative.with_suffix("").parts)

        try:
            importlib.import_module(module_name)
            print(f"✅  Imported successfully: {module_name}")
        except Exception as e:
            print(f"❌  Failed to import: {module_name}")
            print(f"   ↳ {type(e).__name__}: {e}")
            errors.append((module_name, str(e)))

    print("\n📋 Import check complete.")
    if errors:
        print(f"⚠️  {len(errors)} file(s) had import issues.")
    else:
        print("🎉 All imports are working correctly!")

if __name__ == "__main__":
    scan_and_import(".")

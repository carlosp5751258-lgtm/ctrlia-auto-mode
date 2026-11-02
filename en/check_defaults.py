#!/usr/bin/env python3
"""Warns if an autoMode block replaces the built-in rules because "$defaults" was left out.

Usage: python3 check_defaults.py [path/settings.json]   (default ~/.claude/settings.json)
Exits with 1 if any autoMode list lacks "$defaults". Read-only.
"""
import json
import os
import sys

LISTS = ("environment", "allow", "soft_deny", "hard_deny")


def problems(settings):
    """List of warnings for an already loaded settings.json."""
    auto = settings.get("autoMode") or {}
    return [f'autoMode.{k} does not include "$defaults": it replaces the WHOLE built-in list'
            for k in LISTS if isinstance(auto.get(k), list) and "$defaults" not in auto[k]]


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/.claude/settings.json")
    try:
        with open(path, encoding="utf-8") as f:
            settings = json.load(f)
    except FileNotFoundError:
        print(f"{path} does not exist: no autoMode to check.")
        return 0
    except json.JSONDecodeError as err:
        print(f"{path} is not valid JSON: {err}", file=sys.stderr)
        return 2
    warnings = problems(settings)
    for w in warnings:
        print(f"WARNING: {w}")
    if not warnings:
        print(f'OK: {path} does not replace any built-in list (or has no autoMode).')
    # The classifier ignores autoMode in project settings
    if "autoMode" in settings and os.path.normpath(path).replace("\\", "/").endswith((".claude/settings.json", ".claude/settings.local.json")) \
            and os.path.dirname(os.path.abspath(path)) != os.path.expanduser("~/.claude"):
        print("WARNING: autoMode in a project's settings is ignored; put it in ~/.claude/settings.json.")
    return 1 if warnings else 0


if __name__ == "__main__":
    sys.exit(main())

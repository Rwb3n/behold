#!/usr/bin/env python3
"""Behold PreToolUse hook — inject golden suite assertions before governance edits."""
import json
import os
import sys
from pathlib import Path

def find_behold_dir():
    """Walk up from CWD to find .behold/ directory."""
    cwd = Path.cwd()
    for parent in [cwd, *cwd.parents]:
        behold = parent / ".behold"
        if behold.is_dir():
            return behold
    return None

def main():
    hook_input = json.loads(sys.stdin.read()) if not sys.stdin.isatty() else {}
    tool_input = hook_input.get("tool_input", {})
    file_path = tool_input.get("file_path", "")

    behold = find_behold_dir()
    if not behold:
        return

    governance_paths = ["principles.md", "methods.md", "ceremonies/", ".behold/"]
    is_governance_edit = any(seg in file_path for seg in governance_paths)

    if not is_governance_edit:
        return

    golden_file = behold / "golden-suite.jsonl"
    if not golden_file.exists():
        return

    assertions = []
    for line in golden_file.read_text().splitlines():
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
            assertions.append(entry.get("assertion", ""))
        except json.JSONDecodeError:
            continue

    if not assertions:
        return

    msg = "⚠ GOVERNANCE EDIT — Check golden suite assertions:\n"
    for i, a in enumerate(assertions[:10], 1):
        msg += f"  {i}. {a}\n"
    msg += "\nDoes this edit conflict with any assertion above? If so, surface the tension."

    print(msg, file=sys.stderr)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Behold session start hook — count sessions, surface governance context."""
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
    behold = find_behold_dir()
    if not behold:
        return

    counter_file = behold / "session-count"
    count = 0
    if counter_file.exists():
        try:
            count = int(counter_file.read_text().strip())
        except ValueError:
            count = 0
    count += 1
    counter_file.write_text(str(count))

    golden_file = behold / "golden-suite.jsonl"
    golden_count = 0
    if golden_file.exists():
        golden_count = sum(1 for line in golden_file.read_text().splitlines() if line.strip())

    parts = [f"Session {count}"]
    if golden_count:
        parts.append(f"Golden suite: {golden_count} assertions")

    principles = behold / "principles.md"
    if not principles.exists():
        parts.append("⚠ No principles.md — run /behold:init to scaffold")

    print(json.dumps({"behold": " | ".join(parts)}))

if __name__ == "__main__":
    main()

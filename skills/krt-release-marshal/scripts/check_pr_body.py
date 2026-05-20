#!/usr/bin/env python3
"""Validate KRT PR body shape."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


FORBIDDEN = (
    "stacked",
    "stackeada",
    "stack",
    "retarget",
    "retargetear",
    "temporary base",
    "base temporal",
    "depends on",
    "dependency pr",
    "merge sequencing",
    "reviewer",
    "verification",
    "tests pass",
    "ci",
)


def read_body(args: argparse.Namespace) -> str:
    if args.file:
        return Path(args.file).read_text(encoding="utf-8")
    return args.body or sys.stdin.read()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    parser.add_argument("body", nargs="?")
    args = parser.parse_args()

    body = read_body(args).strip()
    errors: list[str] = []

    if not body:
        errors.append("PR body is empty")

    lowered = body.lower()
    for term in FORBIDDEN:
        if term in lowered:
            errors.append(f"PR body contains forbidden operational context: {term!r}")

    lines = [line.rstrip() for line in body.splitlines()]
    jira_lines = [line for line in lines if re.fullmatch(r"https?://\S+/browse/[A-Z][A-Z0-9]+-\d+", line)]
    if jira_lines:
        if lines[-1] != jira_lines[-1]:
            errors.append("Jira URL must be the last line")
        jira_index = lines.index(jira_lines[-1])
        if jira_index > 0 and lines[jira_index - 1] != "":
            errors.append("Jira URL must be separated from change sentences by a blank line")
    elif any("/browse/" in line for line in lines):
        errors.append("Jira link does not match expected /browse/KEY-N format")

    for line in lines:
        if line.startswith("#") or line.startswith("##"):
            errors.append("PR body must not include headings")
        if line.startswith("- "):
            errors.append("Use one factual sentence per line, not markdown bullets")

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    if errors:
        return 1
    print("PR body checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate Compound Master work-package review-unit guardrails."""

from __future__ import annotations

import re
import sys
from pathlib import Path


DOC_SECTIONS = (
    "docs/brainstorms",
    "docs/plans",
    "docs/work-packages",
    "docs/orchestration/compound-master-state.md",
)


def section(text: str, heading: str) -> str:
    pattern = re.compile(rf"^## {re.escape(heading)}\n(.*?)(?=^## |\Z)", re.M | re.S)
    match = pattern.search(text)
    return match.group(1).strip() if match else ""


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_work_package.py <work-package.md>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []

    if "review_units:" not in text:
        errors.append("frontmatter must include review_units: [RU1, ...]")

    review_units = section(text, "Review Units")
    if not review_units:
        errors.append("missing ## Review Units section")
    elif not re.search(r"\|\s*RU\d+\s*\|", review_units):
        errors.append("## Review Units must include table rows named RU1, RU2, ...")

    handoff = section(text, "Branch and PR Handoff Inputs")
    if not handoff:
        errors.append("missing ## Branch and PR Handoff Inputs section")
    else:
        if "Review unit:" not in handoff:
            errors.append("handoff inputs must name the selected Review unit")
        if "PR body bullets" in handoff:
            errors.append("use PR body sentences, not PR body bullets")

    files_tests = section(text, "Files and Tests")
    mixed_docs = [p for p in DOC_SECTIONS if p in text]
    runtime_hint = bool(re.search(r"\b(src|app|web-application|backend|frontend|lib)/", files_tests))
    if mixed_docs and runtime_hint:
        warnings.append(
            "package appears to mix orchestration docs with runtime files; "
            "ensure this is split into review units or explicitly justified"
        )

    generated_hint = re.search(r"(\.auto\.|generated|bindings|definitions\.ts)", text, re.I)
    if generated_hint and "generated" not in review_units.lower():
        warnings.append("generated/mechanical artifacts detected; Review Units should isolate or justify them")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    if errors:
        return 1
    print("work package review-unit checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

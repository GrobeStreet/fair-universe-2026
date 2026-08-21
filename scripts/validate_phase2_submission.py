#!/usr/bin/env python3
"""Validate FAIR Universe Phase 2 submission packaging.

Expected artifact: a .zip containing result.json with a top-level
`ood_scores` list of exactly 10,000 finite numeric values.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import zipfile
from pathlib import Path

EXPECTED_COUNT = 10_000
EXPECTED_NAME = "result.json"


def fail(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


def validate(path: Path) -> int:
    if not path.is_file():
        return fail(f"file not found: {path}")
    if path.suffix.lower() != ".zip":
        return fail("submission artifact must be a .zip file")

    try:
        with zipfile.ZipFile(path) as zf:
            names = [name for name in zf.namelist() if not name.endswith("/")]
            if names != [EXPECTED_NAME]:
                return fail(
                    f"zip must contain exactly {EXPECTED_NAME}; found {names!r}"
                )
            payload = json.loads(zf.read(EXPECTED_NAME))
    except zipfile.BadZipFile:
        return fail("artifact is not a valid zip archive")
    except json.JSONDecodeError as exc:
        return fail(f"result.json is not valid JSON: {exc}")

    if not isinstance(payload, dict):
        return fail("result.json must contain a JSON object")
    if set(payload) != {"ood_scores"}:
        return fail(
            "result.json must contain exactly one top-level key: 'ood_scores'"
        )

    scores = payload["ood_scores"]
    if not isinstance(scores, list):
        return fail("ood_scores must be a JSON list")
    if len(scores) != EXPECTED_COUNT:
        return fail(
            f"ood_scores must contain {EXPECTED_COUNT} values; found {len(scores)}"
        )

    for index, value in enumerate(scores):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            return fail(f"ood_scores[{index}] is not numeric: {value!r}")
        if not math.isfinite(float(value)):
            return fail(f"ood_scores[{index}] is not finite: {value!r}")

    print(
        f"PASS: {path} contains {EXPECTED_COUNT} finite OoD scores in {EXPECTED_NAME}"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("submission_zip", type=Path)
    args = parser.parse_args()
    return validate(args.submission_zip)


if __name__ == "__main__":
    raise SystemExit(main())

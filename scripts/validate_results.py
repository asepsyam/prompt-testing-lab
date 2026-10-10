#!/usr/bin/env python3
"""Validate manually recorded prompt evaluation scores. Uses only Python's standard library."""
import argparse
import csv
import sys
from pathlib import Path

SCORE_COLUMNS = [
    "instruction_adherence",
    "factual_grounding",
    "language_localization",
    "format_compliance",
    "safety_redirection",
]
REQUIRED_COLUMNS = [
    "case_id", "prompt_version", "model", "run_date",
    *SCORE_COLUMNS, "notes", "output_reference",
]

def main():
    parser = argparse.ArgumentParser(
        description="Check the structure and score ranges in a prompt-testing results CSV."
    )
    parser.add_argument("--input", default="results/results_template.csv",
                        help="Path to results CSV (default: results/results_template.csv)")
    args = parser.parse_args()
    path = Path(args.input)

    if not path.exists():
        print(f"ERROR: File not found: {path}", file=sys.stderr)
        return 2

    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        missing = [column for column in REQUIRED_COLUMNS if column not in headers]
        if missing:
            print("ERROR: Missing required columns: " + ", ".join(missing))
            return 2
        rows = list(reader)

    if not rows:
        print("No completed evaluation rows yet. Add scored outputs to begin analysis.")
        return 0

    errors = []
    for index, row in enumerate(rows, start=2):
        if not row.get("case_id", "").strip():
            errors.append(f"Row {index}: case_id is empty")
        if not row.get("prompt_version", "").strip():
            errors.append(f"Row {index}: prompt_version is empty")
        for column in SCORE_COLUMNS:
            raw = (row.get(column) or "").strip()
            # Use N/A only when a dimension genuinely does not apply.
            if raw.upper() == "N/A":
                continue
            try:
                score = int(raw)
                if score not in (0, 1, 2):
                    errors.append(f"Row {index}: {column} must be 0, 1, 2, or N/A")
            except ValueError:
                errors.append(f"Row {index}: {column} must be 0, 1, 2, or N/A")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validation passed: {len(rows)} evaluation rows.")
    print("Reminder: this validates the recording format, not the quality of the judgments.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

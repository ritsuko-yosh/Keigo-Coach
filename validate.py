"""
validate.py - Data quality checker for both CSV files.

Checks data/phrases.csv and data/scenarios.csv for missing fields,
invalid enum values, empty source citations, and unverified rows.

Usage:
    python validate.py

Exit codes:
    0 - no errors (warnings are OK)
    1 - one or more errors found
"""

import sys
import pandas as pd
import config

# ── Helpers ───────────────────────────────────────────────────────────────────

def is_blank(value) -> bool:
    return pd.isna(value) or str(value).strip() == ""


def check_csv(
    path: str,
    expected_cols: list,
    enum_checks: dict,
    label: str,
) -> tuple[list, list]:
    """
    Validate one CSV file.
    enum_checks: {column_name: set_of_valid_values}
    Returns (errors, warnings) as lists of (row_num, message) tuples.
    """
    errors, warnings = [], []

    try:
        df = pd.read_csv(path, dtype=str)
    except FileNotFoundError:
        errors.append((0, f"File not found: {path}"))
        return errors, warnings

    missing_cols = [c for c in expected_cols if c not in df.columns]
    if missing_cols:
        errors.append((0, f"Missing columns: {', '.join(missing_cols)}"))
        return errors, warnings

    for idx, row in df.iterrows():
        row_num = idx + 2  # +2: header is line 1, pandas is 0-indexed

        blank_cols = set()

        # Missing values
        for col in expected_cols:
            if is_blank(row[col]):
                if col in ("source_url", "source_page"):
                    warnings.append((row_num, f"missing {col} (source not yet confirmed)"))
                else:
                    errors.append((row_num, f"missing value in column '{col}'"))
                blank_cols.add(col)

        # Enum checks
        for col, valid_set in enum_checks.items():
            if col not in blank_cols:
                val = str(row[col]).strip()
                if val not in valid_set:
                    errors.append((row_num,
                        f"invalid {col} '{val}' "
                        f"— must be one of: {', '.join(sorted(valid_set))}"))

        # Unverified warning
        if "verified" not in blank_cols:
            if str(row["verified"]).strip().lower() == "false":
                warnings.append((row_num, "verified = false"))

    return errors, warnings


def print_results(label: str, errors: list, warnings: list) -> None:
    print(f"\n--- {label} ---")
    if errors:
        print("ERRORS:")
        for row_num, msg in errors:
            prefix = f"  Row {row_num}: " if row_num else "  "
            print(f"{prefix}{msg}")
    if warnings:
        print("WARNINGS:")
        for row_num, msg in warnings:
            print(f"  Row {row_num}: {msg}")
    if not errors and not warnings:
        print("  All rows valid and verified.")
    else:
        print(f"  {len(errors)} error(s), {len(warnings)} warning(s).")


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    print("Validating CSV files...\n")

    # phrases.csv
    phrase_errors, phrase_warnings = check_csv(
        path=config.CSV_PATH,
        expected_cols=config.PHRASE_COLUMNS,
        enum_checks={
            "situation":  set(config.SITUATIONS),
            "action_by":  set(config.ACTION_BY_VALUES),
            "keigo_type": set(config.KEIGO_TYPES),
        },
        label="phrases.csv",
    )

    # scenarios.csv
    scenario_errors, scenario_warnings = check_csv(
        path=config.SCENARIOS_CSV_PATH,
        expected_cols=config.SCENARIO_COLUMNS,
        enum_checks={
            "situation":    set(config.SCENARIO_SITUATIONS),
            "actor":        set(config.ACTOR_VALUES),
            "listener":     set(config.LISTENER_VALUES),
            "correct_type": set(config.KEIGO_TYPES),
        },
        label="scenarios.csv",
    )

    print_results("data/phrases.csv",   phrase_errors,   phrase_warnings)
    print_results("data/scenarios.csv", scenario_errors, scenario_warnings)

    total_errors = len(phrase_errors) + len(scenario_errors)
    total_warnings = len(phrase_warnings) + len(scenario_warnings)
    print(f"\nTotal: {total_errors} error(s), {total_warnings} warning(s).")

    sys.exit(1 if total_errors else 0)


if __name__ == "__main__":
    main()

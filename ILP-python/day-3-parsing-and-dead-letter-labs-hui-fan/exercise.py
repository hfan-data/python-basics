"""Day 3 exercises -- student stubs.

Implement the four tasks below so that `python3 -m unittest -v` runs green.
The tests in test_exercise.py are pre-written: make them pass, never edit them.

Plumbing below: ROWS (string-valued rows exactly as csv.DictReader yields them)
and make_trips_csv(path) which writes them to a real CSV file.
"""

import csv
import json
from datetime import date  # noqa: F401  (needed once you implement the tasks)

ROWS = [
    {"trip_id": "t-001", "city": "Berlin", "date": "2026-01-05", "minutes": "11", "fare": "14.50"},
    {"trip_id": "t-002", "city": "Hamburg", "date": "2026-01-06", "minutes": "25", "fare": "27.25"},
    {"trip_id": "t-003", "city": "München", "date": "2026-01-07", "minutes": "40", "fare": "46.50"},
    {"trip_id": "t-004", "city": "Köln", "date": "2026-01-08", "minutes": "15", "fare": "19.00"},
    {"trip_id": "t-005", "city": "Berlin", "date": "2026-01-09", "minutes": "8", "fare": "11.05"},
    {"trip_id": "t-006", "city": "Hamburg", "date": "2026-13-01", "minutes": "22", "fare": "20.75"},
    {"trip_id": "t-007", "city": "München", "date": "2026-01-10", "minutes": "-5", "fare": "4.00"},
    {"trip_id": "t-008", "city": "Köln", "date": "2026-01-11", "minutes": "12", "fare": ""},
    {"trip_id": "t-009", "city": "Berlin", "date": "2026-01-12", "minutes": "30", "fare": "31.40"},
    {"trip_id": "t-010", "city": "Hamburg", "date": "2026-01-13", "minutes": "18", "fare": "22.60"},
]

FIELDS = ["trip_id", "city", "date", "minutes", "fare"]


def make_trips_csv(path) -> None:
    """Provided plumbing: write ROWS to a CSV file at path."""
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, restval="")
        writer.writeheader()
        writer.writerows(ROWS)


def parse_row(row: dict) -> dict:
    """Task 1: convert one string-valued row into typed values.

    Returns a dict with keys trip_id (str), city (str), date (date),
    minutes (int >= 0), fare (float > 0). Raises ValueError whose message
    names the offending field for: a missing key, an unparseable date,
    unparseable or negative minutes, and unparseable or non-positive fare.
    """
    required_fields = ["trip_id", "city", "date", "minutes", "fare"]
    for field in required_fields:
        if field not in row:
            raise ValueError(f"missing field: {field}")

    # Parse date
    try:
        parsed_date = date.fromisoformat(row["date"])
    except (ValueError, TypeError) as exc:
        raise ValueError(f"date: invalid date value {row['date']!r}") from exc

    # Parse minutes (must be int and >= 0)
    try:
        minutes = int(row["minutes"])
    except (ValueError, TypeError) as exc:
        raise ValueError(f"minutes: invalid integer {row['minutes']!r}") from exc
    if minutes < 0:
        raise ValueError(f"minutes: value must be non-negative, got {minutes}")

    # Parse fare (must be float and > 0)
    try:
        fare = float(row["fare"])
    except (ValueError, TypeError) as exc:
        raise ValueError(f"fare: invalid float {row['fare']!r}") from exc
    if fare <= 0:
        raise ValueError(f"fare: value must be greater than zero, got {fare}")

    return {
        "trip_id": str(row["trip_id"]),
        "city": str(row["city"]),
        "date": parsed_date,
        "minutes": minutes,
        "fare": fare,
    }


def in_window(rows: list[dict], start: date, end: date) -> list[dict]:
    """Task 2: keep only rows dated inside the half-open window [start, end).

    Rows are already parsed (date is a date object). start is included,
    end is excluded.
    """
    return [r for r in rows if start <= r["date"] < end]


def write_jsonl(rows: list[dict], path) -> None:
    """Task 3: write rows to path as JSON lines.

    One json.dumps per row, each followed by a single newline, dates
    serialised via default=str. The file is written with encoding utf-8.
    """
    with open(path, "w", encoding="utf-8") as handle:
        for r in rows:
            handle.write(json.dumps(r, default=str) + "\n")


def clean_and_split(csv_path, start: date, end: date) -> tuple[list[dict], list[tuple[dict, str]]]:
    """Task 4 -- Synthesis: clean a CSV and dead-letter its rejects.

    Read the CSV at csv_path with csv.DictReader. Parse each row with
    parse_row; malformed rows become (raw_row, reason) rejects. Parsed rows
    are kept only when their date falls in [start, end); out-of-window rows
    are dropped silently (they are not errors). Returns (clean_rows, rejects).
    """
    parsed_rows = []
    rejects = []

    with open(csv_path, "r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for raw_row in reader:
            try:
                parsed = parse_row(raw_row)
                parsed_rows.append(parsed)
            except ValueError as exc:
                rejects.append((raw_row, str(exc)))

    clean_rows = in_window(parsed_rows, start, end)
    return clean_rows, rejects

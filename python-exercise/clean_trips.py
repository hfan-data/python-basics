"""clean_trips.py -- Day 3 live coding final state: a robust CSV cleaner.

Reads trips.csv (creating a messy sample if absent), parses rows defensively,
dead-letters malformed rows to a JSONL rejects file, writes cleaned.json, and
logs an honest summary. Rejects path configurable via REJECTS_PATH.

Run:  python3 clean_trips.py
"""

import csv
import json
import logging
import os
from datetime import date
from pathlib import Path

HERE = Path(__file__).parent
CSV_PATH = HERE / "trips.csv"
CLEANED_PATH = HERE / "cleaned.json"
REJECTS_PATH = Path(os.environ.get("REJECTS_PATH", str(HERE / "rejects.jsonl")))

logger = logging.getLogger(__name__)

SAMPLE_ROWS = [
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


def make_sample_csv() -> None:
    fields = ["trip_id", "city", "date", "minutes", "fare"]
    with CSV_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, restval="")
        writer.writeheader()
        writer.writerows(SAMPLE_ROWS)


def parse_field(row: dict, field: str, convert):
    """Run convert on row[field]; any failure becomes a ValueError naming the field."""
    try:
        return convert(row[field])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"bad {field}: {row.get(field)!r}") from exc


def parse_row(row: dict) -> dict:
    """Convert one CSV string-row into typed values, or raise ValueError naming the field."""
    minutes = parse_field(row, "minutes", int)
    if minutes < 0:
        raise ValueError(f"bad minutes: {minutes} (negative)")
    fare = parse_field(row, "fare", float)
    if fare <= 0:
        raise ValueError(f"bad fare: {fare} (must be positive)")
    return {
        "trip_id": parse_field(row, "trip_id", str),
        "city": parse_field(row, "city", str),
        "date": parse_field(row, "date", date.fromisoformat),
        "minutes": minutes,
        "fare": fare,
    }


def write_jsonl(records: list[dict], path: Path) -> None:
    handle = path.open("w", encoding="utf-8")
    try:
        for record in records:
            handle.write(json.dumps(record, default=str) + "\n")
    finally:
        handle.close()


def read_trips(path: Path) -> tuple[list[dict], list[tuple[dict, str]]]:
    """Parse every CSV row: good rows to clean, bad rows to rejects with the reason."""
    clean: list[dict] = []
    rejects: list[tuple[dict, str]] = []
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            try:
                clean.append(parse_row(row))
            except ValueError as exc:
                rejects.append((row, str(exc)))
    return clean, rejects


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    if not CSV_PATH.exists():
        logger.info("no input found; writing sample %s", CSV_PATH.name)
        make_sample_csv()

    clean, rejects = read_trips(CSV_PATH)

    CLEANED_PATH.write_text(json.dumps(clean, indent=2, default=str) + "\n", encoding="utf-8")
    write_jsonl(
        [{"row": row, "reason": reason} for row, reason in rejects],
        REJECTS_PATH,
    )

    logger.info("accepted %d rows, rejected %d", len(clean), len(rejects))
    for row, reason in rejects:
        logger.warning("rejected %s: %s", row.get("trip_id", "?"), reason)


if __name__ == "__main__":
    main()

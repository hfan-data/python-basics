"""broken_city_report.py -- Day 5 Activity 2, debug station: the city report with four bugs.

The same pipeline your group built in Activity 1, with four bugs planted in it. Run it, follow
the debugging order (traceback, print the suspect value, try the line in the REPL), and fix one
bug at a time. Do not compare with a solution until your group has a fix for all four.

Run:  python3 broken_city_report.py
"""

import csv
from pathlib import Path

HERE = Path(__file__).parent
CSV_PATH = HERE / "trips.csv"
REPORT_PATH = HERE / "report.txt"

SAMPLE_ROWS = [
    {"trip_id": "t-001", "city": "Berlin", "fare": "14.50"},
    {"trip_id": "t-002", "city": " hamburg ", "fare": "27.25"},
    {"trip_id": "t-003", "city": "BERLIN", "fare": "11.05"},
    {"trip_id": "t-004", "city": "München", "fare": "abc"},
    {"trip_id": "t-005", "city": "Köln", "fare": "19.00"},
    {"trip_id": "t-006", "city": "Hamburg", "fare": "-4.00"},
    {"trip_id": "t-007", "city": "berlin", "fare": "31.40"},
    {"trip_id": "t-008", "city": "", "fare": "12.00"},
]


def make_sample_csv() -> None:
    """Write SAMPLE_ROWS to CSV_PATH."""
    with CSV_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["trip_id", "city", "fare"])
        writer.writeheader()
        writer.writerows(SAMPLE_ROWS)


def parse_trip(row: dict) -> dict | None:
    """A typed trip, or None when the city is empty or the fare is not a positive number."""
    city = row["city"]
    city = city.strip().title()
    try:
        fare = float(row["fare"])
        if fare <= 0:
            return None
    except ValueError:
        return None
    if city == "":
        return None
    return {"trip_id": row["trip_id"], "city": city, "fare": fare}


def city_totals(trips: list[dict]) -> dict[str, float]:
    """Total fare per city, rounded to 2 decimals."""
    totals = {}
    for trip in trips:
        totals[trip["city"]] = totals.get(trip["city"], 0.0) + trip["fare"]
    return {city: round(total, 2) for city, total in totals.items()}


def format_report(totals: dict[str, float], skipped: int) -> list[str]:
    """Report lines: cities by revenue (highest first, ties alphabetical), a total, the skip count."""
    ranking = sorted(totals.items(), key=lambda item: (-item[1], item[0]))
    lines = [f"{city:<10}{total:>8.2f}" for city, total in ranking]
    lines.append(f"{'TOTAL':<10}{sum(totals.values()):>8.2f}")
    lines.append(f"skipped: {skipped}")
    return lines


def main() -> None:
    if not CSV_PATH.exists():
        make_sample_csv()

    trips = []
    skipped = 0
    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            trip = parse_trip(row)
            if trip is None:
                skipped += 1
            else:
                trips.append(trip)

    lines = format_report(city_totals(trips), skipped)
    with REPORT_PATH.open("a", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

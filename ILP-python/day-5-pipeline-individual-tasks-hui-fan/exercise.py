"""Day 5 individual tasks -- student stubs.

Implement the four tasks below so that `python3 -m unittest -v` runs green.
The tests in test_exercise.py are pre-written: make them pass, never edit them.

ROWS is provided plumbing: eight string-valued rows, exactly as
csv.DictReader yields them. Four are invalid and cities are messy.
"""

import csv  # noqa: F401  (needed once you implement the tasks)

ROWS = [
    {"trip_id": "r-01", "city": " dresden ", "fare": "18.40"},
    {"trip_id": "r-02", "city": "Leipzig", "fare": "22.10"},
    {"trip_id": "r-03", "city": "DRESDEN", "fare": "9.60"},
    {"trip_id": "r-04", "city": "Bremen", "fare": "n/a"},
    {"trip_id": "r-05", "city": "  ", "fare": "12.00"},
    {"trip_id": "r-06", "city": "leipzig", "fare": "-3.50"},
    {"trip_id": "r-07", "city": "Bremen", "fare": "15.00"},
    {"trip_id": "r-08", "city": "Leipzig", "fare": "0"},
]


def find_rejects(rows: list[dict]) -> list[tuple[str, str]]:
    """Task 1 (design): every row that cannot be used, with the reason.

    Returns [(trip_id, reason), ...] in input order. Check in this order and
    report only the first reason that applies:
      "empty city"         the city is empty or only spaces
      "fare not a number"  float() cannot convert the fare
      "fare not positive"  the fare is zero or negative
    """
    rejects = []
    for row in rows:
        trip_id = row.get("trip_id", "")
        city = row.get("city", "")
        fare_raw = row.get("fare", "")

        if not city.strip():
            rejects.append((trip_id, "empty city"))
            continue

        try:
            fare = float(fare_raw)
        except ValueError:
            rejects.append((trip_id, "fare not a number"))
            continue

        if fare <= 0:
            rejects.append((trip_id, "fare not positive"))
            continue

    return rejects


def city_totals(rows: list[dict]) -> dict[str, float]:
    """Task 2 (evaluate): the fixed version of a colleague's function.

    The colleague wrote:

        def city_totals(rows, totals={}):
            for row in rows:
                city = row["city"].strip
                totals[city] = totals.get(city) + float(row["fare"])
            return totals

    Yours skips every row Task 1 would reject, cleans the city
    (" dresden " and "DRESDEN" are both "Dresden"), rounds every total to
    2 decimals, and gives the same result however often it is called.
    """
    totals = {}
    reject_ids = {r[0] for r in find_rejects(rows)}

    for row in rows:
        if row.get("trip_id") in reject_ids:
            continue
        
        city = row["city"].strip().title()
        fare = float(row["fare"])
        totals[city] = round(totals.get(city, 0.0) + fare, 2)

    return totals


def totals_with_trace(rows: list[dict]) -> tuple[dict[str, float], list[dict[str, float]]]:
    """Task 3 (trace): the totals, plus a trace table of how they grew.

    Returns (totals, snapshots). snapshots has one entry per usable row: the
    whole totals dict as it was right after that row, values rounded to 2
    decimals. Later rows must not change earlier snapshots.
    """
    totals = {}
    snapshots = []
    reject_ids = {r[0] for r in find_rejects(rows)}

    for row in rows:
        if row.get("trip_id") in reject_ids:
            continue

        city = row["city"].strip().title()
        fare = float(row["fare"])
        totals[city] = round(totals.get(city, 0.0) + fare, 2)

        snapshots.append(totals.copy())

    return totals, snapshots


def write_summary(rows: list[dict], path) -> tuple[int, int]:
    """Task 4 -- Synthesis (validate, transform, load, safe to rerun).

    Write a CSV file at path with the header row city,total and then one row
    per city: highest total first, ties in alphabetical order, totals written
    with 2 decimals ("28.00"). Replace whatever the file held before, so
    running twice gives the same file. Returns (cities_written, rows_skipped).
    """
    rejects = find_rejects(rows)
    rows_skipped = len(rejects)
    cities_written = 0
    totals = city_totals(rows)

    sorted_cities = sorted(totals.items(), key=lambda x: (-x[1], x[0]))

    with open(path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["city", "total"])
        for city, total in sorted_cities:
            writer.writerow([city, f"{total:.2f}"])

    cities_written = len(sorted_cities)
    return cities_written, rows_skipped

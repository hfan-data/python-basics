"""Day 1 exercises -- student stubs.

Implement the four tasks below so that `python3 -m unittest -v` runs green.
The tests in test_exercise.py are pre-written: make them pass, never edit them.

TRIPS below is provided plumbing: a small, deliberately messy taxi-trip log.
"""

TRIPS = [
    {"trip_id": "t-001", "city": "  Berlin ", "minutes": 11, "miles": 3.2, "fare": 14.50},
    {"trip_id": "t-002", "city": "Hamburg", "minutes": "1:30", "miles": 7.9, "fare": 27.25},
    {"trip_id": "t-003", "city": "Bad Homburg", "minutes": 8, "miles": 2.1, "fare": 11.05},
    {"trip_id": "t-004", "city": "München", "minutes": "45", "miles": 18.4, "fare": 51.30},
    {"trip_id": "t-005", "city": "Berlin", "minutes": "0:05", "miles": 0.4, "fare": 5.25},
    {"trip_id": "t-006", "city": "köln", "minutes": "banana", "miles": 12.0, "fare": 30.10},
    {"trip_id": "t-007", "city": "Hamburg", "minutes": 22, "miles": 5.5, "fare": 20.75},
]


def clean_city(name):
    """Task 1: normalise a city name.

    Strip surrounding whitespace, lowercase everything, and replace inner
    spaces with underscores. A whitespace-only input returns the empty string.
    Examples: "  Berlin " -> "berlin", "Bad Homburg" -> "bad_homburg".
    """
    if not name:
        return ""
    return name.strip().lower().replace(" ", "_")

def parse_duration(text):
    """Task 2: convert a duration string to whole minutes.

    "H:MM" means hours and minutes ("1:30" -> 90); "MM" means minutes only
    ("45" -> 45, "0:05" -> 5). Anything that is not a duration returns
    None ("banana", "", "1:2:3"). Hint: str.isdigit().
    """
    if not isinstance(text, str) or not text:
        return None
    
    parts = text.split(":")
    if len(parts) == 1:
        if parts[0].isdigit():
            return int(parts[0])
    elif len(parts) == 2:
        hours_str, mins_str = parts
        if hours_str.isdigit() and mins_str.isdigit() and len(mins_str) == 2:
            return int(hours_str) * 60 + int(mins_str)
            
    return None


def fare_report_line(trip):
    """Task 3: format one trip as a fixed-width report row.

    Expects a NORMALISED trip dict with keys trip_id (str), city (str,
    already cleaned), minutes (int), miles (float), fare (float).

    Exact template (column widths are part of the contract):

        f"{trip_id:<6} | {city:<15} | {minutes:>3} min"
        f" | {miles:>5.1f} mi | €{fare:.2f}"

    Example: trip_id "t-001", city "berlin", minutes 11, miles 3.2,
    fare 14.5 produce exactly:
        "t-001  | berlin          |  11 min |   3.2 mi | €14.50"
    """
    trip_id = trip["trip_id"]
    city = trip["city"]
    minutes = trip["minutes"]
    miles = trip["miles"]
    fare = trip["fare"]

    line = (
        f"{trip_id:<6} | {city:<15} | {minutes:>3} min"
        f" | {miles:>5.1f} mi | €{fare:.2f}"
    )
    return line


def build_receipt(trips):
    """Task 4 -- Synthesis: build a complete receipt from messy input.

    For each trip: parse minutes (int passes through, string is parsed with
    Task 2 -- a row whose minutes come back as None is SKIPPED),
    clean the city with Task 1, and format the row with Task 3. Append one
    final line f"TOTAL: €{total:.2f}" where total is the sum of the fares of
    the included trips (rounded to 2 decimals).

    Returns the list of lines, trip lines first, TOTAL line last.
    """
    result_lines = []
    total_fare = 0.0

    for trip in trips:
        raw_minutes = trip["minutes"]

        if isinstance(raw_minutes, int):
            parsed_mins = raw_minutes
        elif isinstance(raw_minutes, str):
            parsed_mins = parse_duration(raw_minutes)
        else:
            parsed_mins = None

        if parsed_mins is None:
            continue

        cleaned_city_name = clean_city(trip["city"])

        cleaned_trip = {
            "trip_id": trip["trip_id"],
            "city": cleaned_city_name,
            "minutes": parsed_mins,
            "miles": trip["miles"],
            "fare": trip["fare"]
        }

        formatted_line = fare_report_line(cleaned_trip)
        result_lines.append(formatted_line)

        total_fare += trip["fare"]

    total_line = f"TOTAL: €{total_fare:.2f}"
    result_lines.append(total_line)

    return result_lines

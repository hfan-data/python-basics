"""fare_report.py -- Day 1's trip-fare report generator: the starting point for Activity 2.

Run it:

    python3 fare_report.py
"""

BASE_FARE = 2.50
PER_MINUTE = 0.40
PER_MILE = 1.75

TRIPS = [
    {"trip_id": "t-001", "city": "Berlin", "minutes": 11, "miles": 3.2},
    {"trip_id": "t-002", "city": "Hamburg", "minutes": 25, "miles": 7.2},
    {"trip_id": "t-003", "city": "München", "minutes": 40, "miles": 16.0},
    {"trip_id": "t-004", "city": "Köln", "minutes": 15, "miles": 6.0},
    {"trip_id": "t-005", "city": "München", "minutes": -5, "miles": 2.0},
]


def fare_estimate(minutes: int, miles: float) -> float:
    """Estimated fare: base plus per-minute and per-mile components, rounded once."""
    return round(BASE_FARE + minutes * PER_MINUTE + miles * PER_MILE, 2)


def is_valid_trip(trip: dict) -> bool:
    """A trip is usable when neither minutes nor miles is negative."""
    return trip["minutes"] >= 0 and trip["miles"] >= 0


def report_line(trip: dict, fare: float) -> str:
    """One aligned table row for the report."""
    return (
        f"{trip['trip_id']:<6} | {trip['city']:<15} | {trip['minutes']:>3} min"
        f" | {trip['miles']:>5.1f} mi | €{fare:.2f}"
    )


def main() -> None:
    print(f"{'trip':<6} | {'city':<15} | {'min':>3}     | {'miles':>5}     | fare")
    total = 0.0
    for trip in TRIPS:
        if not is_valid_trip(trip):
            print(f"skipping {trip['trip_id']}: minutes and miles must be >= 0")
            continue
        fare = fare_estimate(trip["minutes"], trip["miles"])
        total += fare
        print(report_line(trip, fare))
    print(f"TOTAL: €{total:.2f}")


if __name__ == "__main__":
    main()

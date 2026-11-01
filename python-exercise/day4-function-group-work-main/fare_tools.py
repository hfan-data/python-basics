"""Reusable fare toolkit for Day 4 Activity 2.

Run it:

    python3 fare_tools.py
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


def fare_estimate(
    minutes: int, miles: float, *, base=BASE_FARE, per_minute=PER_MINUTE,
    per_mile=PER_MILE, night=False, minimum=0.0,
) -> float:
    """Estimated fare: base plus per-minute and per-mile components, rounded once."""
    total = (base + minutes * per_minute + miles * per_mile) * (1.5 if night else 1.0)
    return round(max(total, minimum), 2)


def is_valid_trip(trip: dict) -> bool:
    """A trip is usable when neither minutes nor miles is negative."""
    return trip["minutes"] >= 0 and trip["miles"] >= 0

def split_trips(trips: list) -> tuple:
    """Return usable trips and invalid trip IDs, preserving input order."""
    valid = [t for t in trips if is_valid_trip(t)]
    invalid_ids = [t["trip_id"] for t in trips if not is_valid_trip(t)]
    return valid, invalid_ids


def price_trip(trip: dict, **pricing_options) -> dict:
    """Return a new priced trip, forwarding named options to fare_estimate."""
    return {
        **trip,
        "fare": fare_estimate(trip["minutes"], trip["miles"], **pricing_options),
    }


def summarise(fares: list[float]) -> tuple[int, float, float]:
    """Return fare count, total and average; use zeros for an empty list."""
    count = len(fares)
    total = round(sum(fares), 2)
    average = round(total / count, 2) if count else 0.0
    return count, total, average


def report_line(trip: dict, fare: float) -> str:
    """One aligned table row for the report."""
    return (
        f"{trip['trip_id']:<6} | {trip['city']:<15} | {trip['minutes']:>3} min"
        f" | {trip['miles']:>5.1f} mi | €{fare:.2f}"
    )


def main() -> None:
    print(f"{'trip':<6} | {'city':<15} | {'min':>3}     | {'miles':>5}     | fare")
    valid, invalid_ids = split_trips(TRIPS)
    priced = [price_trip(trip) for trip in valid]
    for trip in priced:
        print(report_line(trip, trip["fare"]))
    for trip_id in invalid_ids:
        print(f"skipping {trip_id}: minutes and miles must be >= 0")
    count, total, average = summarise([trip["fare"] for trip in priced])
    print(f"TOTAL: €{total:.2f}")
    print(f"COUNT: {count} | AVERAGE: €{average:.2f}")


if __name__ == "__main__":
    main()

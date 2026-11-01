"""city_totals.py -- Day 2 live coding final state: city aggregation & ranking.

Run:  python3 city_totals.py
"""

TRIPS = [
    {"trip_id": "t-001", "city": "Berlin", "fare": 14.50},
    {"trip_id": "t-002", "city": "Hamburg", "fare": 27.25},
    {"trip_id": "t-003", "city": "Berlin", "fare": 11.05},
    {"trip_id": "t-004", "city": "München", "fare": 51.30},
    {"trip_id": "t-005", "city": "Berlin", "fare": 5.25},
    {"trip_id": "t-006", "city": "Köln", "fare": 30.10},
    {"trip_id": "t-007", "city": "Hamburg", "fare": 20.75},
    {"trip_id": "t-008", "city": "München", "fare": 43.60},
    {"trip_id": "t-009", "city": "Hamburg", "fare": 18.90},
    {"trip_id": "t-010", "city": "berlin", "fare": 9.40},
    {"trip_id": "t-011", "city": "Köln", "fare": 26.10},
    {"trip_id": "t-012", "city": "München", "fare": 38.70},
]


def fares_by_city(trips: list[dict]) -> dict[str, list[float]]:
    """Group fares per city using the setdefault group-by idiom."""
    grouped: dict[str, list[float]] = {}
    for trip in trips:
        grouped.setdefault(trip["city"], []).append(trip["fare"])
    return grouped


def averages(grouped: dict[str, list[float]]) -> dict[str, float]:
    """Average fare per city, rounded to 2 decimals, as a dict comprehension."""
    return {city: round(sum(fares) / len(fares), 2) for city, fares in grouped.items()}


def main() -> None:
    grouped = fares_by_city(TRIPS)
    avgs = averages(grouped)
    ranked = sorted(avgs.items(), key=lambda kv: kv[1], reverse=True)

    total_revenue = sum(trip["fare"] for trip in TRIPS)
    big_fares = [trip["fare"] for trip in TRIPS if trip["fare"] >= 30.0]
    best_city, best_avg = max(avgs.items(), key=lambda kv: kv[1])

    print(f"{'city':<15} | {'avg fare':>8} | {'trips':>5}")
    for city, avg in ranked:
        print(f"{city:<15} | {avg:>8.2f} | {len(grouped[city]):>5}")
    print()
    print(f"Best city by average: {best_city} (€{best_avg:.2f})")
    print(f"Trips at or above €30.00: {len(big_fares)}")
    print(f"Total revenue: €{total_revenue:.2f}")


if __name__ == "__main__":
    main()

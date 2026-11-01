"""Day 2 exercises -- student stubs.

Implement the four tasks below so that `python3 -m unittest -v` runs green.
The tests in test_exercise.py are pre-written: make them pass, never edit them.

TRIPS is provided plumbing: the twelve-trip log from the live coding.
Note: "berlin" and "Berlin" are distinct cities in this data.
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


def unique_cities(trips: list[dict]) -> list[str]:
    """Task 1: every distinct city in the trips, as a sorted list.

    Each city appears once; the result is in ascending string order.
    """
    return sorted(list({trip["city"] for trip in trips})) if trips else []


def city_fares(trips: list[dict]) -> dict[str, list[float]]:
    """Task 2: map each city to the list of its fares, in encounter order.

    Build it with the setdefault group-by idiom.
    """
    fares = {}
    for trip in trips:
        city = trip["city"]
        fare = trip["fare"]
        fares.setdefault(city, []).append(fare)
    return fares


def averages(fares_by_city: dict[str, list[float]]) -> dict[str, float]:
    """Task 3: city -> average fare (rounded to 2 decimals), as a dict
    comprehension over .items().
    """
    return {
        city: round(sum(fares) / len(fares), 2)
        for city, fares in fares_by_city.items()
    }


def top_cities(trips: list[dict], n: int) -> list[tuple[str, float]]:
    """Task 4 -- Synthesis: the n best cities by average fare.

    Returns (city, average) tuples, best first. Ties are broken
    alphabetically by city name. An n larger than the number of cities
    returns all cities.
    """
    fares = city_fares(trips)
    avg_fares = averages(fares)

    city_avg_pairs = list(avg_fares.items())

    sorted_cities = sorted(city_avg_pairs, key=lambda pair: (-pair[1], pair[0]))

    return sorted_cities[:n]
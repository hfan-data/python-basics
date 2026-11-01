"""Day 4 exercises -- student stubs.

Implement the four tasks below so that `python3 -m unittest -v` runs green.
The tests in test_exercise.py are pre-written: make them pass, never edit them.

TRIPS is provided plumbing: six trips, two of them invalid (negative minutes
or negative miles).
"""

from email.mime import base


TRIPS = [
    {"trip_id": "t-001", "city": "Berlin", "minutes": 11, "miles": 3.2},
    {"trip_id": "t-002", "city": "Hamburg", "minutes": 25, "miles": 7.2},
    {"trip_id": "t-003", "city": "München", "minutes": 40, "miles": 16.0},
    {"trip_id": "t-004", "city": "Köln", "minutes": -5, "miles": 2.0},
    {"trip_id": "t-005", "city": "Berlin", "minutes": 8, "miles": -1.0},
    {"trip_id": "t-006", "city": "Hamburg", "minutes": 18, "miles": 5.5},
]


def fare(
    minutes: int,
    miles: float,
    *,
    base: float = 2.50,
    per_minute: float = 0.40,
    per_mile: float = 1.75,
    night: bool = False,
) -> float:
    """Task 1: the fare for one trip, rounded to 2 decimals.

    fare = base + minutes * per_minute + miles * per_mile
    When night is True the whole fare is multiplied by 1.5 (before rounding).
    Everything after the `*` is keyword-only (the signature is given).
    """
    total = base + (minutes * per_minute) + (miles * per_mile)
    if night:
        total *= 1.5
    return round(total, 2)


def split_valid(trips: list[dict]) -> tuple[list[dict], list[str]]:
    """Task 2: return (valid_trips, rejected_ids).

    A trip is valid when both minutes and miles are >= 0. Both lists keep
    the input order. rejected_ids holds only the trip_id strings.
    """
    valid = []
    rejected = []
    for trip in trips:
        if trip["minutes"] >= 0 and trip["miles"] >= 0:
            valid.append(trip)
        else:
            rejected.append(trip["trip_id"])
    return valid, rejected


def make_trip(trip_id: str, city: str, *, tags: list[str] | None = None, **extra) -> dict:
    """Task 3: build one trip dict.

    Keys: trip_id, city, tags, plus every extra keyword argument.
    tags is a new list on every call: a copy of the given list, or an empty
    list when none is given. Two trips must never share one tags list.
    """
    tags_copy = list(tags) if tags is not None else []
    
    trip = {
        "trip_id": trip_id,
        "city": city,
        "tags": tags_copy,
    }
    trip.update(extra)
    return trip


def price_trips(trips: list[dict], **pricing) -> tuple[list[dict], list[str], float]:
    """Task 4 -- Synthesis: price every valid trip.

    Split the trips (Task 2). For each valid trip build a NEW dict with all
    its keys plus "fare", computed with Task 1 and any pricing keyword
    arguments passed through unchanged (e.g. night=True). The input dicts
    must not change. Returns (priced_trips, rejected_ids, total_fare), with
    the total rounded to 2 decimals.
    """
    valid_trips, rejected_ids = split_valid(trips)
    priced_trips = []
    
    for trip in valid_trips:
        trip_copy = dict(trip)
        trip_fare = fare(trip["minutes"], trip["miles"], **pricing)
        trip_copy["fare"] = trip_fare
        priced_trips.append(trip_copy)
        
    total_fare = round(sum(t["fare"] for t in priced_trips), 2)
    return priced_trips, rejected_ids, total_fare

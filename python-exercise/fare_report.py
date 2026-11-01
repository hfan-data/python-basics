"""Day 1 exercises -- reference solution (instructor copy)."""

TRIPS = [
    {"trip_id": "t-001", "city": "  Berlin ", "minutes": 11, "miles": 3.2, "fare": 14.50},
    {"trip_id": "t-002", "city": "Hamburg", "minutes": "1:30", "miles": 7.9, "fare": 27.25},
    {"trip_id": "t-003", "city": "Bad Homburg", "minutes": 8, "miles": 2.1, "fare": 11.05},
    {"trip_id": "t-004", "city": "München", "minutes": "45", "miles": 18.4, "fare": 51.30},
    {"trip_id": "t-005", "city": "Berlin", "minutes": "0:05", "miles": 0.4, "fare": 5.25},
    {"trip_id": "t-006", "city": "köln", "minutes": "banana", "miles": 12.0, "fare": 30.10},
    {"trip_id": "t-007", "city": "Hamburg", "minutes": 22, "miles": 5.5, "fare": 20.75},
]


def clean_city(name: str) -> str:
    stripped = name.strip().lower()
    return stripped.replace(" ", "_")


def parse_duration(text: str) -> int | None:
    hours, _, minutes = text.rpartition(":")  # "45" -> ("", "", "45")
    hours = hours or "0"
    if hours.isdigit() and minutes.isdigit():  # "1:2:3" fails: "1:2" is not digits
        return int(hours) * 60 + int(minutes)
    return None


def fare_report_line(trip: dict) -> str:
    return (
        f"{trip['trip_id']:<6} | {trip['city']:<15} | {trip['minutes']:>3} min"
        f" | {trip['miles']:>5.1f} mi | €{trip['fare']:.2f}"
    )


def build_receipt(trips: list[dict]) -> list[str]:
    lines = []
    total = 0.0
    for trip in trips:
        minutes = parse_duration(str(trip["minutes"]))  # 11 -> "11" -> 11
        if minutes is None:
            continue
        normalised = {
            "trip_id": trip["trip_id"],
            "city": clean_city(trip["city"]),
            "minutes": minutes,
            "miles": float(trip["miles"]),
            "fare": float(trip["fare"]),
        }
        lines.append(fare_report_line(normalised))
        total += normalised["fare"]
    lines.append(f"TOTAL: €{round(total, 2):.2f}")
    return lines
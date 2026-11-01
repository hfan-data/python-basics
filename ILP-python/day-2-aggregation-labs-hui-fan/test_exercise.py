"""Day 2 exercise tests -- pre-written, do not edit.

Run from this folder:  python3 -m unittest -v
"""

import unittest

from exercise import TRIPS, averages, city_fares, top_cities, unique_cities


class UniqueCitiesTest(unittest.TestCase):
    def test_sorted_distinct_cities(self):
        self.assertEqual(
            unique_cities(TRIPS),
            ["Berlin", "Hamburg", "Köln", "München", "berlin"],
        )

    def test_empty_input(self):
        self.assertEqual(unique_cities([]), [])


class CityFaresTest(unittest.TestCase):
    def test_exact_grouping(self):
        self.assertEqual(
            city_fares(TRIPS),
            {
                "Berlin": [14.50, 11.05, 5.25],
                "Hamburg": [27.25, 20.75, 18.90],
                "München": [51.30, 43.60, 38.70],
                "Köln": [30.10, 26.10],
                "berlin": [9.40],
            },
        )

    def test_encounter_order_preserved(self):
        grouped = city_fares(TRIPS)
        self.assertEqual(grouped["Berlin"][0], 14.50)
        self.assertEqual(grouped["Berlin"][-1], 5.25)


class AveragesTest(unittest.TestCase):
    def test_exact_averages(self):
        self.assertEqual(
            averages(city_fares(TRIPS)),
            {
                "Berlin": 10.27,
                "Hamburg": 22.30,
                "München": 44.53,
                "Köln": 28.10,
                "berlin": 9.40,
            },
        )

    def test_single_trip_city(self):
        self.assertEqual(averages({"berlin": [9.40]}), {"berlin": 9.40})


class TopCitiesTest(unittest.TestCase):
    def test_top_two(self):
        self.assertEqual(
            top_cities(TRIPS, 2),
            [("München", 44.53), ("Köln", 28.10)],
        )

    def test_ties_break_alphabetically(self):
        trips = [
            {"trip_id": "a", "city": "Köln", "fare": 20.0},
            {"trip_id": "b", "city": "Hamburg", "fare": 20.0},
            {"trip_id": "c", "city": "Hamburg", "fare": 20.0},
        ]
        self.assertEqual(
            top_cities(trips, 2),
            [("Hamburg", 20.0), ("Köln", 20.0)],
        )

    def test_oversized_n_returns_all(self):
        ranked = top_cities(TRIPS, 99)
        self.assertEqual(len(ranked), 5)
        self.assertEqual(ranked[0], ("München", 44.53))


if __name__ == "__main__":
    unittest.main()

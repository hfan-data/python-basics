"""Day 4 exercise tests -- pre-written, do not edit.

Run from this folder:  python3 -m unittest -v
"""

import copy
import unittest

from exercise import TRIPS, fare, make_trip, price_trips, split_valid


class FareTest(unittest.TestCase):
    def test_default_pricing(self):
        self.assertEqual(fare(11, 3.2), 12.50)
        self.assertEqual(fare(25, 7.2), 25.10)

    def test_night_multiplies_by_one_and_a_half(self):
        self.assertEqual(fare(11, 3.2, night=True), 18.75)

    def test_rates_can_be_overridden_by_name(self):
        self.assertEqual(fare(11, 3.2, base=0.0), 10.00)
        self.assertEqual(fare(10, 0.0, per_minute=1.0, base=0.0), 10.00)

    def test_pricing_options_are_keyword_only(self):
        with self.assertRaises(TypeError):
            fare(11, 3.2, 2.50)


class SplitValidTest(unittest.TestCase):
    def test_returns_valid_trips_and_rejected_ids(self):
        valid, rejected_ids = split_valid(TRIPS)
        self.assertEqual([trip["trip_id"] for trip in valid], ["t-001", "t-002", "t-003", "t-006"])
        self.assertEqual(rejected_ids, ["t-004", "t-005"])

    def test_zero_is_valid(self):
        valid, rejected_ids = split_valid([{"trip_id": "z", "minutes": 0, "miles": 0.0}])
        self.assertEqual(len(valid), 1)
        self.assertEqual(rejected_ids, [])

    def test_empty_input(self):
        self.assertEqual(split_valid([]), ([], []))


class MakeTripTest(unittest.TestCase):
    def test_extra_keyword_arguments_become_keys(self):
        trip = make_trip("t-100", "Berlin", minutes=11, miles=3.2)
        self.assertEqual(
            trip,
            {"trip_id": "t-100", "city": "Berlin", "tags": [], "minutes": 11, "miles": 3.2},
        )

    def test_trips_never_share_a_tags_list(self):
        first = make_trip("t-101", "Berlin")
        second = make_trip("t-102", "Hamburg")
        first["tags"].append("night")
        self.assertEqual(second["tags"], [])

    def test_given_tags_are_copied(self):
        tags = ["airport"]
        trip = make_trip("t-103", "Köln", tags=tags)
        trip["tags"].append("night")
        self.assertEqual(tags, ["airport"])
        self.assertEqual(trip["tags"], ["airport", "night"])


class PriceTripsTest(unittest.TestCase):
    def test_default_pricing_totals(self):
        priced, rejected_ids, total = price_trips(TRIPS)
        self.assertEqual([trip["fare"] for trip in priced], [12.50, 25.10, 46.50, 19.32])
        self.assertEqual(rejected_ids, ["t-004", "t-005"])
        self.assertEqual(total, 103.42)

    def test_pricing_options_are_passed_through(self):
        priced, _, total = price_trips(TRIPS, night=True)
        self.assertEqual(priced[0]["fare"], 18.75)
        self.assertEqual(total, 155.14)

    def test_priced_trips_keep_their_other_keys(self):
        priced, _, _ = price_trips(TRIPS)
        self.assertEqual(priced[0]["city"], "Berlin")
        self.assertEqual(priced[0]["minutes"], 11)

    def test_input_trips_are_not_changed(self):
        before = copy.deepcopy(TRIPS)
        price_trips(TRIPS, night=True)
        self.assertEqual(TRIPS, before)

    def test_unknown_pricing_option_fails_loudly(self):
        with self.assertRaises(TypeError):
            price_trips(TRIPS, discount=0.1)


if __name__ == "__main__":
    unittest.main()

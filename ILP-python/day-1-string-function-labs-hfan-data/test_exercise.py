"""Day 1 exercise tests -- pre-written, do not edit.

Run from this folder:  python3 -m unittest -v
Red (NotImplementedError) until exercise.py is implemented, then green.
"""

import unittest

from exercise import TRIPS, build_receipt, clean_city, fare_report_line, parse_duration

FIRST_LINE = "t-001  | berlin          |  11 min |   3.2 mi | €14.50"


class CleanCityTest(unittest.TestCase):
    def test_strips_and_lowercases(self):
        self.assertEqual(clean_city("  Berlin "), "berlin")

    def test_inner_spaces_become_underscores(self):
        self.assertEqual(clean_city("Bad Homburg"), "bad_homburg")

    def test_whitespace_only_returns_empty_string(self):
        self.assertEqual(clean_city("   "), "")


class ParseDurationTest(unittest.TestCase):
    def test_hours_and_minutes(self):
        self.assertEqual(parse_duration("1:30"), 90)

    def test_minutes_only(self):
        self.assertEqual(parse_duration("45"), 45)

    def test_zero_hours_padded_minutes(self):
        self.assertEqual(parse_duration("0:05"), 5)

    def test_not_a_duration_returns_none(self):
        self.assertIsNone(parse_duration("banana"))
        self.assertIsNone(parse_duration(""))
        self.assertIsNone(parse_duration("1:2:3"))


class FareReportLineTest(unittest.TestCase):
    def test_docstring_example(self):
        trip = {"trip_id": "t-001", "city": "berlin", "minutes": 11,
                "miles": 3.2, "fare": 14.5}
        self.assertEqual(fare_report_line(trip), FIRST_LINE)

    def test_second_exact_line(self):
        trip = {"trip_id": "t-004", "city": "münchen", "minutes": 45,
                "miles": 18.4, "fare": 51.30}
        self.assertEqual(
            fare_report_line(trip),
            "t-004  | münchen         |  45 min |  18.4 mi | €51.30",
        )

    def test_money_always_has_two_decimals(self):
        trip = {"trip_id": "t-005", "city": "berlin", "minutes": 5,
                "miles": 0.4, "fare": 5.0}
        self.assertTrue(fare_report_line(trip).endswith(" | €5.00"))


class BuildReceiptTest(unittest.TestCase):
    def test_six_trips_plus_total(self):
        self.assertEqual(len(build_receipt(TRIPS)), 7)

    def test_first_line(self):
        self.assertEqual(build_receipt(TRIPS)[0], FIRST_LINE)

    def test_total_line(self):
        self.assertEqual(build_receipt(TRIPS)[-1], "TOTAL: €130.10")

    def test_unparseable_row_is_skipped(self):
        receipt = build_receipt(TRIPS)
        self.assertFalse(any("t-006" in line for line in receipt))


if __name__ == "__main__":
    unittest.main()

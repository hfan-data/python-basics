"""Day 5 individual task tests -- pre-written, do not edit.

Run from this folder:  python3 -m unittest -v
"""

import copy
import csv
import tempfile
import unittest
from pathlib import Path

from exercise import ROWS, city_totals, find_rejects, totals_with_trace, write_summary


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.reader(handle))


class FindRejectsTest(unittest.TestCase):
    def test_every_bad_row_with_its_reason(self):
        self.assertEqual(
            find_rejects(ROWS),
            [
                ("r-04", "fare not a number"),
                ("r-05", "empty city"),
                ("r-06", "fare not positive"),
                ("r-08", "fare not positive"),
            ],
        )

    def test_only_the_first_reason_is_reported(self):
        row = {"trip_id": "r-99", "city": "", "fare": "abc"}
        self.assertEqual(find_rejects([row]), [("r-99", "empty city")])

    def test_no_rows(self):
        self.assertEqual(find_rejects([]), [])


class CityTotalsTest(unittest.TestCase):
    def test_clean_cities_and_skip_bad_rows(self):
        self.assertEqual(city_totals(ROWS), {"Dresden": 28.0, "Leipzig": 22.1, "Bremen": 15.0})

    def test_same_result_every_call(self):
        self.assertEqual(city_totals(ROWS[:2]), city_totals(ROWS[:2]))
        self.assertEqual(city_totals(ROWS[:2]), {"Dresden": 18.4, "Leipzig": 22.1})

    def test_no_rows(self):
        self.assertEqual(city_totals([]), {})

    def test_input_rows_are_not_changed(self):
        before = copy.deepcopy(ROWS)
        city_totals(ROWS)
        self.assertEqual(ROWS, before)


class TotalsWithTraceTest(unittest.TestCase):
    def test_one_snapshot_per_usable_row(self):
        totals, snapshots = totals_with_trace(ROWS)
        self.assertEqual(totals, {"Dresden": 28.0, "Leipzig": 22.1, "Bremen": 15.0})
        self.assertEqual(
            snapshots,
            [
                {"Dresden": 18.4},
                {"Dresden": 18.4, "Leipzig": 22.1},
                {"Dresden": 28.0, "Leipzig": 22.1},
                {"Dresden": 28.0, "Leipzig": 22.1, "Bremen": 15.0},
            ],
        )

    def test_snapshots_are_independent(self):
        totals, snapshots = totals_with_trace(ROWS)
        self.assertIsNot(snapshots[0], snapshots[1])
        self.assertIsNot(snapshots[-1], totals)

    def test_no_rows(self):
        self.assertEqual(totals_with_trace([]), ({}, []))


class WriteSummaryTest(unittest.TestCase):
    def test_ranked_csv_and_counts(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "summary.csv"
            result = write_summary(ROWS, path)
            rows = read_csv(path)
        self.assertEqual(result, (3, 4))
        self.assertEqual(
            rows,
            [["city", "total"], ["Dresden", "28.00"], ["Leipzig", "22.10"], ["Bremen", "15.00"]],
        )

    def test_ties_are_alphabetical(self):
        tied = [
            {"trip_id": "x-1", "city": "Leipzig", "fare": "10.00"},
            {"trip_id": "x-2", "city": "Bremen", "fare": "10.00"},
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "summary.csv"
            write_summary(tied, path)
            rows = read_csv(path)
        self.assertEqual(rows[1:], [["Bremen", "10.00"], ["Leipzig", "10.00"]])

    def test_running_twice_gives_the_same_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "summary.csv"
            write_summary(ROWS, path)
            first = path.read_bytes()
            write_summary(ROWS, path)
            second = path.read_bytes()
        self.assertEqual(first, second)
        self.assertEqual(second.count(b"Dresden"), 1)


if __name__ == "__main__":
    unittest.main()

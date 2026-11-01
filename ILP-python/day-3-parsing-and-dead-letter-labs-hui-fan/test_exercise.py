"""Day 3 exercise tests -- pre-written, do not edit.

Run from this folder:  python3 -m unittest -v
"""

import json
import tempfile
import unittest
from datetime import date
from pathlib import Path

from exercise import ROWS, clean_and_split, in_window, make_trips_csv, parse_row, write_jsonl

START = date(2026, 1, 5)
END = date(2026, 1, 10)


class ParseRowTest(unittest.TestCase):
    def test_good_row_parses_to_typed_dict(self):
        self.assertEqual(
            parse_row(ROWS[0]),
            {
                "trip_id": "t-001",
                "city": "Berlin",
                "date": date(2026, 1, 5),
                "minutes": 11,
                "fare": 14.50,
            },
        )

    def test_bad_date_names_date(self):
        with self.assertRaisesRegex(ValueError, "date"):
            parse_row(ROWS[5])

    def test_negative_minutes_names_minutes(self):
        with self.assertRaisesRegex(ValueError, "minutes"):
            parse_row(ROWS[6])

    def test_empty_fare_names_fare(self):
        with self.assertRaisesRegex(ValueError, "fare"):
            parse_row(ROWS[7])

    def test_zero_fare_names_fare(self):
        with self.assertRaisesRegex(ValueError, "fare"):
            parse_row({**ROWS[0], "fare": "0"})

    def test_missing_field_is_a_value_error_naming_it(self):
        row = {key: value for key, value in ROWS[0].items() if key != "fare"}
        with self.assertRaisesRegex(ValueError, "fare"):
            parse_row(row)


class InWindowTest(unittest.TestCase):
    def test_start_included_end_excluded(self):
        rows = [
            {"trip_id": "before", "date": date(2026, 1, 4)},
            {"trip_id": "start", "date": START},
            {"trip_id": "inside", "date": date(2026, 1, 9)},
            {"trip_id": "end", "date": END},
        ]
        self.assertEqual(
            [row["trip_id"] for row in in_window(rows, START, END)],
            ["start", "inside"],
        )

    def test_empty_input(self):
        self.assertEqual(in_window([], START, END), [])


class WriteJsonlTest(unittest.TestCase):
    def test_one_line_per_row_and_dates_as_text(self):
        rows = [parse_row(ROWS[0]), parse_row(ROWS[2])]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "clean.jsonl"
            write_jsonl(rows, path)
            lines = path.read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(lines), 2)
        first = json.loads(lines[0])
        self.assertEqual(first["date"], "2026-01-05")
        self.assertEqual(first["fare"], 14.50)
        self.assertEqual(json.loads(lines[1])["city"], "München")

    def test_every_line_ends_with_one_newline(self):
        rows = [parse_row(ROWS[0]), parse_row(ROWS[1])]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "clean.jsonl"
            write_jsonl(rows, path)
            text = path.read_text(encoding="utf-8")
        self.assertTrue(text.endswith("}\n"))
        self.assertEqual(text.count("\n"), 2)


class CleanAndSplitTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        path = Path(tmp.name) / "trips.csv"
        make_trips_csv(path)
        self.clean, self.rejects = clean_and_split(path, START, END)

    def test_five_clean_typed_rows(self):
        self.assertEqual(
            [row["trip_id"] for row in self.clean],
            ["t-001", "t-002", "t-003", "t-004", "t-005"],
        )
        self.assertEqual(self.clean[0]["date"], date(2026, 1, 5))
        self.assertEqual(self.clean[0]["minutes"], 11)

    def test_three_rejects_name_their_fields(self):
        self.assertEqual(
            [raw["trip_id"] for raw, _ in self.rejects],
            ["t-006", "t-007", "t-008"],
        )
        for (_, reason), field in zip(self.rejects, ["date", "minutes", "fare"]):
            self.assertIn(field, reason)

    def test_rejects_keep_the_raw_row(self):
        self.assertEqual(self.rejects[0][0], ROWS[5])

    def test_out_of_window_rows_are_in_neither_list(self):
        seen = [row["trip_id"] for row in self.clean]
        seen += [raw["trip_id"] for raw, _ in self.rejects]
        self.assertNotIn("t-009", seen)
        self.assertNotIn("t-010", seen)


if __name__ == "__main__":
    unittest.main()

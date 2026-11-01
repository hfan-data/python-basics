"""Regression checks for validation, ordering and repeatable report output."""

import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import broken_city_report as report

EXPECTED = (
    "Berlin       56.95\n"
    "Hamburg      27.25\n"
    "Köln         19.00\n"
    "TOTAL       103.20\n"
    "skipped: 3\n"
)


class CityReportTests(unittest.TestCase):
    def test_parse_and_normalise(self):
        row = {"trip_id": "t-001", "city": " hamburg ", "fare": "27.25"}
        self.assertEqual(report.parse_trip(row), {
            "trip_id": "t-001", "city": "Hamburg", "fare": 27.25,
        })
        self.assertEqual(row["city"], " hamburg ")
        self.assertEqual(row["fare"], "27.25")

    def test_invalid_rows(self):
        bad_rows = [
            {}, {"city": None, "fare": "1"}, {"city": "  ", "fare": "1"},
            {"city": "Berlin"}, {"city": "Berlin", "fare": None},
        ]
        bad_rows.extend({"city": "Berlin", "fare": value} for value in
                        ["abc", "0", "-4", "nan", "inf", "-inf"])
        for row in bad_rows:
            with self.subTest(row=row):
                self.assertIsNone(report.parse_trip(row))

    def test_totals_are_independent_and_empty_input_works(self):
        trips = [{"city": "Berlin", "fare": 0.1}, {"city": "Berlin", "fare": 0.2}]
        self.assertEqual(report.city_totals(trips), {"Berlin": 0.3})
        self.assertEqual(report.city_totals(trips), {"Berlin": 0.3})
        self.assertEqual(report.city_totals([]), {})
        self.assertEqual(report.format_report({}, 0), ["TOTAL         0.00", "skipped: 0"])

    def test_sorting_and_ties(self):
        lines = report.format_report({"Köln": 27.25, "Berlin": 56.95, "Hamburg": 27.25}, 0)
        self.assertEqual([line.split()[0] for line in lines[:3]], ["Berlin", "Hamburg", "Köln"])

    def test_pipeline_twice_and_existing_input(self):
        with tempfile.TemporaryDirectory() as directory:
            csv_path = Path(directory) / "trips.csv"
            report_path = Path(directory) / "report.txt"
            with patch.object(report, "CSV_PATH", csv_path), \
                 patch.object(report, "REPORT_PATH", report_path), \
                 contextlib.redirect_stdout(io.StringIO()):
                report.main()
                original_csv = csv_path.read_bytes()
                self.assertEqual(report_path.read_text(encoding="utf-8"), EXPECTED)
                report.main()
                self.assertEqual(report_path.read_text(encoding="utf-8"), EXPECTED)
                self.assertEqual(csv_path.read_bytes(), original_csv)
                csv_path.write_text("trip_id,city,fare\n", encoding="utf-8")
                report.main()
                self.assertEqual(report_path.read_text(encoding="utf-8"),
                                 "TOTAL         0.00\nskipped: 0\n")
                csv_path.write_text("trip_id,city,fare\nx,Berlin,7\n", encoding="utf-8")
                report.main()
                self.assertEqual(report_path.read_text(encoding="utf-8"),
                                 "Berlin        7.00\nTOTAL         7.00\nskipped: 0\n")


if __name__ == "__main__":
    unittest.main()

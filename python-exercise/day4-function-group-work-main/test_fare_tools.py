"""Behavior checks for the Day 4 assignment."""

import contextlib
import copy
import importlib
import io
import unittest

import fare_tools as tools


class FareToolsTests(unittest.TestCase):
    def test_rates_and_keyword_only_options(self):
        self.assertEqual(tools.fare_estimate(11, 3.2), 12.5)
        self.assertEqual(tools.fare_estimate(11, 3.2, night=True), 18.75)
        self.assertEqual(
            tools.fare_estimate(10, 2, base=3, per_minute=1, per_mile=2), 17
        )
        self.assertEqual(tools.fare_estimate(0, 0, minimum=10), 10)
        self.assertEqual(tools.fare_estimate(0, 0, night=True, minimum=10), 10)
        with self.assertRaises(TypeError):
            tools.fare_estimate(11, 3.2, True)

    def test_split_and_price_preserve_input(self):
        original = copy.deepcopy(tools.TRIPS)
        valid, invalid = tools.split_trips(tools.TRIPS)
        self.assertEqual(len(valid), 4)
        self.assertEqual(invalid, ["t-005"])
        priced = tools.price_trip(valid[0], night=True)
        self.assertEqual(priced["fare"], 18.75)
        self.assertIsNot(priced, valid[0])
        self.assertEqual(tools.TRIPS, original)
        self.assertEqual(tools.split_trips([]), ([], []))
        with self.assertRaises(TypeError):
            tools.price_trip(valid[0], nite=True)

    def test_summary(self):
        self.assertEqual(tools.summarise([]), (0, 0.0, 0.0))
        self.assertEqual(tools.summarise([10, 20, 30]), (3, 60, 20))
        fares = [tools.price_trip(t)["fare"] for t in tools.split_trips(tools.TRIPS)[0]]
        self.assertEqual(tools.summarise(fares), (4, 103.1, 25.77))

    def test_imports_are_silent(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            importlib.reload(tools)
            module = importlib.import_module("tools")
            importlib.reload(module)
        self.assertEqual(output.getvalue(), "")
        self.assertEqual(module.double(4), 8)


if __name__ == "__main__":
    unittest.main()

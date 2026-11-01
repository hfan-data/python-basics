**English** | [Deutsch](README_DE.md)

# Day 1 afternoon exercises: string & function labs (12:45–14:45)

**Watch first:** [the video for this lab](https://trytikkr.com/w/lAKYlFxG85elOlg2-np_cw)

**Before you start:** pass the readiness quiz for this assignment in Coder in 90 Classroom. You need 50% to start.

You implement four functions in `exercise.py` until `python3 -m unittest -v` runs green. The tests in `test_exercise.py` are pre-written and complete. Your job is to make them pass, never to edit them. This is exactly how labs work in Modules 4 and 5 of the program.

Run from this folder:

```bash
python3 -m unittest -v
```

Every push is graded by Coder in 90: your score is the number of the 14 tests that pass.

## Reading the test output

You never write or change tests in this course; you only run them and read what they say.

- **One line per test**, ending in `ok`, `FAIL` or `ERROR`. Work through them one task at a time.
- **`ERROR`**: your code crashed. At the start every test shows `NotImplementedError: Task N: ...`; that just means the task is still a stub.
- **`FAIL`**: your code ran but returned the wrong value. The `AssertionError` lines show what the test expected next to what your function returned; the difference is your next fix.
- **The traceback** points at the line in `exercise.py` where things went wrong, just like any other traceback.
- To rerun a single test class while you work on one task: `python3 -m unittest -v test_exercise.CleanCityTest`
- `OK` on the last line means every test passed: the lab is done.

The data (`TRIPS` at the top of `exercise.py`) is a small taxi-trip log. It is deliberately messy: cities have stray whitespace and mixed case, and `minutes` is sometimes an `int`, sometimes a `"H:MM"` or `"MM"` string, sometimes garbage.

## Task 1: `clean_city`

**What:** normalise a city name so downstream grouping works: strip surrounding whitespace, lowercase everything, replace inner spaces with underscores.

**Why:** `"  Berlin "` and `"Berlin"` are the same city to a human and two different dict keys to Python. Pipelines collapse on this.

**Acceptance:** the three `CleanCityTest` cases pass, including whitespace-only input returning the empty string.

## Task 2: `parse_duration`

**What:** turn a duration string into whole minutes. `"H:MM"` means hours and minutes, `"MM"` means minutes only. Anything that is not a duration returns `None`.

**Why:** CSV columns arrive as strings; converting them is the first thing every pipeline does.

**Acceptance:** `"1:30"` → 90, `"45"` → 45, `"0:05"` → 5, and `"banana"`, `""` and `"1:2:3"` return `None` (`ParseDurationTest`).

## Task 3: `fare_report_line`

**What:** format one trip as a fixed-width report row. The exact template is documented in the docstring: `trip_id` left-aligned in 6 columns, `city` left in 15, `minutes` right in 3, `miles` right in 5 with one decimal, money always with exactly 2 decimals, columns separated by `" | "`, and a `€` glued to the fare.

**Why:** aligned columns are the difference between a report humans read and a wall of text.

**Acceptance:** the two exact-string cases and the two-decimal money case in `FareReportLineTest` pass. Tip: copy the template from the docstring into your function. The docstring is the contract.

## Task 4: Synthesis, `build_receipt`

**What:** take the full messy `TRIPS` list and produce a complete receipt: one formatted line per usable trip, then a final `TOTAL: €<amount>` line. A trip is usable when its `minutes` can be parsed (ints pass through, strings are parsed, rows where Task 2 returns `None` are skipped) and its city is cleaned before formatting. The total is the sum of the fares of the included trips, printed with 2 decimals.

**Why:** this combines Tasks 1 to 3 the way a real pipeline does (parse, clean, format, summarise), and the lecture never showed this exact combination.

**Acceptance:** 7 lines total (6 trips plus TOTAL), the first line and the `TOTAL: €130.10` line match exactly, and the unparseable row never appears (`BuildReceiptTest`).

## Handing in

Commit and push to this repository. Each push runs the autograder; the result appears in Coder in 90 Classroom.

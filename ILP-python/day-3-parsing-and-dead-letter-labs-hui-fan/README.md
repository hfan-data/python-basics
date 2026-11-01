**English** | [Deutsch](README_DE.md)

# Day 3 exercises: parsing and dead-letter labs

**Watch first:** [the video for this lab](https://trytikkr.com/w/IsBcwyZxt2uk0-oJezBzrg)

**Before you start:** pass the readiness quiz for this assignment in Coder in 90 Classroom. You need 40% to start.

You implement four functions in `exercise.py` until `python3 -m unittest -v` runs green. The tests in `test_exercise.py` are pre-written and complete. Your job is to make them pass, never to edit them.

Run from this folder:

```bash
python3 -m unittest -v
```

Every push is graded by Coder in 90: your score is the number of the 14 tests that pass. Push whenever you are ready, and as often as you like.

`ROWS` at the top of `exercise.py` is the same messy ten-row log from the live coding. Every value is a string, exactly as `csv.DictReader` delivers it. Three rows are broken on purpose: `t-006` has a month 13, `t-007` has negative minutes and `t-008` has an empty fare. `make_trips_csv(path)` writes those rows to a real CSV file; the tests use it with temporary directories.

## Reading the test output

- **One line per test**, ending in `ok`, `FAIL` or `ERROR`. Work through them one task at a time.
- **`ERROR`**: your code crashed. At the start every test shows `NotImplementedError: Task N: ...`; that only means the task is still a stub.
- **`FAIL`**: your code ran but returned the wrong value, or did not raise the error the test expected. The `AssertionError` lines show what the test expected next to what your function did.
- Read a traceback from the bottom up: the last line says **what** went wrong, then walk up to the first frame in `exercise.py` to find **where**.
- To rerun one test class while you work on one task: `python3 -m unittest -v test_exercise.ParseRowTest`
- `OK` on the last line means every test passed: the lab is done.

## Task 1: `parse_row`

**What:** convert one string-valued row into typed values: `minutes` an `int` (and never negative), `fare` a `float` (and always greater than zero), `date` a `date` object from ISO text. A missing field or a bad value raises `ValueError` **naming the field** in its message.

**Why:** every CSV in the world hands you strings. Converting them with errors that name the field is the first line of defence of every pipeline.

**Acceptance:** the good row parses to the exact typed dict; the three broken rows each raise `ValueError` whose message contains `date`, `minutes` or `fare`; a fare of `"0"` and a row with no `fare` key raise a `ValueError` naming `fare` (`ParseRowTest`).

**Hints:**
- `date.fromisoformat("2026-01-05")` returns a `date`, and raises `ValueError` for text that is not a real date.
- Python's own message (`could not convert string to float: ''`) does not name the field. Catch it and raise your own: `raise ValueError(f"fare: bad value {text!r}") from exc`.
- A missing key raises `KeyError`, not `ValueError`. The tests want a `ValueError`, so catch the one and raise the other.
- `int("-5")` succeeds. A negative number is a rule of *your* data, so check it yourself after converting.

## Task 2: `in_window`

**What:** given already-parsed rows and a `[start, end)` window of `date` objects, return only the rows whose date falls inside: `start` included, `end` excluded.

**Why:** half-open windows are how pipelines avoid processing a boundary day twice. Yesterday's window ends exactly where today's begins, and every row belongs to one of them.

**Acceptance:** a row dated exactly `start` stays; a row dated exactly `end` does not; a row before the window does not; no rows in gives no rows out (`InWindowTest`).

**Hint:** Python lets you chain comparisons: `a <= x < b`.

## Task 3: `write_jsonl`

**What:** write a list of dicts to a path as JSON Lines: one `json.dumps` per row, one newline after each, dates serialised with `default=str`, the file opened with `encoding="utf-8"`.

**Why:** JSON Lines is the audit and interchange format used across the programme's modules. One object per line is what makes a file streamable: a reader can process line 1 before line 40,000 exists.

**Acceptance:** the file has one line per row, each line `json.loads`-parses back, a `date` comes back as the string `"2026-01-05"`, `München` survives the round trip, and the file ends with exactly one newline after the last row (`WriteJsonlTest`).

**Hints:**
- `json.dumps(row)` fails on a `date` with `TypeError: Object of type date is not JSON serializable`. `default=str` tells it what to do with anything it does not know.
- Open the file with `"w"` inside a `with` block, so it is closed even if a row fails.

## Task 4: Synthesis, `clean_and_split`

**What:** wire Tasks 1 and 2 together over a real CSV. Read it with `csv.DictReader` and parse every row. A row that fails to parse becomes a `(raw_row, reason)` reject. Parsed rows are then filtered by the `[start, end)` window; rows outside the window are dropped silently (they are not errors). Return `(clean_rows, rejects)`.

**Why:** this is the dead-letter pattern from the live coding, now driven from a file and with windowing added. One bad row out of 40,000 must not lose the night's data: keep going, and keep what you need to fix the row afterwards.

**Acceptance:** for the sample CSV with the window 2026-01-05 to 2026-01-10: exactly 5 clean rows (`t-001` to `t-005`) with typed values, exactly 3 rejects (`t-006`, `t-007`, `t-008`) whose reasons name the bad fields and whose raw rows are kept unchanged, and `t-009` and `t-010` in neither list (`CleanAndSplitTest`).

**Hints:**
- Reuse your own functions: `parse_row` inside the loop, `in_window` on the result.
- Open the CSV with `newline=""` and `encoding="utf-8"`, as `make_trips_csv` does.
- `str(exc)` is the message of a caught exception, which is your reason.
- Catch `ValueError` only. `except Exception: pass` would hide your own bugs as "rejects".

## Handing in

Commit and push to this repository. Each push runs the autograder; the result appears in Coder in 90 Classroom.

```bash
git add exercise.py
git commit -m "feat: implement parsing labs"
git push
```

---

## Background: errors in one page

```python
try:
    fare = float(text)            # the work that may fail
except ValueError as exc:         # only the error you expect and can handle
    rejects.append((row, str(exc)))
else:
    clean.append(fare)            # runs only when try raised nothing
finally:
    print("done")                 # runs on every exit path
```

Things worth remembering for today:

- `finally` runs **always**: after a normal finish, a `return`, a caught exception and an uncaught one. It is where files and connections get closed. `with open(...) as handle:` does the same for a file without you writing the `finally`.
- Catch the **specific** exception. `except Exception: pass` swallows everything, including your own typos, and the failure resurfaces later somewhere that makes no sense (often as a `NameError`).
- `raise NewError("...") from exc` keeps the original error attached, so the traceback shows both.
- The common ones today: `ValueError` (right type, bad value: `float("twelve")`, `int("")`, month 13), `KeyError` (missing dict key), `TypeError` (wrong type: `"14.50" * 1.5`), `FileNotFoundError`.
- `csv.DictReader` gives you one **dict per row**, keyed by the header row, and every value is a **string**, numbers and dates included. Converting is your job.
- Secrets never go in code. Read them from the environment: `os.environ["DB_PASSWORD"]` fails loudly when the variable is missing, `os.environ.get("LOG_LEVEL", "INFO")` falls back to a default. Environment values are always strings.

### Half-open windows

```text
[2026-01-05, 2026-01-10)   includes the 5th, 6th, 7th, 8th and 9th; not the 10th
[2026-01-10, 2026-01-15)   the next window starts exactly where this one ended
```

### JSON Lines

```text
{"trip_id": "t-001", "city": "Berlin", "date": "2026-01-05", "minutes": 11, "fare": 14.5}
{"trip_id": "t-002", "city": "Hamburg", "date": "2026-01-06", "minutes": 25, "fare": 27.25}
```

One complete JSON object per line, no surrounding list, no commas between lines.

## Further reading

**Official Python documentation**

- Tutorial, errors and exceptions (`try`, `except`, `else`, `finally`, `raise ... from`): https://docs.python.org/3/tutorial/errors.html
- Built-in exceptions and their hierarchy: https://docs.python.org/3/library/exceptions.html
- `csv` module, including `DictReader` and `DictWriter`: https://docs.python.org/3/library/csv.html
- `json` module, including `dumps` and its `default` argument: https://docs.python.org/3/library/json.html
- `datetime.date.fromisoformat`: https://docs.python.org/3/library/datetime.html#datetime.date.fromisoformat
- `os.environ`: https://docs.python.org/3/library/os.html#os.environ
- `logging` HOWTO: https://docs.python.org/3/howto/logging.html
- `unittest`, including `assertRaisesRegex`: https://docs.python.org/3/library/unittest.html

**Tutorials (Real Python)**

- Exceptions: https://realpython.com/python-exceptions/
- Understanding tracebacks: https://realpython.com/python-traceback/
- Reading and writing CSV files: https://realpython.com/python-csv/
- Working with JSON: https://realpython.com/python-json/
- Context managers and `with`: https://realpython.com/python-with-statement/

**Going deeper**

- JSON Lines format: https://jsonlines.org/
- The Twelve-Factor App, config in the environment: https://12factor.net/config

## Self-check before you push

- [ ] `python3 -m unittest -v` ends with `OK` and `Ran 14 tests`.
- [ ] `test_exercise.py` is unchanged (`git diff test_exercise.py` prints nothing).
- [ ] `clean_and_split` calls `parse_row` and `in_window` instead of repeating their work.
- [ ] Your code has no bare `except:` and no `except Exception: pass`.
- [ ] You can explain why `t-009` is in neither list, and why that is not an error.

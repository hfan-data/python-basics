**English** | [Deutsch](README_DE.md)

# Day 5 individual tasks: design, evaluate, trace, deliver alone

This morning your group designed a city report pipeline, then traced, debugged and evaluated a
broken copy at three stations. Here you do each of those steps alone on new data: Dresden,
Leipzig and Bremen. Every task names the morning activity it continues; your group's design,
trace table and bug log are the first places to look when you are stuck.

Do these after the readiness check, as follow-up before the next module.

You implement four tasks in `exercise.py` until `python3 -m unittest -v` runs green. The tests
in `test_exercise.py` are pre-written and complete: make them pass, never edit them.

```bash
python3 -m unittest -v
```

Every push is graded by Coder in 90: your score is the number of the 13 tests that pass.

`ROWS` at the top of `exercise.py` holds eight rows, every value a string exactly as
`csv.DictReader` delivers it. Four rows are unusable and the city names are messy.

## Reading the test output

- **`ERROR`** with `NotImplementedError: Task N` only means the task is still a stub.
- **`FAIL`**: your code ran but returned the wrong value; the `AssertionError` shows expected
  and actual side by side.
- Read a traceback from the bottom up: last line for **what**, first frame in `exercise.py` for
  **where**.
- One test class at a time: `python3 -m unittest -v test_exercise.FindRejectsTest`

## Task 1: `find_rejects`

**From the morning:** Activity 1, part 1 (which rows must be rejected, and why).

**What:** list every unusable row as `(trip_id, reason)`, in input order. The three reasons and
the order to check them are in the docstring; report only the first that applies.

**Acceptance:** exactly `r-04` (fare not a number), `r-05` (empty city), `r-06` and `r-08`
(fare not positive); a row with an empty city and a bad fare reports only `"empty city"`; no
rows gives `[]` (`FindRejectsTest`).

## Task 2: `city_totals`

**From the morning:** station 3 (evaluate someone else's code).

**What:** the docstring shows the colleague's function from station 3. Write the version that
works: skip what Task 1 rejects, clean the city, round, and give the same answer however often
it is called.

**Acceptance:** `{"Dresden": 28.0, "Leipzig": 22.1, "Bremen": 15.0}`; two calls give equal
results; no rows gives `{}`; `ROWS` is unchanged (`CityTotalsTest`).

## Task 3: `totals_with_trace`

**From the morning:** station 1 (trace by hand).

**What:** return the totals together with the trace table your group drew on paper: one
snapshot of the whole totals dict after each usable row.

**Acceptance:** four snapshots, from `{"Dresden": 18.4}` to all three cities; each snapshot is
its own dict, so a later row cannot change an earlier one; no rows gives `({}, [])`
(`TotalsWithTraceTest`).

**Watch out:** appending the same dict four times gives four views of the final totals, not a
trace. If your snapshots all look alike, that is what happened.

## Task 4: Synthesis, `write_summary`

**From the morning:** Activity 1, part 3 (the build) and station 2 (the bugs you fixed).

**What:** write `city,total` as a CSV file, highest total first, ties alphabetical, totals with
two decimals, replacing any earlier content. Return how many cities were written and how many
rows were skipped.

**Why:** the morning's report was a text file built as a group. This one is a CSV that another
program will read, built alone from your own Tasks 1 and 2, and it must survive a rerun: the
four-step shape every pipeline in Modules 4 and 5 has.

**Acceptance:** returns `(3, 4)` and writes the header plus Dresden, Leipzig, Bremen; equal
totals come out alphabetically; running twice leaves an identical file (`WriteSummaryTest`).

## Handing in

```bash
git add exercise.py
git commit -m "feat: implement day 5 individual tasks"
git push
```

## Self-check before you push

- [ ] `python3 -m unittest -v` ends with `OK` and `Ran 13 tests`.
- [ ] `test_exercise.py` is unchanged (`git diff test_exercise.py` prints nothing).
- [ ] `write_summary` uses your Task 1 and Task 2 work instead of repeating it.
- [ ] You can list every problem in the colleague's code and say which line of yours fixes it.

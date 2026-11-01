**English** | [Deutsch](README_DE.md)

# Day 2 exercises: aggregation labs

**Watch first:** [the video for this lab](https://trytikkr.com/w/xu32VyHlyN2c9-q_bKMl8g)

**Before you start:** pass the readiness quiz for this assignment in Coder in 90 Classroom. You need 50% to start.

You implement four functions in `exercise.py` until `python3 -m unittest -v` runs green. The tests in `test_exercise.py` are pre-written and complete. Your job is to make them pass, never to edit them.

Run from this folder:

```bash
python3 -m unittest -v
```

Every push is graded by Coder in 90: your score is the number of the 9 tests that pass. There is no fixed deadline for this lab; push whenever you are ready, and as often as you like.

`TRIPS` at the top of `exercise.py` is the same twelve-trip log used in the live coding. Note that `"berlin"` (lowercase) and `"Berlin"` are distinct cities in this data. Case sensitivity is a real grouping bug, and today you see it from the data side: do **not** clean the names in this lab, the tests expect both.

## Reading the test output

- **One line per test**, ending in `ok`, `FAIL` or `ERROR`. Work through them one task at a time.
- **`ERROR`**: your code crashed. At the start every test shows `NotImplementedError: Task N: ...`; that only means the task is still a stub.
- **`FAIL`**: your code ran but returned the wrong value. The `AssertionError` lines show what the test expected next to what your function returned; the difference is your next fix.
- To rerun one test class while you work on one task: `python3 -m unittest -v test_exercise.CityFaresTest`
- `OK` on the last line means every test passed: the lab is done.

## Task 1: `unique_cities`

**What:** every city that appears in the trips, as a sorted list, each appearing once.

**Why:** expansion lists (loop over every distinct value) are a daily pipeline need.

**Acceptance:** the exact five-element list for `TRIPS` (lowercase `berlin` sorts last), and an empty list for no trips (`UniqueCitiesTest`).

**Hint:** which container removes duplicates for you? Which built-in always gives you back a list, whatever you hand it?

## Task 2: `city_fares`

**What:** a dict mapping each city to the list of its fares, in encounter order.

**Why:** group-by is the backbone of every aggregation. This is the live coding's `fares_by_city`, and the tests pin it down.

**Acceptance:** the exact dict for `TRIPS`, including the list lengths per city, and Berlin's fares in the order they appear (`CityFaresTest`).

**Hint:** `d.setdefault(key, [])` returns the list already stored under `key`, or stores and returns a new empty one. You can call `.append(...)` on what it returns.

## Task 3: `averages`

**What:** given a city-to-fares dict (the shape Task 2 produces), return city-to-average fare, each average rounded to 2 decimals, built as a dict comprehension over `.items()`.

**Why:** "reshape a dict into another dict" is half of what pipeline code does.

**Acceptance:** the exact values for the Task 2 result of `TRIPS`, and a city with a single trip (`AveragesTest`).

**Hint:** an average is `sum(...) / len(...)`. Round the average, not the fares.

## Task 4: Synthesis, `top_cities`

**What:** the `n` best cities by average fare, as `(city, average)` tuples, best first. Ties are broken alphabetically by city name. An `n` larger than the number of cities returns all of them.

**Why:** this chains Task 2, Task 3 and sorting with a two-part key (`-average`, then name). The lecture ranked with a single key and never handled ties. Two-part keys are how real reports stay deterministic.

**Acceptance:** the exact top 2 for `TRIPS`, the alphabetical tie-break on a constructed all-equal input, and the oversized-`n` case (`TopCitiesTest`).

**Hints:**
- Reuse your own functions; Task 4 needs no new loop over the trips.
- `dict.items()` already gives you `(key, value)` pairs, the exact shape the test wants.
- A `key=` function can return a tuple. Python compares tuples element by element: the first elements decide, and only a tie looks at the second.
- Slicing never raises for a stop past the end: `[1, 2, 3][:99]` is `[1, 2, 3]`.

## Handing in

Commit and push to this repository. Each push runs the autograder; the result appears in Coder in 90 Classroom.

```bash
git add exercise.py
git commit -m "feat: implement aggregation labs"
git push
```

---

## Background: the four containers in one page

| | `list` | `tuple` | `dict` | `set` |
|---|---|---|---|---|
| Literal | `[1, 2]` | `(1, 2)` | `{"a": 1}` | `{1, 2}` |
| Ordered | yes | yes | insertion order (since 3.7) | no |
| Mutable | yes | no | yes | yes |
| Duplicates | allowed | allowed | keys unique | never |
| Lookup `x in c` | scans every item, O(n) | O(n) | by key, O(1) on average | O(1) on average |
| Typical use | a sequence that grows | a fixed-shape record, a dict key | lookup by key, group-by | deduplicate, membership |

Things worth remembering for today:

- `{}` is an empty **dict**, not an empty set. An empty set is `set()`.
- `sorted(anything)` always returns a new **list**. `list.sort()` sorts in place and returns `None`.
- Looping over a dict gives you its **keys**. Use `.items()` for `(key, value)` pairs and `.values()` for the values alone.
- `d["missing"]` raises `KeyError`; `d.get("missing")` returns `None` (or the default you pass as the second argument).
- Never add to or remove from a list while you loop over it; build a new list instead (a comprehension).
- Strings sort by code point: all uppercase letters come before all lowercase ones, which is why `"berlin"` lands after `"München"`.
- `round(x, 2)` gives a float that *prints* with at most two decimals. Floats are binary, so `0.1 + 0.2` is `0.30000000000000004`; compare rounded values, as the tests do.

### Comprehensions, the three shapes

```python
[expr for item in items if condition]          # list
{expr for item in items if condition}          # set
{key: value for key, value in d.items()}       # dict
```

The `if` filter goes at the end. Read it aloud as "give me `expr`, for each `item` in `items`, if `condition`".

### Sorting with a key

```python
pairs = [("Köln", 28.1), ("Hamburg", 22.3), ("Bonn", 28.1)]
sorted(pairs, key=lambda pair: pair[1])                 # by value, lowest first
sorted(pairs, key=lambda pair: pair[1], reverse=True)   # by value, highest first
sorted(pairs, key=lambda pair: (-pair[1], pair[0]))     # highest value first, then by name
```

Negating a number turns "highest first" into "lowest first", so one ascending sort can order by one field descending and another ascending.

## Further reading

**Official Python documentation**

- Tutorial, data structures (lists, tuples, sets, dicts, comprehensions, looping techniques): https://docs.python.org/3/tutorial/datastructures.html
- Built-in types reference (every method on list, tuple, set and dict): https://docs.python.org/3/library/stdtypes.html
- `dict.setdefault` and `dict.get`: https://docs.python.org/3/library/stdtypes.html#dict.setdefault
- Sorting HOW TO (key functions, `reverse`, stability and multi-key sorts): https://docs.python.org/3/howto/sorting.html
- Built-in functions (`sorted`, `sum`, `len`, `round`, `min`, `max`): https://docs.python.org/3/library/functions.html
- Floating-point arithmetic, issues and limitations (why `round` matters): https://docs.python.org/3/tutorial/floatingpoint.html
- `collections.defaultdict` and `collections.Counter`, the library versions of today's group-by and count: https://docs.python.org/3/library/collections.html
- `statistics.mean`: https://docs.python.org/3/library/statistics.html
- `unittest`, the framework these tests are written in: https://docs.python.org/3/library/unittest.html

**Tutorials (Real Python)**

- Lists and tuples: https://realpython.com/python-lists-tuples/
- Dictionaries: https://realpython.com/python-dicts/
- Iterating through a dictionary: https://realpython.com/iterate-through-dictionary-python/
- Sets: https://realpython.com/python-sets/
- List comprehensions: https://realpython.com/list-comprehension-python/
- Sorting: https://realpython.com/python-sort/
- `defaultdict`: https://realpython.com/python-defaultdict/
- Rounding numbers: https://realpython.com/python-rounding/

**See your code run**

- Python Tutor draws every list and dict as your code changes it, step by step. Paste the "spot the bug" loop from this morning's warm-up and watch the skipped item: https://pythontutor.com/visualize.html

**Going deeper**

- Time complexity of operations on list, set and dict (why `in` on a set is fast): https://wiki.python.org/moin/TimeComplexity

## Self-check before you push

- [ ] `python3 -m unittest -v` ends with `OK` and `Ran 9 tests`.
- [ ] `test_exercise.py` is unchanged (`git diff test_exercise.py` prints nothing).
- [ ] `top_cities` calls `city_fares` and `averages` instead of repeating their work.
- [ ] You can explain why `"berlin"` is its own row, and what one line would merge it into `"Berlin"`.

**English** | [Deutsch](README_DE.md)

# Day 4 exercises: function labs

This afternoon you work alone. The morning was for talking it through in pairs and groups; now you show yourself you can do it without the group. When you are stuck, go back to the rules your group wrote for cards A–H and to the toolkit you built together before asking the instructor.

You implement four functions in `exercise.py` until `python3 -m unittest -v` runs green. The tests in `test_exercise.py` are pre-written and complete. Your job is to make them pass, never to edit them.

Run from this folder:

```bash
python3 -m unittest -v
```

Every push is graded by Coder in 90: your score is the number of the 15 tests that pass. Push whenever you are ready, and as often as you like.

`TRIPS` at the top of `exercise.py` is a six-trip log; two trips are invalid (`t-004` has negative minutes, `t-005` negative miles). The function signatures are given: today's work is the bodies.

## Reading the test output

- **One line per test**, ending in `ok`, `FAIL` or `ERROR`. Work through them one task at a time.
- **`ERROR`**: your code crashed. At the start every test shows `NotImplementedError: Task N: ...`; that only means the task is still a stub.
- **`FAIL`**: your code ran but returned the wrong value, or did not raise the error the test expected. The `AssertionError` lines show what the test expected next to what your function did.
- Read a traceback from the bottom up: the last line says **what** went wrong, then walk up to the first frame in `exercise.py` to find **where**.
- To rerun one test class while you work on one task: `python3 -m unittest -v test_exercise.FareTest`
- `OK` on the last line means every test passed: the lab is done.

## Task 1: `fare`

**What:** compute one trip's fare from minutes and miles, with base and rates that have defaults and can be overridden by name, and a `night` option that multiplies the whole fare by 1.5. Round once, at the end.

**Why:** almost every function in the programme has a few required inputs and several named options with sensible defaults. This is that shape in its simplest form.

**Acceptance:** default pricing gives `12.50` for 11 minutes / 3.2 miles; `night=True` gives `18.75`; overriding `base` by name works; passing a rate by position raises `TypeError` (`FareTest`).

**Hints:**
- The `*` in the signature already makes the options keyword-only. You do not need any code for the `TypeError` test: Python raises it for you.
- Round only the final result. Rounding each part first can change the last cent.

## Task 2: `split_valid`

**What:** split trips into the valid ones and the ids of the invalid ones, and return both.

**Why:** "good rows here, rejected ids there" is how every cleaning step in the programme reports its result. Returning a tuple and unpacking it at the call site is the standard way.

**Acceptance:** four valid trips and `["t-004", "t-005"]` rejected, both in input order; a trip with zero minutes and zero miles is valid; an empty list gives `([], [])` (`SplitValidTest`).

**Hint:** `return valid, rejected` returns one tuple; the caller writes `valid, rejected = split_valid(trips)`.

## Task 3: `make_trip`

**What:** build a trip dict from two required values, an optional `tags` list, and any number of extra named values.

**Why:** `**kwargs` is how the frameworks in Modules 4 and 5 pass you context. The `tags` rule is the mutable-default trap from the warmup, avoided properly.

**Acceptance:** extra keyword arguments become keys; two trips built without tags never share a list; a `tags` list you pass in is copied, not reused (`MakeTripTest`).

**Hints:**
- Inside the function, `extra` is a plain dict.
- `list(tags)` makes a new list with the same items.
- Test for "not given" with `is None`.

## Task 4: Synthesis, `price_trips`

**What:** combine Tasks 1 and 2. Split the trips, price each valid one into a **new** dict that also carries its `fare`, forward any pricing options to `fare` unchanged, and return the priced trips, the rejected ids, and the total.

**Why:** passing options through one function into another, without changing the caller's data, is the combination the morning showed only in separate pieces.

**Acceptance:** default total `103.42`; with `night=True` the total is `155.14`; priced trips keep their other keys; `TRIPS` is unchanged after the call; an unknown option such as `discount=0.1` raises `TypeError` (`PriceTripsTest`).

**Hints:**
- Reuse your own functions: `split_valid` first, then `fare` for each valid trip.
- `**pricing` in the `def` collects the options; `**pricing` in the call to `fare` passes them on.
- `dict(trip)` is a new dict with the same keys. Change the copy, never `trip`.

## If you finish early

**Practice (more repetitions of today's ideas):**
- In the REPL, call `fare` five different ways (positional only, all by name, mixed). Before each call, predict the result on paper.
- Write `describe_trip(trip, *, currency="€")` that returns a one-line f-string, and call it with and without `currency`.

**Stretch (harder, same ideas):**
- Add a keyword-only `minimum` option to `fare` (no fare is ever below it) without breaking any test.
- Write `price_by_city(trips, **pricing)` that returns `{city: total}` using `price_trips`, and put three `assert` lines under `if __name__ == "__main__":` that check it.
- Self-review: reread your own `price_trips` as if a colleague wrote it, and write down one input that would break it. Then check whether it does.

## Handing in

Commit and push to this repository. Each push runs the autograder; the result appears in Coder in 90 Classroom.

```bash
git add exercise.py
git commit -m "feat: implement function labs"
git push
```

---

## Background: functions in one page

```python
def fare(minutes, miles, *, base=2.50, night=False):   # required, then keyword-only with defaults
    ...

fare(11, 3.2)                  # positional: matched by order
fare(miles=3.2, minutes=11)    # keyword: matched by name, order does not matter
fare(11, 3.2, night=True)      # options after * must be named
fare(11, 3.2, True)            # TypeError: takes 2 positional arguments but 3 were given
```

Things worth remembering for today:

- Parameters with defaults come after those without, or the file does not load (`SyntaxError`).
- `return a, b` returns **one tuple**. Unpack it with as many names as values: `low, high = low_high(fares)`.
- Never use a list or dict as a default value: it is created once and shared by every call. Use `None` and `if tags is None: tags = []`.
- In a `def`, `**extra` collects extra named arguments into a dict. In a call, `**options` spreads a dict into named arguments. A misspelt name still fails with `TypeError`.
- A variable assigned inside a function is local to it. Read module-level constants freely; return results instead of changing module-level variables.
- `trip["fare"] = ...` inside a function changes the caller's dict too. Build a new dict and return it.
- Every `.py` file is a module: `from exercise import fare` is exactly how the tests reach your code. Code under `if __name__ == "__main__":` does not run on import.

## Further reading

**Official Python documentation**

- Tutorial, defining functions (defaults, keyword arguments, special parameters, `*args`/`**kwargs`): https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
- Tutorial, modules and `__name__`: https://docs.python.org/3/tutorial/modules.html
- Tutorial, tuples and sequence unpacking: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
- `unittest`: https://docs.python.org/3/library/unittest.html

**Tutorials (Real Python)**

- Defining your own functions: https://realpython.com/defining-your-own-python-function/
- `*args` and `**kwargs`: https://realpython.com/python-kwargs-and-args/
- Scope and the LEGB rule: https://realpython.com/python-scope-legb-rule/
- Modules and packages: https://realpython.com/python-modules-packages/

## Self-check before you push

- [ ] `python3 -m unittest -v` ends with `OK` and `Ran 15 tests`.
- [ ] `test_exercise.py` is unchanged (`git diff test_exercise.py` prints nothing).
- [ ] `price_trips` calls `split_valid` and `fare` instead of repeating their work.
- [ ] No function in your file has a list or dict as a default value.
- [ ] You can explain why `TRIPS` is the same after `price_trips(TRIPS)` as before.

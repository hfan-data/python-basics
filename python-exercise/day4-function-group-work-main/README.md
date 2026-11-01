**English** | [Deutsch](README_DE.md)

# Day 4 morning: group work guide

This morning has no slides and no live coding. You learn today's ideas by predicting, running
and explaining code with other people. The afternoon lab (your individual `day4-function-labs`
repository) is individual; what you work out together this morning is what you take into it.

| Time | What | Who with |
|------|------|----------|
| 09:00–09:20 | Warmup questions | Your partner, then the whole room |
| 09:20–10:00 | Activity 1, part 1: cards A–H | Your partner |
| 10:00–10:15 | Activity 1, part 2: agree one rule per card | Your pair plus one other pair |
| 10:15–10:30 | Debrief | Whole room |
| 10:30–10:45 | Break | |
| 10:45–11:30 | Activity 2: rebuild Day 1's fare report as a toolkit | Your group of 3–4 |
| 11:30–11:45 | Share-out | Whole room |

## How we work together

- **Predict before you run.** Everyone writes a prediction on paper first. "I do not know,
  because ..." is a valid prediction; a silent shrug is not.
- **One keyboard, rotating.** The **driver** types only what the group decides. The
  **navigators** decide what to type and explain why. Change driver when the guide says so,
  even in the middle of a function.
- **The person who knows explains; the person who does not types.** If you already know the
  answer, your job is to make your partner able to say it, not to say it for them.
- **Every voice once.** Before the group moves on, everyone can explain the result in one
  sentence. If someone cannot, you are not done.
- **Wrong predictions are the point.** A wrong prediction tells you exactly what to learn. Say
  it out loud; do not hide it.
- **Stuck for five minutes?** The driver reads the last line of the traceback aloud. Ask: which
  card does this match? Still stuck: raise a hand. Do not look up the answer online.

---

## Activity 1: predict, run, explain (pairs, then groups of 4)

For every card:

1. **Predict.** Both of you write down what will happen, before anyone types: an output, an
   error type, or "I do not know, because ...".
2. **Run.** One of you types the code into the REPL (`python3`) or a scratch file. Swap typists
   on every card.
3. **Explain.** If a prediction was wrong, keep talking until both of you can say why. Write one
   rule, in one sentence, that would have given you the right prediction.

Cards are independent: if you are stuck on one, move on and come back. Aim for about five
minutes per card.

Keep a rule sheet like this:

| Card | Our prediction | What happened | Our rule (one sentence) |
|------|----------------|---------------|-------------------------|
| A | | | |

**Part 2 (10:00).** Join another pair. Compare your rules card by card and agree on one shared
sentence for each. Where you disagree, run the code again together. Pick one person to read your
group's rules in the debrief.

### Card A: matching arguments to parameters

```python
def fare(minutes, miles, base=2.50):
    return base + minutes * 0.40 + miles * 1.75

print(fare(10, 2))
print(fare(miles=2, minutes=10))
print(fare(2, 10))
print(fare(10, 2, base=3.0))
```

### Card B: where defaults may go

Predict whether this file loads at all. Then find two different ways to fix it.

```python
def fare(minutes=0, miles):
    return 2.50 + minutes * 0.40 + miles * 1.75
```

### Card C: the bare `*`

```python
def fare(minutes, miles, *, night=False):
    total = 2.50 + minutes * 0.40 + miles * 1.75
    return total * 1.5 if night else total

print(fare(10, 2, night=True))
print(fare(10, 2, True))
```

Discuss: who benefits from the `*`, the person writing the function or the person calling it?

### Card D: returning two values

```python
def low_high(fares):
    return min(fares), max(fares)

result = low_high([9.0, 27.25, 14.5])
print(result)
low, high = result
print(high - low)
low, high, middle = low_high([9.0, 27.25])
```

### Card E: a default that remembers

```python
def count_city(city, counts={}):
    counts[city] = counts.get(city, 0) + 1
    return counts

print(count_city("Berlin"))
print(count_city("Köln"))
```

Then rewrite `count_city` so every call that does not pass `counts` starts from an empty dict.

### Card F: collecting and passing on named arguments

```python
def describe(trip_id, **extra):
    return f"{trip_id} {extra}"

def fare(minutes, *, night=False):
    return minutes * 0.40 * (1.5 if night else 1)

print(describe("t-001", city="Berlin", night=True))
options = {"night": True}
print(fare(10, **options))
print(fare(10, **{"nite": True}))
```

Discuss: `**` appears in a `def` and in a call. What does it do in each place?

### Card G: who owns the dict?

```python
def add_fare(trip):
    trip["fare"] = 12.5
    return trip

trip = {"trip_id": "t-001"}
priced = add_fare(trip)
print(trip)
print(priced is trip)
```

Then rewrite `add_fare` so `trip` is the same after the call as before it.

### Card H: importing your own file

Create `tools.py`:

```python
def double(x):
    return x * 2

print("tools loaded")
```

From the same folder, predict and run:

```bash
python3 -c "from tools import double; print(double(4))"
```

Then put the `print` under `if __name__ == "__main__":` and run the same command again. Finally
run it from a different folder and read the error.

---

## Activity 2: rebuild Day 1's fare report as a toolkit (groups of 3–4)

**Goal:** turn Day 1's `fare_report.py` into `fare_tools.py`, a file of small functions that
another file can import, using every rule from Activity 1. One laptop per group; change driver
every ten minutes.

**Start:** copy `fare_report.py` from this repository (Day 1's fare report) to `fare_tools.py`
and run it, so you know what working looks like.

The instructor calls the times.

1. **List what is hard-coded (5 min, on paper).** What would a colleague have to edit the file
   to change? Which part only prints and cannot be reused?
2. **Agree the signatures before any bodies (10 min, on paper).** Write the name, the parameters
   and what each function returns:
   - `fare_estimate`: rates have defaults and can only be changed by name; a `night` option
     multiplies the fare by 1.5
   - `split_trips`: returns the valid trips and the ids of the invalid ones
   - `price_trip`: returns a new dict with a `fare` key and forwards any pricing options to
     `fare_estimate`
   - `summarise`: returns count, total and average of the fares; an empty list must not crash
3. **Build one function at a time (25 min).** Write the body, try it in the REPL, then move on.
   You are on track when:
   - `fare_estimate(11, 3.2)` gives `12.5`, `fare_estimate(11, 3.2, night=True)` gives
     `18.75`, and `fare_estimate(11, 3.2, True)` is a `TypeError`
   - `split_trips(TRIPS)` gives four valid trips and `['t-005']`
   - after `price_trip(TRIPS[0], night=True)`, `TRIPS[0]` has no `fare` key
   - `summarise([])` gives `(0, 0.0, 0.0)`
4. **Prove it imports (5 min).** Rewrite `main()` with the new functions and keep it under the
   `__name__` guard. From a second terminal, in the same folder, run
   `python3 -c "from fare_tools import fare_estimate; print(fare_estimate(11, 3.2, night=True))"`.
   Only `18.75` should print.

**Finished early?** Add a keyword-only `minimum` option to `fare_estimate`: no fare is ever
below it.

**Share-out (11:30).** The instructor gives your group one of these questions. Prepare all four,
with your code on screen:

- Which signature did you change after you started typing, and why?
- Show `price_trip`: how do you know the input is not changed?
- What did `summarise([])` do before you handled it?
- Where would a `**kwargs` parameter be the wrong choice in your file?

## Before lunch

Keep your rule sheet and your group's `fare_tools.py`. This afternoon you work alone, and these
are the first places to look when you are stuck.

# Day 4 Group Work Notes

[中文](group_work_notes.md) | **English** | [Deutsch](group_work_notes_DE.md)

These notes contain observed code results and reference explanations. Individual predictions,
group discussions and role rotation during class still need to be completed in person.

## Activity 1: Rules for Cards A–H

| Card | Actual result | Rule in one sentence |
| --- | --- | --- |
| A | Prints `10.0`, `10.0`, `20.8`, `10.5`, in that order | Positional arguments bind in order, keyword arguments bind by name, and omitted arguments use their defaults. |
| B | Raises `SyntaxError` at definition time; the file cannot load | A required positional parameter cannot follow a positional parameter with a default value. |
| C | Prints `15.0`, then the second call raises `TypeError` | Parameters after a bare `*` must be passed by name, making options explicit for callers. |
| D | Prints `(9.0, 27.25)` and `18.25`, then raises `ValueError` | Multiple return values form a tuple, and the number of unpacking targets must match. |
| E | Prints `{'Berlin': 1}`, then `{'Berlin': 1, 'Köln': 1}` | Default values are created when the function is defined, so mutable defaults are shared across calls. |
| F | Prints `t-001 {'city': 'Berlin', 'night': True}` and `6.0`, then raises `TypeError` | In a definition, `**extra` collects keyword arguments; in a call, `**options` unpacks a dictionary, and misspelled parameter names still cause an error. |
| G | Prints `{'trip_id': 't-001', 'fare': 12.5}` and `True` | A parameter refers to the same dictionary, so in-place changes affect the caller; create a copy to avoid this. |
| H | Before the change, prints `tools loaded` and `8`; with the guard, prints only `8` | The first import executes top-level module statements; code inside the main guard runs only when the file is executed directly. |

Two fixes for B (after reordering parameters, positional calls must use the new order):

```python
def fare(miles, minutes=0):
    return 2.50 + minutes * 0.40 + miles * 1.75

# Alternatively, make the required miles parameter keyword-only: fare(miles=2)
def fare(minutes=0, *, miles):
    return 2.50 + minutes * 0.40 + miles * 1.75
```

Fixes for E and G:

```python
def count_city(city, counts=None):
    if counts is None:
        counts = {}
    counts[city] = counts.get(city, 0) + 1
    return counts


def add_fare(trip):
    return {**trip, "fare": 12.5}
```

H: Running `python3 tools.py` directly prints `tools loaded`. Running
`python3 -c "from tools import double"` from another directory raises `ModuleNotFoundError`
if the module directory is absent from Python's search path. Whether the import succeeds
depends on that search path.

## Activity 2: Toolkit Design

The original program hard-coded rates, sample trips and output formatting. It only printed
results, so other files could not directly reuse priced trips or summary results.

| Function | Input | Return value |
| --- | --- | --- |
| `fare_estimate` | Minutes and miles; keyword-only `base`, `per_minute`, `per_mile`, `night`, `minimum` | Fare rounded to two decimal places; applies the night multiplier first, then the minimum fare |
| `split_trips` | A list of trip dictionaries | `(valid trips, invalid trip IDs)` |
| `price_trip` | One trip and keyword pricing options | A new dictionary containing `fare`; leaves the original dictionary unchanged |
| `summarise` | A list of numeric fares | `(count, total, average)`; returns `(0, 0.0, 0.0)` for an empty list |

In the sample, t-005 has negative minutes, leaving four valid trips. Their fares are 12.50,
25.10, 46.50 and 19.00. The total is 103.10 and the average is 25.77, following Python's
`round` result for these floating-point values.

Run and check from this directory:

```bash
python3 fare_tools.py
python3 -c "from fare_tools import fare_estimate; print(fare_estimate(11, 3.2, night=True))"
python3 -m unittest discover -v
```

The second command prints only `18.75`.

## Share-out: Reference Answers

- The existing `fare_estimate` only supported the `night` option. Keyword rate options and `minimum` now let callers configure pricing without editing global constants.
- `price_trip` uses dictionary unpacking to create a new dictionary and adds only a top-level `fare` key, leaving the input unchanged. A shallow copy is sufficient here because no nested objects are modified.
- Without handling an empty list, calculating the average would divide by zero. When the count is zero, the function now returns an average of `0.0`.
- Replacing the explicit parameters of `fare_estimate` with arbitrary `**kwargs` would make its options unclear. As a forwarding function, `price_trip` can collect pricing options; unknown options still cause `fare_estimate` to raise `TypeError`.

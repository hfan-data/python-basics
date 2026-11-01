**English** | [Deutsch](README_DE.md)

# Day 5 morning: group work guide

No slides, no live coding, and no new syntax today. This morning your group designs and builds
the smallest real data pipeline, then reads, traces and debugs a broken copy of it. The
afternoon is individual: the mini-capstone lab (your individual `day5-pipeline-labs`
repository), then the readiness check.

| Time | What | Who with |
|------|------|----------|
| 09:00–09:20 | Warmup questions | Your partner, then the whole room |
| 09:20–09:35 | Activity 1, part 1: design the pipeline on paper | Your group of 3–4 |
| 09:35–09:45 | Activity 1, part 2: swap designs | Your group plus one other group |
| 09:45–10:20 | Activity 1, part 3: build it | Your group, one laptop |
| 10:20–10:30 | Debrief: run it twice | Whole room |
| 10:30–10:45 | Break | |
| 10:45–11:30 | Activity 2: three stations, 15 min each | A new group of 3 |
| 11:30–11:45 | Debrief | Whole room |

## How we work together

- **Design before you type.** Function names, inputs and outputs go on paper first. A design
  you can explain is worth more than code you cannot.
- **One keyboard, rotating.** The **driver** types only what the group decides; the
  **navigators** decide and explain why. Change driver every ten minutes. Everyone drives at
  least once today, especially if you usually prefer to watch: the readiness check this
  afternoon is done alone.
- **The person who knows explains; the person who does not types.**
- **Every voice once.** Before the group moves on, everyone can explain what the code just did.
- **Change code only when you can say what is wrong.** Guessing and retrying is not debugging.
- **Stuck for five minutes?** The driver reads the last line of the traceback aloud, then the
  group prints the suspect value. Still stuck: raise a hand. Do not look up the answer online.

---

## Activity 1: design, then build, a city report pipeline (groups of 3–4)

**The task.** A CSV file of taxi trips comes in, and some rows are broken. Produce `report.txt`:
one line per city with its total fare (highest first, ties alphabetical), a `TOTAL` line, and a
count of skipped rows. The file must be the same however many times the script runs.

Input (`trips.csv`):

```
trip_id,city,fare
t-001,Berlin,14.50
t-002, hamburg ,27.25
t-003,BERLIN,11.05
t-004,München,abc
t-005,Köln,19.00
t-006,Hamburg,-4.00
t-007,berlin,31.40
t-008,,12.00
```

Expected `report.txt`:

```
Berlin       56.95
Hamburg      27.25
Köln         19.00
TOTAL       103.20
skipped: 3
```

### Part 1: design on paper (15 min)

Answer as a group, before any code:

1. Which rows must be rejected, and for what reason each?
2. Which rows count as the same city? What has to happen to the city text?
3. Name the four steps: extract, validate, transform, load. Which lines of the input or output
   does each step touch?
4. List the functions you will write: name, input, output, and a one-sentence docstring. One job
   per function; the name says what it returns. Aim for four or five.

### Part 2: swap designs (10 min)

Join another group. Each group explains its function list in two minutes. Then ask the other
group, function by function:

- What does this function do with an empty input?
- What does it do with a broken row?
- What happens if the script runs twice?

Change your own design if their questions show a gap.

### Part 3: build (35 min)

One laptop, driver changes every ten minutes.

1. Write the sample rows as a list of dicts and write them to `trips.csv` with
   `csv.DictWriter` (Day 3), so every group has the same file.
2. Type all your function signatures with docstrings and `...` as the body.
3. Fill in one function at a time and try it in the REPL before moving on.
4. Done means your `report.txt` matches the expected output exactly. Then run the script a
   second time and look at the file again.

---

## Activity 2: three stations, trace, debug, evaluate (groups of 3)

Your group visits all three stations for 15 minutes each, starting where the instructor sends
you. At each station take one role and rotate between stations:

- **Writer:** writes the group's answers down.
- **Typist:** the only person at the keyboard.
- **Checker:** reads the station's questions aloud and checks every answer against them before
  the group moves on.

### Station 1: trace by hand

No laptop until the end. Use the printed `city_totals` and `format_report` your instructor
hands out, and feed them the valid trips from Activity 1, in file order.

1. Draw a table with one row per loop pass of `city_totals` and a column each for
   `trip["city"]`, `trip["fare"]` and the whole `totals` dict after that pass.
2. Write the `ranking` list that `format_report` builds, then the exact lines it returns.
3. Change one fare so that two cities tie. Which comes first now, and which part of the `key`
   decides it?

Only when the table is finished, check it on a laptop with `print(f"{totals=}")` inside the
loop.

### Station 2: debug

Copy `broken_city_report.py` from this repository into an empty folder and run it. It has four
bugs: one crashes, two give a wrong report, and one only shows when you run it twice. Delete
`trips.csv` and `report.txt` before each test run. For each bug, follow the debugging order
(read the traceback, print the suspect value, try the line alone in the REPL) and fill in one
row:

| Symptom (what you saw) | Where (file, line) | How you found it (traceback / print / REPL) | Fix |
|------------------------|--------------------|---------------------------------------------|-----|
| | | | |

Keep this bug log: it is useful this afternoon.

### Station 3: evaluate someone else's code

A colleague wrote the function below. Without running it, list every problem you can find, and
for each problem write the input that shows it. Then check your list in the REPL.

```python
def city_totals(rows, totals={}):
    for row in rows:
        city = row["city"].strip
        totals[city] = totals.get(city) + float(row["fare"])
    return totals
```

Then answer the three questions to ask of any function: what happens with an empty input? With
a malformed row? When it runs twice in the same program?

### Debrief (11:30)

Be ready to answer for the station your group started at:

- Station 1: what did your table show that you did not expect?
- Station 2: which bug took longest, and which step of the debugging order found it?
- Station 3: which problem in the colleague's code would do the most damage in production?

## Before lunch

Keep your group's pipeline, your trace table and your bug log. This afternoon's lab is the same
pipeline with one more level (per day), and you build it alone.

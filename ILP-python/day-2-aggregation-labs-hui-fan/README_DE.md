[English](README.md) | **Deutsch**

# Tag 2 Übungen: Aggregations-Labs

**Schau zuerst:** [das Video zu diesem Lab](https://trytikkr.com/w/xu32VyHlyN2c9-q_bKMl8g)

**Bevor du anfängst:** Bestehe das Readiness-Quiz zu dieser Aufgabe in Coder in 90 Classroom. Du brauchst 50 %, um anzufangen.

Du implementierst vier Funktionen in `exercise.py`, bis `python3 -m unittest -v` grün durchläuft. Die Tests in `test_exercise.py` sind fertig geschrieben und vollständig. Deine Aufgabe ist es, sie zum Bestehen zu bringen, niemals sie zu ändern.

Führe sie in diesem Ordner aus:

```bash
python3 -m unittest -v
```

Jeder Push wird von Coder in 90 bewertet: Deine Punktzahl ist die Anzahl der 9 Tests, die bestehen. Für dieses Lab gibt es keine feste Abgabefrist; pushe, wann du so weit bist, und so oft du willst.

`TRIPS` oben in `exercise.py` ist dasselbe Log mit zwölf Fahrten wie im Live-Coding. Beachte, dass `"berlin"` (kleingeschrieben) und `"Berlin"` in diesen Daten verschiedene Städte sind. Groß- und Kleinschreibung ist ein echter Gruppierungsfehler, und heute siehst du ihn von der Datenseite: Bereinige die Namen in diesem Lab **nicht**, die Tests erwarten beide.

## Die Testausgabe lesen

- **Eine Zeile pro Test**, am Ende steht `ok`, `FAIL` oder `ERROR`. Arbeite sie Aufgabe für Aufgabe ab.
- **`ERROR`**: Dein Code ist abgestürzt. Am Anfang zeigt jeder Test `NotImplementedError: Task N: ...`; das heißt nur, dass die Aufgabe noch ein Platzhalter ist.
- **`FAIL`**: Dein Code lief, hat aber den falschen Wert zurückgegeben. Die `AssertionError`-Zeilen zeigen, was der Test erwartet hat, neben dem, was deine Funktion zurückgegeben hat; der Unterschied ist dein nächster Fix.
- Um nur eine Testklasse erneut auszuführen, während du an einer Aufgabe arbeitest: `python3 -m unittest -v test_exercise.CityFaresTest`
- `OK` in der letzten Zeile heißt, dass alle Tests bestanden haben: Das Lab ist fertig.

## Aufgabe 1: `unique_cities`

**Was:** jede Stadt, die in den Fahrten vorkommt, als sortierte Liste, jede genau einmal.

**Warum:** Listen aller verschiedenen Werte (um über jeden davon zu iterieren) braucht eine Pipeline jeden Tag.

**Abnahme:** die exakte Liste mit fünf Elementen für `TRIPS` (das kleingeschriebene `berlin` steht am Ende) und eine leere Liste, wenn es keine Fahrten gibt (`UniqueCitiesTest`).

**Tipp:** Welcher Container entfernt Duplikate für dich? Welche eingebaute Funktion gibt immer eine Liste zurück, egal was du ihr gibst?

## Aufgabe 2: `city_fares`

**Was:** ein Dict, das jede Stadt auf die Liste ihrer Fahrpreise abbildet, in der Reihenfolge, in der sie vorkommen.

**Warum:** Group-by ist das Rückgrat jeder Aggregation. Das ist `fares_by_city` aus dem Live-Coding, und die Tests legen es genau fest.

**Abnahme:** das exakte Dict für `TRIPS`, einschließlich der Listenlängen pro Stadt, und die Berliner Fahrpreise in der Reihenfolge, in der sie vorkommen (`CityFaresTest`).

**Tipp:** `d.setdefault(key, [])` gibt die Liste zurück, die schon unter `key` gespeichert ist, oder speichert eine neue leere Liste und gibt diese zurück. Auf dem Ergebnis kannst du `.append(...)` aufrufen.

## Aufgabe 3: `averages`

**Was:** Bekommt ein Dict von Stadt zu Fahrpreisen (die Form, die Aufgabe 2 liefert) und gibt ein Dict von Stadt zu durchschnittlichem Fahrpreis zurück, jeder Durchschnitt auf 2 Nachkommastellen gerundet, gebaut als Dict-Comprehension über `.items()`.

**Warum:** „Ein Dict in ein anderes Dict umformen“ ist die Hälfte dessen, was Pipeline-Code tut.

**Abnahme:** die exakten Werte für das Ergebnis von Aufgabe 2 auf `TRIPS` und eine Stadt mit nur einer Fahrt (`AveragesTest`).

**Tipp:** Ein Durchschnitt ist `sum(...) / len(...)`. Runde den Durchschnitt, nicht die Fahrpreise.

## Aufgabe 4: Synthese, `top_cities`

**Was:** die `n` besten Städte nach durchschnittlichem Fahrpreis, als Tupel `(city, average)`, die beste zuerst. Bei Gleichstand entscheidet der Städtename alphabetisch. Ein `n`, das größer ist als die Anzahl der Städte, gibt alle zurück.

**Warum:** Das verkettet Aufgabe 2, Aufgabe 3 und das Sortieren mit einem zweiteiligen Schlüssel (`-average`, dann der Name). Die Vorlesung hat mit einem einzigen Schlüssel sortiert und Gleichstände nie behandelt. Zweiteilige Schlüssel sorgen dafür, dass echte Berichte deterministisch bleiben.

**Abnahme:** die exakten Top 2 für `TRIPS`, der alphabetische Tie-Break bei einer konstruierten Eingabe mit lauter gleichen Werten und der Fall mit zu großem `n` (`TopCitiesTest`).

**Tipps:**
- Verwende deine eigenen Funktionen wieder; Aufgabe 4 braucht keine neue Schleife über die Fahrten.
- `dict.items()` liefert schon Paare `(key, value)`, genau die Form, die der Test erwartet.
- Eine `key=`-Funktion darf ein Tupel zurückgeben. Python vergleicht Tupel Element für Element: Das erste Element entscheidet, und nur bei Gleichstand wird das zweite angeschaut.
- Slicing wirft nie einen Fehler, wenn das Ende hinter der Liste liegt: `[1, 2, 3][:99]` ist `[1, 2, 3]`.

## Abgabe

Committe und pushe in dieses Repository. Jeder Push startet den Autograder; das Ergebnis erscheint in Coder in 90 Classroom.

```bash
git add exercise.py
git commit -m "feat: implement aggregation labs"
git push
```

---

## Hintergrund: die vier Container auf einer Seite

| | `list` | `tuple` | `dict` | `set` |
|---|---|---|---|---|
| Literal | `[1, 2]` | `(1, 2)` | `{"a": 1}` | `{1, 2}` |
| Geordnet | ja | ja | Einfügereihenfolge (seit 3.7) | nein |
| Veränderbar | ja | nein | ja | ja |
| Duplikate | erlaubt | erlaubt | Keys eindeutig | nie |
| Suche `x in c` | prüft jedes Element, O(n) | O(n) | über den Key, im Mittel O(1) | im Mittel O(1) |
| Typischer Einsatz | eine Folge, die wächst | ein Datensatz mit fester Form, ein Dict-Key | Suche über einen Key, Group-by | Duplikate entfernen, Mitgliedschaft prüfen |

Was du dir für heute merken solltest:

- `{}` ist ein leeres **Dict**, kein leeres Set. Ein leeres Set ist `set()`.
- `sorted(irgendwas)` gibt immer eine neue **Liste** zurück. `list.sort()` sortiert an Ort und Stelle und gibt `None` zurück.
- Eine Schleife über ein Dict liefert seine **Keys**. Nimm `.items()` für Paare `(key, value)` und `.values()` nur für die Werte.
- `d["fehlt"]` wirft einen `KeyError`; `d.get("fehlt")` gibt `None` zurück (oder den Standardwert, den du als zweites Argument übergibst).
- Füge einer Liste nie Elemente hinzu oder entferne welche, während du über sie iterierst; baue stattdessen eine neue Liste (eine Comprehension).
- Strings werden nach Codepoint sortiert: Alle Großbuchstaben kommen vor allen Kleinbuchstaben, deshalb landet `"berlin"` hinter `"München"`.
- `round(x, 2)` liefert einen Float, der mit höchstens zwei Nachkommastellen *angezeigt* wird. Floats sind binär, deshalb ist `0.1 + 0.2` gleich `0.30000000000000004`; vergleiche gerundete Werte, so wie es die Tests tun.

### Comprehensions, die drei Formen

```python
[expr for item in items if condition]          # Liste
{expr for item in items if condition}          # Set
{key: value for key, value in d.items()}       # Dict
```

Der `if`-Filter steht am Ende. Lies es laut als „gib mir `expr`, für jedes `item` in `items`, falls `condition`“.

### Sortieren mit einem Schlüssel

```python
pairs = [("Köln", 28.1), ("Hamburg", 22.3), ("Bonn", 28.1)]
sorted(pairs, key=lambda pair: pair[1])                 # nach Wert, kleinster zuerst
sorted(pairs, key=lambda pair: pair[1], reverse=True)   # nach Wert, größter zuerst
sorted(pairs, key=lambda pair: (-pair[1], pair[0]))     # größter Wert zuerst, dann nach Name
```

Eine Zahl zu negieren macht aus „größter zuerst“ ein „kleinster zuerst“. So kann eine einzige aufsteigende Sortierung nach einem Feld absteigend und nach einem anderen aufsteigend ordnen.

## Weiterführende Quellen

**Offizielle Python-Dokumentation auf Deutsch**

- Tutorial, Datenstrukturen (Listen, Tupel, Sets, Dicts, Comprehensions, Schleifentechniken): https://docs.python.org/de/3/tutorial/datastructures.html
- Eingebaute Typen (jede Methode von list, tuple, set und dict): https://docs.python.org/de/3/library/stdtypes.html
- Eingebaute Funktionen (`sorted`, `sum`, `len`, `round`, `min`, `max`): https://docs.python.org/de/3/library/functions.html
- Sortieren, HOW TO (Key-Funktionen, `reverse`, Stabilität und Sortieren nach mehreren Schlüsseln): https://docs.python.org/de/3/howto/sorting.html
- Gleitkomma-Arithmetik, Probleme und Einschränkungen (warum `round` wichtig ist): https://docs.python.org/de/3/tutorial/floatingpoint.html

Nicht jede Seite ist schon vollständig übersetzt; was fehlt, steht dort auf Englisch.

**Offizielle Python-Dokumentation auf Englisch**

- `dict.setdefault` und `dict.get`: https://docs.python.org/3/library/stdtypes.html#dict.setdefault
- `collections.defaultdict` und `collections.Counter`, die Bibliotheksversionen des heutigen Group-by und Zählens: https://docs.python.org/3/library/collections.html
- `statistics.mean`: https://docs.python.org/3/library/statistics.html
- `unittest`, das Framework, in dem diese Tests geschrieben sind: https://docs.python.org/3/library/unittest.html

**Tutorials auf Deutsch (python-kurs.eu)**

- Sequentielle Datentypen (Listen, Tupel, Strings): https://www.python-kurs.eu/python3_sequentielle_datentypen.php
- Listen: https://www.python-kurs.eu/python3_listen.php
- Dictionaries: https://www.python-kurs.eu/python3_dictionaries.php
- List Comprehension: https://www.python-kurs.eu/python3_list_comprehension.php
- Lambda (für `key=` beim Sortieren): https://www.python-kurs.eu/python3_lambda.php
- Schleifen: https://www.python-kurs.eu/python3_schleifen.php

**Tutorials auf Englisch (Real Python)**

- Listen und Tupel: https://realpython.com/python-lists-tuples/
- Dictionaries: https://realpython.com/python-dicts/
- Über ein Dictionary iterieren: https://realpython.com/iterate-through-dictionary-python/
- Sets: https://realpython.com/python-sets/
- List Comprehensions: https://realpython.com/list-comprehension-python/
- Sortieren: https://realpython.com/python-sort/
- `defaultdict`: https://realpython.com/python-defaultdict/
- Zahlen runden: https://realpython.com/python-rounding/

**Deinem Code beim Laufen zusehen**

- Python Tutor zeichnet jede Liste und jedes Dict Schritt für Schritt, während dein Code sie verändert. Füge die Schleife aus „Finde den Fehler“ aus dem heutigen Warm-up ein und sieh zu, wie ein Element übersprungen wird: https://pythontutor.com/visualize.html

**Für Fortgeschrittene**

- Zeitkomplexität der Operationen auf list, set und dict (warum `in` auf einem Set schnell ist): https://wiki.python.org/moin/TimeComplexity

## Selbstcheck vor dem Push

- [ ] `python3 -m unittest -v` endet mit `OK` und `Ran 9 tests`.
- [ ] `test_exercise.py` ist unverändert (`git diff test_exercise.py` gibt nichts aus).
- [ ] `top_cities` ruft `city_fares` und `averages` auf, statt deren Arbeit zu wiederholen.
- [ ] Du kannst erklären, warum `"berlin"` eine eigene Zeile ist und mit welcher einen Zeile du es mit `"Berlin"` zusammenführen würdest.

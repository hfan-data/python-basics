[English](README.md) | **Deutsch**

# Tag 4 Übungen: Funktions-Labs

Heute Nachmittag arbeitest du allein. Der Vormittag war zum Durchsprechen in Paaren und Gruppen da; jetzt zeigst du dir selbst, dass du es ohne die Gruppe kannst. Wenn du festhängst, schau zuerst in die Regeln, die deine Gruppe zu den Karten A–H aufgeschrieben hat, und in das Toolkit, das ihr gemeinsam gebaut habt, bevor du die Lehrkraft fragst.

Du implementierst vier Funktionen in `exercise.py`, bis `python3 -m unittest -v` grün durchläuft. Die Tests in `test_exercise.py` sind fertig geschrieben und vollständig. Deine Aufgabe ist es, sie zum Bestehen zu bringen, niemals sie zu ändern.

Führe sie in diesem Ordner aus:

```bash
python3 -m unittest -v
```

Jeder Push wird von Coder in 90 bewertet: Deine Punktzahl ist die Anzahl der 15 Tests, die bestehen. Pushe, wann du so weit bist, und so oft du willst.

`TRIPS` oben in `exercise.py` ist ein Log mit sechs Fahrten; zwei davon sind ungültig (`t-004` hat negative Minuten, `t-005` negative Meilen). Die Funktionssignaturen sind vorgegeben: Deine Arbeit heute sind die Funktionsrümpfe.

## Die Testausgabe lesen

- **Eine Zeile pro Test**, die mit `ok`, `FAIL` oder `ERROR` endet. Arbeite sie Aufgabe für Aufgabe ab.
- **`ERROR`**: Dein Code ist abgestürzt. Am Anfang zeigt jeder Test `NotImplementedError: Task N: ...`; das heißt nur, dass die Aufgabe noch ein Stub ist.
- **`FAIL`**: Dein Code lief, hat aber den falschen Wert zurückgegeben oder den erwarteten Fehler nicht ausgelöst. Die `AssertionError`-Zeilen zeigen, was der Test erwartet hat, neben dem, was deine Funktion geliefert hat.
- Lies einen Traceback von unten nach oben: Die letzte Zeile sagt, **was** schiefging; geh dann nach oben bis zum ersten Frame in `exercise.py`, um zu finden, **wo**.
- Um eine Testklasse erneut auszuführen, während du an einer Aufgabe arbeitest: `python3 -m unittest -v test_exercise.FareTest`
- `OK` in der letzten Zeile heißt, alle Tests bestehen: Das Lab ist fertig.

## Aufgabe 1: `fare`

**Was:** Berechne den Fahrpreis einer Fahrt aus Minuten und Meilen, mit Grundpreis und Tarifen, die Standardwerte haben und per Name überschrieben werden können, und einer Option `night`, die den ganzen Fahrpreis mit 1,5 multipliziert. Runde einmal, ganz am Ende.

**Warum:** Fast jede Funktion im Programm hat ein paar Pflichteingaben und mehrere benannte Optionen mit sinnvollen Standardwerten. Das hier ist diese Form in ihrer einfachsten Gestalt.

**Abnahme:** Die Standardpreise ergeben `12.50` für 11 Minuten / 3,2 Meilen; `night=True` ergibt `18.75`; `base` per Name zu überschreiben funktioniert; einen Tarif per Position zu übergeben löst `TypeError` aus (`FareTest`).

**Hinweise:**
- Der `*` in der Signatur macht die Optionen bereits nur-per-Name. Für den `TypeError`-Test brauchst du keinen Code: Python löst ihn für dich aus.
- Runde nur das Endergebnis. Wenn du jeden Teil vorher rundest, kann sich der letzte Cent ändern.

## Aufgabe 2: `split_valid`

**Was:** Teile die Fahrten in die gültigen und die IDs der ungültigen auf und gib beides zurück.

**Warum:** „Gute Zeilen hierhin, abgelehnte IDs dorthin" ist die Art, wie jeder Bereinigungsschritt im Programm sein Ergebnis meldet. Ein Tupel zurückgeben und es beim Aufruf entpacken ist der Standardweg.

**Abnahme:** vier gültige Fahrten und `["t-004", "t-005"]` abgelehnt, beide in Eingabereihenfolge; eine Fahrt mit null Minuten und null Meilen ist gültig; eine leere Liste ergibt `([], [])` (`SplitValidTest`).

**Hinweis:** `return valid, rejected` gibt ein Tupel zurück; der Aufrufer schreibt `valid, rejected = split_valid(trips)`.

## Aufgabe 3: `make_trip`

**Was:** Baue ein Fahrt-Dict aus zwei Pflichtwerten, einer optionalen `tags`-Liste und beliebig vielen weiteren benannten Werten.

**Warum:** Mit `**kwargs` geben dir die Frameworks in Modul 4 und 5 ihren Kontext. Die `tags`-Regel ist die Falle mit veränderbaren Standardwerten aus dem Warmup, richtig vermieden.

**Abnahme:** Zusätzliche Keyword-Argumente werden zu Schlüsseln; zwei Fahrten ohne Tags teilen sich nie eine Liste; eine übergebene `tags`-Liste wird kopiert, nicht wiederverwendet (`MakeTripTest`).

**Hinweise:**
- In der Funktion ist `extra` ein ganz normales Dict.
- `list(tags)` erzeugt eine neue Liste mit denselben Elementen.
- Prüfe „nicht angegeben" mit `is None`.

## Aufgabe 4: Synthese, `price_trips`

**Was:** Kombiniere Aufgabe 1 und 2. Teile die Fahrten auf, berechne für jede gültige Fahrt den Preis in einem **neuen** Dict, das zusätzlich `fare` enthält, gib alle Preisoptionen unverändert an `fare` weiter, und gib die bepreisten Fahrten, die abgelehnten IDs und die Summe zurück.

**Warum:** Optionen durch eine Funktion in eine andere weiterreichen, ohne die Daten des Aufrufers zu verändern: Diese Kombination hat der Vormittag nur in einzelnen Teilen gezeigt.

**Abnahme:** Standardsumme `103.42`; mit `night=True` ist die Summe `155.14`; bepreiste Fahrten behalten ihre anderen Schlüssel; `TRIPS` ist nach dem Aufruf unverändert; eine unbekannte Option wie `discount=0.1` löst `TypeError` aus (`PriceTripsTest`).

**Hinweise:**
- Nutze deine eigenen Funktionen: zuerst `split_valid`, dann `fare` für jede gültige Fahrt.
- `**pricing` im `def` sammelt die Optionen ein; `**pricing` im Aufruf von `fare` gibt sie weiter.
- `dict(trip)` ist ein neues Dict mit denselben Schlüsseln. Ändere die Kopie, niemals `trip`.

## Wenn du früher fertig bist

**Übung (mehr Wiederholungen der heutigen Ideen):**
- Rufe `fare` in der REPL auf fünf verschiedene Arten auf (nur positionell, alles per Name, gemischt). Sag vor jedem Aufruf das Ergebnis auf Papier voraus.
- Schreibe `describe_trip(trip, *, currency="€")`, das einen einzeiligen f-String zurückgibt, und rufe es mit und ohne `currency` auf.

**Stretch (schwerer, dieselben Ideen):**
- Füge `fare` eine nur-per-Name-Option `minimum` hinzu (kein Fahrpreis liegt je darunter), ohne einen Test zu brechen.
- Schreibe `price_by_city(trips, **pricing)`, das mit `price_trips` ein `{city: total}` zurückgibt, und setze drei `assert`-Zeilen unter `if __name__ == "__main__":`, die es prüfen.
- Selbst-Review: Lies dein eigenes `price_trips`, als hätte es jemand anderes geschrieben, und notiere eine Eingabe, die es zum Absturz bringen würde. Prüfe dann, ob sie das tut.

## Abgabe

Committe und pushe in dieses Repository. Jeder Push startet den Autograder; das Ergebnis erscheint in Coder in 90 Classroom.

```bash
git add exercise.py
git commit -m "feat: implement function labs"
git push
```

---

## Hintergrund: Funktionen auf einer Seite

```python
def fare(minutes, miles, *, base=2.50, night=False):   # Pflicht, dann nur-per-Name mit Standardwerten
    ...

fare(11, 3.2)                  # positionell: nach Reihenfolge zugeordnet
fare(miles=3.2, minutes=11)    # per Name: nach Name zugeordnet, Reihenfolge egal
fare(11, 3.2, night=True)      # Optionen nach * müssen benannt werden
fare(11, 3.2, True)            # TypeError: takes 2 positional arguments but 3 were given
```

Was du dir für heute merken solltest:

- Parameter mit Standardwert kommen nach denen ohne, sonst lädt die Datei gar nicht (`SyntaxError`).
- `return a, b` gibt **ein Tupel** zurück. Entpacke es mit so vielen Namen wie Werten: `low, high = low_high(fares)`.
- Benutze nie eine Liste oder ein Dict als Standardwert: Sie werden einmal erzeugt und von jedem Aufruf geteilt. Nimm `None` und `if tags is None: tags = []`.
- Im `def` sammelt `**extra` zusätzliche benannte Argumente in einem Dict. Im Aufruf verteilt `**options` ein Dict auf benannte Argumente. Ein falsch geschriebener Name scheitert trotzdem mit `TypeError`.
- Eine Variable, der du in einer Funktion etwas zuweist, ist lokal. Konstanten auf Modulebene darfst du frei lesen; gib Ergebnisse zurück, statt Variablen auf Modulebene zu ändern.
- `trip["fare"] = ...` in einer Funktion ändert auch das Dict des Aufrufers. Baue ein neues Dict und gib es zurück.
- Jede `.py`-Datei ist ein Modul: `from exercise import fare` ist genau der Weg, wie die Tests deinen Code erreichen. Code unter `if __name__ == "__main__":` läuft beim Import nicht.

## Weiterführende Links

**Offizielle Python-Dokumentation**

- Tutorial, Funktionen definieren (Standardwerte, Keyword-Argumente, spezielle Parameter, `*args`/`**kwargs`): https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
- Tutorial, Module und `__name__`: https://docs.python.org/3/tutorial/modules.html
- Tutorial, Tupel und Entpacken von Sequenzen: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
- `unittest`: https://docs.python.org/3/library/unittest.html

**Tutorials (Real Python, auf Englisch)**

- Eigene Funktionen definieren: https://realpython.com/defining-your-own-python-function/
- `*args` und `**kwargs`: https://realpython.com/python-kwargs-and-args/
- Scope und die LEGB-Regel: https://realpython.com/python-scope-legb-rule/
- Module und Pakete: https://realpython.com/python-modules-packages/

## Selbstcheck vor dem Push

- [ ] `python3 -m unittest -v` endet mit `OK` und `Ran 15 tests`.
- [ ] `test_exercise.py` ist unverändert (`git diff test_exercise.py` gibt nichts aus).
- [ ] `price_trips` ruft `split_valid` und `fare` auf, statt deren Arbeit zu wiederholen.
- [ ] Keine Funktion in deiner Datei hat eine Liste oder ein Dict als Standardwert.
- [ ] Du kannst erklären, warum `TRIPS` nach `price_trips(TRIPS)` genauso aussieht wie vorher.

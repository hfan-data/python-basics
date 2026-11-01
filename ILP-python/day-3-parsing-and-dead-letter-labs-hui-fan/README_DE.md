[English](README.md) | **Deutsch**

# Tag 3 Übungen: Parsing- und Dead-Letter-Labs

**Schau zuerst:** [das Video zu diesem Lab](https://trytikkr.com/w/IsBcwyZxt2uk0-oJezBzrg)

**Bevor du anfängst:** Bestehe das Readiness-Quiz zu dieser Aufgabe in Coder in 90 Classroom. Du brauchst 40 %, um anzufangen.

Du implementierst vier Funktionen in `exercise.py`, bis `python3 -m unittest -v` grün durchläuft. Die Tests in `test_exercise.py` sind fertig geschrieben und vollständig. Deine Aufgabe ist es, sie zum Bestehen zu bringen, niemals sie zu ändern.

Führe sie in diesem Ordner aus:

```bash
python3 -m unittest -v
```

Jeder Push wird von Coder in 90 bewertet: Deine Punktzahl ist die Anzahl der 14 Tests, die bestehen. Pushe, wann du so weit bist, und so oft du willst.

`ROWS` oben in `exercise.py` ist dasselbe unordentliche Log mit zehn Zeilen wie im Live-Coding. Jeder Wert ist ein String, genau so, wie `csv.DictReader` ihn liefert. Drei Zeilen sind absichtlich kaputt: `t-006` hat einen Monat 13, `t-007` negative Minuten und `t-008` einen leeren Fahrpreis. `make_trips_csv(path)` schreibt diese Zeilen in eine echte CSV-Datei; die Tests nutzen das mit temporären Verzeichnissen.

## Die Testausgabe lesen

- **Eine Zeile pro Test**, am Ende steht `ok`, `FAIL` oder `ERROR`. Arbeite sie Aufgabe für Aufgabe ab.
- **`ERROR`**: Dein Code ist abgestürzt. Am Anfang zeigt jeder Test `NotImplementedError: Task N: ...`; das heißt nur, dass die Aufgabe noch ein Platzhalter ist.
- **`FAIL`**: Dein Code lief, hat aber den falschen Wert zurückgegeben oder nicht den Fehler ausgelöst, den der Test erwartet hat. Die `AssertionError`-Zeilen zeigen, was der Test erwartet hat, neben dem, was deine Funktion getan hat.
- Lies einen Traceback von unten nach oben: Die letzte Zeile sagt, **was** schiefging; dann gehst du nach oben bis zum ersten Frame in `exercise.py` und findest, **wo**.
- Um nur eine Testklasse erneut auszuführen, während du an einer Aufgabe arbeitest: `python3 -m unittest -v test_exercise.ParseRowTest`
- `OK` in der letzten Zeile heißt, dass alle Tests bestanden haben: Das Lab ist fertig.

## Aufgabe 1: `parse_row`

**Was:** Wandle eine Zeile aus Strings in typisierte Werte um: `minutes` als `int` (und nie negativ), `fare` als `float` (und immer größer als null), `date` als `date`-Objekt aus ISO-Text. Ein fehlendes Feld oder ein ungültiger Wert löst `ValueError` aus, dessen Meldung **das Feld nennt**.

**Warum:** Jede CSV-Datei der Welt liefert dir Strings. Sie mit Fehlern umzuwandeln, die das Feld nennen, ist die erste Verteidigungslinie jeder Pipeline.

**Abnahme:** Die gute Zeile wird zum exakten typisierten Dict; die drei kaputten Zeilen lösen jeweils `ValueError` aus, dessen Meldung `date`, `minutes` oder `fare` enthält; ein Fahrpreis von `"0"` und eine Zeile ohne `fare`-Schlüssel lösen einen `ValueError` aus, der `fare` nennt (`ParseRowTest`).

**Tipps:**
- `date.fromisoformat("2026-01-05")` gibt ein `date` zurück und löst `ValueError` für Text aus, der kein echtes Datum ist.
- Pythons eigene Meldung (`could not convert string to float: ''`) nennt das Feld nicht. Fang sie ab und löse deine eigene aus: `raise ValueError(f"fare: bad value {text!r}") from exc`.
- Ein fehlender Schlüssel löst `KeyError` aus, nicht `ValueError`. Die Tests wollen einen `ValueError`, also fang den einen ab und löse den anderen aus.
- `int("-5")` funktioniert. Eine negative Zahl verletzt eine Regel *deiner* Daten, also prüfe sie selbst nach der Umwandlung.

## Aufgabe 2: `in_window`

**Was:** Gib aus bereits geparsten Zeilen und einem Fenster `[start, end)` aus `date`-Objekten nur die Zeilen zurück, deren Datum darin liegt: `start` eingeschlossen, `end` ausgeschlossen.

**Warum:** Halboffene Fenster sind der Weg, auf dem Pipelines vermeiden, einen Grenztag doppelt zu verarbeiten. Das Fenster von gestern endet genau dort, wo das von heute beginnt, und jede Zeile gehört zu genau einem.

**Abnahme:** Eine Zeile mit genau dem Datum `start` bleibt; eine Zeile mit genau dem Datum `end` nicht; eine Zeile vor dem Fenster nicht; keine Zeilen rein ergibt keine Zeilen raus (`InWindowTest`).

**Tipp:** Python erlaubt verkettete Vergleiche: `a <= x < b`.

## Aufgabe 3: `write_jsonl`

**Was:** Schreibe eine Liste von Dicts als JSON Lines in eine Datei: ein `json.dumps` pro Zeile, nach jedem genau ein Zeilenumbruch, Datumswerte über `default=str` serialisiert, die Datei mit `encoding="utf-8"` geöffnet.

**Warum:** JSON Lines ist das Audit- und Austauschformat in allen Modulen des Programms. Ein Objekt pro Zeile macht eine Datei streambar: Ein Leser kann Zeile 1 verarbeiten, bevor Zeile 40.000 existiert.

**Abnahme:** Die Datei hat eine Zeile pro Datensatz, jede Zeile lässt sich mit `json.loads` zurücklesen, ein `date` kommt als String `"2026-01-05"` zurück, `München` übersteht den Hin- und Rückweg, und die Datei endet mit genau einem Zeilenumbruch nach dem letzten Datensatz (`WriteJsonlTest`).

**Tipps:**
- `json.dumps(row)` scheitert an einem `date` mit `TypeError: Object of type date is not JSON serializable`. `default=str` sagt ihm, was es mit allem tun soll, das es nicht kennt.
- Öffne die Datei mit `"w"` in einem `with`-Block, damit sie geschlossen wird, auch wenn eine Zeile scheitert.

## Aufgabe 4: Synthese, `clean_and_split`

**Was:** Verbinde Aufgabe 1 und 2 über eine echte CSV-Datei. Lies sie mit `csv.DictReader` und parse jede Zeile. Eine Zeile, die sich nicht parsen lässt, wird zu einem Reject `(raw_row, reason)`. Geparste Zeilen werden dann nach dem Fenster `[start, end)` gefiltert; Zeilen außerhalb des Fensters fallen stillschweigend weg (sie sind keine Fehler). Gib `(clean_rows, rejects)` zurück.

**Warum:** Das ist das Dead-Letter-Muster aus dem Live-Coding, jetzt aus einer Datei gespeist und mit Zeitfenster. Eine kaputte Zeile von 40.000 darf nicht die Daten der ganzen Nacht kosten: Mach weiter, und behalte, was du brauchst, um die Zeile später zu reparieren.

**Abnahme:** Für die Beispiel-CSV mit dem Fenster 2026-01-05 bis 2026-01-10: genau 5 saubere Zeilen (`t-001` bis `t-005`) mit typisierten Werten, genau 3 Rejects (`t-006`, `t-007`, `t-008`), deren Begründungen die kaputten Felder nennen und deren Rohzeilen unverändert erhalten bleiben, und `t-009` und `t-010` in keiner der beiden Listen (`CleanAndSplitTest`).

**Tipps:**
- Nutze deine eigenen Funktionen: `parse_row` in der Schleife, `in_window` auf dem Ergebnis.
- Öffne die CSV mit `newline=""` und `encoding="utf-8"`, wie `make_trips_csv` es tut.
- `str(exc)` ist die Meldung einer abgefangenen Exception, und das ist deine Begründung.
- Fang nur `ValueError` ab. `except Exception: pass` würde deine eigenen Bugs als "Rejects" verstecken.

## Abgabe

Committe und pushe in dieses Repository. Jeder Push startet den Autograder; das Ergebnis erscheint in Coder in 90 Classroom.

```bash
git add exercise.py
git commit -m "feat: implement parsing labs"
git push
```

---

## Hintergrund: Fehler auf einer Seite

```python
try:
    fare = float(text)            # die Arbeit, die scheitern kann
except ValueError as exc:         # nur der Fehler, den du erwartest und behandeln kannst
    rejects.append((row, str(exc)))
else:
    clean.append(fare)            # läuft nur, wenn try nichts ausgelöst hat
finally:
    print("done")                 # läuft auf jedem Ausgang
```

Was du dir für heute merken solltest:

- `finally` läuft **immer**: nach normalem Ende, nach einem `return`, nach einer abgefangenen und nach einer nicht abgefangenen Exception. Dort werden Dateien und Verbindungen geschlossen. `with open(...) as handle:` erledigt das für eine Datei, ohne dass du das `finally` schreibst.
- Fang die **konkrete** Exception ab. `except Exception: pass` verschluckt alles, auch deine eigenen Tippfehler, und der Fehler taucht später an einer Stelle auf, die keinen Sinn ergibt (oft als `NameError`).
- `raise NewError("...") from exc` hängt den ursprünglichen Fehler an, sodass der Traceback beide zeigt.
- Die häufigsten heute: `ValueError` (richtiger Typ, ungültiger Wert: `float("twelve")`, `int("")`, Monat 13), `KeyError` (fehlender Dict-Schlüssel), `TypeError` (falscher Typ: `"14.50" * 1.5`), `FileNotFoundError`.
- `csv.DictReader` liefert dir **ein Dict pro Zeile**, mit der Kopfzeile als Schlüssel, und jeder Wert ist ein **String**, auch Zahlen und Datumswerte. Die Umwandlung ist deine Aufgabe.
- Geheimnisse gehören nie in den Code. Lies sie aus der Umgebung: `os.environ["DB_PASSWORD"]` scheitert laut, wenn die Variable fehlt, `os.environ.get("LOG_LEVEL", "INFO")` fällt auf einen Standardwert zurück. Werte aus der Umgebung sind immer Strings.

### Halboffene Fenster

```text
[2026-01-05, 2026-01-10)   enthält den 5., 6., 7., 8. und 9.; nicht den 10.
[2026-01-10, 2026-01-15)   das nächste Fenster beginnt genau dort, wo dieses endete
```

### JSON Lines

```text
{"trip_id": "t-001", "city": "Berlin", "date": "2026-01-05", "minutes": 11, "fare": 14.5}
{"trip_id": "t-002", "city": "Hamburg", "date": "2026-01-06", "minutes": 25, "fare": 27.25}
```

Ein vollständiges JSON-Objekt pro Zeile, keine umschließende Liste, keine Kommas zwischen den Zeilen.

## Weiterführende Links

**Offizielle Python-Dokumentation** (auf Englisch; die Tutorial-Seiten gibt es auch auf Deutsch unter https://docs.python.org/de/3/tutorial/)

- Tutorial, Fehler und Exceptions (`try`, `except`, `else`, `finally`, `raise ... from`): https://docs.python.org/3/tutorial/errors.html
- Eingebaute Exceptions und ihre Hierarchie: https://docs.python.org/3/library/exceptions.html
- Modul `csv`, mit `DictReader` und `DictWriter`: https://docs.python.org/3/library/csv.html
- Modul `json`, mit `dumps` und seinem Argument `default`: https://docs.python.org/3/library/json.html
- `datetime.date.fromisoformat`: https://docs.python.org/3/library/datetime.html#datetime.date.fromisoformat
- `os.environ`: https://docs.python.org/3/library/os.html#os.environ
- `logging` HOWTO: https://docs.python.org/3/howto/logging.html
- `unittest`, mit `assertRaisesRegex`: https://docs.python.org/3/library/unittest.html

**Tutorials (Real Python, auf Englisch)**

- Exceptions: https://realpython.com/python-exceptions/
- Tracebacks verstehen: https://realpython.com/python-traceback/
- CSV-Dateien lesen und schreiben: https://realpython.com/python-csv/
- Mit JSON arbeiten: https://realpython.com/python-json/
- Context Manager und `with`: https://realpython.com/python-with-statement/

**Zum Vertiefen**

- Das Format JSON Lines: https://jsonlines.org/
- The Twelve-Factor App, Konfiguration in der Umgebung: https://12factor.net/de/config

## Selbstcheck vor dem Push

- [ ] `python3 -m unittest -v` endet mit `OK` und `Ran 14 tests`.
- [ ] `test_exercise.py` ist unverändert (`git diff test_exercise.py` gibt nichts aus).
- [ ] `clean_and_split` ruft `parse_row` und `in_window` auf, statt ihre Arbeit zu wiederholen.
- [ ] Dein Code hat kein nacktes `except:` und kein `except Exception: pass`.
- [ ] Du kannst erklären, warum `t-009` in keiner der beiden Listen ist, und warum das kein Fehler ist.

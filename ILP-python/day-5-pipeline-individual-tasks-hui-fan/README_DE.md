[English](README.md) | **Deutsch**

# Tag 5 Einzelaufgaben: entwerfen, bewerten, verfolgen, liefern, allein

Heute Vormittag hat deine Gruppe eine Städtebericht-Pipeline entworfen und dann an drei Stationen
eine kaputte Kopie verfolgt, debuggt und bewertet. Hier machst du jeden dieser Schritte allein mit
neuen Daten: Dresden, Leipzig und Bremen. Jede Aufgabe nennt die Aktivität vom Vormittag, an die
sie anknüpft; der Entwurf deiner Gruppe, eure Verfolgungstabelle und euer Bug-Log sind die ersten
Stellen, an denen du nachschaust, wenn du festhängst.

Bearbeite diese Aufgaben nach dem Readiness-Check, als Nacharbeit vor dem nächsten Modul.

Du implementierst vier Aufgaben in `exercise.py`, bis `python3 -m unittest -v` grün durchläuft.
Die Tests in `test_exercise.py` sind fertig geschrieben und vollständig: Bring sie zum Bestehen,
ändere sie nie.

```bash
python3 -m unittest -v
```

Jeder Push wird von Coder in 90 bewertet: Deine Punktzahl ist die Anzahl der 13 Tests, die
bestehen.

`ROWS` oben in `exercise.py` enthält acht Zeilen, jeder Wert ein String, genau so, wie
`csv.DictReader` ihn liefert. Vier Zeilen sind unbrauchbar, und die Städtenamen sind unordentlich.

## Die Testausgabe lesen

- **`ERROR`** mit `NotImplementedError: Task N` heißt nur, dass die Aufgabe noch ein Stub ist.
- **`FAIL`**: Dein Code lief, hat aber den falschen Wert geliefert; der `AssertionError` zeigt
  Erwartetes und Tatsächliches nebeneinander.
- Lies einen Traceback von unten nach oben: letzte Zeile für das **Was**, erster Frame in
  `exercise.py` für das **Wo**.
- Eine Testklasse nach der anderen: `python3 -m unittest -v test_exercise.FindRejectsTest`

## Aufgabe 1: `find_rejects`

**Vom Vormittag:** Aktivität 1, Teil 1 (welche Zeilen abgelehnt werden müssen, und warum).

**Was:** Liste jede unbrauchbare Zeile als `(trip_id, reason)` auf, in Eingabereihenfolge. Die
drei Gründe und die Reihenfolge der Prüfung stehen im Docstring; melde nur den ersten, der
zutrifft.

**Abnahme:** genau `r-04` (fare not a number), `r-05` (empty city), `r-06` und `r-08` (fare not
positive); eine Zeile mit leerer Stadt und schlechtem Fahrpreis meldet nur `"empty city"`; keine
Zeilen ergeben `[]` (`FindRejectsTest`).

## Aufgabe 2: `city_totals`

**Vom Vormittag:** Station 3 (fremden Code bewerten).

**Was:** Der Docstring zeigt die Funktion aus Station 3. Schreib die Version, die funktioniert:
Überspringe, was Aufgabe 1 ablehnt, bereinige die Stadt, runde, und liefere dieselbe Antwort, egal
wie oft sie aufgerufen wird.

**Abnahme:** `{"Dresden": 28.0, "Leipzig": 22.1, "Bremen": 15.0}`; zwei Aufrufe liefern gleiche
Ergebnisse; keine Zeilen ergeben `{}`; `ROWS` ist unverändert (`CityTotalsTest`).

## Aufgabe 3: `totals_with_trace`

**Vom Vormittag:** Station 1 (von Hand verfolgen).

**Was:** Gib die Summen zusammen mit der Verfolgungstabelle zurück, die deine Gruppe auf Papier
gezeichnet hat: ein Schnappschuss des ganzen Summen-Dicts nach jeder brauchbaren Zeile.

**Abnahme:** vier Schnappschüsse, von `{"Dresden": 18.4}` bis zu allen drei Städten; jeder
Schnappschuss ist ein eigenes Dict, sodass eine spätere Zeile keinen früheren verändern kann;
keine Zeilen ergeben `({}, [])` (`TotalsWithTraceTest`).

**Achtung:** Wenn du viermal dasselbe Dict anhängst, bekommst du vier Ansichten der Endsummen,
keine Verfolgung. Wenn alle deine Schnappschüsse gleich aussehen, ist genau das passiert.

## Aufgabe 4: Synthese, `write_summary`

**Vom Vormittag:** Aktivität 1, Teil 3 (der Bau) und Station 2 (die Bugs, die ihr behoben habt).

**Was:** Schreib `city,total` als CSV-Datei, höchste Summe zuerst, bei Gleichstand alphabetisch,
Summen mit zwei Nachkommastellen, und ersetze dabei jeden früheren Inhalt. Gib zurück, wie viele
Städte geschrieben und wie viele Zeilen übersprungen wurden.

**Warum:** Der Bericht vom Vormittag war eine Textdatei, in der Gruppe gebaut. Dieser hier ist
eine CSV, die ein anderes Programm lesen wird, allein aus deinen eigenen Aufgaben 1 und 2 gebaut,
und er muss einen erneuten Lauf überstehen: die Vier-Schritte-Form, die jede Pipeline in Modul 4
und 5 hat.

**Abnahme:** gibt `(3, 4)` zurück und schreibt die Kopfzeile plus Dresden, Leipzig, Bremen;
gleiche Summen erscheinen alphabetisch; zweimal ausführen hinterlässt eine identische Datei
(`WriteSummaryTest`).

## Abgabe

```bash
git add exercise.py
git commit -m "feat: implement day 5 individual tasks"
git push
```

## Selbstcheck vor dem Push

- [ ] `python3 -m unittest -v` endet mit `OK` und `Ran 13 tests`.
- [ ] `test_exercise.py` ist unverändert (`git diff test_exercise.py` gibt nichts aus).
- [ ] `write_summary` nutzt deine Arbeit aus Aufgabe 1 und 2, statt sie zu wiederholen.
- [ ] Du kannst jedes Problem im Code des Kollegen aufzählen und sagen, welche deiner Zeilen es
  behebt.

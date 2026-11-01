[English](README.md) | **Deutsch**

# Tag 1 Nachmittagsübungen: String- und Funktions-Labs (12:45–14:45)

**Schau zuerst:** [das Video zu diesem Lab](https://trytikkr.com/w/lAKYlFxG85elOlg2-np_cw)

**Bevor du anfängst:** Bestehe das Readiness-Quiz zu dieser Aufgabe in Coder in 90 Classroom. Du brauchst 50 %, um anzufangen.

Du implementierst vier Funktionen in `exercise.py`, bis `python3 -m unittest -v` grün durchläuft. Die Tests in `test_exercise.py` sind fertig geschrieben und vollständig. Deine Aufgabe ist es, sie zum Bestehen zu bringen, niemals sie zu ändern. Genau so laufen die Labs in Modul 4 und 5 des Programms.

Führe sie in diesem Ordner aus:

```bash
python3 -m unittest -v
```

Jeder Push wird von Coder in 90 bewertet: Deine Punktzahl ist die Anzahl der 14 Tests, die bestehen.

## Die Testausgabe lesen

In diesem Kurs schreibst oder änderst du nie Tests; du führst sie nur aus und liest, was sie sagen.

- **Eine Zeile pro Test**, am Ende steht `ok`, `FAIL` oder `ERROR`. Arbeite sie Aufgabe für Aufgabe ab.
- **`ERROR`**: Dein Code ist abgestürzt. Am Anfang zeigt jeder Test `NotImplementedError: Task N: ...`; das heißt nur, dass die Aufgabe noch ein Platzhalter ist.
- **`FAIL`**: Dein Code lief, hat aber den falschen Wert zurückgegeben. Die `AssertionError`-Zeilen zeigen, was der Test erwartet hat, neben dem, was deine Funktion zurückgegeben hat; der Unterschied ist dein nächster Fix.
- **Der Traceback** zeigt auf die Zeile in `exercise.py`, in der es schiefging, wie jeder andere Traceback auch.
- Um nur eine Testklasse erneut auszuführen, während du an einer Aufgabe arbeitest: `python3 -m unittest -v test_exercise.CleanCityTest`
- `OK` in der letzten Zeile heißt, dass alle Tests bestanden haben: Das Lab ist fertig.

Die Daten (`TRIPS` oben in `exercise.py`) sind ein kleines Taxifahrten-Log. Es ist absichtlich unordentlich: Städtenamen haben überflüssige Leerzeichen und gemischte Groß- und Kleinschreibung, und `minutes` ist mal ein `int`, mal ein String im Format `"H:MM"` oder `"MM"`, mal Unsinn.

## Aufgabe 1: `clean_city`

**Was:** Normalisiere einen Städtenamen, damit das spätere Gruppieren funktioniert: Leerzeichen am Anfang und Ende entfernen, alles kleinschreiben, innere Leerzeichen durch Unterstriche ersetzen.

**Warum:** `"  Berlin "` und `"Berlin"` sind für einen Menschen dieselbe Stadt und für Python zwei verschiedene Dict-Keys. Genau daran scheitern Pipelines.

**Abnahme:** Die drei Fälle in `CleanCityTest` bestehen, auch der, bei dem eine Eingabe nur aus Leerzeichen den leeren String zurückgibt.

## Aufgabe 2: `parse_duration`

**Was:** Wandle einen Dauer-String in ganze Minuten um. `"H:MM"` bedeutet Stunden und Minuten, `"MM"` nur Minuten. Alles, was keine Dauer ist, gibt `None` zurück.

**Warum:** CSV-Spalten kommen als Strings an; sie umzuwandeln ist das Erste, was jede Pipeline tut.

**Abnahme:** `"1:30"` → 90, `"45"` → 45, `"0:05"` → 5, und `"banana"`, `""` und `"1:2:3"` geben `None` zurück (`ParseDurationTest`).

## Aufgabe 3: `fare_report_line`

**Was:** Formatiere eine Fahrt als Berichtszeile mit festen Spaltenbreiten. Die genaue Vorlage steht im Docstring: `trip_id` linksbündig in 6 Spalten, `city` linksbündig in 15, `minutes` rechtsbündig in 3, `miles` rechtsbündig in 5 mit einer Nachkommastelle, Geldbeträge immer mit genau 2 Nachkommastellen, Spalten getrennt durch `" | "`, und ein `€` direkt vor dem Fahrpreis.

**Warum:** Ausgerichtete Spalten sind der Unterschied zwischen einem Bericht, den Menschen lesen, und einer Textwand.

**Abnahme:** Die zwei Fälle mit exaktem String und der Fall mit zwei Nachkommastellen in `FareReportLineTest` bestehen. Tipp: Kopiere die Vorlage aus dem Docstring in deine Funktion. Der Docstring ist der Vertrag.

## Aufgabe 4: Synthese, `build_receipt`

**Was:** Nimm die komplette unordentliche `TRIPS`-Liste und erzeuge daraus eine vollständige Quittung: eine formatierte Zeile pro brauchbarer Fahrt, dann eine letzte Zeile `TOTAL: €<Betrag>`. Eine Fahrt ist brauchbar, wenn sich ihre `minutes` parsen lassen (Ints werden übernommen, Strings werden geparst, Zeilen, bei denen Aufgabe 2 `None` zurückgibt, werden übersprungen), und ihre Stadt wird vor dem Formatieren bereinigt. Die Summe ist die Summe der Fahrpreise der aufgenommenen Fahrten, mit 2 Nachkommastellen ausgegeben.

**Warum:** Das kombiniert Aufgabe 1 bis 3 so, wie es eine echte Pipeline tut (parsen, bereinigen, formatieren, zusammenfassen), und genau diese Kombination kam in der Vorlesung nicht vor.

**Abnahme:** Insgesamt 7 Zeilen (6 Fahrten plus TOTAL), die erste Zeile und die Zeile `TOTAL: €130.10` stimmen exakt, und die nicht parsbare Zeile taucht nie auf (`BuildReceiptTest`).

## Abgabe

Committe und pushe in dieses Repository. Jeder Push startet den Autograder; das Ergebnis erscheint in Coder in 90 Classroom.

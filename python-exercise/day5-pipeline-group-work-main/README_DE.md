[English](README.md) | **Deutsch**

# Tag 5 Vormittag: Leitfaden für die Gruppenarbeit

Heute gibt es keine Folien, kein Live-Coding und keine neue Syntax. Heute Vormittag entwirft und
baut deine Gruppe die kleinste echte Datenpipeline und liest, verfolgt und debuggt dann eine
kaputte Kopie davon. Der Nachmittag ist Einzelarbeit: das Mini-Capstone-Lab (dein eigenes
Repository `day5-pipeline-labs`), danach der Readiness-Check.

| Zeit | Was | Mit wem |
|------|-----|---------|
| 09:00–09:20 | Warmup-Fragen | Dein Partner, dann der ganze Raum |
| 09:20–09:35 | Aktivität 1, Teil 1: die Pipeline auf Papier entwerfen | Deine Gruppe (3–4) |
| 09:35–09:45 | Aktivität 1, Teil 2: Entwürfe tauschen | Deine Gruppe plus eine weitere Gruppe |
| 09:45–10:20 | Aktivität 1, Teil 3: bauen | Deine Gruppe, ein Laptop |
| 10:20–10:30 | Nachbesprechung: zweimal ausführen | Ganzer Raum |
| 10:30–10:45 | Pause | |
| 10:45–11:30 | Aktivität 2: drei Stationen, je 15 Min. | Eine neue Dreiergruppe |
| 11:30–11:45 | Nachbesprechung | Ganzer Raum |

## So arbeiten wir zusammen

- **Erst entwerfen, dann tippen.** Funktionsnamen, Eingaben und Ausgaben kommen zuerst auf
  Papier. Ein Entwurf, den du erklären kannst, ist mehr wert als Code, den du nicht erklären
  kannst.
- **Eine Tastatur, wechselnd.** Der **Driver** tippt nur, was die Gruppe entscheidet; die
  **Navigatoren** entscheiden und erklären warum. Wechselt den Driver alle zehn Minuten. Jede
  Person ist heute mindestens einmal Driver, besonders wenn du sonst lieber zuschaust: Den
  Readiness-Check heute Nachmittag machst du allein.
- **Wer es weiß, erklärt; wer es nicht weiß, tippt.**
- **Jede Stimme einmal.** Bevor die Gruppe weitergeht, kann jede Person erklären, was der Code
  gerade gemacht hat.
- **Ändert Code erst, wenn ihr sagen könnt, was falsch ist.** Raten und neu probieren ist kein
  Debuggen.
- **Seit fünf Minuten fest?** Der Driver liest die letzte Zeile des Tracebacks laut vor, dann
  gibt die Gruppe den verdächtigen Wert aus. Immer noch fest: Hand heben. Sucht die Antwort nicht
  online.

---

## Aktivität 1: eine Städtebericht-Pipeline entwerfen, dann bauen (Gruppen von 3–4)

**Die Aufgabe.** Eine CSV-Datei mit Taxifahrten kommt herein, und einige Zeilen sind kaputt.
Erzeugt `report.txt`: eine Zeile pro Stadt mit ihrem Gesamtfahrpreis (höchster zuerst, bei
Gleichstand alphabetisch), eine `TOTAL`-Zeile und die Anzahl übersprungener Zeilen. Die Datei
muss gleich bleiben, egal wie oft das Skript läuft.

Eingabe (`trips.csv`):

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

Erwartete `report.txt`:

```
Berlin       56.95
Hamburg      27.25
Köln         19.00
TOTAL       103.20
skipped: 3
```

### Teil 1: auf Papier entwerfen (15 Min.)

Beantwortet als Gruppe, bevor ihr Code schreibt:

1. Welche Zeilen müssen abgelehnt werden, und jeweils aus welchem Grund?
2. Welche Zeilen zählen als dieselbe Stadt? Was muss mit dem Städtetext passieren?
3. Benennt die vier Schritte: Extract, Validate, Transform, Load. Welche Zeilen der Eingabe oder
   Ausgabe betrifft jeder Schritt?
4. Listet die Funktionen auf, die ihr schreiben werdet: Name, Eingabe, Ausgabe und ein Docstring
   in einem Satz. Eine Aufgabe pro Funktion; der Name sagt, was sie zurückgibt. Peilt vier oder
   fünf an.

### Teil 2: Entwürfe tauschen (10 Min.)

Tut euch mit einer anderen Gruppe zusammen. Jede Gruppe erklärt ihre Funktionsliste in zwei
Minuten. Fragt dann die andere Gruppe, Funktion für Funktion:

- Was macht diese Funktion mit einer leeren Eingabe?
- Was macht sie mit einer kaputten Zeile?
- Was passiert, wenn das Skript zweimal läuft?

Ändert euren eigenen Entwurf, wenn ihre Fragen eine Lücke zeigen.

### Teil 3: bauen (35 Min.)

Ein Laptop, der Driver wechselt alle zehn Minuten.

1. Schreibt die Beispielzeilen als Liste von Dicts und schreibt sie mit `csv.DictWriter`
   (Tag 3) in `trips.csv`, damit jede Gruppe dieselbe Datei hat.
2. Tippt alle eure Funktionssignaturen mit Docstrings und `...` als Rumpf.
3. Füllt eine Funktion nach der anderen aus und probiert sie in der REPL, bevor ihr weitergeht.
4. Fertig heißt: Eure `report.txt` entspricht exakt der erwarteten Ausgabe. Führt das Skript dann
   ein zweites Mal aus und schaut euch die Datei noch einmal an.

---

## Aktivität 2: drei Stationen, verfolgen, debuggen, bewerten (Dreiergruppen)

Eure Gruppe besucht alle drei Stationen für je 15 Minuten und beginnt dort, wohin die Lehrkraft
euch schickt. Übernehmt an jeder Station eine Rolle und wechselt zwischen den Stationen:

- **Schreiber:** schreibt die Antworten der Gruppe auf.
- **Tipper:** die einzige Person an der Tastatur.
- **Prüfer:** liest die Fragen der Station laut vor und prüft jede Antwort daran, bevor die
  Gruppe weitergeht.

### Station 1: von Hand verfolgen

Laptop erst am Ende. Nehmt die ausgedruckten Funktionen `city_totals` und `format_report`, die
die Lehrkraft austeilt, und füttert sie mit den gültigen Fahrten aus Aktivität 1, in der
Reihenfolge der Datei.

1. Zeichnet eine Tabelle mit einer Zeile pro Schleifendurchlauf von `city_totals` und je einer
   Spalte für `trip["city"]`, `trip["fare"]` und das ganze Dict `totals` nach diesem Durchlauf.
2. Schreibt die Liste `ranking` auf, die `format_report` baut, und dann die exakten Zeilen, die
   es zurückgibt.
3. Ändert einen Fahrpreis so, dass zwei Städte gleichauf liegen. Welche kommt jetzt zuerst, und
   welcher Teil des `key` entscheidet das?

Erst wenn die Tabelle fertig ist, prüft sie am Laptop mit `print(f"{totals=}")` in der Schleife.

### Station 2: debuggen

Kopiert `broken_city_report.py` aus diesem Repository in einen leeren Ordner und führt es aus.
Es hat vier Bugs: einer stürzt ab, zwei liefern einen falschen Bericht, und einer zeigt sich
erst, wenn ihr es zweimal ausführt. Löscht `trips.csv` und `report.txt` vor jedem Testlauf.
Folgt für jeden Bug der Reihenfolge beim Debuggen (Traceback lesen, verdächtigen Wert ausgeben,
die Zeile allein in der REPL ausprobieren) und füllt eine Zeile aus:

| Symptom (was ihr gesehen habt) | Wo (Datei, Zeile) | Wie gefunden (Traceback / print / REPL) | Fix |
|--------------------------------|-------------------|-----------------------------------------|-----|
| | | | |

Behaltet dieses Bug-Log: Es ist heute Nachmittag nützlich.

### Station 3: fremden Code bewerten

Jemand aus dem Team hat die Funktion unten geschrieben. Listet, ohne sie auszuführen, jedes
Problem auf, das ihr findet, und schreibt zu jedem Problem die Eingabe auf, die es zeigt. Prüft
eure Liste dann in der REPL.

```python
def city_totals(rows, totals={}):
    for row in rows:
        city = row["city"].strip
        totals[city] = totals.get(city) + float(row["fare"])
    return totals
```

Beantwortet dann die drei Fragen, die man jeder Funktion stellen sollte: Was passiert bei einer
leeren Eingabe? Bei einer fehlerhaften Zeile? Wenn sie im selben Programm zweimal läuft?

### Nachbesprechung (11:30)

Seid bereit, für die Station zu antworten, an der eure Gruppe angefangen hat:

- Station 1: Was hat eure Tabelle gezeigt, das ihr nicht erwartet hattet?
- Station 2: Welcher Bug hat am längsten gedauert, und welcher Schritt der Debugging-Reihenfolge
  hat ihn gefunden?
- Station 3: Welches Problem im Code der Kollegin oder des Kollegen würde in Produktion den
  größten Schaden anrichten?

## Vor der Mittagspause

Behalte die Pipeline deiner Gruppe, deine Verfolgungstabelle und dein Bug-Log. Das Lab heute
Nachmittag ist dieselbe Pipeline mit einer Ebene mehr (pro Tag), und du baust es allein.

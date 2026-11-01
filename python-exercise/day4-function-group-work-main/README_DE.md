[English](README.md) | **Deutsch**

# Tag 4 Vormittag: Leitfaden für die Gruppenarbeit

Heute Vormittag gibt es keine Folien und kein Live-Coding. Du lernst die Ideen des Tages, indem
du mit anderen Code vorhersagst, ausführst und erklärst. Das Lab am Nachmittag (dein eigenes
Repository `day4-function-labs`) bearbeitest du allein; was ihr heute Vormittag gemeinsam
erarbeitet, nimmst du dorthin mit.

| Zeit | Was | Mit wem |
|------|-----|---------|
| 09:00–09:20 | Warmup-Fragen | Dein Partner, dann der ganze Raum |
| 09:20–10:00 | Aktivität 1, Teil 1: Karten A–H | Dein Partner |
| 10:00–10:15 | Aktivität 1, Teil 2: eine Regel pro Karte vereinbaren | Euer Paar plus ein weiteres Paar |
| 10:15–10:30 | Nachbesprechung | Ganzer Raum |
| 10:30–10:45 | Pause | |
| 10:45–11:30 | Aktivität 2: den Fahrpreisbericht von Tag 1 als Toolkit neu bauen | Deine Gruppe (3–4) |
| 11:30–11:45 | Vorstellen der Ergebnisse | Ganzer Raum |

## So arbeiten wir zusammen

- **Erst vorhersagen, dann ausführen.** Alle schreiben zuerst eine Vorhersage auf Papier.
  „Ich weiß es nicht, weil ..." ist eine gültige Vorhersage; stummes Schulterzucken nicht.
- **Eine Tastatur, wechselnd.** Der **Driver** tippt nur, was die Gruppe entscheidet. Die
  **Navigatoren** entscheiden, was getippt wird, und erklären warum. Wechselt den Driver, wenn
  der Leitfaden es sagt, auch mitten in einer Funktion.
- **Wer es weiß, erklärt; wer es nicht weiß, tippt.** Wenn du die Antwort schon kennst, ist
  deine Aufgabe, dass dein Partner sie sagen kann, nicht, sie für ihn zu sagen.
- **Jede Stimme einmal.** Bevor die Gruppe weitergeht, kann jede Person das Ergebnis in einem
  Satz erklären. Wenn jemand das nicht kann, seid ihr noch nicht fertig.
- **Falsche Vorhersagen sind der Sinn der Sache.** Eine falsche Vorhersage zeigt dir genau, was
  du lernen musst. Sprich sie aus; versteck sie nicht.
- **Seit fünf Minuten fest?** Der Driver liest die letzte Zeile des Tracebacks laut vor. Fragt:
  Zu welcher Karte passt das? Immer noch fest: Hand heben. Sucht die Antwort nicht online.

---

## Aktivität 1: vorhersagen, ausführen, erklären (Paare, dann Vierergruppen)

Für jede Karte:

1. **Vorhersagen.** Ihr schreibt beide auf, was passieren wird, bevor jemand tippt: eine
   Ausgabe, ein Fehlertyp oder „Ich weiß es nicht, weil ...".
2. **Ausführen.** Eine Person tippt den Code in die REPL (`python3`) oder eine Testdatei. Wechselt
   bei jeder Karte, wer tippt.
3. **Erklären.** Wenn eine Vorhersage falsch war, redet weiter, bis ihr beide sagen könnt, warum.
   Schreibt eine Regel in einem Satz auf, mit der eure Vorhersage richtig gewesen wäre.

Die Karten sind unabhängig voneinander: Wenn ihr bei einer festhängt, macht weiter und kommt
später zurück. Rechnet mit etwa fünf Minuten pro Karte.

Führt ein Regelblatt wie dieses:

| Karte | Unsere Vorhersage | Was passiert ist | Unsere Regel (ein Satz) |
|-------|-------------------|------------------|-------------------------|
| A | | | |

**Teil 2 (10:00).** Tut euch mit einem anderen Paar zusammen. Vergleicht eure Regeln Karte für
Karte und einigt euch auf je einen gemeinsamen Satz. Wo ihr uneins seid, führt den Code noch
einmal gemeinsam aus. Bestimmt eine Person, die eure Regeln in der Nachbesprechung vorliest.

### Karte A: Argumente den Parametern zuordnen

```python
def fare(minutes, miles, base=2.50):
    return base + minutes * 0.40 + miles * 1.75

print(fare(10, 2))
print(fare(miles=2, minutes=10))
print(fare(2, 10))
print(fare(10, 2, base=3.0))
```

### Karte B: Wo Standardwerte stehen dürfen

Sagt voraus, ob diese Datei überhaupt lädt. Findet dann zwei verschiedene Wege, sie zu
reparieren.

```python
def fare(minutes=0, miles):
    return 2.50 + minutes * 0.40 + miles * 1.75
```

### Karte C: Der einzelne `*`

```python
def fare(minutes, miles, *, night=False):
    total = 2.50 + minutes * 0.40 + miles * 1.75
    return total * 1.5 if night else total

print(fare(10, 2, night=True))
print(fare(10, 2, True))
```

Diskutiert: Wem nützt der `*`, der Person, die die Funktion schreibt, oder der Person, die sie
aufruft?

### Karte D: Zwei Werte zurückgeben

```python
def low_high(fares):
    return min(fares), max(fares)

result = low_high([9.0, 27.25, 14.5])
print(result)
low, high = result
print(high - low)
low, high, middle = low_high([9.0, 27.25])
```

### Karte E: Ein Standardwert, der sich erinnert

```python
def count_city(city, counts={}):
    counts[city] = counts.get(city, 0) + 1
    return counts

print(count_city("Berlin"))
print(count_city("Köln"))
```

Schreibt `count_city` dann so um, dass jeder Aufruf ohne `counts` mit einem leeren Dict beginnt.

### Karte F: Benannte Argumente einsammeln und weitergeben

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

Diskutiert: `**` steht einmal in einem `def` und einmal in einem Aufruf. Was macht es jeweils?

### Karte G: Wem gehört das Dict?

```python
def add_fare(trip):
    trip["fare"] = 12.5
    return trip

trip = {"trip_id": "t-001"}
priced = add_fare(trip)
print(trip)
print(priced is trip)
```

Schreibt `add_fare` dann so um, dass `trip` nach dem Aufruf genauso ist wie vorher.

### Karte H: Die eigene Datei importieren

Legt `tools.py` an:

```python
def double(x):
    return x * 2

print("tools loaded")
```

Sagt im selben Ordner voraus, was passiert, und führt aus:

```bash
python3 -c "from tools import double; print(double(4))"
```

Setzt das `print` dann unter `if __name__ == "__main__":` und führt denselben Befehl noch einmal
aus. Führt ihn zum Schluss aus einem anderen Ordner aus und lest die Fehlermeldung.

---

## Aktivität 2: den Fahrpreisbericht von Tag 1 als Toolkit neu bauen (Gruppen von 3–4)

**Ziel:** Macht aus `fare_report.py` von Tag 1 die Datei `fare_tools.py`, eine Sammlung kleiner
Funktionen, die eine andere Datei importieren kann, und wendet dabei jede Regel aus Aktivität 1
an. Ein Laptop pro Gruppe; wechselt den Driver alle zehn Minuten.

**Start:** Kopiert `fare_report.py` aus diesem Repository (den Fahrpreisbericht von Tag 1) nach
`fare_tools.py` und führt sie aus, damit ihr wisst, wie „funktioniert" aussieht.

Die Lehrkraft sagt die Zeiten an.

1. **Auflisten, was fest eingebaut ist (5 Min., auf Papier).** Was müsste jemand in der Datei
   ändern, um etwas anderes zu bekommen? Welcher Teil gibt nur aus und ist nicht wiederverwendbar?
2. **Erst die Signaturen vereinbaren, dann die Rümpfe (10 Min., auf Papier).** Schreibt Name,
   Parameter und Rückgabe jeder Funktion auf:
   - `fare_estimate`: Tarife haben Standardwerte und lassen sich nur per Name ändern; eine Option
     `night` multipliziert den Fahrpreis mit 1,5
   - `split_trips`: gibt die gültigen Fahrten und die IDs der ungültigen zurück
   - `price_trip`: gibt ein neues Dict mit einem Schlüssel `fare` zurück und reicht alle
     Preisoptionen an `fare_estimate` weiter
   - `summarise`: gibt Anzahl, Summe und Durchschnitt der Fahrpreise zurück; eine leere Liste
     darf nicht abstürzen
3. **Eine Funktion nach der anderen bauen (25 Min.).** Schreibt den Rumpf, probiert ihn in der
   REPL aus, dann geht weiter. Ihr seid auf dem richtigen Weg, wenn:
   - `fare_estimate(11, 3.2)` `12.5` ergibt, `fare_estimate(11, 3.2, night=True)` `18.75`
     ergibt und `fare_estimate(11, 3.2, True)` ein `TypeError` ist
   - `split_trips(TRIPS)` vier gültige Fahrten und `['t-005']` ergibt
   - `TRIPS[0]` nach `price_trip(TRIPS[0], night=True)` keinen Schlüssel `fare` hat
   - `summarise([])` `(0, 0.0, 0.0)` ergibt
4. **Zeigen, dass der Import funktioniert (5 Min.).** Schreibt `main()` mit den neuen Funktionen
   um und lasst es unter dem `__name__`-Guard. Führt in einem zweiten Terminal im selben Ordner
   `python3 -c "from fare_tools import fare_estimate; print(fare_estimate(11, 3.2, night=True))"`
   aus. Nur `18.75` sollte erscheinen.

**Früher fertig?** Fügt `fare_estimate` eine nur-per-Name-Option `minimum` hinzu: Kein
Fahrpreis liegt je darunter.

**Vorstellen der Ergebnisse (11:30).** Die Lehrkraft gibt eurer Gruppe eine dieser Fragen.
Bereitet alle vier vor, mit eurem Code auf dem Bildschirm:

- Welche Signatur habt ihr geändert, nachdem ihr mit dem Tippen angefangen hattet, und warum?
- Zeigt `price_trip`: Woher wisst ihr, dass die Eingabe nicht verändert wird?
- Was hat `summarise([])` gemacht, bevor ihr den Fall behandelt habt?
- Wo wäre ein `**kwargs`-Parameter in eurer Datei die falsche Wahl?

## Vor der Mittagspause

Behalte dein Regelblatt und die `fare_tools.py` deiner Gruppe. Heute Nachmittag arbeitest du
allein, und das sind die ersten Stellen, an denen du nachschaust, wenn du festhängst.

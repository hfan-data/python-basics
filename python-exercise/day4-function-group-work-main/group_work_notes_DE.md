# Tag 4: Notizen zur Gruppenarbeit

[中文](group_work_notes.md) | [English](group_work_notes_EN.md) | **Deutsch**

Diese Notizen enthalten die beobachteten Code-Ergebnisse und Erklärungen als Referenz.
Eigene Vorhersagen, Gruppengespräche und der Rollenwechsel im Unterricht müssen weiterhin
persönlich durchgeführt werden.

## Aktivität 1: Regeln für die Karten A–H

| Karte | Tatsächliches Ergebnis | Regel in einem Satz |
| --- | --- | --- |
| A | Gibt nacheinander `10.0`, `10.0`, `20.8`, `10.5` aus | Positionsargumente werden der Reihenfolge nach zugeordnet, Schlüsselwortargumente nach Namen; ausgelassene Argumente verwenden ihre Standardwerte. |
| B | Beim Definieren entsteht ein `SyntaxError`; die Datei lässt sich nicht laden | Ein erforderlicher Positionsparameter darf nicht auf einen Positionsparameter mit Standardwert folgen. |
| C | Gibt zuerst `15.0` aus; der zweite Aufruf löst einen `TypeError` aus | Parameter hinter einem einzelnen `*` müssen mit ihrem Namen übergeben werden, damit die Bedeutung der Optionen beim Aufruf klar ist. |
| D | Gibt `(9.0, 27.25)` und `18.25` aus; danach entsteht ein `ValueError` | Mehrere Rückgabewerte bilden ein Tupel; beim Entpacken muss die Anzahl der Zielvariablen passen. |
| E | Gibt zuerst `{'Berlin': 1}` und dann `{'Berlin': 1, 'Köln': 1}` aus | Standardwerte entstehen beim Definieren der Funktion; veränderbare Standardwerte werden deshalb zwischen Aufrufen geteilt. |
| F | Gibt `t-001 {'city': 'Berlin', 'night': True}` und `6.0` aus; danach entsteht ein `TypeError` | In einer Definition sammelt `**extra` Schlüsselwortargumente, beim Aufruf entpackt `**options` ein Dictionary; falsch geschriebene Parameternamen führen weiterhin zu einem Fehler. |
| G | Gibt `{'trip_id': 't-001', 'fare': 12.5}` und `True` aus | Der Parameter verweist auf dasselbe Dictionary; direkte Änderungen betreffen auch den Aufrufer, weshalb bei Bedarf eine Kopie erstellt werden muss. |
| H | Vor der Änderung werden `tools loaded` und `8` ausgegeben, mit der Main-Abfrage nur `8` | Beim ersten Import werden Anweisungen auf Modulebene ausgeführt; Code innerhalb der Main-Abfrage läuft nur beim direkten Start der Datei. |

Zwei Korrekturen für B (nach einer Änderung der Parameterreihenfolge müssen Positionsargumente
beim Aufruf ebenfalls in der neuen Reihenfolge stehen):

```python
def fare(miles, minutes=0):
    return 2.50 + minutes * 0.40 + miles * 1.75

# Alternativ: miles ist erforderlich und nur per Schlüsselwort übergebbar: fare(miles=2)
def fare(minutes=0, *, miles):
    return 2.50 + minutes * 0.40 + miles * 1.75
```

Korrekturen für E und G:

```python
def count_city(city, counts=None):
    if counts is None:
        counts = {}
    counts[city] = counts.get(city, 0) + 1
    return counts


def add_fare(trip):
    return {**trip, "fare": 12.5}
```

H: Beim direkten Start mit `python3 tools.py` erscheint `tools loaded`. Wird
`python3 -c "from tools import double"` aus einem anderen Verzeichnis gestartet und liegt das
Modulverzeichnis nicht im Python-Suchpfad, entsteht ein `ModuleNotFoundError`. Ob der Import
erfolgreich ist, hängt vom Suchpfad ab.

## Aktivität 2: Entwurf des Funktionsbaukastens

Im ursprünglichen Programm waren Tarife, Beispielfahrten und Ausgabeformat fest im Code
vorgegeben. Ergebnisse wurden nur ausgegeben; andere Dateien konnten die berechneten Fahrten
und Statistiken daher nicht direkt wiederverwenden.

| Funktion | Eingabe | Rückgabewert |
| --- | --- | --- |
| `fare_estimate` | Minuten und Meilen; nur per Schlüsselwort: `base`, `per_minute`, `per_mile`, `night`, `minimum` | Fahrpreis mit zwei Nachkommastellen; zuerst wird der Nachtfaktor angewendet, danach der Mindestpreis |
| `split_trips` | Liste von Fahrt-Dictionaries | `(gültige Fahrten, IDs ungültiger Fahrten)` |
| `price_trip` | Eine Fahrt und Tarifoptionen als Schlüsselwortargumente | Neues Dictionary mit `fare`; das ursprüngliche Dictionary bleibt unverändert |
| `summarise` | Liste numerischer Fahrpreise | `(Anzahl, Summe, Durchschnitt)`; bei einer leeren Liste `(0, 0.0, 0.0)` |

Im Beispiel hat t-005 eine negative Minutenzahl. Damit bleiben vier gültige Fahrten mit den
Preisen 12,50, 25,10, 46,50 und 19,00. Die Summe beträgt 103,10 und der Durchschnitt 25,77,
entsprechend dem Ergebnis von Python `round` für diese Gleitkommawerte.

Ausführen und prüfen, jeweils in diesem Verzeichnis:

```bash
python3 fare_tools.py
python3 -c "from fare_tools import fare_estimate; print(fare_estimate(11, 3.2, night=True))"
python3 -m unittest discover -v
```

Der zweite Befehl gibt nur `18.75` aus.

## Gemeinsame Vorstellung: Antwortvorschläge

- Die vorhandene Funktion `fare_estimate` unterstützte bisher nur die Option `night`. Mit den Tarifoptionen als Schlüsselwortargumenten und `minimum` können Aufrufer die Berechnung anpassen, ohne globale Konstanten zu ändern.
- `price_trip` erstellt durch Dictionary-Entpacken ein neues Dictionary und ergänzt nur den Schlüssel `fare` auf der obersten Ebene. Die Eingabe bleibt unverändert. Eine flache Kopie genügt hier, weil keine verschachtelten Objekte verändert werden.
- Ohne Sonderbehandlung der leeren Liste würde die Durchschnittsberechnung durch null teilen. Bei einer Anzahl von null gibt die Funktion jetzt den Durchschnitt `0.0` zurück.
- Die ausdrücklichen Parameter von `fare_estimate` durch beliebige `**kwargs` zu ersetzen, würde die verfügbaren Optionen unklar machen. Als weiterleitende Funktion kann `price_trip` Tarifoptionen sammeln; unbekannte Optionen lösen in `fare_estimate` weiterhin einen `TypeError` aus.


# Python 字典键值获取与容错策略指南

```python
total = 0
for trip in TRIPS:
    total += trip.get('fare', 0)
print(total)
```

## 🇨🇳 第一部分：三种写法的对比与防错分析

在 Python 字典处理中，获取键值（Key）时不同写法的防错效果对比：

| 写法 | 当 `'fare'` 键缺失时的行为 | 后续执行 `total += ...` 的结果 | 适用场景 |
| :--- | :--- | :--- | :--- |
| **`trip['fare']`** | 触发 **`KeyError`** | 程序直接报错中断 | 100% 确定数据存在时 |
| **`trip.get('fare')`** | 返回 **`None`** | 触发 **`TypeError`**（数字无法与 `None` 相加） | 仅读取/检查数据，不参与数值运算时 |
| **`trip.get('fare', 0)`** | 返回默认值 **`0`** | **正常运行**（加上 `0` 不影响总数） | 需要进行数值累加或有默认值保障时 |

---

## 🇨🇳 第二部分：场景选择决策指南

选哪种写法，核心取决于**对数据质量的信心**以及**对错误处理的策略**：

### 1. 使用 `trip['fare']` —— 追求“严格”与“排错”
* **核心逻辑**：只要数据不规范，就**必须报错**，绝不蒙混过关（Fail Fast）。
* **适用场景**：数据严格受控（如数据库 `NOT NULL` 字段）；缺失数据属于严重 Bug，希望程序立即中断以便定位问题。
```python
# 数据处理管道：缺失价格属于严重错误，应该抛出 KeyError 中断程序
fare = trip['fare']
```

### 2. 使用 `trip.get('fare', 0)` —— 追求“健壮”与“容错”
* **核心逻辑**：数据不全没关系，**用默认值垫上**，确保程序平稳运行。
* **适用场景**：数值累加 / 聚合计算（求和、求平均值）；数据源不稳定（爬虫、三方 API、用户输入）。
```python
# 统计总车费：允许部分订单无车费（默认为 0），保证统计顺利完成
total += trip.get('fare', 0)
```

### 3. 使用 `trip.get('fare')` —— 追求“条件判断”与“逻辑分支”
* **核心逻辑**：允许缺失，但需要**显式识别出“它缺失了”**并做专门处理（区分 `None` 与 `0`）。
* **适用场景**：逻辑分支判断。区分“未填写（`None`）”和“免费（`0`）”。
```python
fare = trip.get('fare')

if fare is None:
    print(f"订单 {trip['trip_id']} 缺失金额，标记为待人工审核")
elif fare == 0:
    print(f"订单 {trip['trip_id']} 是免费行程")
else:
    print(f"订单 {trip['trip_id']} 车费为 {fare} 元")
```

---


# Python Dictionary Access Methods & Error Handling Strategies
## 🇬🇧 Part 1: Comparison of Access Methods

Behavior comparison when retrieving a dictionary key in Python:

| Syntax | Behavior when `'fare'` key is missing | Result of `total += ...` | Best Use Case |
| :--- | :--- | :--- | :--- |
| **`trip['fare']`** | Raises **`KeyError`** | Program crashes immediately | When key existence is guaranteed |
| **`trip.get('fare')`** | Returns **`None`** | Raises **`TypeError`** (cannot add `None` to a number) | Simple data lookup without numeric math |
| **`trip.get('fare', 0)`** | Returns default value **`0`** | **Executes safely** (adds `0` without side effects) | Safe numerical accumulation / aggregation |

---

## 🇬🇧 Part 2: Usage Decision Guide

The choice depends on **data reliability** and your **error handling strategy**:

### 1. Using `trip['fare']` — Strictness & Fast Failure
* **Core Logic**: Fail fast if data is missing or corrupted.
* **Use Cases**: Strictly managed datasets (e.g., `NOT NULL` DB fields); critical bugs where early crash facilitates quick debugging.
```python
# Data pipeline: missing key is critical, throw KeyError immediately
fare = trip['fare']
```

### 2. Using `trip.get('fare', 0)` — Robustness & Fault Tolerance
* **Core Logic**: Gracefully handle missing entries with fallback values.
* **Use Cases**: Numerical accumulation/aggregations (sum, average); unstable external APIs, scrapers, or user inputs.
```python
# Total accumulation: default missing entries to 0 without breaking execution
total += trip.get('fare', 0)
```

### 3. Using `trip.get('fare')` — Conditional Logic & Branching
* **Core Logic**: Allow missing keys while explicitly distinguishing missing values (`None`) from actual values (such as `0`).
* **Use Cases**: Branching logic where "Missing (`None`)" differs semantically from "Free (`0`)".
```python
fare = trip.get('fare')

if fare is None:
    print(f"Trip {trip['trip_id']} missing fare data; flagged for review.")
elif fare == 0:
    print(f"Trip {trip['trip_id']} is free.")
else:
    print(f"Trip {trip['trip_id']} fare: {fare}")
```

---


# Python-Wörterbuch-Zugriffsmethoden und Fehlerbehandlungsstrategien
## 🇩🇪 Teil 1: Vergleich der Zugriffsmethoden

Vergleich des Verhaltens beim Zugriff auf einen Dictionary-Schlüssel in Python:

| Syntax | Verhalten, wenn der Schlüssel `'fare'` fehlt | Ergebnis von `total += ...` | Anwendungsbereich |
| :--- | :--- | :--- | :--- |
| **`trip['fare']`** | Wirft ein **`KeyError`** | Programm stürzt sofort ab | Wenn die Existenz des Schlüssels garantiert ist |
| **`trip.get('fare')`** | Gibt **`None`** zurück | Wirft ein **`TypeError`** (Zahl kann nicht mit `None` addiert werden) | Beim reinen Auslesen ohne mathematische Operationen |
| **`trip.get('fare', 0)`** | Gibt den Standardwert **`0`** zurück | **Läuft sicher durch** (Addition von `0` bleibt ohne Fehler) | Sichere Aufsummierung von Zahlenwerten |

---

## 🇩🇪 Teil 2: Entscheidungsleitfaden für die Praxis

Die Wahl hängt von der **Datenqualität** und Ihrer **Fehlerbehandlungsstrategie** ab:

### 1. Verwendung von `trip['fare']` — Striktheit & Schnelles Fehlschlagen (Fail-Fast)
* **Kernlogik**: Das Programm soll sofort abbrechen, wenn Daten fehlen oder ungültig sind.
* **Anwendungsbereich**: Strikt kontrollierte Datenquellen (z. B. Datenbankfelder mit `NOT NULL`); schwerwiegende Fehler, bei denen ein sofortiger Abbruch das Debuggen erleichtert.
```python
# Datenpipeline: Fehlender Schlüssel ist ein kritischer Fehler -> KeyError auslösen
fare = trip['fare']
```

### 2. Verwendung von `trip.get('fare', 0)` — Robustheit & Fehlertoleranz
* **Kernlogik**: Fehlende Einträge werden durch Standardwerte ersetzt, um den Programmablauf nicht zu unterbrechen.
* **Anwendungsbereich**: Numerische Aufsummierung / Berechnungen (Summen, Durchschnitte); instabile Datenquellen (Web Scraper, externe APIs, Benutzereingaben).
```python
# Summenberechnung: Fehlende Beträge als 0 behandeln, ohne die Schleife zu unterbrechen
total += trip.get('fare', 0)
```

### 3. Verwendung von `trip.get('fare')` — Logische Verzweigungen & Bedingungsprüfungen
* **Kernlogik**: Erlaubt fehlende Schlüssel, ermöglicht aber die explizite Unterscheidung zwischen "Fehlend (`None`)" und "Vorhanden (z. B. `0`)".
* **Anwendungsbereich**: Wenn "Keine Angabe (`None`)" sich fachlich von "Kostenlos (`0`)" unterscheidet.
```python
fare = trip.get('fare')

if fare is None:
    print(f"Fahrt {trip['trip_id']}: Fahrpreis fehlt, zur Überprüfung markiert.")
elif fare == 0:
    print(f"Fahrt {trip['trip_id']}: Die Fahrt war kostenlos.")
else:
    print(f"Fahrt {trip['trip_id']}: Fahrpreis beträgt {fare} €.")
```


---
---
# Python 字典遍历三语指南 / Dictionary Traversal Guide / Leitfaden zur Dictionary-Iteration


## 🇨🇳 中文 (Chinese)

Python 字典有三种最核心的遍历方法，对应不同的使用场景：

| 语法 / 方法 | 返回内容 | 代码示例 | 适用场景 / 最佳实践 |
| :--- | :--- | :--- | :--- |
| **`for key in my_dict:`** | 仅键（Key） | `for city in avgs:`<br>`    print(city)` | **最推荐（Pythonic）**。用于只需要使用键的场景。 |
| **`for key in my_dict.keys():`** | 仅键（Key） | `for city in avgs.keys():`<br>`    print(city)` | 结果与直接遍历相同。通常用于强调“只取 Key”的语义，但略显冗余。 |
| **`for val in my_dict.values():`** | 仅值（Value） | `for fare in avgs.values():`<br>`    print(fare)` | 用于只需要数值/内容，不在乎键是什么的场景（例如求总和）。 |
| **`for key, val in my_dict.items():`** | 键和值 (Key, Value) | `for city, fare in avgs.items():`<br>`    print(city, fare)` | **最常用**。利用解包（Unpacking）同时优雅地获取键和值。 |

---

## 🇬🇧 English

Python provides three primary methods for iterating over dictionaries:

| Syntax / Method | Yields | Code Example | Best Practice / Use Case |
| :--- | :--- | :--- | :--- |
| **`for key in my_dict:`** | Keys only | `for city in avgs:`<br>`    print(city)` | **Most Pythonic**. Recommended when only keys are needed. |
| **`for key in my_dict.keys():`** | Keys only | `for city in avgs.keys():`<br>`    print(city)` | Identical output to implicit iteration. Useful for explicit code intent. |
| **`for val in my_dict.values():`** | Values only | `for fare in avgs.values():`<br>`    print(fare)` | Best when operating solely on values (e.g., aggregating totals). |
| **`for key, val in my_dict.items():`** | Key-Value pairs | `for city, fare in avgs.items():`<br>`    print(city, fare)` | **Standard practice** for accessing both key and value via unpacking. |

---

## 🇩🇪 Deutsch

In Python gibt es drei grundlegende Methoden zur Iteration über Dictionaries:

| Syntax / Methode | Rückgabe | Code-Beispiel | Anwendungsbereich & Best Practice |
| :--- | :--- | :--- | :--- |
| **`for key in my_dict:`** | Nur Schlüssel (Keys) | `for city in avgs:`<br>`    print(city)` | **Sehr Pythonic**. Empfohlen, wenn nur die Schlüssel benötigt werden. |
| **`for key in my_dict.keys():`** | Nur Schlüssel (Keys) | `for city in avgs.keys():`<br>`    print(city)` | Identisches Ergebnis. Dient zur expliziten Hervorhebung der Schlüssel-Iteration. |
| **`for val in my_dict.values():`** | Nur Werte (Values) | `for fare in avgs.values():`<br>`    print(fare)` | Optimal, wenn nur Werte verarbeitet werden (z. B. für Summenbildung). |
| **`for key, val in my_dict.items():`** | Schlüssel-Wert-Paare | `for city, fare in avgs.items():`<br>`    print(city, fare)` | **Standardansatz**, um Schlüssel und Wert gleichzeitig per Entpacken (Unpacking) abzurufen. |
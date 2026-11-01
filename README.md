# python-basics

[中文](#中文) · [English](#english) · [Deutsch](#deutsch)

## 中文

Python 基础学习仓库，以出租车行程数据为主线，记录课堂示例、小组作业、个人练习和学习笔记。
内容从字符串处理、字典和函数，逐步扩展到数据校验、CSV / JSON 文件读写和简单的数据处理流程。

### 项目结构

```text
python-basics/
├── README.md
├── ILP-python/                         # Day 1–5 个人练习及测试
│   ├── day-1-string-function-labs-hfan-data/
│   ├── day-2-aggregation-labs-hui-fan/
│   ├── day-3-parsing-and-dead-letter-labs-hui-fan/
│   ├── day-4-function-labs-hui-fan/
│   └── day-5-pipeline-individual-tasks-hui-fan/
└── python-exercise/                    # 课堂示例、小组作业和笔记
    ├── fare_report.py
    ├── city_totals.py
    ├── clean_trips.py
    ├── f-string.md
    ├── README.md
    ├── day4-function-group-work-main/
    └── day5-pipeline-group-work-main/
```

### 内容导航

| 内容 | 学习重点 |
| --- | --- |
| [Day 1 个人练习](ILP-python/day-1-string-function-labs-hfan-data/README.md) | 城市名清洗、时长解析、格式化输出、收据生成 |
| [Day 2 个人练习](ILP-python/day-2-aggregation-labs-hui-fan/README.md) | 去重、按城市分组、平均值、排名 |
| [Day 3 个人练习](ILP-python/day-3-parsing-and-dead-letter-labs-hui-fan/README.md) | CSV 解析、日期校验、时间窗口、JSONL、错误行隔离 |
| [Day 4 个人练习](ILP-python/day-4-function-labs-hui-fan/README.md) | 关键字参数、默认值、字典复制、计价选项转发 |
| [Day 5 个人练习](ILP-python/day-5-pipeline-individual-tasks-hui-fan/README.md) | 无效行识别、城市汇总、循环追踪、文件报告 |
| [Day 4 小组作业](python-exercise/day4-function-group-work-main/README.md) | A–H 规则卡片、可复用计价工具箱、最低价选项 |
| [Day 5 小组作业](python-exercise/day5-pipeline-group-work-main/README.md) | 提取、校验、转换、写出；调试与可重复运行的城市报告 |
| [字典学习笔记](python-exercise/README.md) | 字典取值、容错和遍历，中英德三语 |
| [f-string 速查](python-exercise/f-string.md) | 字符串插值、数字格式和对齐，中文 |

Day 4 小组记录：[中文](python-exercise/day4-function-group-work-main/group_work_notes.md) ·
[English](python-exercise/day4-function-group-work-main/group_work_notes_EN.md) ·
[Deutsch](python-exercise/day4-function-group-work-main/group_work_notes_DE.md)。
Day 5 另有[中文流程设计、追踪表与调试记录](python-exercise/day5-pipeline-group-work-main/group_work_notes.md)。

### 环境与运行

代码使用 Python 标准库，无需安装第三方依赖。类型注解语法需要 Python 3.10 或以上；
本次验证环境为 Python 3.14.4。以下命令适用于 Bash 等兼容 shell，路径以仓库根目录为起点。

```bash
git clone https://github.com/hfan-data/python-basics.git
cd python-basics

# 课堂示例：城市分组与排名
python3 python-exercise/city_totals.py

# Day 4 小组：计价与统计
python3 python-exercise/day4-function-group-work-main/fare_tools.py

# Day 5 小组：生成城市报告
python3 python-exercise/day5-pipeline-group-work-main/broken_city_report.py
```

Day 5 保留原调试练习文件名 `broken_city_report.py`，其中代码已修复。它在自己的目录中读取
`trips.csv`，文件缺失时生成样例；每次运行覆盖 `report.txt`，避免重复追加。
`python-exercise/clean_trips.py` 是 CSV 清洗示例，运行后会在其目录生成 `cleaned.json`
和默认的 `rejects.jsonl`；可通过环境变量 `REJECTS_PATH` 指定错误行输出路径。
`python-exercise/fare_report.py` 主要提供可导入的收据函数，直接运行不会打印报告。

### 测试与学习方式

每个个人练习目录包含 `exercise.py`、`test_exercise.py` 和英德文任务说明。
请进入具体目录运行测试，因为多个练习使用相同的模块名 `exercise`。

```bash
cd ILP-python/day-1-string-function-labs-hfan-data
python3 -m unittest -v
```

也可以从仓库根目录逐个运行全部 7 组测试，任一组失败即停止：

```bash
for lab in ILP-python/day-* python-exercise/day*-group-work-main; do
    (cd "$lab" && python3 -m unittest discover -v) || exit 1
done
```

本次检查：74 项测试全部通过（个人练习 65 项，小组作业 9 项）。
建议按 Day 1 → Day 5 顺序阅读任务、运行示例、理解实现，再用测试核对结果。
学习记录提供参考解释；个人预测、课堂讨论和角色轮换需要本人参与。

## English

A Python learning repository built around taxi trip data. It brings together classroom examples,
group work, individual exercises and study notes, progressing from strings, dictionaries and
functions to validation, CSV / JSON files and small data pipelines.

### Repository Layout and Contents

`ILP-python/` contains the five individual labs, each with `exercise.py`, `test_exercise.py`,
and task descriptions in English and German. `python-exercise/` contains classroom examples,
the Day 4 and Day 5 group work, and study notes. The directory tree is shown in the Chinese section above.

| Material | Main topics |
| --- | --- |
| [Day 1 individual lab](ILP-python/day-1-string-function-labs-hfan-data/README.md) | City name cleaning, duration parsing, formatting and receipts |
| [Day 2 individual lab](ILP-python/day-2-aggregation-labs-hui-fan/README.md) | Deduplication, grouping, averages and rankings |
| [Day 3 individual lab](ILP-python/day-3-parsing-and-dead-letter-labs-hui-fan/README.md) | CSV parsing, date validation, time windows, JSONL and rejected rows |
| [Day 4 individual lab](ILP-python/day-4-function-labs-hui-fan/README.md) | Keyword arguments, defaults, dictionary copying and forwarding pricing options |
| [Day 5 individual lab](ILP-python/day-5-pipeline-individual-tasks-hui-fan/README.md) | Finding rejected rows, city totals, loop tracing and file reports |
| [Day 4 group work](python-exercise/day4-function-group-work-main/README.md) | Rule cards A–H, a reusable fare toolkit and a minimum fare option |
| [Day 5 group work](python-exercise/day5-pipeline-group-work-main/README.md) | Extract, validate, transform and load; debugging and repeatable city reports |
| [Dictionary notes](python-exercise/README.md) | Dictionary access, error handling and iteration, in Chinese, English and German |
| [f-string reference](python-exercise/f-string.md) | Interpolation, numeric formatting and alignment, in Chinese |

Day 4 group notes: [English](python-exercise/day4-function-group-work-main/group_work_notes_EN.md) ·
[Deutsch](python-exercise/day4-function-group-work-main/group_work_notes_DE.md) ·
[中文](python-exercise/day4-function-group-work-main/group_work_notes.md).
Day 5 also includes [pipeline design, a trace table and debugging notes in Chinese](python-exercise/day5-pipeline-group-work-main/group_work_notes.md).

### Requirements and Running Examples

The code uses only the Python standard library; no third-party dependencies are required.
Type annotation syntax requires Python 3.10 or later. This revision was checked with Python 3.14.4.
The commands below use Bash or a compatible shell and start from the repository root.

```bash
git clone https://github.com/hfan-data/python-basics.git
cd python-basics

# Classroom example: city grouping and ranking
python3 python-exercise/city_totals.py

# Day 4 group work: pricing and statistics
python3 python-exercise/day4-function-group-work-main/fare_tools.py

# Day 5 group work: generate a city report
python3 python-exercise/day5-pipeline-group-work-main/broken_city_report.py
```

The Day 5 script retains its original debugging exercise name, `broken_city_report.py`, but has
been corrected. It reads `trips.csv` from its own directory, creates sample input if missing,
and overwrites `report.txt` on every run to prevent duplicate output.
The classroom cleaner, `python-exercise/clean_trips.py`, writes `cleaned.json` and, by default,
`rejects.jsonl` beside the script. Set `REJECTS_PATH` to choose another rejected-row output path.
`python-exercise/fare_report.py` provides importable receipt functions; running it directly prints no report.

### Testing and Learning

Run individual lab tests from that lab's directory. Several labs use the same module name,
`exercise`, so each test suite should run separately.

```bash
cd ILP-python/day-1-string-function-labs-hfan-data
python3 -m unittest -v
```

To run all seven suites from the repository root, stopping if any suite fails:

```bash
for lab in ILP-python/day-* python-exercise/day*-group-work-main; do
    (cd "$lab" && python3 -m unittest discover -v) || exit 1
done
```

Verification for this revision: all 74 tests passed (65 individual lab tests and 9 group work tests).
Work through Day 1 to Day 5: read each task, run examples, understand the implementation and
check the results with tests. Study notes provide reference explanations; personal predictions,
classroom discussions and role rotation still require participation in person.

## Deutsch

Ein Lernrepository zu Python-Grundlagen anhand von Taxifahrtdaten. Es enthält Unterrichtsbeispiele,
Gruppenarbeiten, Einzelübungen und Lernnotizen. Die Themen reichen von Zeichenketten, Dictionaries
und Funktionen bis zu Datenvalidierung, CSV-/JSON-Dateien und einfachen Datenpipelines.

### Aufbau und Inhalte

`ILP-python/` enthält die fünf Einzelübungen, jeweils mit `exercise.py`, `test_exercise.py`
und Aufgabenbeschreibungen auf Englisch und Deutsch. In `python-exercise/` liegen Unterrichtsbeispiele,
die Gruppenarbeiten für Tag 4 und Tag 5 sowie Lernnotizen. Der Verzeichnisbaum steht oben im chinesischen Abschnitt.

| Material | Schwerpunkte |
| --- | --- |
| [Tag 1: Einzelübung](ILP-python/day-1-string-function-labs-hfan-data/README_DE.md) | Stadtnamen bereinigen, Dauer auslesen, Formatierung und Belege |
| [Tag 2: Einzelübung](ILP-python/day-2-aggregation-labs-hui-fan/README_DE.md) | Duplikate entfernen, gruppieren, Durchschnittswerte und Ranglisten |
| [Tag 3: Einzelübung](ILP-python/day-3-parsing-and-dead-letter-labs-hui-fan/README_DE.md) | CSV-Verarbeitung, Datumsprüfung, Zeitfenster, JSONL und abgewiesene Zeilen |
| [Tag 4: Einzelübung](ILP-python/day-4-function-labs-hui-fan/README_DE.md) | Schlüsselwortargumente, Standardwerte, Dictionary-Kopien und Weitergabe von Tarifoptionen |
| [Tag 5: Einzelübung](ILP-python/day-5-pipeline-individual-tasks-hui-fan/README_DE.md) | Ungültige Zeilen erkennen, Stadtsummen, Schleifen nachverfolgen und Berichte schreiben |
| [Tag 4: Gruppenarbeit](python-exercise/day4-function-group-work-main/README_DE.md) | Regelkarten A–H, wiederverwendbare Tarifberechnung und Mindestpreis |
| [Tag 5: Gruppenarbeit](python-exercise/day5-pipeline-group-work-main/README_DE.md) | Extrahieren, validieren, transformieren und schreiben; Fehlersuche und wiederholbare Stadtberichte |
| [Dictionary-Notizen](python-exercise/README.md) | Zugriff, Fehlerbehandlung und Iteration auf Chinesisch, Englisch und Deutsch |
| [f-string-Kurzübersicht](python-exercise/f-string.md) | Ausdrücke einbetten, Zahlen formatieren und Text ausrichten, auf Chinesisch |

Notizen zur Gruppenarbeit an Tag 4: [Deutsch](python-exercise/day4-function-group-work-main/group_work_notes_DE.md) ·
[English](python-exercise/day4-function-group-work-main/group_work_notes_EN.md) ·
[中文](python-exercise/day4-function-group-work-main/group_work_notes.md).
Für Tag 5 gibt es außerdem [Pipeline-Entwurf, Nachverfolgungstabelle und Debugging-Notizen auf Chinesisch](python-exercise/day5-pipeline-group-work-main/group_work_notes.md).

### Voraussetzungen und Ausführung

Der Code verwendet ausschließlich die Python-Standardbibliothek; zusätzliche Pakete sind nicht nötig.
Die Syntax der Typannotationen setzt Python 3.10 oder neuer voraus. Diese Version des Repositorys
wurde mit Python 3.14.4 geprüft. Die folgenden Befehle verwenden Bash oder eine kompatible Shell
und gehen vom Stammverzeichnis des Repositorys aus.

```bash
git clone https://github.com/hfan-data/python-basics.git
cd python-basics

# Unterrichtsbeispiel: Gruppierung und Rangliste nach Stadt
python3 python-exercise/city_totals.py

# Gruppenarbeit Tag 4: Fahrpreise und Statistik
python3 python-exercise/day4-function-group-work-main/fare_tools.py

# Gruppenarbeit Tag 5: Stadtbericht erzeugen
python3 python-exercise/day5-pipeline-group-work-main/broken_city_report.py
```

Das Skript für Tag 5 behält den ursprünglichen Namen der Debugging-Aufgabe,
`broken_city_report.py`, ist aber bereits korrigiert. Es liest `trips.csv` aus seinem eigenen
Verzeichnis, erzeugt bei fehlender Eingabedatei Beispieldaten und überschreibt `report.txt`
bei jedem Lauf, damit keine doppelten Einträge entstehen.
Das Unterrichtsbeispiel `python-exercise/clean_trips.py` schreibt `cleaned.json` und standardmäßig
`rejects.jsonl` in sein Verzeichnis. Mit der Umgebungsvariablen `REJECTS_PATH` lässt sich ein anderer
Ausgabepfad für abgewiesene Zeilen festlegen. `python-exercise/fare_report.py` stellt importierbare
Funktionen zur Belegerstellung bereit; beim direkten Start wird kein Bericht ausgegeben.

### Tests und Lernweg

Die Tests jeder Einzelübung werden in deren eigenem Verzeichnis gestartet. Mehrere Übungen
verwenden denselben Modulnamen `exercise`; deshalb werden die Tests getrennt ausgeführt.

```bash
cd ILP-python/day-1-string-function-labs-hfan-data
python3 -m unittest -v
```

Alle sieben Testgruppen lassen sich vom Stammverzeichnis aus ausführen. Bei einem Fehler stoppt der Durchlauf:

```bash
for lab in ILP-python/day-* python-exercise/day*-group-work-main; do
    (cd "$lab" && python3 -m unittest discover -v) || exit 1
done
```

Prüfergebnis dieser Version: Alle 74 Tests bestanden (65 Tests der Einzelübungen und 9 Tests der Gruppenarbeiten).
Die Aufgaben bauen von Tag 1 bis Tag 5 aufeinander auf: Aufgabenstellung lesen, Beispiele ausführen,
Implementierung verstehen und Ergebnisse mit Tests prüfen. Die Lernnotizen bieten Erklärungen als
Referenz; eigene Vorhersagen, Unterrichtsgespräche und Rollenwechsel erfordern persönliche Teilnahme.

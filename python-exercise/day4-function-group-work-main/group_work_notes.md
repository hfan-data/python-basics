# Day 4 小组作业记录

以下是代码运行结果与参考解释；课堂上的个人预测、组员讨论和角色轮换需要本人完成。

## Activity 1：A–H 规则表

| 卡片 | 实际结果 | 一句话规则 |
| --- | --- | --- |
| A | 依次输出 `10.0`、`10.0`、`20.8`、`10.5` | 位置参数按顺序绑定，关键字参数按名称绑定，省略的参数使用默认值。 |
| B | 定义时发生 `SyntaxError`，文件不能加载 | 普通位置参数中，没有默认值的参数不能放在有默认值的参数后面。 |
| C | 先输出 `15.0`，第二次调用触发 `TypeError` | 裸 `*` 后面的参数只能按名称传递，让调用者清楚选项含义。 |
| D | 输出 `(9.0, 27.25)` 和 `18.25`，最后触发 `ValueError` | 多返回值组成元组，解包变量数量必须匹配。 |
| E | 先输出 `{'Berlin': 1}`，再输出 `{'Berlin': 1, 'Köln': 1}` | 默认参数在定义时创建，可变默认值会在调用之间共享。 |
| F | 输出 `t-001 {'city': 'Berlin', 'night': True}`、`6.0`，最后触发 `TypeError` | 定义中的 `**extra` 收集关键字，调用中的 `**options` 展开字典，拼错参数名仍会报错。 |
| G | 输出 `{'trip_id': 't-001', 'fare': 12.5}` 和 `True` | 参数引用同一个字典，原地修改会影响调用者；用副本避免这种影响。 |
| H | 修改前输出 `tools loaded` 和 `8`；加 guard 后只输出 `8` | 首次导入会执行模块顶层语句，guard 内代码仅在直接运行时执行。 |

B 的两种修复（调整位置后，调用时也应遵守新的顺序）：

```python
def fare(miles, minutes=0):
    return 2.50 + minutes * 0.40 + miles * 1.75

# 或者让必填的 miles 成为关键字参数：fare(miles=2)
def fare(minutes=0, *, miles):
    return 2.50 + minutes * 0.40 + miles * 1.75
```

E 与 G 的修复：

```python
def count_city(city, counts=None):
    if counts is None:
        counts = {}
    counts[city] = counts.get(city, 0) + 1
    return counts


def add_fare(trip):
    return {**trip, "fare": 12.5}
```

H：直接执行 `python3 tools.py` 输出 `tools loaded`。如果从其他目录启动
`python3 -c "from tools import double"`，且模块目录不在 Python 搜索路径中，会报
`ModuleNotFoundError`；是否可导入取决于搜索路径。

## Activity 2：工具箱设计

原程序把费率、样例行程和输出格式写死，只打印结果，其他文件不能直接复用计价后的数据与统计结果。

| 函数 | 输入 | 返回 |
| --- | --- | --- |
| `fare_estimate` | 分钟、英里；仅限关键字的 `base`、`per_minute`、`per_mile`、`night`、`minimum` | 保留两位小数的车费；先应用夜间系数，再应用最低价 |
| `split_trips` | 行程字典列表 | `(有效行程列表, 无效行程 ID 列表)` |
| `price_trip` | 一个行程及关键字计价选项 | 含 `fare` 的新字典，原字典不变 |
| `summarise` | 数值车费列表 | `(数量, 总价, 平均价)`；空列表为 `(0, 0.0, 0.0)` |

样例中 t-005 的分钟为负数，因此有效行程 4 条；车费分别为 12.50、25.10、46.50、19.00，
总价 103.10，平均价 25.77（按 Python `round` 的结果）。

运行与检查：

```bash
python3 fare_tools.py
python3 -c "from fare_tools import fare_estimate; print(fare_estimate(11, 3.2, night=True))"
python3 -m unittest discover -v
```

第二条命令只输出 `18.75`。

## Share-out 参考回答

- 现有 `fare_estimate` 原本只支持 `night`；现在增加关键字费率和 `minimum`，调用者无需改全局常量。
- `price_trip` 使用字典展开创建新字典，只添加顶层 `fare`，不会修改输入。这里的浅拷贝已经足够，因为没有修改嵌套对象。
- 未处理空列表时，平均值计算会除以零；现在数量为零时直接返回平均值 `0.0`。
- `fare_estimate` 不适合用任意 `**kwargs` 代替明确参数，否则选项不清晰。`price_trip` 是转发层，适合收集计价选项；未知选项仍由 `fare_estimate` 抛出 `TypeError`。

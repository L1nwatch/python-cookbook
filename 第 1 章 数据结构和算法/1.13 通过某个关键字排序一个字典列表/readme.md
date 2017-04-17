### 1.13 通过某个关键字排序一个字典列表

#### 问题

你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表。

#### 解决方案

通过使用 `operator` 模块的 `itemgetter` 函数，可以非常容易的排序这样的数据结构

```python
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
```

`itemgetter()` 函数也支持多个keys

```python
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
```

#### 讨论

`operator.itemgetter()` 函数有一个被 `rows` 中的记录用来查找值的索引参数。可以是一个字典键名称， 一个整形值或者任何能够传入一个对象的 `__getitem__()` 方法的值。

`itemgetter()` 有时候也可以用 `lambda` 表达式代替

```python
rows_by_fname = sorted(rows, key=lambda r: r['fname']
```

但是，使用 `itemgetter()` 方式会运行的稍微快点。因此，如果你对性能要求比较高的话就使用 `itemgetter()` 方式。

不要忘了这节中展示的技术也同样适用于 `min()` 和 `max()` 等函数。比如：

```python
>>> min(rows, key=itemgetter('uid'))
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001}
>>> max(rows, key=itemgetter('uid'))
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
```


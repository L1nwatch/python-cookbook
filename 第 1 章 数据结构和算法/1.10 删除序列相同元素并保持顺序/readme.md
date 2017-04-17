### 1.10 删除序列相同元素并保持顺序

#### 问题

怎样在一个序列上面保持元素顺序的同时消除重复的值？

#### 解决方案

如果序列上的值都是 `hashable` 类型

```python
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
        seen.add(item)
```

如果你想消除元素不可哈希(比如 `dict` 类型)的序列中重复元素的话

```python
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
```

这里的key参数指定了一个函数，将序列元素转换成 `hashable` 类型

```python
>>> a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
>>> list(dedupe(a, key=lambda d: (d['x'],d['y'])))
[{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
>>> list(dedupe(a, key=lambda d: d['x']))
[{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
```

#### 讨论

如果你仅仅就是想消除重复元素，通常可以简单的构造一个集合
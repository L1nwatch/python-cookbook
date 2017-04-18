### 1.20 合并多个字典或映射

#### 问题

合并多个字典或映射，之后还要对其进行操作，如何实现？

#### 解决方案

假设你必须在两个字典中执行查找操作(比如先从 `a` 中找，如果找不到再在 `b` 中找)。 一个非常简单的解决方案就是使用 `collections` 模块中的 `ChainMap` 类。比如：

```python
from collections import ChainMap
c = ChainMap(a,b)
print(c['x']) # Outputs 1 (from a)
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a)
```

#### 讨论

一个 `ChainMap` 接受多个字典并将它们在逻辑上变为一个字典。 然后，这些字典并不是真的合并在一起了， `ChainMap` 类只是在内部创建了一个容纳这些字典的列表 并重新定义了一些常见的字典操作来遍历这个列表。大部分字典操作都是可以正常使用的。

如果出现重复键，那么第一次出现的映射值会被返回。

对于字典的更新或删除操作总是影响的是列表中第一个字典。

`ChainMap` 对于编程语言中的作用范围变量(比如 `globals` , `locals` 等)是非常有用的。 事实上，有一些方法可以使它变得简单：

```python
>>> values = ChainMap()
>>> values['x'] = 1
>>> # Add a new mapping
>>> values = values.new_child()
>>> values['x'] = 2
>>> # Add a new mapping
>>> values = values.new_child()
>>> values['x'] = 3
>>> values
ChainMap({'x': 3}, {'x': 2}, {'x': 1})
>>> values['x']
3
>>> # Discard last mapping
>>> values = values.parents
>>> values['x']
2
>>> # Discard last mapping
>>> values = values.parents
>>> values['x']
1
>>> values
ChainMap({'x': 1})
```

作为 `ChainMap` 的替代，你可能会考虑使用 `update()` 方法将两个字典合并。这样也能行得通，但是它需要你创建一个完全不同的字典对象(或者是破坏现有字典结构)。 同时，如果原字典做了更新，这种改变不会反应到新的合并字典中去。

`ChainMap` 使用原来的字典，它自己不创建新的字典。所以它并不会产生上面所说的结果。
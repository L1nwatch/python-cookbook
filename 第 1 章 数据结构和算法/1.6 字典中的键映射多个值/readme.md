### 1.6 字典中的键映射多个值

#### 问题

怎样实现一个键对应多个值的字典(也叫 `multidict` )？

#### 解决方案

依旧是依靠字典一个键对应一个值，但是这个值可以是列表之类的，这样就实现了一个键对应多个值了。

你可以很方便的使用 `collections` 模块中的 `defaultdict` 来构造这样的字典。`defaultdict` 的一个特征是它会自动初始化每个 `key` 刚开始对应的值，所以你只需要关注添加元素操作了。比如：

```python
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
```

你可以在一个普通的字典上使用 `setdefault()` 方法来代替。比如：

```python
d = {} # A regular dictionary
d.setdefault('a', []).append(1)
```

#### 讨论

创建一个多值映射字典是很简单的。但是，如果你选择自己实现的话，那么对于值的初始化可能会有点麻烦

```python
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)
```

如果使用 `defaultdict` 的话代码就更加简洁了：

```python
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
```


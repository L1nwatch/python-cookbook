### 1.11 命名切片

#### 问题

代码中出现了一大堆硬编码切片下标

#### 解决方案

命名切片

```python
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
```

#### 讨论

内置的 `slice()` 函数创建了一个切片对象，可以被用在任何切片允许使用的地方。比如：

```python
>>> items = [0, 1, 2, 3, 4, 5, 6]
>>> a = slice(2, 4)
>>> items[2:4]
[2, 3]
>>> items[a]
[2, 3]
>>> items[a] = [10,11]
>>> items
[0, 1, 10, 11, 4, 5, 6]
>>> del items[a]
>>> items
[0, 1, 4, 5, 6]
```

如果你有一个切片对象a，你可以分别调用它的 `a.start` , `a.stop` , `a.step` 属性来获取更多的信息。比如：

```python
>>> a = slice(5, 50, 2)
>>> a.start
5
>>> a.stop
50
>>> a.step
2
```

另外，你还能通过调用切片的 `indices(size)` 方法将它映射到一个确定大小的序列上， 这个方法返回一个三元组 `(start, stop, step)` ，所有值都会被合适的缩小以满足边界限制， 从而使用的时候避免出现 `IndexError` 异常。比如：

```python
>>> s = 'HelloWorld'
>>> a.indices(len(s))
(5, 10, 2)
>>> for i in range(*a.indices(len(s))):
... print(s[i])
...
W
r
d
```


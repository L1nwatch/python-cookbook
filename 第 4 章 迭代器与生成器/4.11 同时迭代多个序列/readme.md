### 4.11 同时迭代多个序列

#### 问题

想同时迭代多个序列，每次分别从一个序列中取一个元素。

#### 解决方案

为了同时迭代多个序列，使用 `zip()` 函数。比如：

```python
>>> xpts = [1, 5, 4, 2, 10, 7]
>>> ypts = [101, 78, 37, 15, 62, 99]
>>> for x, y in zip(xpts, ypts):
...     print(x,y)
```

`zip(a, b)` 会生成一个可返回元组 `(x, y)` 的迭代器，其中x来自a，y来自b。

迭代长度跟参数中最短序列长度一致。

如果这个不是你想要的效果，那么还可以使用 `itertools.zip_longest()` 函数来代替。

```python
>>> from itertools import zip_longest
>>> for i in zip_longest(a,b):
...     print(i)
...
(1, 'w')
(2, 'x')
(3, 'y')
(None, 'z')

>>> for i in zip_longest(a, b, fillvalue=0):
...     print(i)
...
(1, 'w')
(2, 'x')
(3, 'y')
(0, 'z')
```

#### 讨论

使用zip()可以打包并生成一个字典：

```python
headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
s = dict(zip(headers,values))
```

`zip()` 可以接受多于两个的序列的参数

```python
>>> a = [1, 2, 3]
>>> b = [10, 11, 12]
>>> c = ['x','y','z']
>>> for i in zip(a, b, c):
...     print(i)
```

`zip()` 会创建一个迭代器来作为结果返回。 如果你需要将结对的值存储在列表中，要使用 `list()` 函数。
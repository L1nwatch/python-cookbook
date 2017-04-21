### 4.10 序列上索引值迭代

#### 问题

想在迭代一个序列的同时跟踪正在被处理的元素索引。

#### 解决方案

内置的 `enumerate()` 函数可以很好的解决这个问题：

```python
>>> my_list = ['a', 'b', 'c']
>>> for idx, val in enumerate(my_list):
...     print(idx, val)
...
0 a
```

为了按传统行号输出(行号从1开始)，你可以传递一个开始参数：

```python
>>> for idx, val in enumerate(my_list, 1)
```

`enumerate()` 对于跟踪某些值在列表中出现的位置是很有用的。 

#### 讨论

， 有时候当你在一个已经解压后的元组序列上使用 `enumerate()` 函数时很容易调入陷阱。 你得像下面正确的方式这样写：

```python
data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]

# Correct!
for n, (x, y) in enumerate(data):
    ...
# Error!
for n, x, y in enumerate(data):
    ...
```


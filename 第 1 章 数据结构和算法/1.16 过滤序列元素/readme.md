### 1.16 过滤序列元素

#### 问题

你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列

#### 解决方案

最简单的过滤序列元素的方法就是使用列表推导。

使用列表推导的一个潜在缺陷就是如果输入非常大的时候会产生一个非常大的结果集，占用大量内存。 如果你对内存比较敏感，那么你可以使用生成器表达式迭代产生过滤的元素。比如：

```python
>>> pos = (n for n in mylist if n > 0)
>>> pos
<generator object <genexpr> at 0x1006a0eb0>
>>> for x in pos:
... print(x)
```

有时候，过滤规则比较复杂，使用内建的 `filter()` 函数

```python
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
```

#### 讨论

过滤操作的一个变种就是将不符合条件的值用新的值代替，而不是丢弃它们

```python
>>> clip_neg = [n if n > 0 else 0 for n in mylist]
```

另外一个值得关注的过滤工具就是 `itertools.compress()` ， 它以一个 `iterable` 对象和一个相对应的 `Boolean` 选择器序列作为输入参数。 然后输出 `iterable` 对象中对应选择器为 `True` 的元素。 当你需要用另外一个相关联的序列来过滤某个序列的时候，这个函数是非常有用的。 

```python
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

>>> from itertools import compress
>>> more5 = [n > 5 for n in counts]
>>> more5
[False, False, True, False, False, True, True, False]
>>> list(compress(addresses, more5))
['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']
```

和 `filter()` 函数类似， `compress()` 也是返回的一个迭代器。
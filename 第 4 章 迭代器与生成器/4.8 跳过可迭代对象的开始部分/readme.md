### 4.8 跳过可迭代对象的开始部分

#### 问题

想遍历一个可迭代对象，但是它开始的某些元素你并不感兴趣，想跳过它们。

#### 解决方案

`itertools` 模块中有一些函数可以完成这个任务。 首先介绍的是 `itertools.dropwhile()`函数。使用时，你给它传递一个函数对象和一个可迭代对象。 它会返回一个迭代器对象，丢弃原有序列中直到函数返回Flase之前的所有元素，然后返回后面所有元素。

为了演示，假定你在读取一个开始部分是几行注释的源文件。比如：

```python
>>> from itertools import dropwhile
>>> with open('/etc/passwd') as f:
...     for line in dropwhile(lambda line: line.startswith('#'), f):
...         print(line, end='')
```

如果你已经明确知道了要跳过的元素的个数的话，那么可以使用 `itertools.islice()` 来代替。比如：

```python
>>> from itertools import islice
>>> items = ['a', 'b', 'c', 1, 4, 10, 15]
>>> for x in islice(items, 3, None):
...     print(x)
...
1
4
10
15
```

`islice()` 函数最后那个 `None` 参数指定了你要获取从第3个到最后的所有元素， 如果 `None` 和3的位置对调，意思就是仅仅获取前三个元素恰恰相反， (这个跟切片的相反操作 `[3:]` 和 `[:3]` 原理是一样的)。

#### 讨论

跳过一个可迭代对象的开始部分跟通常的过滤是不同的。 比如：

```python
with open('/etc/passwd') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')
```

这样写确实可以跳过开始部分的注释行，但是同样也会跳过文件中其他所有的注释行。 

本节的方案适用于所有可迭代对象，包括那些事先不能确定大小的， 比如生成器，文件及其类似的对象。
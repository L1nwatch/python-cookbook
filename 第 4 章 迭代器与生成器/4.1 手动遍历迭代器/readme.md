### 4.1 手动遍历迭代器

#### 问题

不使用 for 循环来实现迭代器

#### 解决方案

使用 `next()` 函数并在代码中捕获 `StopIteration` 异常。

通常来讲， `StopIteration` 用来指示迭代的结尾。 然而，你还可以通过返回一个指定值来标记结尾，比如 `None` 。 

```python
def manual_iter():
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass
# same
with open('/etc/passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')
```

#### 讨论

下面的交互示例向我们演示了迭代期间所发生的基本细节：

```python
>>> items = [1, 2, 3]
>>> # Get the iterator
>>> it = iter(items) # Invokes items.__iter__()
>>> # Run the iterator
>>> next(it) # Invokes it.__next__()
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
StopIteration
```


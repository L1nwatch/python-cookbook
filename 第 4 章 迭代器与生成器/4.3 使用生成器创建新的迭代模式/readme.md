### 4.3 使用生成器创建新的迭代模式

#### 问题

想自定义迭代模式

#### 解决方案

如果你想实现一种新的迭代模式，使用一个生成器函数来定义它。

```python
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment
```

#### 讨论

一个函数中需要有一个 `yield` 语句即可将其转换为一个生成器。

一个生成器函数主要特征是它只会回应在迭代中使用到的 *next* 操作。 一旦生成器函数返回退出，迭代终止。
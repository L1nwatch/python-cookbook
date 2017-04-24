### 7.6 定义匿名或内联函数

#### 问题

你想为 `sort()` 操作创建一个很短的回调函数，但又不想用 `def` 去写一个单行函数， 而是希望通过某个快捷方式以内联方式来创建这个函数。

#### 解决方案

可以使用lambda表达式来代替。lambda表达式典型的使用场景是排序或数据reduce等：

```python
>>> names = ['David Beazley', 'Brian Jones',
...         'Raymond Hettinger', 'Ned Batchelder']
>>> sorted(names, key=lambda name: name.split()[-1].lower())
```

#### 讨论

尽管lambda表达式允许你定义简单函数，但是它的使用是有限制的。 你只能指定单个表达式，它的值就是最后的返回值。
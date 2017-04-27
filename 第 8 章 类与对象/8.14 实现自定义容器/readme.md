### 8.14 实现自定义容器

#### 问题

你想实现一个自定义的类来模拟内置的容器类功能，比如列表和字典。但是你不确定到底要实现哪些方法。

#### 解决方案

`collections` 定义了很多抽象基类，当你想自定义容器类的时候它们会非常有用。 比如你想让你的类支持迭代，那就让你的类继承 `collections.Iterable` 即可：

```python
import collections
class A(collections.Iterable):
    pass
```

你可以先试着去实例化一个对象，在错误提示中可以找到需要实现哪些方法。

`bisect` 模块，它是一个在排序列表中插入元素的高效方式。可以保证元素插入后还保持顺序。

#### 讨论

`collections` 中很多抽象类会为一些常见容器操作提供默认的实现， 这样一来你只需要实现那些你最感兴趣的方法即可。假设你的类继承自 `collections.MutableSequence` ，如下：

```python
class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, index):
        print('Getting:', index)
        return self._items[index]

    def __setitem__(self, index, value):
        print('Setting:', index, value)
        self._items[index] = value

    def __delitem__(self, index):
        print('Deleting:', index)
        del self._items[index]

    def insert(self, index, value):
        print('Inserting:', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('Len')
        return len(self._items)
```

如果你创建 `Items` 的实例，你会发现它支持几乎所有的核心列表方法(如append()、remove()、count()等)。 

`numbers` 模块提供了一个类似的跟整数类型相关的抽象类型集合。
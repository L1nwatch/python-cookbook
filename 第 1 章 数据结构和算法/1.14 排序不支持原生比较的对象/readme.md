### 1.14 排序不支持原生比较的对象

#### 问题

你想排序类型相同的对象，但是他们不支持原生的比较操作。

#### 解决方案

内置的 `sorted()` 函数有一个关键字参数 `key` ，可以传入一个 `callable` 对象给它

```python
class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)

def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(sorted(users, key=lambda u: u.user_id))
```

另外一种方式是使用 `operator.attrgetter()` 来代替lambda函数：

```python
>>> from operator import attrgetter
>>> sorted(users, key=attrgetter('user_id'))
[User(3), User(23), User(99)]
```

#### 讨论

`attrgetter()`函数通常会运行的快点，并且还能同时允许多个字段进行比较。 这个跟 `operator.itemgetter()` 函数作用于字典类型很类似。

这一小节用到的技术同样适用于像 `min()` 和 `max()` 之类的函数
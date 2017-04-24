### 7.1 可接受任意数量参数的函数

#### 问题

你想构造一个可接受任意数量参数的函数。

#### 解决方案

可以使用一个\*参数。

为了接受任意数量的关键字参数，使用一个以\*\*开头的参数。

如果你还希望某个函数能同时接受任意数量的位置参数和关键字参数，可以同时使用*和**。

#### 讨论

一个\*参数只能出现在函数定义中最后一个位置参数后面，而 [\*\*](http://python3-cookbook.readthedocs.io/zh_CN/latest/c07/p01_functions_that_accept_any_number_arguments.html#id5)参数只能出现在最后一个参数。 有一点要注意的是，在\*参数后面仍然可以定义其他参数。

```python
def a(x, *args, y):
    pass

def b(x, *args, y, **kwargs):
    pass
```

这种参数就是我们所说的强制关键字参数。
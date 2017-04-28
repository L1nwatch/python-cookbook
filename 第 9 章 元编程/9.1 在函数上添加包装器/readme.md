### 9.1 在函数上添加包装器

#### 问题

你想在函数上添加一个包装器，增加额外的操作处理(比如日志、计时等)。

#### 解决方案

如果你想使用额外的代码包装一个函数，可以定义一个装饰器函数，例如：

```python
import time
from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper
```

下面是使用装饰器的例子：

```python
>>> @timethis
... def countdown(n):
...     '''
...     Counts down
...     '''
...     while n > 0:
...         n -= 1
...
>>> countdown(100000)
countdown 0.008917808532714844
>>> countdown(10000000)
countdown 0.87188299392912
```

#### 讨论

在上面的 `wrapper()` 函数中， 装饰器内部定义了一个使用 `*args` 和 `**kwargs` 来接受任意参数的函数。 在这个函数里面调用了原始函数并将其结果返回，不过你还可以添加其他额外的代码(比如计时)。 然后这个新的函数包装器被作为结果返回来代替原始函数。

需要强调的是装饰器并不会修改原始函数的参数签名以及返回值。 使用 `*args` 和`**kwargs` 目的就是确保任何参数都能适用。 而返回结果值基本都是调用原始函数 `func(*args, **kwargs)` 的返回结果，其中func就是原始函数。

上面使用 `@wraps(func)` 注解是很重要的， 它能保留原始函数的元数据(下一小节会讲到)，新手经常会忽略这个细节。
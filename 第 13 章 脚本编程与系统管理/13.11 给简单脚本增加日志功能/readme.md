### 13.11 给简单脚本增加日志功能

#### 问题

你希望在脚本和程序中将诊断信息写入日志文件。

#### 解决方案

打印日志最简单方式是使用 `logging` 模块。例如：

```python
import logging

def main():
    # Configure the logging system
    logging.basicConfig(
        filename='app.log',
        level=logging.ERROR
    )

    # Variables (to make the calls that follow work)
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    # Example logging calls (insert into your program)
    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')

if __name__ == '__main__':
    main()
```

`basicConfig()` 的 `level` 参数是一个过滤器。 所有级别低于此级别的日志消息都会被忽略掉。 每个 logging 操作的参数是一个消息字符串，后面再跟一个或多个参数。 

运行这个程序后，在文件 `app.log` 中的内容应该是下面这样：

```shell
CRITICAL:root:Host www.python.org unknown
ERROR:root:Could not find 'spam'
```

如果你想改变输出等级，你可以修改 `basicConfig()` 调用中的参数。例如：

```python
logging.basicConfig(
     filename='app.log',
     level=logging.WARNING,
     format='%(levelname)s:%(asctime)s:%(message)s')
```

上面的日志配置都是硬编码到程序中的。如果你想使用配置文件， 可以像下面这样修改 `basicConfig()` 调用：

```python
import logging
import logging.config

def main():
    # Configure the logging system
    logging.config.fileConfig('logconfig.ini')
    # ...
```

创建一个下面这样的文件，名字叫 `logconfig.ini` ：

```ini
[loggers]
keys=root

[handlers]
keys=defaultHandler

[formatters]
keys=defaultFormatter

[logger_root]
level=INFO
handlers=defaultHandler
qualname=root

[handler_defaultHandler]
class=FileHandler
formatter=defaultFormatter
args=('app.log', 'a')

[formatter_defaultFormatter]
format=%(levelname)s:%(name)s:%(message)s
```

#### 讨论

如果你想要你的日志消息写到标准错误中，而不是日志文件中，调用 `basicConfig()` 时不传文件名参数即可。例如：

```python
logging.basicConfig(level=logging.INFO)
```

`basicConfig()` 在程序中只能被执行一次。如果你稍后想改变日志配置， 就需要先获取 `root logger` ，然后直接修改它。例如：

```python
logging.getLogger().level = logging.DEBUG
```


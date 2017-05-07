### 13.10 读取配置文件

#### 问题

怎样读取普通 .ini 格式的配置文件？

#### 解决方案

`configparser` 模块能被用来读取配置文件。

```python
>>> from configparser import ConfigParser
>>> cfg = ConfigParser()
>>> cfg.read('config.ini')
>>> cfg.sections()
>>> cfg.get('installation','library')
>>> cfg.getboolean('debug','log_errors')
>>> cfg.getint('server','port')
>>> cfg.getint('server','nworkers')
>>> print(cfg.get('server','signature'))
```

如果有需要，你还能修改配置并使用 `cfg.write()` 方法将其写回到文件中。

```python
>>> cfg.set('server','port','9000')
>>> cfg.set('debug','log_errors','False')
>>> import sys
>>> cfg.write(sys.stdout)
```

#### 讨论

配置文件作为一种可读性很好的格式，非常适用于存储程序中的配置数据。 在每个配置文件中，配置数据会被分组（比如例子中的 “installation”、 “debug” 和 “server”）。 每个分组在其中指定对应的各个变量值。

对于可实现同样功能的配置文件和 Python 源文件是有很大的不同的。 首先，配置文件的语法要更自由些，下面的赋值语句是等效的：

```ini
prefix=/usr/local
prefix: /usr/local
```

配置文件中的名字是不区分大小写的。

在解析值的时候，`getboolean()` 方法查找任何可行的值。例如下面都是等价的：

```ini
log_errors = true
log_errors = TRUE
log_errors = Yes
log_errors = 1
```

或许配置文件和 Python 代码最大的不同在于，它并不是从上而下的顺序执行。 文件是安装一个整体被读取的。如果碰到了变量替换，它实际上已经被替换完成了。 例如，在下面这个配置中，`prefix` 变量在使用它的变量之前或之后定义都是可以的：

```ini
[installation]
library=%(prefix)s/lib
include=%(prefix)s/include
bin=%(prefix)s/bin
prefix=/usr/local
```

`ConfigParser` 有个容易被忽视的特性是它能一次读取多个配置文件然后合并成一个配置。

读取这个文件，它就能跟之前的配置合并起来。如：

```python
>>> # Previously read configuration
>>> cfg.get('installation', 'prefix')
'/usr/local'
>>> # Merge in user-specific configuration
>>> import os
>>> cfg.read(os.path.expanduser('~/.config.ini'))
['/Users/beazley/.config.ini']
>>> cfg.get('installation', 'prefix')
>>> cfg.get('installation', 'library')
>>> cfg.getboolean('debug', 'log_errors')
```

变量的改写采取的是后发制人策略，以最后一个为准。

要注意的是 Python 并不能支持 .ini 文件在其他程序（比如 windows 应用程序）中的所有特性。
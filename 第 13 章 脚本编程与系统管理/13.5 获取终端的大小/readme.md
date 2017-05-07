### 13.5 获取终端的大小

#### 问题

你需要知道当前终端的大小以便正确的格式化输出。

#### 解决方案

使用 `os.get_terminal_size()` 函数来做到这一点。

```python
>>> import os
>>> sz = os.get_terminal_size()
>>> sz
os.terminal_size(columns=80, lines=24)
>>> sz.columns
80
>>> sz.lines
24
```

#### 讨论

有太多方式来得知终端大小了，从读取环境变量到执行底层的 `ioctl()` 函数等等。
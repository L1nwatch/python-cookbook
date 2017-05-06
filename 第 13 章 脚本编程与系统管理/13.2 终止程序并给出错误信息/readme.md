### 13.2 终止程序并给出错误信息

#### 问题

你想向标准错误打印一条消息并返回某个非零状态码来终止程序运行

#### 解决方案

你有一个程序像下面这样终止，抛出一个 `SystemExit` 异常，使用错误消息作为参数。例如：

```python
raise SystemExit('It failed!')
```

它会将消息在 `sys.stderr` 中打印，然后程序以状态码 1 退出。

#### 讨论

当你想要终止某个程序时，你可能会像下面这样写：

```python
import sys
sys.stderr.write('It failed!\n')
raise SystemExit(1)
```

如果你直接将消息作为参数传给 `SystemExit()` ，那么你可以省略其他步骤， 比如 import 语句或将错误消息写入 `sys.stderr`。
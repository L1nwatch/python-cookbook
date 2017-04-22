### 5.5 文件不存在才能写入

#### 问题

想向一个文件中写入数据，但是前提必须是这个文件在文件系统上不存在。 也就是不允许覆盖已存在的文件内容。

#### 解决方案

可以在 `open()` 函数中使用 `x` 模式来代替 `w` 模式的方法来解决这个问题。比如：

```python
>>> with open('somefile', 'xt') as f:
...     f.write('Hello\n')
...
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
FileExistsError: [Errno 17] File exists: 'somefile'
```

如果文件是二进制的，使用 `xb` 来代替 `xt`

#### 讨论

 一个替代方案是先测试这个文件是否存在。显而易见，使用x文件模式更加简单。要注意的是x模式是一个Python3对 `open()` 函数特有的扩展。 在Python的旧版本或者是Python实现的底层C函数库中都是没有这个模式的。
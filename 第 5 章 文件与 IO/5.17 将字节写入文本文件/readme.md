### 5.17 将字节写入文本文件

#### 问题

想在文本模式打开的文件中写入原始的字节数据

#### 解决方案

将字节数据直接写入文件的缓冲区即可，例如：

```python
>>> import sys
>>> sys.stdout.write(b'Hello\n')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: must be str, not bytes
>>> sys.stdout.buffer.write(b'Hello\n')
```

类似的，能够通过读取文本文件的 `buffer` 属性来读取二进制数据。

#### 讨论

I/O系统以层级结构的形式构建而成。 文本文件是通过在一个拥有缓冲的二进制模式文件上增加一个Unicode编码/解码层来创建。 `buffer` 属性指向对应的底层文件。如果你直接访问它的话就会绕过文本编码/解码层。

 默认情况下，`sys.stdout` 总是以文本模式打开的。
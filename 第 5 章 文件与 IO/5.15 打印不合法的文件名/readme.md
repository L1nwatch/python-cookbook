### 5.15 打印不合法的文件名

#### 问题

你的程序获取了一个目录中的文件名列表，但是当它试着去打印文件名的时候程序崩溃， 出现了 `UnicodeEncodeError` 异常和一条奇怪的消息—— `surrogates not allowed` 。

#### 解决方案

当打印未知的文件名时，使用下面的方法可以避免这样的错误：

```python
def bad_filename(filename):
    return repr(filename)[1:-1]

try:
    print(filename)
except UnicodeEncodeError:
    print(bad_filename(filename))
```

#### 讨论

当执行类似 `os.listdir()` 这样的函数时，这些不合规范的文件名就会让Python陷入困境。 一方面，它不能仅仅只是丢弃这些不合格的名字。而另一方面，它又不能将这些文件名转换为正确的文本字符串。 Python对这个问题的解决方案是从文件名中获取未解码的字节值比如 `\xhh` 并将它映射成Unicode字符 `\udchh` 表示的所谓的”代理编码”。 下面一个例子演示了当一个不合格目录列表中含有一个文件名为bäd.txt(使用Latin-1而不是UTF-8编码)时的样子：

```python
>>> import os
>>> files = os.listdir('.')
>>> files
['spam.py', 'b\udce4d.txt', 'foo.txt']
```

当你想打印上面的文件名列表时，你的程序就会崩溃。

程序崩溃的原因就是字符 `\udce4` 是一个非法的Unicode字符。 它其实是一个被称为代理字符对的双字符组合的后半部分。 由于缺少了前半部分，因此它是个非法的Unicode。 所以，唯一能成功输出的方法就是当遇到不合法文件名时采取相应的补救措施。 比如可以将上述代码修改如下：

```python
>>> for name in files:
... try:
...     print(name)
... except UnicodeEncodeError:
...     print(bad_filename(name))
...
spam.py
b\udce4d.txt
foo.txt
```

在 `bad_filename()` 函数中怎样处置取决于你自己。 另外一个选择就是通过某种方式重新编码，示例如下：

```python
def bad_filename(filename):
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('latin-1')
```

>   ```
>   surrogateescape:
>   这种是Python在绝大部分面向OS的API中所使用的错误处理器，
>   它能以一种优雅的方式处理由操作系统提供的数据的编码问题。
>   在解码出错时会将出错字节存储到一个很少被使用到的Unicode编码范围内。
>   在编码时将那些隐藏值又还原回原先解码失败的字节序列。
>   它不仅对于OS API非常有用，也能很容易的处理其他情况下的编码错误。
>   ```
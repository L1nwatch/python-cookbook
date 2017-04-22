### 5.13 获取文件夹中的文件列表

#### 问题

你想获取文件系统中某个目录下的所有文件列表。

#### 解决方案

使用 `os.listdir()` 函数来获取某个目录中的文件列表。

 如果你需要通过某种方式过滤数据，可以考虑结合 `os.path` 库中的一些函数来使用列表推导。

对于文件名的匹配，你可能会考虑使用 `glob` 或 `fnmatch` 模块。比如：

```python
import glob
pyfiles = glob.glob('somedir/*.py')

from fnmatch import fnmatch
pyfiles = [name for name in os.listdir('somedir')
            if fnmatch(name, '*.py')]
```

#### 讨论

如果你还想获取其他的元信息，比如文件大小，修改时间等等， 你或许还需要使用到 `os.path` 模块中的函数或着 `os.stat()` 函数来收集数据。比如：

```python
# Alternative: Get file metadata
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)
```

最后还有一点要注意的就是，有时候在处理文件名编码问题时候可能会出现一些问题。 通常来讲，函数 `os.listdir()` 返回的实体列表会根据系统默认的文件名编码来解码。 但是有时候也会碰到一些不能正常解码的文件名。 
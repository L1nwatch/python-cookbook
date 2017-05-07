### 13.9 通过文件名查找文件

#### 问题

你需要写一个涉及到文件查找操作的脚本，比如对日志归档文件的重命名工具， 你不想在 Python 脚本中调用 shell，或者你要实现一些 shell 不能做的功能。

#### 解决方案

查找文件，可使用 `os.walk()` 函数，传一个顶级目录名给它。 

#### 讨论

`os.walk()` 方法为我们遍历目录树， 每次进入一个目录，它会返回一个三元组，包含相对于查找目录的相对路径，一个该目录下的目录名列表， 以及那个目录下面的文件名列表。

使用 `os.path.join()` 合并路径。

 `os.path.abspath()` ，它接受一个路径，可以是相对路径，最后返回绝对路径。

 `os.path.normpath()` ，用来返回正常路径，可以解决双斜杆、对目录的多重引用的问题等。

下面的函数打印所有最近被修改过的文件：

```python
#!/usr/bin/env python3.3

import os
import time

def modified_within(top, seconds):
    now = time.time()
    for path, dirs, files in os.walk(top):
        for name in files:
            fullpath = os.path.join(path, name)
            if os.path.exists(fullpath):
                mtime = os.path.getmtime(fullpath)
                if mtime > (now - seconds):
                    print(fullpath)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('Usage: {} dir seconds'.format(sys.argv[0]))
        raise SystemExit(1)

    modified_within(sys.argv[1], float(sys.argv[2]))
```

在此函数的基础之上，使用 os,os.path,glob 等类似模块，你就能实现更加复杂的操作了。 
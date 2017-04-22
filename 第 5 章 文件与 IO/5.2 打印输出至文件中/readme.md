### 5.2 打印输出至文件中

#### 问题

你想将 `print()` 函数的输出重定向到一个文件中去。

#### 解决方案

```python
with open('d:/work/test.txt', 'wt') as f:
    print('Hello World!', file=f)
```


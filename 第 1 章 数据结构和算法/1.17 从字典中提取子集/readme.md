### 1.17 从字典中提取子集

#### 问题

根据一个字典构造新的字典

#### 解决方案

最简单的方式是使用字典推导。比如：

```python
p1 = {key: value for key, value in prices.items() if value > 200}
```

#### 讨论

大多数情况下字典推导能做到的，通过创建一个元组序列然后把它传给 `dict()` 函数也能实现。比如：

```python
p1 = dict((key, value) for key, value in prices.items() if value > 200)
```

但是，字典推导方式表意更清晰，并且实际上也会运行的更快些
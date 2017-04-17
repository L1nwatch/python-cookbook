### 1.8 字典的运算

#### 问题

如何对字典进行类似于求最大值、最小值等操作？

#### 解决方案

求最大值和最小值、排序：

```python
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')
prices_sorted = sorted(zip(prices.values(), prices.keys()))
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
#                   (45.23, 'ACME'), (205.55, 'IBM'),
#                   (612.78, 'AAPL')]
```

注意 `zip()` 函数创建的是一个只能访问一次的迭代器。 

#### 讨论

如果只想获得值，或者获得键，可以直接使用 key 参数：

```python
min(prices.values()) # Returns 10.75
max(prices, key=lambda k: prices[k]) # Returns 'AAPL'
```

当多个实体拥有相同的值的时候，键会决定返回结果。 比如，在执行 `min()` 和 `max()` 操作的时候，如果恰巧最小或最大值有重复的，那么拥有最小或最大键的实体会返回。
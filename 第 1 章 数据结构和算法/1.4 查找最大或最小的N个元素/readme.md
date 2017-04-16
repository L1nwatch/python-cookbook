### 1.4 查找最大或最小的N个元素

#### 问题

集合里面，求最大或者最小的 N 个元素

#### 解决

heapq模块有两个函数：`nlargest()` 和 `nsmallest()` 可以完美解决这个问题。（其实就是利用了堆这个数据结构的性质）

```python
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]
```

可以使用 `key` 参数，以支持更复杂的数据结构：

```python
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
```

#### 讨论

在底层实现里面，首先会先将集合数据进行堆排序后放入一个列表中：

```python
>>> nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
>>> import heapq
>>> heapq.heapify(nums)
>>> nums
[-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
```

堆数据结构最重要的特征是 `heap[0]` 永远是最小的元素。并且剩余的元素可以很容易的通过调用 `heapq.heappop()` 方法得到， 该方法会先将第一个元素弹出来，然后用下一个最小的元素来取代被弹出元素(这种操作时间复杂度仅仅是O(log N)，N是堆大小)。

```python
>>> heapq.heappop(nums)
-4
>>> heapq.heappop(nums)
1
>>> heapq.heappop(nums)
2
```

如果你仅仅想查找唯一的最小或最大(N=1)的元素的话，那么使用 `min()` 和 `max()` 函数会更快些。 类似的，如果N的大小和集合大小接近的时候，通常先排序这个集合然后再使用切片操作会更快点 ( `sorted(items)[:N]` 或者是 `sorted(items)[-N:]` )。
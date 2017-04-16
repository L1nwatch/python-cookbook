### 1.2 解压可迭代对象赋值给多个变量

#### 问题

1.1 说过如果元素个数和变量个数不匹配，会抛出异常。如何只解压 N 个元素而不抛出异常？

#### 解决方案

使用星号表达式。

```python
>>> record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
>>> name, email, *phone_numbers = record
>>> name
'Dave'
>>> email
'dave@example.com'
>>> phone_numbers
['773-555-1212', '847-555-1212']
```

注意的是上面解压出的 `phone_numbers` 变量永远都是列表类型，不管解压的电话号码数量是多少(包括0个)。 所以，任何使用到 `phone_numbers` 变量的代码就不需要做多余的类型检查去确认它是否是列表类型了。

星号表达式在迭代元素为可变长元组的序列时是很有用的、在字符串操作的时候也会很有用：

```python
>>> line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
>>> uname, *fields, homedir, sh = line.split(':')
>>> uname
'nobody'
>>> homedir
'/var/empty'
>>> sh
'/usr/bin/false'
```

有时候，你想解压一些元素后丢弃它们，你不能简单就使用 `*` ， 但是你可以使用一个普通的废弃名称，比如 `_` 或者 `ign` 。

```python
>>> record = ('ACME', 50, 123.45, (12, 18, 2012))
>>> name, *_, (*_, year) = record
```

还能用这种分割语法去巧妙的实现递归算法。比如：

```python
>>> def sum(items):
... head, *tail = items
... return head + sum(tail) if tail else head
```

【注意递归并不是 Python 擅长的】
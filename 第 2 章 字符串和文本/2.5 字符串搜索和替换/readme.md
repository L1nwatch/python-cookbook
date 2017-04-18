### 2.5 字符串搜索和替换

#### 问题

不仅要搜索还要替换

#### 解决方案

对于简单的字面模式，直接使用 `str.repalce()` 方法即可。

对于复杂的模式，请使用 `re` 模块中的 `sub()` 函数。 

```python
>>> text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
>>> import re
>>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
'Today is 2012-11-27. PyCon starts 2013-3-13.'
```

`sub()` 函数中的第一个参数是被匹配的模式，第二个参数是替换模式。反斜杠数字比如 `\3` 指向前面模式的捕获组号。

对于更加复杂的替换，可以传递一个替换回调函数来代替，比如：

```python
>>> from calendar import month_abbr
>>> def change_date(m):
... mon_name = month_abbr[int(m.group(1))]
... return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
...
>>> datepat.sub(change_date, text)
'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'
```

如果除了替换后的结果外，你还想知道有多少替换发生了，可以使用 `re.subn()` 来代替。

```python
>>> newtext, n = datepat.subn(r'\3-\1-\2', text)
```


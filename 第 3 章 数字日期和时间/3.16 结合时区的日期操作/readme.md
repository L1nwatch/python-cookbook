### 3.16 结合时区的日期操作

#### 问题

进行日期计算时需要涉及到时区问题

#### 解决方案

对几乎所有涉及到时区的问题，你都应该使用 `pytz` 模块。这个包提供了Olson时区数据库， 它是时区信息的事实上的标准，在很多语言和操作系统里面都可以找到。

`pytz` 模块一个主要用途是将 `datetime` 库创建的简单日期对象本地化。 

```python
>>> from datetime import datetime
>>> from pytz import timezone
>>> d = datetime(2012, 12, 21, 9, 30, 0)
>>> print(d)
2012-12-21 09:30:00
>>> # Localize the date for Chicago
>>> central = timezone('US/Central')
>>> loc_d = central.localize(d)
>>> print(loc_d)
2012-12-21 09:30:00-06:00
```

一旦日期被本地化了， 它就可以转换为其他时区的时间了

```python
>>> # Convert to Bangalore time
>>> bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
>>> print(bang_d)
2012-12-21 21:00:00+05:30
```

如果你打算在本地化日期上执行计算，你需要特别注意夏令时转换和其他细节。 比如，在2013年，美国标准夏令时时间开始于本地时间3月13日凌晨2:00(在那时，时间向前跳过一小时)。 如果你正在执行本地计算，你会得到一个错误。比如：

```python
>>> d = datetime(2013, 3, 10, 1, 45)
>>> loc_d = central.localize(d)
>>> print(loc_d)
2013-03-10 01:45:00-06:00
>>> later = loc_d + timedelta(minutes=30)
>>> print(later)
2013-03-10 02:15:00-06:00 # WRONG! WRONG!
```

结果错误是因为它并没有考虑在本地时间中有一小时的跳跃。 为了修正这个错误，可以使用时区对象 `normalize()` 方法。比如：

```python
>>> from datetime import timedelta
>>> later = central.normalize(loc_d + timedelta(minutes=30))
>>> print(later)
2013-03-10 03:15:00-05:00
```

#### 讨论

处理本地化日期的通常的策略先将所有日期转换为UTC时间， 并用它来执行所有的中间存储和操作。比如：

```python
>>> print(loc_d)
2013-03-10 01:45:00-06:00
>>> utc_d = loc_d.astimezone(pytz.utc)
>>> print(utc_d)
2013-03-10 07:45:00+00:00
```

一旦转换为UTC，你就不用去担心跟夏令时相关的问题了。 因此，你可以跟之前一样放心的执行常见的日期计算。 当你想将输出变为本地时间的时候，使用合适的时区去转换下就行了。比如：

```python
>>> later_utc = utc_d + timedelta(minutes=30)
>>> print(later_utc.astimezone(central))
2013-03-10 03:15:00-05:00
```

当涉及到时区操作的时候，有个问题就是我们如何得到时区的名称。为了查找，可以使用ISO 3166国家代码作为关键字去查阅字典 `pytz.country_timezones` 。比如：

```python
>>> pytz.country_timezones['IN']
['Asia/Kolkata']
```

有可能 `pytz` 模块已经不再建议使用了，因为PEP431提出了更先进的时区支持。
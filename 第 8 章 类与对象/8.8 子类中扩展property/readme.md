### 8.8 子类中扩展property

#### 问题

在子类中，你想要扩展定义在父类中的property的功能。

#### 解决方案

如果你仅仅只想扩展property的某一个方法，那么可以像下面这样写：

```python
class SubPerson(Person):
    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name
```

或者，你只想修改setter方法，就这么写：

```python
class SubPerson(Person):
    @Person.name.setter
    def name(self, value):
        print('Setting name to', value)
        # 获取这个方法的唯一途径是使用类变量而不是实例变量来访问它。 这也是为什么我们要使用 super(SubPerson, SubPerson) 的原因。
        super(SubPerson, SubPerson).name.__set__(self, value)
```

#### 讨论

在子类中扩展一个property可能会引起很多不易察觉的问题， 因为一个property其实是 `getter`、`setter` 和 `deleter` 方法的集合，而不是单个方法。 因此，但你扩展一个property的时候，你需要先确定你是否要重新定义所有的方法还是说只修改其中某一个。

如果你只想重定义其中一个方法，那只使用 @property 本身是不够的。比如，下面的代码就无法工作：

```python
class SubPerson(Person):
    @property  # Doesn't work
    def name(self):
        print('Getting name')
        return super().name
```

你应该像之前说过的那样修改代码：

```python
class SubPerson(Person):
    @Person.getter
    def name(self):
        print('Getting name')
        return super().name
```

这么写后，property之前已经定义过的方法会被复制过来，而getter函数被替换。

在这个特别的解决方案中，我们没办法使用更加通用的方式去替换硬编码的 `Person` 类名。 如果你不知道到底是哪个基类定义了property， 那你只能通过重新定义所有property并使用 `super()` 来将控制权传递给前面的实现。

值的注意的是上面演示的第一种技术还可以被用来扩展一个描述器：

```python
# A descriptor
class String:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        instance.__dict__[self.name] = value

# A class with a descriptor
class Person:
    name = String('name')

    def __init__(self, name):
        self.name = name

# Extending a descriptor with a property
class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)
```


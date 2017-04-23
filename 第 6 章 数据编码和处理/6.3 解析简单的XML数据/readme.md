### 6.3 解析简单的XML数据

#### 问题

你想从一个简单的XML文档中提取数据。

#### 解决方案

可以使用 `xml.etree.ElementTree` 模块从简单的XML文档中提取数据。

```python
from urllib.request import urlopen
from xml.etree.ElementTree import parse

# Download the RSS feed and parse it
u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)

# Extract and output tags of interest
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')
```

#### 讨论

在很多应用程序中处理XML编码格式的数据是很常见的。 不仅因为XML在Internet上面已经被广泛应用于数据交换， 同时它也是一种存储应用程序数据的常用格式(比如字处理，音乐库等)。

在很多情况下，当使用XML来仅仅存储数据的时候，对应的文档结构非常紧凑并且直观。

`xml.etree.ElementTree.parse()` 函数解析整个XML文档并将其转换成一个文档对象。 然后，你就能使用 `find()` 、`iterfind()` 和 `findtext()` 等方法来搜索特定的XML元素了。 这些函数的参数就是某个指定的标签名，例如 `channel/item` 或 `title` 。

每次指定某个标签时，你需要遍历整个文档结构。每次搜索操作会从一个起始元素开始进行。 同样，每次操作所指定的标签名也是起始元素的相对路径。 例如，执行 `doc.iterfind('channel/item')` 来搜索所有在 `channel` 元素下面的 `item` 元素。 `doc` 代表文档的最顶层(也就是第一级的 `rss` 元素)。 然后接下来的调用 `item.findtext()` 会从已找到的 `item` 元素位置开始搜索。

`ElementTree` 模块中的每个元素有一些重要的属性和方法，在解析的时候非常有用。`tag` 属性包含了标签的名字，`text` 属性包含了内部的文本，而 `get()` 方法能获取属性值。例如：

```python
>>> doc
<xml.etree.ElementTree.ElementTree object at 0x101339510>
>>> e = doc.find('channel/title')
>>> e
<Element 'title' at 0x10135b310>
>>> e.tag
'title'
>>> e.text
'Planet Python'
>>> e.get('some_attribute')
```

有一点要强调的是 `xml.etree.ElementTree` 并不是XML解析的唯一方法。 对于更高级的应用程序，你需要考虑使用 `lxml` 。 它使用了和ElementTree同样的编程接口，因此上面的例子同样也适用于lxml。 你只需要将刚开始的import语句换成 `from lxml.etree import parse` 就行了。 `lxml` 完全遵循XML标准，并且速度也非常快，同时还支持验证，XSLT，和XPath等特性。
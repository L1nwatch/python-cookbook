### 10.14 创建新的 Python 环境

#### 问题

你想创建一个新的 Python 环境，用来安装模块和包。 不过，你不想安装一个新的 Python 克隆，也不想对系统 Python 环境产生影响。

#### 解决方案

你可以使用 `pyvenv` 命令创建一个新的“虚拟”环境。 这个命令被安装在 Python 解释器同一目录，或 Windows 上面的 Scripts 目录中。下面是一个例子：

```shell
bash % pyvenv Spam
```

传给 `pyvenv` 命令的名字是将要被创建的目录名。当被创建后，Span 目录像下面这样：

```shell
bash % ls
bin include lib pyvenv.cfg
```

在 bin 目录中，你会找到一个可以使用的 Python 解释器：

```shell
bash % Spam/bin/python3
```

这个解释器的特点就是他的 `site-packages` 目录被设置为新创建的环境。 如果你要安装第三方包，它们会被安装在那里，而不是通常系统的 `site-packages` 目录。

#### 讨论

有了一个新的虚拟环境，下一步就是安装一个包管理器，比如 `distribute` 或 `pip`。 但安装这样的工具和包的时候，你需要确保你使用的是虚拟环境的解释器。 它会将包安装到新创建的 `site-packages` 目录中去。

尽管一个虚拟环境看上去是 Python 安装的一个复制， 不过它实际上只包含了少量几个文件和一些符号链接。 所有标准库函文件和可执行解释器都来自原来的 Python 安装。 因此，创建这样的环境是很容易的，并且几乎不会消耗机器资源。

默认情况下，虚拟环境是空的，不包含任何额外的第三方库。如果你想将一个已经安装的包作为虚拟环境的一部分， 可以使用 `“–system-site-packages”` 选项来创建虚拟环境，例如：

```shell
bash % pyvenv --system-site-packages Spam
```


## 第 15 章 C 语言扩展

本章着眼于从 Python 访问 C 代码的问题。许多 Python 内置库是用 C 写的， 访问 C 是让 Python 的对现有库进行交互一个重要的组成部分。 这也是一个当你面临从 Python 2 到 Python 3 扩展代码的问题。 虽然 Python 提供了一个广泛的编程 API，实际上有很多方法来处理 C 的代码。 

相比试图给出对于每一个可能的工具或技术的详细参考， 以下采用的是是集中在一个小片段的 C++ 代码，以及一些有代表性的例子来展示如何与代码交互。 这个目标是提供一系列的编程模板，有经验的程序员可以扩展自己的使用。

这里是我们将在大部分秘籍中工作的代码：

```c++
/* sample.c */_method
#include <math.h>

/* Compute the greatest common divisor */
int gcd(int x, int y) {
    int g = y;
    while (x > 0) {
        g = x;
        x = y % x;
        y = g;
    }
    return g;
}

/* Test if (x0,y0) is in the Mandelbrot set or not */
int in_mandel(double x0, double y0, int n) {
    double x=0,y=0,xtemp;
    while (n > 0) {
        xtemp = x*x - y*y + x0;
        y = 2*x*y + y0;
        x = xtemp;
        n -= 1;
        if (x*x + y*y > 4) return 0;
    }
    return 1;
}

/* Divide two numbers */
int divide(int a, int b, int *remainder) {
    int quot = a / b;
    *remainder = a % b;
    return quot;
}

/* Average values in an array */
double avg(double *a, int n) {
    int i;
    double total = 0.0;
    for (i = 0; i < n; i++) {
        total += a[i];
    }
    return total / n;
}

/* A C data structure */
typedef struct Point {
    double x,y;
} Point;

/* Function involving a C data structure */
double distance(Point *p1, Point *p2) {
    return hypot(p1->x - p2->x, p1->y - p2->y);
}
```

这段代码包含了多种不同的 C 语言编程特性。 首先，这里有很多函数比如 `gcd()` 和 `is_mandel()` 。 `divide()` 函数是一个返回多个值的 C 函数例子，其中有一个是通过指针参数的方式。 `avg()` 函数通过一个 C 数组执行数据聚集操作。`Point` 和 `distance()` 函数涉及到了 C 结构体。

对于接下来的所有小节，先假定上面的代码已经被写入了一个名叫 “sample.c” 的文件中， 然后它们的定义被写入一个名叫 “sample.h” 的头文件中， 并且被编译为一个库叫 “libsample”，能被链接到其他 C 语言代码中。 编译和链接的细节依据系统的不同而不同，但是这个不是我们关注的。 如果你要处理 C 代码，我们假定这些基础的东西你都掌握了。

包括:

* 15.1 使用ctypes访问C代码
* 15.2 简单的C扩展模块
* 15.3 编写扩展函数操作数组
* 15.4 在C扩展模块中操作隐形指针
* 15.5 从扩张模块中定义和导出C的API
* 15.6 从C语言中调用Python代码
* 15.7 从C扩展中释放全局锁
* 15.8 C和Python中的线程混用
* 15.9 用WSIG包装C代码
* 15.10 用Cython包装C代码
* 15.11 用Cython写高性能的数组操作
* 15.12 将函数指针转换为可调用对象
* 15.13 传递NULL结尾的字符串给C函数库
* 15.14 传递Unicode字符串给C函数库
* 15.15 C字符串转换为Python字符串
* 15.16 不确定编码格式的C字符串
* 15.17 传递文件名给C扩展
* 15.18 传递已打开的文件给C扩展
* 15.19 从C语言中读取类文件对象
* 15.20 处理C语言中的可迭代对象
* 15.21 诊断分段错误
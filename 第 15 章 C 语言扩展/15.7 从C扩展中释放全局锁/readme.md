### 15.7 从 C 扩展中释放全局锁

#### 问题

你想让 C 扩展代码和 Python 解释器中的其他进程一起正确的执行， 那么你就需要去释放并重新获取全局解释器锁（GIL）。

#### 解决方案

在 C 扩展代码中，GIL 可以通过在代码中插入下面这样的宏来释放和重新获取：

```c++
#include "Python.h"
//...

PyObject *pyfunc(PyObject *self, PyObject *args) {
   //...
   Py_BEGIN_ALLOW_THREADS
   // Threaded C code.  Must not use Python API functions
   //...
   Py_END_ALLOW_THREADS
   //...
   return result;
}
```

#### 讨论

只有当你确保没有 Python C API 函数在 C 中执行的时候你才能安全的释放 GIL。 GIL 需要被释放的常见的场景是在计算密集型代码中需要在 C 数组上执行计算（比如在 numpy 中） 或者是要执行阻塞的 I/O 操作时（比如在一个文件描述符上读取或写入时）。

当 GIL 被释放后，其他 Python 线程才被允许在解释器中执行。 `Py_END_ALLOW_THREADS` 宏会阻塞执行直到调用线程重新获取了 GIL。
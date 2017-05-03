### 11.3 创建UDP服务器

#### 问题

你想实现一个基于UDP协议的服务器来与客户端通信。

#### 解决方案

跟 TCP 一样，UDP 服务器也可以通过使用 `socketserver` 库很容易的被创建。 例如，下面是一个简单的时间服务器：

```python
from socketserver import BaseRequestHandler, UDPServer
import time

class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        # Get message and client socket
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)

if __name__ == '__main__':
    serv = UDPServer(('', 20000), TimeHandler)
    serv.serve_forever()
```

我们来测试下这个服务器，首先运行它，然后打开另外一个 Python 进程向服务器发送消息：

```python
>>> from socket import socket, AF_INET, SOCK_DGRAM
>>> s = socket(AF_INET, SOCK_DGRAM)
>>> s.sendto(b'', ('localhost', 20000))
0
>>> s.recvfrom(8192)
(b'Wed Aug 15 20:35:08 2012', ('127.0.0.1', 20000))
```

#### 讨论

一个典型的 UDP 服务器接收到达的数据报(消息)和客户端地址。如果服务器需要做应答， 它要给客户端回发一个数据报。对于数据报的传送， 你应该使用 socket 的 `sendto()` 和 `recvfrom()` 方法。 尽管传统的 `send()` 和 `recv()` 也可以达到同样的效果， 但是前面的两个方法对于 UDP 连接而言更普遍。

`UDPServer` 类是单线程的，也就是说一次只能为一个客户端连接服务。 实际使用中，这个无论是对于 UDP 还是 TCP 都不是什么大问题。 如果你想要并发操作，可以实例化一个 `ForkingUDPServer` 或 `ThreadingUDPServer` 对象：

```python
from socketserver import ThreadingUDPServer

if __name__ == '__main__':
    serv = ThreadingUDPServer(('',20000), TimeHandler)
    serv.serve_forever()
```

直接使用 `socket` 来实现一个 UDP 服务器也不难，下面是一个例子：

```python
from socket import socket, AF_INET, SOCK_DGRAM
import time

def time_server(address):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(address)
    while True:
        msg, addr = sock.recvfrom(8192)
        print('Got message from', addr)
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), addr)

if __name__ == '__main__':
    time_server(('', 20000))
```
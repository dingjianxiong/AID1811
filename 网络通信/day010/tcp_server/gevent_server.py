import gevent
from gevent import monkey
monkey.patch_all()#执行脚本插件，修改阻塞行为
from socket import *
#创建套接字
def server():
    s=socket()
    s.bind(('0.0.0.0',8888))
    s.listen(5)
    while True:
        c,addr=s.accept()
        print("connet from ",addr)
        # handle(c)
        gevent.spawn(handle,c)#协程方案，遇到阻塞时，会跳转出循环，接收下一个客户端的连接
        #如果阻塞的io可以运行时，会返回并执行
def handle(c):
    while True:
        data=c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'ok')
    c.close()
server()
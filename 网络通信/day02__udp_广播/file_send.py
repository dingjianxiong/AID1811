#客户端
from socket import *

#创建套接字
sockfd=socket()
#发起连接
sockfd.connect(('127.0.0.1',8888))
f=open('bbb.png','rb')
while True:
    # 消息的发出
    data=f.read(1024)
    if not data:
        break
    sockfd.send(data)
f.close()
sockfd.close()
#tcp_server.py
#服务端
from socket import *
# 1、创建套接字
sockfd=socket()
# 2、绑定地址
sockfd.bind(('0.0.0.0',8888))
# 3、设置监听套接字
sockfd.listen(5)
# 4、等待客户端连接
connfd,addr=sockfd.accept()
print("Connect from",addr)#打印客户端地址
# 5、消息收发
f=open('ccc.jpg','wb')
while True:
    data=connfd.recv(1024)
    if not data:
        break
    f.write(data)
#６、关闭套接字
connfd.close()
sockfd.close()
f.close()
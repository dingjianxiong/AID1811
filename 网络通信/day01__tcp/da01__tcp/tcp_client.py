# tcp_client.py
#客户端
from socket import *

#创建套接字
sockfd=socket()
#发起连接
server_addr=('127.0.0.1',9999)
sockfd.connect(server_addr)
while True:
    # 消息的发出
    data=input('>>')
    if not data:
        break
    sockfd.send(data.encode())
    data=sockfd.recv(1024)
    print('from server:',data.decode())

sockfd.close()
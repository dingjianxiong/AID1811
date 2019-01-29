#客户端ｕｄｐ
from socket import *
sockfd=socket(AF_INET,SOCK_DGRAM)
sockfd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
#发起连接
sockfd.connect(('127.0.0.1',2019))
while True:
    data=input(">>")
    sockfd.send(data.encode())
scokfd.close()
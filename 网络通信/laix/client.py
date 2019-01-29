#客户端
from socket import *
#创建套接字对象于服务端类型一样
sockfd=socket()
#发起连接
sockfd.connect(('127.0.0.1',2030))
print("连接成功")
#消息的发送和收
while True:
    #客户端输入信息准备发送服务端
    data=input(">>")
    if not data:
        break
    #发送消息给服务端，将字符串转换为二进制
    sockfd.send(data.encode())
    #接受服务端的反馈信息
    s=sockfd.recv(1024)
    print(s.decode())
sockfd.close()
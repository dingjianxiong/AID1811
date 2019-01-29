#服务端
from socket import *
#创建数据报套接字
sockfd=socket(AF_INET,SOCK_DGRAM)
#绑定地址
sockfd.bind(('0.0.0.0',8888))
#消息收发
while True:
    #接受消息
    #data:接受的内容
    #addr:发送者的地址
    #recvfrom(1024)发送的大小限制
    data,addr=sockfd.recvfrom(1024)
    #发送给请求者的消息
    print("Receive from %s:%s"%(addr,data.decode()))
    sockfd.sendto(b'Thanks for your msg',addr)
#关闭套接字
sockfd.close()
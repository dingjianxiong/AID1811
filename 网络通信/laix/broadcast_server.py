#udp广播
from socket import *

#创建数据报套接字
sockfd=socket(AF_INET,SOCK_DGRAM)
#设置套接字可以接受广播
sockfd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

sockfd.bind(('0.0.0.0',2019))
#消息的收发
while True:
    try:
        #接受消息
        data,addr=sockfd.recvfrom(1024)
        print("接收广播：",data.decode())
    except KeyboardInterrupt:
        print("停止接收")
        break
    except Exception as e:
        print(e)
sockfd.close()
    
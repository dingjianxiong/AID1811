from socket import *
from time import sleep,ctime

#创建套接字
sockfd=socket()
sockfd.bind(('0.0.0.0',2668))
sockfd.listen(5)

# 设置sockfd为非阻塞
sockfd.setblocking(False)

#设置sockfd的超时时间
# sockfd.settimeout(5)
n=0
while True:
    print("waiting for connect....")
    try:
       connfd,addr=sockfd.accept()#阻塞等待（等待连接客户端）
    except timeout:
        print("我等得花儿都谢了")
    except BlockingIOError:
        sleep(2)
        n+=2
        print("等待连接%dsec"%n,ctime())
    else:
        print("connect from",addr)
        data=connfd.recv(1024)
        print("receive:",data.decode())
        n=0
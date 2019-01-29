from socket import *
import os

#如果存在就删除文件
if os.path.exists('./sock'):
    os.remove('./sock')

#创建本地套接字
sockfd=socket(AF_UNIX,SOCK_STREAM)
#创建本地套接字文件
sockfd.bind('./sock')
#监听本地套接字
sockfd.listen(5)
while True:
    #等待客户端连接
    c,addr=sockfd.accept()
    while True:
        #客户端消息的接收
        data=c.recv(1024)
        if not data:
            break
        print(data.decode())
    #断开后关闭套接字
    c.close()
sockfd.close()

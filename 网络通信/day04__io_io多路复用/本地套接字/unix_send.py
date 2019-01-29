from socket import *

sockfd=socket(AF_UNIX,SOCK_STREAM)
#连接同一个本地套接字文件
sockfd.connect('./sock')
while True:
    msg=input(">>")
    if not msg:
        break
    #发送消息给服务端
    sockfd.send(msg.encode())
sockfd.close()
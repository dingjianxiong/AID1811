#服务端
from socket import *
#创建tcp套接字（默认tcp套接字）
sockfd=socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(("0.0.0.0",2030))

sockfd.listen(5)
while True:
    #等待客户端连接
    connfd,addr=sockfd.accept()
    #如果客户端已连接就打印客户端地址
    print("客户端：",addr,"已连接")
    print(connfd)
    while True:
        #获取客户端的信息并打印出来
        data=connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        #发送给客户端消息
        n=connfd.send(data)
    #关闭套接字
    connfd.close()
sockfd.close()

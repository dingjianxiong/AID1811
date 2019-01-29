#tcp_server.py
#服务端
from socket import *
# 1、创建套接字
sockfd=socket(AF_INET,SOCK_STREAM,proto=0)
# 2、绑定地址
sockfd.bind(('0.0.0.0',6666))

# 3、设置监听套接字
sockfd.listen(10)
while True:
# 4、等待客户端连接
    print("hello word!!!")
    connfd,addr=sockfd.accept()
    print("Connect from",addr)#打印客户端地址
    while True:
        # 5、消息收发
        #客户端退出，服务端recv立即返回空字符串
        data=connfd.recv(1024)
        if not data:
            break
        print('Receive Msg:',data.decode())
        # print(len(data))
        n=connfd.send(data)
        print('Send %d bytes' % n)
        #６、关闭套接字
    connfd.close()
sockfd.close()
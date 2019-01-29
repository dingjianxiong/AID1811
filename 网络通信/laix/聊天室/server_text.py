from socket import *
import os,sys

#创建全局变量
HOST='0.0.0.0'
POST=9999
ADDR=(HOST,POST)

#tcp套接字，创建网络连接
def main():
    s=socket()
    s.getsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    #创建客户端连接
    while True:
        try:
            c,addr=s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit("客户端退出")
        except Exception as e:
            print("error:",e)
            continue
        print("客户端：",addr)
    #创建多进程
    pid=os.fork()
    if pid==0:
        #创建二级进程防止僵尸进程，处理客户端信息
        pid=os.fork()
        if pid==0:
            s.close()#关闭没用的套接字，释放空间
            #创建客户端对象类
            # client=tcp_client(c)
            #循环接收
            while True:
                data=c.recv(1024).decode()
                print(data)
    elif pid>0:
        pass
main()
from socket import *
import os,sys

#连接服务端
def main():
    #用户输入连接地址端口
    if len(sys.argv)<3:
        print("地址输入错误")
        return
    HOST=sys.argv[1]#地址
    POST=int(sys.argv[2])#端口
    ADDR=(HOST,POST)
    s=socket()
    try:
        s.connect((ADDR))#连接服务端
    except Exception as e:
        print("error:",e)
        return
    while True:
        r=input('>>')
        s.send(r.encode())
        data=s.recv(1024).decode()
        print(data)
main()
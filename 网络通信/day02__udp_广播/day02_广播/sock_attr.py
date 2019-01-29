from socket import *

s=socket()
#设置端口立即重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR,))
print(s.type)#套接字类型
print(s.family)#套接字地址类型

s.bind(('176.221.15.207',8866))
print(s.getsockname())#获取套接字绑定地址
print(s.fileno())#文件描述符

s.listen(5)
c,addr=s._accept()
print('Client address:',c.getpeername())

data=c.recv(1024)
c.close()
s.close()

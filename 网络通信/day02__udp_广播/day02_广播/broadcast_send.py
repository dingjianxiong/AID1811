from socket import *
from time import *
#设置广播目标地址
dest=('176.221.15.255',6688)
s=socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
while True:
    sleep(2)
    s.sendto("hello word !!!".encode(),dest)
s.close()
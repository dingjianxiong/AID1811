#类似于聊天室（tcp)
from socket import *
from select import select
import sys
from time import ctime

#准备要关注的IO
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',9996))
s.listen(5)

fd=open("abc.txt",'a')
#设置sockfd为非阻塞
# sockfd.setblocking(False)

#设置sockfd的超时时间
# sockfd.settimeout(5)
#添加关注的列表
rlist=[s,sys.stdin]
wlist=[]
xlist=[]
while True:
    #监控IO的发生
    rs,ws,xs=select(rlist,wlist,xlist)
    #遍历三个列表，确定哪个IO发生
    for r in rs:
        #如果遍历到s说明s就绪则有客户端发起连接
        if r is s:
            c,addr=r.accept()
            print("Connect from",addr)
            rlist.append(c)
        #表示客户端连接套接字就绪，则接收消息
        elif r is sys.stdin:
                data=sys.stdin.readline()
                data=ctime()+' '+data+'\n'
                fd.write(data)
                fd.flush()#清理缓存
        else:
            data=r.recv(1024).decode()
            # c.send(data.encode())
            if not data:
                #客户端退出
                print(addr,'已退出')
                rlist.remove(r)
                r.close()
                # fd.close()
                continue
            data=ctime()+' '+data+'\n'
            fd.write(data)
            fd.flush()
            # print('recvive from %s:%s' % (r.getpeername(),data.decode()))
            r.send(b'hello word')
            # wlist.append(r)

    for w in ws:
        w.send(b"Receive your message")
        wlist.remove(w)

    for x in xs:
        pass


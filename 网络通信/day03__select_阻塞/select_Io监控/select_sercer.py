#类似于聊天室（tcp)
from socket import *
from select import select
from sys import *
#准备要关注的IO
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',5003))
s.listen(5)

fd=open("abc.txt",'w')

#添加关注的列表
rlist=[s]
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
        else:
            data=r.recv(1024)
            fd.write(data.decode())
            if not data:
                #客户端退出
                rlist.remove(r)
                r.close()
                fd.close()
                continue
            print('recvive from %s:%s' % (r.getpeername(),data.decode()))
            # r.send(b'hello word')
            wlist.append(r)

    for w in ws:
        w.send(b"Receive your message")
        wlist.remove(w)

    for x in xs:
        pass


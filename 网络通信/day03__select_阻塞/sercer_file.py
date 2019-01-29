from socket import *
from select import *
s=socket()
s.getsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',9850))
s.listen(5)
#添加关注的列表
rlist=[]
wlist=[]
xlist=[]
while True:
    #监控IO事件
    #rlist是指想要关注的等待发生的事件，如果存在就立即返回给rs
    #wlist是指想要关注即将写入的事件，如果获取到就返回给ws
    #xlist是指想要关注即将报错的事件，如果获取到就会返回给xs
    rs,ws,xs=select(rlist,wlist,xlist)
    for r in rs:
        #等待客户端连接服务端并返回两个值，
        #c:连接套接字（接收的数据）
        #addr:客户端的地址（系统给的）
        c,addr=s.connect(1024)
        print("id:",addr)
        rlist.append(c)
    else:
        #用户连接后发送消息
        data=c.recv(1024)
        if not data:
            rlist.remove(c)
            c.close()
            continue
        
    for w in ws:
        pass
    for x in xs:
        pass

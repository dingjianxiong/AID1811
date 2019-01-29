from socket import *
from select import *
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8899))
s.listen(5)
#创建poll对象
p=poll()

#建立查找字典
fdmap={s.fileno():s}

#注册关注IO
#P.register(fd,ecent)
p.register(s,POLLIN | POLLERR)
while True:
    events=p.poll()#监控IO
    for fd,event in events:
        if fd==s.fileno():
            c,addr=fdmap[fd].accept()
            print("Connect from",addr)
            #添加新的关注事件
            p.register(c,POLLIN | POLLHUP)
            fdmap[c.fileno()]=c
        #通过按位与判断是否某个事件就绪
        elif event & POLLIN:
            data=fdmap[fd].recv(1024)
            if not data:
                #客户端退出取消关注。从字典删除
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
            else:
                print("receive:",data.decode())
                fdmap[fd].send(b'Receive')

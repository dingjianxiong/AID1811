# simple_select.py
# select函数简单示例
from socket import *
from select import *

# 创建socket
server = socket()
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server.bind(("0.0.0.0", 9999)) # ("localhost",9999)
server.listen(5)
print("服务器已启动")

#定义三个列表, 存放读,写,异常三类IO的列表
rlist = [server]  #关注读事件IO列表
wlist = []  #关注写事件IO列表
xlist = []  #关注异常事件IO列表

# 调用select, 注册IO事件
while True:
    rs,ws,xs = select(rlist, wlist, xlist)#阻塞等待事件
    print("监控到有IO事件发生")
    # 遍历返回IO列表,依次进行处理
    for r in rs:  # 读事件列表, 读数据        
        if r is server:# 如果就绪IO是监听socket
            client,addr = server.accept()
            print("收到新的连接:", addr)
            rlist.append(client) #讲客户端通信IO放入读事件列表
        else: # 就绪IO是数据传输socket  
            data = r.recv(1024) # 读数据
            if not data:
                rlist.remove(r) # 移除,不在关注
                continue
            else:
                print("收到数据:", data.decode())
                wlist.append(r) # 加入写事件列表
    for w in ws:  # 写事件列表, 写数据
        w.send("Test Msg".encode())
        wlist.remove(w)
    # for x in xs:  # 异常事件列表, 异常处理
    #     pass

server.close()

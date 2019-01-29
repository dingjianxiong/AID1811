# file_recv.py
# 文件传输接收端
from socket import *
address = ("0.0.0.0", 9999)
server = socket()#创建TCP套接字
server.bind(address)
server.listen(5)
print("服务器已启动")
sockfd, addr = server.accept()#接受请求
try:
    f = open("recv.jpg", "wb")#二进制写模式打开文件
    while True: #循环从socket读取文件内容
        data = sockfd.recv(1024) 
        if not data: # 读取内容为空,不再读取
            break
        else:
            f.write(data)  #写入文件
    f.close() #关闭文件
except:
    print("打开或写入文件错误")
server.close()
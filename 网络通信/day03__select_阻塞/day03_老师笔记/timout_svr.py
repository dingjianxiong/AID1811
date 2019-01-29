# 超时示例
from socket import *
import time
address = ("0.0.0.0", 9999)
svr = socket()
svr.bind(address)
svr.listen(5)
print("服务器已启动:", address)

sockfd,addr = svr.accept()
print("收到客户端请求:",addr)
data = sockfd.recv(1024) #接收
print(data)
time.sleep(10) #sleep 10s
sockfd.send("timeout test msg".encode)
sockfd.close()
svr.close()
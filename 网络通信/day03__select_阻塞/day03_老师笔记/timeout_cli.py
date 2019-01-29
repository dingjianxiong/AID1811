# 简单客户端,超时示例
from socket import *
address = ("127.0.0.1", 9999)
client = socket()
client.settimeout(5)#设置超时时间
client.connect(address)
print("连接服务器成")
client.send("test msg".encode())
print("发送消息成功")
data = client.recv(1024) #接收超时
client.close()



# udp_svr.py
# UDP服务器示例
from socket import *
address = ("0.0.0.0",9999)
# 创建UDP socket:SOCK_DGRAM类型
server = socket(AF_INET, SOCK_DGRAM)
# 绑定
server.bind(address)
print("服务器已启动:", address)
# 收发消息
while True:
    data,addr = server.recvfrom(1024)
    if not data: #收到空数据
        break
    print("收到数据:", data.decode())
    print("发送自:", addr)
    # 回数据
    resp = "你发送的消息已收到:"+data.decode()
    server.sendto(resp.encode(), addr)

server.close()
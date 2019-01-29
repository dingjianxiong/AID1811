# broadcast_send.py
# 广播示例程序: 发送端
# 设置广播地址, 使用ifconfig命令查看
# IP:172.40.91.163  
# 掩码:255.255.255.0
# 广播:172.40.91.255
from socket import * 
dest = ("172.40.91.255", 9999)
s = socket(AF_INET, SOCK_DGRAM) #UDP套接字
# 设置广播选项
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
# 发送广播数据
msg = "Broadcast test message"
s.sendto(msg.encode(), dest) #发送广播信息
print("广播信息已发送")
s.close()


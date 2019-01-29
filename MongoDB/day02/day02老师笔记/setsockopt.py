# setsockopt.py
# socket属性/方法测试示例
from socket import *
address = ("0.0.0.0", 9999)
# 创建socket
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# SO_REUSEADDR 设置端口可以复用
# 允许同一端口启动同一服务器的多个示例
s.bind(address)
print("family:", s.family)#取地址类型
print("type:", s.type) #取套接字类型
print("getsockname:",s.getsockname())#地址
print("**** fileno:",s.fileno())
# 取得SO_REUSEADDR选项值
print("getsockopt:", 
   s.getsockopt(SOL_SOCKET,SO_REUSEADDR))
s.close()
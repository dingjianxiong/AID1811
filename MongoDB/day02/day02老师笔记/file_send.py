# file_send.py
# 读取并发送图片文件到服务器端
# 思路: 循环读取图片文件内容
#       图片读取,发送完成后就退出
from socket import *
# 创建套接字
client = socket() # TCP套接字
client.connect(("127.0.0.1", 9999))
# 读取文件内容并发送
try:
    # 以二进制读模式打开图片
    f = open("/home/tarena/jeans.jpg","rb")
    # 循环读取文件内容,并发送
    while True:
        data = f.read(1024)
        if not data:
            break
        else:
            client.send(data)#data是字节序列
    f.close() #关闭文件
except:
    print("打开或读取文件错误")
client.close()
#此示例示意文件的打开读写
# try:
#     #打开文件
#     # myfile=open("./myfile.py")
#     myfile=open("/home/test/djx/day16/myfile.py")
#     print("打开文件成功")
#     #读/写文件
#     F.read(n)#读取n个字符数据（文本方式)或字节数据(二进制方式)
#             #读取到
#     F.readline()#读取一行，以"\n"结束
#     F.readlines()#读取多行，返回多行，返回列表
#     #关闭文件
#     myfile.close()
#     print("关闭文件成功")
# except OSError:
#     print("打开失败")
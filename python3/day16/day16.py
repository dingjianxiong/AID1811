# day15回顾
#   生成器
#     两种:
#        生成器函数
#        生成器表达式
#   def 函数名(形参列表):
#       ...
#       yield 语句
#       ...
#   生成器函数的调用会返回生成器,生成器是可迭代对象
#   yield 语句
#      生成的数据是给 next(it) 函数
    
#   生成器表达式
#     (x for x in 可迭代对象 if 真值表达式 for y in ...)

#   zip(可迭代对象1, 可迭代对象2, 可迭代对象3, ....)
#       提供的数据的元组(数据1, 数据2, 数据3)
#   enumerate(可迭代对象, start=0)
#        (整数索引start, 数据1)

# 字节串bytes 和  字节数组 bytearray
#     (不可变)        (可变)

# 字节串的创建:
#   1.字面值
#      b'', b"", b'''''', b"""""", b'hello'
#   2.  构造函数 bytes
#     bytes()
#     bytes(整数n)
#     bytes(可迭代对象)  # 数据必须为0~255的整数
#     bytes(字符串, 编码='utf-8')
# 字节数组的创建
#     bytearray()
#     .... (同bytes的构造函数)

# 运算:
#   + += * *= 
#   < <= > >= == !=
#   in / not in         65 in b'ABC'
#   索引和切片  B[整数]   B[起始值:终止值:步长]
#   (注: 字节数组支持索引和切片赋值)
# 函数:
#   len, max, min, sum, any, all
# 字节数的方法:
#     B.append(xxx)
#     B.clear()
#     B.remove(...)
#     ....
#     >>> help(bytearray)



# day16 笔记:
# 文件 File
#   什么是文件
#     文件是用于数据存储的单位
#     文件通常用来长期存储数据
#     文件中的数据是以字节为单位进行顺序存储的

#   文件的操作流程:
#     1. 打开文件
#     2. 读/写文件
#     3. 关闭文件
#     注: 任何操作系统,一个应用程序, 同时打开文件的数量有最大
#         数限制
  
# 文件的打开函数:
#    open(file, mode='rt')  用于打开一个文件,返回已打开的
#                    文件流对象,如果打开文件失败,则会触发
#                    OSError类型的错误
#         返回值:
#             文件流对象
# 文件的关闭方法:
#   F.close()
#     作用:
#       关闭文件,释放系统资源

# 示例见:
#    file_open.py
#    file_open2.py

# 文本文件的读写操作
#   读方法:
#     F.read(size=-1)
#     F.readline()
#     F.readlines()
#     详细解释参见文档
#       python_base_docs_html/文件.html
#   示例见:
#     file_read.py

#   写方法:
#     F.write(字符串/字节串)  
#     F.writelines(字符串或字节串的列表)
#     详见文档:
#       python_base_docs_html/文件.html
#     示例见:
#       file_write.py

#     模式字符串:
#       'w'  只写
#       'x'  如果存在则报错
#       'a'  追加append
#       'r'  读

#   说明:
#     1.文本文件的读写操作是指默认把文件看成存储的内容都是字符数据
#     在读写过程中会自动进行编码(encode)和解码(decode),程序在
#     操作中都是以字符串为单位进行操作
#     2. 以行为单位分隔,在python内部统一用'\n' 作为换行符进行
#        分隔
#   各操作系统的换行符:
#     Linux换行符:       '\n'
#     Windows换行符:     '\r\n'
#     新的Mac OS X换行符: '\n'

#   文本文件的操作模式字符:
#     't'  默认
  
#   文件流对象是可迭代对象,迭代过程将以换行符'\n' 作用分隔符
#   依次获取
#     示例:
#       fr = open('myfile.txt')
#       for line in fr:
#           print(line)
      
# 练习:
#   自己写一个文件'info.txt' 内存存一些文字信息
#   内容和格式如下:
#     小张 20 100
#     小李 18 98
#     小赵 19 80
#   写程序将这些数据读取出来,并以如下格式打印在屏幕终端上
#     小张 今年 20 岁,成绩是: 100
#     小李 今年 18 岁,成绩是: 98
#     小赵 今年 19 岁,成绩是: 80
    

# 标准输入输出文件
#   sys.stdin   标准输入文件(默认是键盘)
#   sys.stdout  标准输出文件(默认是屏幕终端)
#   sys.stderr  标准错误输出文件(默认是屏幕终端)
#   模块名: sys

#   注: 标准文件不需要打开和关闭就可以直接使用
#   示例见:
#     stdout.py
# import sys
# sys.stdout.write("hello world\n")
# sys.stderr.write("我的出现是个错误！！\n")
# #sys.stdout.close()#文件为关闭状态，报错
# sys.stdout.write("我是正常输出\n")

#     stdin.py
# import sys
# # s=sys.stdin.readline()
# # print("你刚才输入的是：",s)
# # sys.stdin.close
# # s2=input("请输入：")
# # print(s2)

# s=sys.stdin.read()
# print("s=",s)


# 二进制文件操作:
#   二进制文件操作的模式字符:
#     'b'
#   说明:
#     默认文件中存储的都是以字节(byte)为单位的数据,通常有人为的
#     格式
#     对二进制文件的读写操作用字节串(bytes)或字节数
#       组(bytearray)进行操作
# a=open("myfile.py","rb")
# rw=a.read()
# print(rw)

#   读文件:
#     F.read()
#     F.readline()
#     F.readlines()
#     对于二进制文件操作 以上三个方法都会返回字节串或字节串数组
#   写文件:
#     F.write(字节串)
#     F.writelines(字节串列表)
#   示例见:
#     file_read_binary_mode.py
#     file_write_binary_mode.py


# try:
#   fr=open("myfile.py","rb")#打开文件，转为二进制编码
#   rw=fr.read(17)#获取17个字节
#   print(rw)
#   fr.close()#关闭文件
#   s=rw.decode()#编译转码
#   print("解码之后的内容是:",s)#输出
# except OSError:
#   print("文件打开失败")

#此示例示意向文件中写入256个字节
# b=bytes(range(256))
# try:
#   fw=open("mybinary","wb")
#   fw.write(b)
#   fw.close()
# except OSError:
#   print("写文件失败")

#     stdin.py
# import sys
# # s=sys.stdin.readline()
# # print("你刚才输入的是：",s)
# # sys.stdin.close
# # s2=input("请输入：")
# # print(s2)

#用程序写print函数
# import sys
# def myprint(*args,sep=" ",end="\n",file=sys.stdout,flush=False):
#   l=[str(obj) for obj in args]
#   file.write(sep.join(l))
#   file.write(end)#输入末尾字符
# myprint(1,2,3,4)

# F.seek方法
#   作用:
#     设置文件的读写位置    当前读写位置F.tell()
#   格式:
#     F.seek(偏移量, whence=相对位置)
#   参数说明:
#     偏移量:
#       大于0的数代表向文件末尾方向移动
#       小于0代表向文件头方向移动
#     相对位置:
#       0 代表从文件头开始偏移
#       1 代表从当前读写位置开始偏移
#       2. 代表从文件尾开始偏移
#   示例见:
#     seek.py

#此示例示意用文件流对象的seek方法来移动文件的读写指针位置
# try:
#   fr=open("byte20.text","rb")
#   b=fr.read(2)
#   print(b)
#   print("当前的读写位置是：",fr.tell())
#   fr.seek(5,0)#相对文件头偏移5个字节
#   b=fr.read(5)#从第五个开始读取
#   print("移动后：b=",b)
#   fr.close()
# except OSError:
#   print("读写失败！！")

# import time
# fw = open("myflush.txt", "w")

# fw.write("这是一行文字!")
# fw.flush()  # 强制清空缓冲区!
# input("请输入回车键继续: ")

# fw.close()
# print("程序退出")

# 练习:
#   写一个电话号码本存储程序,程序启动时循环输入
#      姓名和电话号码,把姓名和电话号码存入文件phone_book.txt
#     如:
#       请输入姓名: 小张
#       请输入电话号码: 13888888888
#       请输入姓名: 小赵
#       请输入电话号码: 13999999999
#       请输入姓名: <回车>结束输入
#     保存后文件内容如下:
#       小张,13888888888
#       小赵,13999999999

# F.flush 方法
#   作用:
#     用来清空缓冲区




# 汉字编码
#   国标系列:
#     GB18030(二字节或四字节编码,共27533个字)
#       GBK(二字节编码,共:21003个字)
#         GB2312(二字节编码, 共7千多个字)
#     注: Windows下常用
#   国际标准:
#     UNICODE32(四字节编码)
#       UNICODE16(二字节编码)
#     (注:Linux/Mac OS X / IOS / Android常用)
#     UTF-8(8-bit Unicode Transformation Format)
#       (一字节,二字节, ....  六字节)
#       0x07FF-0XFFFF(3字节编码（汉字区域）)
# 问题:
#   十个汉字占多少个字节?

# python编码字符串
#   'gb2312'
#   'gbk'
#   'gb18030'
#   'utf-8'
#   'ascii'
#   ....

# 编码注释:
#   在源文件的第一行或第二行写入如下内容为编码注释
#     # -*- coding:gbk -*-
#     # 设置源文件的编码格式为gbk
#     或
#     # -*- coding:utf-8 -*-
#     # 设置源文件的编码格式为utf-8
  
#   作用是告诉python解释执行器当前文件的编码格式是什么?
#     示例见:
#       hello_gbk.py
          




# 练习:
#   1. 写程序,实现复制文件的功能
#     要求:
#       1) 要考虑文件关闭的问题
#       2) 要考虑超大文件的问题(文件太大时将无法全部加载到内存)
#       3) 要能复制二进制文件

#   2. 修改原来的学生信息管理程序,加入两个功能:
#     | 9) 从文件中读取数据(si.txt)   |
#     | 10) 保存信息到文件(si.txt)    |
#     文件格式自己定义(建议用逗号分隔的文本文件保存)
  




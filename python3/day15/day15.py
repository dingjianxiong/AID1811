# day14
#   异常 exception
#     错误
#     异常
#     作用:
#       用作信号通知
#   异常相关的语句:
#     try-except语句
#       try:
#             .. 可能发生异常的语句
#       except 类型1 as 变量1:
#             语句
#       except ....:
#       ...
#       except : 
#           语句
#       else:
#           没有发生异常时执行的语句
#       finally:
#           最终一定要执行的语句
    
#     try-finally 语句
#        执行必须要执行的语句
#     raise 语句
#        触发异常(通知)  让程序进入异常状态(走异常流程)
#     assert 语句
#        当条件不满足时,触发AssertionError类型的错误!

# Python 全部的异常类型
#   >>> help(__builtins__)

# 迭代器 iterator
#   iter(可迭代对象)  函数返回的对象是迭代器

#   变量 = next(迭代器)  # 向可迭代对象取值

#   当迭代器不能提供数据, 会触发StopIteration异常来进行通知

#   for 语句
#      for 变量 in 可迭代对象:
#           语句块







# day15笔记 :
# 生成器 Generator (python 2.5 及之后版本)
#   生成器是能够动态提供数据的可迭代对象
#   生成器是在程序运行时生成数据,与容器类不同,它通常不会在内存
#   中保存大量的数据,而是现用现生成

#   生成器的种类(有两种):
#     生成器函数
#     生成器表达式

# 生成器函数
#   含有yield语句的函数是生成器函数,此函数被调用将返回一个
#   生成器对象
#   yield翻译为(产生或生成)

#   yield 语句
#     语法:
#       yield 表达式
#     说明:
#       yield 用于 def 函数中,目的是将此函数作为生成器函数使用
#       yield 用来生成数据,提供迭代器 next(it) 函数使用
#     示例见:
#       yield.py
#       yield2.py
    
# 生成函数说明:
#   生成器函数的调用返回一个生成器对象,生成器对象是可迭代对象
#   在生成器函数调用return会触发一个StopIteration异常(即生成
#     结束)
#   生成器函数调用时返回的生成器是一次性的,当生成结束后将不再提供
#   数据
#   生成器生成整数的示例见:
#     generator_function.py

# 生成器函数练习:
#   1. 写一个生成器函数:
#     def even(start, stop):
#         '''此生成器函数生成从start开始,到stop结束(不包含stop)
#          的全部偶数'''
#          ... 以下自己实现

#     for x in even(1, 10):
#        print(x)  # [2, 4, 6, 8]
#     L = [x**2 for x in even(10, 20)]
#     print(L)  # [100, 144, ...]

#     it = iter(even(3, 10))
#     print(next(it))  # 4
#     print(next(it))  # 6
#     print(next(it))  # 8
#     print(next(it))  # StopIteration




# 生成器表达式
#   语法:
#     (表达式 for 变量 in 可迭代对象 [if 真值表达式]])
#   说明:
#     if子句可以省略
#     for in 子句可以嵌套多个
#   作用:
#     用推导式形式创建一个新的生成器
#   示例:
#     gen = (x**2 for x in range(1, 5))
#     it = iter(gen)
#     next(it)  # 1
#     next(it)  # 4
#     next(it)  # 9
#     next(it)  # 16
#     next(it)  # StopIteration

# 1. 已知有列表:
#     L = [2, 3, 5, 7]
#     1) 写一个生成器函数,让此函数能够动态提供数据, 提供的数据
#       为原列表的数字的平方+1
#     2) 写一个生成器表达式,让此表达式能够动态提供数据,提供的数
#       据依旧为原列表的数字的平方+1
#     3) 写一个列表,此列表内的数据为原列表的数字的平方+1


# 2. 试写一个生成器函数 myfilter,要求此函数与系统内建的
#     filter函数功能相同
#     如:
#     def myfilter(fn, iterable):
#         ..... # 此处自己实现
    
#     for x in myfilter(lambda y:y%2==1, range(10)):
#         print(x)  # 1 3 5 7 9
    
# 3. 看下列程序的输出结果是什么?为什么?
#   第一个程序:
#     L = [2, 3, 5, 7]
#     A = [x * 10 for x in L]
#     it = iter(A)
#     print(next(it))  # 20
#     L[1] = 333
#     print(next(it))  # 30

#   第二个程序:
#     L = [2, 3, 5, 7]
#     A = (x * 10 for x in L)
#     it = iter(A)
#     print(next(it))  # 20
#     L[1] = 333
#     print(next(it))  # 3330




# 迭代工具函数:
#   zip(iter1[,iter2, iter3, ....])  返回一个zip对象,此对
#       象用于生成一个元组,此元组的数据分别来自于参数中的每个可
#       迭代对象,生成元组的个数由最小的可迭代对象决定
#   enumerate(iterable, start=0)   返回一个enumerate对象
#       此对象生成的类型为(索引,值)的元组,默认索引从零开始,也可
#       以用第二个参数start指定

# 示例:
#   numbers = [10086, 10000, 10010, 95588]
#   names = ['中国移动', '中国电信', '中国联通']
#   for t in zip(numbers, names):
#       print(t)  # (10086, '中国移动') (10000, '中国电信')

#   for a, b, c in zip(range(1, 10000), names, numbers):
#       print("第", a, '个', b, '的客服电话是', c)
#   # 看懂如下语句在做什么事儿?
#   d = dict(zip(numbers, names))

# enumerate 示例:
# names = ['中国移动', '中国电信', '中国联通']
# #   for t in enumerate(names):
# #       print(t)  # (0, '中国移动') (1, '中国电信'), (2,..)

# for no, n in enumerate(names, 1):
#     print("第", no, '个名字是', n)

# 练习:
#   写一个成生器函数myenumerate,要求此函数的功能与内建的
#       enumerate 函数功能完全相同
#     如:
#         def myenumerate(iterable, start=0):
#              .... 以下自己实现
#     测试:
#         d = dict(myenumerate("ABCDE", 1))
#         print(d)  # {1:'A', 2:'B', 3:'C', ...}
    
# 示例:
#   自己实现myzip 函数 功能与zip完全相同,要求只传入两个可迭代对象
#     def myzip(iter1, iter2):
#         .... # 此处自己实现
    
#     d = dict(myzip("ABC", "123"))
#     print(d)  # {'A': '1', 'B': '2', 'C': 3}

# 字节串和字节数组
#   回顾:
#     字符串 str 是用于存储文字信息的序列
#     序列有几种:
#        str, list, tuple, bytes, bytearray

# 字符串(字节序列) bytes
#   作用:
#     存储以字节为单位的数据

# 什么是字节
#   一个字节(byte)等同于8个位(bit)
#   字节是 0~255的整数,用来表示一个字节的取值

# 字节串bytes
#   创建空字节串的字面值:
#     b''
#     b""
#     b''''''
#     b""""""
#   创建非空的字节串的字面值表示:
#     b'ABCD'
#     b"hello"
#     b'\x41\x42'

# 字节串的构造函数 bytes
#   bytes()              生成一个空的字节串,等同于 b''
#   bytes(整数可迭代对象)  用可迭代对象创建一个字节串
#   bytes(整数n)          生成n个值为0的字节串
#   bytes(字符串, encoding='utf-8')  用字符串的转换编码
#                        生成一个字节串

# 示例:
#     B = bytes()  # 空字节串
#     B = bytes([65, 66, 67, 68])  # B = b'ABCD'
#     B = bytes(5)  # B ='\x00\x00\x00\x00\x00'
#     B = bytes("你好ABC", 'utf-8')  # B= 

# 字节串的运算
#   + += * *= 
#   < <= > >= == !=
#   in / not in
#   索引和切片
#   示例:
#     b1 = b'ABC123'
#     65 in b1  # True
#     b'123' in b1  # True
#     print(b1[0])  # 65
#     print(b1[::2])  # b'AC2'
    
# 可以用于字节串的函数:
#    len(x), max(x), min(x), sum(x), any(x), all(x)

# bytes 与 str 的区别
#   bytes 存储字节(0~255)
#   str 存储unicode 字符(0~65536或更大)
  
# bytes 与 str 转换
#        编码(encode)
#   str -------------> bytes
#     b = s.encode(encoding='utf-8')
  
#          解码(decode)
#   bytes -------------> str
#      s = b.decode(encoding='utf-8')
# s="hello"
# b = s.encode(encoding='utf-8')   
# print(b)
# c=b'hello'
# t = c.decode(encoding='utf-8')
# print(t)

# 字节数组 bytearray
#   可变的字节序列

# 字节数组的构造函数 bytearray
#   bytearray()              生成一个空的字节数组
#   bytearray(整数可迭代对象)  用可迭代对象创建一个字节数组
#   bytearray(整数n)          生成n个值为0的字节数组
#   bytearray(字符串, encoding='utf-8')  用字符串的转换编码
#                        生成一个字节数组

# 字节数组的运算
#   + += * *=
#   < <= > >= == != 
#   in / not in 
#   索引 index /切片 slice
#   注:  字节数组支持索引和切片赋值,规则同列表的索引和切片赋
#        值规则 

# 字节数组的方法:
#   见文档:
#     python_base_docs_html/bytearray.html
  


# 练习:
#   写一个程序,从键盘输入一段字符串,用变量s绑定
#     1. 将此字符串转为字节串用变量b绑定,并打印出来
#     2. 打印字符串s的长度和字节串的长度
#     3. 将字节串再转换为字符串变量s2绑定,判断s2与s是否相同
#     再将上述字节串改为字节数组完成上面的练习

# 练习:
#   1. 写一个生成器函数 myxrange(start, stop, step), 
#   来生成一系列整数,规则与range函数完全相同
#   (不允许调用range)
#     用自己写的myxrange结合生成器表达式求1~10的奇数的平方和
   
#   2. 写一个生成器函数 myprimes(n), 此生成器函数用来生成
#     n个素数
#       如:
#         for x in myprimes(5):
#             print(x)  # 2 3 5 7 11
#   3. 写一个程序, 读入任意行的文字,当输入空行时输入结束.
#     打印带有行号的输入结果
#      如:
#        请输入: hello<回车> 
#        请输入: 你好<回车> 
#        请输入: bye<回车> 
#        请输入: <回车> 
#      打印如下:
#        第1行: hello
#        第2行: 你好
#        第3行: bye







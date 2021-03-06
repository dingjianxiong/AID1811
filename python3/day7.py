# day07 回顾:
#   元组 tuple
#   字典 dict

# 元组
#   ()
#   "abcd",
#   ('',)
#   (100, 200, "hello")
#   tuple()
#   tuple("ABCD")
#   运算:
#     +  +=   *  *= 
#     <  <= > >= == != 
#     in / not in 
#     索引/切片
#   序列:
#     字符串 str
#     列表 list
#     元组 tuple

# 字典 dict
#   可变的容器
#   键-值对
#   索引方式为键索引

#   创建方式:
#     {}
#     {1:"One"}
#     {1:"One", 2:"Two"}
#     dict()
#     dict(可迭代对象)
#   字典的方法:
#     D.clear()
#     D.pop(key)   删除一个键,同时返回键所对应的值
#     D.copy()  浅拷贝
#     D.update(D2)
#     D.get(key,default=None)  # D[key]
#     D.keys()  
#     D.values()  
#     D.items()  

#   字典推导式
#     {键表达式: 值表达式 for 变量 in 可迭代对象 if 真值表达式}

# 列表是顺序存储
# 字典是散列存储





# day08笔记:
# 集合 set
#   集合是可变的容器
#   集合内的数据对象都是唯一的(不能重复多次的)
#   集合是无序的存储结构,集合中的数据没有先后顺序关系
#   集合内的元素必须是不可变对象
#   集合是可迭代对象
#   集合是相当于只有键没有值的字典(键则是集合的数据)

# 创建空集合
#   set()
# 创建非空集合的字面值:
#   s = {1, 2, 3}
#   s = {"hello", "china"}
# 集合的构造(创建)函数 set
#   set()  创建一个空的集合对象(不能用{} 来创建空集合)
#   set(iterable)  用可迭代对象创建一个新的集合对象

#   示例:
#     s = set(range(10))  # {0, 1, 2, 3, 4...., 9}
#     s = set("ABCD")
#     s = set("ABCCBA")  #  s ={'A', 'B', 'C'}
#     s = set({1:'One', 5:'five'})  # {1, 5}
#     s = set([1, 0, 3.14, 0.618])
#     s = {True, None, "ABC", (1, 2, 3)}


# 集合的运算:
#   交集&, 并集|, 补集-, 对象补集^, 子集<   超集>

# & 生成两个集合的交集
#   s1 = {1, 2, 3}
#   s2 = {2, 3, 4}
#   s3 = s1 & s2  # s3 = {2, 3}

# | 生成两个集合的并集
#   s1 = {1, 2, 3}
#   s2 = {2, 3, 4}
#   s3 = s1 | s2  # s3 = {1, 2, 3, 4}

# - 生成两个集合的补集
#   s1 = {1, 2, 3}
#   s2 = {2, 3, 4}
#   s1 - s2  # {1}, 生成属于s1,但不属于s2的所有元素的集合

# ^ 生成两个集合的对称补集
#   s1 = {1, 2, 3}
#   s2 = {2, 3, 4}
#   s3 = s1 ^ s2  # {1, 4} # 等同于(s1-s2 | s2-s1)

# < 判断一个集合是另一个集合的子集
# > 判断一个集合是另一个集合的超集
#   s1 = {1, 2, 3}
#   s2 = {2, 3}
#   s1 > s2  # True
#   s2 < s1  # True

# == != 集合相同或不同
#   s1 = {1, 2, 3}
#   s2 = {3, 2, 1}
#   s1 == s2  # True
#   s1 != s2  # False

# <=  >= 子集或相同,超集或相同
#    示例略

# in , not in 运算符
#   等同于字典, in 运算符用于集合中时,判断某个元素是否存在于
#   集合中,如果是则返回True,否则返回False


# 用于集合的函数:
#   len(x), max(x), min(x), sum(x), any(x), all(x)

# 集合是可迭代对象


# 集合练习:
#   经理有: 曹操, 刘备, 孙权
#   技术员有: 曹操,刘备,张飞,关羽
#   用集合求:
#     1. 即是经理也是技术员的有谁?
#     2. 是经理,但不是技术人员的有谁?
#     3. 是技术人员,但不是经理的人都有谁?
#     4. 张飞是经理吗?
#     5. 身兼一职的人都有谁?
#     6. 经理和技术员共有几个人?
# a={"曹操","刘备", "孙权"}
# b={"曹操","刘备","张飞","关羽"}
# print(a&b)
# print(a-b)
# print(b-a)
# print("张飞" in a)
# print(b^a)
# print(len(b|a))

# 集合的方法:
#   文档参见:
#     python_base_docs_html/set.html

# 集合推导式
#   集合推导式是用可迭代对象创建集合的表达式
#   语法:
#     {表达式 for 变量 in 可迭代对象 [if 真值表达式]}
#     注[] 代表其中的内容可省略
#   示例:
#     numbers = [1, 3, 5, 3, 5, 1]
#     s = {x**2 for x in numbers} # s = {1, 9, 25}
#   集合推导式嵌套
#     嵌套规则同列表推导式嵌套



# 固定集合  frozenset
#   固定集合是不可变的,无序的,含有唯一元素的集合
#   作用:
#     固定集合可以作为字典的键,也可以作为集合的值

# 固定集合的构造函数 frozenset
#   frozenset()  创建一个空的固定集合
#   frozenset(iterable)  用可迭代对象创建一个新的固定集合
#   示例:
#     fz = frozenset("hello")  # frozenset({'l', 'o', 'e', 'h'})

# 固定集合的运算:
#   & 交集  --->   &=
#   | 并集  --->   |=
#   - 补集  --->   -=
#   ^ 对称补集 ---> ^=
#   in / not in 
#   >  >= < <= == != 
#   (以上运算规则等同于集合set中的运算规则)

# 固定集合的方法:
#   相当于集合的全部方法 "去掉修改集合" 的方法


# 阶段总结
#   数据类型:
#     不可变数据类型:
#       bool, int, float, complex
#       str, tuple, frozenset, bytes(字节串,后面才学)
#     可变数据类型:
#       list dict, set, bytearray(字节数组,后面才学)
#   值:
#     None, False, True

#   运算符:
#     +  -  *  /  // %  **
#     < <= > >= == !=
#     is, is not   # 验证id
#     in, not in   # 判断一个值是否在容器内
#     not   and   or   # 布尔运算
#     &  |  ^      # 集合运算(位运算符)
#     +(正号)  - (负号)

#   表达式:
#     1
#     1 + 2
#     sum([1, 2, 3]) + sum([4, 5, 6])
#     print("hello")
#     条件表达式  x if x > y else y
#     全部的推导式:  [x for x in range(...)]
#       列表,字典,集合推导式
#     lambda  (返回一个函数, 后面才学)

#   语句
#     表达式语句
#        input("请输入字符串")  # 函数调用是表达式,
#        "abcd"
#     赋值语句
#       变量名(标识符) =  表达式
#       a = 100
#       a = b = c = 200
#       x, y, z = 100, 200, 300
#     del 语句
#       删除变量,可能会释放对象(引用计数)
#     if 语句
#     pass 语句
#     while 语句
#     for 语句
#     break 语句
#     continue 语句

#   内建函数
#     len(x)
#     max(x)
#     min(x)
#     sum(x)
#     any(x)
#     all(x)
#     ------  构造(创建)函数 ----
#     bool(x)
#     int(x)
#     float(x)
#     complex(x)
#     str(x)
#     list(x)
#     tuple(x)
#     dict(x)
#     set(x)
#     frozenset(x)
#     ------- 数值相关的函数-------
#     abs(x)
#     round(x)
#     pow(x, y, z=None)
#     ------- 字符串相关的函数----
#     bin(x)
#     oct(x)
#     hex(x)
#     chr(x)
#     ord(x)
#     ------- 可迭代对象相关的函数---
#     range(start, stop, step)
#     reversed(x)
#     ------- 输入输出函数---------
#     input(x)
#     print(...)
#     -------- 对象和类型---------
#     type(x)
#     id(x)
#     --------------
#     sorted(x)
#     详见:
#        >>> help(__builtins__)







# 函数 function
# 什么是函数
#   函数是可以重复执行的语句块,可以重复调用
#   函数是面向过程编程的最小单位

# 作用:
#   1. 用于封装语句块,提高代码的重用性
#   2. 定义用户级别的函数

# def 语句
#   语法:
#     def 函数名(形参列表):
#         语句块(代码块)

#   说明:
#     1. 函数的名字是语句块的名称
#     2. 函数名的命名规则与变量名相同(函数名必须为标识符)
#     3. 函数名是一个变量(不要轻易对其赋值)
#     4. 函数有自己的名字空间,在函数外部不可以访问函数内部的
#        变量,在函数内部可以访问函数外部的变量(取值)
#     5. 函数如果不需要传入参数,则参数列表可以为空
#     6. 语句部分不能为空,如果为空需要填充pass语句
#   示例见:
#     def.py
#     def2.py
# def max1(a,b):
#     if a<b:
#         print(b,"最大")
#     else:
#         print(a,"最大")
# c=int(input("输入整数"))
# d=int(input("输入整数"))
# max1(c,d)

# 函数调用
#   语法:
#     函数名(实际调用传递参数)
#   说明:
#     函数调用是一个表达式
#     如果没有return语句,函数执行完毕后返回None对象

# 练习
#   1. 写一个函数myadd, 此函数中的参数列表里有两个参数x, y
#   此函数打印两个参数的和(即, x + y 的和)
#     def myadd(...):
#         ....
#     myadd(100, 200)  # 打印 300
#     myadd("ABC", "123")  # 打印 ABC123
# def myadd(x,y):
#     w=x+y
#     print(w)
# c=int(input("输入整数"))
# d=int(input("输入整数"))
# myadd(c,d)
#   2. 写一个函数print_even,传入一个参数n代表终止整数
#     此函数打印 2 4 6 .... n(不包含n)以内的所有偶数
#     函数定义如下:
#       def print_even(n):
#           ..... # 此处自己实现
      
#       print_even(10)
#       打印
#       2
#       4
#       6
#       8
# def print_even(n):
#     for x in range(2,n,2):
#         print(x)
# c=int(input("输入整数"))
# print_even(c)

# return 语句
#   语法:
#     return [表达式]
#     注: []代表可以省略
#   作用:
#     用于函数中,结束当前函数的执行,返回到调用该函数的地方,同
#     时返回一个对象的引用关系
#   说明:
#     return 语句后跟的表达式可以省略,省略后相当于return None
#     如果函数内没有return语句,则函数执行完最后一条语句后
#     返回None(相当于在最后加了一条return None语句)
#   示例见:
#     return.py
# def say_hello():
#     print("hello aaa")
#     print("hello bbb")
#     # return ["结束"]
#     print("hello ccc")
#     return
# v = say_hello()
# print('v=', v)
# print(say_hello())

# 练习:
#   1. 写一个函数mymax(实现返回两个数的最大值)
#       如:
#         def mymax(a, b):
#             ....
#         print(mymax(100, 200))  # 200
#         print(mymax("abc", 'ABCD'))  # abc
# def mymax(a,b):
#     # if a>b:
#     #     return (a,"最大")
#     # else:
#     #     return (b,"最大")
#     # return ("和是",a+b)
#     return a if a>b else b
# c=int(input("输入整数"))
# d=int(input("输入整数"))        
# print(mymax(c,d))

#   2. 写一个函数 mysum, 实现给出两个数,返回这两个数的和
#     def mysum(x, y):
#        ...
#     a = int(input("请输入第一个数: "))
#     b = int(input("请输入第二个数: "))
#     print("您输入的两个数的和是:", mysum(a, b))
# def mysum(x,y):
#     return (x+y)
# a = int(input("请输入第一个数: "))
# b = int(input("请输入第二个数: "))
# print("您输入的两个数的和是:", mysum(a, b))
#  3. 写一个函数input_number
#     def input_number():
#          ....
#     函数用来获取用户循环输入的整数,当用户输入负数时结束输入
#     将用户输入的数字以列表的形式返回,再用内建函数max,min
#     sum等求出用户输入的最大值,最小值及和
#     L = input_number()
#     print(L)
#     print("用户输入的最大值是:", max(L))
#     print("用户输入的最小值是:", min(L))
#     print("用户输入的数据之和是:", sum(L))

# def input_number():
#     l=[]
#     while True:
#         a=int(input("输入整数："))
#         if a<0:
#              break#ruturn l
#         elif a=="":
#             ruturn l
#         else:
#             l.append(a)
#     return l
# l=input_number()
# print("用户输入的最大值是:", max(l))
# print("用户输入的最小值是:", min(l))
# print("用户输入的数据之和是:", sum(l))

# 练习:
#   1. 定义两个函数:
#     sum3(a, b, c)  用于返回三个数的和
#     pow3(x)        用于返回x的三次方(立方)
#     用以上函数计算:
#       1) 计算 1的立方+2的立方+3的立方的和
#       2) 计算 1+2+3的和的立方
#           即: 1**3+2**3+3**3 和 (1+2+3)**3
#   2. 写一个函数 get_chinese_char_count(s) , 此函数返回
#     一个字符串s中所有中文字符的个数
#         def get_chinese_char_count(s):
#             ...
#         s = input("请输入中英文混合的字符串: ")
#         print("您输入的中文字符的个数是:", 
#             get_chinese_char_count(x))
#     注:
#       中文编码范围是: 0x4E00 ~ 0x9FA5(包含)
# def get_chinese_char_count(s):
#     sum=0
#     for x in s:
#         if 0x4E00<=ord(x)<=0x9FA5:
#                 sum+=1
#     return sum
# s = input("请输入中英文混合的字符串: ")
# print("您输入的中文字符的个数是:",get_chinese_char_count(s))
# for x in range(65535):
#     print(chr(x),end='')
#   3. 修改学生信息管理程序,将其修改为两个函数实现
#     函数1:
#         def input_student():
#            ....  # 此函数返回输入学生信息的列表(格式不变)
        
#     函数2:
#         def output_student(L):
#             ... 此处以表格式形式打印学生信息(表格样式不变)
#     测试函数:
#         infos = input_student()
#         print(infos) # 打印字典组成的列表
#         output_student(infos)  # 打印表格
#     保证修改后原功能不变

#  2. 定义两个函数:
#      sum3(a, b, c)   用于返回三个数的和
#      pow3(x)         用于返回x的三次方
#     用以下函数计算:
#        1)  计算1的立方 + 2的立方 + 3的立方的和
#        2)  计算1+2+3的和的立方
#        即:1**3+2**3+3**3 和 (1+2+3) ** 3
# def sum3(a,b,c):
#     return a+b+c
# def pow3(x):
#     return x**3
# w=int(input("输入："))
# e=int(input("输入："))
# r=int(input("输入："))
# print(sum3(pow3(w),pow3(e),pow3(r)))
# print(pow3(sum3(w,e,r)))

# 3. 编写函数fun ,其功能是计算并返回下列多项式的值
#     Sn = 1 + 1/2 + 1/3 + 1/4 + .... + 1/n
#       def fun(n):
#           ...
#       print(fun(2))   # 1.5
#       print(fun(3))   # 1.8333333333333
#       print(fun(10))  # ????

# def fun(n):
#     sum=0
#     for x in range(1,n+1):
#         sum+=1/x
#     return sum
# print(fun(3))
# print(fun(2))
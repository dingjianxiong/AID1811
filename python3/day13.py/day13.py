# day12回顾
#   装饰器 decorator
#     @装饰器函数
#     def 被装饰函数名(形参列表):
#         ...

#     # 装饰器函数的定义方式:
#     def 装饰器函数(fn):
#         创建一个闭包函数
#         return 返回这个闭包函数
    
#   函数的文档字符串
#     >>> help(函数名)
#     def 函数名(....):
#         '''文档字符串'''  # 此字符串会赋值组函数名.__doc__
#   函数的属性
#     __doc__ 
#     __name__属性  用绑定函数的名字

# 模块 Module
#   模块的导入语句:
#     import 语句   :   import math, sys
#     from import 语句    # from math import sin,cos
#     from import *语句   # from math import *
#   原理是在当前作用域内创建 一个本地变量

#   函数:
#     dir(x)  
#     help(x)

# 内建模块的使用:
#   math 模块
#   time 模块 时间相关的函数等
#   sys 模块  运行时系统相关

# 模块分为四类:
#   内建模块  (通常是C语言开发的,通常在python3内部)
#   标准库模块 (通常是python语言开发的,通常在/usr/lib/python3.5)
#   第三方模块
#   自定义模块



# 自定义模块并导入
#   要求:
#     模块文件后缀名必须以.py结尾
#     模块文件名必须是合法的标识符
#     避免名称和内建模块名冲突
#   导入方式:
#     import 语句
#     from import 语句
#     from import *语句
#   正确的模块名:
#     mymod.py  abcde.py  abc123.py
#   错误的模块名:
#     123.py  abc.cpp  math.py

#   示例见:
#     mymod.py  # 自定义模块文件
#     test_mymod.py  # 主模块(用来导入和调用mymod里的函数)


# import 语句 搜索模块的路径顺序
#   1. 搜索内建模块
#   2. 搜索程序的运行时路径(当前工作目录)
#   3. sys.path 提供的路径
#       sys.path是一个列表,里面放的都是模块的搜索路径

# 模块化编程的优点:
#   1. 有利于多人合作开发
#   2. 使代码更加利于维护
#   3. 提高代码的复用率
#   4. 模块化编程有助于解决函数名和变量名冲突(重名) 问题,模块内
#      的变量作用域为模块内全局
  
# 模块的加载过程:
#   在模块导入时,模块的所有语句都会执行
#   如果一个模块已经导入,则再次导入时不会重新执行模块内的语句

# 模块新的重载加载
#    import mymod
#    import imp
#    imp.reload(mymod)  # 重新加载已加载的mymod模块
#    注:  此做法通常只在开发阶段调式时使用

# 模块被导入的执行的过程
#   1. 先搜索相关的路径,找到.py文件
#   2. 判断是否有此文件对应的.pyc文件, 如果没有.pyc文件,则用
#      .py文件生成.pyc文件 
#   3. 如果存在 .pyc文件,需要判断.py是否比.pyc文件新.如果新则
#      重新生成.pyc, 然后再加载.pyc文件 
    
#   pyc文件 ,模块的编译文件
#               编译            解释执行
#     mymod.py  ----> mymod.pyc------> python3

# 模块的属性
#   模块的文档字符串
#     __doc__属性
#       作用:
#         用来绑定模块的文档字符串
  
#   __file__属性
#     作用:
#       用来绑定模块对应的文件路径名
#     注:
#       内建模块没有__file__属性(如:math模块)
  
#   __name__属性
#     作用:
#       1. 用来记录模块的自身的名字
#       2. 用来判断是否为主模块
    
#     注: 主模块是指程序中第一个执行起来的模块
#     说明:
#       当此模块作为主模块运行时,__name__属性 绑定'__main__'
#       当此模块不作为主模块运行时,此__name__属性绑定模块名
#          如:mymod.py 的模块名为'mymod'
    
  

# 模块的 __all__列表
#   模块中 __all__列表是一个用来存放可导出属性的字符串列表
#   作用:
#     限定在用from xxx import *导入时,只导入__all__列表
#     内的属性
#   示例见:
#     mymod3.py
#   注:  此__all__列表,只对from import *语句有效

# 模块的隐藏属性
#   模块中以下划线(_)开头的属性 在 from import *语句导入时
#   将不被导入,通常称这些属性为隐藏属性

#   示例见:
#     mymod4.py

# 标准库模块
#   随机模块 random
#     作用:
#       用于模拟或生成随机数的模块
#     文档参见:
#       python_base_docs_html/随机模块random.html
  
  

# 练习:
#   1. 猜数字游戏
#      随机生成一个0~100的整数,用变量x绑定
#      让用户输入一个数y,输出猜数字的结果
#        如果y大于x,则提示"您猜大了", 继续让用户输入
#        如果y小于x,则提示"您猜小了", 继续猜
#        如果y等于x,则提示"恭喜您猜对了", 打印出猜数字的次数
#          然后退出程序
#     注:
#       直到猜对才退出
# import random as R
# sum=0
# while True:
#     b=int(R.randint(1, 100))#
#     a=int(input("输入一个数字"))
#     sum+=1
#     if a>b:
#         print("你猜大了")
#     elif a<b:
#         print("你猜小了")
#     elif a==b:
#         print("你猜对了","一共猜了",sum,"次")
#         break
# 包 package
#   包的定义
#     包是将模块以文件夹的形式进行分组管理的方法
#   作用:
#     将一系列模块进行分类管理,有利于防止命名冲突
#     可以在需要时加载一个或部分模块而不是全部模块
  
#   包示例:
#     mypack/
#         __init__.py
#         menu.py
#         games/
#             contra.py
#             supermario.py
#             tanks.py
#             __init__.py
#         office/
#             __init__.py
#             word.py
#             excel.py
            
    
# 包的导入:
#   同模块的导入规则相同
#   语法:
#     import 包名 [as 包别名]
#     import 包名.模块名 [as 模块新名]
#     import 包名.子包名.模块名 [as 模块新名]
#     ...

#     from 包名 import 模块名 [as 模块新名]
#     from 包名.子包名 import 模块名 [as 模块新名]
#     from 包名.子包名.模块名 import 属性名 [as 属性新名]
#     ...

#     from 包名 import *
#     from 包名.模块名 import *

# import 语句搜包的路径顺序
#    1. 搜索当前运行时路径(当前工作目录)
#    2. 搜索sys.path 提供的路径
# __init__.py 文件
#   是常规包内必须存在的文件
#   __init__.py 会在包加载时自动调用

#   作用:
#     编写此包的内容
#     在内部填写文档字符串
#     在__init__.py文件内可以加载此包所依懒的一些其它模块
#   示例见:
#     mypack/__init__.py


# __init__.py 内的 __all__列表
#   作用:
#     用来记录此包中有哪些模块或子包需要导入
#     当用from 包 import *语句导入模块时,只查找__all__中
#     所有的模块或子包
#   说明:
#     __all__列表只对 from import *语句起作用
#   示例见:
#     mypack/games/__init__.py


# 包的相对导入
#   包的相对导入是指包内模块的相互导入

#   语法:
#     from 相对路径包或模块 import 属性名或模块名
#     或
#     from 相对路径包或模块 import *

#   相对路径:
#     在用from xxx import yyy 语句中
#     xxx 部分可以使用相对路径
#     . 代表当前目录
#     .. 代表上一级目录
#     ... 代表上二级目录
#     .... 以此类推
#     注: 相对导入时不能超出包的外部
#   示例见:
#     mypack/games/contra.py 






# 练习:
#   1. 使用随机模块,随机生成6位的密码
#      可以作为密码的字符有:
#        a-z  A-Z 0-9
#      写一个程序,每次调用时能随机生成一个密码
#   2. 模拟斗地主游戏发牌,牌共54张
#      黑桃('\u2660'), 梅花('\u2663'),
#      红桃('\u2666'),方块('\u2665')
#      大小王
#      数字: A2~10JQK
#      三个人,每人发17张牌,底牌留三张
#      输入回车,打印第一个人的17张牌
#      输入回车,打印第二个人的17张牌
#      输入回车,打印第三个人的17张牌
#      输入回车,打印3张底牌
# import random
# def pai():
#     l=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
#     l2=["大王","小王"]
#     l1=[]
#     for x in l:
#         l1.append('\u2660'+x)
#         l1.append('\u2666'+x)
#         l1.append('\u2663'+x)
#         l1.append('\u2665'+x)
#     l1=l1+l2
#     a1=random.sample(l1,17)
#     for x in a1:
#         l1.remove(x)
#     b1=input("打印第一个人的17张牌:")
#     if b1=="":
#         print(a1)
#     a2=random.sample(l1,17)
#     for x1 in a2:
#         l1.remove(x1)
#     b2=input("打印第二个人的17张牌:")
#     if b1=="":
#         print(a2)
#     a3=random.sample(l1,17)
#     for x2 in a3:
#         l1.remove(x2)
#     b3=input("打印第三个人的17张牌:")
#     if b3=="":
#         print(a3)
#     b4=input("打印最后的底牌:")
#     if b4=="":
#         print(l1)
# pai()

#   3. 将学生信息管理程序拆分为模块s
#       要求:
#         1. 主事件循环放在main.py中
#         2. show_menu 函数放在menu.py中
#         3. 与学生操作相关的函数放在 student_info.py中

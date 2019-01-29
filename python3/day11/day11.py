# day11回顾
#   函数式编程
#     函数的可重入性
#       可重入函数
#         没有使用除部变量以外的变量的函数
#         输入一定,结果必须一定
#       不可重入函数
#          使用除部变量的外的变量的函数
#   高阶函数:
#     map(函数,可迭代对象1, 可迭代对象2, ....)
#       参数
#         函数 ,形参个数要和可迭代对象的个数相同
    
#     filter(过滤函数, 可迭代对象)
#       参数
#          过滤函数只能有一个形参,此函数要求返回True/False

#     sorted(可迭代对象, key=函数[默认None], reverse=False)
#       参数:
#         函数 只能有一个形参,形参用来绑定可迭代对象提供的数据
    
# 递归函数
#   函数直接或间接的调用自身

# 优点:可以把问题简单化
# 缺点: 递归深度会受限制(可能会出现不可预知的结果)

# 闭包 closure
#   闭包是指引用了此函数外部嵌套函数的变量的函数

#   三个条件
#     1. 有内嵌函数
#     2. 内嵌函数要访问外部嵌套函数的变量
#     3. 外部函数要返回内嵌函数

# 示例
#   用闭包来记录函数的调用次数
#   示例见:
#     call_times.py





# 装饰器  decorators(专业提高篇)
#   装饰器是一个函数,主要作用是用来包装另一个函数或类(后面才讲)

#   作用:
#     在不修改被装饰函数的源代码和不改变被装饰函数的调用方式的
#     基上为函数添加新的功能或改变原有功能
  
#   装饰器的语法:
#     def 装饰器函数名(fn):
#         语句块
#         return 函数对象
    
#     @装饰器函数名 <换行>
#     def 被装饰函数名(形参列表):
#         语句块
#
#   示例见:
#     mydeco1.py
#定义装饰器，并装饰　myfun
# 装饰器　的原理是替换被装饰函数的变量绑定关系
# def mydeco1(fn):
#     def fx():
#         print("+++++++++")
#         fn()
#         print("+++++++++")
#     return fx
# @mydeco1
# def myfun():
#     print("myfun被调用")
# # myfun=mydeco1(myfun)＃一般不写
# myfun()
# 带有参数的装饰器示例见:
#    mydeco3.py


# 函数的文档字符串
#   函数内第一次未赋值给任何变量的字符串是此函数的文档字符串

#   语法:
#     def 函数名(形参列表):
#         '函数的文档字符串'
#         语句块
#   示例:
#     def myfun(a, b, c):
#         '''这是一个自定义的函数
#         a 为第一个参数
#         ...
#         '''
#   说明:
#     文档字符串可以在交互模式下用help(函数名) 查看
#     函数的文档字符串绑定在函数的 __doc__属性中

# 函数的__doc__属性 
#    作用:
#      用于绑定的函数的文档字符串
#     如:
#       print(myfun.__doc__)

# 函数的 __name__ 属性
#   __name__ 属性用来记录函数名

#   说明:
#     以双下划线开头,以双下划线结尾的标识符通常代表python的
#     特殊变量
  
# 函数定义语句(def语句)的完整语法
#     [@装饰器名1]
#     [@装饰器名2]
#     [...]
#     def 函数名([位置形参], [*元组形参], [命名关键字形参],
#           [**字典形参 ]):
#         '''文档字符串'''
#         语句块

# 面试题:
# L = [1, 2, 3]
# def f(n=0, lst=[]):
#     lst.append(n)
#     print(lst)

# f(4, L)  # [1, 2, 3, 4] 
# f(5, L)  # [1, 2, 3, 4, 5]
# f(100)   # [100]
# f(200)   # [100, 200]  # 缺省参数里的[] 在def语句执行
#                            # 就已经创建,并一直被f函数绑定
#     f(300)   # [100, 200, 300]
#   解决方法:
# L = [1, 2, 3]
# def f(n=0, lst=None):
#     if lst is None:
#         lst = []  # 创建新的列表再用lst绑定
#     lst.append(n)
#     print(lst)

# f(4, L)  # [1, 2, 3, 4]
# f(5, L)  # [1, 2, 3, 4, 5]
# f(100)   # [100]
# f(200)   # [200]
# f(300)   # [300]

# 模块 Module
#   模块是一个包含有一系列数据,函数,类等组成的程序组
#   模块是一个文件,模块文件名通常以.py结尾

#   作用:
#     1. 让一些相关的函数,数据,类有逻辑的组织在一起,使逻辑结构
#     更加清晰
#     2. 模块中的数据,函数和类等可以提供给其它模块使用

#   模块的分类:
#     内置模块(builtins) 在解析器的内部可以直接使用
#     标准库模块,安装python时已安装且可以直接使用
#     第三方模块(通常为开源), 需要自己安装
#        安装命令:
#           pip3 install 模块名
#           或
#           pip install 模块名(通常用来安装python3的模块)
#     用户自己编写的模块
  

# 模块的导入语句   import
#   import 语句
#     import 模块名1 [as 模块新名1], 模块名2 [as 模块新名1],...
#   示例:
#     import math
#     import sys, time
#   作用:
#     当某模块整体导入到当前模块中
#   用法:
#     模块名.属性名
#     math.factorial(5)  # 返回120

# dir(obj) 函数,返回obj对象所有的属性的字符串列表
# help(obj) 函数,可以查看模块的文档字符串

# 练习:
#   学习使用数学模块math来计算:
#     1. 输入一个圆的半径,打印出这个圆的面积
#     2. 输入一个圆的面积,打印出这个圆的半径
#        面积 = 圆周率 * r ** 2



# from import 语句
#   语法:
#     from 模块名 import 模块属性名1 [as 属性新名1],
#             模块属性名2 [as 属性新名2], ....
#   作用:
#     将某模块内的一个或多个属性导入到当前模块的作用域
#   示例:
#     from math import factorial as fac
#     from math import sqrt, pi, sin, cos
#     print(sin(pi/2))  # 1.0


# from import * 语句
#   语法:
#     from 模块名 import *
#   作用:
#     将某模块的所有属性导入到当前模块作用域
#   示例:
#     from math import *
#     print(sin(pi / 2))  # 1.0
#     print(factorial(5))  # 120

# dir函数
#   dir([对象])
#     作用:
#       如果没有参数调用,则返回当前作用域内所有变量的列表
#       如果给定一个对象作为参数,则返回这个对象的所有变量的列表
#         对于一个模块,返回这个模块的全部属性(变量)
#         对于一个类对象,返回这个对象的所有变量,并递归基类对象
#           的所有变量
#         对于其它对象返回所有变量,类变量和基类变量
  

# 内建模块
#   math
#   time
#   sys

# math 模块
#   文档参见:
#     python_base_docs_html/数学模块math.html

# time 模块
#   文档参见:
#     python_base_docs_html/时间模块time.html
  


# sys 模块
#   运行时系统相关的信息 (runtime system)

#   文档参见:
#     python_base_docs_html/系统模块sys.html



# 练习:
#   1. 写一个程序,输入您的出生日期(年月日)
#      1) 算出你已经出生多少天?
#      2) 算出你出生那天是星期几?

#   2. 写一个程序,以电子时间的格式显示时间
#      HH:MM:SS 
#      如:
#        17:52:23
# import time
# def time_1():
#     while True:
#         a=time.localtime()
#         print(a[3:6],end=":",sep="\r")
#         time.sleep(1)

# time_1()
#   3. 编写一个闹种程序,启动时设定时间(小时,分钟)
#     到时间后打印一句"时间到!!!" 然后退出程序
# import time
# a=int(input("请输入时间："))
# b=int(input("请输入分钟："))
# c=a*3600+b*60
# print("这是第一句",a,"小时",b,"分钟","后打印")
# time.sleep(c)#让程序睡眠十秒钟，再再执行
# print("这是第二句")
#   4. 写程序打印杨辉三角(只打印6层)
#        1
#       1 1
#      1 2 1
#     1 3 3 1
#    1 4 6 4 1
#   1 5 10 10 5 1
#  3. 编写函数fun 基功能是计算下列多项式的和
#     Sn = 1 + 1/1! + 1/2! + 1/3! + .... + 1/n!
#     (建议用数学模块中的factorial)
#       求当n得20时 Sn的值
#     即:
#       print(fun(20))  # 2.718281828...
# import math
# def fun(n):
#     s=sum(map(lambda n:n/math.factorial(n),range(1,n+1)))
#     print(s)
# fun(20)
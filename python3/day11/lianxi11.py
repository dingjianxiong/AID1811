# 模拟银行业务需求，用装饰扩展新功能
# 银行　存钱、取钱

# def privileged(fn):
#     def fx(n,x):
#         print("权限验证中....")
#         fn(n,x)
#     return fx
# def send_message(fn):
#     #实现业务操作完成后发送短信的功能
#     def fy(n,x):
#         fn(n,x)
#         print("发送短信...",n)
#     return fy
# @privileged
# def savenmoney(name,x):
#     print(name,"存钱",x,"元")
# @send_message
# @privileged
# def widthdraw(name,x):
#     print(name,"取钱",x,"元")

# savenmoney("小王",200)
# savenmoney("小赵",400)
# widthdraw("小李",500)


# 文档字符串
# 文档字符串可以在交互模式下用help(函数名) 查看
#     函数的文档字符串绑定在函数的 __doc__属性中
# def ww(x,y,z):
#     '''这是文档字符串
#     x,1223
#     '''

# 练习:
#   学习使用数学模块math来计算:
#     1. 输入一个圆的半径,打印出这个圆的面积
#     2. 输入一个圆的面积,打印出这个圆的半径
#        面积 = 圆周率 * r ** 2

# 如何调用math数学模块：
#1 import math #调用数学模块
# pi=math.pi

#2 from math import sqrt, pi, sin, cos#调用数学模块，取出里面的值再使用

#3 from math import *  #直接用

# r=int(input("输入圆的半径："))
# s=round(pi*r**2,2)
# print("面积是",s)
# s1=int(input("输入圆的面积："))
# r1=ceil(sqrt(s1/pi))
# print("半径是",r1)

# dir函数
#   dir([对象])
# a=100
# b=200
# print(dir())
# import time
# print("这是第一句，十秒后打印")
# time.sleep(10)#让程序睡眠十秒钟，再再执行
# print("这是第二句")

# 练习:
#   1. 写一个程序,输入您的出生日期(年月日)
#      1) 算出你已经出生多少天?
#      2) 算出你出生那天是星期几?
# import time
# year=int(input("输入你的出生的年："))
# yue=int(input("输入你的出生的月："))
# ri=int(input("输入你的出生的日："))
# nyr=(year,yue,ri,0,0,0,0,0,0)
# #计算出生的秒数
# birth_second=time.mktime(nyr)
# #用现在的秒数－出生的秒数＝得到出生到现在的秒数
# life_second=time.time()-birth_second
# #把秒数换成天数
# life_day=life_second/60/60//12
# print("你已出生",life_day,"天")
# # week={
# #     0:"一",
# #     1:"一",
# #     2:"二",
# #     3:"三",
# #     4:"四",
# #     5:"五",
# #     6:"六",
# #     7:"日",
# # }
# #得到出生时的时间元组
# nyr=time.localtime(birth_second)
# print("你出生的那天是星期",nyr[6])


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
#         print("%2d:%2d:%02d" % a[3:6] ,end="\r")
#         time.sleep(1)
# time_1()
#   3. 编写一个闹种程序,启动时设定时间(小时,分钟)
#     到时间后打印一句"时间到!!!" 然后退出程序
# import time
# def run_alarm(hour,minute):
#     while True:
#         t=time.localtime()
#         print("%2d:%2d:%02d" % t[3:6] ,end="\r")
#         if t[3:5]==(hour,minute):
#             return
#         time.sleep(1)
# a=int(input("请输入时间："))
# b=int(input("请输入分钟："))
# run_alarm(a,b)
# print("时间到了")
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
# fun(2)
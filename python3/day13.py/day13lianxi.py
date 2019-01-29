
# _all_=["ee","myfac"]#只能调用当前列表内的属性，
# def ee(ww):
#     def rr():
#         print("这个数是")
#         ww()
#     return rr

# ##

# def myfac(n):
#     print("正在计算",n,"的阶乘")
# def mysum(n):
#     print("正在计算1+2+3...+%")
# name1="audi"
# name2="Tesla"
# print("当前模块被加载")
# print("day13lainxi._name_的值为：",__name__)
# def caizhi():
#     '''这是一猜数字的游戏
# 这个程序
# '''
#     import random as R
#     b=int(R.randint(1, 100))
#     while True:
#         a=int(input("输入一个数字"))
#         if a>b:
#             print("你猜大了")
#         elif a<b:
#             print("你猜小了")
#         elif a==b:
#             print("你猜对了")
#             break
# caizhi()
# @ee
# def ww():
#     print(b)
# ww()

# 2. 模拟斗地主游戏发牌,牌共54张
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

# day10 回顾
#   函数变量
#     函数名是变量,它在创建函数时绑定一个函数对象
#   调用运算符
#     函数名()  调用
#   函数可以作为实参传入到另一个函数中
#   函数可以作为返回值,从另一个函数中返回

#   def 语句的作用是创建函数,每次执行def语句都会创建一个函数,
#     同时用变量名绑定
#   函数嵌套定义
#       def f1():
#           def f2():
#               pass
#           return f2

# 作用域:
#   L局部
#   E外部嵌套函数作用域
#   G全局(模块级作用域)
#   B内建函数作用域

# global语句
#   声明一个或多个变量,这些变量是在全局作用域中
# nonlocal语句
#   声明一个或多个变量在外部嵌套函数的作用域

# lambda表达式
#   创建函数对象
#   fn = lambda x: x ** 2
#   def fn(x):
#       return x ** 2

#   def fx(fn):
#        fn(100)
#   fx(lambda y: y+1)
#   fx(fn)

    

# exec 和 eval 函数
#    eval(字符串, 表示全局作用域的字典, 表示局部作用域的字典)
#    exec(字符串, ......)




# day11 笔记
# 函数式编程 
#   函数式编程是指用一系列函数解决问题

# 函数式编程的好处:
#   用每个函数完成小的问题,一系列函数的任意组合可以完成大问题
#   函数仅接收输入并产生输出,不包含任何能影响输出的内部状态


# 函数的可重入性
#   当一个函数没有访问除局部变量以外的变量,则此函数为可重入函数

#   说明:
#     可重入函数输入一定,则输出结果必须一定
#   示例:
#     def myadd(x, y):  # 这是一个可重入函数
#         return x + y
#     print(myadd(100, 200))

#     # 不可重入函数示例:
#     s = 0
#     def myadd2(x, y):
#         return s + x + y
#     print(myadd2(100, 200))  # 300
#     s = 10000
#     print(myadd2(100, 200))  # 300????




# 高阶函数  High Order Function
#   什么是高阶函数:
#     满足下列两个条件之一的函数即为高阶函数
#       1. 函数接受一个或多个函数作为参数传入
#       2. 函数返回一个函数
#   示例:
#     fx(fn, x, y):
#        print(fn(x, y))
    
#     fx(lambda a, b: a + b, 100, 200)

#     fy():
#        return lambda a, b: a + b
#     fn = fy()

# python 内建的高阶函数
#    map()处理传入的参数，得到想要的结果    filter(删选、过滤)    sorted（排序）

# map 函数
#   map(func, iterable1, iterable2, ....)
#   形参列表可能定义如下:
#      def map(func, *args)
#   作用:
#     返回一个可迭代对象,此可迭代对象用func函数对可迭代对象
#     iterable 中的每一个元素作为参数传入func计算,得到计算后
#     迭代对象生成结束
#   示例见:
#     map.py
#     map2.py
    
# 练习:
#   1. 求 1**2 + 2**2 + 3**2 + ..... + 9**2的和
#方法１
# def pow2(x):
#     return x**2
# t=0
# for x in map(pow2,range(1,10)):
#     t+=x
# print(t)
#方法二：

# s=sum(map(lambda x:x**2,range(1,10)))
# print(s)
#   2. 求 1**3 + 2**3 + 3**3 + ..... + 9**3的和
# s=sum(map(lambda x:x**3,range(1,10)))
# print(s)
#   3. 求 1**9 + 2**8 + 3**7 + ..... + 9**1的和
# s=sum(map(pow,range(9,0,-1),range(1,10)))
# print(s)

# filter函数
#   格式:
#     filter(func, iterable)
#   作用:
#     筛选可迭代对象iteralbe 中的数据,返回一个可迭代对象,此
#     可迭代对象只返回iterable提供的数据中满足条件的数据
#   参数:
#     func 含有一个形参的数据处理函数,此函数传入的值为iterable
#     中提供的数据,返回True,则保留此数据,返回False则将此数据
#     丢弃
#     iterable为可迭代对象,此可迭代对象提供的数据将传入func
#     判断后决定是否提供给调用者
#   示例见:
#     filter.py
# def isodd(x):
#     return x%2==1
# for x in filter(lambda x: x%2==1,range(1,10)):
#     print(x)    
# 练习:
#   1. 将 1 ~ 20 的全部数字用filter 函数,将偶数部分过滤出来.
#   并打印

#   答案:
#     def iseven(x):
#         return x % 2 == 0
#     for x in filter(iseven, range(1, 21)):
#         print(x)
    
#     for x in filter(lambda x:x%2==0, range(1, 21)):
#         print(x)

# 思考:
#   1. 能否用filter把1~100之间的所有素数放在一个列表内?
#方法一
# def isprime(x):
#     if x<2:
#         return False
#     for i in range(2,x):
#         if x%i==0:
#             return False
#     return True
# l= list(filter(isprime, range(1, 100)))
# print(l)  
#方法二
# def isprime(x):
#     if x<2:
#         return False
#     for i in range(2,x):
#         if x%i==0:
#             return False
#     return Tru
# l=[x for x in filter(isprime,range(100))]
# print(l)
#     第一步,定义一个函数
#         def isprime(x):
#             ....
#             return True/False

#     第二步:
#        L = list(filter(isprime, range(1, 100)))



# sorted 函数
#   作用:
#     将原可迭代对象的数据进行排序,生成排序后的列表
#   格式:
#     sorted(iterable, key=None, reverse=False)
#   参数说明:
#     iterable   可迭代对象
#     key 函数,用来提供一个值,这个值将作为排序的依据
#     reverse 标志用来设置是否降序排序(默认为升序排序)
#   示例:
#     L = [5, -2, -4, 0, 3, 1]
#     L2 = sorted(L)  # L2 = [-4, -2, 0, 1, 3, 5]
#     L3 = sorted(L, reverse=True)  # L3 = [5, 3, 1, 0, -2, -4]
#     L4 = sorted(L, key=abs)  # L4 = [0, 1, -2, 3, -4, 5]
#     L5 = sorted(L, key=abs, reverse=True)     # L5 = [5, -4, 3, -2, 1, 0]

# 示例１：
# l=[x for x in sorted([3,-5,-1,0,6],key=abs)]
# print(l)
# 示例２
#     def myabs(x):
#         if x < 0:
#            return -x
#         return x
#     L6 = sorted(L, key=myabs)
#     print("L6=", L)
# 示例３
# names = ['Tom', 'Jerry', 'Spike', 'Tyke']
# L7 = sorted(names)
# L8 = sorted(names, key=len)   # 按名字的长短排序,短的在前
# print(L8)


# 练习 :
#   names = ['Tom', 'Jerry', 'Spike', 'Tyke']
#   排序的依据为字符串的反序
#            'moT'   'yrreJ'  'ekipS'  'ekyT'
#   排序后的结果为:
#          ['Spike', 'Tyke', 'Tom', 'Jerry']

#   答案:
#     def fk(s):
#         return s[::-1]
#     L = sorted(names, key=fk)

# 练习：１
# l=[(1,5),(3,9),(4,1),(3,6),(5,3)]
# 1、将列表内的五个元组按，第二个数据从小到大顺序排序：结果如下：

# l=[(4,1),(5,3),(1,5),(3,6),(3,9)]
# ww=sorted(l[1],key=l[1])
# def ee(t):
#     return t[1]
# l2=sorted(l,key=ee)
# print(l2)
# print(l[])
# ２、将列表内五个元组按第二个数从大到小排序，打印排序后的结果
# def ee(t):
#     return t[1]
# l2=sorted(l,key=ee,reverse=True)
# print(l2)
# ３、假设元组中的数据是数学直角坐标系的坐标，则按他们距离原点的距离进行排序
# （提示：距离等同于　distance=sqrt(x**2+y**2)）
#                                                                  ssss
# c=sorted(l,key=lambda x y:x**2+y**2)                               
# print(c)

# 递归函数 recursion
#   函数直接或间接的调用自身

# def story():
#     print("从前有座山")
#     # print("山上有座庙")
#     print("庙里有个老和尚讲故事:")
#     story()
# story()
# print("故事讲完了")

# 递归示意:
#   函数直接调用自身
#     def f():
#         ...
#         f()
#         ...
#     f()
#   函数间接调用自身
    # def fa():
    #     fb()

    # def fb():
    #     fa()
    # fa()


# 说明:
#   递归一定要控制递归的层数,当符合某一条件时要终止递归调用
#   几乎所有的递归都能用while循环来代替
# 递推分为两个阶段：
# 　递推阶段：
# 　　　　从原问题出发，按递归公式，从未知到已知，最终返回
# 　回归阶段：
# 　　　　按递归终止条件，逆向代入递归公式，回归到原问题求解
# 示例见:
#   recursion1.py
# def fx(n):
#     print("递归进入第",n,"层")
#     if n==3:
#         return
#     fx(n+1)
#     print("递归退出第",n,"层")
# fx(1)
# print("程序退出")
# def fx1(n):
#     if n==0:
#         return 1
#     s=n*fx1(n-1)   #求ｎ的阶层
#     return s
    
# print(fx1(5))

# 递归求阶乘示例
#   5! = 5 * 4 * 3 * 2 * 1  # 5! = 5 * 4!
#   阶乘的定义
#      n! 等于:
#         值为1             if n == 0
#         值为 n * (n-1)!   if n > 0
#   见:
#     recursion_myfac.py
# 练习:
#   写一个递归求和的函数 recursion_sum(n)
#   此函数返回 1 + 2 + 3 + 4 + .... + n的和

#   def recursion_sum(n):
#       ...  # 此外自己实现
#   print(recursion_sum(100))  # 5050
# def recursion_sum(n):
#     if n==0:
#         return 1
#     s=n+recursion_sum(n-1)
#     return s
# print(recursion_sum(100))
# 思考:
#   已知有五位朋友在一起:
#     第五位朋友比第四位朋友大2岁
#     第四位朋友比第三位朋友大2岁
#     第三位朋友比第二位朋友大2岁
#     第二位朋友比第一位朋友大2岁
#     第一位朋友说他10岁
#     试写程序求出第3位和第5位朋友多少岁
# 方法一
# def get_age(n):
#     if n==1:
#         return 10
#     s=n+get_age(n-2)
#     return s
# print(get_age(5))
#方法二
# def get_age(n):
#     if n==1:
#         return 10
#     else:
#         return get_age(n-1)+2
# print("第3个人",get_age(3),"岁")
# 递归的优缺点:
#   优点:
#     递归可以把问题简单化,让思路更加清晰,代码更简洁
#   缺点:
#     递归因系统环境影响大,当递归深度太大时,可能会出现不可
#     预知的结果

    



# 闭包 closure
#   什么是闭包
#     闭包是指引用了此函数外部嵌套函数的变量的函数

#   闭包必须满足以下三个条件:
#     1. 必须有一个内嵌函数
#     2. 内嵌函数必须引用外部函数中的变量
#     3. 外部函数返回值必须是内嵌函数
#   说明:
#     由于闭包会使得函数中变量都被保存在内存中,内存消耗很多,所
#     以不能滥用闭包
#   示例见:
#     closure.py
# def aa(m):
#     money=m
#     def bb(obj,m):
#         nonlocal money
#         if money>m:
#             money -=m
#             print("买",obj,"花了",m,"剩余",money)
#         else:
#             print("失败")
#     return bb
# cb=aa(1000)
# cb=("sd",200)

# 闭包的应用案例见:
#   closure2.py  
# 创建一系列的函数：
# def aa(y):
#     def bb(x):
#         return x**y
#     return bb
# pow2=aa(2)

# print(pow2(3))
# del pow2



# 练习:
#   1. 写程序算出 1~ 20 的阶乘的和
#     1! + 2! + 3! + 4! + ..... + 20!
# def fx1(n):
#     if n==0:
#         return 1
#     s=n*fx1(n-1)   #求ｎ的阶层
#     return s
# s=sum(map(fx1,range(1,21)))
# print(s)
#    2. 已知有列表:
#     L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
#     1) 写一个函数 print_list(lst) 打印出所有的数字
#        print_list(L)  # 打印 3 5 8 10 13 14  ...
#        注: 不要求打印在一行内
l= [[3, 5, 8], 10, [[13, 14], 15, 18], 20]

# def print_list(list):
#     sum=0
#     for x in list:
#         if type(x) is int:
#             print(x,sum,end=" ")
#         else:
#             print_list(x)
# print_list(l)

#     2) 写一个函数 sum_list(lst) 返回这个列表中所有数字的和
#         print(sum_list(lst))  # 106
#     提示:
#       type(x) 可以返回一个变量的类型,可以用is运算符来比较
#       类型
#         如:
#            type(20) is int  # True
#            type([1, 2, 3]) is list  # True
# def sum_list(lst):
#     sum=0
#     for x in lst:
#         if type(x) is int:
#             sum+=x
#         elif type(x) is list:
#             sum+=sum(x)
# sum_list(l)
#   3. 改写之前的学生信息管理程序
#     要求添加四个功能:
    #   | 5) 按学生成绩高~低显示学生信息 |
    #   | 6) 按学生成绩低~高显示学生信息 |
    #   | 7) 按学生年龄高~低显示学生信息 |
    #   | 8) 按学生年龄低~高显示学生信息 |
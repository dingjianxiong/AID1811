# day08回顾
#   容器:
#     集合 set
#     固定集合 frozenset
#   小结:
#     只能存不可变对象,不能重复,无序
#   运算:
#     &  |  -  ^  <   >  == !=  <= >=
#     in / not in
#     &=  |= -=  ^=
#   集合的方法:
#     S.add(x)
#     S.remove(x)
#     S.discard(x)
#     S.clear()
#     S.copy()
#     S.update(S2)

# 函数 function
#   def 语句
#   return 语句

# def 函数名([形参列表]):
#     语句块

# 函数调用:
#     函数名([实参列表])

# return 语句:
#     return  # 等同于return None
#     return 1 + 3 * 2

# day09笔记:
# python 函数的参数传递

# 函数的参数传递方式:
#   位置传参
#       序列传参
#   关键字传参
#       字典关键字传参

# 位置传参   argument
#    实际参数(实参)的对应关系与形式参数(形参)对应关系是按位置来
#    依次对应的
#   示意:
#     def mymin(a, b, c):
#         pass
    
#     mymin(    1, 2, 3)
#   说明:
#     实参的个数必须与形参的个数相同
#   示例见:
#     positional_give_args.py


# 序列传参
#   序列传参是指在函数调用过程中,用 *将序列拆解后按位置进行
#   传递的传参方式

#   示例见:
#     sequence_give_args.py
#   说明:
#     序列传参时,序列拆解的位置将与形参一一对应
# def myfun(a,b,c):
#     print("a=",a)
#     print("b=",b)
#     print("c=",c)
# l=[1,2,3]
# t=(100,200,300)
# s="abc"
# myfun(l,t,s)  #等同于 myfun(l[0],l[1],l[2])
# myfun(*l)
# myfun(*t)
# myfun(*s)
# 关键字传参:
#   关键字传参是指传参时,按着形参的名字给形参赋值
#   说明:
#     实参和形参接形参名进行匹配,可以不按位置进行匹配
#   示例见:
#     keywords_give_args.py
# def ww(ser,wee):
#     return wee**2
#     return ser**2
# print(ww(2,wee=3))

# 字典关键字传参
#   是指实参为字典,将字典用 ** 拆解后进行关键字传参的传参方式

#   示例见:
#     dict_keywords_give_args.py
#   说明:
#     字典的键名和形参名必须一致
#     字典的键名必须为附合标识命名规则的字符串
#     字典的键要在形参中存在

# def wwe(rr,tt):
#     print("rr是",rr)
#     print("tt是",tt)
# aa={"rr":"二","tt":"三"}
# wwe(**aa)# wwe(tt=a[2],rr=a[3])

# 函数综合传参
#   1. 函数的传参方式在能确定形参能唯一匹配到相应实参的情况下
#   可以任意组合
#   2. 函数的位置传参要先于关键字传参(关键字传参放最后)
#   示例:
    # def myfun1(a, b, c):
    #     pass
    # myfun1(100, *[200, 300])
    # myfun1(*[100, 200], 300)
    # myfun1(*[100], 200, *(300,))
    # myfun1(10, c=30, b=20)
    # myfun1(**{'c':33, 'b':22}, a=11)
    # myfun1(c=30, **{'a':10}, b=20)
    # myfun1(100, 200, c=300)
    # # myfun1(b=200, a=100, 300)  # 错误
    # myfun1(a=200, 100, c=300)　　# 错误
# def f1(x,y):
#     print(x+y)
# a=100
# b=200
# f1(a,b)
# 实参给形参进行赋值传递，并不会赋值新的对象
# 即ｘ和ａ同时引用１００，ｙ和ｂ同时引用２００
# a=[1,2,3]
# b=4
# def f2(x,y):
#     x.append(y)
# f2(a,b)
# print(a)
# print(b)
# a=[1,2,3]
# b=200
# def f2(x,y):
#     x=x+[y]#此处改变的是变量，不是对象
#     return x
# f2(a,b)
# print(a)
# print(b)

# ---------- 以下讲函数的定义部分(函数的形参)-------
# 函数的缺省参数
#   语法:
#     def 函数名(形参名1=默认实参1, 形参名2=默认实参2,...):
#         语句块
#   示例见:
#     default_args.py
#   说明:
#     1. 缺省参数必须自右至左依次存在,如果一个参数有缺省参数,则
#       其右侧的所有参数都必须有缺省参数
#     2. 缺省参数可以有0个,1个或多个,甚至全部都有缺省参数
#   示例:
#     def fn(a, b=10, c):  # <<<---这是错的
#         pass
#     def fn(a=0, b=10, c=20):
#         pass
# def info(name,age=1,address='不详'):
#     print(name,'今年',age,"岁","家住地址：",address)
# info("丁建雄",20,"重庆万州")
# info("丁建雄",20)
# info("丁建雄")

# 练习:
#   写一个函数myadd, 此函数可以计算两个数,三个数,及四个数的和
#     def myadd(.....):
#        ....

#     print(myadd(10, 20))  # 30
#     print(myadd(100, 200, 300))  # 600
#     print(myadd(1, 2, 3, 4))  # 10
# def myadd(a,b=0,c=0,d=0):
#     return (a+b+c+d)
# print(myadd(2,3,4))
# print(myadd(10, 20))  # 30
# print(myadd(100, 200, 300))  # 600
# print(myadd(1, 2, 3, 4))  # 10
# 函数的形参的定义方式:
#   位置形参
#   星号元组形参
#   命名关键字形参
#   双星号字典形参

# 位置形参
#   语法:
#     def 函数名(形参名1, 形参名2, ...):
#         语句块

# 星号元组形参
#   语法:
#     def 函数名(*元组形参名):
#         语句块
#   作用:
#     收集多余的位置传参
#   说明:
#     在一个函数名的形参列表内只能有一个星号元组形参
#     元组形参名一般命名为 'args'
#   示例见:
#     star_tuple_args.py
# def func(*args):
#     print("实参个数是：",len(args))
#     print("args=",args)
# func()
# func(1,2,3,4)
# func(1,2,3,4,'aaa','bbb')
# func(*"abcdefg")

# 练习:
#   写一个函数,mymax, 此函数可以传入任意个实参,返回实参中的
#   最大数
#   def mymax(...):
#       ....

#   print(mymax(4, 6, 9, 3))  # 9
#   print(mymax("ABC", "abc", '123'))  # abc
#   print(mymax(1,2,3,4,5,6,7,8,9))  # 9
# def mysum(*args):
#     return (sum(args))
# print(mysum(4, 6, 9, 3))  # 9
# # print(mysum("ABC", "abc", '123'))  # abc
# print(mysum(1,2,3,4,5,6,7,8,9))  # 9
# 练习:
#   写一个函数mysum 可以传入任意个实参的数字,返回所有实参的和
#     def mysum(*args):
#        ....
#     print(mysum())  # 0
#     print(mysum(1, 2, 3, 4))  # 10
#     要求: 不允许调用内建函数sum


# 命名关键字形参
#   语法:
#     def 函数名(*, 命名关键字形参1, 命名关键字形参2, ...):
#         语句块
#     或
#     def 函数名(*args, 命名关键字形参1, 命名关键字形参2, ...):
#         语句块
#   作用:
#     强制所有的实参都必须用关键字传参或字典关键字传参
#   示例见:
#     named_keyword_args.py
#     named_keyword_args2.py
# def func1(a,b,*,c,d):
#     print(a,b,c,d)
# # print(func1(1,2,3,4))#  错误
# print(func1(11,22,c=33,d=44))
# print(func1(a=11,b=22,c=33,d=44))
# 星号元组形参
# def func1(a,b,*args,c,d):
#     print(a,b,*args,c,d)
# print(func1(11,22,45,543,3,3,c=33,d=44))

# 双星号字典形参
#   语法:
#     def 函数名(**字典形参名):
#         语句块
#   作用:
#     收集多余的关键字传参
#   说明:
#     字典形参名一般命名为'kwargs'
#     一个函数内字典形参最多只能有一个
#   示例见:
#     kwargs.py
# def func(**kwargs):
#     print("关键字个数是：",len(kwargs))
#     print("kwargs=",kwargs)
# func(name="ding",age=20,address="wan")
# func(a=1,b=2,c=3,d="abc",e=[1,2,3])



# 练习:
#   已知内建函数max帮助方档为:
#     max(iterable)
#     max(arg1, arg2, *args)
#   仿造max, 写一个mymax函数,功能与max完全相同
#   (要求不允许调用max函数)
#     print(mymax([6, 8, 3, 5]))  # 8
#     print(mymax(100, 200))  # 200
#     print(mymax(1, 3, 9, 5, 7))  # 9
# def mymax(*args):                             #ssssss
#     lis=[]
#     if len(args)==1:
#         lis=args[0]
#         zuida=lis[0]
#         for x in lis:
#             if x>zuida:
#                 zuida=x
#         return zuida
#     elif len(args)>1:
#         zuida=lis[0]
#         for x in lis:
#             if x>zuida:
#                 zuida=x
#         return zuida

# print(mymax([6, 8, 3, 5]))  # 8
# print(mymax(100,200))  # 200
# print(mymax(1, 3, 9, 5, 7))  # 9

# 说明:
#   位置形参,缺省参数,星号元组形参,双星号字典形参可以混合使用

# 函数参数自左至右的顺序为:
#   位置形参
#   星号元组形参
#   命名关键字形参
#   双星号字典形参

#   示例:
#     def fn(a, b, *args, c, d, **kwargs):
#         pass
#     fn(100, 200, 300, 400, c='C', d='D', e='E')

# 可以接收任意的位置传参和关键字传参的函数定义
#   def fx(*args, **kwargs):
#        pass

# 思考题:
#   查看 >>> help(print)  猜想print 函数的参数列表是如何
#   定义的,能否自己实现一个myprint函数,代替print
#       (内都可以调用print来进行输出)
#   myprint / print(1,2,3,4)
#   myprint / print(1,2,3,4, sep="#")
#   myprint / print(1, 2, 3, 4, 5, end=' ')



# 全局变量 global 和局部变量 local
# 局部变量 local variable
#   定义在函数内部的变量称为局部变量(函数的形参也是局部变量)
#   局部变量只能在函数内部使用
#   局部变量在函数调用时才能够被创建,在函数调用之后会自动销毁

# 全局变量 global variable
#   定义在函数外部,模块内部的变量称为全局变量
#   全局变量,所有的函数都可以直接访问(取值,但函数内不能将其
#     直接赋值)
# 示例见:
#    global_local.py

# 说明:
#   1. 在函数内部赋值语句只会创建函数内部的局部变量,不会对全局
#      变量造成影响
#   2. 局部变量只能在其被声明的函数内部访问,而全局变量可以在整个
#      模块内访问(取值)

# globals 和  locals 函数
#   globals()  返回当前全局作用域内变量的字典
#   locals()  返回当前部作用域内变量的字典
#   示例见:
#     globals_and_locals.py



# 练习:
#   1. 素数练习:
#     1) 写一个函数isprime(x)  判断x是否为素数,如果是素数
#        返回True,否则返回False
#        如:
#         print(isprime(3))  # True
#         print(isprime(4))  # False
def isprime(x):
    if x<=2:
        return True
    elif x>2:
        for w in range(2,x):
            if x%w==0:
                return False
        return True
# a=int(input("输入整数："))
# print(isprime(a))
#     2) 写一个函数prime_m2n(m, n)  返回从m开始,到n结束
#        范围内的素数,返回这些素数的列表,并打印(注:不包含n)
#        如:
        # L = prime_m2n(10, 20)
        # print(L)  # [11, 13, 17, 19]
def prime_m2w(m,n):
    ls=[]
    sm=0
    for y in range(m,n+1):
        # print(a,end="")
        q=isprime(y)
        t=True
        if q==t:
            ls+=[y]
    for x in ls:
        sm+=x
    return sm
    # return ls
# L = prime_m2n(10,20)
# print()
# print(L)  # [11, 13, 17, 19]
    # lt=[]
    # if m<=2:
    #     for a in range(m,n):
    #         lt=[a]
    #     return (l)
    # elif m>2:
    #     for w in range(m,n):
    #         if n%w==0 or m%:
    #             return False
    #         else:
    #             lt=[w]
    #             return lt

#     3) 写一个函数 primes(n) 返回指定范围内的全部素数(不包
#        含n)的列表
#        如:
#        L = primes(10)
#        print(L)  # [2, 3, 5, 7]
#        1> 计算100以内的全部素数的和
#        2> 计算100~200之间全部素数的和
def prime_m2n(w,*args):
    ls=[]
    for y in range(1,w+1):
        # print(a,end="")
        q=isprime(y)
        t=True
        if q==t:
            ls+=[y]
    return ls
def primes(n):
    sum=0
    l = prime_m2n(n)
    for x in l:
        sum+=x
    return sum

print(primes(100))
print(prime_m2w(100,200))
# print(primes(100,200))
#   2.  写一个myrange函数,参数可以传1~3个,实际含义与range函数相同
#      此函数返回符合range() 函数规则的列表:
#        如:
#         L = myrange(4)
#         print(L)  # [0, 1, 2, 3]
#         L = myrange(4, 6)
#         print(L)  # [4, 5]
#         L = myrange(1, 10, 3)
#         print(L)  # [1, 4, 7]
#         L = myrange(10, 0, -3)
#         print(L)  # [10, 7, 4, 1]
#   3. 思考下面程序的结果是什么?为什么?
#     def f1():
#         print("f1")
#     def f2():
#         print("f2")
#     f3 = f1
#     f3()  # 请问打印什么?为什么
#     f1, f2 = f2, f1
#     f1()  # ???
#     f2()  # 打印什么?为什么?
  
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

# def even(start, stop):
#     while start<stop:
#         if start %2==0:
#             yield start
#         start +=1
# for x in even(1,10):
#     print(x,end=' ')  # [2, 4, 6, 8]
# L = [x**2 for x in even(10, 20)]
# print(L)  # [100, 144, ...]


#     L = [2, 3, 5, 7]
#     1) 写一个生成器函数,让此函数能够动态提供数据, 提供的数据
#       为原列表的数字的平方+1
#     2) 写一个生成器表达式,让此表达式能够动态提供数据,提供的数
#       据依旧为原列表的数字的平方+1
#     3) 写一个列表,此列表内的数据为原列表的数字的平方+1

# l=[2,3,5,7]
# def ww():
#     for x in l:
#         a=x**2+1
#         yield a
# it = list(ww())
# print(it)

# b=[x**2+1 for x in l]
# # for x in b:
# #     print(x,end=" ")

# print(b)

# l1=[]
# l1+=(x**2+1 for x in l)
# print(l1)

# 2. 试写一个生成器函数 myfilter,要求此函数与系统内建的
#     filter函数功能相同
#     如:
#     def myfilter(fn, iterable):
#         ..... # 此处自己实现
    
#     for x in myfilter(lambda y:y%2==1, range(10)):
#         print(x)  # 1 3 5 7 9
#方法一：
# def myfilter(fn, iterable):
#     for x in iterable:
#         if x%2==1:
#             yield x
# for x in myfilter(lambda y:y%2==1, range(10)):
#     print(x,end=" ")  # 1 3 5 7 

# 方法二：
# def myfilter(fn,iterable):
#     it=iter(iterable)
#     while True:
#         try:
#            x=next(it)
#            if fn(x):
#                yield x
#         except StopIteration:
#             return
# for x in myfilter(lambda y:y%2==1, range(10)):
#     print(x,end=" ")  # 1 3 5 7 9


# 1. 实现一个python2下的xrange([start], stop, [step])
#     生成器函数,此生成函数按range规则来生成一系列整数
#     要求:
#       myxrange功能与range功能完全相同
#       不允许调用range函数和列表
#   用自己写的myxrange结果生成器表达式求 1~10以内所有奇数的
#     平方和
#   如:
#     def myxrange(start, stop=None, step=None):
#          ....以下自己实现
#     求:1 ** 2 + 3 ** 2 + 5 **2 + ...  9 ** 2
# def myrange(start,stop=None,step=None):
#         if stop==None and step==None:
#             a=0
#             while True:
#                 a+=1
#                 yield a
#                 if a==start-1:
#                     return
#         elif step==None:
#             while True:
#                 yield start
#                 start+=1
#                 if start==stop:
#                     return
#         elif step>0:
#             while True:
#                 yield start
#                 start+=step
#                 if start==stop:
#                     return
#         elif step<0:
#             while True:
#                 stop+=step
#                 if stop<1:
#                     return
#                 yield stop
# sum=0
# for x in myrange(1,11,2):
#     sum+=x**2
# print(sum)

# 2. 写一个程序,从键盘输入一段字符串,用变量s绑定
#      1) 将此字符串转为字节串用变量b绑定,并打印出此字节串b
#      2) 打印字符串s的长度和字节串b的长度
#      3) 将字节串b再转换为字符串用变量s2 绑定,然后判断
#        s2 和 s是否相同
# s=input("请输入一段字符串：")
# b= s.encode(encoding='utf-8')
# print(b)
# print(len(s),len(b))
# s2=b.decode(encoding='utf-8')
# if s2==b:
#     print("s=s2")
# else:
#     print("s!=s2")

# 3. 分解质因数,输入一个正整数,分解质因数
#      如
#        输入: 90
#      打印
#        90 = 2*3*3*5
#     注: 质因数是指最小能被原数整数的素数(不包括1)
def get_all_yinshu(x):
    l=[]
    while x>1:
        #每循环一次找一个质因数
        for i in range(2,x+1):
            if x % i==0:
                l.append(i)
                x=int(x//i)
                break
    # return[2,3,3,5]
n=int(input("请输入："))
l=get_all_yinshu(n)
print(n,"=","*".join((str(x) for x in l)))


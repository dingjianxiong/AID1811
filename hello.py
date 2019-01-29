
# print("hello world")
# print("你好")

# import random
# # print random.randint(1,100)

# a="w q q w e q w w "
# b=213.12312
# print(a.replace(" ",""))
# print(a.center(15))
# print(a.count("w"))
# print("%-+10.2f" % b)
# 输入三行文字,让这三行文字依次以20个字符的宽度右对齐输出
#   如:
#     请输入第1行: hello world
#     请输入第2行: abcd
#     请输入第3行: a
# a="hello world"
# b="abcd"
# c="a"
# print("%20s" % a)
# print("%20s" % b)
# print("%20s" % c)
# l=[2,1,3,1,2,3]
# l.count(2)
# print(l.count(4))


# map(函数,可迭代对象1, 可迭代对象2, ....)
#       参数
#         函数 ,形参个数要和可迭代对象的个数相同
    
# filter(过滤函数, 可迭代对象)
#       参数
#          过滤函数只能有一个形参,此函数要求返回True/False

# sorted(可迭代对象, key=函数[默认None], reverse=False)
#       参数:
#         函数 只能有一个形参,形参用来绑定可迭代对象提供的数据

# a=max(map(lambda x:x*2,range(1,10)))
# a=list(filter(lambda x :x%2==1,range(1,10)))
# l = [5, -2, -4, 0, 3, 1]
# a=list(sorted(l,key=lambda ,reverse=False))
# print(a)

# 以下列表的中的数据进行排序
L = [(1, 5), (3, 9), (4, 1), (3, 6), (5, 3)]
#   1. 将列表内的五个元组按,第二个数据的从小到大的顺序进行排序
#     结果如下:
#     L = [(4, 1), (5, 3), (1, 5), (3, 6), (3, 9) ]

#   2. 将列表内的五个元组按第二个数的从大到小顺序进行排序,打印
#      排序之后的结果

#   3. 假设元组中的数据是数学直角坐标系的坐标,则按他们距离原点
#      的距离进行排序
#      (提示: 距离等同于 distance = sqrt(x**2 + y**2))
# def ss(l):
#     ww=l[0]**2+l[1]**2
#     return ww
# a=sorted(L,key=lambda t:t[0]**2+t[1]**2)
# print(a)
# L4 = sorted(L, key=lambda t: (t[0]**2 + t[1]**2))
# print("L4=", L4)
#  1. 试写一个递归函数 mysum(n), 此函数用递归方式求
#     1 + 2 + 3 + 4 + .... + n 的和
#     def mysum(n):
#         .... # 此处自己实现
#     print(mysum(100))  # 5050
# def mysum(n):
#     for x in range(1,101):
#         x+=x
#     return x

# print(mysum(100))  # 5050
def mysum(n):
    if n == 1:
        return 1
    return n + mysum(n - 1)

print(mysum(10))  # 5050
# enumerate.py

# 练习:
#   写一个成生器函数myenumerate,要求此函数的功能与内建的
#       enumerate 函数功能完全相同
#     如:
#         def myenumerate(iterable, start=0):
#              .... 以下自己实现
#     测试:
#         d = dict(myenumerate("ABCDE", 1))
#         print(d)  # {1:'A', 2:'B', 3:'C', ...}

# def myenumerate(iterable, start=0):
#     it1=iter(iterable)#得到iterable的迭代器
#     while True:
#         try:
#             x1=next(it1)
#             yield (start,x1)
#             start+=1
#         except StopIteration:
#             return
# d = dict(myenumerate("ABCDE"))
# print(d)  # {1:'A', 2:'B', 3:'C', ...}
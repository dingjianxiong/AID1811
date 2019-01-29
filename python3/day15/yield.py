#此示例示意生成器函数的创建和调用
# def myyield():
#     print("即将生成2")
#     yield 2
#     print("生成器生成结束")
# gen=myyield()#调用生成器函数生成一个生成器
# print(gen)#generator

# it=iter(gen)#生成器中可获取的一个迭代器
# print(next(it))#向生成器要数据，此时生成器函数才会执行一步
# print(next(it))#触发StopIteration异常

# def myyield():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#     print("生成器生成结束")

# it=iter(myyield())#生成器中可获取的一个迭代器
# print(next(it))#向生成器要数据，此时生成器函数才会执行一步
# print(next(it))#2
# print(next(it))#3
# print(next(it))#4
# print(next(it))#5
# print(next(it))#遇到return触发StopIteration异常

# def myyield():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#     print("生成器生成结束")

# it=myyield()#生成器中可获取的一个迭代器
# for x in it:
#     print(x)

def myyield():
    print("即将生成1")
    yield 1
    print("即将生成2")
    yield 2
    print("即将生成3")
    yield 3
    print("即将生成4")
    yield 4
    print("即将生成5")
    yield 5
    print("生成器生成结束")

it=iter(myyield())#生成器中可获取的一个迭代器
print(next(it))#向生成器要数据，此时生成器函数才会执行一步
print(next(it))#2
print(next(it))#3
print(next(it))#4
print(next(it))#5
print(next(it))#遇到return触发StopIteration异常
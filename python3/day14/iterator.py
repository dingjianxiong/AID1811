# iterator.py
#此示例示意用迭代器遍历一个列表：
l=[2,3,5,7]
#1.先给l提供一个迭代器
it=iter(l)
#循环从迭代器获取数据，直到接收到StopIteration异常为止
while True:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        break
#.....以上多条语句可以用如下的for循环来实现
for x in l:
    print(x)
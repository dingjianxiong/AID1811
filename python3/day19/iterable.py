class mynumber:
    '''自定义一个数字类，用于表示自定义的数字信息'''
    def __init__(self,iterable=()):
        '''初始化方法'''
        self.data=[x for x in iterable]
    def __repr__(self):#覆盖原来父类的方法
        return "mynumber(%d)" %self.data
    def __iter__(self):
        '''有此方法的对象可以用iter(obj)来获取迭代器'''
        return mylistiterator(self.data)
class mylistiterator:
    '''此类用来创建一个迭代器器，此迭代器可以用来访问mylist类型的对象'''
    def __init__(self,lst):
        self.data2=lst
        self.index=0#用来记录此爹地啊器当前的访问的地点
    def __next__(self):
        if self.index>=len(self.data2):
            raise StopIteration
        r=self.data2[self.index]
        self.index+=1
        return r

myl=mynumber([1,-2,3,-4,5])
# for x in myl:
#     print(x)
it=iter(myl)
while True:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        break
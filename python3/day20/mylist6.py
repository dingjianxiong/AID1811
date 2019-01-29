# 索引 和切片运算符
#   []

# 重载方法
#   方法名                   运算符和表达式  说明
#  __getitem__(self, i)     v = self[i]  索引/切片取值
#  __setitem__(self, i, v)  self[i] = v  索引/切片赋值
#  __delitem__(self, i)     del self[i]  del 语句删除
#                                        索引或切片
#   作用:
#     让自定义的类创建的对象支持索引或切片操作

class MyList:
    def __init__(self,iterable=()):
        self.date=[x for x in iterable]
    def __repr__(self):
        return "MyList(%s)" % self.date
    def __getitem__(self, i):
        return self.date[i]
    def __setitem__(self,i,v):
        self.date[i]=v
        return v
    def __delitem__(self, i):
        del self.date[i]
L1 = MyList([1, -2, 3,-4,-5])
v=L1[2]
print(v)

a=L1[0::2]
print(a)

L1[1]=+2
print(L1)
del L1[2]
print(L1)

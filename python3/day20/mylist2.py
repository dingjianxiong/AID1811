#复合赋值运算符发重载
# 如：i<z
class MyList:
    def __init__(self,iterable=()):
        self.date=[x for x in iterable]
    def __repr__(self):
        return "MyList(%s)" % self.date
    def __add__(self,other):
        a=self.date+other.date
        return MyList(a)
    def __iadd__(self,other):
        '''此方法用于重载 += 运算符'''
        self.date.extend(other.date)# self.date+=other.date
        return self
    def __mul__(self,other):
        return MyList(self.date*other)
    def __rmul__(self,other):
        return MyList(self.date*other)
    
L1 = MyList([1, 2, 3])
L2 = MyList(range(4, 6))
print(id(L1))
L1+=L2
print(id(L1))
print(L1)
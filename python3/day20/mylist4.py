#此示例示意in/not in运算符的重载
class MyList:
    def __init__(self,iterable=()):
        self.date=[x for x in iterable]
    def __repr__(self):
        return "MyList(%s)" % self.date
    def __contains__(self,e):
        return e in self.date
L1 = MyList([1, 2, 3,-4,-5])
print(3 in L1)
print(6 in L1)
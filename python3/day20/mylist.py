#
class MyList:
    def __init__(self,iterable=()):
        self.date=[x for x in iterable]
    def __repr__(self):
        return "MyList(%s)" % self.date
    def __neg__(self):
        gen=(-x for x in self.date)
        return  MyList(gen)
    def __pos__(self):
        gen=(abs(x) for x in self.date )
        return MyList(gen)
    def __invert__(self):
        gen=reversed(self.date)
        return MyList(gen)
L1 = MyList([1, 2, 3,-4,-5])
# L2=-L1#L2=L1.__neg__(L1)
# L3=+L1
L1=~L1
print(L1)
# print(L3)
# print(L2)

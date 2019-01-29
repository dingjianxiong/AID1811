class mylist:
    def __init__(self,iterable=()):
        self.date=[x for x in iterable]
    def __repr__(self):
        return "mylist(%s)" % self.date
    def __len__(self):
        return len(self.date)
        # return self.date.__len__()
    def __abs__(self):
        l=[abs(x) for x in self.date]
        lst=mylist(l)
        return lst
myl=mylist([1,-2,3,-4,5])
print(myl)#调用myl.__repr__(slef)
print(len(myl))

myl2=abs(myl)
print(myl2)
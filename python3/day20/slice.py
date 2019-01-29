# slice 构造函数
#   作用:
#     用于创建一个slice切片对象,此对象存储一个切片的起始值,
#     终止值,步长信息
#   格式:
#     slice(start=None, stop=None, step=None)
#   slice对象的属性
#     s.start 切片的起始值, 默认为None
#     s.stop  切片的终止值, 默认为None
#     s.step  切片的步长, 默认为None

class MyList:
    def __init__(self,iterable=()):
        self.date=[x for x in iterable]
    def __repr__(self):
        return "MyList(%s)" % self.date
    def __contains__(self,e):
        return e in self.date
    def __getitem__(self, i):
        return self.date[i]
L1 = MyList([1, 2, 3,-4,-5])
a=L1[:]#a=L1.__getitem__(slice(none,none,none))
print(a)
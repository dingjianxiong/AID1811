# 练习:
#   实现有序集合类 OrderSet()  能实现两个集合的交集 &,并集 |,
#     补集 -, 对称补集 ^, ==, !=, in/ not in 等 操作
#     规则写集合set 类完全相同
#     要求:集合内部用list存储
class OrderSet:
    def __init__(self, iterable=()):
        self.data = list(iterable)
    def __repr__(self):
        return "OrderSet(%s)" % self.data
    def __and__(self, rhs):
        a=set(self.data) & set(rhs.data)
        return OrderSet(a)
    def __or__(self, rhs):
        a=set(self.data) | set(rhs.data)
        return OrderSet(a)
    def __xor__(self, rhs):
        a=set(self.data) ^ set(rhs.data)
        return OrderSet(a)
    def __xor__(self, rhs):
        return set(self.data) in set(rhs.data)

s1 = OrderSet([1, 2, 3, 4])
s2 = OrderSet([3, 4, 5])
print(s1 & s2)  # OrderSet([3, 4])
print(s1 | s2)  # OrderSet([1, 2, 3, 4, 5])
print(s1 ^ s2)  # OrderSet([1, 2, 5])
if OrderSet([1,2,3]) != OrderSet([1,2,3,4]):
    print("不相等")
if s2 == OrderSet([3,4,5]):
    print("s2 == OrderSet([3,4,5])")
if 2 in s1:
    print("2 in s1")
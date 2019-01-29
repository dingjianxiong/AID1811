class mynumber:
    def __init__(self,value):
        self.data=value
    def __repr__(self):
        return "mynumber(%d)" %self.data
    def __add__(self,other):
        s=self.data+other.data
        return mynumber(s)
    def __sub__(self,rhs):
        s1=self.data-rhs.data
        return mynumber(s1)
    def __mul__(self, rhs):
        s1=self.data*rhs.data
        return mynumber(s1)
    def __truediv__(self, rhs):
        s1=self.data/rhs.data
        return mynumber(s1)
    def __floordiv__(self, rhs):
        s1=self.data//rhs.data
        return mynumber(s1)
n1=mynumber(100)
n2=mynumber(200)
print(n1)

# n3=n1.__add__(n2)
n3=n1+n2 #等同于 n3=n1.__add__(n2)
print(n1,"+",n2,"=",n3)

n4=n2-n1
print(n4)
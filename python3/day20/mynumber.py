# 运算符重载
#   什么是运算符重载
#     让自定义的类生成的对象(实例)能够使用运算符进行操作

#   作用:
#    让自定义的类的实例像内建对象一样进行运算符操作
#    让程序简洁易读
#    对自定义对象将运算符赋予新的运算规则
#   说明:
#     运算符重载方法的参数个数的传参都是有固定的含义,不能随便 
#     修改形参的个数
# 算术运算符重载
#   方法名                     运算符和表达式  说明
#  __add__(self, rhs)          self +  rhs  加法
#  __sub__(self, rhs)          self -  rhs  减法
#  __mul__(self, rhs)          self *  rhs  乘法
#  __truediv__(self, rhs)      self /  rhs  除法
#  __floordiv__(self, rhs)     self // rhs  地板除
#  __mod__(self, rhs)          self %  rhs  求余(取模)
#  __pow__(self, rhs)          self ** rhs  幂运算

#   rhs (right hand side)  右手边

# 二元运算符的重载方法格式:
#    def __xxx__(self, other):
#         .....
class mynumber:
    def __init__(self,value):
        self.data=value
    def __repr__(self):
        return "mynumber(%d)" %self.data
    def __add__(self,other):
        s=self.data+other.data
        return mynumber(s)
n1=mynumber(100)
n2=mynumber(200)
print(n1)

# n3=n1.__add__(n2)
n3=n1+n2 #等同于 n3=n1.__add__(n2)

print(n1,"+",n2,"=",n3)

# print(n3)
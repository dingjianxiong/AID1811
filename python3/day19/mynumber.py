#  函数重写（覆盖）
# 对象转字符串函数的重写方法
#   repr() 函数的重写方法:
#     def __repr__(self):
#         return 字符串
#   str() 函数的重写方法:
#     def __str__(self):
#         return 字符串
#   说明:
#     __repr__ 和 __str__方法必须返回字符串
class mynumber:
    '''自定义一个数字类，用力啊表示自定义的数字信息'''
    def __init__(self,value):
        '''初始化方法'''
        self.data=value
    def __str__(self):#覆盖原来父类的方法
        return "数字："+str(self.data)
    def __repr__(self):#覆盖原来父类的方法
        return "mynumber(%d)" %self.data
n1=mynumber(100)
print(str(n1))
print(repr(n1))

n2=mynumber(200)
print(str(n2))
print(repr(n2))
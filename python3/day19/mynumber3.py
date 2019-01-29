class mynumber:
    '''自定义一个数字类，用力啊表示自定义的数字信息'''
    def __init__(self,value):
        '''初始化方法'''
        self.data=value

    def __repr__(self):#覆盖原来父类的方法
        return "mynumber(%d)" %self.data
    def __int__(self):
        return "i=%d" % n1
n1=mynumber(100)
i=int(n1)
print(i)
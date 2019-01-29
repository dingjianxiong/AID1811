class mynumber:
    '''自定义一个数字类，用力啊表示自定义的数字信息'''
    def __init__(self,value):
        '''初始化方法'''
        self.data=value
    def __len__(self):
        print("__len__方法被调用")
        return len(self.data)
    def __bool__(self):
        for x in self.data:
            if bool(x)==False:
                return False
        return True
                

n1=mynumber([1,-3,0,4,-1])
print(bool(n1))
if n1:
    print("真值")
else:
    print("假值")
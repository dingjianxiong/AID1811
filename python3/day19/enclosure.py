class A:
    def __init__(self):
        self.__money=100#私有属性，只能用此类方法调用
    def borror(self,x):
        if x <self.__money:
            self.__money-=x
            return x
        return 0
a=A()
#访问私有属性失败
# print(a.__money)
# a.__money=100#由类的外部直接操作money属性
# print(a.money)

print("借钱",a.borror(800))
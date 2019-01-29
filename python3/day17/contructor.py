#定义一个新的类用来描述狗的行为和属性
class dog:
    '''这是类的文档字符串
    此类用于描述狗的行为和属性
    '''
    pass
dog1=dog()#用dog来创建一个dog类型的对象
print(id(dog1))
dog2=dog()#用构造函数来创建一个dog类型的对象
print(id(dog2))
list1=list()#用list类创建一个列表对象
print(id(list1))
list2=list()#创建另一个列表对象
print(id(list2))
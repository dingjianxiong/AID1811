# day17 回顾
# 面向对象
#   特征:
#     属性
#       实例属性(实例变量)
#     行为
#       实例方法(method)

# 类
#   class 类名(继承列表):
#       ....

# 构造函数
#   类名(实参列表)

# 实例方法:
#   class 类名(继承列表):
#       def 方法名(self, 形参列表):
#           语句块
#       def __init__(self, 形参列表):
#           '''初始化方法,主要为该类创建的对象添加统一的属性'''
#           语句块
#       def __del__(self):
#           '''析构方法, 在对象被销毁前才被调用'''
      
# 实例方法的调用语法:
#   对象(实例).实例方法名(调用传参)
#   类名.方法名(实例-->self, 调用传参)

# 实例变量(实例属性)
#   对象(实例).实例变量名 = 表达式    # 创建,或修改实例变量
#   v = 对象(实例).实例变量名        # 实例变量的取值操作
# 删除实例变量:
#   del 语句 删除实例变量

# 预置的实例变量(实例属性)
#   __dict__ 属性字典, 绑定的是字典,存储的是 属性--> 值

#   __class__属性  绑定 创建此实例的类

# isinstance(对象, 类或元组)
# type(x)  返回对象的类




# day18笔记
# 类变量(类属性)
#   类变量是类的属性, 此属性属于类,不属于此类的实例 

#   作用:
#     通常用来存储该类创建的对象的共有属性
#   说明:
#     1. 类变量可以通过该类直接访问
#     2. 类变量可以通过类的实例直接访问 
#     3. 类变量可以通过此类的对象的__class__属性间接访问
#   示例见:

#     class_variable.py
# 此示例示意类变量的定义和使用方法
# class Human:
#     total_count = 0  # 类变量,用来记录此类的实例的个数
    
# # 1. 类变量可以通过该类直接访问
# print(Human.total_count)  # 0
# Human.total_count += 100  # 
# print(Human.total_count)  # 100
# class Human:
#     total_count=0
#     def Student(self,n,a,s):
#         self.name=n
#         self.age=a
#         self.score=s
#         self.total_count+=1
#     def count(self):
#         print(self.total_count)
# a=Human()
# a.Student("ww",23,15)
# a.Student("ww",23,15)
# a.count()
#     class_variable2.py
# 此示例示意类变量的定义和使用方法
# class Human:
#     total_count = 0  # 类变量,用来记录此类的实例的个数

# # 2. 类变量可以通过类的实例直接访问(取值)
# h1 = Human()  # 创建一个实例
# print(h1.total_count)  # 0
# h1.total_count = 100  # 创建实例变量的语法
# print(h1.total_count)  # 100

# print("Human.total_count=", Human.total_count)  # 0


#     class_variable3.py
# 此示例示意类变量的定义和使用方法
# class Human:
#     total_count = 0  # 类变量,用来记录此类的实例的个数


# # 3. 类变量可以通过此类的对象的__class__属性间接访问
# h1 = Human()
# print(h1.total_count)  # 0
# h1.__class__.total_count += 100  # Human.total_count += 100
# print(h1.total_count)  # 100

# print(Human.total_count)  # 100


# 类的文档字符串
#   类内第一个没有赋值给任何变量的字符串为类的文档字符串
#   类的文档字符串可以通过help函数查看
#   类的文档字符串可以用 类的 __doc__属性访问
                                                                                                          
#   示例:
#     class Human:
#        '地球上的主载者'
#        pass
#   >>> help(Human)

# 类的__slots__列表
#   作用:
#     限定一个类创建的实例只能有固定的属性(实例变量)
#     不允许对象添加列表以外的实例属性(实例变量)
#     防止用户因错写属性的名称而发生程序运行时错误
#   说明:
#     1. __slots__属性是一个列表,列表的值是字符串
#     2. 含有__slots__属性的列表所创建的实例对象没有__dict__
#        属性即此实例不用字典来存储对象的实例属性(实例变量)
#   示例见:
#     class_slots.py

# class Human:
#     __slots__ = ['name', 'age']
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def show_info(self):
#         print(self.name, self.age)

# s1 = Human('Tarena', 15)
# s1.show_info()  # tarena 15
# # s1.Age = 16  # 错写了属性名为Age,如果有slots列表,则会报错
# s1.show_info()  # tarena 15


# 类方法 @classmethod
#   类方法是用于描述类的行为的方法,类方法属于类,不属于该类创建
#   的对象

#   说明:
#     1. 类方法需要使用@classmethod装饰器定义
#     2. 类方法至少有一个形参,第一个形参用于绑定类,约定写为'cls'
#     3. 类和该类的实例都可以调用类方法
#     4. 类方法不能访问此类创建的对象的实例属性
#   示例见:
#     classmethod.py
# class A:
#     v=0
#     @classmethod
#     def get_v(cls):
#         return cls.v
#     @classmethod
#     def set_v(cls,v):
#         cls.v=v
#         return cls.v
# print(A.v)
# print(A.get_v())

# A.set_v(80)
# print(A.get_v())
# print(A.v)
# a=A()
# print(a.get_v())


# 静态方法 staticmethod
#   静态方法是定义在类的内部的函数,此函数的作用域是类的内部

#   说明:
#     1. 静态方法需要使用@staticmethod装饰器定义
#     2. 静态方法与普通函数定义相同,不需要传入self实例参数和
#       cls 类参数
#     3. 静态方法只能凭借该类或该类创建的实例来调用
#     4. 静态方法不能访问类变量和实例变量
#   示例见:
#     staticmethod.py
# 引示例示意静态方法的定义和使用
# class A:
#     @staticmethod
#     def myadd(a, b):
#         return a + b
    
# print(A.myadd(100, 200))  # 300
# a = A()
# print(a.myadd(30, 40))  # 70

# 实例方法, 类方法, 静态方法, 函数
#     实例方法能访问实例变量, 类变量 和全局变量
#     类方法不能访问实例变量,能访问类变量和全局变量
#     静态方法不能访问实例变量,类变量,但能访问全局变量
#     函数,只能访问全局变量


# 继承 (inheritance) 和派生(derived)
#   什么是继承/派生
#     继承是从已有的类中派生出新的类,新类具有原类的属性和行为,
#     并能扩展新的行为
#     派生类就是从一个已有类中衍生出新类,在新的类上可以添加新
#     的属性和行为
#   为什么继承/派生
#     继承的目的是延续旧类的功能
#     派生的目地是在旧类的基础上添加新功能
#   作用:
#     用继承派生机制, 可以将一些共有功能加在基类中,实现代码共享
#     在不改变基类的代码的基础上改变原有类的功能
#   名词
#     基类(base class)/超类(super class)/父类(father class)
#     派生类(derived class) / 子类(child class)

# 单继承
#   语法:
#     class 类名(基类名):
#         语句块 
#   说明:
#     单继承是指派生类由一个基类衍生出来的
#   示例见:
#     inherit.py

# class Student:
#     def say(self,what):
#         print("说",what)
#     def walk(self,distance):
#         print("走了",distance,"公里")

# class Student1(Student):
#     def xue(self,subject):
#         print("学习：",subject)
# class teacher(Student):
#     def xue(self,subject):
#         print("学习：",subject)
# h2=Student1()
# h2.walk(5)
# h2.say("天气变冷了")
# h2.xue("python")
# t1=teacher()
# t1.say("上课了")
# t1.walk(2)
# t1.xue("数学")

# 继承说明:
#   Python3 任何类都直接或间接的继承自object类
#   object类是一切类的超类

# 类的 __base__ 属性
#   __base__属性用来记录此类的基类(父类,超类)

# Python3内类的继承关系:
#   详见:
#      >>> help(__builtins__)
  

# 思考:
#   list 类里只有apend向末尾加一个元素的方法,但没有向列表头部
#   添加元素的方法,试想能否为列表在不改变原有功能的基础上添加一
#   个 insert_head(n) 方法在列表的头部添加新元素

#     class MyList(list):
#         def insert_head(self, n):
#              ....  # 此自己偿试写代码

#     myl = MyList(range(3, 6))
#     print(myl)  # [3, 4, 5]
#     myl.insert_head(2)
#     print(myl)  # [2, 3, 4, 5]
#     myl.append(6)
#     print(myl)  # [2, 3, 4, 5, 6]





# 覆盖 override
#   什么是覆盖,
#     覆盖是指在有继承关系的类中,子类中实现了与基类同名的方法,
#     在子类的实例调用该方法时,实际调用的是子类中的覆盖版本,这
#     种现象叫覆盖
#   作用:
#     实现和父类同名,但功能不同的方法

#   示例见:
#     override.py
# class A:
#     def work(self):
#         print("A.work被调用!")
    
# class B(A):
#     '''B类继承自A类'''
#     def work(self):
#         print("B.work被调用")
#     pass

# b = B()
# b.work()  # B.work被调用

# b = A()
# b.work() # A.work被调用,根据b绑定的对象的类型来进行查找
# 问题:
#   当覆盖发生时,子类对象能否调用父类中的方法?

# 子类对象显式调用基类方法:
#   基类名.方法名(实例, 实际调用参数....)


# super 函数
#   super(cls, obj)  返回绑定超类的实例(要求obj必须为cls类
#             型的实例或cls子类的实例)
#   super()     返回绑定超类的实例,等同于:
#             super(__class__, 实例方法的第一个参数), 必须
#             用在方法内调用
#   作用:
#     借助super() 返回的实例间接调有和父类的覆盖方法
#   示例见:
#     super.py
# 此示例示意super函数的使用
# class A:
#     def work(self):
#         print("A.work被调用!")
    
# class B(A):
#     def work(self):
#         print("B.work被调用")

#     def do_work(self):
#         # 1. 调用B类的work方法
#         self.work()
#         # 2. 调用A类的work方法
#         super(B, self).work()
#         # 3.  如果在方法内调用,可以写为如下:
#         super().work()  # 等同于super(B, self).work

# b = B()  # 创建一个实例 
# # b.work()  # B.work被调用
# # super(B, b).work()  # A.work被调用
# b.do_work()
# super().work()  # 出错,super无参调用只能在方法中调用


# 显式调用基类的初始化方法:
#   当子类中实现了__init__方法时,基类的初始化方法并不会被调用
#   此时需要显式调用才能完成对父类对象的初始化

#   示例见:
#     super_init.py
#     mylist.py

# class Human:
#     def __init__(self, n, a):
#         self.name = n  # 姓名
#         self.age = a  # 年龄
#         print("Human.__init__被调用")

#     def infos(self):
#         print("姓名:", self.name)
#         print("年龄:", self.age)

# class Student(Human):
#     def __init__(self, n, a, s=0):
#         # self.name, self.age = n, a  # 不符面向对象的编程思想
#         super().__init__(n, a)  # 显式调用父类的初始化方法
#         self.score = s
#         print("Student.__init__被调用!")

#     def infos(self):
#         super().infos()
#         print("成绩:", self.score)

# s1 = Student('小李', 18, 98)
# s1.infos()

# h1 = Human("小张", 20)
# h1.infos()




# 用于类的函数:
#   issubclass(cls, class_or_tuple)  判断一个类是否继承自
#      class, 如果此类cls 是class 或tuple元组中一个类的派生
#      子类,则返回True,否则返回False

#   示例:
#     issubclass(bool, int)   # True
#     class A:
#         pass
#     class B(A):
#         pass
#     class C(B):
#         pass
#     issubclass(C, B)  # True
#     issubclass(B, A)  # True
#     issubclass(C, A)  # True




# 练习:
#   1. 修改原学生信息管理程序, 将原来用字典存储学生信息,改为
#     用对象存储学生信息
#       建议 写一个student.py 内存来存放:
#         class Student:
#              .....
#   2. 写一个Bicycle类,用run方法,调用时显示骑行的里程
#     class Bicycle:
#         def run(self, km):
#             print("自行车骑行了", km, '公里')
    
#     再写一个EBicycle(电动自行车), 在Bicycle类的基础上,添加电池
#     电量volume属性,此类有两个方法:
#       fill_charge(vol)  用来充电,vol为电量(度)
#       run(km) 方法 每骑行 10km 消耗1度电,同时显示当前电量,当
#       电量耗尽时则用脚蹬骑行(调用Bicyle的run方法 )
#     class EBicycle(Bicycle):
#          ....
        
#     测试程序:
#     b = EBicycle(5)  # 新买的电动车内有5度电
#     b.run(10)  # 电动骑行了10km 还剩4度电
#     b.run(100) # 电动骑行了40km 还剩0度电  自行车骑行了 60 公里
#     b.fill_charge(10)  # 电动自行车充电10度
#     b.run(50)  # 电动骑行了50km 还剩5度电
            



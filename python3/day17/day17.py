# day16 回顾
# 文件 File
#   作用:
#     通常长期存储"字节"为单位的数据
#   文件的操作步骤:
#     1. 打开
#     2. 读/写
#     3. 关闭
#   文件的打开模式:
#     文本文件模式: 't'
#         默认把文件中的内容看成是utf-8格式的字符串
#         在文件的读写过程中会自动进行编码和解码操作
#         换行符会自动进行转换: '\r\n' '\n'  --> '\n'
#     二进制文件模式: 'b'
#         默认把文件中的内容看成是以字节为位置的数据
#   文件的读写模式:
#     读文件:
#       模式字符: 'r'(默认)
#       读方法:
#         F.read([最大字符数或字节数])
#         F.readline()
#         F.readlines()
#     写文件:
#       模式字符: 'w', 'x', 'a'
#       写方法:
#         F.write(字节串或字符串)
#         F.writelines(字节串或字符串列表)

#   文件打开函数:
#     open(文件路径名, 打开模式='rt')
#   文件操作的方法:
#     F.close()
#     F.tell()  # 获取当前的读写位置
#     F.seek(偏移量,起始位置)
#     F.flush()  清空缓冲区

# 汉字编码:
#    只有两种
#       GB系列(绝大部分是两字节编码,还有四字节编码)
#         GB18030(GBK(GB2312))
#       UNICODE系列:
#         UNICODE32(UNICODE16)  <--> UTF-8 互转
      
#   编码注释:
#     # -*- coding:utf-8 -*-


# day17笔记
# 面向对象编程 Object-Oriented Programming
#   什么是对象
#     对象是指现实中的物体或实体

#   什么是面向对象
#     把一切看成对象(实例), 用各种对象之间的关系来描述事务

#   对象都有什么特征:
#     对象有很多属性(名词,形容词,数词等)
#       姓名,年龄,性别,衣服颜色
#     对象有很多行为(动作,动词)
#       学习,吃饭,睡觉,踢球,工作

# 什么是类
#   拥有相同属性和行为的对象分为一组,即为一个类
#   类是用来描述对象的工具,用类可以创建此类的对象(实例)

# 示意
#   车(类) ---------->   BYD E6(京A.88888) 实例,对象
#         \
#          \--------> BWM  X(京B.00000)  实例,对象

#   狗(类) ----------> 小京巴(户籍ID:000001) 实例
#         \
#          \--------> 哈士奇(户籍ID: 000002) 实例对象

#   int(类)   --------> 100 (对象,实例)
#           \
#            \--------> 200 (对象,实例)

# 类的创建语句 class 语句
#   语法:
#     class 类名(继承列表):
#         '''类的文档字符串'''
#         实例方法定义
#         类变量的定义
#         类方法(@classmethod) 定义
#         静态方法(@staticmethod) 定义
#   作用:
#     创建一个类
#     类用于描述对象的行为和属性
#     类用于创建此类的一个或多个对象(实例)
#   说明:
#     继承列表可以省略
#     类名必须是一个标识符(写变量的命名相同,建议首字母大写)
#     类名实质上就是变量,它绑定一个类
#   示例见:
#     class.py


# 构造函数
#   构造函数调用表达式
#     类名([创建传参列表])
#   作用:
#     创建这个类的实例对象,并返回此实例对象的引用关系
#   示例见:
#     contructor.py
    
# 名词
#   类     |       对象(实例)
#  class   |     object(instance)


# 实例说明:
#   实例有自己的作用域和名字空间,可以为该实例添加实例变量(属性)
#   实例可以调用实例方法和类方法 
#   实例可以访问实例变量和类变量

# 实例方法(instance method)
#   定义语法:
#     class 类名(继承列表):
#         def 实例方法名(self, 参数1, 参数2, ...):
#             '''方法的文档字符串'''
#               语句块
#   作用:
#     用于描述一个对象的行为.让此类型的全部对象都拥有相同的行为
#   说明:
#     实例方法的实质是函数,是定义在类内的函数
#     实例方法至少有一个形参,第一个形参用来调用这个方法的实例,
#       一般命名为'self'
#   调用语法:
#     实例.实例方法名(调用传参)
#     类名.实例方法名(实例, 调用传参)
#   示例见:
#     instance_method.py



# 实例变量(也称为实例属性)
#   每个实例可以有自己的变量,称为实例变量(实例属性)
#   语法:
#     实例.属性名
#   作用:
#     记录每个对象自身的数据
#   赋值规则:
#     首次为属性赋值则创建此属性
#     再次为属性赋值则改变属性的绑定关系
#   示例见:
#     attribute.py



# 练习:
#   定义一个 '人' (Human) 类
#   class Human:
#       def set_info(self, n, a, addr='不详'):
#           '''此方法用来给对象添加'姓名','年龄',
#           '家庭住址'属性'''
#            ... 此处自己实现
#       def show_info(self):
#           '''此处显示此人的信息'''
#           ...  此处自己实现
#   s1 = Human()
#   s1.set_info("小张", 20, '北京市东城区')
#   s2 = Human()
#   s2.set_info("小李", 18)
#   s1.show_info()  # 小张 今年 20 岁,家庭住址: 北京市东城区
#   s2.show_info()  # 小李 今年 18 岁,家庭住址: 不详
# class Human:
#     def set_info(self,name,age,address='不详'):
#         self.name=name
#         self.age=age
#         self.address=address
#     def show_info(self):
#         print(self.name,"今年：",self.age,"家庭地址：",self.address)
# h1=Human()
# h1.set_info("小张",20,"北京朝阳区")
# h2=Human()
# h2.set_info("小李",20)
# h1.show_info()
# h2.show_info()

# 删除属性
#   del 语句
#     语法:
#        del 对象.实例变量名
#     示例:
#       class Dog:
#           pass

#       dog1 = Dog()
#       dog1.color = '白色'  # <<<--- 添加实例变量
#       print(dog1.color)  # 白色
#       del dog1.color  # 删除实例变量(属性)
#       print(dog1.color)  # 属性错误,没有color这个属性


# 初始化方法:
#   作用:
#     对新创建的对象添加属性
#   格式:
#     class 类名(继承列表):
#         def __init__(self[, 形参列表]):
#             语句块
#     注: []代表其中的内容可省略
#   说明:
#     1. 初始化方法名必须为__init__ 不可改变(注:双下划线)
#     2. 初始化方法会在构造函数创建实例后自动调用,且将实例自身
#        通过第一个参数self传入__init__方法
#     3. 构造函数的实参将通过__init__方法的参数列表传入 
#        到__init__ 方法中
#     4. 初始化方法内如果需要return 语句返回则必须返回None
#   示例见:
#     init_method.py


# 练习:
#   1. 写一个学生类Student类.此类用于描述学生信息,学生信息有:
#      姓名,年龄,成绩(默认为0)
#     1) 为该类添加初始化方法,实现在创建对象时自动设置:
#        姓名(name),年龄(age), 成绩(score)属性
#     2) 添加set_score方法能力对象修改成绩信息
#     3) 添加show_info方法打印学生对象的信息
#   如:
#     class Student:
#         def __init__(...):
#             ...
#         def set_score(self, score):
#             ...
#         def show_info(self):
#             ...
#     L = []
#     L.append(Student("小张", 20, 100))
#     L.append(Student("小李", 18, 98))
#     L.append(Student("小菜", 19))
#     L[-1].set_score(70)
#     for s in L:
#         s.show_info()  # 列出所有学生的信息


# 析构方法
#   格式:
#     def __del__(self):
#         语句块
#   说明:
#     析构方法在对象(实例)销毁前被自动调用
#     python语言建议不要在对象销毁时做任何事情,因为销毁的时间
#     难以确定
#   作用:
#     在对象销毁前,释放此对象占用的资源
#   示例见:
#     del_method.py


# 预置的实例属性
#   __dict__属性
#     __dict__属性绑定一个存储此实例自身变量(属性)的字典

#   示例:
# class Dog:
#     pass
# dog1 = Dog()
# print(dog1.__dict__)   # {}
# dog1.color = "白色"
# print(dog1.__dict__)  # {'color':'白色}

#   __class__ 属性
#     __class__属性用来绑定创建此实例的类
#     作用:
#       可以借助于此属性来访问创建此实例的类

#     示例:      
# class Dog:
#     pass

# dog1 = Dog()
# L = [1, 2, 3, 4]

# print(dog1.__class__)
# dog2 = dog1.__class__()  # 调用构造函数创建一个与
#                         # dog1同类的对象
# print(L)


# 用于类的函数: 
#   isinstance(obj, class_or_tuple) 返回这个对象obj是否是
#            某个类的对象或某些类中一个类的对象，如果是返
#            回True,否则返回False
#   type(obj)  返回对象的类
# 　
#   示例:
#     isinstance("ABC", str)  # True
#     isinstance(123, str)    # False


# 练习:
#   有两个人:
#     1. 姓名: 张三, 年龄: 35
#     2. 姓名: 李四, 年龄: 10
#   行为:
#     1. 教别人学东西 teach
#     2. 工作赚钱  work
#     3. 借钱 borrow
#     4. 显示自己的信息 show_info
#   事情:
#     张三 教 李四 学 python
#     李四 教 张三 学 王者荣耀
#     张三 上班赚钱 1000 元
#     李四 向 张三 借钱 200元
#     35 岁的 张三 有钱 800 元,它学会的技能是: 王者荣耀
#     10 岁的 李四 有钱 200 元,它学会的技能是: python
#   类的封装如下:
#     class Human:
#         def __init__(self, ....):
#             ...
#         ...
#     zhang3 = Human("张三", 35)
#     li4 = Human("李四", 10)
#     .... 此处描述事情的过程



# 练习:
#   1. 分解质因数,输入正整数,分解质因数:
#     如
#       输入:
#         90
#     打印如下:
#       90=2*3*3*5
#     质因数是指最小能被原数整数的素数(不包括1)
#   2. 用类来描述一个学生信息(可以修改之前写的Student类)
#     class Student:
#         此处自己实现
#     学生信息有:
#        姓名,年龄, 成绩
#     将这些学生的对象存于列表中,可以任意添加和删除学生信息
#      1) 打印出学生的个数
#      2) 打印出所有学生的平均成绩
#      3) 打印出所有学生的平均年龄

#   3. 看懂 练习 human2.py中的代码(张三,李四的逻辑)
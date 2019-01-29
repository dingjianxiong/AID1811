
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


# 练习:
#   1. 写一个学生类Student类.此类用于描述学生信息,学生信息有:
#      姓名,年龄,成绩(默认为0)
#     1) 为该类添加初始化方法,实现在创建对象时自动设置:
#        姓名(name),年龄(age), 成绩(score)属性
#     2) 添加set_score方法能力对象修改成绩信息
#     3) 添加show_info方法打印学生对象的信息
#   如:
# class Student:
#     def __init__(self,name,age,score=0):
#         self.name=name
#         self.age=age
#         self.score=score
#     def set_score(self, score):
#         self.score=score
#     def show_info(self):
#         print("姓名：",self.name,"年龄：",self.age,"成绩：",self.score)
# L = []
# L.append(Student("小张", 20, 100))
# L.append(Student("小李", 18, 98))
# L.append(Student("小菜", 19))
# print(L)
# L[-1].set_score(70)
# for s in L:
#     s.show_info()  # 列出所有学生的信息
# print(L)


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
class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.money=0
        self.skill=[]
    def teach(self,other,subject):
        print(self.name,"教",other.name,"学",subject)
        other.skill.append(subject)
    def work(self,money):
        print(self.name,"上班赚钱",money,"元")
        self.money+=money
    def borrow(self,other,money):
        print(self.name,"向",self.name,"借",money,"元")
        self.money-=money
    def show_info(self):
        print(self.age,"的",self.name,"有钱",self.money,"他学会的技能是：",self.skill)
zhang3 = Human("张三", 35)
li4 = Human("李四", 10)

# .... 此处描述事情的过程
zhang3.teach(li4,"python")
li4.teach(zhang3,"王者荣耀")
zhang3.work(1000)
li4.borrow(zhang3,200)
zhang3.show_info()
li4.show_info()
#   2. 用类来描述一个学生信息(可以修改之前写的Student类)
#     class Student:
#         此处自己实现
#     学生信息有:
#        姓名,年龄, 成绩
#     将这些学生的对象存于列表中,可以任意添加和删除学生信息
#      1) 打印出学生的个数
#      2) 打印出所有学生的平均成绩
#      3) 打印出所有学生的平均年龄

# class Student:
#     def __init__(self,n,a,s=0):
#         self.name=n
#         self.age=n
#         self.score=s
# infos=[]
# def add_Student(info,n,a,s):
#     '''添加学生信息'''
#     stu=Student(n,a,s)
#     infos.append(stu)
# def del_student(infos):
#     n=input("请输入要删除的学生姓名：")
#     for index,stu in enumerate(infos):
#         if stu.name==n:
#             del infos[index]
#             print("删除",n,"成功")
#             return
#     print("删除",n,"失败")
# def get_avg_score(infos):
#     s=0
#     for stu in infos:
#         s+=stu.score
#         return s/(infos)
# add_Student(infos,"小张",20,100)
# add_Student(infos,"小李",30,60)
# add_Student(infos,"小王",50,80)
# add_Student(infos,"小赵",10,90)
# # del_student(infos)
# get_avg_score(infos)


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

#     class MyList(list):
#         def insert_head(self, n):
#              ....  # 此自己偿试写代码

# class MyList(list):
#     def insert_head(self, n):
#         # self[0:0]=[n]
#         self.insert(0,n)#insert列表插入函数，插入在第0个位置
# myl = MyList(range(3, 6))
# print(myl)  # [3, 4, 5]
# myl.insert_head(2)
# print(myl)  # [2, 3, 4, 5]
# myl.append(6)
# print(myl)  # [2, 3, 4, 5, 6]


class Dog:
    l=[]
    dog_count=0
    def __init__(self,color,pinz,name):
        self.color=color
        self.pinz=pinz
        self.name=name
        self.__class__.dog_count+=1
        Dog.l.append(self)
    def play(self,w):
        print(self.color,"的",self.pinz,"叫",self.name,"在玩：",w)
    def del_dog(self):
        sa=input("请输入要删除的狗：")
        for index,x in enumerate(self.__class__.l):
            if sa==x.name:
                del self.__class__.l[index]
        print(self.color,"的",self.pinz,"叫",self.name,"走了")
class dog_01(Dog):
        Dog.dog_count+=1
d1=Dog("黄色","哈士奇","二哈")
d2=Dog("灰色","拉布拉多","小灰")
d1.play("球")
d2.play("水")
print(Dog.l)
print("一共有：",Dog.dog_count,"个小狗")
# Dog.del_dog(d1)删除

d2=dog_01("红色","田园犬","小红")
d2.play("玩具")
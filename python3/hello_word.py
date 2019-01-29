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
#     def __init__(self, n, a, s):
#         self.name = n
#         self.age = a
#         self.score = s


# L = []
# L.append(Student("小张", 20, 100))
# L.append(Student('小李', 18, 98))
# L.append(Student('小赵', 19, 88))
# L.append(Student('小钱', 17, 70))

# #  1) 打印出学生的个数
# print('学生数是:', len(L))
# #  2) 打印出所有学生的平均成绩
# total_score = 0
# for s in L:
#     total_score += s.score
# print("平均成绩是:", total_score/len(L))
# print("平均成绩是:", sum(map(lambda s: s.score, L))/len(L))

# #  3) 打印出所有学生的平均年龄
# print("平均年龄:", sum((s.age for s in L))/len(L))

# class Student:
#     l=[]
#     def __init__(self,name,age,score):
#         self.name=name
#         self.age=age
#         self.score=score
#         Student.l.append(self)
#         print(l)
# s1=Student("丁",18,90)
# s1=Student("小王",18,90)
# s1=Student("丁",18,90)

# l=[1,2,3]
# def fun(a):
#     a=[4,5,6]
# fun(l)
# print(l)

# class A:
#     v=100
#     def __init__(self):
#         self.v=200
# a1=A()
# a2=A()
# del a2.v
# print(a1.v)
# print(a2.v)
# a=2 + 2 * 3 * 2 ** 3
# print(a)
# d = {'a': 3, 'b': 2, 'c': 1}
# print(sorted(d))
# x = (y = z+1)
# class Human:
#     def __init__(self, name="Anonymous", age=0, *args):
#         self.name
#         self.age = name, age
#     def infos(self):
#         print(self.name, self.age)

# class Teacher(Human):
#     def __init__(self, name, age, address=""):
#         self.address = address
#     def infos(self):
#         print(self.name, self.age, self.address)
# t1 = Teacher("Mr. zhang", 35)
# t1.infos()

# a = {'one': 1, 'two': 2, 'three': 3}
# print(a.setdefault('one'), a.setdefault('four'))
# print(a)

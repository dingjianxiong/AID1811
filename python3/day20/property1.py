# 特性属性 @property
#   实现其它语言拥有的 getter 和 setter 功能

#   作用:
#     用来模拟一个属性
#     通过@property 装饰器可以对模拟属性的取值和赋值加以控制

class student:
    def __init__(self,s):
        self.__score=s
    def getscore(self):
        return self.__score
    def setscore(self,s):
        assert 0<=s<=100,'成绩效验失败'
        self.__score=s
    score=property(getscore,setscore)
# stu=student(59)
# print(stu.getscore())#取值
# stu.setscore(99)
# print(stu.getscore())

stu=student(59)
print(stu.score)#取值
stu.score=99  #赋值
print(stu.score)
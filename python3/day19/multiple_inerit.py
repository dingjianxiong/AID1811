#多继承
class plane:
    def fly(self,height):
        print("飞机以海拔",height,"米的高度飞行")
class car:
    def run(self,speed):
        print("汽车以",speed,"公里/小时的速度行驶")
class planecar(plane,car):
    '''planecar继承至plane和car类'''
p1=planecar()
p1.fly(1000)
p1.run(300)


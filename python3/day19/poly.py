class shape:
    def draw(self):
        print("shape.draw（）方法被调用")
class point(shape):
    def draw(self):
        print("正在画一个点")
class circle(point):
    def draw(self):
        print("正在画一个圆")
def my_draw(s):
    s.draw()#
s1=circle()
s2=point()
my_draw(s1)
my_draw(s2)
#多继承的调用
class A:            #4
    def go(self):
        print("A")
class B(A):         #2
    def go(self):
        print("B")
        super().go()
class C(A):          #3
    def go(self):
        print("C")
        super().go()
class D(B,C):        #1
    def go(self):
        print("D")
        super().go()
d=D()
d.go()
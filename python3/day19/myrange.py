#   2. 实现一个与系统内建的range类相同功能的类
class MyRange:
    def __init__(self,start,stop=None,step=None):
        if stop==None:
            stop=start
            start=0
        if step==None:
            step=1
        self.start=start
        self.stop=stop
        self.step=step
    def __iter__(self):
        return mylistiterator(self.start,self.stop,self.step)
class mylistiterator:
    def __init__(self,start,stop,step):
        self.start=start
        self.stop=stop
        self.step=step
    def __next__(self):
        if self.step>0:
            if self.start>=self.stop:
                raise StopIteration
            r=self.start
            self.start+=self.step
            return r
        if self.step<0:
            if self.stop>=self.start:
                raise StopIteration
            r=self.stop
            self.stop+=self.step
            return r
        else:
            raise ValueError('range() arg 3 must not be zero')

# 测试调用如下:
L = list(MyRange(5))
print(L)   # [0, 1, 2, 3, 4]
print(sum(MyRange(1, 101)))  # 5050
for x in MyRange(1, 10, 3):
    print(x)  # 1 4 7
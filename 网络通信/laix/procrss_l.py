#import multiprocessing as mp
from time import sleep
from multiprocessing import Process,Queue,Pool
#自定义类
# class aaa(Process):
#     def __init__(self,age):
#         self.age=age
#         super().__init__

def func1(*n):
    for x in n:
        sleep(1)
        print("子进程:%s"%(p.name),x)
def func２(**n):
    # for x in n:
        # sleep(1)
    print("进程池:%s"%(p.name),n)
#创建进程对象
p=Process(target=func1,name='djx',args=range(2))
#创建进程池
pool=Pool()
result=[]
#向进程池放对象
for i in range(3):
    msg="进程：%s"%i
    # r=pool.apply_async(func=func1,args=(msg,))
    # result.append(r)
    pool.apply(func=func2,kwds={'a':1,'b':2,'c':3})
r=pool.map(func２,{'d':4,'e':5,'f':6})
#启动进程
p.daemon
p.start()
#父进程
sleep(5)
print("父进程")
print("process name:",p.name)
print("process pid:",p.pid)
print('process alive:',p.is_alive())
pool.close()
print("hello word")
for x in result:
    print(x.get())

#回收进程
p.join()
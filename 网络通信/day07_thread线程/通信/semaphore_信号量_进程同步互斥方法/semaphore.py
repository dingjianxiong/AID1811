from multiprocessing import Semaphore,Process
from time import sleep
import os

#创建信号量
sem=Semaphore(3)

def fun():
    print("%d想执行事件"%os.getpid())
    #消耗一个信号量
    sem.acquire()
    print("%d 执行事件..."%os.getpid())
    sleep(3)
    print("%d执行完毕"%os.getpid())
    print('sem:',sem.get_value())
    sem.release()#执行完成后添加一个信号量
jobs=[]
#5个进程想执行事件
for x in range(5):
    p=Process(target=fun)
    jobs.append(p)
    p.start()
#回收进程
for i in jobs:
    i.join()
#最后的信号量
print('sem:',sem.get_value())
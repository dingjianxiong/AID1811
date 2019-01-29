from multiprocessing import Semaphore,Process
from time import sleep
import os

sem=Semaphore(3)

def aa(*name):
    sem.acquire()
    print('name:',x,os.getpid())
    sleep(3)
    sem.release()#执行完成后添加一个信号量
    print('信号灯数量１：',sem.get_value())
    
jobs=[]
for x in range(5):
    p=Process(target=aa,name='djx')
    jobs.append(p)
    p.start()
for x in range(5):
    p.join()
print('信号灯数量２：',sem.get_value())
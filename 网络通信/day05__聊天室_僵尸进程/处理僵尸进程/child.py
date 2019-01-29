#创建二级子进程避免僵尸

import os 
from time import sleep

def f1():
    sleep(3)
    print("事件１....")
def f2():
    sleep(4)
    print("事件２....")

pid=os.fork()
if pid<0:
    print('Error')
elif pid==0:
    p=os.fork()#创建二级子进程
    if p==0:
        f2()
    else:
        os._exit(0)#一级子进程退出
else:
    os.wait()#等待回收一级子进程
    f1()
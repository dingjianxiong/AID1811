import multiprocessing as mp
from time import sleep

a=1
#编写进程函数(子进程)
def fun():
    sleep(3)
    global a
    print('a=',a)
    a=10000
    print('子进程事件')

#创建进程对象
p=mp.Process(target=fun)

#启动进程
p.start()
sleep(4)
print("父进程事件")

#回收进程（避免僵尸进程的产生）
# p.join(２)#阻塞函数互相不影响
print('a=',a)

from threading import Thread
from time import sleep

#线程函数
def fun(sec,name):
    print("线程函数传参")
    sleep(sec)
    print("%s线程函数执行完毕"%name)
#同时创建多个线程
thread=[]
for i in range(3):
    t=Thread(target=fun,args=(2,),kwargs={'name':'t%d'%i})
    thread.append(t)
    t.start()

for x in thread:
    x.join()
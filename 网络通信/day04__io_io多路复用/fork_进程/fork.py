import os
from time import sleep

pid=os.fork()
#在创建父进程的同时，也创建了一个子进程,同时执行，不确定先后顺序

if pid<0:
    print(pid)
    print("Create process error")
elif pid==0:
    sleep(2)
    print(pid)
    print("new process")
else:
    sleep(3)
    print(pid)
    print("The old process")
print("fork test end...")
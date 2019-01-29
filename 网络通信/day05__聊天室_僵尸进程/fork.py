import os
from time import sleep
print("---------------")
a=1
#创建进程
pid=os.fork()
if pid<0:
    print('create process failed')
elif pid==0:
    print('child process')
    print("a=",a)
    a=1000
else:
    #让父进程睡眠了０．５秒
    sleep(0.5)
    print('parent process')
    print("a=",a)
print('process end')
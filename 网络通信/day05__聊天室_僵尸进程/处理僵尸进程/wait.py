import os
from time import sleep

pid=os.fork()

if pid<0:
    print("Create process failed")
elif pid==0:
    # sleep(3)
    print("Child %d process exit" %os.getpid())
    os._exit(2)
else:
    #阻塞等待处理僵尸
    pid,status=os.wait()#
    print("pid:",pid)#退出的子进程的pid号
    print("status:",status)#子进程的退出状态,os.WEXITSTATUS(status))显示原来的值
    print("parent process...")
    while True:
        pass
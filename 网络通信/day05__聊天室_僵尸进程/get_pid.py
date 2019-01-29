import os
from time import *

pid=os.fork()
if pid<0:
    print("Error")
elif pid==0:
    
    print(pid)
    print("Child pid:",os.getpid())
    print("get Parent pid:",os.getppid())
else:
    print(pid)
    print("Parent pid",os.getpid())
    print("get Child pid",pid)
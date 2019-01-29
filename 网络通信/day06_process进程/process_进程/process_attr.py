from multiprocessing import Process
from time import ctime,sleep

def tm():
    for i in range(4):
        sleep(2)
        print(ctime())

p=Process(target=tm,name='djx')

p.daemon=True#必须在start创建之前使用

p.start()

print("process name:",p.name)
print("process pid:",p.pid)
print('process alive:',p.is_alive())

# p.join()
from threading import Thread,currentThread
from time import sleep

def fun():
    print('当前线程：',currentThread().getName())
    sleep(3)
    print("线程属性示例")
#线程对象
t=Thread(target=fun,name='djx')

#设置daemon值(不和join()一起使用)
t.setDaemon(True)
#查看daemon值
print('daemon:',t.isDaemon())

t.start()
#修改线程名称
t.setName('DINGJIANXIONG')

# print("name:",t.name)
print("name:",t.getName())

# t.join()

print('线程状态：',t.is_alive())


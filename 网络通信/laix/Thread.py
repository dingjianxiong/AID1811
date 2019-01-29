from threading import Thread,currentThread

def fun1():
    print(t.name)
    print(currentThread().getName())

t=Thread(target=fun1,name='djx')
t.start()
for i in range(3):
    print()
print("线程是否结束：",t.is_alive())
t.join()
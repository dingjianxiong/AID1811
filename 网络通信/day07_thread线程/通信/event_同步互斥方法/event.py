from threading import Event

#创建事件对象
e=Event()

e.set()#设置e
e.wait()

e.clear()#清除设置e

print(e.is_set())#判断e的当前状态，被设置返回true，未被设置返回false
print('--------')
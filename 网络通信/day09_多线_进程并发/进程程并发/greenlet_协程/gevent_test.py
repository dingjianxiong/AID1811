import gevent


def foo(a,b):
    print('running foo',a,b)
    gevent.sleep(2)
    print("running foo again")
def bar():
    print('running bar')
    gevent.sleep(3)
    print("running bar again")
#创建协程对象
f=gevent.spawn(foo,1,2)
b=gevent.spawn(bar)

#回收协程,遇到阻塞,开始运行函数，谁可以运行就运行
gevent.joinall([f,b])
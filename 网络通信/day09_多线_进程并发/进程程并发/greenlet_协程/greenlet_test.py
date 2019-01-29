from greenlet import greenlet

def test1():
    print(132)
    gr2.switch()#暂停，并执行test2
    print(43)
    gr2.switch()#暂停，并继续执行test2
def test2():
    print(55)
    gr１.switch()#暂停，并继续上一次执行
    print(66)
#将两个函数变为协程
gr1=greenlet(test1)
gr2=greenlet(test2)
gr1.switch()#执行协程函数test1
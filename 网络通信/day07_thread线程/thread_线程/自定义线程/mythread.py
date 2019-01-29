from threading import Thread
from time import sleep,ctime

#自定义线程类
class myThread(Thread):
    def __init__(self,target,args=(),kwargs={},name='tedu'):
        super().__init__()
        self.target=target
        self.name=name
        self.args=args
        self.kwargs=kwargs
    def run(self):
        #给player()传参
        self.target(*self.args,**self.kwargs)
#测试线程函数
def player(sec,song):
    for i in range(2):
        print('playing %s:%s'%(song,ctime()))
t=myThread(target=player,args=(3,),kwargs={'song':'凉凉'},name='djx')
t=Thread()
t.start()

t.join()
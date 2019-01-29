from multiprocessing import Process
import time

#接口
class clockproccess(Process):
    def __init__(self,value):
        self.value=value
        # 重新加载父类__init__
        super().__init__()
    #重新run方法
    def run(self):
        for i in range(5):
            print("the time is !",time.ctime())
            time.sleep(self.value)
#创建自定义类进程对象
p=clockproccess(2)
p.start()#自动调用run
p.join()

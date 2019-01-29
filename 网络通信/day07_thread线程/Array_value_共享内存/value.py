from multiprocessing import Process,Value
import time
import random

#创建共享内存
money=Value('i',10000)

#操作共享内存增加
def boy():
    for i in range(30):
        time.sleep(0.2)
        #对value属性操作即对共享内存操作
        money.value+=random.randint(1,1000)
    print('挣钱：',money.value)
def girl():
    for i in range(30):
        time.sleep(0.16)
        #rangdom.rangdint:表示随机整数
        money.value-=random.randint(100,900)
    print("花钱：",money.value)
b=Process(target=boy)
g=Process(target=girl)
b.start()
g.start()
b.join()
g.join()

print("一个月余额：",money.value)
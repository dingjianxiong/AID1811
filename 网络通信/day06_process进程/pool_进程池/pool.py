from multiprocessing import Pool
from time import sleep,ctime

#事件函数
def worker(msg):
    sleep(2)
    print(msg)
    return ctime()

#创建进程池　　（可以自己设置进程事件个数：pool=Pool(４)，不写则默认根据系统自动判断）
pool=Pool()

result=[]
#向进程池添加事件
for i in range(5):
    msg='hello %d'%i
    #异步执行：多个一同执行
    r=pool.apply_async(func=worker,args=(msg,))
    result.append(r)

    #同步执行：一个一个执行
    # pool.apply(func=worker,args=(msg,))
#关闭进程池
pool.close()
#回收进程
pool.join()
for i in result:
    print(i.get())#获取进程事件函数返回值
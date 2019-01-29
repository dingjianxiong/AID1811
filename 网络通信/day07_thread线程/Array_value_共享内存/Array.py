from multiprocessing import Process,Array
import time
#创建一个共享内存
# shm=Array('i',[1,2,3,4])

#开辟５个空间
shm=Array('i',5)

#存入字符串
shm=Array('c',b'hello')

def fun():
    for i in shm:
        print(i)
    # shm[0]=1000#修改共享内存
    shm[0]=b'h'#修改共享内存
p=Process(target=fun)
p.start()
p.join()

print(shm.value)

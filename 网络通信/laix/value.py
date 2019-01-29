from multiprocessing import Process,Value,Array
import time

money=Value('i',5000)
arry=Array('i',5)
arry=Array('i',[1,2,3,4,5])

def bay1():
    money.value=money.value-4000
    for x in arry:
        print(x+1)
    print('花钱：',money.value)
def bay2():
    money.value=money.value+1000
    for i in arry:
        print(i*2)
    print('挣钱：',money.value)
p=Process(target=bay1)
p1=Process(target=bay2)

p.start()
p1.start()
p.join()
p1.join()
print(money.value)
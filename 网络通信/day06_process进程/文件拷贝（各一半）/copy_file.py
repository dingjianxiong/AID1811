import os
filename='ass.txt'
#获取文件的大小
size=os.path.getsize(filename)
#父子进程公用一个偏移量会相互影响
#f=open(filename,'rb')
pid=os.fork()
if pid<0:
    print("error")
elif pid==0:
    #复制上半部分
    f=open(filename,'rb')
    fw=open('1','wb')
    n=size//2
    while True:
        if n<1024:
            data=f.read(n)
            fw.write(data)
            break
        data=f.read(1024)
        fw.write(data)
        n-=1024
    f.close()
    fw.close()
else:
    #复制下半部分
    f=open(filename,'rb')
    fw=open("2",'wb')
    #seek读写指针（读写偏移量）第一个参数读写的大小，第二个参数是开始读写位置
    f.seek(size//2,0)
    while True:
        data=f.read(1024)
        if not data:
            break
        fw.write(data)
    f.close()
    fw.close()
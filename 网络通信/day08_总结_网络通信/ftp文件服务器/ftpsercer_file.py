from socket import *
import os,sys
import time


HOST='0.0.0.0'#地址
PORT=6699#端口
ADDR=(HOST,PORT)
files = '/home/tarena/www/'

#将文件处理功能封装
class ftpserver(object):
    def __init__(self,c):
        self.c=c
    def do_list(self):
        print('执行lsit')
        #获取文件列表
        file_list=os.listdir(files)
        #如果文件目录为空不准获取
        if not file_list:
            self.c.send("文件库为空".encode())
        else:
            self.c.send(b'ok')
            #防止文件粘包
            time.sleep(0.1)
        fil=''
        for file in file_list:
            #删选出普通文件
            if file[0] !='.' and os.path.isfile(files+file):
                fil=fil+file+'#'
        #将拼接好的文件字符串发送
        self.c.send(fil.encode())
    def do_get(self,filename):
        #文件是否存在
        if os.path.exists(files+filename):
            self.c.send('文件存在'.encode())
            return
        try:
            fd=open(files+filename,'rb')
        except Exception:
            self.c.send("文件不存在".encode())
            return
        self.c.send(b'ok')
        time.sleep(0.1)
        #发送文件内容
        while True:
            data=fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.c.send(b'##')
                print("下载成功")
                break
            self.c.send(data)
    #接收文件
    def do_put(self,filename):
        try:
            fd=open(files+filename,'wb')
        except:
            self.c.send("上传失败")
        print("正在上传")
        self.c.send(b'ok')
        data=self.c.recv(128).decode()
        while True:
            data=self.c.recv(1024)
            if data==b'--':
                print("上传成功")
                break
            fd.write(data)
        fd.close()

#封装并发网络模型
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)
print('listen to the port:',PORT)
#等待接收客户端连接
def main():
    while True:
        #客户端连接途中异常处理
        try:
            #等待客户端连接
            c,addr=s.accept()
        except KeyboardInterrupt:
            s.close()
            sys._exit('服务器退出')
        except Exception as e:
            print("服务端异常:",e)
            continue
        print("连接客户端：",addr)

        #创建子进程
        pid=os.fork()
        if pid==0:
            #防止僵尸进程出现，创建二级子进程
            pid=os.fork()
            if pid==0:
                s.close()#关闭不用的套接字，不影响父进程的使用
                #处理客户端请求
                ftp=ftpserver(c)#创建对象
                while True:
                    #接收请求
                    data=c.recv(1024).decode()
                    if not data or data[0]=='q':
                        c.close()
                        sys.exit("客户端退出")
                    elif data[0]=='l':
                        ftp.do_list()
                    elif data[0]=='p':
                        filename=data.split(' ')[-1]
                        ftp.do_put(filename)
                    elif data[0]=='g':
                        filename=data.split(' ')[-1]
                        ftp.do_get(filename)
            else:
                os._exit(0)
        else:
            c.close()
            os.wait()
main()
from socket import *
import os,sys
import time

#具体的请求功能
class ftpclinet(object):
    def __init__(self,s):
        self.s=s
    def do_list(self):
        self.s.send(b"l")#发送请求
        #等待回复
        data=self.s.recv(1024).decode()
        if data=='ok':
            data=self.s.recv(4096).decode()
            files=data.split('#')
            for file in files:
                print(file)
        else:
            print(data)#打印无法操作的原因
    def do_quit(self):
        self.s.send(b'q')
        self.s.close()
        sys.exit("谢谢使用")
    #下载文件
    def do_get(self,filename):
        self.s.send(('g'+filename).encode())
        data=self.s.recv(128).decode()
        if data=='ok':
            fd=open('filename','wb')
            while True:
                data=self.s.recv(1024)
                if data==b'##':
                    break
                fd.write(data)
            fd.close()
        else:
            print(data)
    #上传文件
    def do_put(self,filename):
        try:
            print("正查看文件")
            f=open(filename,'rb')
        except Exception:
            print("没有找到文件")
            return
        self.s.send(('p '+filename).encode())
        data=self.s.recv(128).decode()
        if data=='ok':
            while True:
                data=f.send(1024)
                if not data:
                    time.sleep(0.1)
                    self.s.send(b'--')
                    break
                self.s.send(data)
            f.close()
            print("上传完毕")
        else:
            print(data)    
#网络连接
def main():
    if len(sys.argv)<3:
        print('argv is error')
        return
    HOST=sys.argv[1]#地址
    PORT=int(sys.argv[2])#端口
    ADDR=(HOST,PORT)
    s=socket()
    try:
        s.connect(ADDR)
    except Exception as e:
        print("连接服务器失败：",e)
        return

    ftp=ftpclinet(s)#创建对象
    while True:
        print('\n========命令选项==========')
        print('\n======   list   ========')
        print('\n====== get file ========')
        print('\n====== put file ========')
        print('\n======   quit   ========')
        print('\n========================')
        cmd=input('输入命令：')
        s.send(cmd.encode())
        if cmd.strip()=='list':
            ftp.do_list()
        elif cmd.strip()=='quit':
            ftp.do_quit()
        elif cmd[:3]=='put':
            #上传文件
            filename=cmd.split(' ')[-1]
            ftp.do_put(filename)
        elif cmd[:3]=='get':
            filename=cmd.split(' ')[-1]
            ftp.do_get(filename)

        else:print("请输入正确命令")
        
main()
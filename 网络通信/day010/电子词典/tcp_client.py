from socket import *
import os,sys
import getpass

def main():
    #终端填写地址
    if len(sys.argv)<3:
        print('argv is error')
        return
    host=sys.argv[1]
    port=int(sys.argv[2])
    addr=(host,port)
    #创建套接字
    s=socket()
    while True:
        try:
            s.connect(addr)
            print("连接成功")
        except Exception as e:
            print(e)
            return
        #进入一级界面
        while True:
            print('''
            =========welcome========
            --1.注册  2.登录  3.退出--
            ''')
            cmd=input('输入选项>>')
            if cmd not in ['1','2','3']:
                print("请输入正确选项")
                sys.stdin.flush()#清除标准输入
                continue
            elif cmd=='1':
                do_register(s)#注册功能
            elif cmd=='2':
                do_logon(s)
            elif cmd=='3':
                s.send(b"q")
                s.close()
                sys.exit("客户端退出")
            else:
                print("退出")
                return
    s.close()
#注册功能
def do_register(s):
    while True:
        try:
            name=input("用户名：")
            if not name:
                break
            passwd=getpass.getpass()
            passwd1=getpass.getpass('再输入一次：')
            if (' ' in name) or (' ' in passwd):
                print("用户名或密码不能有空格")
                continue
            if passwd !=passwd1:
                print("两次密码不一致，请重新输入")
                continue
            msg='r %s %s'%(name,passwd)
        except KeyboardInterrupt:
            s.close()
            return
        #发送请求
        s.send(msg.encode())
        #等待回复
        data=s.recv(128).decode()
        if data=='ok':
            print("注册成功")
            do_logon(s)#注册成功，直接进入登录界面
        elif data=='exists':
            print("用户已存在")
        else:
            print('注册失败')
#登录
def do_logon(s):
    name=input("用户名：")
    passwd=getpass.getpass()
    msg='d %s %s'%(name,passwd)
    #发送请求
    s.send(msg.encode())
    #等待回复
    data=s.recv(128).decode()
    if data=='ok':
        print("登录成功")
        do_loghome(s,name)
    else:
        print('登录失败')
#二级菜单
def do_loghome(s,name):
    while True:
        print('''
            ===========welcome2==========
            --1.查单词  2.历史记录  3.注销--
            ''')
        cmd1=input('输入选项>>')
        if cmd1 not in ['1','2','3']:
            print("请输入正确选项")
            sys.stdin.flush()#清除标准输入
            continue
        elif cmd1=='1':
            do_select(s,name)#查询功能
        elif cmd1=='2':#查询历史记录
            do_hist(s,name)
        elif cmd1=='3':#注销
            break
        else:
            print("请输入正确的选项")
            continue
#查询
def do_select(s,name):
    while True:
        print("查询中")
        word=input("请输入你查询的单词：")
        if not word:
            return
        msg='c %s %s'%(word,name)
        s.send(msg.encode())
        #等待回复
        data=s.recv(1024).decode()
        if data=='on':
            print("没有这个单词,请重新输入")
        else:
            print(data)
#查询记录
def do_hist(s,name):
    while True:
        word=input("请输入你想要查询记录的用户：")
        if not word:
            return
        msg='h '+word
        s.send(msg.encode())
        data=s.recv(128).decode()
        if data=='no':
            print("此用户没有任何查询记录")
        else:
            print(data,end='\n')
        
main()
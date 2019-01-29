from socket import *
import os,sys
import pymysql
import time
import signal


#定义一些全局变量
DICT_TEXT='dict.txt'
HOST='0.0.0.0'
PORT=8888
ADDR=(HOST,PORT)


def client_handler(c,db,addr):
    while True:
        try:
            #处理接收到的消息
            data=c.recv(1024).decode()
            if data[0]=='r':
                #注册
                do_register(c,db,data)
            elif data[0]=='d':
                #登录
                do_logon(c,db,data)
            elif data[0]=='c':
                #查询
                do_select(c,db,data)
            elif data[0]=='h':
                #查询历史记录
                do_hist(c,db,data)
            elif data[0]=='q':
                c.close()
                sys.exit("退出服务器")
        except IndexError:
            break
#注册
def do_register(c,db,data):
    l=data.split(' ')
    name=l[1]
    passwd=l[2]
    cursor=db.cursor()
    sql="select * from user where name='%s'"%name
    cursor.execute(sql)
    r=cursor.fetchone()#查询结果
    #如果查询结果不为空，则用户已存在
    if r !=None:
        c.send(b'exists')
        return
    #插入用户
    sql="insert into user (name,passwd) values('%s','%s')"%(name,passwd)
    print("插入成功")
    try:
        cursor.execute(sql)
        db.commit()
        c.send(b'ok')
    except Exception:
        db.rollback()
        c.send(b'fail')
#登录
def do_logon(c,db,data):
    l=data.split(' ')
    name=l[1]
    passwd=l[2]
    cursor=db.cursor()
    sql="select * from user where name='%s'and passwd='%s'"%(name,passwd)
    #查找用户
    cursor.execute(sql)
    r=cursor.fetchone()#查询结果
    #如果查询结果不为空，则用户已存在,可以登录
    if r ==None:
        print("登录失败")
        c.send(b'on')
    else:
        print("登录成功:",name)
        c.send(b'ok')
#查询
def do_select(c,db,data):
    l=data.split(' ')
    word=l[1]
    name=l[2]
    cursor=db.cursor()
    sql="select interpret from words where word='%s'"%word
    cursor.execute(sql)
    r=cursor.fetchone()#查询结果
    #如果查询结果不为空，就表示已查询到结果
    if r ==None:
        c.send(b'on')
        return
    else:
        #查询的记录插入hist表
        c.send("".join(r).encode())
        sql1 = '''insert into hist(name,word,time) values('%s','%s','%s')'''%(name,word,time.ctime()[11:19])
        try:
            cursor.execute(sql1)
            #提交事物（只有修改表才能提交）
            db.commit()
        except Exception:
            #插入失败就回滚到插入前
            db.rollback()
#查询记录
def do_hist(c,db,data):
    while True:
        #把接收到的消息以空格切分开
        n=data.split(' ')
        name=n[1]
        #创建数据库游标
        cursor=db.cursor()
        sql='''select * from hist where name='%s' '''%name
        #执行mysql语句
        cursor.execute(sql)
        r=cursor.fetchall()#查询结果
        if not r:
            c.send(b'no')
            return
        else:
            for x in r:
                msg="姓名：%s  年龄：%s  时间：%s"%(x[1],x[2],x[3])
                c.send(str(r).encode())
def main():
    #创建数据库连接
    db=pymysql.connect('localhost','root','123456','dict')
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    #处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    while True:
        try:
            c,addr=s.accept()#等待客户端连接
            print('客户端：',addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit("退出服务器")
        except Exception as e:
            print("error:",e)
            continue
        pid=os.fork()
        if pid==0:
            #子进程处理客户端请求
            pid=os.fork()
            if pid==0:
                s.close()#关闭没用的套接字
                client_handler(c,db,addr)#子进程函数
                sys.exit(0)
            else:
                c.close()
        elif pid>0:
            #父进程等待下一个客户端连接
            pass

main()
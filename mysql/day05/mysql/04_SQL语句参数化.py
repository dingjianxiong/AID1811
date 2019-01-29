'''sql语句参数化'''
import pymysql

db = pymysql.connect(host="localhost",
                     user="root",
                     password="123456",
                     database="db5",
                     charset="utf8",
                     port=3306)
cur = db.cursor()
# 接收用户从终端的输入
sid = input("请输入ID号:")
sname = input("请输入姓名:")
sscore= input("请输入成绩:")
# 定义sql命令的变量
# '%s'占位,后用　%()补位,此方法不推荐
# ins = "insert into t1 values('%s','%s','%s')" % (sid,sname,sscore)
ins = 'insert into t1 values(%s,%s,%s)'
L = [sid,sname,sscore]
try:
    # 必须用列表进行传参,execute的第2个参数
    cur.execute(ins,L)
    db.commit()
    print("ok")
except Exception as e:
    db.rollback()
    print("Failed",e)

cur.close()
db.close()



















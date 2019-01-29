'''在db5库的t1表中添加　修改　删除1条记录'''
import pymysql

# 利用pymysql模块的connect创建数据库连接对象
db = pymysql.connect(host="localhost",
                     user="root",
                     password="123456",
                     database="db5",
                     charset="utf8",
                     port=3306)
# 利用连接对象的cursor方法创建游标对象
cur = db.cursor()
# 利用游标对象的execute方法执行sql命令
ins = 'insert into t1 values(6,"陶渊明",80)'
upd = 'update t1 set score=100 where name\
       ="李白"'
dele = 'delete from t1 where name="李清照"'
try:
    cur.execute(ins)
    cur.execute(upd)
    cur.execute(dele)
    # 以上命令都执行成功则commit(),否则rollback()
    db.commit()
    print("ok")
except Exception as e:
    db.rollback()
    print("Failed",e)

# 关闭游标对象
cur.close()
# 断开数据库连接
db.close()











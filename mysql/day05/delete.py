# delete.py
# pymysql 删除示例

import pymysql
from db_conf import *#导入配置

try:
    #连接数据库
    conn=pymysql.connect(host,user,password,dbname)
    #获取游标
    cursor=conn.cursor()
    #执行sql语句
    sql='''delete from acct
    where acct_no='62551122202'
    '''
    cursor.execute(sql)#执行sql语句
    conn.commit()#提交事物
    print('删除笔数：%d' % cursor.rowcount)
except Exception as e:
    print("数据库删除异常")
    print(e)
finally:
    cursor.close()
    conn.close()
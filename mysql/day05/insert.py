# insert.py
# pymysql的插入示例
import pymysql
from db_conf import *#导入配置

try:
    #连接数据库
    conn=pymysql.connect(host,user,password,dbname)
    #获取游标
    cursor=conn.cursor()
    #执行sql语句
    sql='''insert into
    acct(acct_no,acct_name,aust_no,acct_type,reg_date,status,balance)
    values('625511000010','robert','C009',1,now(),1,3.00)
    '''
    cursor.execute(sql)#执行sql语句
    conn.commit()#提交事物
    print('插入成功')
except Exception as e:
    print("数据库插入异常")
    print(e)
finally:
    cursor.close()
    conn.close()
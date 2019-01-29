#pymysql查询示例
#   3、pymysql使用流程
# --         导入模块：
import pymysql
# --     1、数据库连接对象 ：db = pymysql.connect(...)
#
host='localhost'  #服务器地址
user='root'       #登录用户名
password='123456' #登录密码
dbname='bank'     #指定数据库
conn=pymysql.connect(host,user,password,dbname)
# --     2、游标对象 ：cur = db.cursor()
#对象获得游标
cursor=conn.cursor()
# --     3、执行命令 ：cur.execute('SQL命令')
#利用cursor对象，执行sql语句
sql='select * from acct'
cursor.execute(sql)  #执行sql语句
#取出查询结果，并打印
# result=cursor.fetchall()#取一笔数据
# for x in result:
#     print(x)
result=cursor.fetchmany(2)#取两笔数据
print(result)
# result=cursor.fetchall()#取出数据
# for x in result:
#     acct_no=x[0]  #账户
#     acct_name=x[1]#户名
#     if x[6]:  #判断是否为空
#         balance=float(x[6])  #余额
#     else:
#         balance=0.00#余额为空设置为0
#     print('账户：%s,户名：%s,余额：%.2f'  %  (acct_no,acct_name,balance))
# --     4、提交事物（如果需要增删改）     ：db.commit()
# --     5、关闭游标 ：cur.close()
cursor.close()
# --     6、断开连接 ：db.close()
conn.close()

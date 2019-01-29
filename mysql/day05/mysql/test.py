# 从mysqlpython模块中导入类 MysqlPython
from mysqlpython import MysqlPython

# 创建对象
sqlh = MysqlPython()
upd = 'update t1 set score=100'
sqlh.zhixing(upd)

sname = input("请输入要查询的名字:")
sele = 'select score from t1 where name=%s'
result = sqlh.All(sele,[sname])
# result : ((100.0,),)
print("%s的成绩为:%s" % (sname,result[0][0]))











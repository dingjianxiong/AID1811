import pymysql

# 创建2个对象
db = pymysql.connect(host="localhost",
                     user="root",
                     password="123456",
                     charset="utf8",
                     port=3306)
cur = db.cursor()

# 执行sql命令
cur.execute('use db5')
# 定义查询语句变量
sel = 'select * from t1'
try:
    cur.execute(sel)
    # fetchone方法
    One = cur.fetchone()
    print(One)
    print("*" * 40)
    # fetchmany方法
    Many = cur.fetchmany(4)
    for m in Many:
        # (2, '杜甫', 90.0)
        print(m[1],m[2])
    print("*" * 40)
    # fetchall方法
    All = cur.fetchall()
    print(All[0][2])
except Exception as e:
    print("Failed",e)

cur.close()
db.close()















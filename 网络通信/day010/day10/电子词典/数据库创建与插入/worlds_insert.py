import pymysql

import pymysql
host = 'localhost'  #服务器地址
user = 'root'      #d登录用户名
password = '123456'  #登录密码
dbname = 'dict'   #指定数据库

try:
    db = pymysql.connect(host,user,password,dbname)
    cur = db.cursor()
    f = open('dict.txt')
    for line in f:
        tmp = line.split(' ')
        world = tmp[0]
        interpret = ' '.join(tmp[1:]).strip()
        print(world)
        print(interpret)
        sql = '''insert into words(word,interpret) values("%s","%s")'''%(world,interpret)
        cur.execute(sql)
        db.commit()
    print('insert ok')
except Exception as e:
    print('数据库插入异常')
    print(e)
finally:
    cur.close()
    f.close()
    db.close()


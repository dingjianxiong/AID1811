import pymysql

class MysqlPython:
    def __init__(self,host="localhost",
                      user="root",
                      password="123456",
                      database="db5",
                      charset="utf8",
                      port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.port = port

    # 定义open方法,创建2个对象
    def open(self):
      self.db = pymysql.connect(host=self.host,
                          user=self.user,
                          password=self.password,
                          database=self.database,
                          charset=self.charset,
                          port=self.port)
      self.cur = self.db.cursor()

    # 定义close方法,关闭2个对象
    def close(self):
      self.cur.close()
      self.db.close()

    # db = MysqlPython()
    # db.zhixing('insert into (%s,%s)',[n1,n2])
    def zhixing(self,sql,L=[]):
        self.open()
        self.cur.execute(sql,L)
        self.db.commit()
        self.close()

    def All(self,sql,L=[]):
        self.open()
        # 执行查询语句
        self.cur.execute(sql,L)
        # 取出查询结果
        result = self.cur.fetchall()
        self.close()
        return result











from pymongo import MongoClient

#创建数据库连接
conn=MongoClient('localhost',27017)

#创建数据库对象
db=conn.stu
myset=db.class0

#数据库操作
#创建索引
# index_name=myset.create_index('name')
# index_name=myset.create_index([('age',-1)],name='Age')
# print(index_name)

#创建特殊类型的索引
# myset.create_index([('name',1),('age',-1)],sparse=True,unique=True)

#删除索引
# myset.drop_index('name_1')
#删除所有索引
# myset.drop_indexes()

#查看索引
# for i in myset.list_indexes():
#     print(i)


#聚合操作
# l=[
#     {'$group':{'_id':'$gender','num':{'$sum':1}}}
# ]
# cursor=myset.aggregate(l)
# for i in cursor:
#     print(i)

#关闭连接
conn.close()
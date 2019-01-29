from pymongo import MongoClient
from random import randint

#创建数据库连接
conn=MongoClient('localhost',27017)

#创建数据库对象
db=conn.stu
myset=db.class0#并进入某个集合

#数据库操作
# １、将没有性别域的文档删除
# myset.delete_many({'gender':{'$exists':False}})

# ２、给所有文档增加一个域
#         分数取值范围６０－１００（随机整数）
#         {'chinese':99,'math':89,'English':63}
# cursor=myset.find()
# for i in cursor:
    # myset.update_one({},{'$set':{'chinese':randint(60,100),'math':randint(60,100),'English':randint(60,100)}})
    # myset.update_one({'_id':i['_id']},{'$set':{'score':{'chinese':randint(60,100),'math':randint(60,100),'English':randint(60,100)}}})
# ３、聚合操作，查看所有女生的英语成绩排序，不显示_id项
l=[{'$match':{'gender':'w'}},{'$sort':{'score.english':1}},{'$project':{'_id':0}}]
sorcor=myset.aggregate(l)
for i in sorcor:
    print(i)
#关闭连接

conn.close()
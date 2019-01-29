from pymongo import MongoClient
import bson.binary

conn=MongoClient('localhost',27017)
db=conn.txt
myset=db.fie

# #读取文件
# with open('./dict.txt','rb') as f:
#     data=f.read()
# #转换mongodb格式
# content=bson.binary.Binary(data)

# #将内容插入集合
# doc={'filename':'dict.txt','data':content}
# myset.insert_one(doc)

#获获取文件
txt=myset.find_one({'filename':'dict.txt'})
with open('fie.txt','wb') as f:
    f.write(txt['data'])
#关闭
conn.close()

作业
    １、整理复习mongodb数据库内容，和mysql对比总结
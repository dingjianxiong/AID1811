from pymongo import MongoClient

#创建数据库连接
conn=MongoClient('localhost',27017)

#创建数据库对象
db=conn.stu

#创建集合对象(没有这个集合会自动生成)
myset=db['class4']

#操作数据
#插入数据
# print(dir(myset))
# myset.insert_one({'name':'张铁林','king':'乾隆'})
# myset.insert_many([{'name':'张国立','king':'康熙'},{'name':'陈道明','king':'康熙'}])
# myset.insert({'name':'唐国强','king':'雍正'})
# myset.insert([{'name':'陈建斌','king':'雍正'},{'name':'聂远','king':'乾隆'}])
#save()插入数据，_id相同时，会替换原有内容
# myset.save({'_id':1,'name':'郑少秋','king':'乾隆'})

#查找数据(所有的字符串都加引号)

#获取游标对象
# cursor=myset.find({'name':{'$exists':True}},{'_id':0})

#查找叫陈道明的或演过乾隆　的
# dic=({'$or':[{'king':'乾隆'},{'name':'陈道明'}]})
# #直接返回查找到的字典
# d=myset.find_one(dic)
# print(d)


# print(cursor)

# 循环获取每一条文档
# for i in cursor:
#     print(i['name'],'---',i['king'])
# print(cursor.next())#获取下一个文档

#跳过第一个，取后面三个数据
# for i in cursor.skip(1).limit(3):
#     print(i)

#按name排序，python的用法如下：
#注意　排序写法同mongo shell不同，用元组表达
# for i in cursor.sort([('name',1)]):
#     print(i)

#修改操作：
#将第一个为乾隆的人插入玄烨
# myset.update_one({'king':'康熙'},{'$set':{'king_name':'玄烨'}},upsert=True)

#将所有king为q乾隆的人插入'king_name':'弘历'
# myset.update_many({'king':'乾隆'},{'$set':{'king_name':'弘历'}})

#删除操作

#删除第一个为乾隆的
# myset.delete_one({'king':'乾隆'})

#删除所有没有'king_name'域的
# myset.delete_many({'king_name':{'$exists':False}})

#复合操作
print(myset.find_one_and_delete({'name':'郑少秋'}))
#关闭连接
conn.close()
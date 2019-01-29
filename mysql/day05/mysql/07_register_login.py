from mysqlpython import MysqlPython
from hashlib import sha1

sqlh = MysqlPython()
# 注册功能

# # 让用户输入用户名
# uname = input("请输入注册用户名:")
# # 到user表中查询此用户信息
# sele = 'select name from user where name=%s'
# r = sqlh.All(sele,[uname])
# # r为元组
# if len(r) != 0:
#     print("该用户已存在")
# else:
#     # 输入密码
#     pwd1 = input("请输入密码:")
#     pwd2 = input("请再次输入密码:")
#     if pwd1 == pwd2:
#         # 把密码加密存入数据库
#         #　1.创建sha1加密对象
#         s = sha1() 
#         # 2.加密,参数一定要为bytes数据类型
#             # encode : 字符串　－> 字节流
#             # decode : 字节流　－> 字符串
#         s.update(pwd1.encode("utf-8"))
#         # 3.返回十六进制加密结果
#         pwd = s.hexdigest()
#         ins = 'insert into user values(%s,%s)'
#         sqlh.zhixing(ins,[uname,pwd])
#         print("注册成功")
#     else:
#         print("两次密码不一致")

# 登录功能
# 接收用户输入的用户名和密码
uname = input("请输入用户名:")
pwd = input("请输入密码:")
# 到数据库查询该用户密码,查看是否为空
sele = 'select password from user where \
        name=%s'
r = sqlh.All(sele,[uname])
# r:(('7c4a8d09ca3762af61e59520943dc26494f8941b',),)
# 对pwd进行sha1加密
s = sha1()
s.update(pwd.encode("utf-8"))
pwd = s.hexdigest()

if len(r) == 0:
    print("用户名错误")
# r[0][0]取出来的为数据库中密码字段的字符串
elif pwd == r[0][0]:
    print("登录成功")
else:
    print("密码错误")









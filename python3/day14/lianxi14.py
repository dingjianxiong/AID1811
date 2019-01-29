# 练习:
#   写一个函数 get_score() 来获取学生输入的成绩(0~100的整数)
#     如果输入出现异常,则此函数返回0,否则返回用户输入的成绩
#     如:
#       def get_score():
#           ....  # 此处自己实现

#       score = get_score()
#       print("学生的成绩是:", score)
# #示例一
# def get_score():
#     a=int(input("请输入学生的成绩："))
#     if 0<=a<=100:
#         return a
#     return 0

# try:
#     score = get_score()
#     print("学生的成绩是:", score)
# except ValueError as err:
#     print("输入成绩失败")
# except:
#     print("输入成绩失败")
# finally:
#     print("学生成绩录入正常")

# # 示例二
# def get_score():
#     try:
#         a=int(input("请输入学生的成绩："))
#     except ValueError:
#         return 0
#     if 0<=a<=100:
#         return a
#     return 0
# score = get_score()
# print("学生的成绩是:", score)


# 练习:
#   写一个函数 get_age() 用来获取一个人的年龄信息
#     此函数规定用户只能输入 1~140之间的整数,如果用户输入其它
#     的数则直接触发ValueError类型的错误!
#     如:
#         def get_age()
#             ...  # 此处自己实现
#         try:
#             age = get_age()
#             print("用户输入的年龄是", age)
#         except ValueError as err:
#             print("获取年龄时发生错误,错误的原因是", err)
# def get_age():
#     a=int(input("请输入年龄："))
#     if a<1 or a>140:
#         error=ValueError("输入的年龄超出范围：",a)
#         raise error#触发一个ValueError类型错误对象
#     return a
# try:
#     age = get_age()
#     print("用户输入的年龄是", age)
# except ValueError as err:
#     print("获取年龄时发生错误,错误的原因是", err)        


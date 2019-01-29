#try_except.py
#此示例示意try_except语句来捕获异常
# def div_apple(n):
#     print("%d个苹果你想分给几个人？" % n)
#     s=input("请输入人数：")
#     count=int(s) #可能会触发VlaueError错误
#     result=n/count#可能会发生ZeroDivisionError错误
#     print("每个人分了",result,"个苹果")
# try:
#     div_apple(10)
#     print("分苹果成功")
# # except ValueError as err:
# #     print("分苹果失败，err=",err)
# # except ZeroDivisionError:
# #     print("没有人来分苹果，苹果被收回！")
# except (ZeroDivisionError,ValueError) as err:
#     print("分苹果失败，苹果被收回！","\n失败原因：",err)
# else:
#     print("未发生异常语句")
# # div_apple(10)
# # print("分苹果成功")
# print("程序正常结束")


# #示例二
# def div_apple(n):
#     print("%d个苹果你想分给几个人？" % n)
#     s=input("请输入人数：")
#     count=int(s) #可能会触发VlaueError错误
#     result=n/count#可能会发生ZeroDivisionError错误
#     print("每个人分了",result,"个苹果")
# try:
#     div_apple(10)
#     print("分苹果成功")
# # except ValueError as err:
# #     print("分苹果失败，err=",err)
# # except ZeroDivisionError:
# #     print("没有人来分苹果，苹果被收回！")
# except (ZeroDivisionError) as err:
#     print("分苹果失败，苹果被收回！","\n失败原因：",err)
# except:
#     print("除ZeroDivisionError以外的错误发生了")
#     print("错误已捕获")
# else:
#     print("未发生异常语句")
# # div_apple(10)
# # print("分苹果成功")
# print("程序正常结束")

#示例三
def div_apple(n):
    print("%d个苹果你想分给几个人？" % n)
    s=input("请输入人数：")
    count=int(s) #可能会触发VlaueError错误
    result=n/count#可能会发生ZeroDivisionError错误
    print("每个人分了",result,"个苹果")
try:
    div_apple(10)
    print("分苹果成功")
# except ValueError as err:
#     print("分苹果失败，err=",err)
# except ZeroDivisionError:
#     print("没有人来分苹果，苹果被收回！")
except ZeroDivisionError as err:
    print("分苹果失败，苹果被收回！","\n失败原因：",err)
except ValueError as err:
    print("分苹果失败，苹果被收回！","\n失败原因：",err)
except:
    print("除ZeroDivisionError、ZeroDivisionError以外的错误发生了")
    print("错误已捕获")
else:
    print("未发生异常语句,一切正常")
finally:
    print("我是try里的finally语句，无论发生错误或正常，我一定会被执行，")
# div_apple(10)
# print("分苹果成功")
print("程序正常结束")
#raise.py
# def make_excpt():
#     print("开始...")
#     # raise ValueError#触发ValueError类型的异常
#     # raise ZeroDivisionError
#     error=ValueError("xxx大街YYY号着火了！")
#     raise error#触发一个ValueError类型错误对象
#     print("结束！！！")
# try:
#     make_excpt()
#     print("make_excpt调用完成")
# except ValueError as err:
#     print("收到ValueError类型的错误通知")
#     print("err=",err)
# except ZeroDivisionError:
#     print("收到ZeroDivisionError类型的错误通知")
# print("程序正常结束")

#示例2
#此示例示意 用raise语句来传递错误信息
# def f1():
#     n=int(input("请输入整数："))
# def f2():
#     try:
#         f1()
#     except ValueError as err:
#         print("f1函数内出错")
#         print("f2里的err=",err)
#         raise
# try:
#     f2()
# except ValueError as err:
#     print("f2内发生了ValueError类型的错误")
#     print("err=",err)


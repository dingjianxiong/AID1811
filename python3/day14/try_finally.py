# try-finally语句
#   语法:
#     try:
#         可能触发异常的语句
#     finally:
#         最终语句
#   说明:
#     finally子句不可以省略
#     一定不存在except 子句
#   作用:
#     通常用try-finally语句来做触发异常时必须要处理的事情,无论
#     异常是否发生,finally子句都会被执行
#   注:
#     try-finally语句不会改变程序的正常/异常状态

#此示例以煎鸡蛋的控制程序来示意try_finally语句用应用
# 场景与作用
def fry_egg():
    print("打开天然气...")
    try:
        try:
            count=int(input("请输入鸡蛋个数："))
            print("完成煎鸡蛋，共煎了%d个鸡蛋！" % count) 
        finally:#保证语句一定会执行，做必须要做的事
            print("关闭天然气")#可能会出现问题
    except:
        print("煎鸡蛋失败")

fry_egg()
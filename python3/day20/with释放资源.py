# with 语句(用于文件)
#   语法:
#     with 表达式1 [as 变量1], 表达式2[ as 变量2], ...:
#         语句块
#   作用:
#     使用于对资源进行访问的场合,确保使用中不管是否发生异常,都
#     会执行必须的"清理"操作,并释放资源,如:
#        文件使用后自动关闭,线程中锁的自动获取和释放等(线程后面
#         会学)
#   说明:
#     执行表达式,用as 子句中的变量绑定生成的对象
#     with语句同try-finally类似,它并不改变程序的异常状态
try:
    fr=open("test.txt","r")
    try:
        for line in fr:
            print(line)
            # 3/0
    finally:
        fr.close()
except OSError:
    print("文件打开失败")
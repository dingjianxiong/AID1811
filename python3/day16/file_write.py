# #此示例示意打开一个文本文件，并向里面写入内容
# try:
#     fw=open("mynote.text","w")#创建文件并写
#     # 写字符串到文件中。。
#     fw.write("hello")
#     fw.write("world")
#     fw.writelines(["abc","123","中文"])
#     fw.close()
#     print("写入成功")
# except OSError:
#     print("打开文件失败")

# 练习：
#   写一个程序，让用户输入很多正整数，将这些整数存于文件mynumbers.text
#   如：
#     请输入：1
#     请输入：2
#     请输入：3
#   将上一个程序输入的内容从mynumvers文件中读取出来，打印和
def shuru():
    try:
        feil=open("mynumbers.text","w")
        while True:
            a=input("输入正整数：")
            if a=="-1":
                break
            feil.write(str(a))
            feil.write("\n")
    except OSError:
        print("写入失败")
    finally:
        feil.close()
shuru=shuru()
try:
    fr=open("mynumbers.text","r")
    l=[]
    while True:
        s=fr.readline()
        if not s:
            break
        print(s.s)
    


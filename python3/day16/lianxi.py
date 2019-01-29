#练习：
#  自己写个文件 info.text 内部写入如下一些文字信息
#    张三 20 100
#    李四 21 96
#    小王 22 98
#    写程序将这些文件读取出来：
#    张三 今年20岁，成绩是 100
#    李四 今年21岁，成绩是 96
#    小王 今年22岁，成绩是 98


# def read_info(filename):
#   try:
#     myf=open("./info.text")
#     l=[]
#     while True:
#       s=myf.readline()
#       if not s:
#         break
#       s2=s.rstrip()#去掉右边字符
#       n,a,c=s2.split()
#       a=int(a)
#       c=int(c)
#       l.append(dict(name=n,age=a,score=c))
#     myf,close()
#   except OSError:
#     print("打开失败")
# info=read_info("info.text")
# def print_info(info):
#   for d in info:
#     print(d["name"],"今年",
#           d["age"],"成绩",
#           d["score"])


# 练习:
#   1. 写程序,实现文件的复制,(注:只复制文件,不复制文件夹)
#     要求:
#       1) 要考虑文件关闭的问题
#       2) 要考虑超大文件无法一下加载到内存的问题
#       3) 要能复制二进制文件(非文本文件)

def copy(src_file, dst_file):
    '''  src_file : 源文件名
         dst_file : 目标文件名
         返回值: True成功, False 失败
    '''
    try:
        fr = open(src_file, 'rb')
        try:
            fw = open(dst_file, 'wb')
            try:
                while True:
                    b = fr.read(4096)
                    if not b:
                        break
                    fw.write(b)
            finally:
                fw.close()
        finally:
            fr.close()
    except OSError:
        return False
    return True

src = input("请输入源文件名: ")
dst = input("请输入目标文件名: ")
if copy(src, dst):
    print("复制文件成功!")
else:
    print("复制文件失败!")
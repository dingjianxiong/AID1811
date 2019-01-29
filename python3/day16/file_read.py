#此示例示意读取文件myfile.py里的内容
try:
    myf=open("myfile.py")
    print("打开文件成功")
    while True:
        s=myf.readline()
        if not s:
            print("文件读取结束")
            break
        print("读取%d个字符" % len(s),"内容是：",s)
    myf.close()#关闭文件
except OSError:
    print("打开文件失败")
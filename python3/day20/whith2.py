#此示例示意用with语句改写with.py中的try-finall的用法
#用于文件
try:
    # fr=open("test.txt","r")
    with open("test.txt","r") as fr:#是否发生异常，都会关闭fr
        for line in fr:
            print(line)
            3/0
        # fr.read()#出错，fr已经被with语句自动关闭
except OSError:
    print("文件打开失败")
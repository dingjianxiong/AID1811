#学生管理系统
def zhen():
    t=[]
    while True:
        a=input("输入你的姓名：")
        if not a:
            break
        # elif a==w["name"]:
        #     print("名字重复，请重新输入",a)
        b=int(input("输入你的年龄(整数))："))
        c=int(input("输入你的成绩(整数))："))
        l={}
        l["name"]=a
        l["age"]=b
        l["score"]=c
        t.append(l)
    return t

def shan():
    while True:
        nae=input("请输入你想删除的信息：")
        if nae=="":
            break
        for x in w:
            if x["name"]==nae:
                w.remove("删除"，x，"成功")
                return
        else:
            print("删除失败")

def gai():
    while True:
        for x in w:
            xiu=input("请输入修改的姓名")
            if xiu=="":
                break     
            elif x["name"]==xiu:
                ae=input("请输入修改的年龄：")
                sd=input("请输入修改的成绩：")
                x["name"]=xiu
                x["age"]=ae
                x["score"]=sd
def cha1():
    while True:
            ca=input("请输入你查找的名字：")
            if ca=="":
                break
            for x in w:
                if x["name"]!=ca:
                    print("没有此人")
                elif x["name"]==ca:
                    print(x)
            # print(x.get(t,"没有此单词"))

def gaodi():
    
def output_student(w):
    print("+---------------+----------+----------+")
    print("|     姓名      |   年龄   |   成绩    |")
    print("+---------------+----------+----------+")
    for yy in w:
        ww=yy["name"]#拿到列表的名字
        ee=str(yy["age"])
        rr=str(yy["score"])
        print('|'+ww.center(12) +'|'+ ee.center(10) +'|'+ rr.center(10) +'|')
    print("+---------------+----------+----------+")
def main():
    w=[]
    while True:
        print("+-------------------------------+")
        print("| 1) 添加学生信息               |")
        print("| 2) 显示学生信息               |")
        print("| 3) 删除学生信息               |")
        print("| 4) 修改学生成绩               |")
        print("| 5) 按学生成绩高~低显示学生信息|")
        print("| 6) 按学生成绩低~高显示学生信息|")
        print("| 7) 按学生年龄高~低显示学生信息|")
        print("| 8) 按学生年龄低~高显示学生信息|")
        print("| q) 退出                       |")
        print("+-------------------------------+")
        playe=input("请选择你的操作：")
        if playe=="1":
            w+=zhen()
        elif playe=="2":
            output_student(shan(w))   
        elif playe=="3":
            output_student(gai(w))
        elif playe=="4":
            output_student(cha1(w))
            output_student(w)
        elif playe=="5":
            output_student(gaodi(w))
        # elif playe=="6":
        # elif playe=="7":
        # elif playe=="8":    
        elif playe=="q":
            return
        else:
            print("输入错误：")
main()
#输出排列，汉字与单词长度不一
# 查找学生信息：查找失败，
    #   | 5) 按学生成绩高~低显示学生信息 |
    #   | 6) 按学生成绩低~高显示学生信息 |
    #   | 7) 按学生年龄高~低显示学生信息 |
    #   | 8) 按学生年龄低~高显示学生信息 |
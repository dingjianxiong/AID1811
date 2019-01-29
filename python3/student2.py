#
def main():
    global w
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
        a=input("请输入你要的操作：")
        if a=="1":
            w.append(del_zhengjia())
        if a=="2":
            xian_shi(l)
def del_zhengjia():
    global l
    l=[]
    while True:
        a=input("请输入学生姓名:")
        if a=="":
            break
        b=int(input("请输入学生年龄:"))
        c=int(input("请输入学生成绩:"))
        global t
        t={}
        t["name"]=a
        t["age"]=b
        t["score"]=c
        l.append(t)
        return l
def xian_shi(t):
    print("+---------------+----------+----------+")
    print("|     姓名      |   年龄   |   成绩   |")
    print("+---------------+----------+----------+")
    for x in t:
        sn=x["name"]
        sb=int(x["age"])
        sc=int(x["score"])
        print("|"+sn.center(18)+"|"+sb.center(18)+"|"+sc.center(18)+"|")
    print("+---------------+----------+----------+")
        # print("|"+"-"*20+)
main()

# # 索引：
# c=[1,2,3,3,4,7,2,9,5]
# v=c[2]
# c[1]=v#赋值
# del c[2]
# w=list(reversed(c))#反向输出列表
# z=sorted(w)#排序
# s.append(z)
# print(s)

#元组
#表示方式：
# 　　　用小括号()括起来，单个元素括起来后加逗号（，）号区分元组还是单个元素
# 创建空元组：
# 　　　（）　＃创建一个空元组
# 创建非空元组：
# 　　t=100,
#     t=(200,)
#     t=(1,2,3)
#     t=100,200,300
#注：typr(x)函数可以返回ｘ的类型　　type(t)

#元组的构造函数：
# 　　tuple()生成一个空元组
# 　　tuple(iterable) 用可迭代对象生成一个元组
# 示例：
# 　　t=tuple()
#     t=tuple("abc")
#     t=tuple(range(1,10,3))
#     t=tuple([1,3,5,7])
# 元组是可迭代对象
# t=tuple("abc")
# for x in t:
#     print(x)
# l=[x for x in t]
#元组的　ｉｎ／ｎｏｔ　ｉｎ运算符
# 　判断一个值是否在元组中，如果存在返回ｔｒｕｅ，否则返回ｆａｌｓｅ
# 索引　　ｉｎｄｅｘ
# 元组不支持索引赋值
# 切片
# 不能切片赋值

# 元组的方法：
# 　　t.index(v,[,bedin[,end]]),返回对应元素的索引下标, begin为开始索引，
#       end为结束索引,当 value 不存在时触发ValueError错误
#     t.count(x) 	返回元组中元素的个数
# 练习：生成一个０－９的整数的平方的元组，如下：
# 　　　(1,4,9,16....81)
# 方法一
# t=()
# for x in range(1,10):
#     t+=(x**2,)
# print(t)
# 方法二：
# t2=tuple([x**2 for x in range(1,10)])
# print(t2)
# 构造函数：
# 　　str(x)  tuple(x)  list(x)
#  reversed(x) ,　　sorted(x,reverse=False) #用于序列(反转／排序)、
# 字典　　dict
#   1、字典是一种可变的容器，可以存储任意类型的数据
#   ２、字典中每个数据都是用“键”(key)　进行索引，而不像列表（字符串，列表），可以用整数下标进行索引
#   ３、字典数据没有先后顺序关系，字典存储是无序的
#   ４、字典中的数据以键(key)－值（value)对的形式进行映射储存
#   ５、字典的键不能重复，且只能用不可变类型作为字典的键
#   字典的字面值表示方式：
#   　字典是以｛｝括起来，以冒号（：）分割键对，各键之间用逗号分割
#   创建空字典：
#   　　d={}
#   创建非空字典：
#   　d={'姓名':'tarena','年龄'：15}
#     d={'a':{'b':100,'c'；２００}}
#     d={tuple(range(4)):list(range(4))}
#     d={1:"一",2:"二",1:"e"}#重复的只保留最后一个
#     字典的构造函数
#     　　dict()创建一个空的字典　等同于｛｝
# 　　　　dict(iterable) 用可迭代对象初始化一个字典
#        dict(**kwargs)　关键字传参形式生成一个字典
#        示例：
#        　　d=dict()　#d={}
#           l=[(1,2),[3,4],"ab"]
#           d=dict(l)   #d={1:2,3:4,'a':'b'}    
#           d=dict(name='tarena',age=15)
#     注：关键字传参时，关键字名字必须是符合标识符命名规则的，字典输出是无序的

# 字典的键(key)必须是不可变类型：
# 　bool ,int ,float,complex,str,tuple,frozenset(固定集合)和bytes(字节串)和ｎｏｎｅ对象
# 　可变数据类型：
# 　　　list,dict,set(集合)，bytearray(字节数组)
# 字典的键索引：
# 　　用[] 运算符可以获取字典内的“键”对应的值
# 　语法：
# 　　　　v=字典值[键]
# 　示例：
# 　　　d={'name'='tarena','age'=15}
#       print(d["name"],'今年',d['age'],'岁')
#     添加和修改字典的元素
#     语法：
#     　字典[键]＝值
#     说明：
#     　　如果键存在则修改键绑定的值
#     　　如果键不存在，创建键，并绑定键对应的值
# 　　示例：
# 　　　　d={}
#       d=['name']='tarena'#创建'name'键，对应'tarena'
#       d['age']=15#创建'age'键，绑定１５
#       d['age']=15#修改'age'键，绑定为１６
#       print(d)

# del 语句
# 删除字典的键，同时解除与值的绑定关系
# 语法：
# 　　del 字典[键]
# 示例：
# 　d={'name'='tarena','age'=15}
#   del d['name'] #删除’name‘键

# 字典的成员判断　in / not in 运算符
# 　　可以用in 运算符来判断一个键是否存在于字典中，如果存在则返回ｔｒｕｅ，否则返回ｆａｌｓｅ
# 　示例：
# 　　d={1:'一','aaa':'三个ａ'}
#     1 in d   #true
#     "一"in d  #false

# 练习：
# １、将以下信息形成一个字典　seasons
#    '键'　　　　'值'
#    １　　　　　　　'春季有１，２，３月'
#    ２　　　　　　　'夏季有４，５，６'
# 　　３
# 　　４
# ２、让用户输入一个整数代表这个季节，打印这个季节的信息
# 　　如果用户输入的信息不在子弹内，则打印"信息不存在"
# t={1:'春季有１，２，３月',2:"夏季有4，5，6",3:"秋季有7，8，9",4:"冬季有10，11，12"}
# print(t)
# a=int(input("输入整数:"))
# if a in t:
#     print(t[a])
# else:
#     print("不存在")

# 字典的比较：
# 　　> >= < <= == !=
#    == 字典是否完全相同(键和值完全相同)
#    !=与==返回值相反
#    > 

# 
# 练习：
# 　　输入一段字符串,打印出这个字符串中出现过的字符及出现的次数
#   如:
#     输入: ABCDABCABA
#     输出:
#       A: 4次
#       B: 3次
#       D: 1次
#       C: 2次
#       注: 不要求打印的顺序
# 方法一
# a=input("输入：")
# sum=0
# t={}
# for x in a:
#     t[x]=a.count(x)
# for t in t.items():
#     print('%s: %d次'% t)
# 方法二：
# d={}
# for ch in s:
#     if ch in d:
#         d[ch]+=1
#     else:
#         d[ch]=1
# for t in t.items():
#     print('%s: %d次'% t)
# 练习：
# 　　输入一些单词和解释，讲单词作为键，解释作为值存于字典中，当输入单词为空时结束输入
# 　　然后进入查词过程
# 　　输入单词，如果单词在字典中，则显示内容，如果单词不存在，则提示没有此单词
#                                             ssssss
# t={}
# while True:
#     a=input("请输入单词")
#     if  a=="":
#         break
#     b=input("请输入解释")
#     t[a]=b
# print(t)
# while True:
#     w=input("输入你查询的单词：")
#     if w in t:
#         print("解释",t[w])

#字典推导式：
# 　语法：
# 　　　{键表达式：值表达式　for 变量　in 可迭代对象　[if 真值表达式]}
# 　　注：[]代表内部的内容可以省略
# 示例：
# 　　生成一个字典，键为数字（１－９），值为键的平方
# d={x:x**2 for x in range(1,10)}
# print(d)
# 练习:
#   1. 有如下字符串列表
#     L = ['tarena', 'xiaozhang', 'hello']
#     生成如下字典:
#     d = {'tarena': 6, 'xiaozhang': 9, 'hello':5}
#     注:  字典的值为键的长度  
# l=['tarena','xiaozhang','hello']
# d={x:len(x) for x in l}
# print(d)

# 2. 已知有两个等长度的列表list1和lists2, 生成相应字典
#     list1 = [1001, 1002, 1005, 1008]
#     list2 = ['Tom', 'Jerry', 'Spike', 'Tyke']
#     生成的字典为:
#     {'Tom':1001, 'Jerry': 1002, ....}    D.keys()
# list1 = [1001, 1002, 1005, 1008]
# list2 = ['Tom', 'Jerry', 'Spike', 'Tyke']
# d={}
# for i in range(len(list1)):
#     d[list2[i]]=list1[i]
# print(d)

# 字典推导式支持嵌套：
# 　　语法规则同列表推导式
# 字典 VS 列表
#   1. 都是可变对象
#   2. 索引方式不同,列表用整数索引,字典用键索引
#   3. 字典的插入,删除,修改的速度可能会快于列表(重要)
#   4. 列表的存储是有序的,字典的存储是无序的
# 练习：
# 　　１、　有一只小猴子，摘了很多桃：
# 　　　第一天吃了全部的一半，感觉不饱又吃了一个
# 　　　第二天吃了剩下的一半，感觉不饱又吃了一个
# 　　　。。。。　以此类推
# 　　　到了第十天，发现只剩下一个了
# 　　　请问第一天摘了多少桃子
# #最后的桃

# # q=a//2-1#第一天

# q=(a-1)//2-1#第二天l=[x+y for x in [10,20,30]for y in [1,2,3]
# a=1
# sum=0
# while q<10:
#     a=(a+1)*2
#     q+=1
# print(a)

# 　　２、写一个程序，实现一个带有菜单界面的字典程序
# 　　　　菜单如下：
# 　　　　　１、添加单词
# 　　　　　２、删除单词
# 　　　　　３、查找单词
# 　　　　　４、退出   D.keys()   {键表达式：值表达式　for 变量　in 可迭代对象
# l={}
# while True:
#     a={1:"添加单词",2:"删除单词",3:"查找单词",4:"退出"}
#     print(a)
#     b=int(input("请输入你要操作的编号："))
#     if b==1:
#         while True:
#             c=input(a[b]+":")
#             c1=input("输入解释：")
#             if c=="" or c1=="":
#                 break
#             elif c in l:
#                 print("添加失败,单词已存在")
#             c1=input("输入解释：")
#             l[c]=c1
#         print(l)
#     elif b==2:
#         while True:
#             e=input(a[b]+":")
#             if e=="":
#                 break
#             del l[e]
#         print(l)
#     elif b==3:
#         while True:
#             t=input(a[b]+":")
#             if t=="":
#                 break
#             print(l.get(t,"没有此单词"))
#     elif b==4:
#         break


    #  3、项目（学生信息管理程序）
    #  　　任意个学生的信息，形成字典后，存入列表中
    #  　　　　学生信息有：姓名，年龄，成绩
    #  　如：
    #  　　　请输入姓名：
    #  　　　请输入年龄：
    #  　　　请输入成绩：
    #  　　　请输入姓名：
    #  　　　请输入年龄：
    #  　　　请输入成绩：
    #  　　　请输入姓名：回车　　　结束输入
    #  　形成内部存储格式如下：
    #  　　　infos=[{'name':'tarena','age':15,'score':99,
    #               'name':'tarena','age':15,'score':99}]
    #         以表格的方式打印上述列表的内容：
    # +---------------+----------+----------+
    # |     姓名      |   年龄    |   成绩    |
    # +---------------+----------+----------+
    # |    tarena     |   15     |    99    |
    # |    name2      |   20     |    88    |
    # ...........
    # +---------------+----------+----------+
# def zsgc():
#      +-----------------------------+
#       | 1) 添加学生信息               |
#       | 2) 删除学生信息               |
#       | 3) 显示学生信息               |
#       | 4) 修改学生成绩               |
#       | q) 退出                      |
#       +-----------------------------+

# def input_student(w):
def zhen():
    t=[]
    while True:
        a=input("输入你的姓名：")
        if not a:
            break
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
                w.remove(x)
    return w
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
            return w
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
    return w
def output_student(t):
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
    global w
    w=[]
    while True:
        print("+"+"-"*29+"+")
        qw="1:添加学生信息"
        er="2:显示学生信息"
        rt="3:删除学生信息"
        ty="4:修改学生信息"
        yu="q:退出"
        print("|"+qw+" "*(23-len(qw))+"|")
        print("|"+er+" "*(23-len(er))+"|")
        print("|"+rt+" "*(23-len(rt))+"|")
        print("|"+ty+" "*(23-len(ty))+"|")
        print("|"+yu+" "*(27-len(yu))+"|")
        print("+"+"-"*29+"+")
        playe=input("请选择你的操作：")
        if playe=="1":
            w+=zhen()
            print(w)

        elif playe=="2":
            output_student(shan())
            print(w)
        elif playe=="3":
            output_student(gai())
            print(w)
        elif playe=="4":
            output_student(cha1())
            print(w)
            output_student(w)
        elif playe=="q":
            return
        else:
            print("输入错误：")
main()
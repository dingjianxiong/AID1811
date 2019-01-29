# for 语句
# 　　作用：
# 　　　　用来遍历可迭代对象的数据元素
# 　　可迭代对象是指能以此获取数据元素的对象
# 可迭代对象包括：
# 　　　字符串　ｓｔｒ
# 　　　　（后面讲）
# 　　　列表　　ｌｉｓｔ
# 语法：
# 　　ｆｏｒ　变量列表　　ｉｎ　　可迭代对象
# 　　　　　语句块１
# 　　ｅｌｓｅ：
# 　　　　　　语句块２
# 说明：
# 　１、　可迭代对象每次提供一个元素依次赋值给变量列表中的变量，赋值完后执行语句块１
# 　　重复执行此步骤，直到可迭代对象不能提供数据为止
# 　２、可迭代对象迭代完所有元素后，执行ｅｌｓｅ子句的语句块２，然后退出循环
# 　

#    s="abcde"
#      for ch in s:　　　　＃ｃｈ可自定义，绑定一个字符串
#         print("ch",ch)
#     else:
#         print("遍历可迭代对象结束")
# sum=0
# a=input("输入：")
# for b in a:
#     if b==" ":
#        sum+=1
# print("空格",sum)
# sum1=0
# for b in a:
#     if(0<=ord(b)<=127):
#         sum1+=1
# print("英文个数是：",sum1)
#                  #用ｗｈｌｉｅ求空格个数　　　　　　ｓｓｓｓｓ
# a=input("输入：")             #打印ｈｅｌｌｏ，倒着输出
# b=0
# sum=0
# while b<len(a):
#     ch=a[b]       
#     if ch==' ':
#         sum+=1 
#     b+=1  
# print("空格的个数：",sum)

# a=input("输入：")                          #ssss
# for ch in s[::-1]:
#     print(ch)

# range 函数
# 　　　函数　　说明：
# 　　　　range(stop) 用来生成0~stop 区间内的整数，直到ｓｔｏｐ为止，不包含ｓｔｏｐ
# 　　　　range(start,stop[,step]) 用来生成ｓｔａｒｔ～ｓｔｏｐ区间内的整数，直到
# 　　　　　　　ｓｔｏｐ为止（不包含ｓｔｅｐ），每个整数间隔ｓｔｅｐ（ｓｔｅｐ可以为负数
#             但不可以为０
# 　　　作用：
# 　　　　　　用来创建一个生成一系列整数的可迭代对象（也叫整数序列生成器）
# 　　　说明：
# 　　　　　此函数调用返回回来的对象可以用ｆｏｒ语句取值
# 　　　示列：
# 　　　　　range(4) 　#生成０，１，２，３
# 　　　　　range(3,6)  #生成　３，４，５
# 　　　　　range(1,10,2) #生成１，３，５，７，９
# 　　　　　range(5,0,-2) #生成５，３，１
# 　　　　　range(4,0)    #空

# for x in range(1,21):
#     print(x,end=" ")
# print()
# for x in range(1,101):
#     if x*(x+1)%11==8:
#         print(x,end=" ")
# print()

# sum=0
# for x in range(1,100,2):
#     sum+=x
# print(sum)

# for 语句注意事项
# 　１、ｆｏｒ　中的ｒａｎｇｅ的调用次序：
# 　　　　#请问此程序打印结果，
# 　　　　i=6
# for x in range(1,i):
#     print("x=",x,"i=",i)
#     i-=1
#     循环５次，循环次数与ｉ没有关系
# 　２、ｆｏｒ语句内的变量可能不会被创建
# 　　　for x in range(4,0):
#         print(x)
#         else:
#             print("x=",x)  #错误，ｘ不存在，未定义，ｒａｎｇｅ（４，０）未创建
# 　ｆｏｒ语句嵌套：
# 　　　与ｗｈｉｌｅ一样，ｆｏｒ语句是语句（复合语句），他可以嵌套在其他符合语句中
# 示例：
# for x in "abc":
#     for y in "123":
#         print(x+y,end="")
# print()

# a=int(input("输入整数："))
# b=0
# while b<=a-1:
#     for x in range(1,a+1):
#         print(x,end="")
#     print()
#     b+=1

# a=int(input("输入整数："))
# for x in range(1,a+1):  #打印出输入的数range(1,a＋１)１到输入的数
#     for y in range(x,a+x): #
#         print(y,end="")       
#     print()

# continue 语句
# 　　　作用：用于循环语句中，不再执行本次循环内continue
#           之后的语句，重新开始一次循环，
#     １、在ｗｈｉｌｅ语句中执行ｃｏｎｔｉｎｕｅ语句，将会
#     　　跳过真值表达式处，重新判断循环条件
#       2、在ｆｏｒ语句中执行continue时，跳过当前循环，
#　　　　　　重新给变量赋值
#     语法：
#     　　continue

# for x in range(5):
#     if(x==2):
#         continue
#     print(x)

# for x in range(10):
#     if(x%2==1):
#         continue
#     print(x)

# a=1
# while a<=10:
#     if(a%2==1):　　#注意，不能一直成立
#         a+=1       #防止死循环，
#         continue
#     print(a)
#     a+=1

# a=1
# sum=0
# for a in range(1,101):
#     if(a%2==0 or a%3==0 or a%5==0 or a%7==0):
#         continue
#     print(a)
#     sum+=a
# print()
# print(sum)

# 循环小结：
# 　　while 语句
# 　　for  语句
# 　　　　　字符串　str
#         range() 调用后返回的值
#     break 语句(终止循环)
#     continue 语句(开始一次新的循环)

# 列表　list
#    什么是列表：
#    　　列表时一种容器
#    　　列表是可以被改变的序列
#    　　列表是由一系列的特定元素组成，元素与元素之间没有任何关系
#    　　他们之间有先后顺序
# python 序列类型简介
# 　　字符串　　str
#    列表　　　list
#    元组　　tuple
#    字节串　bytes
#    字节数组　bytearray
# 　创建空列表的方式
# 　[] 创建空列表
# 　如：
# 　　　l=[] #l绑定一个空列表
# 创建非空列表的方式
# 　　l=[1,2,3,4]
#    l=['beijing','shanghai','shenzhen']
#    l=[1,"是",3.14,"wwee"]
#    l=[1,2,[3.14,3.2],4]
# 列表的构造函数　list
# 　　list() 生成一个空列表，等同于[]
#    list(iterable) 用可迭代对象创建一个列表
# 　示例：
# 　　　l=list()  #l 绑定空列表
# 　　　l=list("hello") #l绑定['h','e','l','l','o']
#      l=list(range(1,10,2))#l=[1,3,5,7,9]

# 列表的运算：
# 　　　算术运算：＋－* / +=   *=
#   + 　　 用于拼接
# 　＋＝　　用于讲右侧或可迭代对象的数据追加在原列表之后
# 　　　语法：
# 　　　　　x+=可迭代对象
# 　　　如：
# 　　　　　x+=[4,5,6]
#         x+=range(10,13)
#         x+="abc"
#     注：
#     　　列表是可变容器，＋＝会改变原列表
# 　　* 生成重复的列表
# 　　x=[1,2]*3   #x=[1,2,1,2,1,2]
#    *=  用于生成重复的列表
#    x=[1,2,3]
#     x *=2   #x=[1,2,3,1,2,3]
# 列表的比较运算：
# 　　运算符：
# 　　　　　< <= > >= == !=
#    说明：
#    　　列表的比较规则与字符串的比较规则相同
#    　　列表要求每两个元素能以此比较，否则会出现类型错误
#    示例：
#    　　x=[1,2,3]
#        y=[2,3,4]
#        x!=y  #true
#        x<y   #true
#        [1,2,3]<[1,3,2]  #true
#        [1,"two"]>["two",1]# TypeError
#     列表是可迭代对象
# a=[1,2,3,4]
# for x in a:
#     print(x)

# a=input("输入１：")
# b=input("输入１：")
# c=input("输入１：")
# l=[a,b,c]
# print(l)

#ssss
# sum=0
# l=[]
# while True:
#     a=int(input("输入："))
#     if a<0:
#         break    
#     l+=[a]
#     sum+=a
# print(l)
# print(sum)  

# 列表的　ｉｎ　／　　ｎｏｔ　ｉｎ运算符：
# 　　判断一个值是否存在于列表中，如果存在，则返回ｔｒｕｅ，不存在
# 　　返回　ｆａｌｓｅ，
# 　示例：
# 　　　x=[1,"two",3,"四"]
#      3 in x   #true
#      4 in x   #false
#      ５　not in x   #true
#      1 not in x   #false

# 九九乘法表：
# 任意输入一个数，判断这个数是否为素数prime(只能被１和自身整除的正整数)
# 输入一个数代表树干的高度，

# for x in range(1,10):
#     for b in range(1,x+1):   
#         a=x*b
#         print("%s" % b ,"*","%s" % x,"=",a,end=" ")
#     print()

#     1x1=1
#     1x2=2 2x2=4
#     1x3=3 2x3=6 3x3=9
#     ....
#     1x9=9 ..........  9x9=81
# a=1
# b=1
# while a<=9:
#     while b<=a+1:
#         print("%s" % a ,"*","%s" % b,"=",a*b,end=" ")
#         b+=1
#     a+=1
# print()

    
    
  
# #求一个数是不是素数             
# a=int(input("输入："))
# for x in range(2,a): 
#     if a%x==0:
#         print("不是素数")
#         break
#     else:
#         print("是素数")
#         break



# 算出 100 ~ 999 范围内的水仙花数(Narcissistic Number)
#     水仙花数是指百位的3次方 + 十位的3次方 + 个位的3次方 等于原
#     数的整数
#     如:
#       153 = 1**3 + 5**3 + 3**3
#     答案:
#       153, 370, ....

#判断１００到１０００中的水仙花数
# for x in range(1,10):
#     for y in range(0,10):
#         for z in range(0,10):
#             a=x*100+y*10+z*1
#             if (x**3+y**3+z**3)==i:
#                 print(i,"是水仙花数")

# for i in range(100,1000):
#     x=i//100
#     y=(i-x*100)//10
#     z=(i-x*100-y*10)
#     if (x**3+y**3+z**3)==i:
#         print(i,"是水仙花数")
#     i+=1

# 3. 输入一个整数,此整数代表树干的高度,打印一棵如下形状的圣
#     诞树
#     如:
#       输入: 2
#     打印:
#      *
#     ***
#      *
#      *
#     如:
#       输入: 3
#     打印:
#       *
#      ***
#     *****
#       *
#       *

#       *        S.center(width[,fill])  "%7.2f" % pi      # '   3.14' 
# a=int(input("输入整数："))
# b=1
# d=1
# while b<=a:
#     c="*"*b
#     print(" "*(a-b),c+(b-1)*"*"," "*(a-b))
#     b+=1
# while d<=a:
#     print(" "*a+"*")
#     d+=1
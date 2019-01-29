# 字符串的格式表达式
# 　作用：
# 　　　生成一定的格式的字符串
# 　运算符％
# 　语法格式：　
# 　　　　格式化字符串％参数值
# 　　　　格式化字符串％（参数值１，参数值２，。。。）
# 示列：
# 　　fmt="name :%s,age:%d"
    
# 格式化字符串中的占位符和类型码
# 　　占位符和类型码　　　　　　　　意义
# 　　％s         字符串，使用ｓｔｒ（ｘ）函数转换
# 　　％ｒ　　　　　字符串，使用ｒｅｐｒ（ｘ）函数转换
# 　　％ｃ　　　　　　整数转换为单个字符
# 　　％ｄ　　　　　　十进制整数
# 　　％ｏ　　　　　　八进制整数
# 　　％ｘ　　　　　　十六进制整数（字符ａ－ｆ小写）
# 　　％Ｘ　　　　　　十六进制整数（字符Ａ－Ｆ大写）
# 　　％ｅ　　　　　　指数型浮点（ｅ小写），
# 　　％Ｅ　　　　　　指数型浮点（ｅ小写），
# 　　％ｆ　％Ｆ　　　　浮点十进制形式
# 　　％ｇ　％Ｇ　　　　十进制形式浮点或指数浮点自动转换
# 　　％％　　　　　　等同于一个％字符
# 　
# 占位符和类型码之间的格式化语法
# 　% [-+0 宽度.精度]　类型码
# 　说明：
# 　　　－　左对齐（默认为右对齐）
# 　　　＋显示正号
# 　　　0　　左侧空白位置补零
# 　宽度　　整数，整个数据输出的宽度（占用的字符串数）
# 　精度　　整数，保留小数站后多少位（默认为６位）
# 输入三行文字　让这三行文字以此以２０个字符串的宽度右对齐输出
# 　　１、　hello world
#     2、　abcd
#     3   a
# hello  world
#         abcd
#            a
# 能否以最长的字符串长度进行右对齐显示（左侧填充空格）
# a=input("输入第一个：")                                           # ssss
# b=input("输入第二个：")
# c=input("输入第三个：") 
# print("%20s" % a)
# print("%20s" % b)
# print("%20s" % c)     

# 循环语句
# 　　while 语句
    #  作用：
    #  　　根据一定的条件，重复的执行一条语句或多条语句
    #  语法：
    #  　　while 真值表达式:
    #     　　　语句块１（此部分的语句可能会重复执行）
    #     else :
    #          语句块２
    # 　　　说明：
    # 　　　　　１　先执行真值表达式，测试布尔值为true 或false
    # 　　　　　２　如果真值表达式测试为true ，则测试语句块１，然后再返回到第一步，
    # 　　　　　　　重复进行测试
    # 　　　　　３　如果真值表达式测试值为false ，则执行语句块２，然后结束此while语句
    # 　　　　　　　如果没有else子句，则直接结束此while语句的执行
    # 　　示例：
# i=1
# while (i<=5):
#    print("hello")
# i +=1
# a=int(input("输入整数："))
# b=1
# while b<=a:
#     print("这是第%s" % b)
#     b+=1
# else:
#     print("结束")
# a=1
# while a<=20:    
#     print(a,end="  ")
#     a+=1
# else:
#     print()

# b=1
# while b<=20:
#     print(b,end=" ")
#     if (b%5==0):
#         print()
#     b+=1
# else:
#     print()

# i=20
# while i>=1:
#     print(i)
#     i-=1
# else:
#         pass

# begin=int(input("请输入一个整数："))
# end=int(input("请输入一个整数："))
# while (begin<=end):
#     print(begin,end=" ")
#     if(begin%5==0 or begin%5<=1):                           #  ssss
#        print()       
#     begin+=1
# else:
#     print()
# a=int(input("请输入整数："))
# print('*'*a)

# while(1<=a-2):         ＃根据输入的数字打印长方形
#     print("*"+" "*(a-2)+"*")                             #sssss
#     a+=1
# if a>=2:
#    print('*'*a)
#    while 语句注意事项
#    １、　要控制循环的真值表达式来防止死循环
#    ２、　通常用真值表达式内的循环变量来控制循环条件
#    ３、　通常在循环语句块内要改变循环变量来控制循环条件和变量的走向
# a=1
# sum=0
# while (a<=100): 
#     sum+=a
#     a+=1
# else:
#     print(sum)
# while 语句嵌套
# 　　　while 语句本身是语句，和其他语句一样，可以嵌入到任何的复合语句中
# 　示意：
# 　　　while  真值表达式１：
# 　　　　　　.......、
# 　　　　　　while  真值表达式１：
# 　　　　　　　　　.......
#     　　　　else:
#      else:
#         　......
# a=int(input("输入一个数："))
# b=1
# c=1
# while c<=a:
#     while (b<=a):
#       print(b,end=" ")
#       b+=1
#     else:
#       print()                              #  sssss
#     c+=1
# break 语句
# 　　问题：
# 　　　　　如果在循环过程中，不想再继承执行此循环了，怎么办？
# 　　作用：
# 　　　　　用于循环语句（while或for）语句中，用来终止当前循环语句的执行
# 　　语法：
# 　　　　break
#    说明；
#    　　　当ｂｒｅａｋ语句执行后，此循环语ｂｒｅａｋ之后的语句不再执行
#    　　　ｂｒｅａｋ语句通常和ｉｆ语句组合使用
#    　　　ｂｒｅａｋ　语句终止循环时，循环语句的ｅｌｓｅ子句的语句将不会执行
#    　　　ｂｒｅａｋ语句只能终止当前循环语句的执行，如果有循环嵌套时，不会跳出嵌套
#    　　　　　　　　的外重循环
#    　　　ｂｒｅａｋ只能在循环语句（while或for）内部使用
# 死循环　　death Loop
#     死循环是指循环条件一直成立
#     死循环通常用break语句来终止循环
#     死循环的ｅｌｓｅ子句永远不会执行


# sum=0
# while True:
#     a=int(input("输入："))
#     if (a<0):
#         break
#     sum+=a 
# print(sum)

# a=0
# c1=0
# sum=0
# while a<=10000:
#     a+=1       
#     if(a%2==1):
#         c1=1/(2*a-1)
#     else:
#         c1=-1/(2*a-1)
#     sum+=c1
# print(sum)
# print(round(sum*4,2))


# a=int(input("请输入一个数字："))            #sssss
# b=1
# while b<=a:
# #   print("打印如下：")
#     print("*"*b)
#     b+=1
# c=1
# while c<=a:               #"%-10d" % 123  S.strip([chars])   S.strip([chars])
#     print((a-c)*" "+"*"*c)
#     c+=1
# d=1
# while d<=a:               #"%-10d" % 123  S.strip([chars])   S.strip([chars])
#     print((" "*d+(a-d)*"*"))
#     d+=1
# e=1
# while a>0:
#     print("*"*a)
#     a-=1

# A=65
# while (A<90):
#     print(chr(A),end="")                  #SSSSSSSSSSS
#     A+=1
# print()
# C=65
# b=97
# while (b<122 or C<90):
#     print(chr(C)+chr(b),end="")                  #SSSSSSSSSSS 97  122
#     b+=1
#     C+=1
# print()

    
    

    

   


    
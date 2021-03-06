# day01 回顾
#   运算符:
#     复合赋值算术运算符
#       += -=  *=  /= //= %= **=
#     比较运算符
#       <  <=  >  >=  ==  !=
#     布尔运算
#       not    and    or
#     正负号运算符
#       +(正号) -(负号)
#       一元运算符
#         + 表达式        - 表达式
#   表达式:
#     条件表达式
#       表达式1 if 真值表达式 else 表达式2
#   语句:
#     if 语句
#       语句:
#         if 真值表达式1:
#             语句块1
#         elif 真值表达式2:
#             语句块2
#         elif .....:
#             语句块3
#         else:
#             语句块
#     pass 语句

# 函数:
#   类型转换的函数:
#     int(x=0), int('字符串', base=10)
#     float(x)
#     complex(read, image)
#     bool(x)
#   数值形函数:
#     abs(x)
#     round(数字, 近似的位数)
#     pow(x, y, z=None)     x**y  x**y%z
#   帮助函数
#     help(对象/类型/字符串)
#   基本输入输出函数
#     input('提示字符串') 
#     print(values,..., sep=' ', end='\n', flush=False)



# day03笔记
# 字符串 str 
#   作用:
#     用来记录文字(文本)信息
#   字符串的表示方式:
#     在非注释中凡是用引号括起来的部分都是字符串
#       '   单引号
#       "   双引号
#       ''' 三单引号
#       """ 三双引号
#   空字符串的字面值表示方法:
#     ''
#     ""
#     ''''''
#     """"""
#     注: 空字符串的布尔测试值bool(x)为False  

#   非空字符串的表示方式:
#     'hello'
#     "hello"
#     '''hello'''
#     """hello"""

#   单引号和双引号的区别:
#     单引号内的双引号不算结束符
#     双引号内的单引号不算结束符
#   示例:
#     print("I'm a teacher")  # I'm a teacher
#     print('I am "weimingze"')  # I am "weimingze"
  
#   三引号字符串
#     以"""或''' 开头和结尾的字符串
#   作用:
#     三引号内可以包含单引号和双引号
#     三引号字符串中的换行会自动转换为换行符'\n'
#   示例见:
#     str.py

# 隐式字符串字面值拼接
#   多个字符串字面值连在一起时,python解释执行器会自动
#   拼接为一个字符串
#    s = "I'm a teacher!"     'my name "weimingze"'
#    print(s)   # 拼接后的字符串

# 用转义序列代表特殊字符
#   字符串字面值中用字符反斜杠(\) 后跟一个或一些字符代表特
#   殊的一个字符
#     转义格式    含义 
#       \'       单引号(')
#       \"       双引号(")
#       \\       一个反斜杠(\)
#       \n       换行符
#       \r       返回光标至行首(回车符)
#       \f       换页
#       \t       水平制表符
#       \v       垂直制表符
#       \b       倒退
#       \a       响铃
#       \0       空字符(字符值为零)
#       \0oo     oo为两位八进制表示的字符
#       \xXX     XX为两位十六进制表示的字符
#       \uXXXX   XXXX为四位十六进制表示的UNICODE16字符
#       \UXXXXXXXX   XXXXXXXX为八位十六进制表示的
#                    UNICODE32字符
# ASCII编码表
#   Linux 查看方式:
#     $ man ascii 

# 常用ASCII编码:
#   字符    十进制      十六进制
#   '0'     48          0x30
#   'A'     65          0x41
#   'a'     97          0x61

# python3中字符串默认存储的是UNICODE编码值
#   0x0000 ~   (从0 开始)

# 序列的概念
#   字符串是序列
#   序列是指有先后顺序的排列

# 求序列的长度的函数len
#   len(s) 返回字符串中字符的个数

# 练习:
#   得到如下字符串中有几个字符
#     1)   'abcd1234'    # 8个
#     2)   '5\'4"'       # 4个
#     3)   '\"\x34\056'  # 3个
#     4)   '\a\b\c\d'    # 6个
#     5)   '\n\t\r\\'    # 4个


# raw 字符串(原始字符串)
#   格式:
#     r'字符串内容'
#     r"字符串内容"
#     r'''字符串内容'''
#     r"""字符串内容"""
#   作用:
#     让转义符号 \ 无效
#   示例:
#     用字符串形成一个Windows下的路径:
#       C:\newfile\test.py
#     path = 'C:\newfile\test.py'
#     print(path)
#     path = r'C:\newfile\test.py'
#     print(path)  # 打印: C:\newfile\test.py



# 字符串的运算
#   运算符:
#     +    +=    *    *= 
# + 加号运算符用于拼接字符串
#   x = "abcd"
#   y = '1234'
#   z = x + y  # 拼接
#   print(z)
#   a = y + x
#   print(a)

# += 运算符 用原字符串与右侧的字符串拼接生成新的字符串,
#          再用原变量绑定新的字符串
#   如:
#     x = 'abcd'
#     x += '123'
#     print(x)  # abcd123

# * 运算符 生成重复的字符串
#   如:
#     x = "ABCD" * 3
#     print(x)  # ABCDABCDABCD
#     y = 3 * "123" 
#     print(y)  # 123123123
#   注: 字符串只能和整数相乘

# *= 运算符  生成重复的字符串，再用变量重新绑定

#   x = '123'
#   x *= 3   # 等同于 x = x * 3
#   print(x)  # 123123

# 练习:
#   写一个程序，打印一个高度为4行的矩形方框
#   如:
#     请输入框形方框的宽度: 10
#   打印如下:
#     ##########
#     #        #
#     #        #
#     ##########
#   注:  宽度为输入数字的个数个#号
# a=int(input("输入矩形的宽度："))
# def kuan(a):
#     print(a*'#')
#     print('#'+(a-2)*' '+'#')
#     print('#'+(a-2)*' '+'#')
#     print(a*'#')
# kuan(a)
# 字符串的比较运算
#   运算符:
#     <  <=   >   >=  ==  != 
#   规则:
#     依次按编码值进行两两比较，一旦不同，则比较结束,返回比
#     较结果，当编码值和长度完全相同时，两个字符串相等
#   示例：
#     'A' < 'B'       # True
#     'ABC' > 'ABB'   # True
#     'ADC' < 'ABC'   # False
#     'ABC' >= '123'  # True
#     'AD' >= 'ABC'   # True
#     'AB' < 'ABC'    # True
#     'ABC' < 'abc'   # True
#     'abcd' != 'dcba' # True



# in / not in 运算符
#   作用:
#     in 用于序列,字典,集合中,用于判断某个值是否存在于容器
#     中,如果存在则返回True,否则返回False
#     not in 写in 的返回结果相反
#   格式:
#     对象 in 序列
#   示例:
#     x = 'welcome to tarena!'
#     'to' in x  # True
#     'hello' in x  # False
#     'a' in x  # True


# 练习:
#   写一个程序,任意输入一段字符串,判断你的名字是否在这个字符
#   串中,如果存在则打印"您的名字出现了" 否则不予理睬


# 字符串的索引操作
# 索引 index
#   python 字符串是不可以改变的序列

#   语法:
#     字符串[整数表达式]
#   说明:
#     python 序列都可以用索引(index) 访问序列中的元素
#     python 序列的正向索引是从0开始的,第二个索引为1,...
#          最后一个索引为len(s)-1
#     python 序列的反向索引是从-1开始的,-1代表倒数第一个
#          -2 代表倒数第二个,以此类推, 第一个是-len(s)
#   示例:
#     s = 'ABCDE'
#     print(s[1])  # B
#     print(s[-1])  # E

# 练习:
#   写程序,输入一行字符串,打印出下内容:
#     1) 打印这个字符串的第一个字符
#     2) 打印这个字符串的最后一个字符
#     3) 如果这个字符串的长度是奇数,打印中间这个字符
#   注:
#     求字符串长度的函数 len(s)
# a=input('请输入一段字符串：')
# def funcname(ww):
#     print(ww[0])
#     print(ww[len(ww)-1])
#     if len(ww) % 2==1:
#         print(ww[len(ww)//2])
# funcname(a)

# 切片 slice
#   作用:
#     从字符串序列中取出相应的元素重新组成一个字符串序列 
#   语法:
#     s[(开始索引b):(结束索引e)(:(步长s))]
#     注: () 代表其中的内容可省略
#   说明:
#     开始索引是切片开始切下的位置,0代表第一个元素,与索引相同
#     结束索引是切片的终止索引(不包含终止点)
#     步长是切片每次获取完当前元素后移动的方向和偏移量
#       1) 没有步长,相当于步长为1(默认值:1)
#       2) 当步长为正整数时,取正向切片:
#         开始索引默认为0,结束索引是最后一个元素的下一个位置
#       3) 当步长为负整数时,取反向切片:
#         反向切片时,默认的起始位置为最后一个元素,终止位置为
#         第一个元素的前一个位置
#   示例:
#     s = "ABCDE"
#     a = s[1:4]    # 'BCD'
#     a = s[1:]     # 'BCDE' 等同于 a = s[1:5]
#     a = s[:4]     # 'ABCD' 等同于 a = s[0:4]
#     a = s[:2]     # 'AB'
#     a = s[1:1]    # ''  空字符串
#     a = s[3:0]    # '' 空字符串
#     a = s[0:5:2]  # 'ACE'
#     a = s[::2]    # 'ACE
#     a = s[4:1:-2]  # 'EC'
#     a = s[:1:-2]  # 'EC'
#     a = s[::-2]   # 'ECA'
#     a = s[::-1]   # 'EDCBA'


# 练习:
#   1. 写一个程序,输入一个字符串,把字符串的第一个字符和最后一个
#     字符去掉后,打印出处理后的字符串

#   2. 输入任意一个字符串,判断这个字符串是否是回文
#     回文示例:
#       上海自来水来自海上
#       ABCCBA
#     回文是指中心对称的文字
    

# 运算符的优先级表见文档:
#   python_base_docs_html/python运算符优先级.html

# 字符串序列相关的函数:
#   len(x)  返回序列的长度
#   max(x)  返回序列中最大值元素
#   min(x)  返回序列的最小值元素
#   l.sort()给序列排序从小到大
# 字符串编码转换函数:
#   ord(c) 返回一个字符c的Unicode 编码值
#   chr(i)  返回i这个值对应的字符
  
# 练习:
#   1. 写一个程序,输入一个字符串,如果字符串不为空,则把这个字符
#      串的第一个字符的编码打印出来

#   2. 写一个程序,输入一个整数值(0~65535之间的整数), 打印出
#     这个数值所对应的字符



# 整数转为字符串的函数
#   bin(i)   将整数转为二进制的字符串
#   oct(i)   将整数转为八进制的字符串
#   hex(i)   将整数转为十六进制的字符串

# 字符串的构造函数 str
#   str(obj='')  将对象转为字符串

# python3 中常用的字符串方法:
#   方法调用语句:
#     对象.方法名(方法传参)
# 　示例:
#    'abc'.isalpha()  # 正确
#    123.isalpha()    # 报错
#   字符串的常用方法文档参见:
#     python_base_docs_html/str.html


# 练习:
#   1. 用字符串 * 运算符 打印三角形
#     要求输入一个数, 此整数代表此三角形离左侧的字符个数
#     如:
#       请输入左侧的空格数: 3
#         *
#        ***
#       *****
#      *******
#   2. 输入一个字符串,把输入的字符串中的空格全部去掉
#     打印出处理之后的字符串的内容
# a=input("输入字符串：")

#   3. 输入三行文字,让这三行文字在一个方框内居中显示
#     如(请不要输入中文):
#       请输入第1行: hello!
#       请输入第2行: I'm studing python!
#       请输入第3行: I like python!
#     打印如下:
#       +---------------------+
#       |       hello!        |
#       | I'm studing python! |
#       |   I like python!    |
#       +---------------------+


# def ww(m,n):
#     l=[]
#     sum=0
#     for x in range(m,n+1):
#         if n%x==0:
#             l+=[x]
#     for y in l:
#         sum+=y**2
#     for z in range(1,sum):
#         if z**2==sum:
#             return (n,sum)
# print(ww(1,42))

# l=[]
# l1=[]
# arry=[1,2,3],[8,9,4],[7,6,5]
# for x in arry:
#     for y in x:
#         l.append(y)
#         l.sort()
# print(l)


# x = [4, 6, 2, 1, 7, 9]
# x.sort()
# print (x) # [1, 2, 4, 6, 7, 9]
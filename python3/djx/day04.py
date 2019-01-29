# day03回顾:
#   字符串 str
#     编码 code
#     str里存储的是文字的编码(UNICODE值)
#   字符串的字面值表示:
#     ''   ""   ''''''   """""" 空字符
#     'hello'  "ABCD"  '''abcd''' """1234""" 非空字符串
#     r'abc'   r"123"   r"""\n\r\t""" 原始字符串

#     '''abc
#     123'''  表示'abc\n123'

#   转义字符
#     \'    \"  \\    \n    \r    \t  ...
#     \xXX   \uXXXX   \UXXXXXXXX  用十六进制值来表示字符

#   $ man ascii

#   字符串的运算
#     +   +=   *   *=  
#     <   <=   >   >=  ==  !=
#     in  / not in
#     is  /  is not
#     索引 切片运算 [] 
#       索引   字符串[整数表达式]
#       切片   字符串[整数:整数]  字符串[整数:整数:整数]
#   函数:
#     len(x)  求字符串长度
#     max(x)  求编码值最大的字符
#     min(x)  求编码值最小的字符

#     ord(x)  返回一个字符的编码值
#     chr(i)  用一个编码值返回对应的字符

#     bin(i)  返回一个整数的二进制binary表示的字符串
#     oct(i)              八进制
#     hex(i)              十六进制

#     str(x)  返回一个对象的字符串表示

# 方法:
#   对象.方法名(   )
#   S.isalpha()  
#   S.isdigit()  
#   S.isupper()
#   S.islower()
#   S.isspace()  '\n\r\t '
#   S.center(宽度, 填充字符)
#   S.count(字符串, begin, end)
#   S.find(字符串, begin, end)
#   S.strip()  / S.lstrip()  /  S.rstrip()
#   S.upper()
#   S.lower()
#   S.repalce()
#   S.startswith()    /   S.endswith()


# day04 笔记
# 字符串的格式化表达式
#   作用:
#     生成一定格式的字符串
#   运算符 %
#   语法格式:
#     格式化字符串 % 参数值
#     格式化字符串 % (参数值1, 参数值2, ....)
#   示例:
#     fmt = "name: %s, age:%d"
#     n = 'tarena'
#     a = 15
#     result = fmt % (n, a)  # result='name: tarena, age:15'

#     s2 = '成绩: %d'  % 100

# 格式化字符串中的占位符和类型码
#   占位符和类型码     意义
#     %s           字符串,使用str(x) 函数转换
#     %r           字符串, 使用repr(x) 函数转换
#     %c           整数转为单个字符
#     %d           十进制整数
#     %o           八进制整数
#     %x           十六进制整数(字符a-f小写)
#     %X           十六进制整数(字符A-F大写)
#     %e           指数型浮点数 (e小写),如:2.9e+10
#     %E           指数型浮点数 (E大写),如:2.9E+10
#     %f,%F        浮点十进制形式
#     %g,%G        十进制形式浮点或指数浮点自动转换
# #     %%           等同于一个%字符
    

# 占位符和类型码之间的格式化语法:
#   % [- + 0 宽度.精度] 类型码
#   说明:
#     -    左对齐(默认为右对齐)
#     +    显示正号
#     0    左侧空白位置补零
#     宽度  整数,整个数据输出的宽度(占用的字符数)
#     精度  整数,保留小数占后多少位(默认为6位)
#   示例:
#     "%d" % 123        # '123'
#     "%10d" % 123      # '       123'
#     "%-10d" % 123     # '123       '
#     "%10s" % "ABC"    # '       ABC'
#     "%010d" % 123     # '0000000123'
#     "%+010d" % 123    # '+000000123'
#     pi = 3.1415926535897932
#     "%f" % pi         # '3.141593'
#     "%.10f" % pi      # '3.1415926536'
#     "%7.2f" % pi      # '   3.14'  

# 练习:
#   输入三行文字,让这三行文字依次以20个字符的宽度右对齐输出
#   如:
#     请输入第1行: hello world
#     请输入第2行: abcd
#     请输入第3行: a
#   输出结果为:
#             hello world
#                    abcd
#                       a
#   做完上面的题后再思考:
#     能否以最长的字符串长度进行右对齐显示(左侧填充空格)


# 循环语句
#   循环语句
#     while 语句
#     for 语句
#   问题:
#     输入一个整数n,写程序打印如下:
#        这是第1行
#        这是第2行
#        ...
#        这是第n行


# while 语句:
#   作用:
#     根据一定条件,重复的执行一条语句或多条语句
#   语法:
#     while 真值表达式:
#         语句块1(此部分的语句可能会重复执行)     
#     else:
#         语句块2
#   说明:
#     1. 先执行真值表达式,测试布尔值为True或False
#     2. 如果真值表达式测试值为True,则执行语句块1,然后再返回到
#        第1步,重复进行测试
#     3. 如果真值表达式测试值为False,则执行语句块2,然后结果此
#        while语句的执行,如果没有 else子句,则直接结束此while
#        语句的执行
#     注: else 子句部分可以省略(同if语句类似)
#   示例见:
#     while1.py
#     while2.py

# 练习:
#   1. 打印 1 ~ 20 的整数, 打印在一行内显示,每个整数之间用
#   一个空格分隔
#     如:
#      1 2 3 4 5 6 7 8 9 10 11 ...... 20

#   2. 打印 1 ~ 20 的整数, 每五个数字打印一行,打印四行
#     如:
#       1 2 3 4 5
#       6 7 8 9 10
#       ...
#     提示:
#       可以将 if 语句嵌入到while语句中

#  3. 用 while语句打印 20 ~ 1之间的数


#  4. 写一个程序
#    输入一个开始的整数用变量begin绑定
#    输入一个结束的整数用变量end绑定
#    打印从 begin 到 end(不包含end) 之间的每个整数,打印在
#    一行内
#    如:
#      请输入开始值: 8
#      请输入结束值: 20
#    打印:
#       8 9 10 11 12 13 14 .... 19

#   附加思考:
#     如何实现每5个打印在一行内,打印多行?


# 5. 写一个程序, 输入一个整数n,打印一个宽度和高度都为n个字符的
#   长方形.
#     如:
#       请输入: 4
#     打印如下:
#       ####
#       #  #
#       #  #
#       ####
#     如: 
#       请输入: 6
#     打印如下:
#       ######
#       #    #
#       #    #
#       #    #
#       #    #
#       ######

# while 语句注意事项:
#   1. 要控制循环的真值表达式来防止死循环
#   2. 通常用真值表达式内的循环变量来控制循环条件
#   3. 通常在循环语句块内要改变循环变量来控制循环条件和变量的走向


# 练习:
#   1. 写一个程序来计算:
#      1 + 2 + 3 + 4 + ...... + 99 + 100 的和
#     答案: 5050
  


# while语句嵌套
#    while 语句本身是语句,和其它语句一样,可以嵌入到任何的复合
#    语句中

#   示意:
#     while 真值表达式1:
#         ....
#         while 真值表达式2:
#             ...
#         else:
#             ...
#         ...
#     else:
#         ...
#   示例:
#     打印 1 ~ 20 的整数,打印在一行
#       1 2 3 4 5 .... 20
#     打印十行

# 练习:
#   1. 输入一个数,打印指定宽度的正方形
#     如:
#       请输入正方形宽度: 5
#     打印如下:
#       1 2 3 4 5
#       1 2 3 4 5
#       1 2 3 4 5
#       1 2 3 4 5
#       1 2 3 4 5
#     如: 
#       请输入正方形宽度: 3
#     打印如下:
#       1 2 3
#       1 2 3
#       1 2 3



    
# break 语句
#   问题:
#     如果在循环过程中,不想再继承执行此循环了,怎么办?
#   作用:
#     用于循环语句(while或for语句)中,用来终止当前循环语句的执行
#   语法:
#     break
#   说明:
#     当break语句执行后,此循环语break之后的语句将不再执行
#     break 语句通常和if语句组合使用
#     break 语句终止循环时,循环语句的else子句的语句将不会执行
#     break 语句只能终止当前循环语句的执行,如果有循环嵌套时,不
#          会跳出嵌套的外重循环
#     break 语句只能在循环语句(while 或 for语句)内部使用
#   示例见:
#     break.py
    

# 死循环 death loop
#   死循环是指循环条件一直成立的循环
#   死循环通常用break语句来终止循环
#   死循环的else子句永远不会执行
  
#   示例:
#     i = 1
#     while True:
#         print(i)
#         if i == 10:
#             break
#         i += 1
       
# 练习:
#   让用户任意输入一些整数,当输入负数时结束输入:
#   当输入完成后,打印用户输入的所有整数的和
#   如:
#     请输入: 1
#     请输入: 2
#     请输入: 3
#     请输入: 4
#     请输入: -1
#   打印如下:
#     您输入的这些数的和是: 10


# 练习:
#   1. 写程序求下列算式的值:
#      1/1 - 1/3 + 1/5 - 1/7 + 1/9 -.... (+-)1/(2*n-1)
#      的和
#     求:
#       1) 当n等于10000时,此算式的和并打印
#       2) 将n等于10000时算式的和乘以4,打印其结果 (3.14)
#   2. 用while语句打印三角形, 输入一个三角形的宽度和高度,打印
#      相应的三角形:
#       如:
#         请输入三角形的宽度: 3
#       1) 打印如下:
#         *
#         **
#         ***
#       2) 打印如下:
#           *
#          **
#         ***
#       3) 打印如下:
#         ***
#          **
#           *
#       4) 打印如下:
#         ***
#         **
#         *

    
#   3. 用程序while语句生成如下字符串,并打印结果
#     1) 'ABCDE........XYZ'
#     2) 'AaBbCcDdEe......XxYyZz'
#    函数:
#       ord(x)  / chr(x)

#     #  
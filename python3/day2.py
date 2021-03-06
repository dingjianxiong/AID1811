day01回顾
  python 语句简介
  应用领域比较广泛
  python的优缺点
    可混合编程Python(C/C++)结合编程
  python官网
    www.python.org

  python 的运行
    1. 解释执行相应的文件
       1) $ python3 xxxx.py
       2) 编辑xxxx.py 加入
          #! /usr/bin/python3
          添加执行权限
          $ chmod +x xxxx.py
          运行
          $ ./xxxx.py  (相对路径查找文件)
          $ /home/tarena/xxxx.py (绝对路径)
    2. 交互模式
       $ python3
       >>> print("hellow world")

  python 的注释:
    # 开头,直至行尾
  python程序的组成
  python 的基本数据类型
    数字:
       整数 int, 浮点型数 float, 复数 complex,
       布尔型数 bool
    整数的表示方式(字面值):
      十进制
        -10, 100, 0, 999999999
      二进制
        0b1010
      八进制
        0o1234567
      十六进制
        0x123789ABCDEF
    浮点数的字面值表示方式
      小数
        3.14
      科学计数
        0.314e1
    复数 
      1j
      1+2j
      (1+2j)
    布尔型数
      True  ===> 1
      False ===> 0

空值 None
  

表达式
  1
  None
  True
  1 + 2 * 3
  id(100)  # 函数调用也是表达式
  表达式一定能返一个值的引用(值有可能是None)
运算符:
  + - * / // % **
  is    is not 

  print(....)
  id(x)

  赋值语句
    变量名 = 表达式
    变量名1 = 变量名2 = 表达式
    变量名1, 变量名2 = 表达式1, 表达式2
  作用:
    创建变量来绑定数据对象
    改变变量的绑定关系
  
  del 语句
    删除变量同时解释与对象的绑定关系
  is / is not
  a is b # 判断 id(a) 是否等于id(b)
  小整数对象池
    -5~256 一直存在
  



day02笔记
复合赋值算术运算符
  +=   -=   *=   /=   //=   %=   **=   
  如:
    x += y   等同于 x = x + y
    x -= y   等同于 x = x - y
    x *= y   等同于 x = x * y
    x /= y   等同于 x = x / y
    x //= y  等同于 x = x // y
    x %= y   等同于 x = x % y
    x **= y  等同于 x = x ** y

比较运算
  <  小于
  <= 小于等于
  >  大于
  >= 大于等于
  == 等于
  != 不等于

  语法
    左表达式 < 右表达式
  说明:
    比较运算符返回布尔类型的值

  示例:
    1 < 2   # True
    1 <= 2  # True
    1 == 2  # False
    1 + 2 < 3 + 4  # True
    x = 60
    0 <= x <= 100   # True


数值对象的构造(创建) 函数
  float(obj)    用字符串或数字转换为浮点数,如不给出参数则
            返回0.0
  int(x, base=10)或 int(x=0)  用数字或字符串转换为整
            数,如果不给出参数则返回0
  complex(r=0.0, i=0.0) 用数字创建一个复数(实部为r,
            虚部为i)
  bool(x)   用x获取一个布尔值(True/False)

函数调用:
  函数名(传参列表)
  说明:
    函数调用是表达式,一定会返回一个对象的引用关系(或者
      返回None)


bool(x) 返回假值的情况:
  bool(x) 用于显式获取x的布尔值

  值          说明
  None         空值
  False       布尔假值
  0  0.0  0j  所有的数字零
  ------以下内容后面才讲------
  ''         空字符串
  []         空列表 
  ()         空元组
  ...

练习:
  将数字3.14 用变量pi绑定
  将pi变量转为整数,用变量i绑定
  将pi变量 与 i 变量相减, 结果用变量f绑定
    1. 判断f是否等于0.14
        # 不相等 
    2. 删除所有的变量
  (注: 用交互模式来做)


预置的数值型函数
  abs(x)      取x的绝对值
  round(number[, ndigits]) 对数据进行近似的值＂四舍
              五入",ndigits是小数向右取整的位数，负数
              表求向左取整
  pow(x, y, z=None)  相当于 x**y 或 x**y%z
  注: [] 表求里面的内容可省略

help() 函数查看帮助文档
  >>> help(函数名)
  如:
  >>> help(abs)


语句 statement
  语句由一些表达式组成,通常一条语句可以独立执行来完成一部分
  事情并形成结果.

  说明:
    一条语句建议写在一行内
    多条语句写在一行内需要用分号(;) 分开
  示列:
    x = 100 + 200
    print(x)
    # 写在一起为:
    x = 100 + 200;  print(x)

显式换行:
  折行符 \(反斜杠)
  折行符必须放在一行的末尾,来示意解释执行器,下一行也是
    本行的语句
  示例见:
    new_line.py

隐式换行
  所有的括号内换行，称为隐式折行
    括号: ()  []  {}

其本输入输出

基本输入函数 input
　input('提示字符串')  返回用户输入的字符串
  说明:
    提示字符串可以为空
  返回值:
    字符串
  示例见:
    input.py

基本输出函数 print
  作用:
    将一系列的值以字符串开式输出到标准输出设备上,默认
    为终端
  格式:
    print(v, ..., sep=' ', end='\n', flush=False)

  关键字参数:
    sep: 两个值之间的分隔符,默认为一个空格
    end: 输出完毕后在字符流末尾自动追加一个字符,默认为换行
         符'\n'
    flush: 是否立即输出到屏幕上,默认为False(不立即输出)

  示例见:
    print.py
    print2.py
    print3.py


练习:
  输入两个整数,分别用变量 x, y 绑定
    1. 计算这两个数的和并打印结果
    2. 计算这两个数的积,并打印结果
    3. 计算 x 的 y次方并打印
  如:
    请输入 x: 100
    请输入 y: 200
  打印如下:
    100 + 200 = 300
    100 * 200 = 20000
    100 ** 200 = 1000000.....



if 语句
  问题:
    有两条语句
      print('是偶数')
      print('是奇数')
    如何只让程序执行其中的一条语句
  作用:
    让程序根据条件选择性的执行某条语句或某些语句
  语法:
    if 真值表达式1:
        语句块1
    elif 真值表达式2:
        语句块2
    elif 真值表达式3:
        语句块3
    ...
    else:
        语句块4
  说明:
    elif 子句可以有0个,1个或多个
    else 子句可以有0个或1个,且只能放在此if语句的最后
  示例见:
    if.py

练习:
  任意输入一个数字
    1) 判断这个数是否大于100
    2) 判断这个数是否小于0
    3) 判断这个数是否在 50 ~ 150 之间

  if语句示例2:
    if2.py

练习:
  1. 输入一个季度 1 ~ 4 ,输出这个季度有哪儿几个月,
     如果用户输入的不是1~4的整数,则提示用户"您输错了"

  2. 输入一年中的月份 1~12, 输出这个月在哪儿个季度,
     如果用户输入的是其它的数,则提示用户"您输错了"

if 语句的真值表达式
  if 100:
      print("真值")

  等同于:
  if bool(100):
      print("真值")

if 语句嵌套
  if 语句本身是由多条子句组成的一条复合语句
  if 语句可以作为语句嵌套到另一个复合语句的内部

  示例见:
    if_embed.py
  





练习:
  写一个程序,输入一个整数, 用if语句计算这个数的绝对值
    并打印出来
     (要求: 不允许用abs函数)



条件表达式
  语法:
    表达式1 if 真值表达式 else 表达式2
  作用:
    根据真值表达式的取值(True/False) 来决定执行表达式1
    或表达式2 并返回结果

  示例见:
    if_express.py


练习:
  1. 写一个程序.输入一个整数,打印出这个整数的绝对值
    要求用 条件表达式来实现,不允许使用abs函数
  
pass 语句
  作用:
    通常用来填充语法空白
  语法:
    pass
  示例见:
    pass.py


布尔运算:
  运算符
    not     and    or
布尔非操作 not
  语法:
    not x
    注: x代表表达式
  作用:
    对x进行布尔取非,bool(x) 为True则返回False, 否则返回
    True
  示例:
    not True  # 返回False
    not False # 返回True

布尔与操作 and
  语法:
    x and y
    注: x, y代表表达式
  作用:
    优先返回假值对象
    当x的布尔值为False,返回x, 否则返回y
  示例:
    True and True    # True
    True and False   # False
    False and True   # False
    False and False  # False
    100 and 3.14     # 3.14
    0 and 3.14       # 0
    0 and 0.0        # 0

布尔或操作 or
  语法:
    x or y
  作用:
    优先返回真值对象
    当x为True时返回x, 否则返回y
  示例:
    True or True    # True
    True or False   # True
    False or True   # True
    False or False  # False
    100 or 3.14     # 100
    0 or 3.14       # 3.14
    0 or 0.0        # 0.0


正负号运算符:
  + (正号)  - (负号)
  一元运算符(一个元素参加运算)

  语法:
    + 表达式
    - 表达式
  示例:
    a = 5
    b = -a
    c = +a


练习:
  1. 北京出租车计价器
    收费标准:
      1. 3公里以内收费 13元
      2. 基本单价 2.3 元/公里(超过3公里以外)
      3. 空驶费: 超过15公里后,每公里加收单价的50%空驶费
         (即3.45元/公里)
    要求: 输入公里数,打印出费用金额(以元为单位精确到分)
  2. 输入三个任意的数:
    1) 打印出最大数是多少?
    2) 打印出最小数是多少?
    3) 打印出三个数的平均值是多少?
  3. BMI指数(Body Mass Index) 又称身体质量指数
    BMI计算公式:  BMI = 体重(公斤) / 身高的平方(米)
    如:  一个69公斤的人,身高是173厘米 则BMI如下:
       BMI = 69 / 1.73 ** 2    得23.05
    标准表:
      BMI < 18.5       体重过轻
      18.5 <= BMI < 24 正常范围
      BMI >= 24        体重过重
    输入身高和体重,打印出BMI值,并打印体重状况

      
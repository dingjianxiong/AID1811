# day09 回顾:
#   实参(实际参数传递)
#     位置传参
#       序列传参  *序列
#     关键字传参   fn(a=10, b=20)
#       字典关键字传参 fn(**{'a':10, 'b':20})
#   形参(接收实参)
#     定义方式:
#       位置形参
#       *元组形参      def fn(*args)
#       命名关键字形参  def fn(*,a,b,c) def fn(*args,a,b,c)
#       **字典形参  def fn(**kwargs):
#     缺省参数
#       在实参传递时,当不传入实参时,默认使用缺省参数
#          def fn(a=10, b=20, c=30, *args, d=40, e=50):

# 全局变量和局部变量
# 局部变量
#    赋值语句可以创建局部变量
#    def 语句可以创建变量(在函数内,将创建局部变量)
#    for x in range(10):  创建变量

# 全局变量
   
# globals()   / locals()  函数
# a=1
# b=2
# c=3
# def fn(c,d):
#     e=400
#     print("返回所有全局变量：",globals(),end="")
#     print("打印全局变量c,   c=:",globals()["c"])
# fn(100,200)
# print()



      


# day10笔记:
# 函数变量
#   函数名是变量,它在创建时绑定一个函数
#   示例1:
#     def f1():
#        print("f1被调用!")
#     f2 = f1  # f2变量绑定f1绑定的函数(注意这里f1没加括号)
#     f2()  # 等同于调用f1这个函数
#     f1() 
#   示例2:
#     def f1():
#         print("f1")
#     def f2():
#         print("f2")
#     f2 = f1
#     f1()  # f1
#     f2()  # f2

    
# 一个函数可以作为另一个函数的实参传递
#   示例见:
#     function_as_args.py
#     function_as_args2.py
# 　# 看懂如下代码在做什么
# def call_fun(fn):
#     L = [1, 3, 9, 7, 5]
#     return fn(L)
# print(call_fun(max))  # 9
# print(call_fun(min))  # 1
# print(call_fun(sum))  # 25
# def f1():
#     print("f1被调用")
# def f2():
#     print("f2被调用")
# def fx(fn):
#     print(fn)
#     fn()
# fx(f1)
# fx(f2)
# fx(print)
# fx(max)#报错  调用ｍａｘ函数,但max函数参数不能为空


# 函数可以作为另一个函数的返回值
#   示例见:
#     return_function.py
# def get_function():
#     s=input("请输入你要做的操作：")
#     if s=="求最大":
#         return max
#     elif s=="求最小":
#         return min
#     elif s=="求和":
#         return sum
# l=[2,3,4,5,10]
# f=get_function()
# print(f(l))


# 练习:
#     写一个计算公式的解释执行器
#       已知有如下一些函数:
# def myadd(x, y):
#     return x + y
# def mysub(x, y):
#     return x - y
# def mymul(x, y):
#     return x * y
# #         ...
# #       再写一个函数
# def get_func(op):
#     # a=input("请输入：")
#     # for x in L:
#     if op=="+":
#         return myadd
#     elif op=="-":
#         return mymul
#     elif op in ("*","乘"):
#         return mymul
# #             .....  # 以下代码自己实现
# #         此函数在传入字符串"加"或'+' 返回myadd函数
# #         此函数在传入字符串"乘"或'*'  返回mymul函数
# #       在主函数程序如下:
# def main():
#     while True:
#         s = input("请输入计算公式: ")  # 10 加 20
#         L = s.split()  # L = ['10', '加', '20']    s.split()默认以 " "分开字符串，并转换为列表
#         a = int(L[0])
#         b = int(L[2])
#         fn = get_func(L[1])
#         print("结果是:", fn(a, b))  # 结果是: 30
# main()


# 函数嵌套定义
#   def 是语句，它可以放在任何复合语句中
#   函数嵌套定义是指一个函数里用def语句来创建其它函数的情况

#   示例:
# def fn_outer():
#     print("fn_outer调用开始...")
#     def fn_inner():
#         print("fn_inner被调用")
#     fn_inner()
#     fn_inner()
#     print("fn_outer调用结束!")
# fn_outer()



# python3 中的作用域
#   作用域也叫命名空间，是访问变量时查找变量名的范围空间

# python 中的四个作用域
#   作用域                 英文解释          英文简写
# 局部作用域(函数内)   Local(function)           L
# 外部嵌套函数作用域   Enclosing function Local  E
# 函数定义所在模块作用域   Global(module)         G
# python内置模块的作用域  Builtin(Python)        B
# v=100
# def f1():
#     v=200
#     print("f1.v=",v)
#     def f2():
#         v=300
#         print("f2.v=",v)
#     f2()
# f1()
# print("v=",v)
# 示例见:
#   namespace.py


# 变量名的查找规则
# 　L --> E  --> 　G  --> B
#   在访问变量时，先查找本地变量,然后是包裹此函数外部函数内
#   的变量，之后是全局变量，最后是内置变量
#   在默认情况下，变量名赋值会创建或者改变当前作用域变量




# global　语句
#   作用:
#     告诉解释器,global语句声明的一个或多个变量，这些变量的作用
#     域为模块级的作用域，也称作全局变量
#     global全局声明将赋值语句的变量映射到模块文件内部的作用域
#   语法:
#     global 变量名1, 变量名2, ...
#   示例见:
#     global.py
#   说明:
#     1. 全局变量如果要在函数内部被赋值,则必须经过全局声明(否则
#       会被认为是局部变量)
#     2. 全局变量在函数内部不经过声明就可以直接访问(取值)
#     3. 不能先声明局部变量,再用global声明为全局变量,此做法不
#       符合规则
#     4. global变量列表里的变量名不能出现在函数的形参列表里
# v=300
# def f1():
#     v=100
#     global v #声明全局变量
#     # v=200#让这条赋值语句改变全局的v
#     print(v)
# f1()
# print("v=",v)

# 练习:
#   用全局变量记录一个函数hello被调用的次数,部分代码如下:
#     count = 0
#     def hello(....):
#         ...
#     hello("小张")  # 打印:你好,小张
#     hello("小李")  # 打印:你好,小李
#     print("hello这个函数被调用", count, '次')
# count = 0
# def hello(name):
#     print("你好",name)
#     global count
#     count +=1
# while True:
#     s=input("请输入姓名：")
#     if not s:
#         break
#     hello(s)
# print("hello这个函数被调用", count, '次')


# 思考题:
#     L = [1, 2, 3]
#     def f1(lst):
#         L = lst  # 这是在做什么?可以吗?

#     def f2(lst):
#         L += lst  # 这么做可以吗? 为什么?

#     def f3(lst):
#         L.extend(lst)  # 这么做可以吗? 为什么?
    
#     f1([4, 5, 6])
#     f2([4, 5, 6])
#     f3([4, 5, 6])
#     print(L)  # ???
#   答案见:
#     exercise/faq.py



# nonlocal语句
#   作用:
#     告诉解释执行器,nonlocal声明的变量,不是局部变量,也不是全
#     局变量,而是外部嵌套函数内的变量
#   语法:
#     nonlocal 变量名1, 变量名2, ....
#   示例见:
#     nonlocal.py
#   说明:
#     1. nonlocal 语句只能在被嵌套函数的内部进行使用
#     2. 对nonlocal变量进行赋值将对外部嵌套函数作用域的变量进行
#        操作
#     3. 当有两层或两层以上函数嵌套时,访问 nonlocal 变量只对
#        最近的一层变量进行操作
#     4. nonlocal 语句的变量列表里的变量名,不能出现在此函数的
#        形参列表中
# v=100
# def f1():
#     v=200
#     print("函数开始时：f1.v=",v)
#     def f2():
#         nonlocal v
#         v=300
#     f2()
#     print("函数结束时：f2.v=",v)
# f1()
# print("全局的v=",v)


# lambda 表达式
#   作用:
#     创建一个匿名函数对象
#     同def 类拟,但不提供函数名
#   语法:
#     lambda [函数形参列表]: 表达式
#     注: [] 内部的形参列表可以省略
#   示例见:
#     lambda.py
#   说明:
#     lambda 表达式创建的函数只能包含一条表达式
#     lambda 比函数简单,且可以随时创建和销毁,有利于减少程序
#       的偶合度(偶合度为程序模块之间的关联程度)
#
# def myadd(x,y):
#     return x+y
# myadd=lambda x,y:x+y  #改写上面的def 语句
# print("20+30=",myadd(20,30))

# 练习:
#   1. 写一个lambda 表达式
#       fx = lambda n: ....
#   此表达式创建的函数判断n这个数的2次方+1能否被5整除,如果能
#   整除返回True,否则返回False
#     如:
#       print(fx(3))  # True
#       print(fx(4))  # False
# fx = lambda n: (n**2+1)%5==0
# print(fx(3))
#   2. 写一个lambda表达式来创建函数,此函数返回两个形参变量的
#     最大值:
#     def mymax(x, y):
#         ....
#     mymax = lambda .....
#     print(mymax(100, 200))  # 200
#     要求: 尽可能不调用max函数
# mymax = lambda x,y:max(x,y)
# mymax = lambda x,y:x if x>y else y
# print(mymax("ABC","123"))
# print(mymax(200,123))

#   3. 看懂下面的程序在做什么?
#     def fx(f, x, y):
#         print(f(x, y))
    
#     fx((lambda a, b: a + b), 100, 200)
#     fx((lambda c, d: c ** d), 3, 4)

# eval 函数 exec 函数
# eval 函数:
#   作用:
#     把一个字符串当成一个表达式来执行,返回表达式执行后的结果
#   格式:
#     eval(source, globals=None, locals=None)
#     参数:
#       source 是要解释执行的字符串(此字符串必须是符合python
#              语法的表达式)
#       globals 是在source运行时的全局作用域的变量的字典
#       locals  是source 运行时局部作用域的变量的字典
#   示例见:
#     eval.py
#     eval2.py
# s1="1+2*3"
# x="t"
# y="e"
# s2="x+y"#定义ｘ　ｙ
# v=eval(s1)
# print(v)#结果：　7
# v2=eval(s2,{'x':10,'y':20})#给ｘ，ｙ一个字典作用域（可以用来定义ｘｙ的变量）
# print(v2)#把x,y字符串相加
# v2=eval(s2,{'x':40,'y':30},{'y':20})
# print(v2)


# exec 函数
#   作用:
#     把一个字符串当成程序来执行
#   格式:
#     exec(source, globals=None, locals=None)
#   参数说明:
#        source 用于执行语句的字符串(此字符串必须是符合python
#              语法的表达式)
#       globals 是在source运行时的全局作用域的变量的字典
#       locals  是source 运行时局部作用域的变量的字典
#   示例见:
#     exec.py
    
# 练习:
#   自己写一个程序的解释执行器,解释执行我们自己输入的程序
#     如:
#       请输入程序: >>> x = 100<回车>
#       请输入程序: >>> y = 200<回车>
#       请输入程序: >>> print("x+y=",x+y)<回车>
#       x+y= 300
#     提示用: exec函数





# 练习:
#   1. 写一个函数mysum(x)  来计算:
#     1 + 2 + 3 + 4 + ..... + n 的值
#     (要求: 不允许用sum)
#   如:
#     print(mysum(100))  # 5050

#   2. 写一个函数myfac(n)  来计算n!(n的阶乘)
#     n! = 1 * 2 * 3 * 4 * ... * n
#   如:
#     print(myfac(5))   # 120

#   3. 写一个函数mypow(n)计算 1 + 2**2 + 3**3 + ... n**n的和
#     (注: n给个小点的数)
#    如:
#     print(mypow(3))  # 32

#   4. 实现带有字符界面的学生信息管理系统
#     要求有如下的操作可以选择功能
#     +-----------------------------+
#     | 1) 添加学生信息               |
#     | 2) 显示学生信息               |
#     | 3) 删除学生信息               |
#     | 4) 修改学生成绩               |
#     | q) 退出                      |
#     +-----------------------------+
#     请选择: 1<回车>
#     学生信息包括:姓名,年龄,成绩(与之前相同),
#     注: 每个功能与一个函数与之相对应
    

    
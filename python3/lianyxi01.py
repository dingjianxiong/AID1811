# bool(x) 返回假值的情况:
#   bool(x) 用于显式获取x的布尔值

#   值          说明
#   None         空值
#   False       布尔假值
#   0  0.0  0j  所有的数字零
#   ------以下内容后面才讲------
#   ''         空字符串
#   []         空列表 
#   ()         空元组
# x=2
# y=2
# z=4
# print(pow(x,y,z))
# print(v, ..., sep=' ', end='\n', flush=False)

#   关键字参数:
#     sep: 两个值之间的分隔符,默认为一个空格
#     end: 输出完毕后在字符流末尾自动追加一个字符,默认为换行
#          符'\n'
#     flush: 是否立即输出到屏幕上,默认为False(不立即输出)
# print(2,3,4,5, sep=' ', end='\n', )
# print(2,3,4,5, sep='', end='' )
# print(2,3,4,5, sep='', end='' )
# print(0 and 17)   #（输出假的，两个都为假输出前面）　　前面为真。就看后面，后面也为真就输出后面，后面为假就输出后面　　前面为假就输出前面　｜　　||
# 优先返回真值对象
#     当x为True时返回x, 否则返回y
#   示例:
#     True and True    # True
    # True and False   # False
    # False and True   # False
    # False and False  # False
    # 100 and 3.14     # 3.14
    # 0 and 3.14       # 0
    # 0 and 0.0        # 0
# print(-34 or 17)     #有一个为真就输出第一个  
#  True or True    # True
#     True or False   # True
#     False or True   # True
#     False or False  # False
#     100 or 3.14     # 100
#     0 or 3.14       # 3.14
#     0 or 0.0        # 0.0


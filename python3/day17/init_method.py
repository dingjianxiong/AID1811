# 初始化方法:
#   作用:
#     对新创建的对象添加属性
#   格式:
#     class 类名(继承列表):
#         def __init__(self[, 形参列表]):
#             语句块
#     注: []代表其中的内容可省略
# class car:
#     def __init__(self,c,b,m='不详'):
#         self.color=c
#         self.brand=b
#         self.model=m
#     def run(self,speed):
#         print(self.color,"的",self.brand,self.model,"小汽车正在以",speed,"公里/每小时速度行驶")

# a4=car("红色","奥迪","A4")
# a4.run(199)

# t4=car("蓝色","tesla","model s")
# t4.run(230)

# t4.__init__("银色","tesla","model s")
# t4.run(150)

# car("银色","奥迪","A5").run(200)
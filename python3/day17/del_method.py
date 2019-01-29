# 析构方法
#   格式:
#     def __del__(self):
#         语句块
#   说明:
#     析构方法在对象(实例)销毁前被自动调用
#     python语言建议不要在对象销毁时做任何事情,因为销毁的时间
#     难以确定
#   作用:
#     在对象销毁前,释放此对象占用的资源

class car:
    def __init__(self,info):
        self.info=info
        print("汽车：",info,"对象被创建！")
    def __del__(self):#销毁资源释放方法
        print("汽车：",self.info,"对象被销毁！")
c1=car("BYD E6")

# del c1     #c1销毁资源释放
# c1=None    #c1销毁资源释放

input("请输入回车键继续：")
print("程序正常退出")



def maop(value):
    #外部循环：对应走访数据的次数
    #内部循环：对每次走访的次数
    for i in range(len(value)-1):
        for j in range(len(value)-i-1):
            #从小到大排序，如果前者大于后者，两者交换
            if value[j]>value[j+1]:
                value[j],value[j+1]=value[j+1],value[j]
    #打印遍历次数
    print("遍历次数：",i+1)

if __name__=='__main__':
    #原始数据　－
    value=[100,190,165,170,155,108,139,175,160,180]
    maop(value)
    print('排序后：',value)
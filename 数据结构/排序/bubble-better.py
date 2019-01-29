def maop(value):
    #外部循环：对应走访数据的次数
    #内部循环：对每次走访的次数
    for i in range(len(value)-1):
        #设置标志位
        flag=False
        for j in range(len(value)-i-1):
            #从小到大排序，如果前者大于后者，两者交换
            if value[j]>value[j+1]:
                print(value)
                value[j],value[j+1]=value[j+1],value[j]
                flag=True
        #若未发生数据交换，则证明剩余数据有序，则无需进行下一次走访
        if flag==False:
            break
    #打印遍历次数
    print("遍历次数：",i+1)

if __name__=='__main__':
    #原始数据　－
    value=[100, 108, 139, 155, 160, 165, 170, 180, 190, 175]
    maop(value)
    print('排序后：',value)
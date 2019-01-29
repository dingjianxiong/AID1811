# [80, 70, 30, 50, 69, 78, 90, 100, 65, 88]
      

def insert(value):
    for i in range(1,len(value)):
        #获取当前无序数据
        temp=value[i]
        #存放该数据的位置
        pos=i
        for j in range(i-1,-1,-1):
            #对比有序数据和取出数据
            if value[j]>temp:
                #该数据后移
                value[j+1]=value[j]
                #更新插入取出数据的位置
                #对应遍历完索引数据时
                #在有序数据首部插入元素的位置
                pos=j
            else:
                #若有序数据小于等于取出数据，则在该有序数据后插入取出数据
                pos=j+1
                #找到插入位置后退出内部循环
                break
        #在指定位置插入取出数据
        value[pos]=temp
if __name__ == "__main__":
    #原始数据
    value=[80, 70, 30, 50, 69, 78, 90, 100, 65, 88]
    print('排序前',value)
    #插入排序
    insert(value)
    print('排序后',value)

# def insert(value):
#     for y in range(len(value)-1):
#         for x in value:
#             if value[y+1]>x:
#                 value[y],value[y+1]==value[y+1],value[y]
  
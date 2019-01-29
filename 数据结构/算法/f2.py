#二分查找
#原始数据　－value->[1,2,3,4,5,6,7,8,9,10,11,12,13]
#待查找数据-key-->9
#每次查找范围的左侧下标值：left
#每次查找范围的右侧下标值：right
# def ff(value,key,left,right):
#     if left>right:
#         #查找失败，返回－１
#         return -1
#     #获取中间元素对应下标值
#     middle=(left+right)//2
#     #对比中间元素值与指定查找值
#     #如果两者相同
#     if value[middle]==key:
#         #查找成功
#         return middle
#     elif value[middle]>key:
#         #则在左侧继续查找
#         return ff(value,key,left,middle-1)
#     else:
#         #则在右侧继续查找
#         return ff(value,key,middle+1,right)
# if __name__=='__main__':
#     #原始数据　－
#     value=[1,2,3,4,5,6,7,8,9,10,11,12,13]
#     #待查找数据
#     key=9
#     #顺序查找
#     res=ff(value,key,0,len(value))
#     if res==-1:
#         print("查找失败")
#     else:
#         print("查找成功，对应的下标值：",res)

#循环二分查找
def aa(value,key):
    #获取左侧和右侧对应下标值
    left=0
    right=len(value)
    #若存在合法查找范围则查找数据
    while left<=right:
        #获取对应值下标
        middle=(left+right)//2
        if value[middle]==key:
            return middle
        elif value[middle]>key:
            right=middle-1
        elif value[middle]<key:
            left=middle+1
    return -1
if __name__=='__main__':
    #原始数据　－
    value=[1,2,3,4,5,6,7,8,9,10,11,12,13]
    #待查找数据
    key=9
    #顺序查找
    res=aa(value,key)
    if res==-1:
        print("查找失败")
    else:
        print("查找成功，对应的下标值：",res)
        

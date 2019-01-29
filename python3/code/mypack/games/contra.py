#file:mypack/games/contra.py

def play():
    print("正在玩魂斗罗..."")
def gameover():
    '''此函数示意包的相对导入，在当前的contra.py模块中
    导入上一级
    '''
    print("游戏结束！！！")
    import time
    time.sleep(2)
    
print("魂斗罗模块被加载！！！")
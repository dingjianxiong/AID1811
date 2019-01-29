
# assert
def get_score():
    s=int(input("请输入学生成绩："))
    assert 0<=s<=100,"成绩超出范围"
    return s
try:
    score = get_score()
    print("学生成绩是：",score)
except AssertionError as err:
    print("断言失败！ err=",err)
except ValueError as err:
    print("输入的成绩错误：",err)
import re
# ３、自己找一篇文档，使用正则表达式匹配
#         １、所有以大写字母开头的单词
#         ２、所有的数字，包含整数、小数、负数、分数、百分数
# s='What4 will 33.22 happen 3/5 If\  FF0.1 DD() People. 44 live 7.4 without 5.5% love In -7.8 my point of view,'
# obj=re.findall(r'[A-Z]+\S*',s)
# obj1=re.findall(r'-?\d+\.?\d*%?',s)
# print(obj)
# print(obj1)
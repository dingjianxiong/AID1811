import re

# pattern=r'\d+'
# s='2018年中国经济整涨6.6%,与2017年基本持平，2019面临很多困难'
# it=re.finditer(pattern,s)
# #match对象属性
# # print(dir(next(it)))

# 返回匹配到的内容，失败返回None
# try:
#     obj=re.fullmatch(r'\w+','hello1973')
#     print(obj.group())
# except Exception as e:
#     print('error:'e)

# 匹配目标字符串开始位置
# obj=re.match(r'[A-Z]\w+','hello word')
# print(obj.group())

# 匹配目标字符第一处匹配内容
s='2018年中国经济整涨6.6%,与2017年基本持平，2019面临很多困难'
obj=re.search(r'\d+',s)
print(obj.group())
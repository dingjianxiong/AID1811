import re

#忽略大小写(re.I)
# s='Hello world'
# pattern=r'hello'
# regex=re.compile(pattern,flags=re.I)
# l=regex.findall(s)
# print(l)

#使用ascii字符(re.A)
# s='Hello 你好'
# pattern=r'\w+'
# regex=re.compile(pattern,flags=re.A)
# l=regex.findall(s)
# print(l)

#作用域元字符 .　使其可以匹配\n(re.S)
# s='''Hello world
# nihao china
# '''
# pattern=r'.+'
# regex=re.compile(pattern,flags=re.S)
# l=regex.findall(s)
# print(l)

#作用域^$使其可以匹配每行的开头结尾(re.M)
# s='''Hello world
# nihao china
# '''
# pattern=r'world$'
# regex=re.compile(pattern,flags=re.M)
# l=regex.findall(s)
# print(l)

# 给正则表达式每行加#注释
# s="abcdefgh"
# pattern=r'''(ab) #第一行分组
# \w+ #任意字符串
# (?P<dog>ef) #dog组
# '''
# regex=re.compile(pattern,flags=re.X)
# l=regex.findall(s)
# print(l)
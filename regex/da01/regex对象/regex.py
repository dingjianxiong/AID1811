import re

#匹配数字
pattern=r'(\w)+:(\d+)'
s='张:1994,李:1995'

#直接用re调用
# l=re.findall(pattern,s)
# print(l)

#compile对象调用
# regex=re.compile(pattern)
# l=regex.findall(s,pos=0,endpos=10)
# print(l)

# 列表　切割后的内容
# l=re.split(r'\s+','hello   world  nihao    kitty')
# print(l)

# 使用字符串替换正则匹配内容
# s=re.sub(r'\s+','##','hello   world  nihao    kitty',2)
# print(s)

# subn():与sub相同，多返回一个替换个数
# s=re.subn(r'\s+','##','hello   world  nihao    kitty',2)
# print(s)


import re

# １、普通字符
# s='hello word to python'
# a=re.findall('hello',s)
# print(a)

# ２、或
# s='hello word to python'
# a=re.findall('hello|python',s)
# print(a)

# ３、匹配单个字符
#  .  表示匹配任意一个字符
# s='hello word to python'
# a=re.findall('h.',s)
# print(a)

# ４、匹配字符串开始位置
# s='hello word to hello python'
# a=re.findall('^hello',s)
# print(a)

# ５、匹配字符串的结尾位置
# s='hello word to python hello'
# a=re.findall('hello$',s)
# print(a)

# ６、匹配重复
# 元字符：　*
# s='hooooooooewrwqerwqe'
# a=re.findall('ho*',s)
# print(a)

# ７、匹配重复
# 元字符：+
# s='ewrwqerwqe'
# a=re.findall('w*',s)
# print(a)

# ８、匹配重复
#     元字符：？
# a=re.findall('ab?',"sadsaewgreabeer")
# print(a)

# ９、匹配重复
#     元字符：{n}
# a=re.findall('b{2}',"asadbbbadawdbbb")
# print(a)

# １０、匹配重复
#     元字符:{m,n}
# a=re.findall('ab{2,4}',"aba abbbww sabbbbbb")
# print(a)

# １１、匹配字符集
#         元字符：[字符集]
# a=re.findall('s[dw]',"abs sdw sww 123 海　你好")
# print(a)
# a=re.findall('[A-Z]+[a-z]',"Aasd fe GG YTRTFe123 海　你好")
# print(a)

# １２、匹配字符集
#         元字符：[^...]
# a=re.findall('[^A-Z]+[a-z]',"Aasd fe GG YTRTFe123 海　你好")
# print(a)
# a=re.findall('[^, ]+',"Aasd fe GG YTRTFe123 海 你好")
# #*除了逗号和空格外，多个字符
# print(a)

# １３、匹配任意（非）数字字符
#         元字符：\d  \D
# a=re.findall('1\d{10}',"1232136764,341243,12132131234 1356547673")
# print(a)

# １４、匹配任意普通字符
#         元字符：\w \W 
# a=re.findall('[\W+]',"seew#1312 44% 下降")
# print(a)

# １５、匹配任意（非）空字符
#         元字符：\s \S 
# a=re.findall('\S+',"hello    word ")
# print(a)

# １６、匹配字符串开头位置
#         元字符：\A \Z
# a=re.findall('\A\d+-\d+\Z',"1000-1500")
# print(a)

# １７、匹配（非）单词边界
#         元字符:\b \B 
# a=re.findall(r'\bis\b',"this is a test")
# print(a)

# 正则表达式分组：
# a=re.search(r'(ab)+\d','abababababab1234').group()
# print(a)

# a=re.search(r'\w+@\w+\.(cn|com)','abc@123.com').group()
# print(a)

# a=re.search(r'(http|https|ftp|file)://\S+','http://www.baidu.com').group(1)
# print(a)

# a=re.search(r'(?P<piglet>ab)cde','abcdefght').group("piglet")
# print(a)

#身份证规范
# a=re.search(r'\d{17}(\d|x)','50010119980815251x').group()
# print(a)

# re模块使用
# regex=re.compile('abc')
# print(regex)


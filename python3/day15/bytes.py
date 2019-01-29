#bytes与str相互转换
s="hello"
b = s.encode(encoding='utf-8')   #字符串  转换为  字节串
print(b)

c=b'hello'
t = c.decode(encoding='utf-8')   #字节串  转换为  字符串
print(t)
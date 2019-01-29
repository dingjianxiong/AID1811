import re
import sys


def get_address(port):
    f=open('1.txt')
    while True:
        data=''
        for line in f:
            if line!='\n':
                data+=line
            else:
                break
        #已经到文件的结尾
        if not data:
            return '未找到'
        #匹配首单词，查看是否为目标段落
        try:
            PORT=re.match(r'\S+',data).group()
        except Exception as e:
            print(e)
            continue
        if PORT == port:
            # pattern=r'address is ([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})'
            pattern=r'address is ((\d{3}\.){3}\d{1,3}/\d+|Unknow)'
            address=re.search(pattern,data).group(1)
            return address


if __name__ == "__main__":
    port=sys.argv[1]
    addr=get_address(port)
    print(addr)


# data=fd.readline()
# if data[0]==port:
#     # 192.168.100.254/24
#     # 192.168.1.100/24
#     print("查找")
#     pattern=r'\d.\d.\d.\d/\d'
#     regex=re.compile(pattern,flags=re.M)
#     l=regex.findall(port)
#     return l
#     if data==[]:
#         fd.close()
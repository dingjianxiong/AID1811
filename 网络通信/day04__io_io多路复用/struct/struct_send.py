from socket import *
import struct
#与接收方数据结构相同

s=socket(AF_INET,SOCK_DGRAM)

ADDR=('127.0.0.1',8866)

# st=struct.Struct('i5sf')
while True:
    id=int(input("id:"))
    name=input("name:")
    height=float(input("height:"))
    data=st.pack('i5sf',id,name.encode(),height)
    s.sendto(data,ADDR)
s.close()
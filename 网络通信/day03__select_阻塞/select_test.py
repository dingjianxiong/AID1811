from socket import *
from select import *

s=socket()
s.bind(('0.0.0.0',6666))
s.listen(3)
print("监控IO")
rs,ws,xs=select([s],[],[])
print("就绪rs(IO)：",rs)
print("就绪ws(IO)：",ws)
print("就绪xs(IO)：",xs)
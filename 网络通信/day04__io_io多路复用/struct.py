import struct
st=struct.Struct('i5sf')
data=st.pack(1,b'zhang',1.75)
print(data)
data1=st.unpack(data)
print(data1)

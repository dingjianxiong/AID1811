from socketserver import *

#创建服务器类(多线程)
class Server(ThreadingMixIn,TCPServer):
    pass
#编写具体请求处理类
class Handler(StreamRequestHandler):
    #具体处理方法(重写方法)
    def handle(self):
        print("cennect from",self.client_address)
        while True:
            #self.request就是accept返回的套接字
            data=self.request.recv(1024)
            if not data:
                break
            print(data.decode())
            self.request.send(b'ok')

#创建服务器对象，绑定处理类
server_addr=('0.0.0.0',8888)
server=Server(server_addr,Handler)
server.serve_forever()#启动服务

#conding=utf-8
'''
HTTP Server v2.0
多线程并发
可以做request解析
能够返回简单的数据
使用类进行封装
'''

from socket import *
from threading import Thread
import sys
#httpserver 主体功能
class HTTPServer(object):
    def __init__(self,addr,static_dir):
        self.server_addr=addr
        self.static_dir=static_dir
        self.ip=addr[0]
        self.port=addr[1]
        #创建套接字
        self.create_socket()
    #创建套接字
    def create_socket(self):
        self.socket=socket()
        self.socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.socket.bind(self.server_addr)
    def serve_forever(self):
        self.socket.listen(3)
        print("listen to the port%d"%self.port)
        while True:
            try:
                connfd,addr=self.socket.accept()
            except KeyboardInterrupt:
                self.socket.close()
                sys.exit("服务器退出")
            except Exception as e:
                print("error",e)
                continue
            #创建线程处理客户端请求
            clientThread=Thread(target=self.handle,args=(connfd,))
            clientThread.setDaemon(True)
            clientThread.start()
    #处理客户端请求
    def handle(self,connfd):
        #接收http请求
        request=connfd.recv(4096)
        #客户端断开
        if not request:
            connfd.close()
            return
        #按行切割
        request_lines=request.splitlines()
        print(connfd.getpeername(),':',request_lines[0])
        #获取具体请求内容
        getrequest=str(request_lines[0]).split(' ')[1]
        if getrequest=='/' or getrequest[-5:]=='.html':
            self.get_html(connfd,getrequest)
        else:
            self.get_data(connfd,getrequest)
        connfd.close()
    

    #发送网页给客户端
    def get_html(self,connfd,getrequest):
        if getrequest=='/':
            filename=self.static_dir+'/index.com'
        else:
            filename=self.static_dir+getrequest
        try:
            f=open(filename)
        except Exception:
            #没有网页
            responseHeaders='HTTP/1.2 404 NOT found\r\n'
            responseHeaders+='\r\n'
            responseBody='<h1>sorry ,not found the page<h1>'
        else:
            responseHeaders='HTTP/1.2 200 OK\r\n'
            responseHeaders+='\r\n'
            responseBody=f.read()
        finally:
            response=responseHeaders+responseBody
            connfd.send(response.encode())
    def get_data(self,connfd,getrequest):
        urls=['/time','/tedu','/hello']
        if getrequest in urls:
            responseHeaders='HTTP/1.2 200 OK\r\n'
            responseHeaders+='\r\n'
            if getrequest=='/time':
                import time
                responseBody=time.ctime()
            elif getrequest=='/tedu':
                responseBody='tedy python'
            elif getrequest=='/hello':
                responseBody='hello world'
            else:
                responseHeaders='HTTP/1.2 404 NOT found\r\n'
                responseHeaders+='\r\n'
                responseBody='sorry ,not found the page'
            #将数据发送给客户端
            response=responseHeaders+responseBody
            connfd.send(response.encode())


#测试使用，当被别人import 调用后，不会被执行
if __name__=="__main__":
    #用户自己确定
    server_addr=('0.0.0.0',8888)
    static_dir='./static' #存放网页

    #创建服务器对象
    httpd=HTTPServer(server_addr,static_dir)
    #启动http server
    httpd.serve_forever()
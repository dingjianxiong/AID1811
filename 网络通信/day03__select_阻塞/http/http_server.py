from socket import *

#执行函数中处理客户端请求
def handle(connfd):
    print("客户端地址：",connfd.getpeername())#获取客户端地址
    request=connfd.recv(4096)#获取http请求
    #将请求按照行切割
    request_lines=request.splitlines()
    for  line in request_lines:
        print(line)
    #给浏览器客户端返回响应
    try:
        f=open("index.html")
    except IOError:
        response='HTTP/1.1 404 Not found\r\n'
        response+='\r\n'
        response+='=== sorry not found the page==='
    else:
        response="HTTP/1.1 200 ok\r\n"
        response+='\r\n'
        response+=f.read()
    finally:
        #将结果发送给客户端
        connfd.send(response.encode())
        #data='''HTTP/1.1 200 OK
        # Content-Encoding:gizp
        # Content-Type:text/html
        # <h1>welcome to python</h1>
        # <p>新年快乐,学习使我快乐</p>
        # ''' 
    # connfd.send(data.encode())
#在主函数中创建套接字
def main():
    sockfd=socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)#重用端口
    sockfd.bind(('0.0.0.0',6688))
    sockfd.listen(5)
    print("listen to the port 6688...")
    while True:
        connfd,addr=sockfd.accept()
        #处理客户端请求
        print(connfd)
        handle(connfd)
        connfd.close()
main()
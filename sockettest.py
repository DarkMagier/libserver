senddata="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1 style="background-color:red">我收到了你的请求！滚！</h1>

</body>
</html>
"""

import socket#导入socket包
import json
server=socket.socket()#建立socket连接对象
server.bind(('127.0.0.1',80))#将socket对象绑定ip和端口
server.listen()#监听端口
while True:
    conn,addr=server.accept()#等待有人连接
    request=conn.recv(1024)#接受请求信息
    print(request)
    if 'www.chinese.com'in request.decode():#Host: www.chinese.com
        conn.send('HTTP/1.1 200 OK\r\n\r\n'.encode(encoding='utf-8'))#发送http response 头
        conn.send('这是中文系'.encode(encoding='gbk'))#发送报文
    elif 'www.english.com'in request.decode():#Host: www.english.com
        conn.send('HTTP/1.1 200 OK\r\n\r\n'.encode(encoding='utf-8'))  # 发送http response 头
        conn.send('this is english major'.encode(encoding='gbk'))  # 发送报文
    # else:
    #     conn.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode(encoding='utf-8'))
    #     conn.send('没这个网页，滚。'.encode(encoding='gbk'))

    conn.close()
server.close()
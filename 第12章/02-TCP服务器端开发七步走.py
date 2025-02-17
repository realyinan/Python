import socket

# 1.创建套接字对象
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(tcp_server_socket)

# 2.绑定ip地址和端口号(本机或服务器地址) 注意参数类型是元组
tcp_server_socket.bind(("", 8080))

# 3.设置监听(让代码监听端口传过来的数据), 代表最大的连接数
tcp_server_socket.listen(128)

# 4.等待客户端连接
# 客户端与服务器端连接成功后, 信息的发送和接受都依赖新产生的套接字对象, 其内部保存了客户端和服务器端相关的信息
new_socket, ip_port = tcp_server_socket.accept()
print(new_socket)
print(ip_port)

# 5.接受客户端发送过来的数据
recv_data = new_socket.recv(1024)
recv_data= recv_data.decode('gbk')
print(f"{ip_port}: {recv_data}")

# 6.处理客户端请求并返回数据
new_socket.send("再见".encode('gbk'))

# 7.关闭套接字对象
tcp_server_socket.close()
new_socket.close()
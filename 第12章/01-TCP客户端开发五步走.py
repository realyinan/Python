import socket

# 1.创建套接字对象 socket.AF_INET -> ipv4, socket.SOCK_STREAM -> TCP协议
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4 TCP协议

# 2.与服务器建立连接
tcp_client_socket.connect(("192.168.0.106", 8080))

# 3.发送数据 (不可以是文本类型, 必须编码为字节流)
tcp_client_socket.send("Hello World".encode(encoding='utf-8'))

# 4.接受数据 (接收的为字节流数据, 需要解码为文本数据)
recv_data = tcp_client_socket.recv(1024)
recv_data = recv_data.decode(encoding='utf-8')
print(recv_data)

# 关闭套接字对象
tcp_client_socket.close()
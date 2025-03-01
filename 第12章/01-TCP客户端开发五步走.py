import socket

# 1.创建套接字对象 socket.AF_INET -> ipv4, socket.SOCK_STREAM -> TCP协议
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4 TCP协议

# 2.与服务器建立连接
tcp_client_socket.connect(("127.0.0.1", 8080))

# 3.发送数据 (不可以是文本类型, 必须编码为字节流)
tcp_client_socket.send("Hello World".encode(encoding='utf-8'))

# 4.接受数据 (接收的为字节流数据, 需要解码为文本数据)
recv_data = tcp_client_socket.recv(1024)
recv_data = recv_data.decode(encoding='utf-8')
print(recv_data)

# 5.关闭套接字对象
tcp_client_socket.close()


# TCP（三次握手，Three-Way Handshake）是TCP协议建立连接的过程，确保客户端与服务器之间的连接是可靠的。具体流程如下：

# 第1次挥手： A发送请求（ 随机数u）  
# 第2次挥手： B回消息（U+1）A确认U；关闭A到B的连接
# 第3次挥手： B发送消息（U+1，w）
# 第4次挥手：A回复消息（U+1, w+1）B确认w；关闭B到A的连接

# 四次挥手说TCP断开链接的时候需要经过4次确认。TCP连接是双向，A连接B、B连接A都要断开

# 第1次挥手： A发送请求（ 随机数u）  
# 第2次挥手： B回消息（U+1）A确认U；关闭A到B的连接
# 第3次挥手： B发送消息（U+1，w）
# 第4次挥手：A回复消息（U+1, w+1）B确认w；关闭B到A的连接


# TCP协议

# 全称叫: Transmission Control Protocol, 传输控制协议. 类似于: 打电话.
# 特点
# 面向有连接.
# 采用字节流的方式发送数据, 理论上无大小限制.
# 安全(可靠)协议.
# 传输效率相对较低.
# 区分客户端和服务器端.

# UDP协议
# 面向无连接. 类似于: 群聊
# 采用数据报包(package)的形式传输数据, 每个包的大小不能超过64KB.
# 不安全(不可靠)协议.
# 传输效率相对较高.
# 不区分客户端和服务器端, 叫: 发送端和接收端.


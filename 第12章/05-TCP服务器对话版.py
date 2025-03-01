import socket

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置端口复用
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

tcp_server_socket.bind(("", 8080))

tcp_server_socket.listen(128)

while True:
    try:
        new_socket, ip_port = tcp_server_socket.accept()
        while True:
            try:
                recv_data = new_socket.recv(1024)
                if len(recv_data) > 1:
                    recv_data = recv_data.decode('gbk')
                    print(f"{ip_port}: {recv_data}")

                content = input("本机: ").encode("gbk")
                new_socket.send(content)

            except ConnectionResetError:
                print("客户端连接已断开")

    except Exception as e:
        print("出错, 退出服务器监听")
        break

tcp_server_socket.close()



# 当 TCP 客户端程序想要和 TCP 服务端程序进行通信的时候必须要先建立连接
# TCP 客户端程序一般不需要绑定端口号，因为客户端是主动发起建立连接的。
# TCP 服务端程序必须绑定端口号，否则客户端找不到这个 TCP 服务端程序。
# listen 后的套接字是被动套接字，只负责接收新的客户端的连接请求，不能收发消息。
# 当 TCP 客户端程序和 TCP 服务端程序连接成功后， TCP 服务器端程序会产生一个新的套接字，收发客户端消息使用该套接字。
# 关闭 accept 返回的套接字意味着和这个客户端已经通信完毕。
# 关闭 listen 后的套接字意味着服务端的套接字关闭了，会导致新的客户端不能连接服务端，但是之前已经接成功的客户端还能正常通信。
# 当客户端的套接字调用 close 后，服务器端的 recv 会解阻塞，返回的数据长度为0，服务端可以通过返回数据的长度来判断客户端是否已经下线，反之服务端关闭套接字，客户端的 recv 也会解阻塞，返回的数据长度也为0。








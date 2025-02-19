import socket

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_server_socket.bind(("", 8080))

tcp_server_socket.listen(128)

while True:
    new_socket, ip_port = tcp_server_socket.accept()
    # print(ip_port)
    recv_data = new_socket.recv(1024)
    recv_data = recv_data.decode('gbk')
    print(f"{ip_port}: {recv_data}")
    content = "收到".encode('gbk')
    new_socket.send(content)
    new_socket.close()




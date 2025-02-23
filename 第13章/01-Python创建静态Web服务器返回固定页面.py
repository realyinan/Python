import socket

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

tcp_server_socket.bind(("", 9000))

tcp_server_socket.listen(128)

while True:

    new_socket, ip_port = tcp_server_socket.accept()

    client_request_data = new_socket.recv(1024).decode('utf-8')

    print(client_request_data)

    with open(r"第13章\Source\1.jpg", "rb") as f:
        data = f.read()

    # 1.响应行
    response_line = "HTTP/1.1 200 OK\r\n"
    # 2.响应头
    response_header = "Content-Type: image/jpeg\r\n" + "Server: PythonWebServer\r\n"
    # 3.空行

    # 4.响应体
    response_body = data

    response_data = (response_line + response_header + '\r\n').encode('utf-8') + response_body

    new_socket.send(response_data)

    new_socket.close()




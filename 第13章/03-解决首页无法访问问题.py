import socket

if __name__ == "__main__":

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server_socket.bind(("", 9000))

    tcp_server_socket.listen(128)

    while True:
        new_socket, ip_port = tcp_server_socket.accept()
        recv_data = new_socket.recv(1024)

        if recv_data:
            # 获取请求地址
            recv_data = recv_data.decode('utf-8')
            request_list = recv_data.split(' ', maxsplit=2)
            request_path = request_list[1]
            # print(request_path)

            # 判断用户请求的URL是否为"/"
            if request_path == "/":
                request_path = "/index.html"
            
            # 根据请求资源路径返回指定页面
            with open("第13章/Source" + request_path, "rb") as f:
                data = f.read()
            # 组装http相应报文
            response_line = "HTTP/1.1 200 OK\r\n"
            response_header = "Server: WebServer\r\n"
            response_body = data
            response_data = (response_line + response_header + "\r\n").encode("utf-8") + data
            new_socket.send(response_data)
            new_socket.close()

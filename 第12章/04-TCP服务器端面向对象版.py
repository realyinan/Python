import socket

class Webserver():
    def __init__(self):
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.bind(("", 8080))
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

    def handle_request(self, new_socket, ip_port):
        # 接送消息
        recv_data = new_socket.recv(1024)
        recv_data = recv_data.decode('gbk')
        print(f"{ip_port}: {recv_data}")

        # 发送消息
        content = "我已收到".encode('gbk')
        new_socket.send(content)

        # new_socket.close()

    def start(self):
        while True:
            new_socket, ip_port = self.tcp_server_socket.accept()
            self.handle_request(new_socket, ip_port)



ws = Webserver()
ws.start()
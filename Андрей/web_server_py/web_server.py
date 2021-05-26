import socket
import threading
from datetime import date


class ForbiddenError(Exception):
    pass


class DiscError(Exception):
    pass


class ThreadedServer():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target=self.listenToClient, args=(client, address)).start()

    def get_page(self, request_data, address):
        today = date.today()
        ip = address[0]
        path = request_data.split(' ')[1]
        try:
            if path == '/':
                path = "/index.html"
            elif path.split('.')[1] in ("png"):
                type = "image/png"
            else:
                type = "text/html"
            if path.split(".")[1] in ("html", "css", "js", "png"):
                with open('templates' + path, 'rb') as file:
                    response = file.read()
                HDRS = f'HTTP/1.1 200 0K\r\nDate: {today}\r\nContent-Type: {type}; charset=utf-8\r\nServer: Python\r\nContent-length: {len(response)}\r\nConnection: close\r\n\r\n'
                res = HDRS.encode('utf—8') + response
                code = 200
            else:
                raise ForbiddenError()
        except FileNotFoundError:
            response = "<H1>This page not found.</H1>"
            HDRS_404 = f'HTTP/1.1 404 0K\r\nDate: {today}\r\nContent-Type: text/html; charset=utf-8\r\nServer: Python\r\nContent-length: {len(response)}\r\nConnection: close\r\n\r\n'
            res = (HDRS_404 + response).encode('utf—8')
            code = 404
        except ForbiddenError:
            response = "<H1>Access denied!</H1>"
            HDRS_403 = f'HTTP/1.1 403 0K\r\nDate: {today}\r\nContent-Type: text/html; charset=utf-8\r\nServer: Python\r\nContent-length: {len(response)}\r\nConnection: close\r\n\r\n'
            res = (HDRS_403 + response).encode('utf—8')
            code = 403
        print(today, ip, path, code)
        return res

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size).decode('utf—8')
                if data:
                    content = self.get_page(data, address)
                    client.send(content)
                else:
                    raise DiscError('Client disconnected')
            except:
                client.close()
                return False

if __name__ == "__main__":
    port_num = 8787
    ThreadedServer('', port_num).listen()
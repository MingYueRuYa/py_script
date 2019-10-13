import socket
import threading
import json

server = socket.socket()
server.bind(("0.0.0.0", 8000))
server.listen()


def handle_sock(sock_, addr):
    while True:
        tmp_data = sock_.recv(1024 * 10)
        tmp_data = tmp_data.decode("utf8")
        print(tmp_data)
        request_line = tmp_data.splitlines()[0]
        if request_line:
            method = request_line.split()[0]
            path = request_line.split()[1]
            if method == "GET":
                response_template = '''HTTP/1.1 200 OK
        Access-Control-Allow-Origin: http://localhost:63342

        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
        <form action="/" method="POST" enctype="multipart/form-data">
            <input type="text" name="name"/>
            <input type="password" name="password">
            <input type="file" name="file">
            <input type="submit" value="登录">
        </form>

        </body>
        </html>

'''
                sock_.send(response_template.encode("utf8"))
                sock_.close()
                break
            elif method == "POST":
                response_template = '''HTTP/1.1 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: http://localhost:63342

{}

'''
                data = [
                    {
                        "name": "linux系统入门",
                        "teacher": "linux",
                        "url": "http://www.baidu.com"
                    },
                    {
                        "name": "shell编程",
                        "teacher": "shell",
                        "url": "http://www.baidu.com"
                    }
                ]
                sock_.send(response_template.format(json.dumps(data)).encode("utf8"))
                sock_.close()
                break

while True:
    sock, addr = server.accept()
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()

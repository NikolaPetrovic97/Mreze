import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        print("Poruka od {} :".format(self.client_address[0]))

        data = data.decode("utf-8")
        print(data)

        self.request.sendall(data.upper().encode())



HOST, PORT = "192.168.2.203", 34300
server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
server.serve_forever()
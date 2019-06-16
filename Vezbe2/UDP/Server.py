import socketserver
import json


class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        prijemStr = data.decode("utf-8")
        print("Poruka od {} :".format(self.client_address[0]))
        print(prijemStr)

        porukaZaSlanje = {1: 1, 2: 2, 3: 3}
        porukaZaSlanjeJOSN = json.dumps(porukaZaSlanje)
        porukaZaSlanjeBytes = porukaZaSlanjeJOSN.encode()
        socket.sendto(porukaZaSlanjeBytes, self.client_address)


HOST, PORT = "192.168.2.203", 34300
server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
server.serve_forever()

# 1. Samo slanje!
# 2. Prevodjenje, String u byte (samo broj bez recnika - liste)
# 3. Prevodjenje, podatak u JSON (komlikovaniji podatak)

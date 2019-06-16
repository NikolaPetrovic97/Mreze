import socketserver
import pickle
import random

class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        primljeniPodatak = self.request[0].strip()
        socket = self.request[1]

        y = pickle.loads(primljeniPodatak)


        if(y["komanda"] == "GET"):
            odgovor = str(random.randint(1,3))
        else:
            print(y)
            odgovor = 'Ok'
        porukaZaOdgovorByte = odgovor.encode()
        socket.sendto(porukaZaOdgovorByte, self.client_address)


HOST = "192.168.81.10"
PORT = 6500
server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
server.serve_forever()

import socketserver
import pickle
import random

class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        primljeni_podatak=self.request[0].strip()
        socket=self.request[1]
        
        y=pickle.loads(primljeni_podatak)

        if (y["komanda"]=="GET"):
            odgovor=str(random.randint(1, 3))
        else:
            print(y)
            odgovor="OK"
            
        poruka_za_odgovorByte=odgovor.encode()
        socket.sendto(poruka_za_odgovorByte, self.client_address)

HOST="192.168.81.10"
PORT= 6500

server=socketserver.UDPServer((HOST, PORT), MyUDPHandler)
server.serve_forever()

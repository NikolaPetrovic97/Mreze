import socketserver
from threading import Thread
import json
import random

komanda = 'komanda'

moguciParametriP = ['ime', 'prezime', 'indeks']
random.shuffle(moguciParametriP)
print(moguciParametriP)

opcijeMenija = ['kalkulator', 'zasticeno', 'izlaz']

users = {}

class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        primljenoByte = self.request[0].strip()
        socket = self.request[1]
        primljenoString = primljenoByte.decode()
        primljenoRecnik = json.loads(primljenoString)

        if(komanda in primljenoRecnik):
            k = primljenoRecnik[komanda].upper()
            print(k)
            if(k == 'L'):
                print("L -> P")
                key = random.randint(999,9999)
                users[key] = {moguciParametriP[0]:"",moguciParametriP[1]:""}
                self.send({
                    komanda:'P',
                    1:moguciParametriP[0],
                    2:moguciParametriP[1],
                    'key': key
                }, socket, self.client_address)
            elif(primljenoRecnik[komanda] == 'PL'):
                print("PL -> M")
                key = primljenoRecnik['key']
                users[key][moguciParametriP[0]] = primljenoRecnik['1']
                users[key][moguciParametriP[1]] = primljenoRecnik['2']
                self.send({
                    komanda: 'M',
                    1: opcijeMenija[0],
                    2: opcijeMenija[1],
                    3: opcijeMenija[1],
                    'key': primljenoRecnik['key']
                }, socket, self.client_address)
            elif (primljenoRecnik[komanda] == 'I'):
                print(primljenoRecnik)
                if('1' in primljenoRecnik):
                    izbor = primljenoRecnik['1']
                    key = primljenoRecnik['key']
                    if(izbor == 1):
                        print("Pitanje")
                    elif(izbor == 2):
                        print("S. Pitanje")
                    elif(izbor == 3):
                        code = random.randint(999999,9999999)
                        users[key]['code'] = code
                        print(users[key])
                        self.send({
                            komanda: 'E',
                            1: code
                        }, socket, self.client_address)





        # porukaZaSlanje = {1: 1, 2: 2, 3: 3}
        # porukaZaSlanjeJOSN = json.dumps(porukaZaSlanje)
        # porukaZaSlanjeBytes = porukaZaSlanjeJOSN.encode()
        # socket.sendto(porukaZaSlanjeBytes, self.client_address)

    def send(self, poruka, socket, adresa):
        porukaZaSlanje = poruka
        porukaZaSlanjeJOSN = json.dumps(porukaZaSlanje)
        porukaZaSlanjeBytes = porukaZaSlanjeJOSN.encode()
        socket.sendto(porukaZaSlanjeBytes, adresa)


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        print("Poruka od {} :".format(self.client_address[0]))

        data = data.decode("utf-8")
        print(data)

        self.request.sendall(data.upper().encode())



HOST, PORT = "192.168.2.203", 1212
serverUDP = socketserver.UDPServer((HOST, PORT), MyUDPHandler)

HOST, PORT = "192.168.2.203", 2121
serverTCP = socketserver.TCPServer((HOST, PORT), MyTCPHandler)


thread1 = Thread(target=serverTCP.serve_forever)
thread1.daemon = True
thread1.start()

thread2 = Thread(target=serverUDP.serve_forever)
thread2.daemon = True
thread2.start()

thread1.join()
thread2.join()
import socketserver
import pickle
import random

opcije={"komanda": "M", "1": " Nasumicni broj", "2": " Prognoza", "3": " Kalkulator", "0": " Izlaz"}

temperatura=random.randint(-25, 40)
vlaznost=random.randint(0, 100)
sansa_za_kisu=random.randint(0, 100)

login_zahtevi=[]
ulogovani_useri=[]

def send_data(socket, adresa, podatak):
    poruka_za_odgovor_byte=pickle.dumps(opcije)
    socket.sendto(poruka_za_odgovor_byte, self.client_address)

class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        primljeni_podatak=self.request[0].strip()
        socket=self.request[1]    
        y=pickle.loads(primljeni_podatak)
        print(y)
        if(y["komanda"]=="L"):
            code=random.randint(1000, 9999)
            login_zahtevi.append(code)

            odgovor={"komanda": "LZ", "code": code}
            send_data(socket, self.client_addres, odgovor)
            
        if(y["komanda"]=="Z"):
            print("Login: " + y["ime"] + " " + y["prezime" ] + " " + y["br"])
            send_data(socket, self.client_address, opcije)
        elif(y["komanda"]=="G"):
            send_data(socket, self.client_address, opcije)
        elif(y["komanda"]=="I"):
            if(y["izbor"]==0):
                send_data(socket, self.client_address, opcije)
            elif(y["izbor"]==1):
                broj=random.randint(1, 100)
                odgovor={"komanda": "B", "broj": broj}
                send_data(socket, self.client_address, odgovor)
            elif(y["izbor"]==2):
                odgovor={"komanda": "P", "t": temperatura, "v": vlaznost, "s": sansa_za_kisu }
                send_data(socket, self.client_address, odgovor)
            elif(y["izbor"]==3):
                broj1=y["broj1"]
                broj2=y["broj2"]
                operacija=y["operacija"]
                if(operacija=="+"):
                    rezultat=broj1 + broj2
                elif(operacija=="-"):
                    rezultat=broj1 - broj2
                elif(operacija=="*"):
                    rezultat=broj1 * broj2
                elif(operacija=="/"):
                    rezultat=broj1 / broj2

HOST="192.168.81.60"
PORT= 6500

server=socketserver.UDPServer((HOST, PORT), MyUDPHandler)
server.serve_forever()


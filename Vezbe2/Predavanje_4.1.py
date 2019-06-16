import socket
import pickle

HOST="192.168.81.60"
PORT=6500

podatak=input(">")

podatak={"komanda": "Z"}
podatak_byte=pickle.dumps(podatak)
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(podatak_byte, (HOST, PORT))

podatak={"komanda": "L", "ime": "Nikola", "prezime": "Petrovic", "br": "IT-02-29/2016"}
podatak_byte=pickle.dumps(podatak)

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(podatak_byte, (HOST, PORT))
primljeni_odgovor_recnik={"komanda": ""}

def send_data(sock, podatak):
    podatak_byte=pickle.dumps(podatak)
    sock.sendto(podatak_byte, (HOST, PORT))

def print_prognoza(primljeni_odgovor_recnik):
    print("Temperatura" + str(primljeni_odgovor_recnik["t"]))
    print("Vlaznost" + str(primljeni_odgovor_recnik["v"]) + "%")
    print("Sanse za kisom" + str(primljeni_odgovor_recnik["s"]) + "%")

def ispis_menija(primljeni_odgovor_recnik):
    for i in primljeni_odgovor_recnik:
        if(i!= "komanda"):
            print(i + "." + primljeni_odgovor_recnik[i])

while (primljeni_odgovor_recnik["komanda"]!="E"):
    primljeni_odgovor=sock.recv(1024)
    primljeni_odgovor_recnik=pickle.loads(primljeni_odgovor)

    if(primljeni_odgovor_recnik["komanda"]=="M"):
        ispis_menija(primljeni_odgovor_recnik)
        izbor=int (input(">"))
        if(izbor==3):
            podatak["broj1"]=int(input("broj1= "))
            podatak["broj2"]=int(input("broj2= "))
            podatak["operacija"]=input("operacija: ")#dorada pomocu menija
        send_data(sock, podatak)
    elif(primljeni_odgovor_recnik["komanda"=="B"]):
        print(primljeni_odgovor_recnik["broj"])
        send_data(sock, {"komanda": "G"})
    elif(primljeni_odgovor_recnik["komanda"=="P"]):
        print_prognoza(primljeni_odgovor_recnik)
        send_data(sock, {"komanda": "G"})
        
                                                    
print("Klijent je zavrsio sa radom")



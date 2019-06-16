import socket
import pickle

HOST="192.168.81.10"
PORT=6500

podatak={"ime": "Nikola", "prezime": "Petrovic", "broj_indeksa": "IT-02-29/2016"}
while (podatak !="Exit"):
    podatak=input(">")

    podatak={"komanda": "GET"}
    podatakByte=pickle.dumps(podatak)

    sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(podatakByte, (HOST, PORT))

    primljeni_odgovor=sock.recv(1024)
    primljeni_odgovorString=primljeni_odgovor.decode("utf-8")

    dal=False
    if(primljeni_odgovorString == "1"):
        podatak={"ime": "Nikola"}
        dal=True
        
     elif (primljeni_odgovorString == "2"):
         podatak={"prezime": "Petrovic"}
         dal=True
         
    elif (primljeni_odgovorString == "3"):
            podatak={"broj_indeksa": "IT-02-29/2016"}
            dal=True
            
    elif(primljeni_odgovorString == "OK"):
            print("Gotov zadatak")

    if(dal):
         podatakByte=pickle.dumps(podatak)

        sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(podatakByte, (HOST, PORT))



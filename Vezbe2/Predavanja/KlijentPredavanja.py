import socket
import pickle


HOST, PORT = "192.168.81.10", 6500

podatak = ""
while(podatak != "Exit"):
    podatak = input(">")

    podatak = {'komanda': 'GET'}  # recnik
    podatakByte = pickle.dumps(podatak)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(podatakByte, (HOST, PORT))

    primljniOdgovor = sock.recv(1024)
    primljniOdgovorString = primljniOdgovor.decode("utf-8")

    if(primljniOdgovorString == "1"):
        print("Jedan")
    if (primljniOdgovorString == "2"):
        print("Dva")
    if (primljniOdgovorString == "3"):
        print("Tri")
    if(primljniOdgovorString == "Ok"):
        print("Gotov zadatak")



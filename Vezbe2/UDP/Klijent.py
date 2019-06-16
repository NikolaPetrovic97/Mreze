import socket
import json

HOST, PORT = "192.168.2.203", 1212
poruka = ""

while (poruka != "Exit"):
    poruka = input("Poruka: ")

    # Slanje -----------------------------------------------------------
    porukaByte = poruka.encode()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(porukaByte, (HOST, PORT))
    # ------------------------------------------------------------------

    # Prijem -----------------------------------------------------------
    primljenoByte = sock.recv(1024)
    primljenoString = primljenoByte.decode()
    primljenoRecnik = json.loads(primljenoString)
    print(primljenoRecnik)
    # ------------------------------------------------------------------

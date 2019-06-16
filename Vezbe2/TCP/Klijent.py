import socket
import sys
data = "Poruka"
while (data != "Exit"):
    HOST, PORT = "192.168.2.203", 2121
    VELICINA_BUFFERA = 1024
    data = input("Poruka: ")
    data = data + "\n"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.send(data.encode())  # posalji poruku

    received = sock.recv(VELICINA_BUFFERA)
    sock.close()
    print(received.decode()) #ispisi sta je server vratio
import socket
import json

HOST, PORT = "192.168.2.203", 1212
poruka = ""

parametri = {
    'ime': 'Filip',
    'prezime': 'vasic',
    'indeks': '123'
}


def send(poruka):
    poruka = json.dumps(poruka)
    porukaByte = poruka.encode()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(porukaByte, (HOST, PORT))
    return sock


poruka = {'komanda': 'L'}
poruka = json.dumps(poruka)
porukaByte = poruka.encode()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(porukaByte, (HOST, PORT))

while True:
    primljenoByte = sock.recv(1024)
    primljenoString = primljenoByte.decode()
    primljenoRecnik = json.loads(primljenoString)
    print(primljenoRecnik)
    if ('komanda' in primljenoRecnik):
        k = primljenoRecnik['komanda']
        if (k == 'P'):
            print("P -> PL")
            sock = send({
                'komanda': 'PL',
                1: parametri[primljenoRecnik['1']],
                2: parametri[primljenoRecnik['2']],
                'key': primljenoRecnik['key']
            })
        elif (k == 'M'):
            print("M -> I")
            i = int(input("Izbor: "))
            sock = send({
                'komanda': 'I',
                1: i,
                'key': primljenoRecnik['key']
            })
        elif(k == 'E'):
            print("Exit...")
            break

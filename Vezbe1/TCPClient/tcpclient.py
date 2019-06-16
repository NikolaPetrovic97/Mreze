# client.py  
import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()                           
port = 9997

class MySock:
    def __init__(self):
        print("init class")
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("exit class")
        s.close()

s.connect((host, port))                              

with MySock() as t:
    while True:
        print("Ocekuje se unos poruke:")
        msg = sys.stdin.readline()
        if msg == "q\n": break
        print("Salje se poruka...")
        s.send(msg.encode('utf-8'))
        print("Prijem poruke...")
        res = s.recv(1024)
        print(res.decode("utf-8"))



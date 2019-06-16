# server.py 
import select
import socket
import sys

SOCKET_LIST = [sys.stdin]

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()   
print(host)
port = 9997
serversocket.bind((host, port))  
serversocket.listen(5)                                           

SOCKET_LIST.append(serversocket)

run = True
while run:
    print("Ceka se prijem podataka...")
    ready_to_read, ready_to_write, in_error = select.select(SOCKET_LIST, [], [])#, 0)
    for sock in ready_to_read:
        if sock == sys.stdin:
            msg = sys.stdin.readline()
            if msg == "q\n":
                run = False
                break
        elif sock == serversocket:
            sockfd, addr = serversocket.accept()
            SOCKET_LIST.append(sockfd)
            print("Client (%s, %s) connected" % addr)
        else:
            try:
                print("Prijem podataka...")
                data = sock.recv(1024)
                if len(data) == 0:
                    SOCKET_LIST.remove(sock)
                    continue
                res="prijem potvrdjen"
                print(data.decode("utf-8"))
                sock.send(res.encode("utf-8"))
            except:
                continue

    
sock.close()


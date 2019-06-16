import socket
import sys
    
if(len(sys.argv) < 3):
    print('Usage : python fileserver.py hostname port')
    sys.exit()

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)

# connect to remote host
try:
    s.connect((host, port))
except:
    print('Unable to connect')
    sys.exit()
        
s.send(("Hello server!").encode('utf-8'))

with open('received_file', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data.decode("utf-8")))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')
import socket

# Inicijalizuje se UDP soket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server ocekuje komunikaciju na lokalnoj adresi, port 10000
server_address = ('localhost', 10000)
print('server pokrenut na adresi %s port %s' % server_address)
sock.bind(server_address)
while True:
    print('\nocekuje se prijem poruke...')
    data, address = sock.recvfrom(4096)
    
    print('primljena poruka duzine %s bajta sa adrese %s' % (len(data), address))
    # Python stringovi su u Unicode formatu, pa je potrebno dekodovati bytestream
    # za pravilno prikazivanje
    print(data.decode('utf-8'))
    
    if data:
        sent = sock.sendto(data, address)
        print('poslata poruka duzine %s bajta nazad na adresu %s' % (sent, address))
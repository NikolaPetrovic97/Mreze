import socket
import sys

# Inicijalizuje se UDP soket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = 'Ovo je tekst poruke koja se salje!'

try:

    # Send data
    print('salje se poruka: "%s"' % message)
    # Python stringovi su u Unicode formatu, pa je potrebno enkodovati
    # tekst da bi se formirao ispravan bytestream za slanje
    sent = sock.sendto(message.encode('utf-8'), server_address)

    # Receive response
    print('ocekuje se prijem poruke...')
    data, server = sock.recvfrom(4096)
    # Python stringovi su u Unicode formatu, pa je potrebno dekodovati bytestream
    # za pravilno prikazivanje
    print('primljena poruka: "%s"' % data.decode('utf-8'))

finally:
    print('soket se zatvara i izlazi iz aplikacije...')
    sock.close()
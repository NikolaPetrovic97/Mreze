import socket
import sys
import pickle
import random
from time import sleep

client_list = []

in_port = 10001
out_port = 10002
# login socket
#slogin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#slogin.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#slogin.bind(('', login_port))
#slogin.listen(5)

# update socket
sin = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sin.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sin.settimeout(0)
sin.bind(('', in_port))

sout = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sout.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# sout.settimeout(0.5)
sout.bind(('', out_port))

print("starting up on port %d" % in_port)

while True:
#    Incomming, wlist, xlist = select.select([slogin, supdate], [], [], 0.05)
#    for conn in Incomming:


    try:
        for i in range(100):
            data, address = sin.recvfrom(4096)

            if data:
                dt = pickle.loads(data)
                if dt[0] == "l":
                    c = ["p", len(client_list) + 1, random.randint(0, 600), random.randint(0, 600), random.randint(0, 0xffffffff), address]
                    sent = sout.sendto(pickle.dumps(c), address)
                    c[0] = "u"
                    client_list.append(c)
                    print('received login from %s port %s, assigned id %d' % (address[0], address[1], len(client_list)))
                    break
                if dt[0] == "o":
                    for cl in client_list:
                        if cl[1] == dt[1]:
                            client_list.remove(cl)
                            print('client id %d removed, clients connected %d' % (cl[1], len(client_list)))
                if dt[0] == "u":
                    for cl in client_list:
                        if cl[1] == dt[1]:
                            cl[2] = dt[2]
                            cl[3] = dt[3]
                            #print >> sys.stderr, 'client %d position updated to %d, %d, with color %d' % (cl[1], cl[2], cl[3], cl[4])
    except Exception as e:
        pass

    if len(client_list) > 0:
        lst = pickle.dumps(client_list)
        for cl in client_list:
            #print >> sys.stderr, 'sending update to client %s with id %d' % (cl[5], cl[1])
            sout.sendto(lst, cl[5])
        
    sleep(1/30)
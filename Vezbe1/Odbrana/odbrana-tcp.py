#importuju se moduli
import socket
import pickle

#otvaranje soketa
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.4.10"
port = 9997
#konekcija sa serverom(cini mi se da je rekao da za ovo ide 5 bodova XD)
s.connect((host,port))

#prvi najbitniji blok
#pravljenje liste koja ce se poslati serveru(prvi deo "l" govori
# serveru da se logujete i on ce poslati nazad pitanja
l = ("l", "IT-03-12/2016", "Kosta", "Plecevic")
#slanje liste
s.send(pickle.dumps(l))

#pravimo petlju koja ce da ide sve dok je ne prekinemo
while True:
    #ovde u petlji primamo podatke koje nam server posalje svaki put kad ona krene ispocetka
    data = s.recv(4096)
    #ovde otpakujemo te podatke i stavimo u p, koje je sada lista
    p = pickle.loads(data)
    #pravimo k listu koja sadrzi samo argument za slanje odgovora serveru
    k = ["a"]
    #radi sprecavanja gresaka, ovde pravimo promenljivu resenje, gde ce se ubacivati resenje zadatka
    resenje = ""
    #sad, kad su podaci otpakovani, proveravamo da li je prvi clan liste q(question) ili e(end),
    #to su jedina dva argumenta koja server moze da nam posalje
    if p[0] == "q":
        #ako je q, onda znaci da nam server salje pitanje, pa proveravamo koja je operacija u pitanju
        #operacija se nalazi na drugom mestu u listi, tako da je broj indeksa 1
        if p[1] == "+":
            #dva broja koja se salju uz operaciju su na indeksnom mestu 2 i 3,
            # pa se ovako moze raditi sa njima
            resenje = p[2] + p[3]
        elif p[1] == "-":
            resenje = p[2] + p[3]
        elif p[1] == "*":
            resenje = p[2] + p[3]
        elif p[1] == "/":
            resenje = p[2] + p[3]
        #nakon odradjivanja jedne od operacija resenje ce se dodati u listu k
        #nakon dodavanja resenja, k ce izgledati ovako ["a", resenje]
        k.append(resenje)
        #nakon sredjivanja liste, istu saljemo serveru kao odgovor
        s.send(pickle.dumps(k))
    #ako je server poslao listu sa prvim argumentom e(end),
    # onda znaci da je primio odogovor na sva pitanja koja je postavio,
    # i da je poslao rezultat koji cemo odstampati na ekranu sa komandom ispod
    elif p[0] == "e":
        print(p[1])
        #nakon ispisivanja na ekranu, sa break prekidamo while petlju
        break
#sa ovim zatvaramo socket(ovo je najvaznije pored prvog bloka i mora se odmah napisati)
s.close()

#znaci, while petlja ce da ide, i da prima od servera sve dok on ne posalje listu sa prvim
# argumentom e, bilo da je u medjuvremenu poslato 1 ili 1001 pitanje
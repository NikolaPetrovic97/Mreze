import json

podatak = {"ime": "Filip", "prezime": "Vasic"} #recnik
x = json.dumps(podatak)                        #prevodimo recniku string
print(x[0])                                    #x je string

y = json.loads(x)                              #prevodimo string u recnik
print(y["ime"])                                #ispisujemo podatak po kljucu
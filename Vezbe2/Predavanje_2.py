import json

podatak={"ime": "Nikola", "prezime": "Petrovic"}
x=json.dumps(podatak)
print(x[0])

y=json.loads(x)
print(y["ime"])

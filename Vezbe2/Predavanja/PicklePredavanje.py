import pickle

podatak = [1,2,3]
x = pickle.dumps(podatak)       #prevodimo podatak u byte
print(x)

y = pickle.loads(x)             #prevodimo byte u podatak
print(y)
import pickle

podatak=[1, 2, 3]
x=pickle.dumps(podatak)
print(x)

y=pickle.loads(x)
print(y)

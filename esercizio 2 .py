import random
#sapendo che  la funzione random. radint(start,end)
#genera un numero intero compreso trastart e end, end compreso
#costruire una lista di numeri casuali lunga 100
#stampare la somma di tutti i numeri

import random

lista=[]

for x in range (100):
    Numerox=random.randint(1,10)
    lista.append(Numerox)

SommaRandom=sum(lista)

print(SommaRandom)

#oppure
inc =[]
for i in range(100):
    inc.append(random.randint(1, 10))

for i in [7, 8, 9]:
    print(i)
    #coi il for fà stampare gli elementi della collezzione



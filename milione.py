#calcola la somma 
import random

lista=[]



#generatore randomico

for y in range(1000001):
    NumeroRandom=random.randint(1,1000001)
    lista.append(NumeroRandom)

SommaRandom=sum(lista)

print(SommaRandom)

#media 

media=SommaRandom/1000000

print(media)
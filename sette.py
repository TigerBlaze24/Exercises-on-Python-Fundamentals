import random
import time 

"""start=time.time_ns()
lista=[]
for v in range(1,10000000):
    lista.append(random.randint(1,1000))

end=time.time_ns()

print(f"il tempo richiesto è: {(end-start)/10000000}")

import random
import time

# Costruzione della lista
start = time.time_ns()
lista = []
for v in range(1, 10000000):
    lista.append(random.randint(1, 1000000000))
end = time.time_ns()

print(f"Il tempo richiesto è: {(end-start)/1000000000}")

# Ricerca nella lista
start = time.time_ns()
trovati = 0

for v in range(1, 10000000):
    if random.randint(1, 1000000000) in lista:
        trovati += 1
end = time.time_ns()

print(f"Il tempo richiesto per cercare è: {(end-start)/1000} e ne ha trovati {trovati}"
) """
#####################################costruzionnede set#
start = time.time_ns()
aset = set()
for v in range(1, 10000000):    
        aset.add(random.randint(1, 1000000000))
end = time.time_ns()

print(f"Il tempo richiesto è: {(end-start)/1000000000}")

start = time.time_ns()
trovati = 0
for v in range(1, 10000000):
    if random.randint(1, 1000000000) in aset:
        trovati += 1
end = time.time_ns()

print(
    f"Il tempo richiesto per cercare è: {(end-start)/1000000000} e ne ha trovati {trovati}"
)
#il set è più veloce della lista perchè mantiene i numeri all'interno di esso

print(hash("mario")%17)
#esempio di hash
#scriverre una funzion colore casuale()che torna una stringa
#casuale tra "rosso""verde "blu""arancio "ciano
import random

def colorecasuale():
   colori =["rosso","giallo","verde","blu","arancio","ciano","rosa","turchese"]
   return colori[random.randint(0, len(colori)-1)]

print(colorecasuale())
print(colorecasuale())
print(colorecasuale())
print(colorecasuale())
    

#stabilisce qual'è il numero maggiore:
print(max(10,20))


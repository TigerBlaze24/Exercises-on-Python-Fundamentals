fin = open("alice.txt", "r")
linee = fin.readlines()  #legge tutte le linee
fin.close() #con questo comando si chiude il file

l1=[]
 
for l in linee:
    l1.append(l.strip()) #questa funzione fa tornare una copia della stringain cui toglie:
                         #spazi, tabulazione e fine riga,ma funziona solo all'inizio e fine riga


linee=l1
print(linee)

#esercizio con split
s = "alfa;beta;gamma"
print(s.split(";"))

#dato alice.txt, stampare, una per riga,tutte le parole che la compongono:
fin = open("alice.txt", "r") #fin.(funzione che trova un file) open(apre il file)
linee = fin.readlines()

parole =[]

for l in linee:
    parole.extend(l.split(" "))

print(parole)

#data una lista di stringhe , eliminare nella lista tutte le stringhe vuote

ls = ["uno","","due", "tre", "", " ", "", "fine"]

lnuova=[]

for i in ls:
    
    if len (i.strip()) >0:
        lnuova.append(i)

print(lnuova)


#contare quanti caratteri ci sono in alice.txt e poi contare quanti caratteri con spazi bianchi
#infine contare quanti caratteri alfanumerici[a-2A-z0-9]ci sono in alice. txt

fin = open ("alice.txt", "r")
linee = fin.readlines()
fin.close()

tot=0

for linea in linee:
    tot = tot + len (linea)

print("caratteri: ",tot)

#2)

fin = open("alice.txt" , "r")
alice=fin.read()
fin.close()
notblank=0
for c in alice:
    if c!=" ":
        notblank += 1

print("notblank ",tot)

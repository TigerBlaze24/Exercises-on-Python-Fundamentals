fin = open("alice.txt", "r")
linee = fin.readlines()  #legge tutte le linee
fin.close()

l1=[]
 
for l in linee:
    l1.append(l.strip()) #questa funzione fa tornare una copia della stringain cui toglie:
                         #spazi, tabulazione e fine riga,ma funziona solo all'inizio e fine riga


linee=l1
print(linee)



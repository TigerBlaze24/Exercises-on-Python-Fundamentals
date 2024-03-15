fin = open("persone.csv" , "r")
persone = fin.readlines()
fin.close()

lista=[]
print(persone)

for Y in persone:
    print(Y) #così la stampa non và bene perchè ci sono gli spazi bianchi e endline(/n)
    
    lista.append(Y.strip().split(","))
#per togliere/n tab e gli spazi binchi, tab e endline(/n) uso stri e poi split per dividere le liste dove c'èla virgola


    
for l in lista:# l è l'elemento contatore in un ciclo
    print("Nome: ", l[0] , "cognome" , l[1] , "età" , l[2])


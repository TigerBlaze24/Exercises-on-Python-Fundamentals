lista=[2,3,4]
lista3=[y for x in lista for y in range(1, x) ]
print(lista3)

nomi=["mario","blanco","verde"]
cognomi=["rossi","bianchi","verdi"]
coppie= list(zip(nomi, cognomi))
print(coppie)
#esercizio con l'operatore zip(che unisce due elementi)

numero =""
virgola=False
while True:
    c = input("Digita 0-9,+-*/=: ")

    if len(c)>0:
        c=c[0]

    if c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ","]:
        print("il numero è", numero)
        break
    elif c==",":
        if not virgola:  
            numero = numero + c 
        else:
          continue
    
#Maria Paola Bongiorno
#18/04/2024


#2.3)usa una variabile per rappresentare un nome di una persona, stampa il messaggio della persona
name :str = "Mary"
print("ciao ti và di mparare un pò di python insieme?")
#oppurecosì in cui la variabile contiene il messaggio
message: str = f"ciao{name}, ti và di imparare un pò di python insieme?"

#2.4)
#questa variabile contiene il nome di una persona
name: str ="luca"

#questa variabile contiene il nome in minuscolo
name_lower: str = name.lower()

#questa variabile contiene il nome in maiuscolo
name_upper: str = name.upper()

print( f" {name}, {name.lower} ,{name.upper}")



#2.5)
autore :str='Giuliocesare'
frase = "quoue tu bruts fili mi"
print(frase)

#2.6)
famousperson:str="famousperson"
message = "piange il telefono"
print(message)

#2.8)
filename:str ="prova.txt"
print(filename.removesuffix(".txt"))

#3.1)
name =["luca","elena","gino" , "giuseppe"]
print(name[0])
print(name[1])
print(name[2])
print(name[3])

#3.2)
print("ciao best " , name[0] , "come stai?")
print("ciao tata", name[1] ,"stai andado a casa?")
print("ciao bello" , name[2] , "vieni al cinema?")
print("ciao splendore" , name[3] , "vieni dal paninaro stasera?")

#3.3)
car :list =["Mercedes","Ferrari","Lamborghini","Maserati"]
message :list= ["vorreiguidare una", "mi piacerebbe avere una","mi piacerebbe comprarne una","desidero una"]
print(message[0] , car[0])

#3.4)
guests : list =["Terenzio" ,"Fabrizio" , "Annibale", "Marco"]
for name in guests :
    print(name, " vieni a cena?")


#3.5)
print("Terenzio")
guests[0]= "Tommaso"

for name in guests :
    print(name, " vieni a cena?")

#3.6)
print("ragazzi ho trovato un tavolo più grande")
guests.insert(0, "Cesare")
guests.insert(2, "Nerone")
guests.append("Caio")

print(guests)






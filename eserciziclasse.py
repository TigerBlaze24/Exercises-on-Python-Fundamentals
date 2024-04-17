d={ "pippo":2 ,"pluto":1, "topolino" : 5}

keys = list(d.keys())
i = 0
somma = 0
while i < len(keys):
    key = keys[i]
    val = d[key]
    somma = somma + val
    i += 1

print(somma)
#farlo con il for
somma = 0
for key in d:
    somma = somma + d[key]  

print(somma)

#esempio per prendere chiave e valore in un dizionario con un ciclo:
# for chiave , valore, in d.items()
#print (chiave valore) [puoi printarlo o fare ciò che vuoi]

d = {"pippo " :2,"pluto":1 ,"topolino":5}
somma = sum(list(d.values()))
d1 = {"pippo":0.25,"pluto":0.125,"topolino":0.625}
#valori finali di d1 si avranno facendo la somma di vecchi diviso i nuovi
d1={}
somma = sum (list(d.values()))
for k , v in d.items():
    d1[k] = v / somma

print(d1)
#creare un dizionario con questi valori:
l=[1,2,3,3,4,5,2,2,6,3,7,16]
d ={"somma_pari":0 ,"somma_dispari":0}
for elem in l:
    if elem % 2 == 0:
        d["somma_pari"]+=elem
    else:
        d["somma_dispari"]+=elem
print(d)

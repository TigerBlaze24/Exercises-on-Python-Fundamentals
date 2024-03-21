#6)Quanti calciatori hanno giocato per l'italia?

import json

filejson = open("es jason allworld-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()
calcita = 0
for i in worldcup:
    if i["Team"] == "ITA":
        calcita += 1
    elif i["Team"] == "Italy":
        calcita += 1
    else:
        continue
print("Calciatori italiani: ", calcita)

#6)
calciatore_piu_giovane = None
eta_piu_giovane = 200
for giocatore in worldcup:
    campionato = giocatore["Year"]
    data_di_nascita = giocatore['DateOfBirth']
    if data_di_nascita:
        anno_di_nascita = int(data_di_nascita.split('-')[0])
        eta = campionato - anno_di_nascita


        if eta < eta_piu_giovane:
            eta_piu_giovane = eta
            calciatore_piu_giovane = giocatore
print("Il calciatore più giovane è:" , calciatore_piu_giovane,eta_piu_giovane)
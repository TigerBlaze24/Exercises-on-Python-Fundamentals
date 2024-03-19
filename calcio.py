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

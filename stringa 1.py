#ho una stringa "123" la voglio trasformare in  [1, 2,3]
#definisci la funzione che risolva il problema

def trasfstringa(sd):
   listacifre=[]    
   for x in sd:
      listacifre.append(int(x)) 
   return listacifre
   
print(trasfstringa("123"))   


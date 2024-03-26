##GENERA UNA LISTA CHE CONTIENE NUMERI CASUALI DA 1 A N e contare quanti numeri uguali ci sono
import random

def generalista (N):
        ls=[]
        lscheck=[]
        for i in range(N):
            v= random.randint(1,N)
            ls.append(v)
        return ls
print(generalista(10))

def contauguali(ls,lschecheck): 
        uguali=0
        for i in range(len(ls)):#len(lunghezzadellalista)
            if ls[i]== lschecheck[i]:   
                  uguali = uguali + 1
        return uguali
N=8
ls=generalista(N)
lschecheck=generalista(N)
print(ls)
print(lschecheck)
print(contauguali(ls , lschecheck))
#ultima parte:
#[1, 1, 4, 3, 1]#[4, 2, 1, 3, 2] (4 e 1)
#[5, 5, 3, 1, 4]=1
#[5, 4, 2, 5, 5] (5,4)

#[5, 1, 3, 2, 4]
#[1, 5, 4, 4, 2] (1, 5,4,2)
#[3, 2, 3, 4, 5]
#[1, 5, 4, 5, 5](4)



def contaugualidiverso(ls,lschecheck):
    ls= [1,4,3,4,6,2]
    lschecheck= [2,4,4,8,6,1]
    stessoposto=0
    for i in range(len(lschecheck)):
        if lschecheck[i]==ls[i]:
            stessoposto += 1  
            ls[i] = -1
            lschecheck[i] = -1
            
            

      
         


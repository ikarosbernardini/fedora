# Vanligversion
test = True
if test == True:
    tal = 34
else:
    tal = 0


# Snabbversion av if 
tal = 34 if test==True else 0 


# Vanligversion
for x in range(10):
    lista = x 


# Snabbversion av for 
lista =  [x for x in range(10)] 

def addera(tal1, tal2):
    return tal1 + tal2

def returnera(tal1, tal2):
    return tal1, tal2

värden = returnera(32, 43)

värde1,värd2 = returnera(32, 43)

for i,value in enumerate(["A","B","C","D"]):
    print(f"index={str(i)} och value = {value}")

    #v1,v2 = tal1, tal2, 

for value in {"A":"1","B":2,"C": "text"}.values():
    pass 
for key in {"A":"1","B":2,"C": "text"}.keys():
    pass 
for key,value in {"A":"1","B":2,"C": "text"}.items():
    pass 



Lista = [1,2,3,4,5,6,3,4]
Dict = {1:"Hello",2:"World",3:"!"}
Tuple = (42, 23) = 42, 23  

set(Lista) # tar borta alla dubbletter och läser enbart in unika värden. bra för att sortera ut objekt som vi ej vill ha dubbelt av. 


# Decorator, kör annan kod innnan och/eller efter er kod .
@test()
def addera(tal1, tal2):
    pass 


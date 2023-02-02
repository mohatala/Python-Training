import random
import string

#print(ord("A"))
#print(chr(80))

#l=[1,2,5,4]
#print(random.sample(l,3))
   #Methode 1  
L1 = string.ascii_uppercase
L2 = string.ascii_lowercase
L3=string.digits

password=random.sample(L1,5)+random.sample(L2,5)+random.sample(L3,3)
print("Methode 1 ")
print(password)

s=""
print(s.join(random.sample(password,len(password))))


######################################################"
#Methode 2
def generermp(c1,c2,n):
    x=ord(c1)
    y=ord(c2)
    lower=list(range(x,y+1))
    i2=random.sample(lower,n)
    return i2

mdp=generermp("a","z",5)+generermp("A","Z",5)+generermp("1","9",3)
mdp=random.sample(mdp,len(mdp))
print("Methode 2 ")
print(mdp)
mdp2=""
for ch in mdp:
    mdp2+=(chr(ch))
print(mdp2)
    
    








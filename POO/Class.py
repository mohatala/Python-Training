

class Employe:
    #Constructeur D'initialisation
    def __init__(self,n,no,s):
        self.n=n
        self.nom=no
        self.salaire=s
    def __str__(self):
        ch=str(self.n)+":"+self.nom+":"+str(self.salaire)
        return(ch)
    def __eq__(self,other):
        return(self.nom==other.nom and self.salaire==other.salaire)
    

E1=Employe(1,"a",10000)
E2=Employe(2,"a",10000)
E3=Employe(3,"yassin",8000)
E4=Employe(4,"amal",20000)
#print(E1)

societe=[E1,E2,E3,E4]

#print(societe[2].nom)

def masssalaire():
    somme=0
    for item in societe:
        somme=somme+item.salaire
    return(somme)

print(masssalaire())

def moyen_salaire():
    som=masssalaire()
    moyen=som/len(societe)
    return(moyen)

print(round(moyen_salaire(),2))

def salaire_max():
    s=[]
    for item in societe:
        s.append(item.salaire)
    m=max(s)
    for item in societe:
        if item.salaire==m:
            return(item.nom,item.salaire)
        
x,y=salaire_max()
print(x,y)

def salaire_max_index():
    s=[]
    for item in societe:
        s.append(item.salaire)
    m=max(s)
    pos=s.index(m)
    return(societe[pos].nom)

print(salaire_max_index())

def plusieur_salaire_max():
    s=[]
    l=[]
    for item in societe:
        s.append(item.salaire)
    m=max(s)
    for item in societe:
        if item.salaire==m:
            l.append(item.nom)
    return(l)        
        
x=plusieur_salaire_max()
print(x)

print(E1==E2)
if E1==E2:
    print("E1 et E2 sont equivalent")

#les listes
l=[10,5,8,6]
#add 7 in back of the list
l.append(7)
print(l)
#add 2 in the index 0 in the list
l.insert(0,2)
print(l)
#delete item from list using the index
l.pop(-1)
print(l)
#delete item from list using value
l.remove(5)
print(l)
#search index using value
x=l.index(8)
print(x)

l2=[2,1,2,-7,3,2]
x=l2.index(2)
print(x)

#fonction pour chercher dans liste avec une valeur
def index2(l,y):
    t=[]
    i=0
    for item in l:
        if item==y:
            t.append(i)
        i+=1

    return(t)

print(index2(l2,3))
            
    

    

        


    
    

    
    

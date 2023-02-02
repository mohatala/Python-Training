class Employe:
    valeur=12
    def __init__(self,mat,nom,insal):
        self.matricule=mat
        self.nom=nom
        self.indice_salarial=insal

    def __str__(self):
        ch=str(self.matricule)+" "+self.nom+" "+str(self.indice_salarial)
        return ch

    def Salaire(self):
        s=self.valeur*self.indice_salarial
        return s


#e1=Employe(1,"med",5)
#e2=Employe(2,"mt",2)
#print(e1.Salaire())
#Employe.valeur=10
#print(e2.Salaire())


class Responsable(Employe):

    def __init__(self,mat,nom,insal,L):
        Employe.__init__(self,mat,nom,insal)
        self.inf=L
    def __str__(self):
        ch=Employe.__str__(self)
        for i in self.inf:
            ch=ch+" > "+str(i)
        return ch
    def affiche(self):
        ch=Employe.__str__(self)
        for i in self.inf:
            if type(i)==Responsable:
                for j in i.inf:
                    ch=ch+" | "+str(j)
            else:
                ch=ch+" | "+str(i)
        return ch


#R1=Responsable(3,"imad",7,[e1,e2])
#print(R1)
#e3=Employe(5,"imane",5)
#e4=Employe(6,"morad",2)
#R2=Responsable(4,"yassin",8,[e3,R1,e4])

#print(R2.affiche())

class Commerciale(Employe):
    sf=6000
    def __init__(self,mat,nom,insal,v):
        Employe.__init__(self,mat,nom,insal)
        self.commission=v
        
    def comm(self):
        if 0<int(self.commission)<500:
            return 2000
        elif 500<=int(self.commission)<1000:
            return 3000
        else:
            return 4500
        
    def __str__(self):
        ch=Employe.__str__(self)+'|'+str(self.commission)
        return ch
    
    def miseajour(self,nv):
        self.commission=nv

    def Salaire(self):
        s=self.sf+self.comm()
        return s

#c1=Commerciale(1,"imed",5,400)
#print(c1)
#print(c1.Salaire())
#c=input('Taper commission:')
#c1.miseajour(c)
#print(c1.Salaire())
e1=Employe(1,"med",5)
e2=Employe(2,"mt",2)
R1=Responsable(3,"imad",7,[e1,e2])
#print(R1)
e3=Employe(5,"imane",5)
e4=Employe(6,"morad",2)
R2=Responsable(4,"yassin",8,[e3,R1,e4])
c1=Commerciale(7,"imed",5,400)
c2=Commerciale(8,"imed",5,800)

def SalaireVerser(L):
    s=0
    for i in L:
        s+=i.Salaire()
    return s
        
        
    
    
L=[e1,e2,R1,e3,e4,R2,c1,c2]
result=1
while int(result)>0:
    print("---------------Menu---------------")
    print("1:Liste Responsables")
    print("2:Liste Employe")
    print("3:Liste Commerciale")
    print("4:Liste Employe d'un Responsable")
    print("5:Somme Salaire")
    print("6:Afficher Tous")
    print("0:Fin du programme")
    result=input("Tapez Le nombre de l'operation que vous choisie:")
    if int(result)==1:
        for i in L:
            if type(i)==Responsable:
                print(i)
    elif int(result)==2:
        for i in L:
            if type(i)==Employe:
                print(i)
        
    elif int(result)==3:
        for i in L:
            if type(i)==Commerciale:
                print(i)
                
    elif int(result)==4:
        for i in L:
            if type(i)==Responsable:
                n=input('Taper Le Nom de Responsable')
                if i.nom==n:
                    print(i)
        
    elif int(result)==5:
        print(SalaireVerser(L))
        
    elif int(result)==6:
        for i in L:
            print(i)
            
                
        



        
        
    
        
        
        
        
        

    

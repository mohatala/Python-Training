# Exercice 1: Les Fonctions
def supp_ponctuation(ch):
    s=ch
    l=['.',';','?',':','!',',']
    for item in l:
        s=s.replace(item,'')
    return s

print(supp_ponctuation("Formation : en ligne, Python.?!!"))

# Exercice 2 :La programmation orientee objet

# Question 1
class technicien :
    # Question 2
    def __init__(self,no,p,v,s):
        self.nom=no
        self.pre=p
        self.ville=v
        self.salaire=s
    # Question 3
    def __str__(self):
        ch=self.nom+'|'+self.pre+'|'+self.ville+'|'+str(self.salaire)
        return ch
    # Question 4
    def salaireAN(self):
        s=self.salaire*12
        return s

# Question 5
T1=technicien("med","imad","casablanca",3500)
T2=technicien("morad","med","safi",4500)
T3=technicien("yassin","aziz","rabat",5500)

# Question 6
print(T1)
print(T2.ville)
print(T3.nom+' '+T3.pre)

# Question 7
print(T2.salaireAN())

# Question 8

equipe=[T1,T2,T3]

# Question 9
stotale=0
for i in equipe:
    stotale+=i.salaire
print(stotale)

# Question 10
s=0
for i in equipe:
    s+=i.salaireAN()
salairemoyen=s/len(equipe)
print(salairemoyen)


#Exercice n°3 heritage en POO

#Question 1
class Personne:
    def __init__(self,no,ag):
        self.nom=no
        self.age=ag
    def __str__(self):
        return self.nom+' '+str(self.age)


#Question 2
class Etudiant(Personne):
    def __init__(self,no,ag,note):
        Personne.__init__(self,no,ag)
        self.note=note
    def __str__(self):
        return Personne.__str__(self)+' '+str(self.note)
        
    def Mention(self):
        if 0>self.note<10:
            print("Insuffisant")
        elif self.note<13:
            print("Passable")
        elif self.note<15:
            print("A Bien")
        elif self.note<17:
            print("Bien")
        else:
            print("T Bien")

class Enseignant(Personne):
    def __init__(self,no,ag,spec):
        Personne.__init__(self,no,ag)
        self.specialite=spec
    def __str__(self):
        return Personne.__str__(self)+' '+self.specialite


#Question 3

E1=Etudiant("imad",18,16)
E2=Etudiant("morad",18,12)
Prof=Enseignant("Mohammed",35,"Informatique")

print(E1)
E1.Mention()
print(E2)
E2.Mention()
print(Prof)

x=input
    

    


        
    
        

    

class enseignant:
    def __init__(self,no,pr,nbh):
        self.nom=no
        self.prenom=pr
        self.nbheure=nbh
        
    def __str__(self):
        ch=self.nom+"|"+self.prenom+"|"+str(self.nbheure)
        return(ch)
    
    def calcule(self):
        pass

class enseignant_chercheur(enseignant):
    def __init__(self,no,pr,nbh):
        enseignant.__init__(self,no,pr,nbh)
        self.salaire=2000
    def __str__(self):
        ch=enseignant.__str__(self)+"|"+str(self.salaire)
        return(ch)

    def calcule(self):
        sa=0
        if enseignant.nbheure>192:
            nbh=enseignant.nbheure-192
            sa=(self.salaire*12)+(nbh*40)
        else:
            sa=self.salaire*12

        return(sa)
    
class vacataire(enseignant):
    def __init__(self,no,pr,nbh,org):
        enseignant.__init__(self,no,pr,nbh)
        self.organisme=org
    def __str__(self):
        ch=enseignant.__str__(self)+"|"+self.organisme
        return(ch)

    def calcule(self):
        sa=enseignant.nbheure*40
        return(sa)

class doctorant(enseignant):
    def __init__(self,no,pr,nbh):
        enseignant.__init__(self,no,pr,nbh)
    def __str__(self):
        ch=enseignant.__str__(self)+"|"+self.organisme
        return(ch)

    def calcule(self):
        sa=0
        if enseignant.nbheure<=96:
            sa=nbh*30
        else:
            sa=96*30
        return(sa)

EN=enseignant_chercheur("med","med",200)
va=vacataire("imad","imad",196,"ibgis")
do=doctorant("morad","morad",85)

print(EN.calcule())
print(va.calcule())
print(do.calcule())


            
        
        

    
        
        
    


class Vehicule:
    def __init__(self,m,mar,hi):
        self.mat=m
        self.marq=mar
        self.hisp_pannes=hi
    def __str__(self):
        ch=self.mat+"|"+self.marq+"|"+str(self.hisp_pannes)
        return ch
    def affiche_pannes():
        print(self.hisp_pannes)


class Camion(Vehicule):
    def __init__(self,m,mar,hi,cm):
        Vehicule.__init__(self,m,mar,hi)
        self.capacite_max=cm
    def __str__(self):
        ch=Vehicule.__str__(self)+"|"+str(self.capacite_max)
        return ch
    
H=["h1","h2","h3"]
C1=Camion("123456","MAN",H,1500)
#print(C1)



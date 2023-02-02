

class MaClasse:
    def __init__(self,x=2,y=3):
        self.x=x
        self.y=y
    def __str__(self):
        ch=str(self.x)+' '+str(self.y)
        return(ch)
    def affiche(self):
        print(self.x,":",self.y)
  


obj=MaClasse(10,20)
print(obj)

obj.affiche()

class Livre:
    def __init__(self,ti,th):
        self.titre=ti
        self.theme=th
        

    def __str__(self):
        ch=self.titre+"|"+str(self.theme)
        return(ch)

class Bibliotheque(Livre):
    def __init__(self,no,Liste_li):
        self.nom=no
        self.liste_li=Liste_li
        
        
    def __str__(self):
        ch=self.nom
        for item in self.liste_li:
            ch+=" | "+item.__str__()
        return(ch)
    
    def recherche(self,s):
        for item in self.liste_li:
            for th in item.theme:
                if th.find(s)>-1:
                    print(item.titre)
                    break
                    


L1=Livre("Titre1",["theme1","theme2","theme3"])
L2=Livre("Titre2",["theme4","theme2","theme5"])

B1=Bibliotheque("B1",[L1,L2])

s="theme5"

B1.recherche(s)



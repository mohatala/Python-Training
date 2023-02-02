class Etudiant:

    def __init__(self,no,pre,list_n):
        self.nom=no
        self.prenom=pre
        if len(list_n)<=10:
            self.list_note=list_n
        else:
            self.list_note=list_n[0:10]
        

    def __str__(self):
        ch=self.nom+"|"+self.prenom+"|"+str(self.list_note)
        return(ch)
    
    def moyenne(self):
        moy=sum(self.list_note)/len(self.list_note)
        return(moy)
    def admis(self):
        i=0
        moy=self.moyenne()
        if moy>=10:
            i=1
        return(i)
    #function inside class
    def meme_moyenne(self,other):
        i=0
        if self.moyenne()==other.moyenne():
            i=1
        return(i)
    

    
        
#Function outside class                        
def meme_moy(moy1,moy2):
    i=0
    if moy1==moy2:
        i=1
    return(i)
        

E1=Etudiant("A","B",[10,3,5,15,12])
E2=Etudiant("C","D",[10,15,20,15,12,17,5,8,10,15,16,18,12,16])


class Et(Etudiant):
    def __init__(self,no,pre,list_n,note_memoire):
        Etudiant.__init__(self,no,pre,list_n)
        self.note_memoire=note_memoire
        
    def __str__(self):
        ch=Etudiant.__str__(self)+"|"+str(self.note_memoire)
        return(ch)
    def admis(self):
        i=Etudiant.admis(self)
        j=0
        if self.note_memoire>=10:
            j=1
        if i==1 and j==1:
            return(1)
        else:
            return(0)
    def meme_moyenne(self,other):
        i=Etudiant.meme_moyenne(self,other)
        j=0
        if self.note_memoire==other.note_memoire:
            j=1
        if i==1 and j==1:
            return(1)
        else:
            return(0)
    def __eq__(self,other):
        self.note_memoire=other.note_memoire
        
E3=Et("A","B",[10,15,15,15,12],15)
E4=Et("E","F",[10,15,15,15,12],15)
print(E3)
print(E3.moyenne())
print(E3.admis())
print(E3.meme_moyenne(E4))
    

if E3==E4:
    print("fffff")
#print(E2.moyenne())
#print(E2.admis())
#print(E1.meme_moyenne(E1))
#print(meme_moy(E1.moyenne(),E2.moyenne()))








        
        
    
        
        
        

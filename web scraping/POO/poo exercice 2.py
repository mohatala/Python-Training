class CompteBancaire:
    def __init__(self,numeroCompte,nom,solde):
        self.numeroCompte=numeroCompte
        self.nom=nom
        self.solde=solde

    def Versement(self,montant):
        self.solde+=montant
        
    def Retrait(self,montant):
        if(montant<self.solde):
            self.solde-=montant
        else:
            print("solde insufisant")
            
        

    def __str__(self):
        ch=str(self.numeroCompte)+" "+self.nom+" "+str(self.solde)
        return(ch)


client1=CompteBancaire(1,'med',10000)
client2=CompteBancaire(2,'mt',20000)
client3=CompteBancaire(3,'imad',30000)

client1.Versement(2000)
print(client1)

client2.Retrait(2000)
print(client2)

d={client1.numeroCompte:client1.solde,client2.numeroCompte:client2.solde,client3.numeroCompte:client3.solde}
print(d.keys())
print(d.values())




    
        
        

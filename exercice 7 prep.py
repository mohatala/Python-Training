class Rue:
    def __init__(self,code_rue,n_rue):
        self.code_rue=code_rue
        self.nom_rue=n_rue

    def __str__(self):
        ch="Rue-> Num :"+ str(self.code_rue)+" | Nom: "+ self.nom_rue
        return ch

class Immeuble:
    def __init__(self,num_imm,nb_etage,rue):
        self.num_immeuble=num_imm
        self.Nb_Etage_total=nb_etage
        self.rue=rue

    def __str__(self):
        ch="IMM-> Num :"+str(self.num_immeuble)+" |Nb_Etage_total: "+ str(self.Nb_Etage_total)+ " | "+ str(self.rue)
        return ch

class Etage:
    def __init__(self,num_et,nb_app,imm):
        self.num_etage=num_et
        self.nb_app_total=nb_app
        self.imm=imm

    def __str__(self):
        ch="Etage-> Num :"+str(self.num_etage)+" |Nb_App_total: "+str(self.nb_app_total)+ " | "+ str(self.imm)
        return ch

class Appartement:
    def __init__(self,lettre_app,nb_pieces,et):
        self.lettre_appartement=lettre_app
        self.nb_pieces_total=nb_pieces
        self.etage=et

    def __str__(self):
        ch="APP-> Num : "+ str(self.lettre_appartement)+" | Nb_Pieces_total: "+ str(self.nb_pieces_total)+ " | "+str(self.etage)
        return ch

R1=Rue(1,"Bernoussi")
R2=Rue(2,"Ainsbaa")
I1=Immeuble(1,4,R1)
I2=Immeuble(2,3,R2)
ET1=Etage(1,5,I1)
ET2=Etage(2,2,I2)
APP1=Appartement(1,3,ET1)
APP2=Appartement(2,3,ET2)

print(APP1)
print(APP2)


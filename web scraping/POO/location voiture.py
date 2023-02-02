

class voiture:
    def __init__(self,mod,imm,kil,et):
        self.modele=mod
        self.immatriculation=imm
        self.kilometrage=kil
        self.etat=et

    def __str__(self):
        ch=self.modele+" "+self.immatriculation+" "+str(self.kilometrage)+" "+self.etat
        return ch


v1=voiture("clio","1321-a-1",50000,"Disponible")
v2=voiture("ford","2011-b-1",60000,"Disponible")
v3=voiture("dacia","2004-a-1",100000,"Disponible")
v4=voiture("mercides","2005-a-1",80000,"Location")
v5=voiture("ford","2006-a-1",70000,"Location")

        
parc=[v1,v2,v3,v4,v5]

def position(matricule,parc):
    i=1
    for item in parc:
        if(matricule==item.immatriculation):
            return(i)
        else:
            i+=1

    if(i==len(parc)+1):
        return(-1)


print("position Voiture : "+str(position("2008-a-1",parc)))

def louer(matricule,parc):
    i=0
    for item in parc:
        if(matricule==item.immatriculation):
            i=1
            if(item.etat=="Location"):
                print("En Location")
            else:
                item.etat="Location"
                return(parc)

    if(i==0):
        print("La voiture n'existe pas")
    
    
def afficher(parc):
    for item in parc:
        print(item)


def louer1(matricule,parc):
    p=position(matricule,parc)-1
    if(p>=0):
        if(parc[p].etat=="Disponible"):
            parc[p].etat="Location"
        else:
            print("En Location")
    else:
        print("La voiture n'existe pas")
    return(parc)

#louer1("2011-b-1",parc)
#afficher(parc)

def retour(matricule,parc):
    p=position(matricule,parc)-1
    if(p>=0):
        if(parc[p].etat=="Location"):
            kil=input("Tapez Le nombre kilometre effectue")
            parc[p].kilometrage=parc[p].kilometrage+int(kil)
            parc[p].etat="Disponible"
    else:
        print("La voiture n'existe pas")
    return(parc)

#retour("2006-a-1",parc)
#afficher(parc)

def etat(matricule,parc):
    p=position(matricule,parc)-1
    if(p>=0):
        print(parc[p].modele+" "+parc[p].immatriculation+" "+str(parc[p].kilometrage)+" "+parc[p].etat)
    else:
        print("La voiture n'existe pas")
    
#etat("2006-a-1",parc)

def etatparc(parc):
    i=0
    j=0
    vlouer=[]
    vdispo=[]
    somme=0
    for v in parc:
        if(v.etat=="Location"):
            i+=1
            vlouer.append(v.immatriculation)
        else:
            j+=1
            vdispo.append(v.immatriculation)
        somme+=v.kilometrage
    moy=somme/len(parc)
    etat="nombre totale de voiture: "+str(len(parc))+"\n"+"nombre voiture en location: "+str(i)+"\n"
    for im in vlouer:
        etat+=im+"\n"
        
    etat+="nombre voiture disponible: "+str(j)+"\n"
    for im in vdispo:
        etat+=im+"\n"
    etat+="kilometrage moyen : "+str(int(moy))
    return(etat)
    

#print(etatparc(parc))

def save(parc):
    f = open("parc.txt", "w")
    f.write(etatparc(parc))
    f.close()

#save(parc)
result=1
while int(result)>0:
    print("---------------Menu---------------")
    print("1:Louer une voiture")
    print("2:Retour d'une voiture")
    print("3:Etat d'une voiture")
    print("4:Etat du parc de voiture")
    print("5:Sauvegarder l'etat du parc")
    print("0:Fin du programme")
    result=input("Tapez Le nombre de l'operation que vous choisie:")
    if int(result)==1:
        mat=input("Tapez Matricule de voiture:")
        louer(mat,parc)
    elif int(result)==2:
        mat=input("Tapez Matricule de voiture:")
        retour(mat,parc)
    elif int(result)==3:
        mat=input("Tapez Matricule de voiture:")
        etat(mat,parc)
    elif int(result)==4:
        print(etatparc(parc))
    elif int(result)==5:
        save(parc)

        
        
        
        
        
        

    


       
    
        
            
            
          
        



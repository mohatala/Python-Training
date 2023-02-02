

def ecrire(ncin,nom,prenom,age,decision):
    f = open("concours.txt", "a")
    f.write(ncin+';'+nom+';'+prenom+';'+age+';'+decision+'\n')
    f.close()

def ecrire2():
    while True:
        ncin=input("Votre Cin:")
        nom=input("Votre nom:")
        prenom=input("Votre prenom:")
        age=input("Votre age:")
        decision=input("Votre decision:")
        c=input("Voulez Vous Tapez Autre Candidat(oui Ou non):")
        ecrire(ncin,nom,prenom,age,decision)
        if(c=="non"):
            break;
    
    


def admis():
    f = open("concours.txt", "r")
    f1=open("admis.txt","a")
    for x in f:
        ch=x.split(';')
        if (ch[4].rstrip("\n")=="admis"):
            f1.write(x)
    f1.close()

def attente():
    f=open("admis.txt","r")
    f1=open("attente.txt","a")
    for x in f:
        ch=x.split(';')
        if (int(ch[3])>30):
            f1.write(ch[0]+';'+ch[1]+';'+ch[2])
            #print(x)

def statistiques(dec):
    f=open("concours.txt","r")
    n=0
    t=0
    for x in f:
        n+=1
        ch=x.split(';')
        if (ch[4].rstrip("\n")==dec):
            t+=1
    p=(t/n)*100
    return p

def supprimer():
    f=open("admis.txt","r")
    fs=f.readlines()
    f.close()
    f=open("admis.txt","w")
    for l in fs:
        ch=l.split(';')
        if (int(ch[3])<=30):
            f.write(l) 
    f.close()
        
        

#ecrire('med','qwerty','azerty','admis')
#ecrire2()
#admis()
#attente()
#statistiques("admis")
print(statistiques("admis"))
supprimer()







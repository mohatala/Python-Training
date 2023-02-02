import sqlite3

cn=sqlite3.connect("C:/Users/21260/Desktop/Master/Formation Licence Web Mobile/python/club/MY_ClUB.db")

c=cn.cursor()


#4 Affichez les adherent en ordre alphabetique
print ("****Affichez les adherent en ordre alphabetique*****")
for ligne in c.execute("SELECT * FROM adherent ORDER BY NOMADH"):
    print (ligne)

#5  Affichez le nom et le prénom d’adhérent dont NOSPORT=2
print ("****Affichez le nom et le prénom d’adhérent dont NOSPORT=2****")    
for ligne in c.execute("SELECT NOMADH,PRENAGH FROM adherent WHERE NOSPORT=2 "):
    print (ligne)

#6 Affichez NOMADH, PRENADH, NOMSP, MONTANT
print ("****  Affichez NOMADH, PRENADH, NOMSP, MONTANT ****")

for ligne in c.execute("SELECT NOMADH,PRENAGH,NOMSP,MONTANT FROM adherent,activite WHERE adherent.NOSPORT=activite.NOSPORT "):
    print (ligne)

#7 Montant général / Sport
print ("****  Montant général / Sport ****")

for ligne in c.execute("SELECT NOMSP,SUM(MONTANT) FROM activite GROUP BY NOSPORT "):
    print (ligne)
    
#8 Nombre d’adhésions / Sport
print ("****  Nombre d’adhésions / Sport ****")

for ligne in c.execute("SELECT NOMSP,Count(NOADH) FROM adherent,activite WHERE adherent.NOSPORT=activite.NOSPORT GROUP BY activite.NOSPORT "):
    print (ligne)


#9. Modifiez le nom de l’adhérent n° 2
print ("****  Modifiez le nom de l’adhérent n° 2 ****")
c.execute("UPDATE adherent SET NOMADH='Mouad' WHERE NOADH=2 ")
cn.commit()

#10.Supprimez un adhérent de votre choix
print ("****  Supprimez un adhérent de votre choix ****")
#c.execute("DELETE FROM adherent  WHERE NOADH=3 ")
#cn.commit()

#11.Créez un menu contenant trois opérations (insertion, modification et suppression)

table=input("Pour Execute une Tache sur Adherent Taper 1, Sur Sport Taper 2")
choix=input("Si vous voulez Inserer Taper 1,Modifier Taper 2, Supprimer Taper 3 ")


if(int(table)==1):
    if(int(choix)==1):
       # print("adherent/Insertion")
        idt=input("Tapez l'identifient de l'adherent:")
        nom=input("Tapez le Nom de l'adherent:")
        prenom=input("Tapez le Prenom de l'adherent:")
        ids=input("Tapez numero de Sport de l'adherent:")
        adh=[(idt,nom,prenom,ids)]
        c.executemany("INSERT INTO adherent VALUES (?,?,?,?)",adh)
        cn.commit()
    elif(int(choix)==2):
       #print("adherent/Modifier")
        idt=input("Tapez l'identifient de l'adherent que vous voulez modifier:")
        nom=input("Tapez le Nom de l'adherent:")
        prenom=input("Tapez le Prenom de l'adherent:")
        ids=input("Tapez numero de Sport de l'adherent:")
        adh=[(nom,prenom,ids,idt)]
        c.executemany("UPDATE adherent SET NOMADH=?,PRENAGH=?,NOSPORT=? WHERE NOADH=?",adh)
        cn.commit()
    elif(int(choix)==3):
        print("adherent/Supprimer")
        idt=input("Tapez l'identifient de l'adherent que vous voulez modifier:")
        c.execute("DELETE FROM adherent  WHERE NOADH=? ",idt)
        cn.commit()
    else:
        print("Taper un Numero Dans Menu")
elif(int(table)==2):
    if(int(choix)==1):
        print("activite/Insertion")
        ids=input("Tapez l'identifient de l'activite:")
        noma=input("Tapez le Nom de l'activite:")
        montant=input("Tapez Montant de l'activite:")
        act=[(ids,noma,montant)]
        c.executemany("INSERT INTO activite VALUES (?,?,?)",act)
        cn.commit()
    elif(int(choix)==2):
        print("activite/Modifier")
        ids=input("Tapez l'identifient de l'activite que vous voulez modifier:")
        noma=input("Tapez le Nom de l'activite:")
        montant=input("Tapez Montant de l'activite:")
        act=[(noma,montant,ids)]
        c.executemany("UPDATE activite SET NOMSP=?,MONTANT=? WHERE NOSPORT=?",act)
        cn.commit()
    elif(int(choix)==3):
        print("activite/Supprimer")
        ids=input("Tapez l'identifient de l'activite que vous voulez modifier:")
        c.execute("DELETE FROM activite  WHERE NOSPORT=? ",ids)
        cn.commit()
    else:
        print("Taper un Numero Dans Menu")
    
    
        







 


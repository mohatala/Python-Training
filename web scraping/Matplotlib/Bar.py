import matplotlib.pyplot as plt

plt.title("Hello World")
plt.xlabel("x")
plt.ylabel("y")
x=["lundi","mardi","mercredi","jeudi","vendredi"]
y=[2,1,6,5,6]
plt.bar(x,y)
plt.show()

#**************************************
#Prix total de chaque commande
commandes = [(1,"casa",320,12,"scanner","12/03/2022"),
             (2,"rabat",2200,3,"pc","18/04/2022"),
             (3,"casa",2000,6,"pc","23/02/2022"),
             (4,"tanger",80,9,"clavier","01/02/2022"),
             (5,"casa",300,12,"scanner","22/03/2022"),
             (6,"rabat",5000,5,"pc","10/09/2022"),
             (7,"casa",2000,6,"pc","09/02/2022"),
             (8,"agadir",1000,3,"clavier","22/04/2022")]

plt.title("Commande")
plt.xlabel("N°commande")
plt.ylabel("Prix Total")
x=[]
y=[]
for i in commandes:
    x.append(i[0])
    y.append(i[2]*i[3])

plt.bar(x,y)
plt.show()

#*************************************************
#Nombre des commande pour chaque ville
commandes = [(1,"casa",320,12,"scanner","12/03/2022"),
             (2,"rabat",2200,3,"pc","18/04/2022"),
             (3,"casa",2000,6,"pc","23/02/2022"),
             (4,"tanger",80,9,"clavier","01/02/2022"),
             (5,"casa",300,12,"scanner","22/03/2022"),
             (6,"rabat",5000,5,"pc","10/09/2022"),
             (7,"casa",2000,6,"pc","09/02/2022"),
             (8,"agadir",1000,3,"clavier","22/04/2022")]

plt.title("Commande/ville")
plt.xlabel("Ville")
plt.ylabel("Nb Commandes")
x=[]
y=[]
v=[]
for i in commandes:
    v.append(i[1])
v2=list(set(v))
for i in v2:
    x.append(i)
    y.append(v.count(i))
plt.bar(x,y)
plt.show()


#*****************************************************
#Nombre des commande pour chaque produit
commandes = [(1,"casa",320,12,"scanner","12/03/2022"),
             (2,"rabat",2200,3,"pc","18/04/2022"),
             (3,"casa",2000,6,"pc","23/02/2022"),
             (4,"tanger",80,9,"clavier","01/02/2022"),
             (5,"casa",300,12,"scanner","22/03/2022"),
             (6,"rabat",5000,5,"pc","10/09/2022"),
             (7,"casa",2000,6,"pc","09/02/2022"),
             (8,"agadir",1000,3,"clavier","22/04/2022")]

plt.title("Commande/Produit")
plt.xlabel("Produit")
plt.ylabel("Nb Commandes")
x=[]
y=[]
v=[]
for i in commandes:
    v.append(i[4])
v2=list(set(v))
v2.sort()
for i in v2:
    x.append(i)
    y.append(v.count(i))
plt.bar(x,y)
plt.show()

#**************************************************
#Nombre des commande pour chaque mois(numero de  mois)
import datetime
commandes = [(1,"casa",320,12,"scanner","12/03/2022"),
             (2,"rabat",2200,3,"pc","18/04/2022"),
             (3,"casa",2000,6,"pc","23/02/2022"),
             (4,"tanger",80,9,"clavier","01/02/2022"),
             (5,"casa",300,12,"scanner","22/03/2022"),
             (6,"rabat",5000,5,"pc","10/09/2022"),
             (7,"casa",2000,6,"pc","09/02/2022"),
             (8,"agadir",1000,3,"clavier","22/04/2022")]

plt.title("NB Commande/Mois")
plt.xlabel("Mois")
plt.ylabel("Nb Commandes")
x=[]
y=[]
v=[]
for i in commandes:
    datem = datetime.datetime.strptime(i[5], "%d/%m/%Y")
    v.append(datem.month)
#print(v)
v2=list(set(v))
v2.sort()
for i in v2:
    x.append(str(i))
    y.append(v.count(i))
plt.bar(x,y)
plt.show()

#**********************************************
#Nombre des commande pour chaque mois(intitule mois)
commandes = [(1,"casa",320,12,"scanner","12/03/2022"),
             (2,"rabat",2200,3,"pc","18/04/2022"),
             (3,"casa",2000,6,"pc","23/02/2022"),
             (4,"tanger",80,9,"clavier","01/02/2022"),
             (5,"casa",300,12,"scanner","22/03/2022"),
             (6,"rabat",5000,5,"pc","10/09/2022"),
             (7,"casa",2000,6,"pc","09/02/2022"),
             (8,"agadir",1000,3,"clavier","22/04/2022")]
monthDict = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 
            7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
plt.title("NB Commande/Mois")
plt.xlabel("Mois")
plt.ylabel("Nb Commandes")
x=[]
y=[]
v=[]
for i in commandes:
    datem = datetime.datetime.strptime(i[5], "%d/%m/%Y")
    v.append(datem.month)
#print(v)
v2=list(set(v))
v2.sort()
for i in v2:
    x.append(monthDict[i])
    y.append(v.count(i))
plt.bar(x,y)
plt.show()
import matplotlib.pyplot as plt
plt.title("Hello World")
plt.xlabel("x")
x=[2,1,6,5]
plt.pie(y)
plt.show()

#***********************************
#Pourcentage pour chaque produit 

commandes = [(1,"casa",320,12,"scanner","12/03/2022"),
             (2,"rabat",2200,3,"pc","18/04/2022"),
             (3,"casa",2000,6,"pc","23/02/2022"),
             (4,"tanger",80,9,"clavier","01/02/2022"),
             (5,"casa",300,12,"scanner","22/03/2022"),
             (6,"rabat",5000,5,"pc","10/09/2022"),
             (7,"casa",2000,6,"pc","09/02/2022"),
             (8,"agadir",1000,3,"clavier","22/04/2022")]

plt.title("Produit Commande")
plt.xlabel("Produit")
x=[]
y=[]
v=[]
for i in commandes:
    v.append(i[4])
v2=list(set(v))
v2.sort()
for i in v2:
    x.append(v.count(i))
plt.pie(x,labels =v2,autopct='%1.1f%%')
plt.show()

#**************************************
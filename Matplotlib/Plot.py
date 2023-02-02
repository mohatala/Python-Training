import matplotlib.pyplot as plt
plt.title("Hello World")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["prix","quantite"])
x=[1,3,4]
y=[2,1,6]
z=[3,5,4]
plt.plot(x,y)
plt.plot(x,z)
plt.show()




#-***************************************************
#Nombre des commande contre la quantite
commandes = [(1,"casa",320,12,"scanner","12/03/2022"),
             (2,"rabat",2200,3,"pc","18/04/2022"),
             (3,"casa",2000,6,"pc","23/02/2022"),
             (4,"tanger",80,9,"clavier","01/02/2022"),
             (5,"casa",300,12,"scanner","22/03/2022"),
             (6,"rabat",5000,5,"pc","10/09/2022"),
             (7,"casa",2000,6,"pc","09/02/2022"),
             (8,"agadir",1000,3,"clavier","22/04/2022")]
plt.title("NB Commande/quantite")
plt.xlabel("N°commande")
plt.ylabel("Quantite")
x=[]
y=[]
v=[]
p=0
for i in commandes:
    p+=i[3]
    x.append(i[0])
    y.append(p)
    
plt.plot(x,y,marker = 'o')
plt.show()
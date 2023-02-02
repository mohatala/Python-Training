x=input("Saisie Un Nombre superieur a 100 : ")

s=0

for i in x:
    s+=int(i)

somme=0
for j in str(s):
    if s>9:
        somme+=int(j)
    else:
        somme=s
    
    


#print(s)
#print(somme)

x=str(somme)+x
print(x)

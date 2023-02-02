
x=input("Saisie Mot")

D={"A":1,"E":5,"I":9,"O":15,"U":21,"Y":25}
y=1
s=0

for i in x:
    if i in D.keys():
         s+=y*D[i]    
    y+=1

print(s)
            
            
            


    

import os

l=[]
for root, dirs, files in os.walk("D:\Projetpython"):
     for file in files:
          l.append(file.split(".")[-1])
     
#print(l)
l2= list(dict.fromkeys(l))
#print(l2)
D={}
for i in l2:  
     D[i]=l.count(i)
          
print(D)
          

          

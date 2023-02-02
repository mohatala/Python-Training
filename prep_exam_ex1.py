#exercice 1
#x=input("Saisie un entier")    
#print(x)
#y=str(x)
#i=0
#for c in y:
#    for b in y :
#        if(c==b):
 #           i=i+1
   # if(i>1):
        #print("nombre non distincts")
   # else:
        #print("nombre distincts")        
   # i=0
#t=True
#for c in y:
#    if x.count(c)>1:
#        t=False
#        break

#if t==True:
#    print("nombre distincts")
#else:
#    print("nombre non distincts")

#Exercice 2

x=input("Saisie un entier")

if 100<=int(x)<=999:
    y=str(x)
    s=0
    m=1
    for c in y:
        s=s+int(c)
        m=m*int(c)
    print(s)
    print(m)
    if m%s==0:
        print(True)
    else:
        print(False)
else:
    print("erreur")
    
        
    



    






    



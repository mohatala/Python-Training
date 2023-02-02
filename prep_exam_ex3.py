x=input("Entrer Un Entier: ")

if 1000<=int(x)<=9999:
    y=str(x)
    t=False
    for i in [1,2,3,4,5]:
        s=0
        for c in y:
            s=s+int(c)**i
        if s==int(x):
            t=True

    if t==True:
        print("Nombre Verifie")
    else:
        print("Nombre Non Verifie")
else:
    print("Erreur")


    
    
        
        
    



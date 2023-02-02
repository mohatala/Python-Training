ip=input("Taper Adresse IP: ")

x=ip.split(".")

b=False
if len(x)==4:
    b=True
    for i in x:
        if 0<=int(i)<=255:
            b=True
        else:
            b=False
            break
else:
    b=False
    

if b==True:
    print("Adresse IP Valide")
else:
    print("Adresse IP Non Valide")

        

p=int(input("Entrer intervalle 1: "))
q=int(input("Entrer intervalle 2: "))


def premier(x):
    for i in range(2,x//2):
        if x%i==0:
            return False
        else:
            return True

#print(premier(111))

for i in range(p,q+1):
    y=str(i)
    v=y[0]+y[1]+y[2]
    v1=y[1]+y[2]+y[0]
    v2=y[2]+y[0]+y[1]
    
    if premier(int(v)) and premier(int(v1)) and premier(int(v2)):
        print(v)




        
    
        
        
            


    



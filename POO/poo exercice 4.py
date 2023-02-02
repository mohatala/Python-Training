class Calcul:
    def __init__(self):
        pass


    def Factorielle(self,x):
        f=1;
        i=1
        if(x==0):
            f=1
        else:      
            while i<=x:    
                f=f*i
                i=i+1
        return(f)

    def Somme(self,n):
        i=0
        s=0
        while i<=n:    
                s+=i
                i=i+1
        return(s)
    
    def tableMult(self,n):
        i=0
        while i<=10:
            print(str(n)+'*'+str(i)+'='+str(i*n))
            i=i+1
    
    def allTablesMult(self):
        for i in range(1,10):
            self.tableMult(i)
            print("-----------")

    @staticmethod
    def listDiv(n):
        for i in range(1,n+1):
            if(n%i==0):
                print(i)
                
            

obj1=Calcul()
print("factorielle")
print(obj1.Factorielle(5))
print("somme")
print(obj1.Somme(4))
print("Table Multiplication")
obj1.tableMult(5)

print("tous les Table Multiplication")
obj1.allTablesMult()

print(" les diviseurs d’un entier ")
obj1.listDiv(10)
print("************")
Calcul.listDiv(20) 

        

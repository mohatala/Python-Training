from math import sqrt
class Vecteur3d:
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z

    def __str__(self):
        ch='('+str(self.x)+','+str(self.y)+','+str(self.z)+')'
        return ch

    def __add__(self, other):
        return Vecteur3d(self.x+other.x,self.y+other.y,self.z+other.z)

    def __mul__(self,other):
        return self.x*other.x+self.y*other.y+self.z*other.z

    def coincide(self,other):
        if self.x==other.x and self.y==other.y and self.z==other.z:
            return True
        else:
            return False
        
    def __eq__(self,other):
        if self.x==other.x and self.y==other.y and self.z==other.z:
            return True
        else:
            return False
        
    def __ne__(self,other):
        if self.x!=other.x or self.y!=other.y or self.z!=other.z:
            return True
        else:
            return False
        
    def norme(self):
        return sqrt(self.x**2+self.y**2+self.z**2)
        
    def normax(self,other):
        if self.norme()>other.norme():
            return self
        elif self.norme()<other.norme():
            return other
    def __pow__(self,other):
        return Vecteur3d(self.x**other.x,self.y**other.y,self.z**other.z)
    
#+ __add__
#* __mul__
#== __eq__
#!= __ne__
#<  __lt__
#<= __le__
#>  __gt__
#>= __ge__
                
    
        

v1=Vecteur3d(1,2,-5)
v2=Vecteur3d(4,5,-2)
v3=Vecteur3d(1,2,-5)

print(v1)
print(v1+v2)
print(v1*v2)
print(v1.coincide(v3))
print(v1==v2)
print(v1!=v3)
print(v1.norme())
print(v2.norme())
print(v1.normax(v2))
print(v1**v2)



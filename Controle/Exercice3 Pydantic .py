import re
from pydantic import constr,PositiveInt,validator,BaseModel
from typing import Optional, List
import string

class Voiture(BaseModel):
    Matricule:PositiveInt
    Couleur:str
    Carburant:str
    Prix_vente:float

    @validator("Couleur")
    def couleur(cls, v): 
        
        if  any([v=='noir',v=='rouge',v=='bleu' ]) : 
            return v
        else:
            raise ValueError("Couleur non valide")
    
    @validator("Carburant")
    def carburant(cls, v): 
        
        if  any([v=='diesel',v=='essence']) : 
            return v
        else:
            raise ValueError("Carburant non valide")
    
    @validator("Prix_vente")
    def prix_v(cls, v): 
        if  130000<=v<= 230000:  
            return v
        else:
            raise ValueError("Prix non valide")

V1=Voiture(Matricule=20325,Couleur='noir',Carburant='diesel',Prix_vente=150000)

print(V1)
    
    


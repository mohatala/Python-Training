from pydantic import constr,PositiveInt,validator,BaseModel
from typing import Optional, List

class etudiant(BaseModel): 

    id_Etud: constr(min_length=10,max_length=10) 
    
    @validator("id_Etud") 
    def id_etud(cls, v): 
        if v[:2]=="UH":
            if v[2:].isdigit():
                    if len(v[2:])==8:
                        return v
            else:
                raise ValueError("La 2eme partie doit etre des numeros")
        else:
            raise ValueError("La 1er partie doit etre (UH)'")

et=etudiant(id_Etud="UH58021532")

print(et)
                        
        
        

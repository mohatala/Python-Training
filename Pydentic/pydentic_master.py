from pydantic import constr,PositiveInt,validator,BaseModel
from typing import Optional, List
import datetime
from dateutil.relativedelta import relativedelta

class Service(BaseModel):
    Num_service: PositiveInt
    nom_service: List[str]=[]

    @validator("Num_service") 
    def Num_service_value(cls, v): 
        if v < 30: 
            raise ValueError("Num_service doit etre supérieur à 30") 
        return v

    @validator("nom_service")
    def nom_service_valid(cls, v): 
        if  any([v=='info',v=='compta',v=='finance' ]) : 
            return v
        else:
            raise ValueError("nom_service non valide")


class Personne(BaseModel):
    Num:PositiveInt
    Nom :constr( max_length=15)
    Prenom:constr( max_length=15)
    is_married:bool
    Ville:List[str]=[]
    date_Embauche:datetime
    Ser:Service

    @validator("Num") 
    def Num_service_value(cls, v): 
        if v < 30: 
            raise ValueError("Num doit etre supérieur à 30") 
        return v

    @validator("Ville")
    def Ville_valid(cls, v): 
        if  any([v=='casa',v=='tanger',v=='agadir',v=='meknes' ]) : 
            return v
        else:
            raise ValueError("Ville non valide")

    @validator('date_embauche')
    def date_embauche_must_be_valid(cls, v):
        if v < datetime.now():
            raise ValueError('date_embauche must be greater than or equal to current date')
        return v
    def anciennete(self):
        an = relativedelta(datetime.date.today(),self.date_Embauche).years 
        return an
    
S1 = Service(num_service=120, nom_service='finance')

D1 = {
    'num': 40,
    'nom': 'John',
    'prenom': 'Doe',
    'age': 30,
    'is_married': True,
    'ville': 'casa',
    'date_embauche': datetime.now(),
    'serv': S1
}

P1 = Personne(**D1)


D2 = {
    'num': 20,
    'nom': 'Jane',
    'prenom': 'Doe',
    'age': 30,
    'is_married': True,
    'ville': 'paris',
    'date_embauche': "05/05/2023",
    'serv' :S1
    }

try:
  p2=Personne(**D2)
except:
  print("An exception occurred")

    





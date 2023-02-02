from pydantic import BaseModel, validator
from datetime import datetime

class Service(BaseModel):
    num_service: int
    nom_service: str

    @validator('num_service')
    def num_service_must_be_positive(cls, v):
        if v <= 30:
            raise ValueError('num_service must be greater than 30')
        return v

    @validator('nom_service')
    def nom_service_must_be_valid(cls, v):
        if v not in ['info', 'compta', 'finance']:
            raise ValueError('nom_service must be one of: info, compta, finance')
        return v

class Personne(BaseModel):
    num: int
    nom: str
    prenom: str
    age: int
    is_married: bool
    ville: str
    date_embauche: datetime
    serv: Service

    @validator('num')
    def num_must_be_positive(cls, v):
        if v <= 30:
            raise ValueError('num must be greater than 30')
        return v

    @validator('nom')
    def nom_must_have_max_length(cls, v):
        if len(v) > 15:
            raise ValueError('nom must have max length of 15 characters')
        return v

    @validator('prenom')
    def prenom_must_have_max_length(cls, v):
        if len(v) > 15:
            raise ValueError('prenom must have max length of 15 characters')
        return v

    @validator('ville')
    def ville_must_be_valid(cls, v):
        if v not in ['casa', 'tanger', 'agadir', 'meknes']:
            raise ValueError('ville must be one of: casa, tanger, agadir, meknes')
        return v

    @validator('date_embauche')
    def date_embauche_must_be_valid(cls, v):
        if v < datetime.now():
            raise ValueError('date_embauche must be greater than or equal to current date')
        return v

    def anciennete(self):
        return (datetime.now() - self.date_embauche).years

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

P1 = Personne(D1)


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
  p2=Personne(D2)
except:
  print("An exception occurred")


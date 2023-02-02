import re
from pydantic import constr,PositiveInt,validator,BaseModel
from typing import Optional, List
import string

class Address(BaseModel): 
    id: int
    address_line_1: constr(max_length=50) 
    address_line_2: Optional[constr(max_length=50)] = None
    pincode: PositiveInt
    city: constr(max_length=30) 
    cp:List[int]=[]
    @validator("pincode") 
    def pincode_length(cls, v): 
        if len(str(v)) != 6: 
            raise ValueError("Pincode must be of six digits") 
        return v

adr1 = Address(id=1,address_line_1="12 BD ANOUAL",address_line_2= 
None,pincode=123456,city="CASA",cp=[12000,13000])

print(adr1)

class User(BaseModel):
    username:str
    password:str
    age:PositiveInt
    score:float
    name: constr(min_length=2, max_length=6)
    email:Optional[str]
    phone_number:Optional[str]
    adr: Address
    @validator("username")
    def username_valid(cls,value):
        tr = False
        for v in value:
            if v in string.punctuation:
                tr = True
                raise ValueError("username must not include punctuation")
        if tr == False:
            return value
    
    @validator("username")
    def username_length(cls, v): 
        if len(str(v)) < 4: 
            raise ValueError("username must be > 3 caracters") 
        return v
      
    @validator("email")
    def check(cls,v):   
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex,v)):   
            return v  
        else:   
            raise ValueError("Email invalide") 

user1 = User(username="user120",password="123",age=33,score=3.4,name="alami"
,email="user1@gmail.com",phone_number="000",adr=adr1)

#print(user1)
print(list(user1))

data2 = {
        "username": "user2222", 
        "password": "passpass", 
        "age": 20,
        "score": 2.6,
        "name": "khaldi",
        "email": "khaldi@hotmail.fr",
        "phone_number":"12121",
    "adr": { 
        "id": 1, 
        "address_line_1": "Sector- 136", 
        "address_line_2": "Sector- 136", 
        "pincode": 201305, 
        "city": "Noida", 
        "cp": [10000,24000], 
        }, 
}

user2 = User(**data2)
print(user2)

class Employee(BaseModel):
    mat:int
    nom:constr(min_length=5, max_length=20)
    salaire:int
    sit:constr(min_length=1, max_length=1)
    
    @validator("salaire")
    def Min_salaire(cls, v): 
        if  v< 4000: 
            raise ValueError("Salaire est <4000") 
        return v
    
    @validator("sit")
    def Situation(cls, v): 
        
        if  any([v=='M',v=='D',v=='C' ]) : 
            return v
        else:
            raise ValueError("Situation non valide")
        
E1=Employee(salaire=4000,nom='mohammed',mat=1,sit='C')
print(E1)

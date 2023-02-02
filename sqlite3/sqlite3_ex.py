from tkinter import *
import sqlite3
from tkinter.messagebox import *
from tkinter.ttk import *

# create database

conn=sqlite3.connect("exam.db")
c=conn.cursor()
sql2=""" CREATE TABLE  Rue(
                            code_rue INTERGER PRIMARY KEY,
                            nom_rue TEXT NOT NULL
                            )
     """
c.execute(sql2)
sql2=""" CREATE TABLE Immeuble(
                            num_immeuble INTERGER PRIMARY KEY,
                            Nb_Etage_total INTERGER NOT NULL,
                            num_rue INTEGER,
                            FOREIGN key(num_rue) REFERENCES Rue(code_rue)
                            )
     """
c.execute(sql2)
sql2=""" CREATE TABLE Etage(
                            num_etage INTERGER PRIMARY KEY,
                            nb_app_total INTERGER NOT NULL,
                            num_imm INTEGER,
                            FOREIGN key(num_imm) REFERENCES Immeuble(num_immeuble)
        
                            )
     """
c.execute(sql2)
sql2=""" CREATE TABLE Appartement(
                            lettre_appartement INTERGER PRIMARY KEY,
                            nb_pieces_total INTERGER NOT NULL,
                            num_etage INTEGER,
                            FOREIGN key(num_etage) REFERENCES Etage(num_etage)
                            )
     """
c.execute(sql2)
conn.commit()
#**************************#

class Rue:
    def __init__(self,code_rue,n_rue):
        self.code_rue=code_rue
        self.nom_rue=n_rue

    def __str__(self):
        ch="Rue-> Num :"+ str(self.code_rue)+" | Nom: "+ self.nom_rue
        return ch
    def insert_rue(self):
        liste=[(self.code_rue,self.nom_rue)]
        c.executemany("INSERT INTO Rue VALUES (?,?)",liste)
        conn.commit()
        print("Insert successful")
    def modifier(self):
        liste=[(self.nom_rue,self.code_rue)]
        c.executemany("UPDATE Rue SET nom_rue=? WHERE code_rue=?",liste)
        conn.commit()
        print("UPDATE successful")
    def delete(self):
        liste=[(self.code_rue)]
        c.executemany("DELETE Rue WHERE code_rue=?",liste)
        conn.commit()
        print("DELETE successful")
    def affiche():
        liste=[(self.code_rue)]
        for ligne in c.execute("SELECT * FROM Rue where code_rue=?",liste):
            print (ligne)
        

class Immeuble:
    def __init__(self,num_imm,nb_etage,rue):
        self.num_immeuble=num_imm
        self.Nb_Etage_total=nb_etage
        self.rue=rue

    def __str__(self):
        ch="IMM-> Num :"+str(self.num_immeuble)+" |Nb_Etage_total: "+ str(self.Nb_Etage_total)+ " | "+ str(self.rue)
        return ch
    def insert(self):
        liste=[(self.num_immeuble,self.Nb_Etage_total,self.rue)]
        c.executemany("INSERT INTO Immeuble VALUES (?,?,?)",liste)
        conn.commit()
        print("Insert successful")
    def modifier(self):
        liste=[(self.Nb_Etage_total,self.rue,self.num_immeuble)]
        c.executemany("UPDATE Immeuble SET Nb_Etage_total=? , num_rue=?  WHERE num_immeuble=?",liste)
        conn.commit()
        print("UPDATE successful")
    def delete(self):
        liste=[(self.num_immeuble)]
        c.executemany("DELETE Immeuble WHERE num_immeuble=?",liste)
        conn.commit()
        print("DELETE successful")
    def affiche(self):
        liste=[(self.num_immeuble)]
        for ligne in c.execute("SELECT Immeuble.num_immeuble,Immeuble.Nb_Etage_total,Rue.code_rue,Rue.nom_rue FROM Immeuble INNER JOIN Rue ON Immeuble.num_rue=Rue.code_rue WHERE num_immeuble=?",liste):
            print (ligne)


class Etage:
    def __init__(self,num_et,nb_app,imm):
        self.num_etage=num_et
        self.nb_app_total=nb_app
        self.imm=imm

    def __str__(self):
        ch="Etage-> Num :"+str(self.num_etage)+" |Nb_App_total: "+str(self.nb_app_total)+ " | "+ str(self.imm)
        return ch
    def insert(self):
        liste=[(self.num_etage,self.nb_app_total,self.imm)]
        c.executemany("INSERT INTO Etage VALUES (?,?,?)",liste)
        conn.commit()
        print("Insert successful")
    def modifier(self):
        liste=[(self.nb_app_total,self.imm,self.num_etage)]
        c.executemany("UPDATE Etage SET nb_app_total=? , num_imm=?  WHERE num_etage=?",liste)
        conn.commit()
        print("UPDATE successful")
    def delete(self):
        liste=[(self.num_etage)]
        c.executemany("DELETE Etage WHERE num_etage=?",liste)
        conn.commit()
        print("DELETE successful")
    def affiche(self):
        liste=[(self.num_etage)]
        for ligne in c.execute("SELECT Etage.num_etage,Etage.nb_app_total,Immeuble.num_immeuble,Immeuble.Nb_Etage_total,Rue.code_rue,Rue.nom_rue FROM Etage INNER JOIN Immeuble ON Etage.num_imm=Immeuble.num_immeuble INNER JOIN Rue ON Immeuble.num_rue=Rue.code_rue WHERE num_etage=?",liste):
            print (ligne)

class Appartement:
    def __init__(self,lettre_app,nb_pieces,et):
        self.lettre_appartement=lettre_app
        self.nb_pieces_total=nb_pieces
        self.etage=et

    def __str__(self):
        ch="APP-> Num : "+ str(self.lettre_appartement)+" | Nb_Pieces_total: "+ str(self.nb_pieces_total)+ " | "+str(self.etage)
        return ch
    def insert(self):
        liste=[(self.lettre_appartement,self.nb_pieces_total,self.etage)]
        c.executemany("INSERT INTO Appartement VALUES (?,?,?)",liste)
        conn.commit()
        print("Insert successful")
    def modifier(self):
        liste=[(self.nb_pieces_total,self.etage,self.lettre_appartement)]
        c.executemany("UPDATE Appartement SET nb_pieces_total=? , num_etage=?  WHERE lettre_appartement=?",liste)
        conn.commit()
        print("UPDATE successful")
    def delete(self):
        liste=[(self.lettre_appartement)]
        c.executemany("DELETE Appartement WHERE lettre_appartement=?",liste)
        conn.commit()
        print("DELETE successful")
    def affiche(self):
        liste=[(self.lettre_appartement)]
        for ligne in c.execute("SELECT Appartement.lettre_appartement,Appartement.nb_pieces_total,Etage.num_etage,Etage.nb_app_total,Immeuble.num_immeuble,Immeuble.Nb_Etage_total,Rue.code_rue,Rue.nom_rue FROM Appartement INNER JOIN Etage ON Appartement.num_etage=Etage.num_etage INNER JOIN Immeuble ON Etage.num_imm=Immeuble.num_immeuble INNER JOIN Rue ON Immeuble.num_rue=Rue.code_rue WHERE lettre_appartement=?",liste):
            print (ligne)

R1=Rue(1,"Bernoussi")
R2=Rue(2,"Ainsbaa")
I1=Immeuble(1,4,R1.code_rue)
I2=Immeuble(2,3,R2.code_rue)
ET1=Etage(1,5,I1.num_immeuble)
ET2=Etage(2,2,I2.num_immeuble)
APP1=Appartement(1,3,ET1.num_etage)
APP2=Appartement(2,3,ET2.num_etage)

#print(APP1)
#print(APP2)

#******************#
#R1.insert_rue()
#R2.insert_rue()
#I1.insert()
#I2.insert()
#ET1.insert()
#ET2.insert()
#APP1.insert()
#APP2.insert()

#R1.affiche()
I1.affiche()
ET1.affiche()
APP2.affiche()

#APP3=Appartement(2,5,ET1.num_etage)
#APP3.modifier()




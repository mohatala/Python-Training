from tkinter import *
import sqlite3


conn=sqlite3.connect("Institut_IBEGIS.db")


conn.execute(""" CREATE TABLE if not exists Sections(
                            Id_section INTERGER,
                            nom_section TEXT 
                            )        
     """)


conn.execute(""" CREATE TABLE if not exists Etudiants(
                            Id INTERGER PRIMARY KEY,
                            nom TEXT ,
                            email TEXT ,
                            phone TEXT ,
                            Id_section INTERGER,
                            FOREIGN KEY (Id_section) REFERENCES Sections(Id_section)
                            )
     """)


c=conn.cursor()
def Saisie_section():
    print("Entrer ID Section")
    id=int(input());
    print("Entrer Nom Section")
    nom_section=input();
    l=[id,nom_section]
    c.execute("INSERT INTO Sections VALUES (?,?)",l)
    conn.commit()

def Saisie_etudiant():
    print("Entrer ID Etudiant")
    id=int(input());
    print("Entrer Nom Etudiant")
    nom_Etudiant=input();
    print("Entrer Email Etudiant")
    email_Etudiant=input();
    print("Entrer Phone Etudiant")
    phone_Etudiant=input();
    print("Entrer Id section")
    id_sec=int(input());
    l=[id,nom_Etudiant,email_Etudiant,phone_Etudiant,id_sec]
    c.execute("INSERT INTO Etudiants VALUES (?,?,?,?,?)",l)
    conn.commit()

def Modifier_Nom(id):
    print("Entrer Nom Etudiant")
    nom_Etudiant=input();
    l=[nom_Etudiant,id]
    c.execute("UPDATE Etudiants SET nom=? WHERE Id=?",l)
    conn.commit()

def Supprimer_Nom(id):
    l=[id]
    c.execute("DELETE FROM Etudiants WHERE Id=?",l)
    conn.commit()





result=1
while int(result)>0:
    print("---------------Menu---------------")
    print("1:Saisie info Section")
    print("2:Saisie Infos Etudiant")
    print("3:Modifier Nom Etudiant")
    print("4:Supprimer un Etudiant")
    print("0:Fin du programme")
    result=input("Tapez Le nombre de l'operation que vous choisie:")
    if int(result)==1:
        Saisie_section()
    elif int(result)==2:
        Saisie_etudiant()
    elif int(result)==3:
        mat=input("Tapez ID de L'Etudiant:")
        Modifier_Nom(int(mat))
    elif int(result)==4:
        mat=input("Tapez ID de L'Etudiant:")
        Supprimer_Nom(int(mat))






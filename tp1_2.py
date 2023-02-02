import sqlite3

conn=sqlite3.connect("ibgis.db")
c=conn.cursor()
#----------------------------definir nom db avec variable---------------
#db=input("Saisir le nom de la BD")
 
#ntable=input("saisir la table")

#conn=sqlite3.connect(db)
#c.conn.cursor()
#c.execute("CREATE TABLE ?",ntable)

#-------------------Requete Sql---------------------------------------

#for ligne in  c.execute("SELECT nom,note FROM etudiant WHERE note>14"):
#    print(ligne)

#for ligne in  c.execute("SELECT * FROM etudiant WHERE nom='Alami'"):
 #   print(ligne)

#for ligne in  c.execute("SELECT nom,MAX(note) FROM etudiant"):
#    print(ligne)

#for ligne in  c.execute("SELECT nom,note FROM etudiant WHERE note>11 AND note<15"):
  #  print(ligne)

#----------------------Relation entre table-------------------------------
sql2=""" CREATE TABLE projet(
                            num_pr INTERGER PRIMARY KEY,
                            sujet TEXT NOT NULL,
                            date_pr DATE NOT NULL,
                            num INTEGER,
                            FOREIGN key(num) REFERENCES etudiant(num))
     """
#c.execute(sql2)

prj=[(1,"python","01/11/2021",12),(2,"java","02/11/2021",12),(3,"C","03/11/2021",14),(4,"cobol","05/11/2021",12)]                               
prj1=[(5,"python avance","01/11/2021",30),(6,"jee","02/11/2021",30)]                               

#c.executemany("INSERT INTO projet VALUES (?,?,?,?)",prj1)
#conn.commit()

for ligne in  c.execute("SELECT * FROM projet"):
    print(ligne)

#for ligne in  c.execute("SELECT etudiant.nom,projet.sujet,projet.date_pr FROM etudiant,projet WHERE etudiant.num=projet.num"):
 #   print(ligne)

#for ligne in  c.execute("SELECT etudiant.nom,projet.sujet,projet.date_pr FROM etudiant,projet WHERE projet.num=12 AND etudiant.num=projet.num"):
#    print(ligne)  
    

import sqlite3

conn=sqlite3.connect("ibgis.db")


c=conn.cursor()

sql1=""" CREATE TABLE etudiant(
                               num INTEGER PRIMARY KEY,
                               nom TEXT NOT NULL,
                               prenom TEXT NOT NULL,
                               note REAL )
    """
#c.execute(sql1)
 
etd=[(12,"Alami","Sara",14.5),(13,"imane","alami",11.5),(14,"imad","med",12.0),(16,"test","test",15.0)]                               
etd1=[(21,"mt","Sara",14.5),(22,"med","alami",11.5),(23,"imad","med",12.0),(24,"test","test",15.0)]                               

#c.executemany("INSERT INTO etudiant VALUES (?,?,?,?)",etd1)

# commande pour valider la requete sql 
conn.commit()
for row in c.execute("SELECT * FROM etudiant"):
    print(row)

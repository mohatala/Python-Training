import sqlite3


conn=sqlite3.connect("C:/Users/21260/Desktop/Master/Python/gestion des visites médicales/Cabinet_Medicale.db")
c=conn.cursor()
sql2="""CREATE TABLE IF NOT EXISTS USERS(
                            Id INTERGER PRIMARY KEY,
                            Username TEXT NOT NULL,
                            Password TEXT NOT NULL
                            )
     """
c.execute(sql2)

sql2="""CREATE TABLE IF NOT EXISTS MEDECIN(
                            NUM_MATRICULE INTERGER PRIMARY KEY,
                            NOM_MEDECIN TEXT NOT NULL,
                            ADR_MEDECIN TEXT NOT NULL,
                            SPECIALITE TEXT NOT NULL
                            )
     """
c.execute(sql2)

sql2="""CREATE TABLE IF NOT EXISTS PATIENT(
                            NUM_SEC_SOCIALE INTERGER PRIMARY KEY,
                            NOM_PAT TEXT NOT NULL,
                            PRENOM_PAT TEXT NOT NULL,
                            ADR_PAT TEXT NOT NULL,
                            DATE_NAISS TEXT NOT NULL
                            )
     """
c.execute(sql2)

sql2="""CREATE TABLE IF NOT EXISTS CONSULTATION(
                            NUM_SEC_SOCIALE INTERGER NOT NULL,
                            NUM_MATRICULE INTERGER NOT NULL,
                            DATE_CONS TEXT NOT NULL,
                            FOREIGN key(NUM_SEC_SOCIALE) REFERENCES PATIENT(NUM_SEC_SOCIALE)
                            FOREIGN key(NUM_MATRICULE) REFERENCES MEDECIN(NUM_MATRICULE)

                            )
     """
c.execute(sql2)
conn.commit()
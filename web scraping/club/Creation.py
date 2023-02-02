import sqlite3

cn=sqlite3.connect("MY_ClUB.db")

c=cn.cursor()

sql="""CREATE TABLE sport(
                          NOSPORT INTEGER PRIMARY KEY,
                          NOMSP TEXT NOT NULL,
                          MONTANT REEL NOT NULL
                          )
                 
                          
    
"""
#c.execute(sql)
sql1=""" CREATE TABLE adherent(
                          NOADH INTEGER PRIMARY KEY,
                          NOMADH TEXT NOT NULL,
                          PRENAGH TEXT NOT NULL,
                          NOSPORT INTEGER,
                          FOREIGN key(NOSPORT) REFERENCES sport(NOSPORT)
                          )
                          """
#c.execute(sql1)

#cn.commit()


# Rename the SQLite Table

renameTable = "ALTER TABLE sport RENAME TO activite"
#c.execute(renameTable)

 

# Query the SQLite master table
tableQuery = "select * from sqlite_master"
c.execute(tableQuery)
tableList = c.fetchall()


for table in tableList:
    print("Name of the table: "+table[2])

addColumn = "ALTER TABLE activite ADD COLUMN nature TEXT"
#c.execute(addColumn)


for row in c.execute('SELECT * FROM activite'):
    print(row)

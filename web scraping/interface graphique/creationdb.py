import sqlite3

cn=sqlite3.connect("graphique.db")
c=cn.cursor()

#c.execute("""CREATE TABLE testgraph(
                                  #  id INTEGER PRIMARY KEY,
                                   # nom TEXT NOT NULL) """)
#cn.commit()

c.execute("""INSERT INTO testgraph VALUES(1,'med') """)
cn.commit()

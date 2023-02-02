import sqlite3

cn=sqlite3.connect("MY_ClUB.db")

c=cn.cursor()


sp1=[(4,"baseball",300),(5,"FootBall",100),(6,"Natation",200)]
adh1=[(4,"Med","imad",4),(5,"chawki","yassin",2),(6,"yossra","iraki",6)]

c.executemany("INSERT INTO sport VALUES(?,?,?)",sp1)
c.executemany("INSERT INTO adherent VALUES(?,?,?,?)",adh1)

cn.commit()

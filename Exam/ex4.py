import sqlite3

conn=sqlite3.connect("examen.db")
c=conn.cursor()


sql1=""" CREATE TABLE departement(
 DNO INTEGER PRIMARY KEY,
 DNOM TEXT NOT NULL,
 VILLE TEXT NOT NULL )
 """
c.execute(sql1)

sql1=""" CREATE TABLE employe(
 ENO INTEGER PRIMARY KEY,
 ENOM TEXT NOT NULL,
 PROF TEXT NOT NULL,
 SAL TEXT NOT NULL,
 COMM TEXT NOT NULL,
 DNO INTEGER ,
 FOREIGN key(DNO) REFERENCES departement(DNO))
 """
c.execute(sql1)

conn.commit()

dep=[(1,"Informatique","CASABLANCA")]

c.executemany("INSERT INTO departement VALUES (?,?,?)",dep)
conn.commit()
c.execute("DELETE FROM employe where ENO=333")
conn.commit()

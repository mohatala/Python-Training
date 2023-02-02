from tkinter import *
import sqlite3
from tkinter.messagebox import *
from tkinter.ttk import *
conn =sqlite3.connect("C:/Users/21260/Desktop/Master/Formation Licence Web Mobile/python/interface graphique/graphique.db")
c=conn.cursor()
##########################
query = "SELECT * FROM testgraph"
c.execute(query)
result = c.fetchall()
idx=0

def importer():
    for ligne in c.execute("SELECT * FROM testgraph "):
        print (ligne)

def inser():
    liste=[(int(txt1.get()),txt2.get())]
    c.executemany("INSERT INTO testgraph VALUES (?,?)",liste)
    conn.commit()
    showinfo("message","Insert succesfuly")
def modifier():
    liste=[(txt2.get(),int(txt1.get()))]
    c.executemany("UPDATE testgraph SET nom=? WHERE id=?",liste)
    conn.commit()
    showinfo("message","Deleted succesfuly")

def firstitem():
    global idx
    idx=0
    txt1.delete(0, END)
    txt2.delete(0, END)
    txt1.insert(0,result[idx][0])
    txt2.insert(0,result[idx][1])
def lastitem():
    global idx
    idx=len(result)-1
    txt1.delete(0, END)
    txt2.delete(0, END)
    txt1.insert(0,result[idx][0])
    txt2.insert(0,result[idx][1])
def nextitem():
    global idx
    idx=idx+1
    if(idx==len(result)):
        showinfo("message","Last Row")
    else:
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt1.insert(0,result[idx][0])
        txt2.insert(0,result[idx][1])
        
def backitem():
    global idx
    idx=idx-1
    if(idx==-1):
        showinfo("message","First Row")
    else:
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt1.insert(0,result[idx][0])
        txt2.insert(0,result[idx][1])


    

    
##########################
w = Tk()
w.title("Interface")

w.geometry("350x200")
style = Style()
style.configure('W.TButton', font =
               ('calibri', 10, 'bold', 'underline'),
                foreground = 'blue')
lbl1=Label(w,text="ID")
lbl1.place(x=20,y=20)

txt1=Entry(w)
txt1.place(x=100,y=20)

lbl2=Label(w,text="Nom")
lbl2.place(x=20,y=50)

txt2=Entry(w)
txt2.place(x=100,y=50)

btn1=Button(w,text="<<",style = 'W.TButton',command=firstitem)
btn1.place(x=10,y=80)
btn2=Button(w,text="<",style = 'W.TButton',command=backitem)
btn2.place(x=90,y=80)
btn3=Button(w,text=">",style = 'W.TButton',command=nextitem)
btn3.place(x=185,y=80)
btn4=Button(w,text=">>",style = 'W.TButton',command=lastitem)
btn4.place(x=270,y=80)



insert=Button(w,text="Insert",command=inser)
insert.place(x=10,y=150)
impor=Button(w,text="Import",command=importer)
impor.place(x=90,y=150)
modif=Button(w,text="Update",command=modifier)
modif.place(x=170,y=150)
w.mainloop()





